import argparse
from pathlib import Path
import sys
from typing import List, Dict, Union

from create_images import constants


def parse_args() -> Union[Dict[str, any], float]:
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
        "-nb",
        "--no-border",
        action="store_true",
        help="disable borders on the longer image dimension",
        dest="disable_borders",
    )
    parser.add_argument(
        "-xs",
        "--extra-small",
        action="store_true",
        help="add extra small borders on the longer image dimension",
        dest="xs_borders",
    )
    parser.add_argument(
        "-sm",
        "--small",
        action="store_true",
        help="add small borders on the longer image dimension",
        dest="sm_borders",
    )
    parser.add_argument(
        "-md",
        "--medium",
        action="store_true",
        help="add medium borders on the longer image dimension (default)",
        dest="md_borders",
    )
    parser.add_argument(
        "-lg",
        "--large",
        action="store_true",
        help="add large borders on the longer image dimension",
        dest="lg_borders",
    )
    parser.add_argument(
        "-xl",
        "--extra-large",
        action="store_true",
        help="add extra large borders on the longer image dimension",
        dest="xl_borders",
    )

    args = vars(parser.parse_args())
    edge_size = None

    for key in args:
        if key != "image_paths" and args[key]:
            edge_size = (
                constants.EDGE_MAP[key]
                if edge_size == None
                else parser.error("please specify one border size flag only")
            )

    return args, edge_size if edge_size != None else constants.EDGE_MAP["md_borders"]


def validate_paths(img_paths: List[str]) -> None:
    """Validate whether the command-line arguments are directory/file paths

    Args:
        img_paths (List[str]): List of paths provided via stdin
    """
    for path in img_paths:
        check_path = Path(path)
        if not check_path.is_file() and not check_path.is_dir():
            sys.exit(constants.INVALID_PATHS_PROVIDED)
