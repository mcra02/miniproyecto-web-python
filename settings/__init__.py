import os
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR + '/.env')

# Server
HOST = '0.0.0.0'
PORT = os.getenv('PORT')

# Secret key
SECRET_KEY = os.getenv('SECRET_KEY')

# Apps
INSTALLED_APPS = [
]

# Allowed hosts
ALLOWED_HOSTS = [
    '*'
]

DB_AUTOCOMMIT = True
BRAND_NAME = "Falcon REST API Template"
