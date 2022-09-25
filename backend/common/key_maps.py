from models.aspect_ratio import AspectRatio

EDGE_MAP = {
    "disable_borders": 0.0,
    "xs_borders": 0.02,
    "sm_borders": 0.04,
    "md_borders": 0.06,
    "lg_borders": 0.08,
    "xl_borders": 0.1,
}

ASPECT_RATIO_MAP = {
    "ratio_1_1": AspectRatio(1, 1),
    "ratio_5_4": AspectRatio(4, 5),
    "ratio_3_2": AspectRatio(2, 3),
    "ratio_16_9": AspectRatio(9, 16),
}
