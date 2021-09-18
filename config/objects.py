from consts import DIRECTION_CCW, DIRECTION_CW

# Конфигурация поиска обьектов сбоку
SIDE_RED = {
    'zone': ((54, 178), (302, 512)),
    'bin_min': (0, 186, 56),
    'bin_max': (14, 255, 127),
    'area_min': 118,
    'show_unbinarized': True
}

SIDE_GREEN = {
    'zone': ((62, 144), (0, 89)),
    'bin_min': (66, 181, 44),
    'bin_max': (91, 255, 126),
    'area_min': 100,
    'show_unbinarized': True
}

SIDE_ZONE = {
    DIRECTION_CW: ((30, 176), (300, 640)),
    DIRECTION_CCW: ((75, 174), (0, 66)),
}

# Конфигурация поиска линии
MAIN_LINE = {
    'zone': ((180, 270), (200, 240)),
    'bin_min': (0, 80, 30),
    'bin_max': (255, 255, 255),
    'area_min': 50
}

# Конфигурация поиска обьектов
RED_MARKER = {
    'zone': ((129, 333), (35, 152)),
    'bin_min': (0, 21, 0),
    'bin_max': (48, 255, 255),
    'area_min': 1500
}

GREEN_MARKER = {
    'zone': ((129, 333), (255, 367)),
    'bin_min': (0, 140, 0),
    'bin_max': (89, 255, 255),
    'area_min': 1500
}
