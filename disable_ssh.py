import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

SECURITY_GROUP_ID = 'sg-0b92f94bb54aefc8e'   # replace(qatest-ec2-sg-name)

def remove_ssh():
    try:
        ec2.revoke_security_group_ingress(
            GroupId=SECURITY_GROUP_ID,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print("SSH access removed successfully")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    remove_ssh()