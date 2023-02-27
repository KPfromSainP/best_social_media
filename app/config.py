import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()
if sys.version_info >= (3, 11):
    print(1)
print(sys.version_info)
# application config
APP_HOST = getenv('APP_HOST')
APP_PORT = getenv('APP_PORT')
SECRET_K = getenv('SECRET_K')

# database config
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_USER = getenv('DB_USER')
DB_PSWD = getenv('DB_PSWD')
DB_NAME = getenv('DB_NAME')
