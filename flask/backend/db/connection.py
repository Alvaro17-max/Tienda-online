from mysql.connector import connect, Error
from dotenv import load_dotenv
import os   

load_dotenv()

def get_db_connection():
    try:
        connection = connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None