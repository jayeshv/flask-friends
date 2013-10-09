
from flask import Blueprint


class FollowManager(object):

    def __init__(self, self, app=None, flask_sqlalchemy_db=None):
        self.init_app(app, flask_sqlalchemy_db)

    def init_app(self, app=None, flask_sqlalchemy_db=None):
        pass

    def add_group(self):
        follow_group = FollowGroup()
        follow_group.save()

    def drop_group(self):
        pass

    def follow(self, user1, user2, group):
        """ user1 following user2
        request initiated by user1 """

        follow = Follow()
        follow.follower = user1
        follow.following = user2
        follow.group = group
        follow.save()

    def get_followers(self, user, group):
        """ Get all users that <user> follows"""

        Follow.query.filter(follower=user)

    def get_following(self, user):
        """ Get all users following <user>"""

        Follow.query.filter(folloing=user)

    def unfollow(self, follow):
        pass


class FriendshipManager(object):

    def __init__(self, self, app=None, flask_sqlalchemy_db=None):
        self.init_app(app, flask_sqlalchemy_db)

    def init_app(self, app=None, flask_sqlalchemy_db=None):
        pass
