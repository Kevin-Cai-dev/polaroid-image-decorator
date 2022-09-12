from create_images import constants, resize
import io
from pathlib import Path, PurePath
import sys
from typing import List

from PIL import Image, ImageCms, ImageOps, UnidentifiedImageError

from create_images.aspect_ratio import AspectRatio


def create_polaroid_images(
    img_paths: List[Path], edge_size: float, aspect_ratio: AspectRatio
) -> None:
    """Iterates over the given file/directory path(s) and aattempts to generate
    polaroid images

    Args:
        img_paths (List[Path]): List of file/directory path(s)
        edge_size (float): size of the thin edge as a percentage
        aspect_ratio (AspectRatio): new image aspect ratio
    """
    for img_path in img_paths:
        if img_path.is_file():
            if constants.SUFFIX not in str(img_path):
                generate_new_image(img_path, edge_size, aspect_ratio)
        elif img_path.is_dir():
            files = [f for f in img_path.iterdir() if Path(f).is_file()]
            for fpath in files:
                if constants.SUFFIX not in str(fpath):
                    generate_new_image(fpath, edge_size, aspect_ratio)
        else:
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def generate_new_image(path: Path, edge_size: float, aspect_ratio: AspectRatio) -> None:
    """Generates a new polaroid-esque image of the provided image and saves the
    file in the same location as the original. The original file is preserved.

    Args:
        path (Path): file paths to the image to be converted
        edge_size (float): size of the thin edge as a percentage
        aspect_ratio (AspectRatio): new image aspect ratio
    """
    try:
        # Using correct image orientation
        old_image = ImageOps.exif_transpose(Image.open(str(path)))
        old_size = old_image.size

        # Saving iccProfile if it exists to preserve image colours
        iccProfile = old_image.info.get("icc_profile")
        originalColourProfile = None
        if iccProfile:
            iccBytes = io.BytesIO(iccProfile)
            originalColourProfile = ImageCms.ImageCmsProfile(iccBytes)

        # Creating new polaroid image
        new_size = resize.get_new_dimensions(old_size, edge_size, aspect_ratio)
        if new_size is None:
            print(f"Couldn't convert image {path}: bad aspect ratio")
            return
        new_image = Image.new("RGB", new_size, "White")
        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_image.paste(old_image, box)

        # Saving new image in same location as original
        parent_dir = path.parent
        file_name = path.stem
        new_file_path_string = file_name + constants.SUFFIX + constants.JPEG
        new_file_path = PurePath.joinpath(parent_dir, new_file_path_string)
        new_image.save(
            str(new_file_path),
            icc_profile=originalColourProfile.tobytes() if iccProfile else None,
        )
    except (UnidentifiedImageError):
        pass
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
