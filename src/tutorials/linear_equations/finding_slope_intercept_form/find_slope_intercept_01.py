"""Template for finding equations of lines using slope-intercept form."""

from manim import *
from src.templates.linear_equations.finding_slope_intercept_form.t_find_slope_intercept import FindSlopeInterceptFormTemplate


class FindSlopeInterceptForm01(FindSlopeInterceptFormTemplate):
    """A tutorial that teaches how to find the equation of a line using slope-intercept form."""

# Core equation values and final result
SLOPE = 1/2                         # The slope value as a fraction
Y_INTERCEPT = 1                     # The y-intercept value as a number
FINAL_EQUATION = "y=\\frac{1}{2}x+1"  # Final equation with LaTeX

# Display and spoken representations
SLOPE_DISPLAY = "\\frac{1}{2}"      # How the slope appears in LaTeX
SLOPE_SPOKEN = "one half"           # How the slope should be spoken in voiceover
Y_INTERCEPT_DISPLAY = "1"           # How the y-intercept appears in LaTeX
Y_INTERCEPT_SPOKEN = "one"          # How the y-intercept should be spoken
FINAL_EQUATION_SPOKEN = "y equals one half x plus one"  # Spoken version of the final equation

# Coordinate points
POINT1 = [0, 1]                     # First point [x, y] - typically the y-intercept
POINT2 = [4, 3]                     # Second point [x, y]
USE_Y_INTERCEPT = True              # Whether point1 is the y-intercept

# Rise and run values for slope visualization
RISE_VALUE = 2                      # Simple rise value (numerator of slope after simplification)
RISE_SPOKEN = "two"                 # Spoken version of rise value
RUN_VALUE = 4                       # Simple run value (denominator of slope after simplification)
RUN_SPOKEN = "four"                 # Spoken version of run value
RISE_DIRECTION = "UP"               # Direction for rise: "UP" or "DOWN"
RUN_DIRECTION = "RIGHT"             # Direction for run: "LEFT" or "RIGHT"

# Coordinate plane settings
AXES_RANGE = [-6, 6, 1]             # Range for axes: [min, max, step]
X_LINE_RANGE = [-5, 5]              # X-range for plotting the line

# UI elements and styling
TIP_MESSAGE = "The slope measures how much the line rises or falls as we move from left to right."
Y_INTERCEPT_COLOR = YELLOW
SLOPE_COLOR = GREEN
RISE_COLOR = BLUE
RUN_COLOR = RED
POINT_COLOR = PINK
LINE_COLOR = WHITE

