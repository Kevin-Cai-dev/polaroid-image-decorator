from io import BytesIO
from fastapi import APIRouter, UploadFile, Form
from controllers.image_controller import generate_image

router = APIRouter(prefix="/images")


@router.post("/generate/")
def modify_image(
    file: UploadFile,
    even_border: bool = Form(),
    border_width_key: str = Form(),
    aspect_ratio_key: str = Form(),
) -> BytesIO:
    """POST endpoint to generate new polaroid-esque image

    Args:
        file (UploadFile): input image
        even_border (bool, optional): equal borders check. Defaults to Form().
        border_width_key (str, optional): specified border thickness, provided
        as a key. Defaults to Form().
        aspect_ratio_key (str, optional): specified aspect ratio, provided as a key. Defaults to Form().

    Returns:
        BytesIO: generated image, as bytes
    """
    img_bytes = generate_image(
        file.file, even_border, border_width_key, aspect_ratio_key
    )
    return img_bytes
