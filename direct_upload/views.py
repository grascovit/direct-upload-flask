from time import time

from flask import Blueprint, flash, redirect, render_template, request, url_for

from direct_upload import Document, db
from direct_upload.helpers import upload_file

blueprint = Blueprint('direct_upload', __name__)
document_blueprint = Blueprint('document', __name__, url_prefix='/documents')


@blueprint.route('/')
def index():
    return render_template('index.html')


@document_blueprint.route('/new')
def new():
    return render_template('documents/new.html')


@document_blueprint.route('/create', methods=['POST'])
def create():
    start = time()

    for file in request.files.getlist('files'):
        upload_file(file)
        document = Document(name=file.filename, content_type=file.headers['Content-Type'])
        db.session.add(document)
        db.session.commit()

    flash('Finished in {:.2f}s'.format(time() - start))

    return redirect(url_for('direct_upload.index'))
