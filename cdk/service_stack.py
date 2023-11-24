from aws_cdk import (
    # Duration,
    Aspects,
    Stack,
    Tags
    # aws_sqs as sqs,
)
from cdk_nag import AwsSolutionsChecks
from constructs import Construct

from cdk.service.constants import OWNER_TAG, SERVICE_NAME, SERVICE_NAME_TAG
from cdk.service.s3_construct import S3Construct
from cdk.service.utils import get_username

class ServiceStack(Stack):
    """_summary_

    Args:
        Stack (_type_): _description_
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self._add_stack_tags()
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "UniversalProfileServiceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        
        self.s3 = S3Construct(
            self,
            id_='universal-profile-service',
            appconfig_app_name='universal-profile-service',
            is_production_env=False
        )
        
        # add security check
        self._add_security_tests()

    def _add_stack_tags(self) -> None:
        # best practice to help identify resources in the console
        Tags.of(self).add(SERVICE_NAME_TAG, SERVICE_NAME)
        Tags.of(self).add(OWNER_TAG, get_username())

    def _add_security_tests(self) -> None:
        Aspects.of(self).add(AwsSolutionsChecks(verbose=True))
        # Suppress a specific rule for this resource
