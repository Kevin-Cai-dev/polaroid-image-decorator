from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/images")


@router.post("/generate/")
async def modify_image(file: UploadFile = File(...)):
    return {"filename": file.filename}
