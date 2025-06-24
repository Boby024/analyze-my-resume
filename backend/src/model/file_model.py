from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import BYTEA
import uuid, io
import pandas as pd
# from ..utils import helper
# from ..config import Config


class FileModel(db.Model):
    __tablename__ = 'files'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String(256), nullable=False)
    content_type = db.Column(db.String(128), nullable=False)
    content = db.Column(BYTEA, nullable=False)  # store as BLOB
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(UUID(as_uuid=False))

    def serialize(self):
        return {
            "id": str(self.id),
            "filename": self.filename,
            "content_type": self.content_type,
            "created_at": self.created_at
        }

    def serialize_blob(self):
        return {
            "id": str(self.id),
            "filename": self.filename,
            "content_type": self.content_type,
            "content": self.content
        }


    # def process_file(self):
    #     """
    #     Placeholder for logic to extract text from PDFs or Word files.
    #     You can implement this using packages like PyPDF2, pdfplumber, or python-docx.
    #     """
    #     ext = self.filename.rsplit('.', 1)[-1].lower()

    #     if ext == 'pdf':
    #         # Process PDF content (e.g., with pdfplumber or PyPDF2)
    #         return "PDF processing not implemented yet"
    #     elif ext in ['doc', 'docx']:
    #         # Process Word content (e.g., with python-docx)
    #         return "Word processing not implemented yet"
    #     else:
    #         return "Unsupported file type"
