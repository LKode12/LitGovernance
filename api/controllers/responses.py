import json

class Responses(object):

    def __init__(self, jsonResponse):
        self.__dict__ = json.loads(jsonResponse)

if __name__ == "__main__":
    responses = '{"action": "print", "method": "onData"}'

    resps = Responses(responses)

    print(resps.action)
