from modules.accounts.views import (
    AccountIDView,
    AccountView
)

routes = [
    ('accounts/{id}', AccountIDView()),
    ('accounts', AccountView())
]
