import argparse
from pathlib import Path
import sys
from typing import List, Union

from create_images import constants


def parse_args() -> Union[List[str], float]:
    """Parses command-line arguments

    Returns:
        Union[List[str], float]: Image paths, border sizing
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        constants.IMAGE_PATHS,
        type=str,
        nargs="+",
        help=constants.IMAGE_PATHS_HELP,
    )
    parser.add_argument(
        "-nb",
        "--no-border",
        action="store_true",
        help=constants.DISABLE_BORDERS_HELP,
        dest=constants.DISABLE_BORDERS,
    )
    parser.add_argument(
        "-xs",
        "--extra-small",
        action="store_true",
        help=constants.XS_BORDERS_HELP,
        dest=constants.XS_BORDERS,
    )
    parser.add_argument(
        "-sm",
        "--small",
        action="store_true",
        help=constants.SM_BORDERS_HELP,
        dest=constants.SM_BORDERS,
    )
    parser.add_argument(
        "-md",
        "--medium",
        action="store_true",
        help=constants.MD_BORDERS_HELP,
        dest=constants.MD_BORDERS,
    )
    parser.add_argument(
        "-lg",
        "--large",
        action="store_true",
        help=constants.LG_BORDERS_HELP,
        dest=constants.LG_BORDERS,
    )
    parser.add_argument(
        "-xl",
        "--extra-large",
        action="store_true",
        help=constants.XL_BORDERS_HELP,
        dest=constants.XL_BORDERS,
    )

    args = vars(parser.parse_args())
    edge_size = None

    for key in args:
        if key != constants.IMAGE_PATHS and args[key]:
            edge_size = (
                constants.EDGE_MAP[key]
                if edge_size == None
                else parser.error(constants.TOO_MANY_SIZE_FLAGS)
            )

    return (
        args[constants.IMAGE_PATHS],
        edge_size if edge_size != None else constants.EDGE_MAP[constants.MD_BORDERS],
    )


def validate_paths(img_paths: List[str]) -> None:
    """Validate whether the command-line arguments are directory/file paths

    Args:
        img_paths (List[str]): List of paths provided via stdin
    """
    for path in img_paths:
        check_path = Path(path)
        if not check_path.is_file() and not check_path.is_dir():
            sys.exit(constants.INVALID_PATHS_PROVIDED)
