from aws_cdk import core as cdk
import aws_cdk.aws_s3 as _s3

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkMultiEnviromentStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        if is_prod:
            bucket = _s3.Bucket(self, "MyProdBucket",
            versioned = True
            )
        else:
            bucket = _s3.Bucket(self, "MyDevBucket")
