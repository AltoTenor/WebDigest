from flask import Blueprint, request 
from flask_restful import Api, Resource
from qnabackend.common.utils import getAnswer

resources = Blueprint('resources', __name__)
api = Api(resources)

class Backend(Resource):
    def post(self):
        url = request.json['url']
        question = request.json['question']

        print(url, question)
        answer = getAnswer(url, question)

        return {'question' : question, 'answer' : answer}
    
api.add_resource(Backend, '/question')