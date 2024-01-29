from app import db

class Student(db.Model):
    rollno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    age = db.Column(db.Integer,nullable=False)
    city = db.Column(db.String(100))

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # def __repr__(self):
    #     return self.name