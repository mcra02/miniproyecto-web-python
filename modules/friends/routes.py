from modules.friends.views import (
    FriendIDView,
    FriendView,
    FriendNestedView,
    # Friend optionals routes
    FriendPostView,
    FriendDelPostView
)

routes = [
    ('friends/{id}', FriendIDView()),
    ('friends', FriendView()),
    ('account/{account}/friends', FriendNestedView()),
    # Friend optonal routes
    ('add_friend', FriendPostView()),
    ('remove_friend', FriendDelPostView())
]
