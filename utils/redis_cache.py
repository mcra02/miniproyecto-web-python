import os
import redis
import json
from datetime import datetime

HOST = os.getenv('REDIS_HOST')
PORT = os.getenv('REDIS_PORT')
PASSWORD = os.getenv('REDIS_PASSWORD')

master = redis.Redis(host=HOST,
                     port=PORT, password=PASSWORD)


def find(schema):
    try:
        data = master.lrange(schema, 0, -1)
        return list(json.loads(x) for x in data)
    except Exception as e:
        raise Exception(e)


def findOne(schema, **kwargs):
    try:
        all = find(schema=schema)
        data = {}
        for x in all:
            for key in kwargs.keys():
                data = x if(x[key] == kwargs[key]) else data
        if (len(data.keys()) > 0):
            return data
        else:
            raise Exception('No de encontro ningun registro')
    except Exception as e:
        raise Exception(e)


def findIndex(schema, **kwargs):
    try:
        all = find(schema=schema)
        one = findOne(schema, **kwargs)
        index = all.index(one)
        return index
    except Exception as e:
        raise Exception(e)


def create(schema, object_payload):
    try:
        object_payload['created'] = str(datetime.now())
        object_payload['updated'] = ''
        new_payload = json.dumps(object_payload)
        master.lpush(schema, new_payload)
        return object_payload
    except Exception as e:
        raise Exception(e)


def update(schema, data, **kwargs):
    try:
        obj = findOne(schema, **kwargs)
        index = findIndex(schema, **kwargs)
        obj.update(data)
        obj['updated'] = str(datetime.now())
        master.lset(schema, index, json.dumps(obj))
        return obj
    except Exception as e:
        raise Exception(e)


def delete(schema, **kwargs):
    try:
        obj = findOne(schema, **kwargs)
        master.lrem(schema, 1, json.dumps(obj))
        return obj
    except Exception as e:
        raise Exception(e)


# user = {
#     'name': 'juan',
#     'age': '50'
# }

# print(create('USERS', user))
# print(findOne('USERS', name='maicol'))
# print(update('USERS', {'age': '20'}, name='maicol'))
# print(delete('USERS', name='maicol'))
