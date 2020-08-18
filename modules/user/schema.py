from marshmallow import fields, Schema, validate

from base.schema import BaseSchema


class User(BaseSchema):
    class Meta:
        strict = True

    username = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
    password = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
    permisions = fields.List(fields.String())
