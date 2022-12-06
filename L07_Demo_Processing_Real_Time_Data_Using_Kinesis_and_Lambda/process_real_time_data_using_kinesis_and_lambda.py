import json
import base64

def lambda_handler(event, context):    

    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        partitionKey = (record['kinesis']['partitionKey'])
        sequenceNumber = (record['kinesis']['sequenceNumber'])
        print("Sequence Number: " + sequenceNumber)
        print("Partition Key: " + partitionKey)
        print("Decoded payload: " + str(payload))

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda is receiving Kinesis Data Streams!')
    }
