from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.types import JSON
import uuid


class FileProcessedModel(db.Model):
    __tablename__ = 'file_processed'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(555), nullable=True)
    keywords = db.Column(JSON, nullable=False) #  for other DB like SQLite or MySQL
    # keywords = db.Column(ARRAY(db.String), nullable=False) # only for PostgreSQL
    text_raw = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    file_id = db.Column(UUID(as_uuid=False))

    def serialize(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "keywords": self.keywords,
            "text": self.text,
            "created_at": self.created_at
        }



class FileProcessedRequest:
    keywords: any
    title: str
    text_raw: str
    text: str
    file_id: str

    def __init__(self, keywords, title, text_raw, text, file_id):
        self.keywords = keywords
        self.title = title
        self.text_raw = text_raw
        self.text = text
        self.file_id = file_id
        
    def dict(self):
        return {
            "keywords": self.keywords,
            "title": self.title,
            "text": self.text,
            "file_id": self.file_id
        }
