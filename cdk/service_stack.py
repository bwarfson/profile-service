from aws_cdk import (
    # Duration,
    Aspects,
    Stack,
    # aws_sqs as sqs,
)
from cdk_nag import AwsSolutionsChecks
from constructs import Construct

class ServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "UniversalProfileServiceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        # add security check
        self._add_security_tests()
        
    def _add_security_tests(self) -> None:
        Aspects.of(self).add(AwsSolutionsChecks(verbose=True))
        # Suppress a specific rule for this resource