import os

from boto3 import Session


def __get_s3_client():
    session = Session(
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )

    return session.client('s3')


def get_object_url(key):
    return __get_s3_client().generate_presigned_url(
        'get_object',
        Params={
            'Bucket': os.environ.get('AWS_BUCKET'),
            'Key': key
        }
    )


def get_presigned_post(key, content_type):
    return __get_s3_client().generate_presigned_post(
        Bucket=os.environ.get('AWS_BUCKET'),
        Key=key,
        Fields={'Content-Type': content_type},
        Conditions=[
            {'Content-Type': content_type}
        ]
    )
