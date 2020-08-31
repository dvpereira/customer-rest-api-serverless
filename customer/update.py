import json
import time
import logging
import os

from customer import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
from validate_docbr import CPF
cpf = CPF()


def update(event, context):
    data = json.loads(event['body'])
    if 'document' not in data or not cpf.validate(data['document']):
        logging.error("Validation Failed")
        # create a response
        response = {
            "statusCode": 400,
            "body": "{\n\"error\" : \"Invalid document\"\n}"
        }
        return response

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the customer in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#name': 'name',
        },
        ExpressionAttributeValues={
          ':name': data['name'],
          ':mothersName': data['mothersName'],
          ':addresses': data['addresses'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #name = :name, '
                         'mothersName = :mothersName, '
                         'addresses = :addresses, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
