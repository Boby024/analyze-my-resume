from flask import Blueprint, request
from ..utils.log import Logger
from src.config import Config
from src.model.file_job_detail_model import FileJobDetailRequest
from ..service import analyzer_service
from ..payload.response import response
from ..utils.auth_security import token_required


analyzer_bp = Blueprint("analyzer", __name__)
logger = Logger(name=__name__, log_file=Config.log_path)


@analyzer_bp.route('/start', methods=['POST'])
@token_required
def start(user):
    try:
        data = request.get_json()
        fjdr = FileJobDetailRequest(**data)
        fjdr.user_id = user.id

        result = analyzer_service.start(fjdr)
        return response.response_data(data=result, code=200, serialized=False)
    except Exception as e:
        print(e)
        return response.response_msg("Internal Server Error", 500)
