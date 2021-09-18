from consts import *


#   Направление:
#       Последний маркер:
#           Следующий маркер:

MANEUVERS = {
    DIRECTION_CW: {
        MARKER_GREEN: {
            MARKER_RED: (300, 50, 4000),
            MARKER_GREEN: (800, 50, 4000),
            MARKER_NONE: (1200, 50, 4000),
        },
        MARKER_RED: {
            MARKER_RED: (800, 50, 4000),
            MARKER_GREEN: (3500, 50, 3100),
            MARKER_NONE: (2800, 50, 3100),
        },
        MARKER_NONE: {
            MARKER_RED: (0, 50, 700),
            MARKER_GREEN: (200, 50, 400),
            MARKER_NONE: (0, 50, 4000),
        }
    },
    DIRECTION_CCW: {
        MARKER_GREEN: {
            MARKER_GREEN: (0, -50, 800),
            MARKER_NONE: (250, -50, 800),
        },
        MARKER_RED: {
            MARKER_GREEN: (50, -50, 800),
            MARKER_NONE: (250, -50, 800),
        },
        MARKER_NONE: {
            MARKER_GREEN: (25, -50, 800),
            MARKER_NONE: (250, -50, 800),
        }
    }
} 

QUALIFICATION_MANEUVER = {
    DIRECTION_CW: (300, 50, 700),
    DIRECTION_CCW: (300, -50, 700),
}
