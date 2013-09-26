from flask import Blueprint


class FollowManager(object):
    
    def __init__(self, self, app=None, flask_sqlalchemy_db=None):
        self.init_app(app, flask_sqlalchemy_db)

    def init_app(self, app=None, flask_sqlalchemy_db=None):
        pass


class FriendshipManager(object):
    pass
