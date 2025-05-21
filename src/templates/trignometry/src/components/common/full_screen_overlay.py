"""Common full screen overlay component for tutorials."""

from manim import *

class FullScreenOverlay(VGroup):
    """Base class for full screen overlays with text and optional content."""
    
    def __init__(
            self,
            body_text,
            background_color="#121212",
            text_color=WHITE,
            fill_opacity=0.95,
            font_size=40,
            **kwargs
    ):
        """Initialize a full screen overlay with text.
        
        Args:
            body_text: Text to display at the top
            background_color: Color of the background rectangle
            text_color: Color of the text
            fill_opacity: Opacity of the background
            font_size: Size of the text
            **kwargs: Additional arguments passed to VGroup
        """
        super().__init__(**kwargs)
        
        # Create full screen rectangle
        self.full_screen = Rectangle(
            width=16,  # Make wider than the screen
            height=9,  # Make taller than the screen
            fill_color=background_color,
            fill_opacity=fill_opacity,
            stroke_width=0,
        )
        
        # Create text
        self.text = Text(
            body_text,
            color=text_color,
            font_size=font_size
        )
        
        # Position text at the top
        self.text.to_edge(UP, buff=1)
        
        # Add rectangle and text
        self.add(self.full_screen, self.text)
        
        # Center the entire group
        self.center()
        
    def add_content(self, content: VMobject):
        """Add additional content to the overlay.
        
        Args:
            content: VMobject to add to the overlay
        """
        self.add(content)
        return self 