from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from ..config import Config
from ..utils import helper

PASSWORD_SECRET_KEY = Config.PASSWORD_SECRET_KEY


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    lastname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=helper.get_dt_utcnow())
    updated_at = db.Column(db.DateTime, nullable=True)
    is_email_verified = db.Column(db.Boolean, default=False, nullable=False)
    role = db.Column(db.String(120), nullable=True)
    email_verifications = db.Column(db.Boolean, default=False, nullable=True)

    def set_password(self, plaintext_password):
        salted_password = plaintext_password + PASSWORD_SECRET_KEY  # Add secret key to password
        self.password = generate_password_hash(salted_password)

    def verify_password(self, plaintext_password):
        salted_password = plaintext_password + PASSWORD_SECRET_KEY  # Add secret key to password
        return check_password_hash(self.password, salted_password)

    def serialize(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
        }
