import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0e38b48473ea57778',
     InstanceType='t2.micro',
     KeyName='demo'
 )