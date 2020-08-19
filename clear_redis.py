import os
import redis
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')

HOST = os.getenv('REDIS_HOST')
PORT = os.getenv('REDIS_PORT')
PASSWORD = os.getenv('REDIS_PASSWORD')


master = redis.Redis(host=HOST,
                     port=PORT, password=PASSWORD)


def clear_cache():
    try:
        master.delete(os.getenv('REDIS_USERS'))
        master.delete(os.getenv('REDIS_ACCOUNTS'))
        master.delete(os.getenv('REDIS_FRIENDS'))
        master.delete(os.getenv('REDIS_ENDPOINTS'))
        print('Cache limpiado correctamente')
    except Exception as e:
        raise Exception('Error al limpiar la cache')


clear_cache()
