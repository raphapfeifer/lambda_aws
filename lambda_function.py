import json
import boto3
from log import print_log

s3_client = boto3.client('s3')
 

def lambda_handler(event, context):
    
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    response = s3_client.get_object(Bucket=bucket, Key=key)
    size_in_bytes = response['ContentLength']
    mega_byte = 1024 * 1024

    if size_in_bytes > mega_byte:
        print('The object is too large!')
        return 'The object is too large!'

    return 'The object is ok!'
    #return {
    #    'statusCode': 200,
    #    'body': f'<html><body>Requests Data {json.dumps(event)}<body><html>',
    #    'headers': {
    #        'content-type': 'text/html'
    #    }
    #}
