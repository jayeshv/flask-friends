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
        """ Drop the follow object"""

        pass


class FriendshipManager(object):

    def __init__(self, self, app=None, flask_sqlalchemy_db=None):
        self.init_app(app, flask_sqlalchemy_db)

    def init_app(self, app=None, flask_sqlalchemy_db=None):
        pass

    def get_friends(self, user. group):
        """Get all relations for user, filter by group if any"""
        pass

    def get_pending_requests(self, user):
        """Get all requests for user with pending staus"""
        pass

    def get_pending_requests_sent(self, user):
        """Get all requests from user with pending, rejected staus
        ignored staus is considerd as pending"""
        pass

    def drop_friendship(self, friendship):
        """Drop friendship object"""
        pass

    def accept_request(self, request):
        """Accept request. Change status to accepted"""
        pass

    def decline_request(self, request):
        """Reject request. Change status to declined"""
        pass

    def ignore_request(self, request):
        """Ignore request. Change status to ignored"""
        pass

    def withdraw_request(self, request):
        """Withdraw a pending request.
        Can be done only iff peding state"""
        pass

    def get_route(self, from_user, to_user):
        """Get shortest degree of relation between two users.
        Returns all routes if more than one exists with same degree"""
        pass

    def get_common_friends(self, user1, user2):
        """Returns friends commmon to user1 and user2"""
        pass
