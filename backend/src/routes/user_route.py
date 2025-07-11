from flask import Blueprint, request
from ..utils.log import Logger
from src.config import Config
from src.payload.request.user_register_request import UserRegisterRequest, UserLoginRequest
from ..service import user_service
from ..payload.response import response
from ..utils.auth_security import token_required


user_bp = Blueprint("user", __name__)
logger = Logger(name=__name__, log_file=Config.log_path)


@user_bp.route('/register', methods=['POST'])
def create_user():
    auth_resp = None
    try:
        data = request.get_json()
        urr = UserRegisterRequest(**data)
        auth_resp = user_service.register(urr)

        if auth_resp is None:
            return response.response_msg("Email already used OR Invalid credentials!", 400)
    except Exception as e:
        print(e)
        return response.response_msg("Missing Attributes: username, password, email, firstname, lastname", 400)

    if auth_resp:
        return response.response_data(auth_resp.serialize(), 201)
    response.response_msg("Internal Server Error", 500)


@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        ulr = UserLoginRequest(**data)
        login_response = user_service.login(ulr)
        if login_response:
            return response.response_data(login_response.serialize(), 200)
        else:
            return response.response_msg("Invalid credentials!", 400)
    except Exception as e:
        print(e)
        return response.response_msg("Internal Server Error!", 500)


@user_bp.route('/users', methods=['GET'])
@token_required
def get_users(user):
    try:
        logger.info("list of all users")
        users = user_service.get_users()
        return response.response_data(data=users, code=200, serialized=True)
    except Exception as e:
        print(e)
        return response.response_msg("Internal Server Error", 500)

