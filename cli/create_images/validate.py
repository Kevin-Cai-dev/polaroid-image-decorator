from argparse import ArgumentParser
from pathlib import Path
import sys
from typing import List, Tuple, Optional

from create_images import constants
from create_images.aspect_ratio import AspectRatio


def parse_args() -> Tuple[List[str], float, Optional[AspectRatio]]:
    """Parses command-line arguments

    Returns:
        Tuple[List[str], float, Optional[AspectRatio]]: Image paths, thin border
        sizing as a percentage, desired aspect ratio if equal borders are not specified
    """
    parser = ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        constants.IMAGE_PATHS,
        type=str,
        nargs="+",
        help=constants.IMAGE_PATHS_HELP,
    )
    add_equal_border_flag(parser)
    add_edge_size_flags(parser)
    add_aspect_ratio_flags(parser)

    args = vars(parser.parse_args())
    edge_size = None
    aspect_ratio = None

    even_borders = True if args[constants.EQUAL_BORDERS] else False

    for key in args:
        if key in constants.EDGE_KEYS and args[key]:
            edge_size = (
                constants.EDGE_MAP[key]
                if edge_size is None
                else parser.error(constants.TOO_MANY_SIZE_FLAGS)
            )
        if key in constants.RATIO_KEYS and args[key]:
            if even_borders:
                parser.error(constants.EQUAL_BORDERS_WITH_ASPECT_RATIO)
            aspect_ratio = (
                constants.ASPECT_RATIO_MAP[key]
                if aspect_ratio is None
                else parser.error(constants.TOO_MANY_ASPECT_RATIO_FLAGS)
            )

    if not aspect_ratio and not even_borders:
        aspect_ratio = constants.ASPECT_RATIO_MAP[constants.RATIO_1_1]

    return (
        args[constants.IMAGE_PATHS],
        edge_size
        if edge_size is not None
        else constants.EDGE_MAP[constants.MD_BORDERS],
        aspect_ratio,
    )


def add_equal_border_flag(parser: ArgumentParser) -> None:
    """Adds equal border flag to the argument parser

    Args:
        parser (ArgumentParser): Argument parser used for command-line flags
    """
    parser.add_argument(
        "-e",
        "--eq",
        action="store_true",
        help=constants.EQUAL_BORDERS_HELP,
        dest=constants.EQUAL_BORDERS,
    )


def add_edge_size_flags(parser: ArgumentParser) -> None:
    """Adds border size related flags to the argument parser

    Args:
        parser (ArgumentParser): Argument parser used for command-line flags
    """
    parser.add_argument(
        "--nb",
        "--no-border",
        action="store_true",
        help=constants.DISABLE_BORDERS_HELP,
        dest=constants.DISABLE_BORDERS,
    )
    parser.add_argument(
        "--xs",
        "--extra-small",
        action="store_true",
        help=constants.XS_BORDERS_HELP,
        dest=constants.XS_BORDERS,
    )
    parser.add_argument(
        "--sm",
        "--small",
        action="store_true",
        help=constants.SM_BORDERS_HELP,
        dest=constants.SM_BORDERS,
    )
    parser.add_argument(
        "--md",
        "--medium",
        action="store_true",
        help=constants.MD_BORDERS_HELP,
        dest=constants.MD_BORDERS,
    )
    parser.add_argument(
        "--lg",
        "--large",
        action="store_true",
        help=constants.LG_BORDERS_HELP,
        dest=constants.LG_BORDERS,
    )
    parser.add_argument(
        "--xl",
        "--extra-large",
        action="store_true",
        help=constants.XL_BORDERS_HELP,
        dest=constants.XL_BORDERS,
    )


def add_aspect_ratio_flags(parser: ArgumentParser) -> None:
    """Adds aspect ratio related flags to the argument parser

    Args:
        parser (ArgumentParser): Argument parser used for command-line flags
    """
    parser.add_argument(
        "--3-2",
        "--2-3",
        action="store_true",
        help=constants.RATIO_3_2_HELP,
        dest=constants.RATIO_3_2,
    )
    parser.add_argument(
        "--5-4",
        "--4-5",
        action="store_true",
        help=constants.RATIO_5_4_HELP,
        dest=constants.RATIO_5_4,
    )
    parser.add_argument(
        "--16-9",
        "--9-16",
        action="store_true",
        help=constants.RATIO_16_9_HELP,
        dest=constants.RATIO_16_9,
    )


def validate_paths(img_paths: List[str]) -> List[Path]:
    """Validate whether the command-line arguments are directory/file paths, and
    return them in Path format if valid

    Args:
        img_paths (List[str]): List of paths provided via command-line

    Returns:
        List[Path]: List of Path representations for each file/directory pathstring
    """
    valid_paths = []
    for path in img_paths:
        check_path = Path(path)
        if not check_path.is_file() and not check_path.is_dir():
            sys.exit(constants.INVALID_PATHS_PROVIDED)
        valid_paths.append(check_path)
    return valid_paths
