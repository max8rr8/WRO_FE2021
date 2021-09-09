from consts import *

############# БАЗОВАЯ КОНФИГУРАЦИЯ
ENABLE_MOTORS = True

############# КОНФИГУРАЦИЯ ЕЗДЫ ПО СТЕНКЕ
KP = 1.5
KD = 1
ROUNDER = 1
CW_POINT = 42.9
CCW_POINT = 42.9
WALL_BIN = {'bin_min': (0, 0, 0), 'bin_max': (255, 255, 70)}

POINT_SHIFT = {
    MARKER_RED: -15,
    MARKER_GREEN: +15,
    MARKER_NONE: 0
}