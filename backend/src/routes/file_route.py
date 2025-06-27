from flask import Blueprint, request
from werkzeug.utils import secure_filename
from ..utils.log import Logger
from src.config import Config
from ..payload.response import response
from ..utils.auth_security import token_required
from src.payload.request.file_uploader_request import FileUploaderRequest, FileFilterRequest
from ..service import file_service
from flask import send_file
import io


file_bp = Blueprint("upload_file", __name__)
logger = Logger(name=__name__, log_file=Config.log_path)
ALLOWED_EXTENSIONS_FILE = Config.ALLOWED_EXTENSIONS_FILE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_FILE


@file_bp.route('/upload', methods=['POST'])
@token_required
def upload_file(user):
    if 'file' not in request.files:
        return response.response_msg("No file part in request", 400)

    file = request.files['file']
    if file.filename == '':
        return response.response_msg("No selected file", 400)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        content_type = file.content_type
        file_data = file.read()  # read binary content

        fur = FileUploaderRequest(filename=filename, content_type=content_type, content=file_data)
        fur.user_id = user.id
        file_uploaded = file_service.upload_file(fur)

        if file_uploaded:
            return response.response_data(data={"id": str(file_uploaded.id)}, code=201, serialized=False)
        else:
            return response.response_msg("Missing Attribute!", 400)
    return response.response_msg("Invalid file type", 400)


@file_bp.route('/single', methods=['GET'])
@token_required
def get_uploaded_file(user):
    id = request.args.get('id')
    user_id = user.id
    file_record = file_service.get_file(user_id, id)
    if not file_record:
        return response.response_msg("File not found", 404)

    try:
        data = send_file(
            io.BytesIO(file_record.content),
            as_attachment=True,  # Set to False to preview inline (e.g., PDF in browser)
            download_name=file_record.filename,
            mimetype=file_record.content_type
        )
        return data
    except Exception as e:
        return response.response_msg(str(e), 400)


@file_bp.route('/delete', methods=['GET'])
@token_required
def delete_file(user):
    try:
        user_id = user.id
        id = request.args.get("id")
        is_deleted = file_service.delete_file(user_id, id)

        if is_deleted is False:
            return response.response_msg("File does not exist", 404)
        else:
            return response.response_msg("File deleted successfully", 200)
    except Exception as e:
        print(e)
    return response.response_msg("Internal Server Error!", 400)


@file_bp.route('/pagination', methods=['GET'])
@token_required
def filter_campaign(user):
    try:
        params = request.args.to_dict()
        ffr = FileFilterRequest(**params)
        files = file_service.filter_files(ffr)
        return response.response_data(data=files, code=200, serialized=False)
    except Exception as e:
        print(e)
        return response.response_msg("Internal Server Error", 500)
