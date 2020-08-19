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

from middleware.permissions import is_user_auth

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
    FriendPutSerializer,
    FriendDelPostSerializer
)

SCHEMA = os.getenv('REDIS_FRIENDS')
SCHEMA_ACCOUNT = os.getenv('REDIS_ACCOUNTS')
URL_PAGINATION = os.getenv('URL_PAGINATION')


class FriendGetIDView(BaseResource):
    @is_user_auth
    def on_get(self, req, res, id):
        try:
            data = findOne(SCHEMA, id=id)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendGetView(BaseResource):
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
        pagination = {
            'page': page,
            'count': limit,
            'next': next
        }
        try:
            data = find(SCHEMA, page, limit)
            self.on_success(res, to_camel_case(data), pagination)
        except Exception as e:
            print(e)
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendPostView(BaseResource):
    schema = FriendPostSerializer()

    @is_user_auth
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
    @is_user_auth
    def on_delete(self, req, res, id):
        try:
            data = delete(SCHEMA, id=id)
            self.on_success(res, to_camel_case(data))
        except Exception as e:
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})


class FriendDelPostView(BaseResource):
    schema = FriendDelPostSerializer()

    @is_user_auth
    def on_post(self, req, res):
        try:
            id = req['id']
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
    @is_user_auth
    @falcon.before(OffsetPaginationHook(
        default_limit=10,
        max_limit=10,
        offset_key='page'
    ))
    def on_get(self, req, res, account):
        limit = req.context['pagination']['limit']
        page = req.context['pagination']['offset']
        if(page == 0):
            page += 1
        next = URL_PAGINATION + req.path + '?limit=' + \
            '10' + '&page=' + \
            str(page+1)
        pagination = {
            'page': page,
            'count': limit,
            'next': next
        }
        try:
            data = findCollection(SCHEMA, page, limit,
                                  starting_account_id=account)
            self.on_success(res, to_camel_case(data), pagination)
        except Exception as e:
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class FriendsRelationView(BaseResource):
    @is_user_auth
    @falcon.before(OffsetPaginationHook(
        default_limit=10,
        max_limit=10,
        offset_key='page'
    ))
    def on_get(self, req, res, account, friend):
        limit = req.context['pagination']['limit']
        page = req.context['pagination']['offset']
        if(page == 0):
            page += 1
        next = URL_PAGINATION + req.path + '?limit=' + \
            '10' + '&page=' + \
            str(page+1)
        pagination = {
            'page': page,
            'count': limit,
            'next': next
        }
        try:
            array = []
            account_one = findCollection(SCHEMA, starting_account_id=account)
            account_two = findCollection(SCHEMA, starting_account_id=friend)
            for x in account_one:
                for y in account_two:
                    if(x['ending_account_id'] == y['ending_account_id']):
                        array.append(y)
            start = (page * 10)-10
            end = start + limit
            data = array[start:end]
            self.on_success(res, to_camel_case(data), pagination)
        except Exception as e:
            print(e)
            self.on_error(
                res, error={'code': 500, 'message': 'El servidor encontró una condición inesperada que le impidió cumplir con la solicitud.', 'status': falcon.HTTP_500})


class FriendNestedView(FriendNestedGetView):
    pass
