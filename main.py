from create_images import create_image as ci, validate as val


if __name__ == "__main__":
    args, edge_size = val.parse_args()
    paths = args["image_paths"]
    val.validate_paths(paths)
    ci.create_polaroid_images(paths, edge_size)
