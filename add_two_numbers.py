import json

def lambda_handler(event, context):
    """
    Lambda function to add two numbers and return the result.
    """
    try:
        # Extract numbers from the event
        num1 = int(event.get('num1', 0))
        num2 = int(event.get('num2', 0))
        result = num1 + num2
        
        # Return the result
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
