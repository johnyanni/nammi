"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from .smart_tex import *

# Common settings
BACKGROUND_COLOR = "#121212"

class MathTutorialScene(VoiceoverScene):
    """Base scene class that handles Azure voiceover setup."""
    
    def setup(self):
        """Setup Azure voice configuration and common scene settings."""
        super().setup()
        # Set up Azure voice
        self.set_speech_service(
            AzureService(
                voice="en-US-DerekMultilingualNeural",
                prosody={
                    "rate": "-15%",  # Slower for better comprehension
                }
            )
        )
        
        # Set common scene settings
        self.camera.background_color = BACKGROUND_COLOR 

def apply_smart_colorize(elements, color_map):
    """Apply SmartColorizeStatic to a list of elements using the given color map.
    
    Args:
        elements: List of Manim mobjects to colorize
        color_map: Dictionary mapping text patterns to colors
    """
    for element in elements:
        SmartColorizeStatic(element, color_map)

def create_step(title, *content, buff=0.3):
    """Create a vertical group of elements with consistent formatting.
    
    Args:
        title: Title mobject for the step
        *content: Variable number of content mobjects to include
        buff: Buffer space between elements
        
    Returns:
        VGroup containing the title and content arranged vertically
    """
    return VGroup(title, *content).arrange(DOWN, aligned_edge=LEFT, buff=buff) 