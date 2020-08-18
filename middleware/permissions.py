import os
import falcon

import settings as settings
from utils.errors import UnauthorizedError
from utils.jwt import jwt_decode
from utils.redis_cache import findOne

SCHEMA = os.getenv('REDIS_USERS')


def is_user_auth(funcion_a):
    def funcion_HTTP(self, req, res):
        token = req.headers.get('AUTHORIZATION', None)

        try:
            userpayload = jwt_decode(token)
            user = findOne(SCHEMA, username=userpayload['username'])

            if(len(user.keys()) == 0):
                raise UnauthorizedError(description='Acceso no autorizado!')

        except Exception as e:
            raise UnauthorizedError(description='Invalid token')

        result = funcion_a(self, req, res)

        return result

    return funcion_HTTP
