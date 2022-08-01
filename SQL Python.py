import mysql.connector
from mysql.connector import Error
import pandas as pd
# The following creates the connection to the MySQL database Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

pw = "FoxtrotDelta7884*" # Put your MySQL ROOT Terminal password above, MAKE SURE IT IS MYSQL ROOT PASSWORD.
db = "school" # This is the name of the database you'd like to create

connection = create_server_connection("localhost", "root", pw)

# The following creates the database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)