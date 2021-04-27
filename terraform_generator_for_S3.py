import terrascript
import terrascript.provider as provider
import terrascript.resource as resource

def terraform_s3(data):

    aws_access_key_id = data["aws_access_key_id"]
    aws_secret_access_key = data["aws_secret_access_key"]
    region = data["location"]
    bucket_name = data["s3_name"]
    acl = data["s3_acl"]
  
    config = terrascript.Terrascript()

    config += provider.aws(access_key = aws_access_key_id,secret_key = aws_secret_access_key, region=region)
    config += terrascript.resource.aws_s3_bucket(
        bucket_name,
        bucket= bucket_name,
        acl= acl,
           )

    with open('config.tf.json', 'wt') as fp:
        fp.write(str(config))
