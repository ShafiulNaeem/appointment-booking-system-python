import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT")
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
            )
            if conn.is_connected():
                print("Connected to the database")
                self.cursor = conn.cursor(dictionary=True)
                self.conn = conn
            else:
                print("Failed to connect to the database")
            return self.conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None



