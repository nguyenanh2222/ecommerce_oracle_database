import json

from fastapi import UploadFile
from sqlalchemy import insert
from sqlalchemy.orm import Session
from starlette import status
from starlette.exceptions import HTTPException

from database import SessionLocal
from model import Sku


class FileRepo():
    def create_upload_file_repo(self, file: UploadFile):
        session: Session = SessionLocal()
        filename = f"{file.filename}"
        end_file = filename[filename.find("."):]
        if end_file != '.png' \
                and end_file != '.jpg' \
                and end_file != '.jpeg' \
                and end_file != '.gif' \
                and end_file != '.webp':
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        image = json.dumps([{"name": filename}])
        stmt = insert(Sku).values(images=image)
        session.execute(stmt)
        session.commit()
