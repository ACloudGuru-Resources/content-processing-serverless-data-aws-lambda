import boto3
import awswrangler as wr

courses_bucket_name = 'guru-rewards-datafeed'
s3_courses_csv_file_name = 'guru-premium-courses/premium-courses.csv'

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    print('Received event from Step Functions')
    print(event)
    response = {}
    response ['Message'] = 'Well done, this was a hard quiz and you nailed it! Here are your premium courses!'
    response['Score'] = event["Score"]
    
    csv_file = f's3://' + courses_bucket_name + '/' + s3_courses_csv_file_name
    df = wr.s3.read_csv(csv_file)
    response['Courses'] = df.to_dict()

    return response