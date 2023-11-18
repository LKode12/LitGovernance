import json
from flask import Flask
from flask import request
from flask import jsonify
import requests
from controllers.responses import Responses

app = Flask(__name__)

# The request body will have the company key and director Id
# This will be used to update the relevant table
requestBodyJson = None
responses = None

@app.route("/responses", methods=['POST'])
def postResponsesFromQuestionnaire():

    requestBodyJson = json.dumps(request.get_json())
    responses = Responses(requestBodyJson)
    
    return jsonify('{"message":"request was successful"}')

def queryDb():
    
    # This should generate an sql query to update relevant table
    pass
    
@app.route()
def getResponseToHome():

    # If the sql query was successful return response and direct it to homepage
    # so we pop the board member from list of directors 
    pass

def postEmailKeyBackHome():

    """
        This method sends the email key back to the home
        API for every submission
    """
    requests.post("")

if __name__ == "__main__":
    app.run()
