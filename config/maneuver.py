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
            MARKER_RED: (25, 50, 700),
            MARKER_NONE: (200, 50, 700),
        },
        MARKER_RED: {
            MARKER_RED: (50, 50, 700),
            MARKER_NONE: (200, 50, 600),
        },
        MARKER_NONE: {
            MARKER_RED: (0, 50, 700),
            MARKER_NONE: (150, 50, 700),
        }
    },
    DIRECTION_CCW: {
        MARKER_GREEN: {
            MARKER_GREEN: (0, -50, 800),
            MARKER_NONE: (250, -50, 800),
        },
        MARKER_RED: {
            MARKER_GREEN: (50, -50, 800),
            MARKER_NONE: (200, -50, 800),
        },
        MARKER_NONE: {
            MARKER_GREEN: (25, -50, 800),
            MARKER_NONE: (150, -50, 600),
        }
    }
}

# Manuvers for qualification turns (for all sections except for 3, 7, 11)
# each maneuver is complex maneuver, format is: (forward_ticks, servo_angle, turn_ticks)
# Dict are aranged in following format:
#   Direction:
QUALIFICATION_MANEUVER = {
    DIRECTION_CW: (100, 50, 600),
    DIRECTION_CCW: (100, -50, 600),
}

# Manuvers for pre-final qualification turns (for 3, 7, 11 section)
# each maneuver is complex maneuver, format is: (forward_ticks, servo_angle, turn_ticks)
# Dict are aranged in following format:
#   Direction:
#      Sector to finish in (-1 near to outer wall, 0 for central sector, 1 for inner wall):
QUALIFICATION_PRE_FINAL_MANEUVER = {
    DIRECTION_CW: {
        -1: (100, 50, 600),
        00: (0, 50, 600),
        +1: (0, 50, 700) # BROKEN
    },
    DIRECTION_CCW: {
        -1: (100, -50, 600),
        00: (0, -50, 700),
        +1: (0, -50, 700) # BROKEN
    },
}