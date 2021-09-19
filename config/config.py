from consts import *

############# БАЗОВАЯ КОНФИГУРАЦИЯ
QUALIFICATION_MODE = False
ENABLE_MOTORS = True

############# КОНФИГУРАЦИЯ ЕЗДЫ ПО СТЕНКЕ
KP = 1.5
KD = 2
ROUNDER = 1
WALL_POINT = 50
QUALIFICATION_WALL_POINT = 100

WALL_SEARCH_Y = (80, 240)
WALL_SEARCH_X = 60
WALL_BIN = {'bin_min': (0, 0, 0), 'bin_max': (255, 255, 40)}

POINT_SHIFT = {
    MARKER_RED: -15,
    MARKER_GREEN: +15,
    MARKER_NONE: 0
}

QUALIFICATION_SECTOR_BORDERS = (30, 90)
