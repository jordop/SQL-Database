import mysql.connector
from mysql.connector import Error
import pandas as pd

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

pw = FoxtrotDelta7884* # IMPORTANT! Put your MySQL Terminal password here.
db = "school" # This is the name of the database we will create in the next step - call it whatever you like.

connection = create_server_connection("localhost", "root", pw)