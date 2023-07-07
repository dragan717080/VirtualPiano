import graphene
from db_models import User, MusicSheet, Comment
from api.types import UserType, MusicSheetType, CommentType
from helpers import Helpers

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID())
    all_sheets = graphene.List(MusicSheetType)
    sheet = graphene.Field(MusicSheetType, id=graphene.ID())
    all_comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, id=graphene.ID())
    sheets_by_user = graphene.Field(graphene.List(MusicSheetType), id=graphene.ID())

    def resolve_all_users(self, info):
        return User.get_all()
        
    def resolve_user(self, info, id):
        return User.get_by_id(id)

    def resolve_all_sheets(self, info):
        return MusicSheet.get_all()
    
    def resolve_sheet(self, info, id):
        return MusicSheet.get_by_id(id)

    def resolve_all_comments(self, info):
        return Comment.get_all()
    
    def resolve_comment(self, info, id):
        return Comment.get_by_id(id)

    def resolve_sheets_by_user(self, info, id):
        return User.get_by_id(id).sheets

schema = graphene.Schema(query=Query)
