from flask import request, Blueprint, jsonify
from flask_login import current_user
from db_models import User
from flask_graphql import GraphQLView
from flask import jsonify, request
from graphql import execute, parse
from flask_cors import cross_origin
from api.resolvers import schema

api_pages = Blueprint('api', __name__, url_prefix = '/api')

@cross_origin()
@api_pages.route('/', methods=['GET', 'POST'])
def graphql():
    return GraphQLView.as_view('graphql', schema=schema, graphiql=True)()

