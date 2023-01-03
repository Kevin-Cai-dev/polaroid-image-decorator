from create_images import create_image as ci, validate as val


if __name__ == "__main__":
    paths, input_args = val.parse_args()
    valid_paths = val.validate_paths(paths)
    ci.create_polaroid_images(valid_paths, input_args)
