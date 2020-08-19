from modules.friends.views import (
    FriendIDView,
    FriendView,
    FriendNestedView
)

routes = [
    ('friends/{id}', FriendIDView()),
    ('friends', FriendView()),
    ('account/{account}/friends', FriendNestedView())
]
