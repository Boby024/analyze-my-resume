from src.model.file_model import FileModel
from src.extensions import db
from src.payload.request.file_uploader_request import FileUploaderRequest, FileFilterRequest
from sqlalchemy import or_, asc, desc


def upload_file(fur: FileUploaderRequest):
    uploaded_file = FileModel(
        filename=fur.filename,
        content_type=fur.content_type,
        content=fur.content,
        user_id=fur.user_id
    )
    db.session.add(uploaded_file)
    db.session.commit()
    
    if uploaded_file:
        return uploaded_file
    return None


def get_file(user_id: str, id: str):
    file = FileModel.query.filter_by(user_id=user_id, id=id).first()
    if file is None:
        return None
    return file


def delete_file(user_id: str, id: str):
    file = FileModel.query.filter_by(user_id=user_id, id=id).first()
    if file is None:
        return False

    db.session.delete(file)
    db.session.commit()
    return True


def get_files(user_id: str):
    files = FileModel.query.filter_by(user_id=user_id).all()
    data = [file.serialize() for file in files]
    return data


def filter_files(file_filter_request: FileFilterRequest):
    # Build query
    filename = file_filter_request.query
    content_type = file_filter_request.query
    page = file_filter_request.page
    size = file_filter_request.size
    order = file_filter_request.order

    query = FileModel.query
    filters = []

    if filename:
        filters.append(FileModel.filename.ilike(f'%{filename}%'))
    if content_type:
        filters.append(FileModel.content_type.ilike(f'%{content_type}%'))

    if filters:
        query = query.filter(or_(*filters))

    # Sorting
    if order == 'asc':
        query = query.order_by(asc(FileModel.created_at))
    elif order == 'desc':
        query = query.order_by(desc(FileModel.created_at))
    else:
        query = query.order_by(FileModel.created_at)

    # Apply pagination
    pagination = query.paginate(page=page, per_page=size, error_out=False)

    # Serialize results
    results = [item.serialize() for item in pagination.items]

    # Return response
    return {
        'total': pagination.total,
        'pages': pagination.pages,
        'page': pagination.page,
        'results': results
    }
