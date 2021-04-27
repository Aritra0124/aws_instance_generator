import terrascript
import terrascript.provider
import terrascript.resource

def terraform_ec2():

    aws_access_key_id = data["aws_access_key_id"]
    aws_secret_access_key = data["aws_secret_access_key"]
    region = data["location"]
    ImageId = data["ec2_image_id"]
    instance = data["ec2_instance"]

    config = terrascript.Terrascript()

    # AWS provider
    config += terrascript.provider.aws(access_key = aws_access_key_id,secret_key = aws_secret_access_key, region=region)


    # AWS EC2 instance referencing the variable.
    config += terrascript.resource.aws_instance(
        "example",
        instance_type=instance,
        ami=ImageId,
    )

    with open('config.tf.json', 'wt') as fp:
        fp.write(str(config))
