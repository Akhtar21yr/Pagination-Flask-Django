from flask_restful import Resource
from app.models.models import Student
from app.serializers.serializers import StudentSchema
from flask import jsonify,request,abort
from app import db
class StudentView(Resource):
    def get(self,rollno=None):
        if rollno:
            student = Student.query.filter_by(rollno=rollno).first()
            if student :
                serializer = StudentSchema()
                data = serializer.dump(student)
                return ({'student':data}),200
            else :
                abort(404)
        else :
            page = request.args.get('page',1,type=int)
            count = request.args.get('count',1,type=int)
            students = Student.query.paginate(page=page,per_page=count)

            serializer = StudentSchema(many=True)
            data = serializer.dump(students)
            return ({'students':data}),200
        
    def post(self):
        data = request.get_json()
        serializer = StudentSchema()
        try:
            student = serializer.load(data)
            # student.save_to_db()
            student  = Student(name=student['name'],age = student['age'],city=student['city'])
            # student.save_to_db()
            db.session.add(student)
            db.session.commit()
            return ({'msg':'student created successfully'}),201
        except Exception as e :
            return jsonify({'msg':'some error occured'}),400
        
    def put(self,rollno):
        data = request.get_json()
        student = Student.query.filter_by(rollno=rollno).first()
        if student:
            serializer = StudentSchema()
            try :
                update_student = serializer.load(data)
                update_student.rollno = rollno
                update_student.save_to_db()
                return jsonify({'msg':'student updated'})
            except :
                return jsonify({'msg':'some error occured'}),400
        else :
            return jsonify({'msg':'student not found'}),404
        

    def patch(self,rollno):
        data = request.get_json()
        student = Student.query.filter_by(rollno=rollno).first()
        if student:
            serializer = StudentSchema()
            try :
                update_student = serializer.load(data,partial=True)
                update_student.rollno = rollno
                update_student.save_to_db()
                return jsonify({'msg':'student updated'})
            except :
                return jsonify({'msg':'some error occured'}),400
        else :
            return jsonify({'msg':'student not found'}),404
        
    def delete(self,rollno):
        student = Student.query.filter_by(rollno=rollno).first()
        if student:
            student.delete_from_db()
            return jsonify({'msg':'student deleted successfully'})
        else :
            return jsonify({'msg':'user not found'})
    