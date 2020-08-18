from modules.auth.routes import routes as auth_route

api_routes = [
    auth_route
]


def register_routes(routes, app, prefix=None):
    for module in routes:
        for route in module:
            if prefix:
                app.add_route(f'/{prefix}/{route[0]}', route[1])
            else:
                app.add_route(f'/{route[0]}', route[1])