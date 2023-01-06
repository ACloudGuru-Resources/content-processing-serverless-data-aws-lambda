import boto3
import awswrangler as wr

lessons_bucket_name = 'guru-rewards-datafeed'
s3_lessons_csv_file_name = 'guru-premium-lessons/premium-lessons.csv'

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    print('Received event from Step Functions')
    print(event)
    response = {}
    response ['Message'] = "You didn't pass. Don't worry! Practice makes perfect. Here are premium lessons to keep you going!"
    response['Score'] = event["Score"]
    
    csv_file = f's3://' + lessons_bucket_name + '/' + s3_lessons_csv_file_name
    df = wr.s3.read_csv(csv_file)
    response['Lessons'] = df.to_dict()

    return response