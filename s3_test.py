import boto3


def create_s3(data):
    aws_access_key_id = data["aws_access_key_id"]
    aws_secret_access_key = data["aws_secret_access_key"]
    region = data["location"]
    bucket_name = data["s3_name"]
    acl = data["s3_acl"]
    s3 = boto3.client("s3", aws_access_key_id= aws_access_key_id,
                      aws_secret_access_key= aws_secret_access_key, region_name= region)
    response = s3.create_bucket(
        ACL=acl,
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        },

    )
    return(response["Location"])

