"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from fractions import Fraction
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from .smart_tex import *
from .custom_axes import CustomAxes


MATH_SCALE = 0.60
MATH_SCALE_SMALL = 0.55
TEXT_SCALE = 0.55

TEX_SCALE = 0.70

FOOTNOTE_SCALE = 0.6


QUICK_PAUSE = 0.5
STANDARD_PAUSE = 1.0
COMPREHENSION_PAUSE = 2.0


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

    def color_component(self, formula, component, color, index=0):
        """Color a component in a formula.
        
        Args:
            formula: The MathTex object containing the formula
            component: The character to color (e.g., "m" or "b")
            color: The color to use
            index: Which occurrence of the component to color (default: 0 for first occurrence)
        """
        char = formula[0][search_shape_in_text(formula, MathTex(component))[index]]
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


    # ------------------------------------------------------------
    # QUADRATICS TEMPLATE 
    # ------------------------------------------------------------

    def create_labeled_step(
                self,
                label_text,
                expressions,
                color_map=None,
                label_color=GREY,
                label_scale=0.5,
                label_buff=0.2,
        ):
            label = Tex(label_text, color=label_color).scale(label_scale)
            exp_group = expressions
                
            if color_map:
                self.apply_smart_colorize(exp_group, color_map)
                
            return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
        
    def create_surrounding_rectangle(
            self,
            mobject,
            color="#9A48D0",
            corner_radius=0.1, buff=0.1
    ):
        return SurroundingRectangle(mobject, color=color, corner_radius=corner_radius, buff=buff)
    
    
    def indicate(self, mobject, color="#9A48D0", run_time=2.0):
        """Indicate a mobject with a color."""
        return Indicate(mobject, color=color, run_time=run_time)
    
    
    def get_elements(self, equation, element_text, color=None, opacity=None, occurrence=None):
        """
        Helper function to isolate elements from a MathTex or Tex object.
        
        Args:
            equation: The MathTex or Tex object containing the expression
            element_text: The text of the element to isolate (e.g., "x", "1")
            color: Optional color to apply to the elements
            opacity: Optional opacity to set for the elements
            occurrence: Optional specific occurrence to return (0-based index)
                    None returns all occurrences as a list
                    Integer returns that specific occurrence (0=first, 1=second, etc.)
        
        Returns:
            If occurrence is None: List of all matching components
            If occurrence is int: The specific component at that occurrence
            Returns empty list or None if not found
        """
        indices = search_shape_in_text(equation, MathTex(element_text))
        
        if not indices or len(indices) == 0:
            print(f"Warning: Could not find '{element_text}' in the expression")
            return [] if occurrence is None else None
        
        # If a specific occurrence is requested
        if occurrence is not None:
            if occurrence < 0 or occurrence >= len(indices):
                print(f"Warning: Requested occurrence {occurrence} is out of range (0-{len(indices)-1})")
                return None
            
            element = equation[0][indices[occurrence]]
            if color:
                element.set_color(color)
            if opacity is not None:
                element.set_opacity(opacity)
            return element
        
        # Return all occurrences
        elements = []
        for idx in indices:
            element = equation[0][idx]
            if color:
                element.set_color(color)
            if opacity is not None:
                element.set_opacity(opacity)
            elements.append(element)
        
        return elements





    def find_element(self, pattern, exp, nth=0, as_group=False, color=None, opacity=None):
        """
        Find a specific occurrence of a pattern within an expression.
        
        Args:
            pattern: The text pattern to search for (e.g., "x", "1")
            exp: The MathTex or Tex object to search within
            nth: Which occurrence to return (0-based index)
            as_group: If True, returns the element wrapped in a VGroup
            color: Optional color to set for the element
            opacity: Optional opacity to set for the element
        
        Returns:
            The matching element, or a VGroup containing the element if as_group=True
            None if not found
        """
        indices = search_shape_in_text(exp, MathTex(pattern))
        if not indices or nth >= len(indices):
            print(f"Warning: Could not find occurrence {nth} of '{pattern}'")
            return None
        
        element = exp[0][indices[nth]]
        
        if color:
            element.set_color(color)
        
        if opacity is not None:
            element.set_opacity(opacity)
        
        return VGroup(element) if as_group else element


    def find_elements(self, pattern, exp, as_group=True, color=None, opacity=None):
        """
        Find all occurrences of a pattern within an expression.
        
        Args:
            pattern: The text pattern to search for (e.g., "x", "1")
            exp: The MathTex or Tex object to search within
            as_group: If True, returns all elements as a VGroup
            color: Optional color to set for all found elements
            opacity: Optional opacity to set for all found elements
        
        Returns:
            A VGroup of all matching elements if as_group=True
            A list of all matching elements if as_group=False
            None if no matches found
        """
        indices = search_shape_in_text(exp, MathTex(pattern))
        if not indices:
            print(f"Warning: No occurrences of '{pattern}' found")
            return None
        
        elements = []
        for idx in indices:
            element = exp[0][idx]
            
            if color:
                element.set_color(color)
            
            if opacity is not None:
                element.set_opacity(opacity)
                
            elements.append(element)
        
        return VGroup(*elements) if as_group else elements
    
    
    def add_annotations(self, term_added, left_term, right_term, color=None, h_spacing=0):
        terms = VGroup(*[MathTex(rf"{term_added}").scale(FOOTNOTE_SCALE) for _ in range(2)])
        if color:
            terms.set_color(color)
            
        terms[0].next_to(left_term, DOWN)
        terms[1].next_to(right_term, DOWN)
        
        # Apply horizontal spacing adjustment
        terms[0].shift(LEFT * h_spacing)  # Move left annotation further left
        terms[1].shift(RIGHT * h_spacing)  # Move right annotation further right
        
        
        if terms[0].get_y() < terms[1].get_y():
            terms[1].align_to(terms[0], DOWN)
        else:
            terms[0].align_to(terms[1], DOWN)

        return terms

