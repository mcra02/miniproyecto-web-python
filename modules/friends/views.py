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
    findOne,
    findCollection
)

from modules.friends.seralizer import (
    FriendPostSerializer,
    FriendPutSerializer
)

SCHEMA = os.getenv('REDIS_FRIENDS')
SCHEMA_ACCOUNT = os.getenv('REDIS_ACCOUNTS')


class FriendGetIDView(BaseResource):
    def on_get(self, req, res, id):
        try:
            data = findOne(SCHEMA, id=id)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendGetView(BaseResource):
    def on_get(self, req, res):
        try:
            data = find(SCHEMA)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            print(e)
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendPostView(BaseResource):
    schema = FriendPostSerializer()

    def on_post(self, req, res):
        try:
            req = to_snake_case(req.context['json'])
            try:
                one = findOne(SCHEMA, **req)
                if(one):
                    self.on_error(
                        res, error={'code': 404, 'message': 'Ya existe el registro!', 'status': falcon.HTTP_400})
            except Exception as e:
                try:
                    one_one = findOne(
                        SCHEMA_ACCOUNT, id=req['starting_account_id'])
                    one_two = findOne(
                        SCHEMA_ACCOUNT, id=req['starting_account_id'])
                    req['id'] = str(uuid.uuid4())
                    data = create(SCHEMA, req)
                    self.on_success(res, to_camel_case(data))
                except Exception as e:
                    self.on_error(
                        res, error={'code': 404, 'message': 'No existe alguno de los registros proveidos!', 'status': falcon.HTTP_400})
        except Exception as e:
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class FriendDeleteView(BaseResource):
    def on_delete(self, req, res, id):
        try:
            data = delete(SCHEMA, id=id)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendIDView(FriendGetIDView,
                   FriendDeleteView):
    pass


class FriendView(FriendPostView,
                 FriendGetView):
    pass


class FriendNestedGetView(BaseResource):
    def on_get(self, req, res, account):
        try:
            data = findCollection(SCHEMA, starting_account_id=account)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class FriendNestedView(FriendNestedGetView):
    pass
