from create_images import create_image as ci, validate as val


if __name__ == "__main__":
    paths, edge_size = val.parse_args()
    val.validate_paths(paths)
    ci.create_polaroid_images(paths, edge_size)
