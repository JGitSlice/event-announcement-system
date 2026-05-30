import json
import boto3
import os

sns = boto3.client('sns')

TOPIC_ARN = "PASTE_YOUR_TOPIC_ARN_HERE"

def lambda_handler(event, context):

    body = json.loads(event['body'])

    email = body['email']

    sns.subscribe(
        TopicArn=TOPIC_ARN,
        Protocol='email',
        Endpoint=email
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Subscription request sent. Check your email.'
        })
    }
