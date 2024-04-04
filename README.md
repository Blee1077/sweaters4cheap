# Sweaters4Cheap - Sweater Discount Notifier

## Overview
The `sweaters4cheap` project contains a Python application designed to notify users of discounts on sweaters from the Paul James Knitwear online store. The application scrapes the product pages, checks for discounts against a set threshold, and sends out an email notification with the details of the discounted items.

## Structure
The repository is structured as follows:

- `sweater_discount_notifier/`: Contains the Python scripts for the application logic.
  - `app.py`: The main Lambda function handler that orchestrates the scraping, analysis, and notification.
  - `scraper.py`: Contains the scraping logic to retrieve product prices from the Paul James website.
  - `urls.py`: Lists the URLs of the sweater products to be monitored.
  - `requirements.txt`: Lists the dependencies to be installed.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `template.yaml`: AWS SAM template for deploying the application as a serverless function.
- `README.md`: Provides information about the project and how to set it up.

## Features
- Scrapes sweater prices from the Paul James Knitwear website.
- Determines if the price of a sweater meets the discount threshold.
- Sends an email notification with details of discounted items using a pretty HTML table.

## Configuration
Before deploying the application, update the `template.yaml` with appropriate values:
- `DiscountThreshold`: Minimum discount percentage to trigger a notification. Default is `25`.
- `EmailSecretBucket`: Name of the S3 bucket that contains the email secret JSON file.
- `EmailSecretJsonKey`: Name of the JSON file with email credentials.
- `SNSEmailParameter`: Email address for SNS topic subscription on errors.
- `Schedule`: Cron expression for the frequency of function invocation. Default is `cron(0 8 * * ? *)`.
- `FunctionTimeout`: The number of seconds for the function to execute before it is terminated. Default is `600` seconds.
- `FunctionMemorySize`: The amount of memory allocated for the function. Default is `275` MB.

## Prerequisites
Ensure you have the following configured:
- AWS CLI with appropriate permissions.
- An S3 bucket with your email secrets in a JSON file.
- Python 3.9 or later.

## Deployment
To deploy the function using the AWS SAM CLI, run:
```sh
sam build
sam deploy --guided
```

## Usage
Once deployed, the Lambda function will run according to the schedule set in the template.yaml file. When a discount threshold is met or exceeded, an email notification will be sent.