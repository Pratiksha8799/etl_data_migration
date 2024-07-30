# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:16:43 2024

@author: pr@t!ksha
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

def db_connection():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='*****',          # Replace with your MySQL server host
            user='*****',      # Replace with your MySQL username
            password='********',  # Replace with your MySQL password
            database='*****'     # Replace with your database name
        )
        
        if connection.is_connected():
            print("Connected to MySQL Server")
        return connection
    except Error as e:
        print(f"Error: {e}")
        
def insert_data(conn):
    df = pd.read_csv('movies.csv')
    cursor = conn.cursor()
    data = df.values.tolist()
    
    sql = """
    INSERT INTO <table_name> (Columns_names) VALUES (Values) 
    ON DUPLICATE KEY UPDATE Title = VALUES(Title), Director = VALUES(Director), Genre = VALUES(Genre), 
    Release_Date = VALUES(Release_Date), Duration = VALUES(Duration), Rating = VALUES(Rating)
    """   # Some examples of columns
    # Execute the INSERT statement for each row of data
    for row in data:
        try:
            cursor.execute(sql, tuple(row))
        except Exception as e:
            print('Error while inserting.: ',e)
    
    # Commit the changes to the database
    conn.commit()
    cursor.close()
    print("Data inserted successfully.")

    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed.")
            


if '__name__' == '__main__':
    conn = db_connection()
    insert_data(conn)
    
