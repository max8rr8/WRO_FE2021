from consts import DIRECTION_CCW, DIRECTION_CW
from config.config import QUALIFICATION_MODE

# Configuration for red side marker
SIDE_RED = {
    'zone': ((54, 178), (302, 512)),
    'bin_min': (0, 0, 0),
    'bin_max': (30, 255, 255),
    'area_min': 118,
    'show_unbinarized': True
}

# Configuration for green side marker
SIDE_GREEN = {
    'zone': ((54, 178), (0, 190)),
    'bin_min': (50, 100, 80),
    'bin_max': (90, 255, 255),
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
    'bin_min': (4, 29, 65),
    'bin_max': (62, 202, 184),
    'area_min': 50
    }, 
    DIRECTION_CCW: { # BLUE LINE

    'zone':  ((170, 320), (60, 360)) if QUALIFICATION_MODE else ((170, 280), (200, 240)),
    'bin_min': (78, 29, 30),
    'bin_max': (140, 255, 135),
    'area_min': 50
    }
}

# Configuration for red marker
RED_MARKER = {
    'zone': ((129, 333), (35, 172)),
    'bin_min': (0, 0, 0),
    'bin_max': (30, 255, 255),
    'area_min': 800
}

# Configuration for green marker
GREEN_MARKER = {
    'zone': ((44, 262), (246, 425)),
    'bin_min': (48, 136, 70),
    'bin_max': (75, 255, 255),
    'area_min': 1300
}
