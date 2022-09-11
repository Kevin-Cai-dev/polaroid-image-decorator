from pathlib import Path, PurePath
import sys
import io
from typing import List
import constants

from PIL import Image, ImageCms, UnidentifiedImageError


def validate_args(img_paths: List[str]) -> None:
    for path in img_paths:
        check_path = Path(path)
        if not check_path.is_file() and not check_path.is_dir():
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def create_polaroid_images(img_paths: List[str]) -> None:
    for path in img_paths:
        img_path = Path(path)
        if img_path.is_file():
            generate_new_image(path)
        elif img_path.is_dir():
            files = [f for f in img_path.iterdir() if Path(
                PurePath(path).joinpath(f)).is_file()]
            for fpath in files:
                generate_new_image(fpath)
        else:
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def generate_new_image(path: str) -> None:
    try:
        img_path = PurePath(path)
        old_image = Image.open(path)
        iccProfile = old_image.info.get('icc_profile')
        iccBytes = io.BytesIO(iccProfile)
        originalColorProfile = ImageCms.ImageCmsProfile(iccBytes)
        old_size = old_image.size

        new_dimension = int((1 + constants.EDGE_SIZE) *
                            max(old_image.height, old_image.width))
        new_size = (new_dimension, new_dimension)
        new_image = Image.new("RGB", new_size, "White")

        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_image.paste(old_image, box)

        img_path = PurePath(path)
        parent_dir = img_path.parent
        file_name = img_path.stem
        new_file_path = PurePath.joinpath(
            parent_dir, file_name + "_polaroid" + constants.JPEG)

        new_image.save(str(new_file_path),
                       icc_profile=originalColorProfile.tobytes())
    except (UnidentifiedImageError):
        pass
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(constants.NO_PATHS_PROVIDED)

    paths = sys.argv[1:]
    validate_args(paths)
    create_polaroid_images(paths)
