"""Specialized overlay for demonstrating slope concepts."""

from manim import *
from .full_screen_overlay import FullScreenOverlay

class SlopeOverlay(FullScreenOverlay):
    """Overlay that demonstrates positive and negative slopes."""
    
    def __init__(self, body_text="Understanding Slope Direction", **kwargs):
        """Initialize a slope overlay with examples.
        
        Args:
            body_text: Text to display at the top
            **kwargs: Additional arguments passed to FullScreenOverlay
        """
        super().__init__(body_text, **kwargs)
        
        # Create smaller axes for examples
        axes_config = {
            "x_range": [-3, 3, 1],
            "y_range": [-3, 3, 1],
            "x_length": 4,
            "y_length": 4,
            "axis_config": {
                "color": WHITE,
                "include_ticks": True,
                "tick_size": 0.05,
                "font_size": 16,
            },
            "tips": False
        }
        
        # Create left axes (negative slope)
        left_axes = Axes(**axes_config)
        left_axes.shift(LEFT * 3.5)
        
        # Create line with negative slope (y = -x)
        negative_line = Line(
            start=left_axes.c2p(-2, 2),
            end=left_axes.c2p(2, -2),
            color=RED,
            stroke_width=3
        )
        
        # Label for negative slope
        negative_label = MathTex(r"\text{Negative Slope}", color=RED, font_size=30)
        negative_label.next_to(left_axes, DOWN, buff=0.5)
        
        # Create right axes (positive slope)
        right_axes = Axes(**axes_config)
        right_axes.shift(RIGHT * 3.5)
        
        # Create line with positive slope (y = x)
        positive_line = Line(
            start=right_axes.c2p(-2, -2),
            end=right_axes.c2p(2, 2),
            color=GREEN,
            stroke_width=3
        )
        
        # Label for positive slope
        positive_label = MathTex(r"\text{Positive Slope}", color=GREEN, font_size=30)
        positive_label.next_to(right_axes, DOWN, buff=0.5)
        
        # Group the examples
        examples_group = VGroup(
            left_axes, negative_line, negative_label,
            right_axes, positive_line, positive_label
        )
        
        # Position the examples group in the center of the screen
        examples_group.center()
        examples_group.shift(DOWN * 0.5)
        
        # Add examples to the overlay
        self.add_content(examples_group) 