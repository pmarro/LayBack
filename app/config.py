from dotenv import load_dotenv
from os import environ


load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)

ELEMENTS_PER_PAGE = 2

SECRET_KEY = environ.get('SECRET_KEY')