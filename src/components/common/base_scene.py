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
TEX_SCALE = 0.75


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
                label_color="#DBDBDB",
                label_scale=0.6,
                label_buff=0.2,
        ):
            label = Tex(label_text, color=label_color).scale(label_scale)
            exp_group = expressions
                
            if color_map:
                self.apply_smart_colorize(exp_group, color_map)
                
            return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
    # def create_multi_exp_labeled_step(
    #         self,
    #         label_text,
    #         *expressions,
    #         color_map=None,
    #         label_color="#DBDBDB",
    #         label_scale=0.6,
    #         label_buff=0.2,
    #         exps_buff=0.2,
    #     ):
    #         label = Tex(label_text, color=label_color).scale(label_scale)
    #         exp_group = VGroup(expressions).arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
    #         if color_map:
    #             self.apply_smart_colorize(exp_group, color_map)

    #         return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
        
        
    def create_multi_exp_labeled_step(
        self,
        label_text,
        *expressions,
        color_map=None,
        label_color="#DBDBDB",
        label_scale=0.6,
        label_buff=0.2,
        exps_buff=0.2,
    ):
        label = Tex(label_text, color=label_color).scale(label_scale)
        # Fix: Use * to unpack the expressions instead of passing them as a tuple
        exp_group = VGroup(*expressions).arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)

        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
        
    def create_labeled_step_alt(
                self,
                label_text,
                expressions,
                color_map=None,
                label_color="#757575",
                label_scale=0.6,
                label_buff=0.15,
                eq_hbuff=0.2,
                tex_scale=TEX_SCALE
        ):
            label = Tex(label_text, color=label_color).scale(label_scale)
            exp_group = VGroup(*[MathTex(exp).scale(tex_scale) for exp in expressions])
            exp_group.arrange(RIGHT, buff=eq_hbuff)
            
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
    
    
    
    
    def create_callout(
            self,
            text,
            target,
            position=UP,
            color=TEAL,
            text_scale=0.55,
            buff=0.2,
            animate=True,
            run_time=1,
    ):
        """
        Creates and animates a callout with highlighting behavior.

        Parameters:
        -----------
        text : str
            The text to display in the callout
        target : Mobject
            The object to highlight and position the callout near
        position : np.array or UP/DOWN/LEFT/RIGHT, default=UP
            Direction to place the callout relative to target
        color : color, default=TEAL
            Color for highlighting and callout text
        text_scale : float, default=0.55
            Scale of the callout text
        buff : float, default=0.2
            Space between callout and target
        animate : bool, default=True
            Whether to animate the callout appearance
        run_time : float, default=1
            Duration of the animation

        Returns:
        --------
        CalloutManager : A class with methods to show and hide the callout
        """
        # Store original properties
        original_color = target.get_color()

        callout_text = Tex(text, color=color).scale(text_scale)

        background_width = callout_text.width + 0.4
        background_height = callout_text.height + 0.4

        rounded_background = RoundedRectangle(
            width=background_width,
            height=background_height,
            corner_radius=0.15,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0,
        )

        rounded_background.move_to(callout_text.get_center())

        callout = VGroup(rounded_background, callout_text)
        callout.next_to(target, position, buff=buff)
        callout.set_z_index(10)

        # Create a manager class for this specific callout
        class CalloutManager:
            def __init__(
                self, scene, callout_obj, target_obj, orig_color, position, buff
            ):
                self.scene = scene
                self.callout = callout_obj
                self.target = target_obj
                self.original_color = orig_color
                self.is_visible = False
                self.position = position
                self.buff = buff

                self.callout.add_updater(
                    lambda m: m.next_to(target_obj, position, buff=buff)
                )

            def show(self, run_time=1):
                """Show the callout and highlight the target"""
                animations = []

                # Only change color if it's not already highlighted
                if self.target.get_color() != color:
                    animations.append(self.target.animate.set_color(color))

                if not self.is_visible:
                    animations.append(FadeIn(self.callout))
                    self.is_visible = True

                if animations:
                    self.scene.play(*animations, run_time=run_time)
                return self

            def hide(self, run_time=1):
                """Hide the callout and restore original color"""
                animations = []

                if self.target.get_color() != self.original_color:
                    animations.append(
                        self.target.animate.set_color(self.original_color)
                    )

                if self.is_visible:
                    animations.append(FadeOut(self.callout))
                    self.is_visible = False

                if animations:
                    self.scene.play(*animations, run_time=run_time)
                return self

            def add_to_scene(self):
                """Just add the callout to the scene without animation"""
                self.scene.add(self.callout)
                # Also update target color
                self.target.set_color(color)
                self.is_visible = True
                return self

            def get_callout(self):
                """Return the callout object"""
                return self.callout

        # Create the manager
        manager = CalloutManager(self, callout, target, original_color, position, buff)

        # Animate if requested
        if animate:
            manager.show(run_time=run_time)

        return manager


    # def find_element(self, pattern, exp, nth=0, as_group=False, color=None, opacity=None):
    #     """
    #     Find a specific occurrence of a pattern within an expression.
        
    #     Args:
    #         pattern: The text pattern to search for (e.g., "x", "1")
    #         exp: The MathTex or Tex object to search within
    #         nth: Which occurrence to return (0-based index)
    #         as_group: If True, returns the element wrapped in a VGroup
    #         color: Optional color to set for the element
    #         opacity: Optional opacity to set for the element
        
    #     Returns:
    #         The matching element, or a VGroup containing the element if as_group=True
    #         None if not found
    #     """
    #     try:
    #         # Create a temporary MathTex object for matching
    #         # We don't add this to the scene - it's just for pattern matching
    #         pattern_tex = MathTex(pattern)
            
    #         # Find the pattern in the expression
    #         indices = search_shape_in_text(exp, pattern_tex)
            
    #         if not indices or nth >= len(indices):
    #             print(f"Warning: Could not find occurrence {nth} of '{pattern}'")
    #             return None
            
    #         # Get the specific element
    #         element = exp[0][indices[nth]]
            
    #         # Apply color and opacity if specified
    #         if color:
    #             element.set_color(color)
            
    #         if opacity is not None:
    #             element.set_opacity(opacity)
            
    #         # Return as appropriate format
    #         return VGroup(element) if as_group else element
            
    #     except Exception as e:
    #         print(f"Error finding pattern '{pattern}': {e}")
    #     return None
    
    

    # def find_element(self, pattern, exp, nth=0, as_group=False, color=None, opacity=None):
    #     """
    #     Find a specific occurrence of a pattern within an expression.
        
    #     Args:
    #         pattern: The text pattern to search for (e.g., "x", "1")
    #         exp: The MathTex or Tex object to search within
    #         nth: Which occurrence to return (0-based index)
    #         as_group: If True, returns the element wrapped in a VGroup
    #         color: Optional color to set for the element
    #         opacity: Optional opacity to set for the element
        
    #     Returns:
    #         The matching element, or a VGroup containing the element if as_group=True
    #         None if not found
    #     """
    #     indices = search_shape_in_text(exp, MathTex(pattern))
    #     if not indices or nth >= len(indices):
    #         print(f"Warning: Could not find occurrence {nth} of '{pattern}'")
    #         return None
        
    #     element = exp[0][indices[nth]]
        
    #     # Apply color if specified
    #     if color is not None:
    #         element.set_color(color)
        
    #     # Apply opacity if specified
    #     if opacity is not None:
    #         element.set_opacity(opacity)
        
    #     # Return element, wrapped in VGroup if requested
    #     if as_group:
    #         return VGroup(element)
    #     return element




    # def find_elements(self, pattern, exp, as_group=True, color=None, opacity=None):
    #     """
    #     Find all occurrences of a pattern within an expression.
        
    #     Args:
    #         pattern: The text pattern to search for (e.g., "x", "1")
    #         exp: The MathTex or Tex object to search within
    #         as_group: If True, returns all elements as a VGroup
    #         color: Optional color to set for all found elements
    #         opacity: Optional opacity to set for all found elements
        
    #     Returns:
    #         A VGroup of all matching elements if as_group=True
    #         A list of all matching elements if as_group=False
    #         None if no matches found
    #     """
    #     indices = search_shape_in_text(exp, MathTex(pattern))
    #     if not indices:
    #         print(f"Warning: No occurrences of '{pattern}' found")
    #         return None
        
    #     elements = []
    #     for idx in indices:
    #         element = exp[0][idx]
            
    #         if color:
    #             element.set_color(color)
            
    #         if opacity is not None:
    #             element.set_opacity(opacity)
                
    #         elements.append(element)
        
    #     return VGroup(*elements) if as_group else elements
    
    


    # def find_adjacent_elements(self, pattern1, pattern2, exp, nth1=0, nth2=0, color=None):
    #     """Find two adjacent patterns and group them together."""
        
    #     # Count occurrences to provide better warnings
    #     indices1 = search_shape_in_text(exp, MathTex(pattern1))
    #     indices2 = search_shape_in_text(exp, MathTex(pattern2))
        
    #     if not indices1:
    #         print(f"Warning: Pattern '{pattern1}' not found in expression")
    #         return None
        
    #     if not indices2:
    #         print(f"Warning: Pattern '{pattern2}' not found in expression")
    #         return None
        
    #     # Validate nth1 is in range
    #     if abs(nth1) > len(indices1):
    #         print(f"Warning: Requested occurrence {nth1} for '{pattern1}' is out of range (found {len(indices1)} occurrences)")
    #         return None
        
    #     # Validate nth2 is in range
    #     if abs(nth2) > len(indices2):
    #         print(f"Warning: Requested occurrence {nth2} for '{pattern2}' is out of range (found {len(indices2)} occurrences)")
    #         return None
        
    #     # Get the elements
    #     elem1 = exp[0][indices1[nth1 % len(indices1)]]
    #     elem2 = exp[0][indices2[nth2 % len(indices2)]]
        
    #     group = VGroup(elem1, elem2)
        
    #     if color:
    #         group.set_color(color)
        
    #     return group
    
    
    
        
    # def find_adjacent_elements(self, first_pattern, second_pattern, exp, color=None, opacity=None):
    #     """
    #     Find two adjacent elements within an expression and return them as a VGroup.
        
    #     Args:
    #         first_pattern: The text pattern to search for first element (e.g., "-")
    #         second_pattern: The text pattern to search for second element (e.g., "5")
    #         exp: The MathTex or Tex object to search within
    #         color: Optional color to set for the elements
    #         opacity: Optional opacity to set for the elements
        
    #     Returns:
    #         A VGroup containing the two adjacent elements
    #         None if not found
    #     """
    #     # Find indices of both patterns
    #     first_indices = search_shape_in_text(exp, MathTex(first_pattern))
    #     second_indices = search_shape_in_text(exp, MathTex(second_pattern))
        
    #     if not first_indices or not second_indices:
    #         print(f"Warning: Could not find '{first_pattern}' or '{second_pattern}'")
    #         return None
        
    #     # Check for adjacency - find pairs where second follows first
    #     adjacent_pairs = []
    #     for first_idx in first_indices:
    #         for second_idx in second_indices:
    #             # Check if they're adjacent (second follows first)
    #             if isinstance(first_idx, slice) and isinstance(second_idx, slice):
    #                 if first_idx.stop == second_idx.start:
    #                     adjacent_pairs.append((first_idx, second_idx))
        
    #     if not adjacent_pairs:
    #         print(f"Warning: No adjacent occurrences of '{first_pattern}' and '{second_pattern}' found")
    #         return None
        
    #     # Use the first adjacent pair found
    #     first_idx, second_idx = adjacent_pairs[0]
        
    #     # Get the elements
    #     first_element = exp[0][first_idx]
    #     second_element = exp[0][second_idx]
        
    #     # Create a VGroup with both elements
    #     result = VGroup(first_element, second_element)
        
    #     # Apply color if specified
    #     if color is not None:
    #         result.set_color(color)
        
    #     # Apply opacity if specified
    #     if opacity is not None:
    #         result.set_opacity(opacity)
        
    #     return result
    
    
    
    # def find_adjacent_elements(self, first_pattern, second_pattern, exp, nth=0, color=None, opacity=None):
    #     """
    #     Find the nth occurrence of two adjacent elements within an expression and return them as a VGroup.
        
    #     Args:
    #         first_pattern: The text pattern to search for first element (e.g., "-")
    #         second_pattern: The text pattern to search for second element (e.g., "5")
    #         exp: The MathTex or Tex object to search within
    #         nth: Which occurrence to find (default: 0)
    #         color: Optional color to set for the elements
    #         opacity: Optional opacity to set for the elements
        
    #     Returns:
    #         A VGroup containing the two adjacent elements
    #         None if not found
    #     """
    #     # Find indices of both patterns
    #     first_indices = search_shape_in_text(exp, MathTex(first_pattern))
    #     second_indices = search_shape_in_text(exp, MathTex(second_pattern))
        
    #     if not first_indices or not second_indices:
    #         print(f"Warning: Could not find '{first_pattern}' or '{second_pattern}'")
    #         return None
        
    #     # Check for adjacency - find pairs where second follows first
    #     adjacent_pairs = []
    #     for first_idx in first_indices:
    #         for second_idx in second_indices:
    #             # Check if they're adjacent (second follows first)
    #             if isinstance(first_idx, slice) and isinstance(second_idx, slice):
    #                 if first_idx.stop == second_idx.start:
    #                     adjacent_pairs.append((first_idx, second_idx))
        
    #     if not adjacent_pairs or nth >= len(adjacent_pairs):
    #         print(f"Warning: No adjacent occurrences at index {nth} of '{first_pattern}' and '{second_pattern}' found")
    #         return None
        
    #     # Use the nth adjacent pair found
    #     first_idx, second_idx = adjacent_pairs[nth]
        
    #     # Get the elements
    #     first_element = exp[0][first_idx]
    #     second_element = exp[0][second_idx]
        
    #     # Create a VGroup with both elements
    #     result = VGroup(first_element, second_element)
        
    #     # Apply color if specified
    #     if color is not None:
    #         result.set_color(color)
        
    #     # Apply opacity if specified
    #     if opacity is not None:
    #         result.set_opacity(opacity)
        
    #     return result
    
    
    
    
    # def find_element(self, pattern, exp, nth=0, color=None, opacity=None, as_group=False):
    #     """
    #     Enhanced find_element that automatically handles negative numbers and other patterns.
        
    #     Args:
    #         pattern: The text pattern to search for (e.g., "x", "1", "-5")
    #         exp: The MathTex or Tex object to search within
    #         nth: Which occurrence to return (0-based index)
    #         color: Optional color to set for the element
    #         opacity: Optional opacity to set for the element
    #         as_group: If True, returns the element wrapped in a VGroup
        
    #     Returns:
    #         The matching element, or a VGroup containing the element if as_group=True
    #         None if not found
    #     """
    #     # First try direct search
    #     try:
    #         indices = search_shape_in_text(exp, MathTex(pattern))
    #         if indices and nth < len(indices):
    #             element = exp[0][indices[nth]]
                
    #             if color is not None:
    #                 element.set_color(color)
                
    #             if opacity is not None:
    #                 element.set_opacity(opacity)
                
    #             return VGroup(element) if as_group else element
    #     except Exception:
    #         pass  # If direct search fails, try adjacent elements approach
        
    #     # If pattern looks like it might be a negative number, try adjacent search
    #     if pattern.startswith('-') and len(pattern) > 1:
    #         try:
    #             num_part = pattern[1:]  # Remove the minus sign
    #             minus_indices = search_shape_in_text(exp, MathTex("-"))
    #             num_indices = search_shape_in_text(exp, MathTex(num_part))
                
    #             # Find adjacent pairs
    #             adjacent_pairs = []
    #             for minus_idx in minus_indices:
    #                 for num_idx in num_indices:
    #                     if isinstance(minus_idx, slice) and isinstance(num_idx, slice):
    #                         if minus_idx.stop == num_idx.start:
    #                             adjacent_pairs.append((minus_idx, num_idx))
                
    #             if adjacent_pairs and nth < len(adjacent_pairs):
    #                 minus_idx, num_idx = adjacent_pairs[nth]
    #                 minus_element = exp[0][minus_idx]
    #                 num_element = exp[0][num_idx]
                    
    #                 # Create a group with both elements
    #                 result = VGroup(minus_element, num_element)
                    
    #                 if color is not None:
    #                     result.set_color(color)
                    
    #                 if opacity is not None:
    #                     result.set_opacity(opacity)
                    
    #                 return result
    #         except Exception:
    #             pass  # If adjacent search fails, fall back to default behavior
        
    #     # If all else fails, warn and return None
    #     print(f"Warning: Could not find occurrence {nth} of '{pattern}'")
    #     return None
    
    
    
    def find_element(self, pattern, exp, nth=0, color=None, opacity=None, as_group=False, context=None):
        """
        Enhanced find_element that automatically handles negative numbers, context, and other patterns.
        
        Args:
            pattern: The text pattern to search for (e.g., "x", "1", "-5")
            exp: The MathTex or Tex object to search within
            nth: Which occurrence to return (0-based index)
            color: Optional color to set for the element
            opacity: Optional opacity to set for the element
            as_group: If True, returns the element wrapped in a VGroup
            context: Optional context pattern to disambiguate elements
                (e.g., "4ac" for finding "a" in "4ac")
        
        Returns:
            The matching element, or a VGroup containing the element if as_group=True
            None if not found
        """
        # If context is provided, try context-aware finding first
        if context:
            try:
                # Find all occurrences of the pattern
                pattern_indices = search_shape_in_text(exp, MathTex(pattern))
                
                if pattern_indices:
                    # Find the context pattern
                    context_indices = search_shape_in_text(exp, MathTex(context))
                    
                    if context_indices:
                        # Find matches within or adjacent to the context
                        context_matches = []
                        for p_idx in pattern_indices:
                            for c_idx in context_indices:
                                # Check if pattern is within or adjacent to the context
                                if isinstance(p_idx, slice) and isinstance(c_idx, slice):
                                    # Within context
                                    if (p_idx.start >= c_idx.start and p_idx.stop <= c_idx.stop):
                                        context_matches.append(p_idx)
                                    # Adjacent to context (just before or after)
                                    elif (abs(p_idx.stop - c_idx.start) <= 1) or (abs(p_idx.start - c_idx.stop) <= 1):
                                        context_matches.append(p_idx)
                        
                        # Use the nth match found in context
                        if context_matches and nth < len(context_matches):
                            element = exp[0][context_matches[nth]]
                            
                            if color is not None:
                                element.set_color(color)
                            
                            if opacity is not None:
                                element.set_opacity(opacity)
                            
                            return VGroup(element) if as_group else element
            except Exception as e:
                print(f"Context search failed: {e}, falling back to standard search")
                # Continue with regular search methods
        
        # First try direct search
        try:
            indices = search_shape_in_text(exp, MathTex(pattern))
            if indices and nth < len(indices):
                element = exp[0][indices[nth]]
                
                if color is not None:
                    element.set_color(color)
                
                if opacity is not None:
                    element.set_opacity(opacity)
                
                return VGroup(element) if as_group else element
        except Exception:
            pass  # If direct search fails, try adjacent elements approach
        
        # If pattern looks like it might be a negative number, try adjacent search
        if pattern.startswith('-') and len(pattern) > 1:
            try:
                num_part = pattern[1:]  # Remove the minus sign
                minus_indices = search_shape_in_text(exp, MathTex("-"))
                num_indices = search_shape_in_text(exp, MathTex(num_part))
                
                # Find adjacent pairs
                adjacent_pairs = []
                for minus_idx in minus_indices:
                    for num_idx in num_indices:
                        if isinstance(minus_idx, slice) and isinstance(num_idx, slice):
                            if minus_idx.stop == num_idx.start:
                                adjacent_pairs.append((minus_idx, num_idx))
                
                if adjacent_pairs and nth < len(adjacent_pairs):
                    minus_idx, num_idx = adjacent_pairs[nth]
                    minus_element = exp[0][minus_idx]
                    num_element = exp[0][num_idx]
                    
                    # Create a group with both elements
                    result = VGroup(minus_element, num_element)
                    
                    if color is not None:
                        result.set_color(color)
                    
                    if opacity is not None:
                        result.set_opacity(opacity)
                    
                    return result
            except Exception:
                pass  # If adjacent search fails, fall back to default behavior
        
        # If we get here, both context search and standard searches failed
        print(f"Warning: Could not find occurrence {nth} of '{pattern}'" + 
            (f" within context '{context}'" if context else ""))
        return None
    
    
    
    
    
    def create_annotated_expression(self, main_expr, annotations=None, buff=0.3, h_spacing=0):
        # Create main expression
        if isinstance(main_expr, str):
            expr = MathTex(main_expr).scale(TEX_SCALE)
        else:
            expr = main_expr
        
        # If no annotations, just return the expression
        if not annotations:
            return VGroup(expr)
        
        # Create annotations to measure actual height
        annotation_terms = []
        for text, target1, target2, color in annotations:
            terms = VGroup(*[MathTex(rf"{text}").scale(FOOTNOTE_SCALE) for _ in range(2)])
            if color:
                terms.set_color(color)
            annotation_terms.append(terms)
        
        annotation_height = max(term.height for term in annotation_terms) if annotation_terms else 0.3
        
        # Create placeholder rectangle ONLY for the space below the expression
        placeholder = Rectangle(
            width=expr.width,
            height=buff + annotation_height,  # Only buffer + annotation height
            fill_opacity=0,
            stroke_opacity=0
        )
        
        # Position the placeholder below the expression
        placeholder.next_to(expr, DOWN, buff=0)
        
        # Create the result group with expression and placeholder
        result = VGroup(expr, placeholder)
        
        # Position annotations
        for i, (text, target1, target2, color) in enumerate(annotations):
            terms = annotation_terms[i]
            
            # Find targets
            target1_obj = self.find_element(target1, expr)
            target2_obj = self.find_element(target2, expr)
            
            if target1_obj and target2_obj:
                # Position annotations
                terms[0].next_to(target1_obj, DOWN, buff=buff)
                terms[1].next_to(target2_obj, DOWN, buff=buff)
                
                # Apply horizontal spacing
                if h_spacing != 0:
                    terms[0].shift(LEFT * h_spacing)
                    terms[1].shift(RIGHT * h_spacing)
                
                # Align vertically
                if terms[0].get_y() < terms[1].get_y():
                    terms[1].align_to(terms[0], DOWN)
                else:
                    terms[0].align_to(terms[1], DOWN)
                
                # Add to result
                result.add(terms)
        
        return result

    
    def create_labeled_step_with_annotations(
        self, 
        label_text, 
        expressions,
        annotations=None,
        color_map=None,
        label_color="#DBDBDB",
        label_scale=0.6,
        label_buff=0.2,
        expression_buff=0.2
    ):
        """Create a step with a label, multiple expressions, and annotations between them."""
        # Create the label
        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Create expression mobjects
        expression_mobjects = []
        for expr in expressions:
            if isinstance(expr, str):
                expr_obj = MathTex(expr).scale(TEX_SCALE)
            else:
                expr_obj = expr
            expression_mobjects.append(expr_obj)
        
        # Apply colorization if needed
        if color_map:
            for expr in expression_mobjects:
                self.apply_smart_colorize([expr], color_map)
        
        # Create groups for expressions and their annotations
        expression_groups = []
        annotation_groups = []
        
        # Process each expression
        for i, expr in enumerate(expression_mobjects):
            # For the first expression, check if it has annotations
            if i == 0 and annotations:
                # Create the annotations
                annotation_objs = []
                for text, from_term, to_term, color in annotations:
                    from_element = self.find_element(from_term, expr)
                    to_element = self.find_element(to_term, expr)
                    
                    if from_element and to_element:
                        anno = self.add_annotations(text, from_element, to_element, color=color)
                        annotation_objs.append(anno)
                
                # Group annotations separately
                if annotation_objs:
                    annotation_group = VGroup(*annotation_objs)
                    annotation_groups.append(annotation_group)
                else:
                    annotation_groups.append(None)
                
                # Just add the expression alone
                expression_groups.append(VGroup(expr))
            else:
                expression_groups.append(VGroup(expr))
                annotation_groups.append(None)
        
        # Correctly position the annotations relative to their expressions
        for i, (expr_group, anno_group) in enumerate(zip(expression_groups, annotation_groups)):
            if anno_group:
                # Combine for positioning but don't include annotations in the expression group
                combined = VGroup(expr_group, anno_group)
                # We'll position these manually in the final arrangement
        
        # Arrange expressions vertically
        expressions_vgroup = VGroup(*expression_groups)
        for i, (expr, anno) in enumerate(zip(expression_groups, annotation_groups)):
            if i > 0:
                expr.next_to(expression_groups[i-1], DOWN, buff=expression_buff, aligned_edge=LEFT)
        
        # Position annotations with their expressions
        for expr, anno in zip(expression_groups, annotation_groups):
            if anno:
                # Annotations are already positioned relative to their expression terms
                pass
        
        # Arrange the whole step
        step = VGroup(label)
        for expr, anno in zip(expression_groups, annotation_groups):
            step.add(expr)
            if anno:
                step.add(anno)
        
        # Position the label
        expressions_vgroup = VGroup(*[expr for expr in expression_groups])
        label.next_to(expressions_vgroup, UP, buff=label_buff, aligned_edge=LEFT)
        
        # Create an easy-to-use structure for animations
        result = VGroup(label, expressions_vgroup)
        
        # Add extra attributes for easier access
        result.label = label
        result.expressions = expression_groups
        result.annotations = annotation_groups
        
        return result