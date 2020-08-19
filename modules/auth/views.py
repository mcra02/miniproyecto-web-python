import os
import falcon
import json
import bcrypt

from base.api import BaseResource
from utils.errors import PasswordNotMatch, UsernameNotAvailable, UserNotExistsError
from utils.jwt import (
    jwt_encode,
    jwt_decode
)
from utils.bcrypt import (
    b_encode,
    b_compare
)

from utils.convert_case import (
    to_camel_case,
    to_snake_case
)

from middleware.permissions import is_user_auth

from utils.redis_cache import (
    find,
    findOne,
    create,
    update,
    delete
)


from modules.auth.serializer import (
    AuthSignUpSerilzer,
    AuthSignInSerializer
)

SCHEMA = os.getenv('REDIS_USERS')


class AuthSignUpPostView(BaseResource):

    schema = AuthSignUpSerilzer()

    def on_post(self, req, res):
        req = to_snake_case(req.context['json'])
        req['permissions'] = []
        if(req['password'] != req['password_confirmation']):
            raise PasswordNotMatch(
                description='Password and passwordConfirmation don\'t match!')
        del req['password_confirmation']
        username_length = 0
        try:
            user_exists = findOne(SCHEMA, username=req['username'])
            username_length = len(user_exists['username'])
            if(username_length > 0):
                raise UsernameNotAvailable(
                    description='Username is not available')
        except Exception as e:
            if(username_length > 0):
                raise UsernameNotAvailable(
                    description='Username is not available')
            try:
                req['password'] = b_encode(req['password'])
                user = create(SCHEMA, req)
                del user['password']
                token = jwt_encode(user)
                data = {
                    'apikey': token,
                    'user': user
                }
                self.on_success(res, to_camel_case(data))
            except Exception as e:
                self.on_error(
                    res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class AuthSignInPostView(BaseResource):

    schema = AuthSignInSerializer()

    def on_post(self, req, res):
        req = to_snake_case(req.context['json'])
        try:
            user = findOne(SCHEMA, username=req['username'])
        except Exception as e:
            raise UserNotExistsError(
                description='User or password is not available')
        if(b_compare(req['password'], user['password']) is False):
            raise UserNotExistsError(
                description='User or password is not available')
        try:
            del user['password']
            token = jwt_encode(user)
            data = {
                'apikey': token,
                'user': user
            }
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class AuthMeGetView(BaseResource):
    @is_user_auth
    def on_get(self, req, res):
        try:
            token = req.headers.get('AUTHORIZATION', None)
            encode = token.split(' ')
            userpayload = jwt_decode(token)
            data = {
                'apikey': encode[1],
                'user': userpayload
            }
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})
