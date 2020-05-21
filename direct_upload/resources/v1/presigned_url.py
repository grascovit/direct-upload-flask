import os

from boto3 import Session
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('content_type', type=str)


class PresignedUrlV1(Resource):
    def post(self):
        args = parser.parse_args()
        session = Session(
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
        client = session.client('s3')
        presigned_post_data = client.generate_presigned_post(
            Bucket=os.environ.get('AWS_BUCKET'),
            Key=args['name'],
            Fields={'Content-Type': args['content_type']},
            Conditions=[
                {'Content-Type': args['content_type']}
            ]
        )

        return presigned_post_data
