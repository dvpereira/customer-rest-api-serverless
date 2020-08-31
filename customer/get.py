import os
import json

from customer import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
	table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

	# fetch customer from the database
	result = table.get_item(
		Key={
			'id': event['pathParameters']['id']
		}
	)

	# create a response
	if not 'Item' in result:
		response = {
		"statusCode": 404,
		"body": "{\n\"error\" : \"No records found\"\n}"
		}
	else:
		response = {
			"statusCode": 200,
			"body": json.dumps(result['Item'],
							   cls=decimalencoder.DecimalEncoder)
		}

	return response
