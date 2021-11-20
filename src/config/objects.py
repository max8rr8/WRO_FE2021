from consts import DIRECTION_CCW, DIRECTION_CW
from config.config import QUALIFICATION_MODE

# Configuration for red side marker
SIDE_RED = {
    'zone': ((54, 178), (100, 512)),
    'bin_min': (0, 50, 35),
    'bin_max': (28, 256, 100),
    'area_min': 50,
    'show_unbinarized': True
}

# Configuration for green side marker
SIDE_GREEN = {
    'zone': ((54, 178), (0, 190)),
    'bin_min': (68, 209, 37),
    'bin_max': (96, 255, 74),
    'area_min': 50,
    'show_unbinarized': True
}

# Unused
SIDE_ZONE = {
    DIRECTION_CW: ((30, 176), (300, 640)),
    DIRECTION_CCW: ((75, 174), (0, 66)),
}

# Configuration for line(orange and blue) binarization
MAIN_LINE = {
    DIRECTION_CW: { # ORANGE LINE
    'zone':  ((170, 320), (60, 360)) if QUALIFICATION_MODE else ((170, 280), (200, 240)),

    'bin_min': (10, 28, 69),
    'bin_max': (75, 155, 155),
    'area_min': 50
    }, 
    DIRECTION_CCW: { # BLUE LINE

    'zone':  ((170, 320), (150, 345)) if QUALIFICATION_MODE else ((170, 280), (200, 240)),

    'bin_min': (93, 159, 55),
    'bin_max': (114, 255, 144),
    'area_min': 50
    }
}

# Configuration for red marker
RED_MARKER = {
    'zone': ((80, 333), (35, 200)),
    'bin_min': (0, 0, 0),
    'bin_max': (30, 255, 255),
    'area_min': 700
}

# Configuration for green marker
GREEN_MARKER = {
    'zone': ((44, 262), (246, 425)),
    'bin_min': (61, 212, 47),
    'bin_max': (92, 255, 96),
    'area_min': 1300
}