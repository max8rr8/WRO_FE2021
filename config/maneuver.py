from consts import *


#   Направление:
#       Последний маркер:
#           Следующий маркер:

MANEUVERS = {
    DIRECTION_CW: {
        MARKER_GREEN: {
            MARKER_RED: (25, 50, 700),
            MARKER_NONE: (200, 50, 700),
        },
        MARKER_RED: {
            MARKER_RED: (50, 50, 700),
            MARKER_NONE: (150, 50, 700),
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
            MARKER_NONE: (150, -50, 800),
        }
    }
} 

QUALIFICATION_MANEUVER = {
    DIRECTION_CW: (300, 50, 700),
    DIRECTION_CCW: (300, -50, 700),
}

QUALIFICATION_PRE_FINAL_MANEUVER = {
    DIRECTION_CW: {
        -1: (300, 50, 700),
        00: (300, 50, 700),
        +1: (300, 50, 700)
    },
    DIRECTION_CCW: {
        -1: (300, 50, 700),
        00: (300, 50, 700),
        +1: (300, 50, 700)
    },
}