<!--
title: 'AWS Serverless REST API with DynamoDB store example in Python'
description: 'This example demonstrates how to setup a RESTful Web Service allowing you to create, list, get, update and delete Todos. DynamoDB is used to store the data.'
layout: Doc
framework: v1
platform: AWS
language: Python
authorLink: 'https://github.com/godfreyhobbs'
authorName: 'Godfrey Hobbs'
authorAvatar: 'https://avatars1.githubusercontent.com/u/8434141?v=4&s=140'
-->
# Serverless REST API

This example demonstrates how to setup a [RESTful Web Services](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) allowing you to create, list, get, update and delete Customers. DynamoDB is used to store the data. This is just an example and of course you could use any data storage as a backend.

## Structure

This service has a separate directory for all the customer operations. For each operation exactly one file exists e.g. `customer/delete.py`. In each of these files there is exactly one function defined.

The idea behind the `customer` directory is that in case you want to create a service containing multiple resources e.g. addresses, contact infos and etc you could do so in the same service. While this is certainly possible you might consider creating a separate service for each resource. It depends on the use-case and your preference.


## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  serverless-rest-api-with-dynamodb-dev-update: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-update
  serverless-rest-api-with-dynamodb-dev-get: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-get
  serverless-rest-api-with-dynamodb-dev-list: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-list
  serverless-rest-api-with-dynamodb-dev-create: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-create
  serverless-rest-api-with-dynamodb-dev-delete: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-delete
```

## Usage

You can create, retrieve, update, or delete customers with the following commands:

### Create a Customer

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer --data '{
    "document" : "000.000.000-00",
    "mothersName" : "Mamãe Querida",
    "addresses" : [
        {
            "street" : "Rua da avenida do bairro",
            "neighbour" : "Bairro",
            "zip": "2222222",
            "number" : "999",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"
        },
        {
            "street" : "Rua da avenida do bairro2",
            "neighbour" : "Bairro",
            "zip": "2222223",
            "number" : "990",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"
        }
    ]
}'
```

No output

### List all Customers

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer
```

Example output:
```bash
[{
    "id": "4c6a7a27-ea1d-11ea-a6ac-bb90133ae872",
    "document": "000.000.000-00",
    "mothersName": "Mamãe Querida",
    "addresses": [
        {
            "street": "Rua da avenida do bairro",
            "neighbour": "Bairro",
            "zip": "2222222",
            "number": "999",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "country": "BR"
        },
        {
            "street": "Rua da avenida do bairro2",
            "neighbour": "Bairro",
            "zip": "2222223",
            "number": "990",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "country": "BR"
        }
    ],
    "createdAt": "1598722214.5070543",
    "updatedAt": "1598722214.5070543"
}]%
```

### Get one Customer

```bash
# Replace the <id> part with a real id from your customer table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer/<id>
```

Example Result:
```bash
{
    "id": "4c6a7a27-ea1d-11ea-a6ac-bb90133ae872",
    "document": "000.000.000-00",
    "mothersName": "Mamãe Querida",
    "addresses": [
        {
            "street": "Rua da avenida do bairro",
            "neighbour": "Bairro",
            "zip": "2222222",
            "number": "999",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "country": "BR"
        },
        {
            "street": "Rua da avenida do bairro2",
            "neighbour": "Bairro",
            "zip": "2222223",
            "number": "990",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "country": "BR"
        }
    ],
    "createdAt": "1598722214.5070543",
    "updatedAt": "1598722214.5070543"
}%
```

### Update a Customer

```bash
# Replace the <id> part with a real id from your customers table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer/<id> --data '{ "text": "Learn Serverless", "checked": true }'
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%
```

### Delete a Customer

```bash
# Replace the <id> part with a real id from your customers table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer/<id>
```

No output

