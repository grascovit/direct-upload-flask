from flask_restful import Api

from direct_upload.resources.v1.document import DocumentsV1

api = Api()
api.add_resource(DocumentsV1, '/api/v1/documents')
