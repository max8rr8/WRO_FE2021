from consts import *

############# BASIC CONFIGURATION
QUALIFICATION_MODE = False # False: final mode, True: qualification mode
ENABLE_MOTORS = True # Enable motors, for debug purpose

############# WALL MOVEMENT CONFIGURATION
if QUALIFICATION_MODE: # QUALIFICATION
    KP = 1 # PID proportional coefficient
    KD = 3 #для большей скорости увеличивать # PID differential coefficient
else: # FINAL
    KP = 1.5 # PID proportional coefficient
    KD = 3 #для большей скорости увеличивать # PID differential coefficient


ROUNDER = 1 # UNUSED

# уменьшать если скорость увеличиывем# Target point for wall movement (final mode), the bigger the more near to wall we move
# WALL_POINT = 65 
WALL_POINT = {
    DIRECTION_CW: 59,
    DIRECTION_CCW: 59,
}

QUALIFICATION_WALL_POINT = 80  # Same as previous, but for qualification mode

if QUALIFICATION_MODE: # If we are in qualification mode
    WALL_SEARCH_Y = (80, 240) # Min y and max y for wall search zone (qualification mode)
    WALL_SEARCH_X = 60  # Width of search zone  (qualification mode)
else:
    WALL_SEARCH_Y = (60, 260) # Min y and max y for wall search zone (final mode)
    WALL_SEARCH_X = 80  # Width of search zone (final mode)

WALL_BIN = {'bin_min': (0, 0, 0), 'bin_max': (255, 255, 55)} # Wall binarizatin parameters

POINT_SHIFT = { # Point shift for wall movement, for clockwise direction (in ccw they will be inverted)
    MARKER_RED: -15,
    MARKER_GREEN: +15,
    MARKER_NONE: 0
}

QUALIFICATION_SECTOR_BORDERS = (35, 70) # Rnage of distance to wall for central sector (qualification mode)