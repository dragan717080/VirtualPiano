import graphene

class GenreType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class MusicSheetType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    content = graphene.String()
    genre = graphene.Field(GenreType)

class UserType(graphene.ObjectType):
    id = graphene.ID()
    email = graphene.String()
    username = graphene.String()
    is_admin = graphene.Boolean()
    avatar = graphene.String()
    music_sheets = graphene.List(MusicSheetType)

class CommentType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    author = graphene.Field(UserType)

class MessageType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    author = UserType
