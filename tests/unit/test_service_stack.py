import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.service_stack import ServiceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in universal_profile_service/universal_profile_service_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServiceStack(app, "universal-profile-service")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
