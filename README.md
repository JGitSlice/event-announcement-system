# Serverless Event Announcement System

A serverless event announcement platform built using **Amazon S3, AWS Lambda, Amazon API Gateway, and Amazon SNS**. The application allows users to view upcoming events, subscribe to email notifications, and create new events through a web interface.

## Overview

The Serverless Event Announcement System demonstrates how AWS services can work together to build a cloud-based application without managing servers.

The frontend is hosted on Amazon S3 Static Website Hosting. API Gateway exposes HTTP endpoints that invoke Lambda functions to process subscription requests and event creation. Event details are stored in an S3 JSON file, while Amazon SNS sends email notifications to subscribers whenever a new event is announced.

## Features

- **Event Listing:** Displays upcoming events with titles, dates, and descriptions.
- **Email Subscriptions:** Allows users to subscribe to event notifications using their email addresses.
- **Event Creation:** Enables users to create events through a web form.
- **Dynamic Event Storage:** Updates event data in an S3-hosted `events.json` file.
- **Email Notifications:** Sends event announcements to confirmed SNS email subscribers.
- **Responsive Frontend:** Provides a simple interface built with HTML, CSS, and JavaScript.
- **Serverless Architecture:** Uses managed AWS services without maintaining application servers.

## Architecture

```text
                 Users
                   |
                   v
          Amazon S3 Website
          HTML, CSS, JavaScript
                   |
                   v
           Amazon API Gateway
             /           \
            v             v
     POST /subscribe   POST /create-event
            |             |
            v             v
    subscribeUserLambda  createEventLambda
            |             |
            v          +--+----------+
       Amazon SNS      |             |
            ^          v             v
            |      Amazon S3     Amazon SNS
            |      events.json   Publish message
            |                        |
            +------------------------+
                         |
                         v
                  Email Subscribers
```

### Request Flow

**1. Subscribe to notifications**

1. A user submits an email address on the website.
2. API Gateway forwards the request to `subscribeUserLambda`.
3. Lambda calls Amazon SNS to create an email subscription.
4. SNS sends a confirmation email to the user.
5. After confirmation, the user can receive event announcements.

**2. Create an event**

1. A user submits the event title, date, and description.
2. API Gateway forwards the request to `createEventLambda`.
3. Lambda retrieves the existing `events.json` file from S3.
4. The new event is appended to the existing event list and saved back to S3.
5. Lambda publishes an announcement through Amazon SNS.
6. Confirmed subscribers receive an email notification.
7. The frontend fetches the updated JSON data and displays the new event.

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Hosts the static website and stores event data |
| AWS Lambda | Processes subscription and event creation requests |
| Amazon API Gateway | Exposes HTTP API endpoints |
| Amazon SNS | Manages email subscriptions and sends notifications |
| AWS IAM | Provides permissions for Lambda to access AWS services |
| Amazon CloudWatch | Provides Lambda execution logs for debugging |

## Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python
- **Cloud Platform:** Amazon Web Services (AWS)
- **API:** Amazon API Gateway HTTP API
- **Storage:** Amazon S3 with JSON
- **Notifications:** Amazon SNS
- **Version Control:** Git and GitHub

## Project Structure

```text
event-announcement-system/
├── index.html
├── style.css
├── script.js
├── events.json
├── README.md
└── lambda/
    ├── subscribeUserLambda.py
    └── createEventLambda.py
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/subscribe` | Subscribes an email address to event notifications |
| POST | `/create-event` | Creates an event, updates S3 data, and publishes an SNS notification |

### Example: Subscribe Request

```json
{
  "email": "user@example.com"
}
```

### Example: Create Event Request

```json
{
  "title": "AWS Cloud Workshop",
  "date": "2026-11-15",
  "description": "A hands-on workshop covering AWS cloud services."
}
```

### Example: Event Data

The `events.json` file stores events as a JSON array.

```json
[
  {
    "title": "AWS Cloud Workshop",
    "date": "2026-11-15",
    "description": "A hands-on workshop covering AWS cloud services."
  }
]
```

## Setup and Deployment

To recreate the project in your own AWS account:

1. **Create an S3 bucket** and upload `index.html`, `style.css`, `script.js`, and `events.json`.
2. **Configure static website hosting** for the frontend.
3. **Create an SNS topic** for event announcements.
4. **Create the Lambda functions** using the Python files in the `lambda/` directory.
5. **Configure IAM permissions** so the Lambda functions can access the required S3 and SNS resources.
6. **Create an API Gateway HTTP API** with the `/subscribe` and `/create-event` routes.
7. **Configure CORS** to allow requests from the frontend origin.
8. **Update the configuration values** in the Lambda code with your own S3 bucket name and SNS topic ARN.
9. **Update the API URL** in `script.js` to use your API Gateway invoke URL.
10. Test email subscriptions, event creation, S3 updates, and SNS notifications.

Refer to the official AWS documentation for service-specific configuration instructions.

## Security Considerations

- Grant Lambda execution roles only the IAM permissions they need.
- Restrict API access and validate incoming request data.
- Configure CORS to allow only trusted website origins in production.
- Avoid exposing sensitive credentials, account information, or secrets in source code.
- Consider Amazon CloudFront with HTTPS for production website hosting.
- Add authentication and authorization before allowing public users to create events.
- Consider a database such as Amazon DynamoDB if concurrent event creation or more advanced data management is required.

**Note:** This project was built and tested as a learning project. The AWS resources used for the demonstration have been deleted, so the live application and API endpoints are not currently available. The source code is retained in this repository for reference and redeployment.

## Learning Outcomes

Through this project, I gained practical experience with:

- Building serverless applications on AWS.
- Integrating API Gateway with Python Lambda functions.
- Using Amazon S3 for static website hosting and JSON data storage.
- Implementing email subscriptions and notifications with Amazon SNS.
- Configuring IAM permissions and CORS.
- Debugging frontend-to-backend requests using CloudWatch logs.
- Managing source code with Git and GitHub.

## Future Improvements

- Add authentication for event administrators.
- Migrate event storage from JSON to Amazon DynamoDB.
- Add event editing and deletion.
- Use Amazon CloudFront for secure content delivery.
- Add automated deployment through GitHub Actions.
- Add request validation, rate limiting, and improved error handling.


If you find this project useful, feel free to explore the code and adapt it for your own learning.
