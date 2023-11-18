import json
from flask import Flask
from flask import request
from flask import jsonify
from controllers.responses import RequestDeserializer

litGovernanceAPI = Flask(__name__)

# The request body will have the company key and director Id
# This will be used to update the relevant table

@litGovernanceAPI.route("/responses", methods=['POST'])
def addDataFromQuestionnaire():

    # This should include a header in the url that confirms access to this endpoint
    if request.method == 'POST':
        
        responses = deserializeJson()
        addDataFromQuestionnaire(responses)

        return jsonify('{"message":"request was successful"}')
    
    return denyEndPointAccess()


@litGovernanceAPI.route("/dashboard", methods=['GET'])
def getDataForDashBoard():

    """
        This method should call a database method
        The database method should get data from the database
        This method should return a json format of the data
    """

    dashboarRequest = deserializeJson(jsonify(request.get_json()))

    if checkRequestHeaderValue(dashboarRequest) and request.method == 'GET':
        jsonForDashboard = {
            "Purpose" : "Purpose result from database",
            "Performance" : "Performance result from database",
            "Sustainability" : "Performance result from database",
            "Conformance" : "Conformance result from database",
            "Board Composition" : "Board composition data from database"
            }
    
        return jsonify(jsonForDashboard)
    
    return denyEndPointAccess()


def denyEndPointAccess():

    return jsonify('"message" : "You do not have access to this api endpoint"')


def addDataToDatabase():
    
    # This should call method from database that creates the data
    # if table exists in the database and request header value is valid: add data
    # If the table does not exist and the request header value is valid: create table and add data
    pass


def getDashBoardDataFromDB():

    # This method should call a database method to get dashboard data
    # If table exist in database and request header value is valid: get data
    # If table does not exist but request header value is valid: inform accordingly
    # If request header value is invalid: inform accordingly
    pass


def deserializeJson():

    # This method desirializes all json from requests
    requestBodyJson = jsonify(json.dumps(request.get_json()))
    responses = RequestDeserializer(requestBodyJson)

    return responses


def checkRequestHeaderValue(requestHeaderValue):

    if request.access_control_request_headers:
        return True

    return False


if __name__ == "__main__":
    litGovernanceAPI.run(debug=True)
