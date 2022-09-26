from create_images.aspect_ratio import AspectRatio

# error messages
TOO_MANY_SIZE_FLAGS = "please specify one border size flag only"
TOO_MANY_ASPECT_RATIO_FLAGS = "please specify one aspect ratio flag only"
INVALID_PATHS_PROVIDED = "Please provide valid image or directory paths!"

# image naming substrings
SUFFIX = "_POLAROID"
JPEG = ".jpg"

# flag keys
IMAGE_PATHS = "image_paths"
DISABLE_BORDERS = "disable_borders"
EQUAL_BORDERS = "equal_borders"
XS_BORDERS = "xs_borders"
SM_BORDERS = "sm_borders"
MD_BORDERS = "md_borders"
LG_BORDERS = "lg_borders"
XL_BORDERS = "xl_borders"
RATIO_1_1 = "ratio_1_1"
RATIO_5_4 = "ratio_5_4"
RATIO_3_2 = "ratio_3_2"
RATIO_16_9 = "ratio_16_9"

EDGE_KEYS = {XS_BORDERS, SM_BORDERS, MD_BORDERS, LG_BORDERS, XL_BORDERS}
RATIO_KEYS = {RATIO_5_4, RATIO_3_2, RATIO_16_9}

# flag help messages
IMAGE_PATHS_HELP = "image paths or directory paths to images to be 'polaroidised'"
DISABLE_BORDERS_HELP = "disable borders on the longer image dimension"
EQUAL_BORDERS_HELP = "add equal sized borders to the image"
XS_BORDERS_HELP = "add extra small borders on the longer image dimension"
SM_BORDERS_HELP = "add small borders on the longer image dimension"
MD_BORDERS_HELP = "add medium borders on the longer image dimension (default)"
LG_BORDERS_HELP = "add large borders on the longer image dimension"
XL_BORDERS_HELP = "add extra large borders on the longer image dimension"
RATIO_5_4_HELP = "create an image with a 5:4 aspect ratio if possible, following original \
orientation"
RATIO_3_2_HELP = "create an image with a 3:2 aspect ratio if possible, following original \
orientation"
RATIO_16_9_HELP = "create an image with a 16:9 aspect ratio if possible, following original \
orientation"

EDGE_MAP = {
    DISABLE_BORDERS: 0.0,
    XS_BORDERS: 0.02,
    SM_BORDERS: 0.04,
    MD_BORDERS: 0.06,
    LG_BORDERS: 0.08,
    XL_BORDERS: 0.1,
}

ASPECT_RATIO_MAP = {
    RATIO_1_1: AspectRatio(1, 1),
    RATIO_5_4: AspectRatio(4, 5),
    RATIO_3_2: AspectRatio(2, 3),
    RATIO_16_9: AspectRatio(9, 16),
}
