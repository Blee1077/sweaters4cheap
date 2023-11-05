import re
import os
import json
import boto3
import logging
import pandas as pd
from redmail import EmailSender
from pretty_html_table import build_table
from scraper import get_product_price_paul_james
from urls import PROD_URL_DICT

# Set up logging
logger = logging.getLogger('sweater-discount-notifier')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

s3 = boto3.resource('s3')

def load_json(bucket: str, key: str):
    """Loads a JSON file from S3.
    
    Args:
        bucket(str): S3 bucket name
        key (str): S3 key of JSON file
        
    Returns:
        dict
    """
    content_object = s3.Object(bucket, key)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    return json.loads(file_content)


def lambda_handler(event, context):
    # Scrape product details
    results = []
    for url in PROD_URL_DICT.get('paul_james'):
        results.append(get_product_price_paul_james(url))
    
    # Filter results for those with sales
    filt_res = [prod for prod in results if prod]
    df = pd.DataFrame.from_records(filt_res)
    logger.info(f"{len(df)} items are currently on sale.")

    if len(df) > 0:
        html = """
        <html>
            <head></head>
            <body>
            Sweaters just got a whole lot cheaper, check out the deals below!
            {0}
            </body>
        </html>
        """.format(
            build_table(
                df.sort_values(by='Sale Price', ascending=False),
                'blue_light'
            )
        )

        # Make links clickable in the html
        urls = re.findall(r'(?=https://).*.html', html)
        for url in urls:
            html = html.replace(url, f'<a href={url}>{url}</a>')
            
        # Put thumbnails into the html
        img_urls = re.findall(r'(?=www.).*.jpg', html)
        for img_url in img_urls:
            html = html.replace(img_url, f'<img src="https://{img_url}" alt="" width="135" height="200">')

        # Set up email
        email_secret = load_json(os.environ['EMAIL_SECRET_BUCKET'], os.environ['EMAIL_SECRET_JSON_KEY'])
        email = EmailSender(
                host=email_secret['host'],
                port=email_secret['port'],
                username=email_secret['sender_email'],
                password=email_secret['password']
            )

        # Send email
        email.send(
            subject="Paul James Knitwear has discounts on their sweaters!",
            sender=email_secret['sender_email'],
            receivers=[email_secret['receiver_email']],
            html=html
        )
        logger.info("Successfully sent email with items on sale.")
        
        return True
    
    else:
        logger.info("No items are currently on sale, no email to send.")
        return True
