import json
from log import print_log

def lambda_handler(event, context):
    print_log(event)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
