# TODO replace the name of the file with the name of the service you are calling
import requests

# api-endpoint, do not change
URL = "http://0.0.0.0:5001/"


def service_endpoint(payload):
    '''
    Makes a call to the service endpoint
    '''
    headers = {}
    response = requests.request(
        "POST", URL + "string", headers=headers, data=payload)
    return response