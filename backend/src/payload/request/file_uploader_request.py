class FileUploaderRequest:
    user_id: str
    filename: str
    content_type: str
    content: any

    def __init__(self, filename, content_type, content):
        self.filename = filename
        self.content_type = content_type
        self.content = content
        
    def dict(self):
        return {
            "user_id": self.user_id,
            "filename": self.filename,
            "content_type": self.content_type,
            "content": self.content
        }

class FileFilterRequest:
    query = ""
    page = 0
    size = 10
    order = "asc"

    def __init__(self, query, page, size, order):
        self.query = str(query).strip().lower()
        self.page = int(page)
        self.size = int(size)
        self.order = order

    def dict(self):
        return {
            "query": self.query,
            "page": self.page,
            "size": self.size
        }
