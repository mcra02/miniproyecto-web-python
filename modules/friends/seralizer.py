from marshmallow import fields, Schema, validate


class FriendPostSerializer(Schema):
    class Meta:
        strict = True

    startingAccountId = fields.String(required=True)
    endingAccountId = fields.String(required=True)


class FriendPutSerializer(FriendPostSerializer):
    starting_account_id = fields.Integer()
    ending_account_id = fields.Integer()


class FriendDelPostSerializer(Schema):
    id = fields.String(required=True)
