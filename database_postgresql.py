# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:43:34 2024

@author: user
"""
############################################## PostgreSQL ##############################################

import psycopg2
import pandas as pd

def db_connection_post():
    try:
        conn = psycopg2.connect(
        host='********',
        port='********',              
        database='********',     
        user='********',
        password='********'         
        )
      
        return conn
    except Exception as e:
        print(f"Error: {e}")
        
def insert_data(conn):
    df = pd.read_csv('movies.csv')
    cursor = conn.cursor()
    data = df.values.tolist()
    
    sql = """
    INSERT INTO <your_table_name> (Title, Director, Genre, Release_Date, Duration, Rating) 
    VALUES (%s, %s, %s, %s, %s, %s) 
    """
    # ON CONFLICT (ID) DO NOTHING postgreSQl db

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

     # Check if the connection is still open
    if conn.closed == 0:
        conn.close()
        print("Connection close.")
   
       
      
if __name__ == '__main__':
    conn = db_connection_post()
    insert_data(conn)
    

