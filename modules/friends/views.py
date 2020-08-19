import os
import falcon
import json
import uuid

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

from modules.friends.seralizer import (
    FriendPostSerializer,
    FriendPutSerializer
)

SCHEMA = os.getenv('REDIS_FRIENDS')


class FriendGetIDView(BaseResource):
    def on_get(self, req, res, id):
        try:
            data = findOne(SCHEMA, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendGetView(BaseResource):
    def on_get(self, req, res):
        try:
            data = find(SCHEMA)
            for x in data:
                x['friend_collection_url'] = os.getenv(
                    'URL_WEB') + x['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendPostView(BaseResource):
    schema = AccountsPostSerializer()

    def on_post(self, req, res):
        req = to_snake_case(req.context['json'])
        req['id'] = uuid.uuid4()
        data = create(SCHEMA, req)
        self.on_success(res, to_camel_case(data))


class FriendPutView(BaseResource):

    schema = AccountPutSerializer()

    def on_put(self, req, res, id):
        try:
            req = to_snake_case(req.context['json'])
            data = update(SCHEMA, req, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + data['friend_collection_url']
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendDeleteView(BaseResource):
    def on_delete(self, req, res, id):
        try:
            data = delete(SCHEMA, id=id)
            data['friend_collection_url'] = os.getenv(
                'URL_WEB') + '/' + id + '/friends'
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendIDView(FriendGetIDView,
                   FriendDeleteView,
                   FriendPutView):
    pass


class FriendView(FriendPostView,
                 FriendGetView):
    pass
