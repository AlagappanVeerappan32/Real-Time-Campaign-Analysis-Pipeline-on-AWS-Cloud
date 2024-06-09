import json
import boto3

# Initialize the Kinesis client
client = boto3.client('kinesis')

def lambda_handler(event, context):
    try:
        # Parse the JSON body from the incoming event
        messages = json.loads(event['body'])

        # Iterate over each message and send it to the Kinesis stream
        for message in messages:
            data = json.dumps(message)
            client.put_record(StreamName="hellotesting", Data=data, PartitionKey="1")
            print("Data Inserted")

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except KeyError as e:
        print(f"Missing key in event data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

