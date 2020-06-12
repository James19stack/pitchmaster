from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    pitch=db.relationship('Pitch',backref='user',lazy='dynamic')

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def save_u(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    
    
    def __repr__(self):
        return f'User {self.username}'    

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comment=Comment.query.filter_by(pitch_id=pitch_id).all()
        return comment

    def __repr__(self):
        return f"Comment ('{self.comment}','{self.user}')"    

date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))

    

class Pitch(db.Model):
    __tablename__='pitch'
    id=db.Column(db.Integer,primary_key=True)
    pitch=db.Column(db.String())
    pitch_category=db.Column(db.String(20))
    posted=db.Column(db.DateTime,default=time_zone)
    upvotes=db.Column(db.Integer)
    downvotes=db.Column(db.Integer)
    comment=db.relationship('Comment',backref='pitch',lazy='dynamic')
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'