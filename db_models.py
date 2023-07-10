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

    @classmethod
    def get_all(cls):
        return [cls.remove_excluded_keys(item) for item in cls.query.all()]

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_by_letter(cls, field, letter):
        return cls.query.filter(getattr(cls, field).startswith(letter)).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_one(cls, **kwargs):
        cls.query.filter_by(**kwargs).delete()
        db.session.commit()

    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    @classmethod
    def get_latest(cls, limit=None):
        users = cls.query.order_by(cls.created_at).all()
        users.reverse()
        return users if limit is not None else users[:limit]
    
    @classmethod
    def to_dict(cls, self):
        return {k: v for k, v in vars(self).items() if k not in self.excluded_keys}

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'
    
class Message(BaseModel):
    __bind_key__ = __tablename__ = 'messages'
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author = db.relationship('User', foreign_keys=[author_id])
    recipient = db.relationship('User', foreign_keys=[recipient_id])

class User(BaseModel, UserMixin):
    __bind_key__ = __tablename__ = 'users'
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_teaching = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    excluded_keys = BaseModel.excluded_keys + ['password']

    avatar = db.relationship('Avatar', backref='user', uselist=False)
    music_sheets = db.relationship('MusicSheet', backref='author')
    comments = db.relationship('Comment', backref='author')
    # Message has two foreign keys of same model
    #messages = db.relationship('Message', primaryjoin="or_(User.id == Message.author_id, User.id == Message.recipient_id)", backref='user')

class Avatar(BaseModel):
    __bind_key__ = 'avatars'
    image = db.Column(db.LargeBinary, nullable=False)
    image_format = db.Column(db.String(10), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class MusicSheet(BaseModel):
    __bind_key__ = 'music_sheets'
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class Comment(BaseModel):
    __bind_key__ = 'comments'
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Artist(BaseModel):
    __bind_key__ = __tablename__ = 'artists'
    name = db.Column(db.String(100), nullable=False, unique=True)
    image = db.Column(db.LargeBinary)
    image_format = db.Column(db.String(10))
    sheets = db.relationship('MusicSheet', backref='artist')

class Genre(BaseModel):
    __bind_key__ = __tablename__ = 'genres'
    name = db.Column(db.String(100), nullable=False, unique=True)

    sheets = db.relationship('MusicSheet', backref='genre')

class Quote(BaseModel):
    __bind_key__ = __tablename__ = 'quotes'
    content = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
