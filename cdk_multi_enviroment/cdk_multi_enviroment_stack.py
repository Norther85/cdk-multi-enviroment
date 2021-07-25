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

        # The code that defines your stack goes here
        if is_prod:
            # user data script
            with open("bootstrap_scripts/install.sh", mode="r") as file:
                user_data = file.read()

            print(user_data)

            vpc = _ec2.Vpc.from_lookup(self, "MyVPC", is_default=True)
            ec2 = _ec2.Instance(self, "MyInstance",
                                instance_type=_ec2.InstanceType(
                                    instance_type_identifier="t2.nano"),
                                vpc=vpc,
                                vpc_subnets=_ec2.SubnetSelection(
                                    subnet_type=_ec2.SubnetType.PUBLIC),
                                machine_image=_ec2.MachineImage.generic_linux(
                                    {"eu-west-1": "ami-058b1b7fe545997ae"}),
                                user_data=_ec2.UserData.custom(user_data)
                                )
            ec2.connections.allow_from_any_ipv4(
                _ec2.Port.tcp(80), description="Web traffic")

            ec2.instance.add_property_override(
                "BlockDeviceMappings", [
                    {
                        "DeviceName": "/dev/sdb",
                        "Ebs": {"VolumeSize": "8"}
                    }
                ]
            )
            # vpc = _ec2.Vpc(self, "MyVPCPROD",
            #                cidr="10.0.0.0/16"
            #                )
            # tag_vpc = core.Tags.of(vpc).add("Owner", "Tomasz Czekaj")
        else:
            vpc = _ec2.Vpc(self, "MyVPCDEV",
                           cidr="10.0.0.0/16"
                           )
        # Importing existing resources
        # bucket_imported = _s3.Bucket.from_bucket_name(self, "MyImportedBucket",
        #                             "bucket_name_to_import"
        #                             )
        # vpc2 = _ec2.Vpc.from_lookup(self, "importedVpc",
        # # is_default=True, or
        # vpc_id="vpc_id_to_import"
        # )
