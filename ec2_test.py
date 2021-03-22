import boto3


def create_ec2(data):
    aws_access_key_id = data["aws_access_key_id"]
    aws_secret_access_key = data["aws_secret_access_key"]
    region = data["location"]
    imageid = data["ec2_image_id"]
    instance = data["ec2_image_id"]
    ec2_client = boto3.client("ec2", aws_access_key_id= aws_access_key_id,
                              aws_secret_access_key= aws_secret_access_key, region_name=region)
    instances = ec2_client.run_instances(

        ImageId=imageid,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance,

    )

    return (instances["Instances"][0])


