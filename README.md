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
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service customer-rest-api-with-dynamodb.zip file to S3 (1.27 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
......................................
Serverless: Stack update finished...
Service Information
service: customer-rest-api-with-dynamodb
stage: dev
region: us-east-1
stack: customer-rest-api-with-dynamodb-dev
resources: 35
api keys:
  None
endpoints:
  POST - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/customer
  GET - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/customer
  GET - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/customer/{id}
  PUT - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/customer/{id}
  DELETE - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/customer/{id}
functions:
  create: customer-rest-api-with-dynamodb-dev-create
  list: customer-rest-api-with-dynamodb-dev-list
  get: customer-rest-api-with-dynamodb-dev-get
  update: customer-rest-api-with-dynamodb-dev-update
  delete: customer-rest-api-with-dynamodb-dev-delete
layers:
  None
Serverless: Removing old service artifacts from S3...
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
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer/<id> --data '{
    "name" : "Nome Teste", 
    "document" : "074.378.320-46",
    "mothersName" : "Mamãe Querida",
    "addresses" : [
        {
            "street" : "Rua da avenida do bairro",
            "neighbour" : "Barra da Tijuca",
            "zip": "2222222",
            "number" : "999",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"
        },
        {
            "street" : "Rua da avenida do bairro2",
            "neighbour" : "Barra da Tijuca2",
            "zip": "2222223",
            "number" : "990",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"
        },
        {
            "street" : "Rua da avenida do bairro3",
            "neighbour" : "Barra da Tijuca3",
            "zip": "2222224",
            "number" : "990",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"
        },
        {
            "street" : "Rua da avenida do bairro3",
            "neighbour" : "Barra da Tijuca3",
            "zip": "2222224",
            "number" : "990",
            "city" : "Rio de Janeiro",
            "state" : "RJ",
            "country" : "BR"  
        }
    ]
}'
```

Example Result:
```bash
{
    "updatedAt": 1598728283295,
    "mothersName": "Mamãe Querida",
    "addresses": [
        {
            "zip": "2222222",
            "number": "999",
            "country": "BR",
            "city": "Rio de Janeiro",
            "street": "Rua da avenida do bairro",
            "neighbour": "Barra da Tijuca",
            "state": "RJ"
        },
        {
            "zip": "2222223",
            "number": "990",
            "country": "BR",
            "city": "Rio de Janeiro",
            "street": "Rua da avenida do bairro2",
            "neighbour": "Barra da Tijuca2",
            "state": "RJ"
        },
        {
            "zip": "2222224",
            "number": "990",
            "country": "BR",
            "city": "Rio de Janeiro",
            "street": "Rua da avenida do bairro3",
            "neighbour": "Barra da Tijuca3",
            "state": "RJ"
        },
        {
            "zip": "2222224",
            "number": "990",
            "country": "BR",
            "city": "Rio de Janeiro",
            "street": "Rua da avenida do bairro3",
            "neighbour": "Barra da Tijuca3",
            "state": "RJ"
        }
    ],
    "createdAt": "1598728010.98645",
    "id": "cb610a13-ea2a-11ea-9d69-2b2db892b2f9",
    "document": "074.378.320-46",
    "name": "Nome Teste"
}%
```

### Delete a Customer

```bash
# Replace the <id> part with a real id from your customers table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/customer/<id>
```

No output

