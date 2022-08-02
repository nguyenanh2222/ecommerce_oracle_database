from fastapi import UploadFile

from repo.file import FileRepo


class FileService():

    def create_upload_file_service(self, file: UploadFile):
        product = FileRepo().create_upload_file_repo(file=file)