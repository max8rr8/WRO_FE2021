from consts import *

# Конфигурация поиска обьектов сбоку
SIDE_RED = {
    'bin_min': (0, 137, 49),
    'bin_max': (15, 255, 219),
    'area_min': 100,
    'show_unbinarized': True
}

SIDE_GREEN = {
    'bin_min': (0, 140, 0),
    'bin_max': (89, 255, 255),
    'area_min': 400,
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
