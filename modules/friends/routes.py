from modules.friends.views import (
    FriendIDView,
    FriendView,
    FriendNestedView,
    FriendsRelationView,
    # Friend optionals routes
    FriendPostView,
    FriendDelPostView
)

routes = [
    ('friends/{id}', FriendIDView()),
    ('friends', FriendView()),
    ('account/{account}/friends', FriendNestedView()),
    ('account/{account}/mutualfriends/{friend}',
     FriendsRelationView()),
    # Friend optonal routes
    ('add_friend', FriendPostView()),
    ('remove_friend', FriendDelPostView())
]
