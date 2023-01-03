from fastapi import APIRouter, UploadFile, Form, Response
from controllers.image_controller import generate_image

router = APIRouter(prefix="/images")


@router.post(
    "/generate",
    responses={200: {"content": {"image/jpeg": {}}}},
    response_class=Response,
)
def modify_image(
    file: UploadFile,
    even_border: bool = Form(),
    border_width_key: str = Form(),
    aspect_ratio_key: str = Form(),
) -> Response:
    """POST endpoint to generate new polaroid-esque image

    Args:
        file (UploadFile): input image
        even_border (bool, optional): equal borders check. Defaults to Form().
        border_width_key (str, optional): specified border thickness, provided
        as a key. Defaults to Form().
        aspect_ratio_key (str, optional): specified aspect ratio, provided as a key. Defaults to Form().

    Returns:
        Response: generated image, as bytes
    """
    img_bytes = generate_image(
        file.file, even_border, border_width_key, aspect_ratio_key
    )
    return Response(content=img_bytes, media_type="image/jpeg")
