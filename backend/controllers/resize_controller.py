from typing import Tuple, Union
from models.aspect_ratio import AspectRatio


def get_new_size(
    old_size: Tuple[int, int],
    border_width: float,
    aspect_ratio: Union[AspectRatio, None],
) -> Union[Tuple[int, int], None]:
    """calculates new image size based off image sizing params

    Args:
        old_size (Tuple[int, int]): original image size
        border_width (float): thin edge percentage sizing
        aspect_ratio (Union[AspectRatio, None]): target aspect ratio

    Returns:
        Union[Tuple[int, int], None]: new image size, or None if aspect ratio
        cannot be achieved
    """
    # even borders
    if aspect_ratio is None:
        border_px = int(border_width * max(old_size[0], old_size[1]))
        return (old_size[0] + border_px, old_size[1] + border_px)

    if old_size[1] > old_size[0]:
        return get_new_portrait_size(old_size, border_width, aspect_ratio)
    else:
        return get_new_landscape_size(old_size, border_width, aspect_ratio)


def get_new_portrait_size(
    old_size: Tuple[int, int],
    border_width: float,
    aspect_ratio: AspectRatio,
) -> Union[Tuple[int, int], None]:
    """calculates new image size for portrait orientations

    Args:
        old_size (Tuple[int, int]): original image size
        border_width (float): thin edge percentage sizing
        aspect_ratio (AspectRatio): target aspect ratio

    Returns:
        Union[Tuple[int, int], None]: new image size, or None if aspect ratio
        cannot be achieved
    """
    ratio = aspect_ratio.get_portrait()
    # aspect ratio cannot be created with current image
    if (ratio[1] / ratio[0]) > (old_size[1] / old_size[0]):
        return None

    new_dimension = int((1 + border_width) * max(old_size[0], old_size[1]))
    return (int(new_dimension / ratio[1] * ratio[0]), new_dimension)


def get_new_landscape_size(
    old_size: Tuple[int, int],
    border_width: float,
    aspect_ratio: AspectRatio,
) -> Union[Tuple[int, int], None]:
    """calculates new image size for landsacape orientations

    Args:
        old_size (Tuple[int, int]): original image size
        border_width (float): thin edge percentage sizing
        aspect_ratio (AspectRatio): target aspect ratio

    Returns:
        Union[Tuple[int, int], None]: new image size, or None if aspect ratio
        cannot be achieved
    """
    ratio = aspect_ratio.get_landscape()
    # aspect ratio cannot be created with current image
    if (ratio[0] / ratio[1]) > (old_size[0] / old_size[1]):
        return None

    new_dimension = int((1 + border_width) * max(old_size[0], old_size[1]))
    return (new_dimension, int(new_dimension / ratio[0] * ratio[1]))
