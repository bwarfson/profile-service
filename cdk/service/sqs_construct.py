""" CDK Construct for SQS """
from aws_cdk import (
    Duration,
    aws_sqs as sqs,
)
from constructs import Construct


class SQSConstruct(Construct):
    """ CDK Construct for SQS """
    def __init__(self, scope: Construct, id_: str) -> None:
        super().__init__(scope, id_)
        self.dead_letter_queue = self.build_dead_letter_queue(id_)
        self.queue = self.build_queue(id_)

    def build_dead_letter_queue(self, id_: str) -> sqs.DeadLetterQueue:
        """ Build SQS Dead Letter Queue """
        return sqs.Queue(
            self,
            f'{id_}-dead-letter-queue',
            encryption=sqs.QueueEncryption.SQS_MANAGED,
            retention_period=Duration.days(14),
            enforce_ssl=True,
        )

    def build_queue(self, id_: str) -> sqs.Queue:
        """ Build SQS Queue """
        return sqs.Queue(
            self,
            id=f'{id_}',
            encryption=sqs.QueueEncryption.SQS_MANAGED,
            enforce_ssl=True,
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=3,
                queue=self.dead_letter_queue,
            )
        )
