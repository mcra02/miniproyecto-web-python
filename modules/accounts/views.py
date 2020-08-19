import os
import falcon
import json
import uuid

from base.api import BaseResource

from falcon_pagination.offset_pagination_hook import OffsetPaginationHook

from utils.convert_case import (
    to_camel_case,
    to_snake_case
)

from utils.redis_cache import (
    create,
    delete,
    update,
    find,
    findOne,
)

from middleware.permissions import is_user_auth

from modules.accounts.serializer import (
    AccountsPostSerializer,
    AccountPutSerializer
)

SCHEMA = os.getenv('REDIS_ACCOUNTS')
SCHEMA_USERS = os.getenv('REDIS_USERS')
URL_PAGINATION = os.getenv('URL_PAGINATION')


class AccountsGetIDView(BaseResource):
    @is_user_auth
    def on_get(self, req, res, id):
        try:
            data = findOne(SCHEMA, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountGetView(BaseResource):
    @is_user_auth
    @falcon.before(OffsetPaginationHook(
        default_limit=10,
        max_limit=10,
        offset_key='page'
    ))
    def on_get(self, req, res):
        limit = req.context['pagination']['limit']
        page = req.context['pagination']['offset']
        if(page == 0):
            page += 1
        next = URL_PAGINATION + req.path + '?limit=' + \
            '10' + '&page=' + \
            str(page+1)
        try:
            data = find(SCHEMA, page, limit)
            pagination = {
                'page': page,
                'count': limit,
                'next': next
            }
            for x in data:
                x['friend_collection_url'] = os.getenv(
                    'URL_WEB') + x['friend_collection_url']
            self.on_success(res, to_camel_case(data), pagination)
        except Exception as e:
            print(e)
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountPostView(BaseResource):
    schema = AccountsPostSerializer()

    @is_user_auth
    def on_post(self, req, res):
        req = to_snake_case(req.context['json'])
        try:
            username = req['user']
            try:
                user = findOne(SCHEMA_USERS, username=username)
                try:
                    req['id'] = str(uuid.uuid4())
                    req['friend_collection_url'] = '/account/' + \
                        req['id'] + '/friends'
                    data = create(SCHEMA, req)
                    data['friend_collection_url'] = os.getenv(
                        'URL_WEB') + data['friend_collection_url']
                    self.on_success(res, to_camel_case(data))
                except Exception as e:
                    self.on_error(
                        res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})
            except Exception as e:
                self.on_error(
                    res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})
        except Exception as e:
            try:
                req['id'] = str(uuid.uuid4())
                req['user'] = ''
                index = req['id']
                req['friend_collection_url'] = '/account/' + index + '/friends'
                data = create(SCHEMA, req)
                data['friend_collection_url'] = os.getenv(
                    'URL_WEB') + data['friend_collection_url']
                self.on_success(res, to_camel_case(data))
            except Exception as e:
                self.on_error(
                    res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountPutView(BaseResource):

    schema = AccountPutSerializer()

    @is_user_auth
    def on_put(self, req, res, id):
        req = to_snake_case(req.context['json'])
        try:
            username = req['user']
            try:
                user = findOne(SCHEMA_USERS, username=username)
                try:
                    data = update(SCHEMA, req, id=id)
                    data['friend_collection_url'] = os.getenv(
                        'URL_WEB') + data['friend_collection_url']
                    self.on_success(res, to_camel_case(data))
                except Exception as e:
                    self.on_error(
                        res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})
            except Exception as e:
                self.on_error(
                    res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})
        except Exception as e:
            try:
                req['user'] = ''
                data = update(SCHEMA, req, id=id)
                data['friend_collection_url'] = os.getenv(
                    'URL_WEB') + data['friend_collection_url']
                self.on_success(res, to_camel_case(data))
            except Exception as e:
                self.on_error(
                    res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountDeleteView(BaseResource):
    @is_user_auth
    def on_delete(self, req, res, id):
        try:
            data = delete(SCHEMA, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountIDView(AccountsGetIDView,
                    AccountDeleteView,
                    AccountPutView):
    pass


class AccountView(AccountPostView,
                  AccountGetView):
    pass
