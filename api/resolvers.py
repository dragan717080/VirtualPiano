import graphene
from db_models import User, MusicSheet, Comment
from api.types import UserType, MusicSheetType

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID())
    all_sheets = graphene.List(MusicSheetType)

    def resolve_all_users(self, info):
        return User.get_all()
        
    def resolve_user(self, info, id):
        return User.get_by_id(id)

    def resolve_all_sheets(self, info):
        return MusicSheet.get_all()
    
    def resolve_sheet(self, info, id):
        return MusicSheet.get_by_id(id)

schema = graphene.Schema(query=Query)
