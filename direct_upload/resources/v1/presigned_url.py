from flask_restful import Resource, reqparse

from direct_upload.helpers import get_presigned_post

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('content_type', type=str)


class PresignedUrlV1(Resource):
    def post(self):
        args = parser.parse_args()

        return get_presigned_post(args['name'], args['content_type'])
