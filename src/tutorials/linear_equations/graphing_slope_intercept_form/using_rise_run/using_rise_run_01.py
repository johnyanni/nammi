"""Tutorial on graphing linear equations using slope-intercept form."""

from manim import *
from src.templates.linear_equations.graphing_slope_intercept_form.t_using_rise_run import GraphSlopeInterceptFormUsingRiseRunTemplate


class UsingRiseRun01(GraphSlopeInterceptFormUsingRiseRunTemplate):
    """A tutorial that teaches how to graph a linear equation using slope-intercept form."""
    
    
    # Core equation values
    SLOPE = -3/4                        # The slope value as a fraction
    Y_INTERCEPT = 3                     # The y-intercept value as a number
    EQUATION_FORMATTED = "y=-\\frac{3}{4}x+3"  # Formatted equation with LaTeX

    # Display and spoken representations
    SLOPE_DISPLAY = "-\\frac{3}{4}"     # How the slope appears in LaTeX
    SLOPE_SPOKEN = "negative three fourths"  # How the slope should be spoken in voiceover
    Y_INTERCEPT_DISPLAY = "3"           # How the y-intercept appears in LaTeX
    Y_INTERCEPT_SPOKEN = "three"        # How the y-intercept should be spoken
    SPOKEN_EQUATION = "y equals negative three fourths x plus three"  # Spoken version for voiceover

    # Animation indices for transformations
    SLOPE_SRC_INDICES = [2, 6]          # Source indices in problem_text_equation for slope
    SLOPE_TGT_INDICES = [-2, None]      # Target indices in step1_info_2 for slope value
    Y_INTERCEPT_SRC_INDICES = [-1, None]  # Source indices in problem_text_equation for y-intercept
    Y_INTERCEPT_TGT_INDICES = [-1, None]  # Target indices in step1_info_3 for y-intercept value
    COORD_SRC_INDICES = [-5, None]
    COORD_TGT_INDICES = [-5, None]

    # Coordinate points and visual ranges
    Y_INTERCEPT_POINT = [0, 3]          # Coordinates of y-intercept point
    SECOND_POINT = [4, 0]               # Coordinates of second point (run 4, rise -3)
    AXES_RANGE = [-4, 8, 1]             # Range for axes: [min, max, step]
    X_LINE_RANGE = [-3.5, 7.5]          # X-range for plotting the line

    # Rise and run values for slope visualization
    RISE_VALUE = 3                      # Simple rise value (absolute value of slope numerator)
    RISE_SPOKEN = "three"               # Spoken version of rise value
    RUN_VALUE = 4                       # Simple run value (slope denominator)
    RUN_SPOKEN = "four"                 # Spoken version of run value
    RISE_DIRECTION = "DOWN"             # Direction for rise: "UP" or "DOWN"
    RUN_DIRECTION = "RIGHT"             # Direction for run: "LEFT" or "RIGHT"

    # UI elements and styling
    TIP_MESSAGE = "When the slope (m) is negative, we go down (rise) and then to the right (run)."
    Y_INTERCEPT_COLOR = YELLOW
    SLOPE_COLOR = GREEN
    RISE_COLOR = BLUE
    RUN_COLOR = RED
    LINE_COLOR = WHITE

