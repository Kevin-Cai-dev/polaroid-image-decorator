import sys

from create_image import parse_args, validate_paths, create_polaroid_images

if __name__ == "__main__":
    args = parse_args()
    paths = args["image_paths"]
    validate_paths(paths)
    create_polaroid_images(paths)
    sys.exit(0)
