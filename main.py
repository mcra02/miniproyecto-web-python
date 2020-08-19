import falcon

from falcon_cors import CORS

import settings
from routes import (
    api_routes,
    register_routes
)

from utils.errors import AppError
from falcon_marshmallow import Marshmallow


def create_app():
    cors = CORS(allow_origins_list=settings.ALLOWED_HOSTS)

    middlewares = [
        cors.middleware,
        Marshmallow(),
    ]

    app = falcon.API(middleware=middlewares)
    app.req_options.auto_parse_form_urlencoded = True
    app.add_error_handler(AppError, AppError.handle)
    register_routes(api_routes, app, prefix='api/v1.0')

    return app


app = application = create_app()
