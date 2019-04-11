from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


tags = db.Table(
    'Post_Tags',
    db.Column('post_id', db.Integer(), db.ForeignKey('Posts.id')),
    db.Column('tag_id', db.Integer(), db.ForeignKey('Tags.id'))
)


class Post(db.Model):
    __tablename__ = 'Posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('Users.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "Post '{}'>".format(self.title)


class Tag(db.Model):
    __tablename__ = 'Tags'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)


class Comment(db.Model):
    __tablename__ = 'Commetns'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('Posts.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])


@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
    app.run()
