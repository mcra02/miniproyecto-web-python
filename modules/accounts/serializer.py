from marshmallow import fields, Schema, validate


class AccountsPostSerializer(Schema):
    class Meta:
        strict = True

    user = fields.String()
    name = fields.String(
        required=True, validate=validate.Length(min=4, max=50))


class AccountPutSerializer(AccountsPostSerializer):
    name = fields.String()
