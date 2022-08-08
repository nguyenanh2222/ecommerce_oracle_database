import json

from fastapi import UploadFile
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Sku


class FileRepo():
    def create_upload_file_repo(self, file: UploadFile):
        session: Session = SessionLocal()
        image = json.dumps([{"name": f"{file.filename}"}])
        stmt = insert(Sku).values(images=image)
        session.execute(stmt)
        session.commit()
