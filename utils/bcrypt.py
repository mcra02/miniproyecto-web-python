import bcrypt


def b_encode(payload):
    return bcrypt.hashpw(payload.encode('utf8'), bcrypt.gensalt()).decode('utf8')


def b_compare(payload, bcrypt_encode):
    print(payload, bcrypt_encode)
    return bcrypt.checkpw(payload.encode('utf8'), bcrypt_encode.encode('utf8'))
