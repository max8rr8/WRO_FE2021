from consts import *
from config.config import QUALIFICATION_MODE

############# BASIC CONFIGURATION
QUALIFICATION_MODE = True # False: final mode, True: qualification mode
ENABLE_MOTORS = True # Enable motors, for debug purpose

############# WALL MOVEMENT CONFIGURATION
KP = 1.5 # PID proportional coefficient
KD = 3  # PID differential coefficient
ROUNDER = 1 # UNUSED
WALL_POINT = 47 # Target point for wall movement (final mode), the bigger the more near to wall we move
QUALIFICATION_WALL_POINT = 80  # Same as previous, but for qualification mode

if QUALIFICATION_MODE: # If we are in qualification mode
    WALL_SEARCH_Y = (80, 240) # Min y and max y for wall search zone (qualification mode)
    WALL_SEARCH_X = 60  # Width of search zone  (qualification mode)
else:
    WALL_SEARCH_Y = (60, 260) # Min y and max y for wall search zone (final mode)
    WALL_SEARCH_X = 80  # Width of search zone (final mode)

WALL_BIN = {'bin_min': (0, 0, 0), 'bin_max': (255, 255, 40)} # Wall binarizatin parameters

POINT_SHIFT = { # Point shift for wall movement, for clockwise direction (in ccw they will be inverted)
    MARKER_RED: -15,
    MARKER_GREEN: +15,
    MARKER_NONE: 0
}

QUALIFICATION_SECTOR_BORDERS = (30, 90) # Rnage of distance to wall for central sector (qualification mode)
