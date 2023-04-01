from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import TA_Model
from schemas import TA_update_Schema , TA_add_Schema

#creating a blueprint object for the teaching assistant views
blp = Blueprint("teaching_assistant", __name__ , description = "CRUD operations on teaching assistant data")

#class for retrieving, updating and deleting data in TA table 
@blp.route("/TA/<int:id>")
class TeachingAssitant(MethodView):

     # handle GET request for a specific TA with the given id
    @jwt_required()
    @blp.response(200, TA_update_Schema)
    def get(self, id):
        item = TA_Model.query.get_or_404(id)
        return item

    # handle PUT request to update the TA with the given id
    @jwt_required()
    @blp.arguments(TA_update_Schema)
    @blp.response(200, TA_update_Schema)
    def put(self, data, id):

        #querying TA table to get the data for the particular id
        queryset = TA_Model.query.get(id)

        if queryset:
            queryset.native_english_speaker = data['native_english_speaker']
            queryset.course_instructor = data['course_instructor']
            queryset.course = data['course']
            queryset.semester = data['semester']
            queryset.class_size = data['class_size']
            queryset.performance_score = data['performance_score']
        else:
            queryset = TA_Model(id=id, **data)

        db.session.add(queryset)
        db.session.commit()

        return queryset

    # handle DELETE request to delete the TA with the given id
    @jwt_required()
    def delete(self, id):

        queryset = TA_Model.query.get_or_404(id)
        db.session.delete(queryset)
        db.session.commit()
        return {"message": "Item deleted."},200


#class for adding/creating data in TA table 
@blp.route("/TA/add/")
class AddDetails(MethodView):

    # handle POST request to create a new TA
    @jwt_required()
    @blp.arguments(TA_add_Schema)
    @blp.response(201,TA_add_Schema)
    def post(self, data):
        data = TA_Model(**data)
        try:
            db.session.add(data)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message= "An error occured while adding the details.")

        return data
    


