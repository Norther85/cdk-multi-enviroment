from aws_cdk import core as cdk
import aws_cdk.aws_s3 as _s3
import aws_cdk.aws_ec2 as _ec2

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkMultiEnviromentStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        prod_confs = self.node.try_get_context('envs')['dev']
        print(prod_confs)
        # The code that defines your stack goes here
        if is_prod:
            vpc = _ec2.Vpc(self, "MyVPCPROD",
                           cidr="10.0.0.0/16"
                           )
            tag_vpc = core.Tags.of(vpc).add("Owner", "Tomasz Czekaj")
        else:
            vpc = _ec2.Vpc(self, "MyVPCDEV",
                           cidr="10.0.0.0/16"
                           )
        # Importing existing resources
        # bucket_imported = _s3.Bucket.from_bucket_name(self, "MyImportedBucket",
        #                             "bucket_name_to_import"
        #                             )
