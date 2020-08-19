import falcon
import json
import os

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

from utils.alchemy import new_alchemy_encoder
from settings import BRAND_NAME
from utils.errors import NotSupportedError


class BaseResource(object):
    HELLO_WORLD = {
        "server": "%s" % BRAND_NAME,
    }

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def from_db_to_json(self, db):
        return json.dumps(db, cls=new_alchemy_encoder())

    def on_error(self, res, error=None):
        res.status = error["status"]
        meta = OrderedDict()
        meta["code"] = error["code"]
        meta["message"] = error["message"]

        obj = OrderedDict()
        obj["meta"] = meta
        res.body = self.to_json(obj)

    def on_success(self, res, data=None, pagination={}):
        res.status = falcon.HTTP_200
        meta = OrderedDict()
        meta["code"] = 200
        meta["message"] = "OK"

        obj = OrderedDict()
        obj["meta"] = meta
        obj["data"] = data
        obj["pagination"] = pagination
        res.body = self.to_json(obj)

    def on_get(self, req, res):
        if req.path == "/":
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.HELLO_WORLD)
        else:
            raise NotSupportedError(method="GET", url=req.path)

    def on_post(self, req, res):
        raise NotSupportedError(method="POST", url=req.path)

    def on_put(self, req, res):
        raise NotSupportedError(method="PUT", url=req.path)

    def on_delete(self, req, res):
        raise NotSupportedError(method="DELETE", url=req.path)
