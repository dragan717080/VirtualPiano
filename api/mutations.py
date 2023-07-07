import graphene
from db_models import User, Comment
from api.types import UserType, CommentType
from flask import abort

class responseMessage(graphene.ObjectType):
    message = graphene.String()

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        is_admin = graphene.Boolean(default_value=False)

    user = graphene.Field(UserType)

    def mutate(self, info, email, username, password, is_teaching=False, is_admin=False):
        # Create a new user instance
        new_user = User(
            email=email,
            username=username,
            password=password,
            is_teaching=is_teaching,
            is_admin=is_admin
        )
        new_user.save()

        return CreateUserMutation(user=new_user)

class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String(default_value=None)
        username = graphene.String(default_value=None)

    user = graphene.Field(UserType)

    def mutate(self, info, id, email=None, username=None):
        # Retrieve the user from the database based on the provided ID
        current_user = User.get_by_id(id)

        if current_user is None:
            raise Exception("User not found.")

        # Update the user fields if provided
        if email is not None:
            current_user.email = email

        if username is not None:
            current_user.username = username

        # Save the updated user to the database
        current_user.save()

        return UpdateUserMutation(user=current_user)

class DeleteUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    Output = responseMessage

    def mutate(root, info, id):
        # Delete the user from the database
        if not User.query.get(id):
            abort(404, "User not found")  # Raises a 404 HTTPException

        User.delete_one(id=id)

        # Return the custom response message
        return responseMessage(message="User deleted")

class CreateCommentMutation(graphene.Mutation):
    class Arguments:
        content = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    comment = graphene.Field(CommentType)

    def mutate(self, info, content, author_id):
        # Create a new comment instance
        new_comment = Comment(content=content, author_id=author_id)
        new_comment.save()

        return CreateCommentMutation(comment=new_comment)
        
class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
    create_comment = CreateCommentMutation.Field()

