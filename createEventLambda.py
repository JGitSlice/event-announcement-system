import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET_NAME = "event-announcement-system-jahid"
EVENTS_FILE = "events.json"
TOPIC_ARN = "arn:aws:sns:ap-south-1:105499013835:event-announcements-topic"

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))

    new_event = {
        "title": body.get("title"),
        "date": body.get("date"),
        "description": body.get("description")
    }

    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=EVENTS_FILE
    )

    events = json.loads(response['Body'].read().decode('utf-8'))

    events.append(new_event)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=EVENTS_FILE,
        Body=json.dumps(events, indent=2),
        ContentType="application/json"
    )

    message = f"""
New Event Announced!

Title: {new_event['title']}
Date: {new_event['date']}
Description: {new_event['description']}
"""

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="New Event Announcement",
        Message=message
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps({
            "message": "Event created and notification sent successfully!"
        })
    }
