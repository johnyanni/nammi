"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from fractions import Fraction
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from .annotation import Annotation
from .smart_tex import *
from .custom_axes import CustomAxes

from functools import partial, partialmethod


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