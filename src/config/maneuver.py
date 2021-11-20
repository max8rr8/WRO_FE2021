from consts import *

# Maneuvers for turns
# each maneuver is complex maneuver, format is: (forward_ticks, servo_angle, turn_ticks)
# Dict are aranged in following format:
#   Direction:
#       Last seen marker:
#           Next(side) marker:
MANEUVERS = {
    DIRECTION_CW: {
        MARKER_GREEN: {
            MARKER_RED: (0, 50, 450), 
            MARKER_NONE: (150, 50, 400), 
        },
        MARKER_RED: {
            MARKER_RED: (50, 50, 400), 
            MARKER_NONE: (300, 50, 500), 
        },
        MARKER_NONE: {
            MARKER_RED: (0, 50, 400), 
            MARKER_NONE: (150, 50, 400),
        }
    },
    DIRECTION_CCW: {
        MARKER_GREEN: {
            MARKER_GREEN: (0, -50, 400), 
            MARKER_NONE: (350, -50, 400), 
        },
        MARKER_RED: {
            MARKER_GREEN: (0, -50, 400),
            MARKER_NONE: (200, -50, 400), 
        },
        MARKER_NONE: {
            MARKER_GREEN: (20, -50, 400),
            MARKER_NONE: (300, -50, 400),
        }
    }
}

# Manuvers for qualification turns (for all sections except for 3, 7, 11)
# each maneuver is complex maneuver, format is: (forward_ticks, servo_angle, turn_ticks)
# Dict are aranged in following format:
#   Direction:
QUALIFICATION_MANEUVER = {
    DIRECTION_CW: (180, 50, 500),
    DIRECTION_CCW: (180, -50, 500),
}

# Manuvers for pre-final qualification turns (for 3, 7, 11 section)
# each maneuver is complex maneuver, format is: (forward_ticks, servo_angle, turn_ticks)
# Dict are aranged in following format:
#   Direction:
#      Sector to finish in (-1 near to outer wall, 0 for central sector, 1 for inner wall):
QUALIFICATION_PRE_FINAL_MANEUVER = {
    DIRECTION_CW: {
        -1: (250, 50, 500), #OK2
        00: (150, 50, 600), 
        +1: (0, 50, 700) # BROKEN
    },
    DIRECTION_CCW: {
        -1: (280, -50, 500),
        00: (50, -50, 600), 
        +1: (0, -50, 700) # BROKEN
    },
}