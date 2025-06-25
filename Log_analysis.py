import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('processeLoges')   # Replace Table with your Table name

def lambda_handler(event, context):
    for record in event['Records']:
        s3_data = record['s3']
        bucket = s3_data['bucket']['name']
        key = s3_data['object']['key']

        s3 = boto3.client('s3')
        log_file = s3.get_object(Bucket=bucket, Key=key)
        log_content = log_file['Body'].read().decode('utf-8')

        for line in log_content.splitlines():
            log_name = str(uuid.uuid4())
            table.put_item(Item={
                'log_name': log_name,
                'log_line': line
            })

    return {
        'statusCode': 200,
        'body': 'Log processed successfully!'
    }

