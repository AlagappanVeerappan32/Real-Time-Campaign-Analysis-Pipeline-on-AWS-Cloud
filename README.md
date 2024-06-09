# Real-Time Campaign Analysis Pipeline on AWS Cloud

## Overview

The **Real-Time Campaign Analysis Pipeline** is designed to provide insights into the performance of email marketing campaigns. By leveraging AWS services and SendGrid, this pipeline captures real-time data on email interactions, such as open rates and click rates, and processes this data to help optimize campaign performance.

## Services Used

- **Python**
- **Webhook**
- **SendGrid**
- **AWS Lambda**
- **Kinesis Data Stream**
- **Kinesis Firehose**
- **Amazon S3**
- **API Gateway**
- **Streaming Pipeline Design**

## Architecture

The architecture involves several components to capture, process, and analyze email interaction data:

1. **SendGrid**: Sends marketing emails and tracks interactions.
2. **API Gateway**: Receives webhook events from SendGrid.
3. **AWS Lambda**: Processes incoming webhook events.
4. **Kinesis Data Stream**: Streams processed events for further processing.
5. **Kinesis Firehose**: Delivers streaming data to Amazon S3.
6. **Amazon S3**: Stores processed data.
8. **S3 Select**: Queries and analyzes data in S3.

## Prerequisites

1. **SendGrid Account**:
    - Verify your email account.
    - Generate an API key.
    - Enable email tracking.
    - Configure event webhook to send POST requests.

## Setup Instructions

### SendGrid Configuration

1. **Verify Email Account**: Ensure your SendGrid account email is verified.
2. **Generate API Key**: Create an API key for API access.
3. **Enable Tracking**: Enable email event tracking in SendGrid.
4. **Configure Event Webhook**: Set up SendGrid to send event data via webhook to your API Gateway endpoint.

### AWS Configuration

1. **API Gateway**: Create an API Gateway to receive webhook events.
2. **Lambda Function**: Set up a Lambda function to process incoming events from the API Gateway.
3. **Kinesis Data Stream**: Create a Kinesis Data Stream to handle real-time data processing.
4. **Kinesis Firehose**: Configure Kinesis Firehose to deliver data to Amazon S3.
5. **Amazon S3**: Set up an S3 bucket to store the processed data.

## Example Event

```json
{
  "email": "email_id",
  "event": "open",
  "ip": "your_ip",
  "sg_content_type": "html",
  "sg_event_id": "****",
  "sg_machine_open": false,
  "sg_message_id": "******",
  "timestamp": ******,
  "useragent": "*****"
}
