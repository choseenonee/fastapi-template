import os

from dotenv import load_dotenv

load_dotenv("deploy/.env")


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


DB_USER_NAME = os.getenv("DB_USER_NAME")
DB_USER_PASSWORD = os.getenv("DB_USER_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

if None in [DB_HOST, DB_PORT, DB_NAME, DB_USER_NAME, DB_USER_PASSWORD]:
    raise ValueError(".env parsing error: ", DB_HOST, DB_PORT, DB_NAME, DB_USER_NAME, DB_USER_PASSWORD)