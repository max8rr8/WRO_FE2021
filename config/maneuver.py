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
            MARKER_NONE: (800, 50, 4000),
        }
    },
    DIRECTION_CCW: {
        MARKER_GREEN: {
            MARKER_RED: (1000, -50, 4000),
            MARKER_GREEN: (800, -50, 4500),
            MARKER_NONE: (1200, -50, 4000),
        },
        MARKER_RED: {
            MARKER_RED: (1500, -50, 3100),
            MARKER_GREEN: (0, -50, 4000),
            MARKER_NONE: (2800, -50, 3100),
        },
        MARKER_NONE: {
            MARKER_RED: (2000, -50, 4000),
            MARKER_GREEN: (0, -50, 4000),
            MARKER_NONE: (800, -50, 4000),
        }
    }
}
