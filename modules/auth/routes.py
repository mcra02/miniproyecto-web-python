from modules.auth.views import (
    AuthSignInPostView,
    AuthSignUpPostView,
    AuthMeGetView
)

routes = [
    ('auth/signin', AuthSignInPostView()),
    ('auth/signup', AuthSignUpPostView()),
    ('auth/me', AuthMeGetView())
]
