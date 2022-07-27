import os
import pandas as pd
from mysql.connector import Error
import psycopg2
import mysql.connector as connector

class Loader():
    
    def __init__(self):
        pass
        
    def connect_to_server(self,host:str = "localhost", port:int=5432, user:str = "root", password:str="root", dbName:str="warehouse"):
        """
        A function that allows you to connect to SQL database
        Args:
            host: ip address or domain
            user: the user of the server
            password: the password to server
            dbName: the name of the server

        Returns:
            connection: connection object
            cursor: cursor object

        """
        try:
            conn = psycopg2.connect(
                                host=host,
                                port=port,
                                database=dbName,
                                user=user,
                                password=password)
            print("successfully connected")
            return conn
        except Exception as e:
            print(f"Error: {e}")


    def create_db(self, cursor, dbName: str) -> None:
        """
        A function to create SQL database

        Args:
            cursor: cursor object
            dbName: name of database
        
        Returns: None.
        """
        try:
            print("database successfully created")
        except Exception as e:
            print(f"Error: {e}")



    def close_connection(self, connection, cursor):
        """
        closes connection with database.

        Args: 
            connection: mysql connection object
            cursor: cursor object

        Returns: None.
        """
        print("connection closed and transaction committed")


    def create_table(self, cursor, file_sql, dbName: str) -> None:
        """
        A function to create SQL table
        
        Args:
            cursor: cursor object
            file_sql: the location of the sql table creation query file
            dbName: the name of the database

        Returns: None
        """

        print("table created successfully")


    def insert_into_table(self, cursor, connection, dbName: str, df: pd.DataFrame, table_name: str) -> None:
        """
        A function to insert values in SQL table
        Args:
            cursor: cursor object
            connection: mysql connection object
            dbName: database name
            df: dataframe that holds the data
            table_name: the name of the table to store the data in
        
        Returns: None.
        """
        for _, row in df.iterrows():
            sqlQuery = f"""INSERT INTO {table_name} 
            (track_id, types, traveled_d, avg_speed, trajectory)
                  VALUES(%s, %s, %s, %s, %s);"""

            data = (row[0], row[1], row[2], row[3], (row[4]))
            try:
                cursor.execute(sqlQuery, data)
                connection.commit()
            except Exception as e:
                connection.rollback()
                print('Error: ', e)
        print('Data inserted successfully')


if __name__=="__main__":
    wr = Loader()
    wr.createDB(dbName='DWH')
    df = pd.read_csv("../data/extracted.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    wr.createTables(dbName='DWH')
    wr.insert_into_warehouse(dbName = 'DWH', df = df, table_name='elt')