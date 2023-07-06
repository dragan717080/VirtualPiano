import graphene
from db_models import User, MusicSheet, Comment

class UserType(graphene.ObjectType):
    id = graphene.ID()
    email = graphene.String()
    username = graphene.String()
    is_admin = graphene.Boolean()

class MusicSheetType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    content = graphene.String()
    genre = graphene.String()

class CommentType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    author = UserType

class MessageType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    author = UserType
