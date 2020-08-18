from marshmallow import fields, Schema, validate


class AuthSignUpSerilzer(Schema):
    class Meta:
        strict = True

    username = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
    password = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
    passwordConfirmation = fields.String(
        required=True, validate=validate.Length(min=4, max=12))


class AuthSignInSerializer(Schema):
    class Meta:
        strict = True

    username = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
    password = fields.String(
        required=True, validate=validate.Length(min=4, max=12))
