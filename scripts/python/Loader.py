import os
import pandas as pd
import psycopg2

class Loader():
    
    def __init__(self):
        pass
        
    def connect_to_server(self,host:str = "localhost", port:int=5432, user:str = "warehouse", password:str="warehouse", dbName:str="warehouse"):
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
            cur = conn.cursor()
            print("successfully connected")
            return conn, cur
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
        sqlFile = file_sql
        fd = open(sqlFile, 'r')
        readsqlFile = fd.read()
        fd.close()
        sqlCommands = readsqlFile.split(';')
        for command in sqlCommands:
            try:
                result = cursor.execute(command)
                print(f"table created successfully")
            except Exception as e:
                print('command skipped: ', command)
                print(e)
        


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
    pass