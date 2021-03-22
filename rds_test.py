import boto3


def create_rds(data):
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

    rds = boto3.client("rds", aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key, region_name=region)

    response = rds.create_db_instance(DBInstanceIdentifier=db_identifier,
                                      AllocatedStorage=AllocatedStorage,
                                      DBName=DBName,
                                      Engine=Engine,
                                      # General purpose SSD
                                      StorageType=StorageType,
                                      StorageEncrypted=False,
                                      AutoMinorVersionUpgrade=True,
                                      # Set this to true later?
                                      MultiAZ=False,
                                      MasterUsername=MasterUsername,
                                      MasterUserPassword=MasterUserPassword,
                                      DBInstanceClass=DBInstanceClass
                                      )
    return(response)
