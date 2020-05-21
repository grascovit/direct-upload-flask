from flask_restful import Resource, reqparse

from direct_upload.db import db
from direct_upload.models import Document

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('content_type', type=str)


class DocumentsV1(Resource):
    def post(self):
        args = parser.parse_args()
        document = Document(name=args['name'], content_type=args['content_type'])
        db.session.add(document)
        db.session.commit()

        return document.to_json()
