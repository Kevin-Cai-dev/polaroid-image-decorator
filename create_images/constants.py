TOO_MANY_SIZE_FLAGS = "please specify one border size flag only"
INVALID_PATHS_PROVIDED = "Please provide valid image or directory paths!"
SUFFIX = "_POLAROID"
JPEG = ".jpg"

IMAGE_PATHS = "image_paths"
DISABLE_BORDERS = "disable_borders"
XS_BORDERS = "xs_borders"
SM_BORDERS = "sm_borders"
MD_BORDERS = "md_borders"
LG_BORDERS = "lg_borders"
XL_BORDERS = "xl_borders"

IMAGE_PATHS_HELP = "image paths or directory paths to images to be 'polaroidised'"
DISABLE_BORDERS_HELP = "disable borders on the longer image dimension"
XS_BORDERS_HELP = "add extra small borders on the longer image dimension"
SM_BORDERS_HELP = "add small borders on the longer image dimension"
MD_BORDERS_HELP = "add medium borders on the longer image dimension (default)"
LG_BORDERS_HELP = "add large borders on the longer image dimension"
XL_BORDERS_HELP = "add extra large borders on the longer image dimension"

EDGE_MAP = {
    DISABLE_BORDERS: 0,
    XS_BORDERS: 0.02,
    SM_BORDERS: 0.04,
    MD_BORDERS: 0.06,
    LG_BORDERS: 0.08,
    XL_BORDERS: 0.1,
}
