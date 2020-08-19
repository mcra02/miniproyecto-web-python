from modules.auth.routes import routes as auth_route
from modules.accounts.routes import routes as account_route
from modules.friends.routes import routes as friend_route

api_routes = [
    auth_route,
    account_route,
    friend_route
]


def register_routes(routes, app, prefix=None):
    for module in routes:
        for route in module:
            if prefix:
                app.add_route(f'/{prefix}/{route[0]}', route[1])
            else:
                app.add_route(f'/{route[0]}', route[1])
