from modules.friends.routes import routes as friend_route
from modules.accounts.routes import routes as account_route
from modules.auth.routes import routes as auth_route
from modules.endpoints.routes import routes as endpoint_route
import os
import redis
from utils.redis_cache import (
    create,
    find
)
HOST = os.getenv('REDIS_HOST')
PORT = os.getenv('REDIS_PORT')
PASSWORD = os.getenv('REDIS_PASSWORD')


master = redis.Redis(host=HOST,
                     port=PORT, password=PASSWORD)

api_routes = [
    auth_route,
    account_route,
    friend_route,
    endpoint_route
]

SCHEMA = os.getenv('REDIS_ENDPOINTS')

endpoints = []


def register_routes(routes, app, prefix=None):
    for module in routes:
        for route in module:
            if prefix:
                url = {
                    'endpoint': str(f'/{prefix}/{route[0]}')
                }
                endpoints.append(url)
                app.add_route(f'/{prefix}/{route[0]}', route[1])
            else:
                url = {
                    'endpoint': str(f'/{route[0]}')
                }
                endpoints.append(url)
                app.add_route(f'/{route[0]}')
    master.delete(SCHEMA)
    for x in endpoints:
        create(SCHEMA, x)
