from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_s3 as s3,
)

class S3Construct(Construct):

    def __init__(self, scope: Construct, id_: str, appconfig_app_name: str, is_production_env: bool) -> None:
        super().__init__(scope, id_)
        self.id_ = id_
        self.access_logs_bucket = self._build_access_logs_bucket()
        self.temp_bucket = self._build_temp_bucket()


    def _build_access_logs_bucket(self) -> s3.Bucket:
        return s3.Bucket(
            self,
            id=f'{self.id_}-access-logs-bucket',
            bucket_name=f'{self.id_}-access-logs-bucket',
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
            public_read_access=False,
            removal_policy=RemovalPolicy.RETAIN,
            versioned=True,
            enforce_ssl=True
        )

    def _build_temp_bucket(self) -> s3.Bucket:
        return s3.Bucket(
            self,
            id=f'{self.id_}-temp-bucket',
            bucket_name=f'{self.id_}-temp-bucket',
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
            public_read_access=False,
            removal_policy=RemovalPolicy.RETAIN,
            server_access_logs_bucket=self.access_logs_bucket,
            server_access_logs_prefix='temp-bucket/serverAccessLogging_',
            versioned=False,
            enforce_ssl=True
        )

    def add_event_notification(self, event, destination):
        """ Add event notification to temp bucket """
        self.temp_bucket.add_event_notification(event, destination)
