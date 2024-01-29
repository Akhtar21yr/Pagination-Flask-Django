from flask_marshmallow import Marshmallow
from app.models.models import Student
from flask_marshmallow import Marshmallow
from app import app

ma = Marshmallow(app)

class StudentSchema(ma.Schema):
    class Meta:
        model = Student
        fields = ['rollno','name','age','city']