import json

class RequestDeserializer(object):

    def __init__(self, jsonResponse):
        self.__dict__ = json.loads(jsonResponse)

if __name__ == "__main__":
    pass
