import boto3
import base64
import json

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function to upload a file to an S3 bucket.
    """
    try:
        # Replace with your S3 bucket name
        bucket_name = 'ys3-First'
        
        # Extract file details from the event
        file_name = event['LAmda']
        file_content = base64.b64decode(event['file_content'])
        
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
