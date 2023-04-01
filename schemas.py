from marshmallow import Schema, fields

class TA_add_Schema(Schema):
    id = fields.Int(dump_only = True,)
    native_english_speaker = fields.Int(required = True)
    course_instructor = fields.Int(required = True)
    course = fields.Int(required = True)
    semester = fields.Int(required = True)
    class_size = fields.Int(required = True)
    performance_score = fields.Int(required = True)

class TA_update_Schema(Schema):
    id = fields.Int(dump_only=True)
    native_english_speaker = fields.Int()
    course_instructor = fields.Int()
    course = fields.Int()
    semester = fields.Int()
    class_size = fields.Int()
    performance_score = fields.Int()

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)