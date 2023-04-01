from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from db import db
from models import UserModel, Blocklist
from schemas import UserSchema
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt,jwt_required,get_jwt_identity

#creating a blueprint object for the User views
blp = Blueprint("User",__name__,"user blueprint")

#class for user registration
@blp.route('/register')
class UserRegistration(MethodView):

    @blp.arguments(UserSchema)
    def post(self, data):

        #querying the user table to check if the username already exists
        if UserModel.query.filter(UserModel.username == data['username']).first():
            abort(409, message="username already exists.")

        user = UserModel(username=data['username'], password=pbkdf2_sha256.hash(data['password']))

        #adding username and password to the database after checking not exist constraint
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message= "An error occured while adding the details.")
        
        return {'message': 'User registered successfully'},201

    
#class for user login
@blp.route("/login")
class UserLogin(MethodView):

    #post method to check existence of username in the user table and compare password hash
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        #if authenticated, generate a jwt token to be used in further API requests
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")      

#class for user logout
@blp.route("/logout")
class UserLogout(MethodView):

    #post request to logout session and add the jti present in the jwt token to the blocklist table
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        blocklist_token = Blocklist(blocked_jti=jti)
        try:
            db.session.add(blocklist_token)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message= "An error occured while token revocation")
        return {"message": "Successfully logged out"}, 200
    
#class for refreshing session
@blp.route("/refresh")
class TokenRefresh(MethodView):

    #post method for exchanging the refresh token for an access token and then putting the refresh token in the blocklist
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti = get_jwt()["jti"]
        blocklist_token = Blocklist(blocked_jti=jti)
        try:
            db.session.add(blocklist_token)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message= "An error occured while token revocation")
        return {"access_token": new_token}, 200