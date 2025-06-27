from src.model.file_model import FileModel
from src.model.file_processed_model import FileProcessedModel, FileProcessedRequest
from src.model.file_job_detail_model import FileJobDetailModel, FileJobDetailRequest
from src.extensions import db
from src.core import extractor


def save_job_detail(fjdr: FileJobDetailRequest):
    fjdm = FileJobDetailModel(
        title=fjdr.title,
        description=fjdr.description,
        user_id=fjdr.user_id,
        file_id=fjdr.file_id
    )
    db.session.add(fjdm)
    db.session.commit()

    if fjdm:
        return fjdm
    return None


def save_file_processed(fpr: FileProcessedRequest):
    fpm = FileProcessedModel(
        title=fpr.title,
        description=fpr.description,
        user_id=fpr.user_id,
        file_id=fpr.file_id
    )
    db.session.add(fpm)
    db.session.commit()

    if fpm:
        return fpm
    return None


def start(fjdr: FileJobDetailRequest):
    fjd = save_job_detail(fjdr)

    file = FileModel.query.filter_by(id=fjdr.file_id).first()
    if file:
        fp_result = extractor.TextExtractor(content_type=file.content_type, content=file.content, title=fjd.title).extract()

        # save file detail after Text extraction, keywords extraction
        fpr = FileProcessedRequest(title=fp_result["title"],
                                   keywords=fp_result["keywords"],
                                   text_raw=fp_result["text_raw"],
                                   text=fp_result["text"],
                                   file_id=fjdr.file_id
                                )
        fpm_saved = save_file_processed(fpr)
    
        if fjd and fpm_saved:
            # Generate suggestions for resume improvement
            pass
