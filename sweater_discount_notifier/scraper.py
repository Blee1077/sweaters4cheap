import requests
from bs4 import BeautifulSoup

def get_product_price_paul_james(url: str):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the element that contains the price
    # Note: The class or id used here might change, you need to inspect the website to get the correct one
    product_name_element = soup.find('h1', class_='h2 product-single__title')
    product_sku_element = soup.find('p', class_='product-single__sku')
    full_price_element = soup.find('span', class_='product__price')
    sale_price_element = soup.find('span', class_='product__price on-sale')
    saving_element = soup.find('span', class_='product__price-savings')
    img_url = soup.find('div', class_='image-wrap').find('img')['data-photoswipe-src'][2:]
    img_url = img_url[:img_url.find('?')]

    if full_price_element is None:
        raise ValueError("Website has changed, reconfigure script.")
    
    if sale_price_element:
        element_dict = {
            "URL": url + ".html",
            "Product Name": product_name_element.get_text().strip(),
            "Product SKU": product_sku_element.get_text().strip(),
            "Image": img_url,
            "Full Price": float(full_price_element.get_text().strip().strip("£")),
            "Sale Price": float(sale_price_element.get_text().strip().strip("£")),
            "Savings": saving_element.get_text().strip()
        }
        
        return element_dict
    else:
        return False