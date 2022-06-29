import os
from dotenv import load_dotenv


load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE = os.getenv('POSTGRES_DATABASE')
HOST = os.getenv('POSTGRES_SERVER')

REDIS_SERVER = os.getenv('REDIS_SERVER')

POSTGRES_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

REDIS_DATABASE_URL = f"redis://{REDIS_SERVER}"
