from io import BytesIO
from PIL import Image, ImageOps, ImageCms, UnidentifiedImageError
from typing import BinaryIO, Tuple, Union

from common.exceptions import BAD_IMAGE, BAD_PARAMETERS, UNKNOWN_EXCEPTION
from common.key_maps import EDGE_MAP, ASPECT_RATIO_MAP
from controllers.resize_controller import get_new_size
from models.aspect_ratio import AspectRatio


def generate_image(
    file: BinaryIO, even_borders: bool, border_width_key: str, aspect_ratio_key: str
) -> BytesIO:
    """Generates a polaroid-esque image for the given file

    Args:
        file (BinaryIO): input file
        even_borders (bool): equal sized borders check
        border_width_key (str): thinner edge width key
        aspect_ratio_key (str): aspect ratio key to retrieve matching aspect ratio

    Raises:
        BAD_PARAMETERS: provided params cannot be used to create the image
        BAD_IMAGE: something went wrong when opening the image
        UNKNOWN_EXCEPTION: general exception for unexpected errors

    Returns:
        BytesIO: generated image as bytes
    """
    border_size, aspect_ratio = validate_params(
        even_borders, border_width_key, aspect_ratio_key
    )
    try:
        old_img = ImageOps.exif_transpose(Image.open(file))
        old_size = old_img.size

        iccProfile = old_img.info.get("icc_profile")
        originalColourProfile = None
        if iccProfile:
            iccBytes = BytesIO(iccProfile)
            originalColourProfile = ImageCms.ImageCmsProfile(iccBytes)

        new_size = get_new_size(old_size, border_size, aspect_ratio)
        if new_size is None:
            raise BAD_PARAMETERS

        new_img = Image.new("RGB", new_size, "white")
        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_img.paste(old_img, box)

        byte_io = BytesIO()

        new_img.save(
            byte_io,
            format="JPEG",
            icc_profile=originalColourProfile.tobytes()
            if originalColourProfile
            else None,
        )
        byte_io.seek(0)

        return byte_io
    except UnidentifiedImageError:
        raise BAD_IMAGE
    except Exception as e:
        print(f"An error occurred: {e}")
        raise UNKNOWN_EXCEPTION


def validate_params(
    even_borders: bool, border_width_key: str, aspect_ratio_key: str
) -> Tuple[float, Union[AspectRatio, None]]:
    """validates the input params

    Args:
        even_borders (bool): equal sized borders check
        border_width_key (str): thinner edge width key
        aspect_ratio_key (str): aspect ratio key to retrieve matching aspect ratio

    Raises:
        BAD_PARAMETERS: provided params are invalid

    Returns:
        Tuple[float, Union[AspectRatio, None]]: border width percentage, target
        aspect ratio
    """
    if (border_width_key not in EDGE_MAP) or (
        aspect_ratio_key not in ASPECT_RATIO_MAP and not even_borders
    ):
        raise BAD_PARAMETERS

    border_size = EDGE_MAP[border_width_key]
    aspect_ratio = None
    if not even_borders:
        aspect_ratio = ASPECT_RATIO_MAP[aspect_ratio_key]

    return border_size, aspect_ratio
