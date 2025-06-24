from .user_route import user_bp
from .file_route import file_bp
from .analyzer_route import analyzer_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix="/api/account")
    app.register_blueprint(file_bp, url_prefix="/api/file")
    app.register_blueprint(analyzer_bp, url_prefix="/api/analyzer")
