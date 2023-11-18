import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
# from database import createDB as cb
# from database import insertDb as ib

app = Flask(__name__)

# The request body will have the company key and director Id
# This will be used to update the relevant table

@app.route("/responses", methods=['POST'])
def addDataFromQuestionnaire():

    resp = deserializeJson(request)

    # This should include a header in the url that confirms access to this endpoint
    if request.method == 'POST' and confirmDirectors:

        if not resp.get("terms"):
            return "You need to agree to terms and conditions"

        addDataToDatabase(resp)

        return "Data submitted successfully!"
    
    abort(401)
    return "Not Authorised"



@app.route("/dashboard", methods=['GET'])
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
    abort(401)
    return "Not Authorised"

@app.route("/authenticate_sirdar", methods=['GET'])
def authenticateSirDarEmployee():

    resp = deserializeJson(request)

    if resp.get("email") and request.method == "GET":
        return "Successfully logged in"
    
    abort(401)
    return "Not Authorised"

@app.route("/authenticate_director", methods=['GET'])
def authenticateDirector():

    resp = deserializeJson(request)

    if resp.get("email") and request.method == "GET":
        return "Successfully logged in"
    
    abort(401)
    return "Not Authorised"

@app.route("/add_client", methods=["POST"])
def addClientsInDB():

    return "Successful"


def addDataToDatabase(desirializedJson):
    
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

def confirmDirectors(requestObject):

    # Get directors from DB
    if requestObject.get("email"):
        return True
    return False


def deserializeJson(req):

    # Deserialize json in request
    responses = req.json
    return responses


def checkRequestHeaderValue(requestHeaderValue):

    if request.access_control_request_headers:
        return True

    return False


if __name__ == "__main__":
    app.run(debug=True, port=5050)
