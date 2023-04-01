from db import db 

class TA_Model(db.Model):

    __tablename__ = "TA"

    id = db.Column(db.Integer, primary_key=True)
    native_english_speaker = db.Column(db.Integer, unique=False, nullable = False)
    course_instructor = db.Column(db.Integer, unique = False, nullable = False )
    course = db.Column(db.Integer, unique = False, nullable = False)
    semester = db.Column(db.Integer, unique = False, nullable = False)
    class_size = db.Column(db.Integer, unique = False, nullable = False)
    performance_score = db.Column(db.Integer, unique = False, nullable = False)



