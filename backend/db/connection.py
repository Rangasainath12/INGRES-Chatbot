# db_connector.py

import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """Establishes a connection to the MySQL database.
    
    Returns:
        MySQLConnection object if connection is successful, else None.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Your MySQL host
            database='water_data_db',  # The name of your database
            user='root',      # Replace with your MySQL username
            password='password' #password 
        )
        if connection.is_connected():
            print("✅ Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None

def execute_query(connection, query, fetch=True):
    """Executes a SQL query on the given connection.
    
    Args:
        connection (MySQLConnection): The active database connection.
        query (str): The SQL query string to execute.
        fetch (bool): True to fetch results (for SELECT queries), False otherwise.

    Returns:
        A list of dictionaries for SELECT queries, or None for others.
    """
    if not connection or not connection.is_connected():
        print("❌ Database connection is not active.")
        return None

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        if fetch:
            results = cursor.fetchall()
            return results
        else:
            connection.commit()
            print("Query executed successfully.")
            return None
    except Error as e:
        print(f"❌ An error occurred during query execution: {e}")
        return None
    finally:
        cursor.close()
