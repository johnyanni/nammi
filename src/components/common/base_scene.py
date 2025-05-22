"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from fractions import Fraction
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from .annotation import Annotation
from .smart_tex import *
from .custom_axes import CustomAxes

from functools import partial, partialmethod

#NEW CONSTANTS

#FONT SIZES
MATH_SCALE = 0.75
TEXT_SCALE = 0.60
LABEL_SCALE = 0.55
ANNOTATION_SCALE = 0.60

#SPACING
LABEL_BUFF = 0.20
EXP_BUFF = 0.25
STEP_BUFF = 0.4




# MATH_SCALE = 0.60
# MATH_SCALE_SMALL = 0.55


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
    
    
    def add_annotations(self, term_added, left_term, right_term, color=RED, h_spacing=0):
        terms = VGroup(*[MathTex(rf"{term_added}").scale(ANNOTATION_SCALE) for _ in range(2)])
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
    
    
    
    def create_annotated_equation(self, equation_text, annotation_text, from_term, to_term, color=RED, scale=MATH_SCALE):
        """Create an equation with annotations in one step.
        
        Args:
            equation_text: Text for the equation
            annotation_text: Text for the annotation (e.g., "\\div 4")
            from_term: Term to annotate from (e.g., "4")
            to_term: Term to annotate to (e.g., "48")
            color: Color for the annotation (default: GREEN)
            scale: Scale for the equation (default: TEX_SCALE)
            
        Returns:
            VGroup containing the equation and its annotations
        """
        equation = MathTex(equation_text).scale(scale)
        
        annotations = self.add_annotations(
            annotation_text,
            self.find_element(from_term, equation),
            self.find_element(to_term, equation),
            color=color
        )
        
        return VGroup(equation, annotations)
    
    
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
    
    def find_element_lazy(self, pattern, nth=0, color=None, opacity=None, as_group=False, context=None):
        return partial(self.find_element, pattern=pattern, nth=nth, color=color, opacity=opacity, as_group=as_group, context=context)
    
    
    
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







        

        
    

   
 
    
    
    
    
    
    
    
    
    
    ### Labeled Steps ###
    
    
    
    # def create_labeled_step_vertical(
    #     self,
    #     label_text,
    #     expressions,
    #     color_map=None,
    #     label_color="#757575",
    #     label_scale=0.6,
    #     label_buff=0.15,
    #     exps_buff=0.2,
    #     tex_scale=TEX_SCALE,
    #     preserve_arrangement=False
    # ):
    #     """Create a labeled step with expressions arranged vertically.
    #     Supports mixed types of expressions (strings and MathTex objects).
    #     """
    #     label = Tex(label_text, color=label_color).scale(label_scale)
        
    #     # Process each expression based on its type
    #     processed_expressions = []
    #     for exp in expressions:
    #         if isinstance(exp, str):
    #             # Convert string to MathTex
    #             processed_expressions.append(MathTex(exp).scale(tex_scale))
    #         else:
    #             # Use pre-created object as is
    #             processed_expressions.append(exp)
        
    #     # Create VGroup and arrange
    #     if isinstance(expressions, VGroup) and preserve_arrangement:
    #         exp_group = expressions
    #     else:
    #         exp_group = VGroup(*processed_expressions)
    #         if not preserve_arrangement:
    #             exp_group.arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        
    #     if color_map:
    #         self.apply_smart_colorize(exp_group, color_map)
            
    #     return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)




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
        

    
    # backward compatibility
    
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







    
    
    
    
    
    
    # final version of multi exp labeled step
    def create_multi_exp_labeled_step_tex(
        self,
        label_text,
        *expressions,
        color_map=None,
        label_color="#757575",
        label_scale=TEXT_SCALE,
        label_buff=0.2,
        exps_buff=0.2,
        default_scale=MATH_SCALE  # Add default_scale parameter
    ):
        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Process expressions to convert strings to MathTex with default scaling
        processed_expressions = []
        for exp in expressions:
            if isinstance(exp, str):
                # Convert string to MathTex with default scaling
                processed_expressions.append(MathTex(exp).scale(default_scale))
            else:
                # Use pre-created object as is
                processed_expressions.append(exp)
        
        # Create VGroup and arrange
        exp_group = VGroup(*processed_expressions).arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)

        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    
    
    
    
    
    # v1 Vertical labeled step without mathtex conversion 
    
    def create_labeled_step_vertical(
        self,
        label_text,
        expressions,
        color_map=None,
        label_color="#757575",
        label_scale=0.6,
        label_buff=0.15,
        exps_buff=0.2,
        preserve_arrangement=False
    ):
        """Create a labeled step with expressions arranged vertically."""
        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Create group and arrange
        if isinstance(expressions, VGroup) and preserve_arrangement:
            exp_group = expressions
        else:
            exp_group = VGroup(*expressions)
            if not preserve_arrangement:
                exp_group.arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)
            
        # Create the final group with label and expressions
        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    

    # v2 version of vertical tex labeled step with mathtex conversion
    
    # def create_labeled_step_vertical_tex(
    #     self,
    #     label_text,
    #     expressions,
    #     color_map=None,
    #     label_color="#757575",
    #     label_scale=TEXT_SCALE,
    #     label_buff=0.2,
    #     exps_buff=0.25,
    #     default_scale=MATH_SCALE,  # Default scaling for string conversions
    #     preserve_arrangement=False
    # ):

    #     label = Tex(label_text, color=label_color).scale(label_scale)
        
    #     # Handle single expression
    #     if not isinstance(expressions, (list, tuple, VGroup)):
    #         expressions = [expressions]
        
    #     # Process each expression
    #     processed_expressions = []
    #     for exp in expressions:
    #         if isinstance(exp, str):
    #             # Convert string to MathTex with default scaling
    #             processed_expressions.append(MathTex(exp).scale(default_scale))
    #         else:
    #             # Use pre-created object as is (assume it has the scaling you want)
    #             processed_expressions.append(exp)
        
    #     # Create group and arrange
    #     if isinstance(expressions, VGroup) and preserve_arrangement:
    #         exp_group = expressions
    #     else:
    #         exp_group = VGroup(*processed_expressions)
    #         if not preserve_arrangement:
    #             exp_group.arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        
    #     if color_map:
    #         self.apply_smart_colorize(exp_group, color_map)
            
    #     return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)




    #v3 version of vertical tex labeled step with mathtex conversion

    def create_labeled_step_vertical_tex(
        self,
        label_text,
        expressions,
        color_map=None,
        label_color="#757575",
        label_scale=TEXT_SCALE,
        label_buff=0.2,
        exps_buff=0.25,
        default_scale=MATH_SCALE  # Default scaling for string conversions
    ):

        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Handle single expression
        if not isinstance(expressions, (list, tuple, VGroup)):
            expressions = [expressions]
        
        # Process each expression
        processed_expressions = []
        for exp in expressions:
            if isinstance(exp, str):
                # Convert string to MathTex with default scaling
                processed_expressions.append(MathTex(exp).scale(default_scale))
            else:
                # Use pre-created object as is
                processed_expressions.append(exp)
        
        # Create group and always arrange vertically
        exp_group = VGroup(*processed_expressions)
        exp_group.arrange(DOWN, aligned_edge=LEFT, buff=exps_buff)
        
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)
            
        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)





























    def create_labeled_step_horizontal(
            self,
            label_text,
            expressions,
            color_map=None,
            label_color="#757575",
            label_scale=0.6,
            label_buff=0.15,
            exps_buff=0.2,
            tex_scale=MATH_SCALE,
            preserve_arrangement=False
        ):
            """Create a labeled step with expressions arranged horizontally.
            
            Args:
                label_text: Text for the label
                expressions: Either a list of strings, list of MathTex objects, or a pre-arranged VGroup
                color_map: Dictionary mapping text to colors for smart colorization
                label_color: Color for the label
                label_scale: Scale factor for the label
                label_buff: Buffer between label and expressions
                exps_buff: Buffer between expressions (if newly arranged)
                tex_scale: Scale factor for MathTex objects (if created from strings)
                preserve_arrangement: If True, won't rearrange pre-created expression objects
                
            Returns:
                VGroup containing the label and expressions arranged vertically (label above horizontal expressions)
            """
            label = Tex(label_text, color=label_color).scale(label_scale)
            
            # Check if expressions are strings that need to be converted
            if all(isinstance(exp, str) for exp in expressions):
                exp_group = VGroup(*[MathTex(exp).scale(tex_scale) for exp in expressions])
                # Only arrange if we created new objects
                exp_group.arrange(RIGHT, buff=exps_buff)
            else:
                # If given pre-created objects
                if isinstance(expressions, VGroup) and preserve_arrangement:
                    # Use the VGroup as is if it should be preserved
                    exp_group = expressions
                else:
                    # Create a new VGroup and arrange if needed
                    exp_group = VGroup(*expressions)
                    if not preserve_arrangement:
                        exp_group.arrange(RIGHT, buff=exps_buff)
            
            if color_map:
                self.apply_smart_colorize(exp_group, color_map)
                
            return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
        
        
        
        
        
        
        
        
        
    def create_multi_exp_labeled_step_horizontal_tex(
        self,
        label_text,
        *expressions,
        color_map=None,
        label_color="#757575",
        label_scale=TEXT_SCALE,
        label_buff=0.2,
        exps_buff=0.2,
        default_scale=MATH_SCALE  # Default scaling for string conversions
    ):
        """Create a labeled step with expressions arranged horizontally.
        Takes expressions as variadic parameters for easier use.
        
        Args:
            label_text: Text for the label
            *expressions: Variable number of expressions (strings or MathTex objects)
            color_map: Dictionary mapping text to colors for smart colorization
            label_color: Color for the label
            label_scale: Scale factor for the label
            label_buff: Buffer between label and expressions
            exps_buff: Buffer between expressions
            default_scale: Default scale to apply to string expressions
            
        Returns:
            VGroup containing the label and expressions arranged with label above and expressions in a horizontal row
        """
        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Process expressions to convert strings to MathTex with default scaling
        processed_expressions = []
        for exp in expressions:
            if isinstance(exp, str):
                # Convert string to MathTex with default scaling
                processed_expressions.append(MathTex(exp).scale(default_scale))
            else:
                # Use pre-created object as is
                processed_expressions.append(exp)
        
        # Create VGroup and arrange HORIZONTALLY
        exp_group = VGroup(*processed_expressions).arrange(RIGHT, buff=exps_buff)
        
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)

        # Arrange label above the horizontal expressions
        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def create_step_from_list(
        self,
        *elements,
        color_map=None,
        label_color="#DBDBDB",
        label_scale=0.6,
        label_exp_buff=0.1,
        exp_exp_buff=0.2,
        annotation_exp_buff=0.2,
        exp_annotation_buff=0.2,
    ):

        min_arrange = min(
            label_exp_buff, exp_exp_buff, annotation_exp_buff, exp_annotation_buff
        )

        def add_space(group, space):
            if space > 0:
                # will not be added to the output, just a placehoder for spaceing
                group.add(Rectangle(height=space, width=1).set_opacity(0))

        step_group = VGroup()  # the output group that contains all of the elements
        arrange_group = VGroup()  # used only for arranging
        exp_group = VGroup()  # hold only exps for colorizing and more

        for i, elem in enumerate(elements):
            if type(elem) is str:
                label = Tex(elem, color=label_color).scale(label_scale)
                step_group.add(label)
                arrange_group.add(label)
                if i < len(elements) - 1:
                    add_space(arrange_group, label_exp_buff - min_arrange)
            elif type(elem) is MathTex:
                exp = elem.scale(TEX_SCALE)
                exp_group.add(exp)
                step_group.add(exp)
                # if there an expression coming
                if i < len(elements) - 1:
                    # add the exp to the arrangement if the incoming element is exp
                    if type(elements[i + 1]) is MathTex:
                        arrange_group.add(exp)
                        add_space(arrange_group, exp_exp_buff - min_arrange)
                else:
                    # add exp if it is the last element
                    arrange_group.add(exp)
            elif type(elem) is Annotation:
                # ensure that we have an exp to annotate and reject multiple annotation
                # per expression (exp should be followed by zero or one annotation)
                assert len(exp_group) >= 1 and type(elements[i - 1]) is MathTex
                # get the preceeding exp
                to_annotate = exp_group[-1]
                # call the Annotation class (do the actual annotation)
                annotation = elem(self, to_annotate)
                step_group.add(annotation)
                print("to: ", to_annotate)
                arrange_group.add(
                    VGroup(to_annotate, annotation).arrange(
                        DOWN, buff=exp_annotation_buff
                    )
                )
                # if there is an expression coming
                if i < len(elements) - 1:
                    add_space(arrange_group, annotation_exp_buff - min_arrange)
            else:
                assert False, "Unreachable"

        if color_map:
            self.apply_smart_colorize(exp_group, color_map)

        arrange_group.arrange(DOWN, aligned_edge=LEFT, buff=min_arrange)
        return step_group

    def create_ordered_steps(
        self,
        *steps,
        color_map=None,
        label_color="#DBDBDB",
        label_scale=0.6,
        label_exp_buff=0.1,
        exp_exp_buff=0.2,
        annotation_exp_buff=0.2,
        exp_annotation_buff=0.2,
        step_step_buff=0.5,
    ):
        steps_group = VGroup()
        for i, step in enumerate(steps):
            step_ = self.create_step_from_list(
                *step,
                color_map=color_map,
                label_color=label_color,
                label_scale=label_scale,
                label_exp_buff=label_exp_buff,
                exp_exp_buff=exp_exp_buff,
                annotation_exp_buff=annotation_exp_buff,
                exp_annotation_buff=exp_annotation_buff,
            )
            steps_group.add(step_)
        steps_group.arrange(DOWN, aligned_edge=LEFT, buff=step_step_buff)
        return steps_group