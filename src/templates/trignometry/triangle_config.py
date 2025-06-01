from manim import PI, DEGREES, LEFT, RIGHT, UP, DOWN, ORIGIN
from math import acos

ROTATION_CONFIG = {
    "top_right": PI,
    "top_left": -PI / 2,
    "bottom_right": PI / 2,
    "bottom_left": 0,
    "perpendicular_foot": 0
}

ANGLE_CONFIG = {
    "top_right": {
        "alpha": {"angle": 235 * DEGREES, "arrow_start": "right", "arrow_radius": -PI / 3},
        "beta": {"angle": -155 * DEGREES, "arrow_start": "right", "arrow_radius": PI / 3},
    },
    "top_left": {
        "alpha": {"angle": 5 * DEGREES, "arrow_start": "left", "arrow_radius": -PI / 3},
        "beta": {"angle": -85 * DEGREES, "arrow_start": "left", "arrow_radius": PI / 3},
    },
    "bottom_right": {
        "alpha": {"angle": -25 * DEGREES, "arrow_start": "right", "arrow_radius": -PI / 3},
        "beta": {"angle": -155 * DEGREES, "arrow_start": "down", "arrow_radius": PI / 3},
    },
    "bottom_left": {
        "alpha": {"angle": 200 * DEGREES, "arrow_start": "up", "arrow_radius": PI / 3},
        "beta": {"angle": -155 * DEGREES, "arrow_start": "left", "arrow_radius": PI / 3},
    },
    "perpendicular_foot": {
        "alpha": {"angle": -65 * DEGREES, "arrow_start": "right", "arrow_radius": PI / 3},
        "beta": {"angle": -45 * DEGREES, "arrow_start": "down", "arrow_radius": -PI / 3},
    }
}

SIDE_NAMES_CONFIG = {
    "alpha": {"a": "opp", "b": "adj", "c": "hyp"},
    "beta":  {"a": "adj", "b": "opp", "c": "hyp"},
}

SIDE_EDGE_CONFIG = {
    "top_right": {"a": LEFT, "b": DOWN},
    "top_left": {"a": DOWN, "b": RIGHT},
    "bottom_right": {"a": UP, "b": LEFT},
    "bottom_left": {"a": RIGHT, "b": UP, "c": DOWN},
    "perpendicular_foot": {"a": ORIGIN, "b": ORIGIN, "h": RIGHT},
}
