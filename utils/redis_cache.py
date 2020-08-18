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
    data = master.lrange(schema, 0, -1)
    return list(json.loads(x) for x in data)


def findOne(schema, **kwargs):
    all = find(schema=schema)
    data = {}
    for x in all:
        for key in kwargs.keys():
            data = x if(x[key] == kwargs[key]) else data
    return data


def findIndex(schema, **kwargs):
    all = find(schema=schema)
    one = findOne(schema, **kwargs)
    index = all.index(one)
    return index


def create(schema, object_payload):
    object_payload['created'] = str(datetime.now())
    object_payload['updated'] = ''
    new_payload = json.dumps(object_payload)
    master.lpush(schema, new_payload)
    return object_payload


def update(schema, data, **kwargs):
    obj = findOne(schema, **kwargs)
    index = findIndex(schema, **kwargs)
    obj.update(data)
    obj['updated'] = str(datetime.now())
    master.lset(schema, index, json.dumps(obj))
    return obj


def delete(schema, **kwargs):
    obj = findOne(schema, **kwargs)
    master.lrem(schema, 1, json.dumps(obj))
    return obj


# user = {
#     'name': 'juan',
#     'age': '50'
# }

# print(create('USERS', user))
# print(findOne('USERS', name='maicol'))
# print(update('USERS', {'age': '20'}, name='maicol'))
# print(delete('USERS', name='maicol'))
