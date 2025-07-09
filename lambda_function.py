import json
from log import print_log

def lambda_handler(event, context):
    print_log(event)
    return {
        'statusCode': 200,
        'body': f'<html><body>Requests Data {json.dumps(event)}<body><html>',
        'headers': {
            'content-type': 'text/html'
        }
    }
