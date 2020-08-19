from marshmallow import fields, Schema, validate


class FriendPostSerializer(Schema):
    class Meta:
        strict = True

    id = fields.Integer()
    starting_account_id = fields.Integer(required=True)
    ending_account_id = fields.Integer(required=True)


class FriendPutSerializer(FriendPostSerializer):
    starting_account_id = fields.Integer()
    ending_account_id = fields.Integer()
