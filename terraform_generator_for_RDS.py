import terrascript
import terrascript.provider
import terrascript.resource

def terraform_rds(data):

    aws_access_key_id = data["aws_access_key_id"]
    aws_secret_access_key = data["aws_secret_access_key"]
    region = data["location"]
    db_identifier = data["rds_instance_identifier"]
    AllocatedStorage = data['rds_allocated_storage']
    DBName = data['rds_db_name']
    Engine = data['rds_engine_name']
    DBInstanceClass = data['rds_instance_class']
    MasterUsername = data['rds_master_username']
    MasterUserPassword = data['rds_master_password']
    StorageType = data['rds_storage_type']

    config = terrascript.Terrascript()

    # AWS provider
    config += terrascript.provider.aws( access_key = aws_access_key_id, secret_key = aws_secret_access_key, 
                                        region=region)


    # AWS EC2 instance referencing the variable.
    config += terrascript.resource.aws_db_instance(
        "rds",
        identifier=db_identifier,
        allocated_storage=20,
        rds_name=DBName,
        engine=Engine,
        storage_type=StorageType,
        storage_encrypted=False,
        aulti_az=False,
        username=MasterUsername,
        password=MasterUserPassword,
        instance_class=DBInstanceClass
    )
    

    with open('config.tf.json', 'wt') as fp:
        fp.write(str(config))
