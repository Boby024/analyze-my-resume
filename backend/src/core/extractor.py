import io
from PyPDF2 import PdfReader
from docx import Document


class TextExtractor:
    content: bytes
    content_type: str
    text_raw: None
    result = {"title": None, "keywords": [], "text_raw": None, "text": None} # keys: keywords, title and text (cleaned)

    def __init__(self, content_type: str, content: bytes):
        self.content_type = content_type
        self.content = content


    def extractor_pdf(self) -> str:
        try:
            with io.BytesIO(self.content) as pdf_file:
                reader = PdfReader(pdf_file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() or ''
                return text
        except Exception as e:
            return f"Error extracting PDF text: {e}"


    def extractor_word(self) -> str:
        try:
            with io.BytesIO(self.content) as word_file:
                doc = Document(word_file)
                text = '\n'.join([para.text for para in doc.paragraphs])
                return text
        except Exception as e:
            return f"Error extracting Word text: {e}"


    def process_text(self):
        """
            Cleaning using NLP
            Keywords extraction
        """
        return self.result


    def extract(self):
        if "pdf" in self.content_type:
            self.text_raw = self.extractor_pdf()
        elif "doc" in self.content_type or "docx" in self.content_type:
            self.text_raw = self.extractor_word()
        else:
            self.text = None # "Unsupported file type"

        return self.process_text()
