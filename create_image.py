import argparse
import constants
import io
from pathlib import Path, PurePath
import sys
from typing import List, Dict

from PIL import Image, ImageCms, ImageOps, UnidentifiedImageError


def parse_args() -> Dict[str, any]:
    """Setup command-line argument parser

    Returns:
        Dict[str, any]: Dictionary representation of command-line args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image_paths",
        type=str,
        nargs="+",
        help="image paths or directory paths to images to be 'polaroidised'",
    )
    parser.add_argument(
        "-n",
        action="store_true",
        help="disable borders on the longer image dimension",
        dest="disable_borders",
    )

    return vars(parser.parse_args())


def validate_paths(img_paths: List[str]) -> None:
    """Validate whether the command-line arguments are directory/file paths

    Args:
        img_paths (List[str]): List of paths provided via stdin
    """
    for path in img_paths:
        check_path = Path(path)
        if not check_path.is_file() and not check_path.is_dir():
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def create_polaroid_images(img_paths: List[str]) -> None:
    """Iterates over the given file/directory path(s) and attempts to generate
    polaroid images

    Args:
        img_paths (List[str]): List of file/directory path(s)
    """
    for path in img_paths:
        img_path = Path(path)
        if img_path.is_file():
            if constants.SUFFIX not in str(img_path):
                generate_new_image(img_path)
        elif img_path.is_dir():
            files = [f for f in img_path.iterdir() if Path(f).is_file()]
            for fpath in files:
                if constants.SUFFIX not in str(fpath):
                    generate_new_image(fpath)
        else:
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def generate_new_image(path: Path) -> None:
    """Generates a new polaroid-esque image of the provided image and saves the
    file in the same location as the original. The original file is preserved.

    Args:
        path (Path): file path to the image to be converted
    """
    try:
        old_image = ImageOps.exif_transpose(Image.open(str(path)))
        old_size = old_image.size

        iccProfile = old_image.info.get("icc_profile")
        originalColorProfile = None
        if iccProfile:
            iccBytes = io.BytesIO(iccProfile)
            originalColorProfile = ImageCms.ImageCmsProfile(iccBytes)

        new_dimension = int(
            (1 + constants.EDGE_SIZE) * max(old_image.height, old_image.width)
        )
        new_size = (new_dimension, new_dimension)
        new_image = Image.new("RGB", new_size, "White")

        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_image.paste(old_image, box)

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
