from fastapi import HTTPException

BAD_PARAMETERS = HTTPException(status_code=400, detail="Invalid image params")

BAD_IMAGE = HTTPException(
    status_code=400, detail="Something went wrong trying to open the file provided"
)

UNKNOWN_EXCEPTION = HTTPException(status_code=400, detail="Something went wrong")
