from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class FileJobDetailModel(db.Model):
    __tablename__ = 'files_to_job_detail'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(555), nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    file_id = db.Column(UUID(as_uuid=True))
    user_id = db.Column(UUID(as_uuid=True))

    def serialize(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "file_id": str(self.file_id),
            "created_at": self.created_at
        }


class FileJobDetailRequest:
    user_id: str
    file_id: str
    title: str
    description: str

    def __init__(self, title, description, file_id):
        self.title = title
        self.description = description
        self.file_id = file_id
        
    def dict(self):
        return {
            "user_id": self.user_id,
            "file_id": self.file_id,
            "title": self.title,
            "description": self.description
        }
