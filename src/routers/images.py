from fastapi import APIRouter

router = APIRouter()


@router.get("/image")
def image():
    return "TODO"
