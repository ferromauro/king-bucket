#! usr/bin/
import logging
import boto3
from botocore.exceptions import ClientError
from kb_settings import settings

# Logging Level configuration
logging.basicConfig(level=logging.INFO)

class KingBucket():
    def __init__(self):
        self.s3 = boto3.resource('s3',  aws_access_key_id = settings.ACCESS_KEY, aws_secret_access_key = settings.SECRET_KEY)
        
    def create_bucket(self, name):
        try:
            location = {'LocationConstraint': settings.REGION}
            self.s3.create_bucket(Bucket=name, CreateBucketConfiguration=location)
            logging.info(f'\tBucket "{name}" created.')
        except ClientError as e:
            logging.error(e)

    def delete_bucket(self, name):
        try:
            self.s3.Bucket(name).delete()
            logging.info(f'\tBucket "{name}" deleted.')
        except ClientError as e:
            logging.error(e)