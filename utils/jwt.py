import os
import jwt


secret_key = os.getenv('JWT_SECRET_KEY')
algorithm = 'HS256'


def jwt_encode(payload):
    return jwt.encode(payload=payload, key=secret_key, algorithm=algorithm).decode('utf8')


def jwt_decode(payload):
    encode = payload.split(" ")
    try:
        return jwt.decode(jwt=encode[1], key=secret_key, algorithms=[algorithm])
    except Exception as e:
        raise Exception('Error')
