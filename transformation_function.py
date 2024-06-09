import json
import boto3
import base64
from typing import List, Dict, Any

def process_record(record: Dict[str, Any]) -> Dict[str, Any]:
    try:
        payload = base64.b64decode(record['data']).decode('utf-8')
        print('payload:', payload)
        
        row_w_newline = payload + "\n"
        print('row_w_newline type:', type(row_w_newline))
        
        encoded_data = base64.b64encode(row_w_newline.encode('utf-8')).decode('utf-8')
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': encoded_data
        }
        
        return output_record
    
    except Exception as e:
        print(f"Error processing record {record['recordId']}: {e}")
        return {
            'recordId': record['recordId'],
            'result': 'ProcessingFailed',
            'data': record['data']
        }

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, List[Dict[str, Any]]]:
   
    print(event)
    
    output = []
    
    for record in event['records']:
        output_record = process_record(record)
        output.append(output_record)
    
    print(f'Processed {len(event["records"])} records.')
    
    return {'records': output}

