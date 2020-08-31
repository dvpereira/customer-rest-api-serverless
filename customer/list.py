import json
import os
import logging

from customer import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
	table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

	# fetch all customers from the database
	result = table.scan()

	logging.info(result)

	if result['Count'] == 0:
		response = {
			"statusCode": 404,
			"body": "{\n\"error\" : \"No records found\"\n}"
		}
	else:
		# create a response
		response = {
			"statusCode": 200,
			"body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
		}

	return response