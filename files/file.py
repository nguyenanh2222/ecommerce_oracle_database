import os
from fastapi import APIRouter, UploadFile

from project.schemas import DataResponse
from service.admin.product import ProductService

router = APIRouter()


class FileLoad():
    @router.post(
        path="/",
        response_model=DataResponse
    )
    async def create_upload_file(self, file: UploadFile):
        product = ProductService().create_upload_file_service(file=file)
        try:
            os.mkdir("../files")
        except Exception as e:
            print(e)
        file_name = os.getcwd() + "/files/" + file.filename.replace(" ", "-")
        with open(file_name, 'wb+') as f:
            f.write(file.file.read())
            f.close()
        return DataResponse(data={'file_name': file.filename})

