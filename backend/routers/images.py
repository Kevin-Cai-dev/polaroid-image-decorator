from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel

from controllers.image_controller import open_image

router = APIRouter(prefix="/images")


class Params(BaseModel):
    evenBorder: bool
    borderWidth: str
    aspectRatio: str


@router.post("/generate/")
def modify_image(file: UploadFile = File(None), params: str = Form()):
    open_image(file.file)
    return "OK"
