import flask
import flask.ext.sqlalchemy
import flask.ext.friends


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)


def get_gravatar(email):
    return ''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    email = db.Column(db.Unicode, unique=True)


#friendship_manager = flask.ext.friends.Friends()

#1st release
#Follow
#friendship_manager.add_group()                  #to group friends 
#friendship_manager.grop_group()                 #all relations in the group will be dropped
#friendship_manager.follow(user1, user2, group)  #group is none by default
#friendship_manager.get_followers(user1, group)
#friendship_manager.get_following(user1)
#friendship_manager.unfollow(follow)

#2nd release
#Mutual Friends
#friendship_manager.friend_request(user1, user2)
#friendship_manager.get_requests(user1)
#friendship_manager.accept_requests(request)   
#friendship_manager.reject_requests(request)
#friendship_manager.ignore_requests(request)
#friendship_manager.get_friends(user1, group)   #group is none by deafult 
#friendship_manager.get_relation(user1, user2)  #including route
#friendship_manager.drop_relation(relation)
#friendship_manager.add_to_group(relation, group)


@app.route('/')
def index_page():
    pass


def get_friends():
    pass


def add_friend():
    pass


db.create_all()
app.run()

