import json
import logging
import os
import time
import uuid

import boto3
from validate_docbr import CPF
dynamodb = boto3.resource('dynamodb')
cpf = CPF()

def create(event, context):
    data = json.loads(event['body'])
    if 'document' not in data or not cpf.validate(data['document']):
        logging.error("Validation Failed")
        # create a response
        response = {
            "statusCode": 400,
            "body": "{\n\"error\" : \"Invalid document\"\n}"
        }
        return response
        #raise Exception("Couldn't create the todo item.")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'document': data['document'],
        'name' : data['name'],
        "mothersName" : data['mothersName'],
        "addresses" : data['addresses'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
