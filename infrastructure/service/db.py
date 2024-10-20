import os

from dotenv import load_dotenv
from peewee import MySQLDatabase

load_dotenv()

def get_database():
    return MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
    )
