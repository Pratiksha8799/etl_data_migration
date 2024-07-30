
# Data Migration from MySQL to BigQuery 📚

The project involves developing an ETL (Extract, Transform, Load) pipeline to migrate data from a MySQL database to a BigQuery database. This migration aims to utilize BigQuery's powerful data processing capabilities for enhanced analytics and reporting.

## Features
- Data Extraction: Extract data from various tables in the MySQL database.

- Data Transformation: Clean, transform, and format the data to ensure compatibility with BigQuery's schema and optimize for performance.

- Data Loading: Load the transformed data into BigQuery tables, ensuring data integrity and consistency.

- Automation: Schedule the ETL process to run at regular intervals, ensuring continuous and up-to-date data migration.

- Error Handling: Implement robust error handling and logging mechanisms to track and resolve issues during the ETL process.


## Prerequisites
Before you begin, ensure you have the following installed:

- Google Cloud Platform (GCP) Account:
```bash
    Access Google Cloud Console.

    BigQuery enabled in your GCP project.
``` 
- MySQL Database:
- Python Environment:
```bash
pandas

mysql.connector

Google-cloud-bigquery (for interacting with BigQuery)

```
- Scheduler:
```bash 
Task Scheduler: If you are running the ETL script on Windows.
```
- Service Account:
```bash 
A service account with appropriate permissions to access BigQuery and Google Cloud Storage.

Download the JSON key file for the service account and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the key file.
```


## Setup
- MySQL Database Setup:

    1. Ensure the MySQL database is running and accessible.

    2. Create a user with read permissions to the tables you need to extract data from.

- Google Cloud Setup:

    1. Create a new project in Google Cloud Console (if not already created).

    2. Enable BigQuery APIs.

    3. Create datasets and tables in BigQuery to match the schema of the transformed data.
    4. Create a service account with appropriate permissions to access BigQuery.
    5. Download the JSON key file for the service account and set the GOOGLE_APPLICATION_CREDENTIALS environment variable.

## Implementation Steps

* Extract: Connect to the MySQL database using a Python script and extract data from the specified tables.
* Transform: Use Pandas to clean and transform the extracted data, ensuring it adheres to the schema and performance requirements of BigQuery.
* Load: Load the transformed data directly into the corresponding BigQuery tables.
* Automate: Set up a scheduler to automate the ETL process, ensuring regular updates to the BigQuery database.
* Monitor: Implement logging and error handling to monitor the ETL process and address any issues that arise.


## Used By

- Data Analysts:

    To migrate and transform data for advanced analytics.

    Leveraging BigQuery’s querying capabilities for generating insights and reports.

- Data Engineers:

    To set up and maintain robust data pipelines.

    To ensure efficient data flow and processing between MySQL and BigQuery.

- Data Scientists:

    To prepare large datasets for machine learning models.

    To perform complex data transformations and analyses on scalable platforms.
## Future scope

* Machine Learning Integration: Use the transformed data in BigQuery for building and deploying machine learning models, driving predictive analytics.

##  Conclusion 🚀

The ETL data migration project from MySQL to BigQuery successfully establishes a robust and efficient pipeline for transferring, transforming, and loading data. By leveraging the powerful capabilities of BigQuery.
## Support

For support, email pratikshagarkar871999@gmail.com


[![Kaggle](https://img.shields.io/badge/Kaggle-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/pratikshagarkar)

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@pratiksha.garkar)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pratiksha-garkar-110a9a171/)
