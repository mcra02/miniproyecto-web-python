from any_case import converts_keys


def to_camel_case(s):
    case = converts_keys(s, case='camel')
    return case


def to_snake_case(s):
    case = converts_keys(s, case='snake')
    return case
