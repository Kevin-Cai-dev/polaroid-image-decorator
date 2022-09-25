from create_images import create_image as ci, validate as val


if __name__ == "__main__":
    paths, edge_size, aspect_ratio = val.parse_args()
    valid_paths = val.validate_paths(paths)
    ci.create_polaroid_images(valid_paths, edge_size, aspect_ratio)
