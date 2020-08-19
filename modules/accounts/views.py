import os
import falcon
import json

from base.api import BaseResource

from utils.convert_case import (
    to_camel_case,
    to_snake_case
)

from utils.redis_cache import (
    create,
    delete,
    update,
    find,
    findOne
)

from modules.accounts.serializer import (
    AccountsPostSerializer,
    AccountPutSerializer
)

SCHEMA = os.getenv('REDIS_ACCOUNTS')


class AccountsGetIDView(BaseResource):
    def on_get(self, req, res, id):
        data = findOne(SCHEMA, id=id)
        if(len(data.keys()) > 0):
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        else:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountGetView(BaseResource):
    def on_get(self, req, res):
        data = find(SCHEMA)
        for x in data:
            x['friend_collection_url'] = os.getenv(
                'URL_WEB') + x['friend_collection_url']
        self.on_success(res, to_camel_case(data))


class AccountPostView(BaseResource):
    schema = AccountsPostSerializer()

    def on_post(self, req, res):
        req = to_snake_case(req.context['json'])
        alldata = find(SCHEMA)
        index = str(len(alldata))
        req['id'] = index
        req['friend_collection_url'] = '/' + index + '/friends'
        data = create(SCHEMA, req)
        data['friend_collection_url'] = os.getenv(
            'URL_WEB') + '/' + index + '/friends'
        self.on_success(res, to_camel_case(data))


class AccountPutView(BaseResource):

    schema = AccountPutSerializer()

    def on_put(self, req, res, id):
        req = to_snake_case(req.context['json'])
        one = findOne(SCHEMA, id=id)
        if(len(one.keys()) > 0):
            data = update(SCHEMA, req, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        else:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountDeleteView(BaseResource):
    def on_delete(self, req, res, id):
        data = delete(SCHEMA, id=id)
        if(len(data.keys()) > 0):
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + '/' + id + '/friends'
            self.on_success(res, to_camel_case(data))
        else:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class AccountIDView(AccountsGetIDView,
                    AccountDeleteView,
                    AccountPutView):
    pass


class AccountView(AccountPostView,
                  AccountGetView):
    pass
