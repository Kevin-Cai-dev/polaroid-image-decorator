from typing import Tuple, Optional

from create_images.aspect_ratio import AspectRatio


def get_new_dimensions(
    old_dim: Tuple[int, int], edge_size: float, aspect_ratio: Optional[AspectRatio]
) -> Optional[Tuple[int, int]]:
    """Returns dimensions of new image, based on provided edge size and aspect
    ratio. New dimensions match the original image orientation

    Args:
        old_dim (Tuple[int, int]): Original image size
        edge_size (float): Edge thickness along the longer image axis
        asp_ratio (Optional[AspectRatio]): New aspect ratio

    Returns:
        Optional[Tuple[int, int]]: New dimensions if new aspect ratio is
        possible without cropping the original image, otherwise None
    """
    if not aspect_ratio:
        border_px = int(edge_size * max(old_dim[0], old_dim[1]))
        return (old_dim[0] + border_px, old_dim[1] + border_px)
    if old_dim[1] > old_dim[0]:
        return get_portrait_dimensions(old_dim, edge_size, aspect_ratio)
    else:
        return get_landscape_dimensions(old_dim, edge_size, aspect_ratio)


def get_portrait_dimensions(
    old_dim: Tuple[int, int], edge_size: float, aspect_ratio: AspectRatio
) -> Optional[Tuple[int, int]]:
    """Returns dimensions of new portrait image, based on provided edge size and aspect ratio

    Args:
        old_dim (Tuple[int, int]): Original image size
        edge_size (float): Edge thickness along the longer image axis
        asp_ratio (AspectRatio): New aspect ratio

    Returns:
        Optional[Tuple[int, int]]: New dimensions if new aspect ratio is
        possible without cropping the original image, otherwise None
    """
    ratio = aspect_ratio.get_portrait()
    if (ratio[1] / ratio[0]) > (old_dim[1] / old_dim[0]):
        return None
    new_dimension = int((1 + edge_size) * max(old_dim[0], old_dim[1]))
    return (int(new_dimension / ratio[1] * ratio[0]), new_dimension)


def get_landscape_dimensions(
    old_dim: Tuple[int, int], edge_size: float, aspect_ratio: AspectRatio
) -> Optional[Tuple[int, int]]:
    """Returns dimensions of new landscape image, based on provided edge size and aspect ratio

    Args:
        old_dim (Tuple[int, int]): Original image size
        edge_size (float): Edge thickness along the longer image axis
        asp_ratio (AspectRatio): New aspect ratio

    Returns:
        Optional[Tuple[int, int]]: New dimensions if new aspect ratio is
        possible without cropping the original image, otherwise None
    """
    ratio = aspect_ratio.get_landscape()
    if (ratio[0] / ratio[1]) > (old_dim[0] / old_dim[1]):
        return None
    new_dimension = int((1 + edge_size) * max(old_dim[0], old_dim[1]))
    return (new_dimension, int(new_dimension / ratio[0] * ratio[1]))
