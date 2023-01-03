from pathlib import Path, PurePath
import sys
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image, ImageOps, UnidentifiedImageError

from create_images import constants, resize
from create_images.aspect_ratio import AspectRatio


def create_polaroid_images(
    img_paths: List[Path], input_args: Dict[float, Optional[AspectRatio]]
) -> None:
    """Iterates over the given file/directory path(s) and aattempts to generate
    polaroid images

    Args:
        img_paths (List[Path]): List of file/directory path(s)
        input_args (Dict[float, Optional[AspectRatio]]): image resizing arguments
    """
    for img_path in img_paths:
        if img_path.is_file():
            if constants.SUFFIX not in str(img_path):
                generate_new_image(img_path, input_args)
        elif img_path.is_dir():
            files = [f for f in img_path.iterdir() if Path(f).is_file()]
            for fpath in files:
                if constants.SUFFIX not in str(fpath):
                    generate_new_image(fpath, input_args)
        else:
            sys.exit(constants.INVALID_PATHS_PROVIDED)


def generate_new_image(
    path: Path, input_args: Dict[float, Optional[AspectRatio]]
) -> None:
    """Generates a new polaroid-esque image of the provided image and saves the
    file in the same location as the original. The original file is preserved.

    Args:
        path (Path): file paths to the image to be converted
        input_args (Dict[float, Optional[AspectRatio]]): image resizing arguments
    """
    try:
        # Using correct image orientation
        old_image = ImageOps.exif_transpose(Image.open(str(path)))
        old_size = old_image.size

        original_colour_profile = old_image.info.get("icc_profile")

        # Get new image dimensions
        new_size = resize.get_new_dimensions(
            old_size,
            input_args[constants.EDGE_SIZE],
            input_args[constants.ASPECT_RATIO],
        )
        if new_size is None:
            print(f"Couldn't convert image {path}: bad aspect ratio")
            return

        # Creating new polaroid image
        new_image = create_new_image(old_image, old_size, new_size)

        if input_args[constants.INSTA_OPTIMISED]:
            new_image = insta_resize_image(new_image)

        # Saving new image in same location as original
        save_image(path, new_image, original_colour_profile)
    except (UnidentifiedImageError):
        pass
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def create_new_image(
    old_image: Image, old_size: Tuple[int, int], new_size: Tuple[int, int]
) -> Image:
    """Creates a new polaroid image

    Args:
        old_image (Image): Original image
        old_size (Tuple[int, int]): Original image size
        new_size (Tuple[int, int]): New image size

    Returns:
        Image: New polaroid image
    """
    new_image = Image.new("RGB", new_size, "White")
    box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
    new_image.paste(old_image, box)
    return new_image


def insta_resize_image(image: Image) -> Image:
    """Resizes the polaroid image to optimise for instagram

    Args:
        image (Image): Polaroid image

    Returns:
        Image: Resized image
    """
    insta_size = resize.get_instagram_dimensions(image.size)
    return image.resize(insta_size)


def save_image(path: Path, image: Image, icc_profile: Optional[Any]) -> None:
    """Function to save the newly generated image

    Args:
        path (Path): Original image path
        image (Image): New polaroid image
        original_colour_profile (Optional[Any]): Original icc_profile
    """
    parent_dir = path.parent
    file_name = path.stem
    new_file_path_string = file_name + constants.SUFFIX + constants.JPEG
    new_file_path = PurePath.joinpath(parent_dir, new_file_path_string)
    image.save(
        str(new_file_path),
        format="JPEG",
        quality=95,
        dpi=(300, 300),
        icc_profile=icc_profile,
    )
