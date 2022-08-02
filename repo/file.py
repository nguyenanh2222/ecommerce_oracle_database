from fastapi import UploadFile
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Sku


class FileRepo():
    def create_upload_file_repo(self, file: UploadFile):
        session: Session = SessionLocal()
        stmt = insert(Sku).values(images=file.filename)
        session.execute(stmt)
        session.commit()