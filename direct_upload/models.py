from direct_upload.db import db
from direct_upload.helpers import get_object_url


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    content_type = db.Column(db.String())

    @property
    def url(self):
        return get_object_url(self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'content_type': self.content_type,
            'url': self.url
        }
