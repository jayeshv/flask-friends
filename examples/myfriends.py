import flask
import flask.ext.sqlalchemy
import flask.ext.friends

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    email = db.Column(db.Unicode, unique=True)


@app.route('/login')
def login_view():
    pass


@app.route('/')
def index_page():
    pass


def get_friends():
    pass


def add_friend():
    pass


db.create_all()
app.run()

