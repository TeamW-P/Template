from flask import jsonify, abort, Blueprint, request, make_response
from core.TemplateCore import Template
import json
from . import routes

# TODO rename path, and method name
# path of the endpoint, for convention see here -> https://restfulapi.net/resource-naming/
@routes.route('/template-endpoint', methods=['POST'])
def template_endpoint():
    '''
    Represents an endpoint to be added. When adding a new endpoint, name the path 
    according to convention, and add it to the API documentation so it can be referred 
    to by everyone. Make sure to add error handling like the example below
    '''
    something = 2+2
    try:
        if (something):
            raise Exception("Something went wrong")

        result = something
        return jsonify(result)

    except Exception as e:
        abort(400, "Error: " + str(e))