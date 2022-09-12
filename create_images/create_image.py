from create_images import constants
import io
from pathlib import Path, PurePath
import sys
from typing import List

from PIL import Image, ImageCms, ImageOps, UnidentifiedImageError


def create_polaroid_images(img_paths: List[str], edge_size: float) -> None:
    """Iterates over the given file/directory path(s) and attempts to generate
    polaroid images

    Args:
        img_paths (List[str]): List of file/directory path(s)
    """
    for path in img_paths:
        img_path = Path(path)

        if img_path.is_file():
            if constants.SUFFIX not in str(img_path):
                generate_new_image(img_path, edge_size)
        elif img_path.is_dir():
            files = [f for f in img_path.iterdir() if Path(f).is_file()]
            for fpath in files:
                if constants.SUFFIX not in str(fpath):
                    generate_new_image(fpath, edge_size)
        else:
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def generate_new_image(path: Path, edge_size: float) -> None:
    """Generates a new polaroid-esque image of the provided image and saves the
    file in the same location as the original. The original file is preserved.

    Args:
        path (Path): file path to the image to be converted
    """
    try:
        old_image = ImageOps.exif_transpose(Image.open(str(path)))
        old_size = old_image.size

        # Saving iccProfile if it exists to preserve image colours
        iccProfile = old_image.info.get("icc_profile")
        originalColorProfile = None
        if iccProfile:
            iccBytes = io.BytesIO(iccProfile)
            originalColorProfile = ImageCms.ImageCmsProfile(iccBytes)

        # Creating new image frame
        new_dimension = int((1 + edge_size) * max(old_image.height, old_image.width))
        new_size = (new_dimension, new_dimension)
        new_image = Image.new("RGB", new_size, "White")
        # Copying old image to centre of new image
        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_image.paste(old_image, box)

        # Saving new image in same location as original
        parent_dir = path.parent
        file_name = path.stem
        new_file_path_string = file_name + constants.SUFFIX + constants.JPEG
        new_file_path = PurePath.joinpath(parent_dir, new_file_path_string)
        new_image.save(
            str(new_file_path),
            icc_profile=originalColorProfile.tobytes() if iccProfile else None,
        )
    except (UnidentifiedImageError):
        pass
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
