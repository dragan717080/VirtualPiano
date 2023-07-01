from datetime import datetime
from config.config import db
from flask_login import UserMixin

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    excluded_keys = ['_sa_instance_state']

    @staticmethod
    def remove_excluded_keys(item):
        return {var: value for var, value in vars(item).items() if var not in BaseModel.excluded_keys}

    @staticmethod
    def find_all(cls):
        return [cls.remove_excluded_keys(item) for item in cls.query.all()]

    @staticmethod
    def find_by_id(cls, id):
        return cls.query.filter(cls.id == id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete_one(cls, **kwargs):
        cls.query.filter_by(**kwargs).delete()
        db.session.commit()

    @staticmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'
    
class User(BaseModel, UserMixin):
    __bind_key__ = __tablename__ = 'users'
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_teaching = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    excluded_keys = BaseModel.excluded_keys + ['password']

    avatar = db.relationship('Avatar', backref='user', uselist=False)
    music_sheets = db.relationship('MusicSheet', backref='user')
    comments = db.relationship('Comment', backref='user')

"""     @staticmethod
    def find_all():
        return super.find_all(User) """

class Avatar(BaseModel):
    __bind_key__ = 'avatars'
    image = db.Column(db.LargeBinary, nullable=False)
    image_format = db.Column(db.String(10), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class MusicSheet(BaseModel):
    __bind_key__ = 'music_sheets'
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    genre = db.Column(db.String(100))

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Comment(BaseModel):
    __bind_key__ = 'comments'
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
