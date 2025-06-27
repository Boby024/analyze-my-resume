import io
from PyPDF2 import PdfReader
from docx import Document
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from keybert import KeyBERT

class TextExtractor:
    content: bytes
    title: str
    content_type: str
    text_raw: None
    result = {"title": None, "keywords": [], "text_raw": None, "text": None} # keys: keywords, title and text (cleaned)

    def __init__(self, content_type: str, content: bytes, title=""):
        self.content_type = content_type
        self.content = content
        self.title = title
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.keyword_model = KeyBERT('sentence-transformers/all-MiniLM-L6-v2')


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


    def process_text(self, raw_text: str, top_n: int = 10):
        """
        Clean text using NLTK and extract keywords using KeyBERT (Transformer-based).
        """
        try:
            # Tokenize, lowercase, remove stopwords and punctuation
            raw_text = self.title + " " + raw_text
            tokens = nltk.word_tokenize(raw_text)
            tokens = [
                self.lemmatizer.lemmatize(word.lower())
                for word in tokens
                if word.isalpha() and word.lower() not in self.stop_words
            ]
            cleaned_text = ' '.join(tokens)

            # Extract keywords using KeyBERT (unsupervised + BERT)
            keywords = self.keyword_model.extract_keywords(cleaned_text, top_n=top_n)
            keywords_only = [kw[0] for kw in keywords]

            return {
                "title": self.title,
                "text_raw": self.text_raw,
                "text": cleaned_text,
                "keywords": keywords_only
            }
        except Exception as e:
            print(e)
            return None


    def extract(self):
        if "pdf" in self.content_type:
            self.text_raw = self.extractor_pdf()
        elif "doc" in self.content_type or "docx" in self.content_type:
            self.text_raw = self.extractor_word()
        else:
            self.text = None # "Unsupported file type"

        return self.process_text(raw_text=self.text_raw)
