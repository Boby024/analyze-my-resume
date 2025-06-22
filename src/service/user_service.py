from src.payload.request.user_register_request import UserRegisterRequest, UserLoginRequest
from src.model.user_model import User
from ..app import db
from ..utils.log import Logger
from src.config import Config
from flask_mail import Message
from ..extensions import mail
from src.payload.response.auth_response import AuthResponse
from ..utils.auth_security import generate_token
from ..utils import helper
from datetime import datetime, date



logger = Logger(name=__name__, log_file=Config.log_path)
JWT_ACCESS_TOKEN_EXPIRES = Config.JWT_ACCESS_TOKEN_EXPIRES


def register(data: UserRegisterRequest):
    # check if email not exist
    user_found = User.query.filter_by(email=data.email).first()
    if user_found is not None:
        return None

    new_user = User()
    new_user.email = data.email
    new_user.password = data.password
    new_user.username = data.username
    new_user.firstname = data.firstname
    new_user.lastname = data.lastname
    new_user.role = "USER"
    new_user.set_password(data.password)
    db.session.add(new_user)
    db.session.commit()

    exp = helper.get_dt_utcnow() + JWT_ACCESS_TOKEN_EXPIRES
    token = generate_token(user=new_user, exp=exp)
    result = AuthResponse(id=new_user.id, email=new_user.email, username=new_user.username, token=token, msg_="")

    # # Send verification mail
    # email_sent = send_email_verification(receiver=new_user.email, name=new_user.firstname)
    # if email_sent:
    #     result.msg = "email sent"
    # else:
    #     result.msg = "email not sent"
    return result


def login(data: UserLoginRequest):
    user = User.query.filter_by(email=data.email).first()

    # Validate password using secret key
    if user and user.verify_password(data.password):
        exp = helper.get_dt_utcnow() + JWT_ACCESS_TOKEN_EXPIRES
        token = generate_token(user=user, exp=exp)
        result = AuthResponse(id=user.id, email=user.email, username=user.username, token=token, msg_="")
        return result
    return None


def verify_email(data):
    email = data["email"]
    code = data["code"]
    user = User.query.filter_by(email=data.email).first()
    if user:
        email_verifications = EmailVerification.query.filter_by(email=email).first()
        pass


def get_users():
    return User.query.all()


def send_email_verification(receiver, name):
    email_verification_code = helper.generate_verification_code(10)
    subject = Config.MAIL_EMAIL_VERIFICATION_SUBJECT
    sender = Config.MAIL_USERNAME
    # content = Config.MAIL_EMAIL_VERIFICATION_CONTENT
    content = content = helper.read_file(Config.MAIL_EMAIL_VERIFICATION_CONTENT_PATH_DEV)
    receiver = str(receiver).strip()
    body = content.replace("sender_info_surname", name).replace("email_verification_code", email_verification_code)
    status = False
    try:
        msg = Message(subject=subject,
                      sender=sender,
                      recipients=[receiver])
        msg.body = body
        mail.send(msg)
    except Exception as e:
        print(e)
        pass

    if status:
        return True
    return False
