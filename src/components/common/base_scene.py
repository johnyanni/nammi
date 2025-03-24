"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from fractions import Fraction
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from .smart_tex import *
from src.components.styles.constants import *

# Common settings
BACKGROUND_COLOR = ManimColor("#121212")

class MathTutorialScene(VoiceoverScene):
    """Base scene class that handles Azure voiceover setup."""
    
    def __init__(self):
        """Initialize the scene."""
        super().__init__()
    
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

    def color_component(self, formula, component, color):
        """Color a component in a formula.
        
        Args:
            formula: The MathTex object containing the formula
            component: The character to color (e.g., "m" or "b")
            color: The color to use
        """
        char = formula[0][search_shape_in_text(formula, MathTex(component))[0]]
        char.set_color(color)
        return char
    
    def highlight_formula_component(self, formula, component, color, duration=1):
        """Highlight a component in a formula with an arrow and indication.
        
        Args:
            formula: The MathTex object containing the formula
            component: The character to highlight (e.g., "m" or "b")
            color: The color to use for highlighting
            duration: How long to show the highlight
        """
        char = formula[0][search_shape_in_text(formula, MathTex(component))[0]]
        char.set_color(color)
        
        arrow = Arrow(
            start=char.get_top() + UP * 0.8,
            end=char.get_top() + UP * 0.10,
            buff=0.05,
            color=color,
            stroke_width=6,
            tip_shape=ArrowTriangleFilledTip,
            max_tip_length_to_length_ratio=0.4
        )
        
        self.play(GrowArrow(arrow))
        self.play(Indicate(char, color=color, scale_factor=1.8))
        self.wait(duration)
        self.play(FadeOut(arrow))

    def apply_smart_colorize(self, elements, color_map):
        """Apply SmartColorizeStatic to a list of elements using the given color map.
        
        Args:
            elements: List of Manim mobjects to colorize
            color_map: Dictionary mapping text patterns to colors
        """
        for element in elements:
            SmartColorizeStatic(element, color_map)
            
            
            
            
    def setup_smart_coloring(self, elements_and_patterns, color_dict):
        """Create a smart coloring list based on elements and patterns.
        
        Args:
            elements_and_patterns: Dictionary mapping elements to lists of patterns to color
            color_dict: Dictionary mapping pattern strings to colors
            
        Returns:
            List of (element, color_map) tuples for use with apply_element_specific_coloring
            
        Example:
            elements_and_patterns = {
                step2_info_1: [r"\text{rise}", r"\text{run}"],
                step4_info_2: [r"\frac{1}{2}", "1"]
            }
            
            color_dict = {
                r"\text{rise}": rise_color,
                r"\text{run}": run_color,
                r"\frac{1}{2}": slope_color,
                "1": y_intercept_color
            }
        """
        smart_coloring = []
        
        for element, patterns in elements_and_patterns.items():
            # Create a specific color map for this element
            element_color_map = {}
            for pattern in patterns:
                if pattern in color_dict:
                    element_color_map[pattern] = color_dict[pattern]
            
            # Add to the smart coloring list if we have mappings
            if element_color_map:
                smart_coloring.append((element, element_color_map))
                
        return smart_coloring

    def apply_element_specific_coloring(self, coloring_list):
        """Apply different color maps to specific elements.
        
        Args:
            coloring_list: List of tuples (element, color_map) where each element 
                          gets its own specific color mapping
                          
        Example:
            smart_coloring = [
                (step2_info_1, {r"\text{rise}": rise_color, r"\text{run}": run_color}),
                (step4_info_2, {r"\frac{1}{2}": slope_color, "1": y_intercept_color})
            ]
            self.apply_element_specific_coloring(smart_coloring)
        """
        for element, color_map in coloring_list:
            SmartColorizeStatic(element, color_map)
            

    def create_step(self, title, *content, buff=0.3):
        """Create a vertical group of elements with consistent formatting.
        
        Args:
            title: Title mobject for the step
            *content: Variable number of content mobjects to include
            buff: Buffer space between elements
            
        Returns:
            VGroup containing the title and content arranged vertically
        """
        return VGroup(title, *content).arrange(DOWN, aligned_edge=LEFT, buff=buff) 


    def create_axes(self, x_range=[-6, 6, 1], y_range=[-6, 6, 1], x_length=6, y_length=6):
        """Create standardized axes with customizable ranges and lengths.
        
        Args:
            x_range: List of [min, max, step] for x-axis (default: [-6, 6, 1])
            y_range: List of [min, max, step] for y-axis (default: [-6, 6, 1])
            x_length: Length of x-axis in screen units (default: 6)
            y_length: Length of y-axis in screen units (default: 6)
            
        Returns:
            Tuple of (axes, axes_labels) where axes is the Axes object and axes_labels is a VGroup
            containing the x and y labels
            
        Examples:
            # For a larger coordinate plane
            axes, axes_labels = self.create_axes(x_range=[-10, 10, 1], y_range=[-10, 10, 1], x_length=8, y_length=8)

            # For a smaller coordinate plane
            axes, axes_labels = self.create_axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=4, y_length=4)
        """
        
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_ticks": True,
                "numbers_to_exclude": [0],
                "tip_length": 0.2,
                "tip_width": 0.2,
                "font_size": 20,
            },
            tips=True
        ).to_edge(RIGHT)

        axes_labels = VGroup(
            axes.get_x_axis_label("x"),
            axes.get_y_axis_label("y")
        )
        
        return axes, axes_labels

    def create_text_with_background(self, text, text_color=WHITE, background_color=BLACK, border_color=None, 
                                  background_opacity=1, border_opacity=1, border_width=2, buff=0.2, 
                                  corner_radius=0.1):
        """Creates a text object with a customizable background and border.
        
        Args:
            text: The text to display (can be MathTex, Tex, or Text)
            text_color: Color of the text (default: WHITE)
            background_color: Color of the background (default: BLACK)
            border_color: Color of the border (default: None, uses background_color)
            background_opacity: Opacity of the background (default: 1)
            border_opacity: Opacity of the border (default: 1)
            border_width: Width of the border line (default: 2)
            buff: Padding around the text (default: 0.15)
            corner_radius: Radius of the corners (default: 0.0 for sharp corners)
            
        Returns:
            VGroup: A group containing the background and text
        """
        # Convert string to MathTex if needed
        if isinstance(text, str):
            text = MathTex(text, color=text_color)
            
        # Create the background rectangle
        background = SurroundingRectangle(
            text,
            color=border_color if border_color else background_color,
            fill_color=background_color,
            fill_opacity=background_opacity,
            stroke_width=border_width,
            corner_radius=corner_radius,
            buff=buff
        )
        
        # Set border opacity if specified
        if border_opacity != 1:
            background.set_stroke(opacity=border_opacity)
            
        # Group the background and text
        return VGroup(background, text)


