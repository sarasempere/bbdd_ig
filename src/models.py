from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)

    #relation
    followers = db.relationship('Follower', lazy=True)

    comments = db.relationship('Comment', lazy=True)

    posts = db.relationship('Post', lazy=True)
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username" : self.username,
            "firstName": self.firstName,
            "lastName": self.lastName
            # do not serialize the password, its a security breach
        }

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=False, nullable=False)

    #relation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User")

    def __repr__(self):
        return '<Follower %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username" : self.username
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    date = db.Column(db.String(20))
    

    #relation many to one user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User")

    #relation one to many comments
    comments = db.relationship('Comment', lazy=True)

    def __repr__(self):
        return '<Post %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "content" : self.content,
            "date" : self.date
            # do not serialize the password, its a security breach
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commentText = db.Column(db.Text, unique=False, nullable=False)

    #relation many to one user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User")

    #relation many to one post
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship("Post")

    def __repr__(self):
        return '<Comment %r>' % self.commentText

    def serialize(self):
        return {
            "id": self.id,
            "commentText" : self.commentText
            # do not serialize the password, its a security breach
        }


class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer)
    url = db.Column(db.String(20))

    #relation many to one post
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship("Post")

    def __repr__(self):
        return '<Media %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "tipo" : self.tipo,
            "url" : self.url
            # do not serialize the password, its a security breach
        }