import json
from flask import Flask
from flask import request
from flask import jsonify



class questionaireAPI:

    def __inti__(self, jsonQuestinaireRequest):

        # Request from the assessment q
        self.jsonQuestinaireRequest = jsonQuestinaireRequest

        # The request body will have the company key and director Id
        # This will be used to update the relevant table
        self.data = request.data

    @app.route("/assessment", methods=[POST])
    def queryDb():
        
        # This should generate an sql query to update relevant table

        pass

    def queryResponse():

        # If the sql query was successful return response and direct it to homepage
        # so we pop the board member from list of directors 
        
