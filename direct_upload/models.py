from direct_upload.db import db


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    content_type = db.Column(db.String())
