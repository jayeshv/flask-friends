from flask import Blueprint


class FollowManager(object):
    
    def __init__(self, self, app=None, flask_sqlalchemy_db=None):
        self.init_app(app, flask_sqlalchemy_db)

    def init_app(self, app=None, flask_sqlalchemy_db=None):
        pass

    def add_group(self): 
        pass

    def drop_group(self):
        pass

    def follow(self, user1, user2, group):
        pass

    def get_followers(self, user, group):
        pass

    def get_following(self, user):
        pass

    def unfollow(self, follow):
        pass


class FriendshipManager(object):
    pass
