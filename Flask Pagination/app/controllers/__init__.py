from flask import Blueprint
from flask_restful import Api
from .views import StudentView

def create_blueprint() :
    blueprint = Blueprint('api',__name__)
    api = Api(blueprint)

    api.add_resource(StudentView,'/api/students','/api/student/<int:rollno>/')

    return blueprint