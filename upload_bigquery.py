# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:00:11 2024

@author: pr@t!ksha
"""

import mysql.connector
from google.cloud import bigquery
import pandas as pd
import os

# Set the environment variable (for testing purposes)
a=os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<your_file_path.json>"

def fetch_data_from_mysql():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='*****',          # Replace with your MySQL server host
            user='*****',      # Replace with your MySQL username
            password='*****',  # Replace with your MySQL password
            database='*****'     # Replace with your database name
        )
        
        query = "SELECT * FROM <table_name>"  # Replace with your SQL query
        df = pd.read_sql(query, conn)
        
        conn.close()
        return df
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def upload_to_bigquery(df):
    try:
        client = bigquery.Client()  # Create a BigQuery client
        
        dataset_id = '*****'  # Replace with your dataset ID
        table_id = '*****'  # Replace with your table ID
        
        # Load DataFrame to BigQuery
        job = client.load_table_from_dataframe(df, f"{dataset_id}.{table_id}")
        
        job.result()  # Wait for the job to complete
        
        print(f"Data loaded to BigQuery table {table_id} successfully.")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    df = fetch_data_from_mysql()
    df = df.rename(columns={'Release_Date': 'Release Date'})
    if df is not None:
        upload_to_bigquery(df)

if __name__ == "__main__":
    main()
