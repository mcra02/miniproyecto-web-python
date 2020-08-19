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
    find
)

SCHEMA = os.getenv('REDIS_ENDPOINTS')
URL_PAGINATION = os.getenv('URL_PAGINATION')


class EndpointsGetView(BaseResource):
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
            self.on_success(res, to_camel_case(data), pagination)
        except Exception as e:
            print(e)
            self.on_error(
                res, error={'code': 404, 'message': 'No se encontro ningun registro!', 'status': falcon.HTTP_400})
