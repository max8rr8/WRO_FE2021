from consts import DIRECTION_CCW, DIRECTION_CW
from config.config import QUALIFICATION_MODE

# Configuration for red side marker
SIDE_RED = {
    'zone': ((54, 178), (302, 512)),
    'bin_min': (0, 186, 56),
    'bin_max': (14, 255, 127),
    'area_min': 118,
    'show_unbinarized': True
}

# Configuration for green side marker
SIDE_GREEN = {
    'zone': ((62, 144), (0, 89)),
    'bin_min': (66, 181, 44),
    'bin_max': (91, 255, 126),
    'area_min': 100,
    'show_unbinarized': True
}

# Unused
SIDE_ZONE = {
    DIRECTION_CW: ((30, 176), (300, 640)),
    DIRECTION_CCW: ((75, 174), (0, 66)),
}

# Configuration for line(orange and blue) binarization
MAIN_LINE = {
    'zone':  ((170, 320), (60, 360)) if QUALIFICATION_MODE else ((180, 270), (200, 240)),
    'bin_min': (3, 24, 112),
    'bin_max': (22, 255, 142),
    'area_min': 50
}

# Configuration for red marker
RED_MARKER = {
    'zone': ((129, 333), (35, 152)),
    'bin_min': (0, 71, 54),
    'bin_max': (30, 255, 255),
    'area_min': 1500
}

# Configuration for green marker
GREEN_MARKER = {
    'zone': ((129, 333), (255, 367)),
    'bin_min': (60, 156, 37),
    'bin_max': (85, 255, 97),
    'area_min': 1500
}
