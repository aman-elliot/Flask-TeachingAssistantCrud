import sys
sys.path.append("..")
from models import UserModel
import pytest
from app import create_app
from db import db
import json

token = ''

@pytest.fixture()
def app():
    app = create_app("sqlite://")
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()

    print("db created")
    yield app

@pytest.fixture()
def client(app):
    with app.test_client() as client:
        yield client


class testcrud():

    def __init__(self,client,app):
        self.client = client
        self.app = app
        

    def test_registration_successful(self):
        response = self.client.post("/register", json = {"username":"xyz" , "password":"1234" })
        assert b'message' in response.data
        return response


    def test_login(self):
        response = self.client.post("/login", json = {"username":"xyz" , "password":"1234" })
        assert b'access_token' in response.data
        self.token  = response.json['access_token']
        print(self.token)
        return  response

    def test_create(self):
        header = {"Authorization":"Bearer {}".format(self.token)}
        response = self.client.post("/TA/add/", json = {
            "native_english_speaker":1,
            "course_instructor":7,
            "course":7,
            "semester":2,
            "class_size":70,
            "performance_score":3
        }, headers = header)
        return response

    def test_get(self):
        header = {"Authorization":"Bearer {}".format(self.token)}
        response = self.client.get("/TA/1", headers = header)
        return response

    def test_put(self):
        header = {"Authorization":"Bearer {}".format(self.token)}
        response = self.client.put("/TA/1", json = {
            "native_english_speaker":2,
            "course_instructor":8,
            "course":8,
            "semester":2,
            "class_size":80,
            "performance_score":3
            }, headers = header)
        return response

    def test_delete(self):
        header = {"Authorization":"Bearer {}".format(self.token)}
        response = self.client.delete("/TA/1", headers = header)
        return response
    


def test_registration(client,app):
    obj = testcrud(client,app)
    response1 = obj.test_registration_successful()
    assert response1.status_code == 201


def test_login(client,app):
    obj = testcrud(client,app)
    obj.test_registration_successful()
    response2 = obj.test_login()
    assert response2.status_code == 200

def test_create(client,app):
    obj = testcrud(client,app)
    obj.test_registration_successful()
    obj.test_login()
    response = obj.test_create()
    assert response.status_code == 201

def test_get(client,app):
    obj = testcrud(client,app)
    obj.test_registration_successful()
    obj.test_login()
    obj.test_create()
    response = obj.test_get()
    assert response.status_code == 200

def test_put(client,app):
    obj = testcrud(client,app)
    obj.test_registration_successful()
    obj.test_login()
    obj.test_create()
    response = obj.test_put()
    assert response.status_code == 200

def test_delete(client,app):
    obj = testcrud(client,app)
    obj.test_registration_successful()
    obj.test_login()
    obj.test_create()
    response = obj.test_delete()
    assert response.status_code == 200

