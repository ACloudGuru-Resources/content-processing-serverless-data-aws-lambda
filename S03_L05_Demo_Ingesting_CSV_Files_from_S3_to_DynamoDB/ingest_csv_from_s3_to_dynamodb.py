import boto3
import json

s3_client = boto3.client("s3") 
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Courses")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_csv_file_name = event['Records'][0]['s3']['object']['key']
    csv_object= s3_client.get_object(Bucket=bucket_name, Key=s3_csv_file_name)
    data = csv_object['Body'].read().decode("utf-8")
    courses = data.split("\n")

    for course in courses:
        print(course)
        course_data = course.split(",")
        #add to dynamodb
        try:
            print(course_data[0])
            print(course_data[1])
            # When you insert data into DynamoDB you have to specify the type of data in the json object.
            table.put_item(
                Item = {
                    'id': int(course_data[0]),
                    'name': course_data[1]
                    }
                )
            print('Successfully added the course: ', course_data[1])
        except Exception as e:
            print("Exception", e)
            raise e

    return{
        'statusCode': 200,
        'body': json.dumps('Items were written to the Courses Dynamodb table')
    }
