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
    
    
    
    # def create_annotated_equation(self, equation_text, annotation_text, from_term, to_term, color=RED, scale=MATH_SCALE):
    #     """Create an equation with annotations in one step.
        
    #     Args:
    #         equation_text: Text for the equation
    #         annotation_text: Text for the annotation (e.g., "\\div 4")
    #         from_term: Term to annotate from (e.g., "4")
    #         to_term: Term to annotate to (e.g., "48")
    #         color: Color for the annotation (default: GREEN)
    #         scale: Scale for the equation (default: TEX_SCALE)
            
    #     Returns:
    #         VGroup containing the equation and its annotations
    #     """
    #     equation = MathTex(equation_text).scale(scale)
        
    #     annotations = self.add_annotations(
    #         annotation_text,
    #         self.find_element(from_term, equation),
    #         self.find_element(to_term, equation),
    #         color=color
    #     )
        
    #     return VGroup(equation, annotations)
    
    
    # def create_annotated_equation(self, equation_text, annotation_text, from_term, to_term, 
    #                             color=RED, scale=MATH_SCALE, nth_from=0, nth_to=0, h_spacing=0):
    #     """Create an equation with annotations in one step.
        
    #     Args:
    #         equation_text: Text for the equation
    #         annotation_text: Text for the annotation (e.g., "\\div 4")
    #         from_term: Term to annotate from (e.g., "4")
    #         to_term: Term to annotate to (e.g., "48")
    #         color: Color for the annotation (default: RED)
    #         scale: Scale for the equation (default: MATH_SCALE)
    #         nth_from: Which occurrence of from_term to use (default: 0)
    #         nth_to: Which occurrence of to_term to use (default: 0)
    #         h_spacing: Horizontal spacing adjustment (default: 0)
            
    #     Returns:
    #         VGroup containing the equation and its annotations
    #     """
    #     equation = MathTex(equation_text).scale(scale)
        
    #     # Use nth parameters in find_element calls
    #     from_element = self.find_element(from_term, equation, nth=nth_from)
    #     to_element = self.find_element(to_term, equation, nth=nth_to)
        
    #     if from_element is None or to_element is None:
    #         print(f"Warning: Could not find elements for annotation. from_term='{from_term}' (nth={nth_from}), to_term='{to_term}' (nth={nth_to})")
    #         return VGroup(equation)  # Return just the equation if annotation fails
        
    #     # Create annotations with h_spacing parameter
    #     annotations = self.add_annotations(
    #         annotation_text,
    #         from_element,
    #         to_element,
    #         color=color,
    #         h_spacing=h_spacing
    #     )
        
    #     result = VGroup(equation, *annotations)  # <-- Flatten the group
    #     result._is_annotated_equation = True
    #     return result
    
    
    # def create_annotated_equation(
    #     self, equation_text, annotation_text, from_term, to_term,
    #     color=RED, scale=MATH_SCALE, nth_from=0, nth_to=0, h_spacing=0
    # ):
    #     equation = MathTex(equation_text).scale(scale)
        
    #     from_element = self.find_element(from_term, equation, nth=nth_from)
    #     to_element = self.find_element(to_term, equation, nth=nth_to)

    #     if from_element is None or to_element is None:
    #         print(f"[WARN] Couldn't find: from='{from_term}' or to='{to_term}'")
    #         annotated = VGroup(equation)
    #         annotated.equation = equation
    #         annotated.annotations = VGroup()
    #         return annotated

    #     annotations = self.add_annotations(
    #         annotation_text, from_element, to_element, color=color, h_spacing=h_spacing
    #     )

    #     annotated = VGroup(equation, *annotations)
    #     annotated._is_annotated_equation = True

    #     # ✅ Named access
    #     annotated.equation = equation
    #     annotated.annotations = annotations

    #     return annotated
    
    
    
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
    
    
    
    
    
    
    
    
    
    # def create_smart_step(
    #     self,
    #     *elements,
    #     color_map=None,
    #     label_color="#DBDBDB", 
    #     label_scale=0.6,
    #     math_tex_scale=MATH_SCALE,
    #     element_buff=0.25,
    # ):
    #     """
    #     Smart step creation focused on element type handling.
    #     For annotations, use create_annotated_equation first.
    #     """
    #     processed_elements = []
        
    #     for elem in elements:
    #         if isinstance(elem, str):
    #             # String becomes a label
    #             label = Tex(elem, color=label_color).scale(label_scale)
    #             processed_elements.append(label)
                
    #         elif isinstance(elem, MathTex):
    #             # Scale MathTex objects
    #             math_expr = elem.scale(math_tex_scale)
    #             processed_elements.append(math_expr)
                
    #         else:
    #             # Everything else (VGroups, pre-created objects, etc.) - add as-is
    #             processed_elements.append(elem)
        
    #     # Create result and arrange
    #     result = VGroup(*processed_elements)
    #     result.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
    #     # Apply coloring
    #     if color_map:
    #         self.apply_smart_colorize(result, color_map)
        
    #     return result
    
    
    
    
    # def create_smart_steps(
    #     self, 
    #     *step_element_lists, 
    #     step_spacing=0.5,
    #     **step_kwargs
    # ):
    #     """Create and arrange multiple smart steps"""
    #     steps = []
    #     for step_elements in step_element_lists:
    #         step = self.create_smart_step(*step_elements, **step_kwargs)
    #         steps.append(step)
        
    #     result = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=step_spacing)
    #     return result
    
    
    
    
    
    
    # def create_smart_step(
    #     self,
    #     *elements,
    #     # Content control
    #     color_map=None,
    #     element_buff=0.25,
        
    #     # Label detection and styling
    #     label_positions="auto",     # "auto", list of indices, or None
    #     auto_label_first=True,      # When "auto", make first string a label
    #     label_color="#DBDBDB",
    #     label_scale=0.6,
        
    #     # Text styling (non-label strings)
    #     text_color=GRAY,
    #     text_scale=0.5,
        
    #     # MathTex scaling
    #     element_scales=None,        # List of scales for each element [None, 1.2, 0.8, None]
    #     default_math_tex_scale=MATH_SCALE,
    # ):
    #     """
    #     Enhanced smart step creation with auto-detection and individual element control.
        
    #     Args:
    #         *elements: Mixed elements (str, MathTex, VGroup, etc.)
    #         label_positions: "auto" (detect first string as label), list of indices, or None (no labels)
    #         auto_label_first: When "auto", whether to make first string a label
    #         element_scales: List of scales for each element - None for non-MathTex elements
    #         element_buff: Spacing between elements in this step
            
    #     Examples:
    #         # Auto-detect first string as label
    #         step = self.create_smart_step("Step 1", MathTex("x=5"), "explanation text")
            
    #         # No labels - all strings are text
    #         step = self.create_smart_step("text", MathTex("x=5"), label_positions=None)
            
    #         # Custom labels
    #         step = self.create_smart_step("Main", MathTex("x=5"), "Sub", MathTex("y=3"), 
    #                                     label_positions=[0, 2])
            
    #         # Custom scaling
    #         step = self.create_smart_step("Step", MathTex("big"), MathTex("small"),
    #                                     element_scales=[None, 1.5, 0.8])
    #     """
        
    #     # Handle label position detection
    #     if label_positions == "auto":
    #         label_positions = []
    #         if auto_label_first:
    #             # Find first string and make it a label
    #             for i, elem in enumerate(elements):
    #                 if isinstance(elem, str):
    #                     label_positions = [i]
    #                     break
    #     elif label_positions is None:
    #         label_positions = []  # No labels, all strings are text
    #     # else: use the provided list as-is
        
    #     # Process elements
    #     processed_elements = []
        
    #     for i, elem in enumerate(elements):
    #         if isinstance(elem, str):
    #             if i in label_positions:
    #                 # This string is a label
    #                 processed = Tex(elem, color=label_color).scale(label_scale)
    #             else:
    #                 # This string is regular text
    #                 processed = Text(elem, color=text_color).scale(text_scale)
    #             processed_elements.append(processed)
                
    #         elif isinstance(elem, MathTex):
    #             # Apply custom scale if provided, otherwise use default
    #             if element_scales and i < len(element_scales) and element_scales[i] is not None:
    #                 scale = element_scales[i]
    #             else:
    #                 scale = default_math_tex_scale
                
    #             math_expr = elem.scale(scale)
    #             processed_elements.append(math_expr)
                
    #         else:
    #             # VGroups, pre-created objects, etc. - add as-is
    #             processed_elements.append(elem)
        
    #     # Create result and arrange with custom spacing
    #     result = VGroup(*processed_elements)
    #     result.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
    #     # Apply coloring if specified
    #     if color_map:
    #         self.apply_smart_colorize(result, color_map)
        
    #     return result
    
    
    
    
    # def create_smart_step(
    #     self,
    #     *elements,
    #     # Content control
    #     color_map=None,
        
    #     # Spacing control
    #     label_buff=0.15,
    #     element_buff=0.25,
        
    #     # Label styling
    #     label_color="#DBDBDB", 
    #     label_scale=0.6,                    # Separate label scaling
        
    #     # Text styling
    #     text_color=GRAY,
    #     text_scale=0.5,
        
    #     # MathTex scaling for content only
    #     content_scales=None,                # List of scales for content elements only [1.2, None, 0.8]
    #     default_math_tex_scale=MATH_SCALE,
    # ):
    #     """
    #     Smart step creation with separate label and content scaling.
        
    #     Args:
    #         *elements: Mixed elements - auto-detects label vs content
    #         label_scale: Scale for the label (if present)
    #         content_scales: List of scales for content elements only (excludes label)
    #                     [1.5, None, 3.6] applies to content elements in order
            
    #     Examples:
    #         step = self.create_smart_step(
    #             "Step 1",                    # Uses label_scale
    #             MathTex("x = 4"),           # Uses content_scales[0] = 1.5
    #             "Text explanation",          # Uses text_scale (content_scales[1] ignored)
    #             MathTex("y = 2"),           # Uses content_scales[2] = 3.6
                
    #             label_scale=0.8,            # Label scaling
    #             content_scales=[1.5, None, 3.6]  # Content scaling
    #         )
    #     """
        
    #     if len(elements) == 0:
    #         return VGroup()
        
    #     # Auto-detect label
    #     if isinstance(elements[0], str) and len(elements) > 1:
    #         has_label = True
    #         label_text = elements[0]
    #         content_elements = elements[1:]
    #     else:
    #         has_label = False
    #         label_text = None
    #         content_elements = elements
        
    #     # Process content elements
    #     processed_content = []
        
    #     for i, elem in enumerate(content_elements):
    #         if isinstance(elem, str):
    #             # Non-label strings become text (uses text_scale)
    #             text = Text(elem, color=text_color).scale(text_scale)
    #             processed_content.append(text)
                
    #         elif isinstance(elem, MathTex):
    #             # Apply content scale if provided
    #             if (content_scales and 
    #                 i < len(content_scales) and 
    #                 content_scales[i] is not None):
    #                 scale = content_scales[i]
    #             else:
    #                 scale = default_math_tex_scale
                
    #             math_expr = elem.scale(scale)
    #             processed_content.append(math_expr)
                
    #         else:
    #             # VGroups, annotations, etc. - no scaling applied
    #             processed_content.append(elem)
        
    #     # Create content structure
    #     if len(processed_content) == 0:
    #         content_group = VGroup()
    #     elif len(processed_content) == 1:
    #         content_group = processed_content[0]
    #     else:
    #         content_group = VGroup(*processed_content)
    #         content_group.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
    #     # Create final result
    #     if has_label:
    #         # Apply label_scale to label
    #         label = Tex(label_text, color=label_color).scale(label_scale)
    #         result = VGroup(label, content_group)
    #         result.arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    #     else:
    #         result = content_group
        
    #     if color_map:
    #         self.apply_smart_colorize(result, color_map)
        
    #     return result
    
    
    
    
    
    # Using the smart flattening function I mentioned earlier
    # def unpack_steps_smart(*steps):
    #     """Smart unpacking that handles annotated equations"""
    #     all_elements = []
    #     for step in steps:
    #         for element in step:
    #             if (isinstance(element, VGroup) and 
    #                 hasattr(element, '_is_annotated_equation')):
    #                 # Unpack annotated equation
    #                 all_elements.extend(element)
    #             else:
    #                 all_elements.append(element)
    #     return VGroup(*all_elements)

    # Usage:
    # all_elements = unpack_steps_smart(step2)
    # Results in: [label, equation, annotation, result_equation]
    
    
    
    
    # def unpack_steps_for_scroll_manager(self, *steps, preserve_annotations=True):
    #     """Smart unpacking that preserves annotation dependencies."""
    #     all_elements = []
        
    #     for step_index, step in enumerate(steps):
    #         print(f"Processing step {step_index}: {type(step)}, length: {len(step)}")
            
    #         # Add the label (always step[0])
    #         all_elements.append(step[0])
    #         print(f"  Added label: {step[0]}")
            
    #         # Handle content (step[1])
    #         content = step[1]
    #         print(f"  Content type: {type(content)}")
            
    #         if isinstance(content, VGroup):
    #             print(f"  Content is VGroup with {len(content)} items")
    #             for item_index, item in enumerate(content):
    #                 print(f"    Item {item_index}: {type(item)}")
    #                 print(f"    HasAttr _is_annotated_equation: {hasattr(item, '_is_annotated_equation')}")
                    
    #                 if (preserve_annotations and 
    #                     isinstance(item, VGroup) and 
    #                     hasattr(item, '_is_annotated_equation')):
    #                     print(f"    PRESERVING annotated equation as single unit")
    #                     all_elements.append(item)
    #                 else:
    #                     print(f"    Adding regular item")
    #                     all_elements.append(item)
    #         else:
    #             print(f"  Adding single content item")
    #             all_elements.append(content)
        
    #     print(f"Final elements count: {len(all_elements)}")
    #     return VGroup(*all_elements)
    
    
    
    
    
    
    
    
    def create_annotated_equation(
        self, equation_text, annotation_text, from_term, to_term,
        color=RED, scale=MATH_SCALE, nth_from=0, nth_to=0, h_spacing=0
    ):
        """Create an equation with annotations that works with ScrollManager."""
        equation = MathTex(equation_text).scale(scale)
        
        from_element = self.find_element(from_term, equation, nth=nth_from)
        to_element = self.find_element(to_term, equation, nth=nth_to)

        if from_element is None or to_element is None:
            print(f"[WARN] Couldn't find: from='{from_term}' or to='{to_term}'")
            # Even if no annotations, still mark it properly
            annotated = VGroup(equation)
            annotated._is_annotated_equation = True
            annotated.equation = equation
            annotated.annotations = VGroup()
            return annotated

        annotations = self.add_annotations(
            annotation_text, from_element, to_element, color=color, h_spacing=h_spacing
        )

        # Create the annotated group - IMPORTANT: equation first, then annotations
        annotated = VGroup(equation, *annotations)
        
        # CRITICAL: Mark this as an annotated equation for ScrollManager
        annotated._is_annotated_equation = True
        annotated._annotation_count = len(annotations)
        
        # Named access for convenience
        annotated.equation = equation
        annotated.annotations = annotations
        
        print(f"Created annotated equation with {len(annotations)} annotations")
        print(f"  Equation: {equation}")
        print(f"  Annotations: {annotations}")
        print(f"  Marked with _is_annotated_equation: {annotated._is_annotated_equation}")

        return annotated
    
    



    # PATCH 4: Enhanced create_smart_step that works with ScrollManager
    # def create_smart_step(
    #     self,
    #     *elements,
    #     color_map=None,
    #     label_buff=0.15,
    #     element_buff=0.25,
    #     label_color="#DBDBDB", 
    #     label_scale=0.6,
    #     default_math_tex_scale=MATH_SCALE,
    #     content_scales=None,
    #     mark_annotations=True,  # NEW: Auto-mark annotated equations
    # ):
    #     """
    #     Smart step creation with ScrollManager annotation support.
    #     """
    #     if len(elements) == 0:
    #         return VGroup()
        
    #     # Auto-detect label
    #     if isinstance(elements[0], str) and len(elements) > 1:
    #         has_label = True
    #         label_text = elements[0]
    #         content_elements = elements[1:]
    #     else:
    #         has_label = False
    #         label_text = None
    #         content_elements = elements
        
    #     # Process content elements
    #     processed_content = []
        
    #     for i, elem in enumerate(content_elements):
    #         if isinstance(elem, str):
    #             text = Text(elem, color=GRAY).scale(0.5)
    #             processed_content.append(text)
    #         elif isinstance(elem, MathTex):
    #             if (content_scales and 
    #                 i < len(content_scales) and 
    #                 content_scales[i] is not None):
    #                 scale = content_scales[i]
    #             else:
    #                 scale = default_math_tex_scale
                
    #             math_expr = elem.scale(scale)
    #             processed_content.append(math_expr)
    #         else:
    #             # VGroups, annotations, etc.
    #             # Check if this looks like an annotated equation and mark it
    #             if (mark_annotations and isinstance(elem, VGroup) and 
    #                 len(elem) > 1 and not hasattr(elem, '_is_annotated_equation')):
    #                 # Heuristic: if it's a VGroup with MathTex + other elements, likely annotated
    #                 if (isinstance(elem[0], MathTex) and 
    #                     any(hasattr(item, 'get_center') for item in elem[1:])):
    #                     elem._is_annotated_equation = True
    #                     elem.equation = elem[0]
    #                     elem.annotations = VGroup(*elem[1:])
                
    #             processed_content.append(elem)
        
    #     # Create content structure
    #     if len(processed_content) == 0:
    #         content_group = VGroup()
    #     elif len(processed_content) == 1:
    #         content_group = processed_content[0]
    #     else:
    #         content_group = VGroup(*processed_content)
    #         content_group.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
    #     # Create final result
    #     if has_label:
    #         label = Tex(label_text, color=label_color).scale(label_scale)
    #         result = VGroup(label, content_group)
    #         result.arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    #     else:
    #         result = content_group
        
    #     if color_map:
    #         self.apply_smart_colorize(result, color_map)
        
    #     return result






    def create_smart_step(
        self,
        label_text,
        *content_elements,
        
        # Spacing
        label_buff=0.15,
        element_buff=0.25,
        
        # Styling
        label_color="#DBDBDB", 
        label_scale=0.6,
        default_math_tex_scale=MATH_SCALE,
        
        # Coloring
        color_map=None,
    ):
        """
        Simplified smart step: Always label + content elements.
        
        Args:
            label_text: String for the label (always first)
            *content_elements: Any number of content elements (MathTex, VGroup, etc.)
            color_map: Applied to content only (not label)
        """
        
        # Create label
        label = Tex(label_text, color=label_color).scale(label_scale)
        
        # Process content elements
        processed_content = []
        for elem in content_elements:
            if isinstance(elem, str):
                # Convert string to MathTex
                processed_content.append(MathTex(elem).scale(default_math_tex_scale))
            elif isinstance(elem, MathTex):
                # Scale MathTex if not already scaled
                processed_content.append(elem.scale(default_math_tex_scale))
            else:
                # VGroups, annotated equations, etc. - use as-is
                processed_content.append(elem)
        
        # Create content structure
        if len(processed_content) == 1:
            content_group = processed_content[0]
        else:
            content_group = VGroup(*processed_content)
            content_group.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
        # Create final result
        result = VGroup(label, content_group)
        result.arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
        
        # Apply color mapping to content only (not label)
        if color_map:
            if isinstance(content_group, VGroup):
                self.apply_smart_colorize(content_group, color_map)
            else:
                self.apply_smart_colorize([content_group], color_map)
        
        return result
    
    
    def create_smart_steps(
        self, 
        *step_element_lists, 
        # Global spacing controls
        step_spacing=0.5,
        element_buff=0.25,        # ← NEW: Controls spacing within each step
        label_buff=0.15,          # ← NEW: Controls label-to-content spacing
        
        # Global styling controls  
        label_color="#DBDBDB",
        label_scale=0.6,
        default_math_tex_scale=MATH_SCALE,
        color_map=None,
        **step_kwargs                # For any other create_smart_step parameters
    ):
        """Create multiple smart steps with global control over spacing and styling."""
        
        steps = []
        for step_elements in step_element_lists:
            step = self.create_smart_step(
                *step_elements, 
                element_buff=element_buff,      # ← Apply global spacing
                label_buff=label_buff,          # ← Apply global spacing
                label_color=label_color,        # ← Apply global styling
                label_scale=label_scale,        # ← Apply global styling
                default_math_tex_scale=default_math_tex_scale,
                color_map=color_map,
                **step_kwargs
            )
            steps.append(step)
        
        result = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=step_spacing)
        return result
    
    
    
    # def create_smart_step(
    #     self,
    #     first_element,
    #     *content_elements,
        
    #     # Spacing
    #     label_buff=0.15,
    #     element_buff=0.25,
        
    #     # Styling
    #     label_color="#DBDBDB", 
    #     label_scale=0.6,
    #     default_math_tex_scale=MATH_SCALE,
        
    #     # Coloring
    #     color_map=None,
    # ):
    #     """
    #     Simplified smart step with flexible first element.
        
    #     Args:
    #         first_element: String (becomes label) OR MathTex/VGroup (no label)
    #         *content_elements: Any number of content elements
    #         default_math_tex_scale: Scale applied to strings converted to MathTex
    #         color_map: Applied to content only (not label)
    #     """
        
    #     # Handle first element check
    #     if isinstance(first_element, str):
    #         # Has label case
    #         label = Tex(first_element, color=label_color).scale(label_scale)
    #         elements_to_process = content_elements
    #         has_label = True
    #     else:
    #         # No label case - first element is content
    #         elements_to_process = [first_element] + list(content_elements)
    #         has_label = False
        
    #     # Process content elements
    #     processed_content = []
    #     for elem in elements_to_process:
    #         if isinstance(elem, str):
    #             # Convert string to MathTex with default scaling
    #             processed_content.append(MathTex(elem).scale(default_math_tex_scale))
    #         elif isinstance(elem, MathTex):
    #             # Use pre-created MathTex as-is (respects custom styling)
    #             processed_content.append(elem)
    #         else:
    #             # VGroups, annotated equations, etc. - use as-is
    #             processed_content.append(elem)
        
    #     # Create content structure
    #     if len(processed_content) == 1:
    #         content_group = processed_content[0]
    #     else:
    #         content_group = VGroup(*processed_content)
    #         content_group.arrange(DOWN, aligned_edge=LEFT, buff=element_buff)
        
    #     # Create final result
    #     if has_label:
    #         result = VGroup(label, content_group)
    #         result.arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    #     else:
    #         result = content_group
        
    #     # Apply color mapping to content only (not label)
    #     if color_map:
    #         if isinstance(content_group, VGroup):
    #             self.apply_smart_colorize(content_group, color_map)
    #         else:
    #             self.apply_smart_colorize([content_group], color_map)
        
    #     return result


    # def create_smart_steps(
    #     self, 
    #     *step_element_lists, 
        
    #     # Global spacing controls
    #     step_spacing=0.5,
    #     element_buff=0.25,
    #     label_buff=0.15,
        
    #     # Global styling controls  
    #     label_color="#DBDBDB",
    #     label_scale=0.6,
    #     default_math_tex_scale=MATH_SCALE,
        
    #     # Global coloring
    #     color_map=None,
        
    #     **step_kwargs  # For any other create_smart_step parameters
    # ):
    #     """
    #     Create multiple smart steps with global control over spacing and styling.
        
    #     Args:
    #         *step_element_lists: Each argument is a list of elements for one step
    #         step_spacing: Vertical spacing between steps
    #         element_buff: Spacing within each step between elements
    #         label_buff: Spacing between label and content
    #         default_math_tex_scale: Default scale for strings converted to MathTex
    #         color_map: Color mapping applied to all steps
    #     """
        
    #     steps = []
    #     for step_elements in step_element_lists:
    #         step = self.create_smart_step(
    #             *step_elements, 
    #             # Apply global parameters
    #             element_buff=element_buff,
    #             label_buff=label_buff,
    #             label_color=label_color,
    #             label_scale=label_scale,
    #             default_math_tex_scale=default_math_tex_scale,
    #             color_map=color_map,
    #             **step_kwargs
    #         )
    #         steps.append(step)
        
    #     result = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=step_spacing)
    #     return result
    
        
        # PATCH 3: Update the unpack function to handle annotations properly
    def unpack_steps_for_scroll_manager(self, *items, preserve_annotations=True):
        """Smart unpacking that only preserves annotated equations."""
        all_elements = []
        
        for item_index, item in enumerate(items):
            print(f"Processing item {item_index}: {type(item)}")
            
            # Check if this is a single element (not a step)
            if isinstance(item, (MathTex, Tex, Text)):
                print(f"  Adding single element: {type(item)}")
                all_elements.append(item)
                continue
            
            # Check if this is an annotated equation (preserve it)
            if (isinstance(item, VGroup) and hasattr(item, '_is_annotated_equation')):
                print(f"  PRESERVING annotated equation as single unit")
                all_elements.append(item)
                continue
            
            # Handle steps (VGroups with label + content structure)
            if isinstance(item, VGroup) and len(item) >= 2:
                print(f"  Processing step with {len(item)} parts")
                
                # Add the label (always item[0])
                all_elements.append(item[0])
                print(f"    Added label: {item[0]}")
                
                # Handle content (item[1]) - ALWAYS UNPACK unless it's an annotation
                content = item[1]
                print(f"    Content type: {type(content)}")
                
                if isinstance(content, VGroup):
                    # UNPACK all VGroups except annotations
                    for sub_item_index, sub_item in enumerate(content):
                        if (preserve_annotations and 
                            isinstance(sub_item, VGroup) and 
                            hasattr(sub_item, '_is_annotated_equation')):
                            print(f"      PRESERVING annotated equation as single unit")
                            all_elements.append(sub_item)
                        else:
                            print(f"      UNPACKING: Adding {type(sub_item)}")
                            # If it's a VGroup, unpack it further
                            if isinstance(sub_item, VGroup):
                                for nested_item in sub_item:
                                    print(f"        Adding unpacked item: {type(nested_item)}")
                                    all_elements.append(nested_item)
                            else:
                                all_elements.append(sub_item)
                else:
                    print(f"    Adding single content item")
                    all_elements.append(content)
            else:
                # Fallback: unpack if it's a VGroup, otherwise add as single element
                if isinstance(item, VGroup):
                    print(f"  UNPACKING VGroup with {len(item)} items")
                    for nested_item in item:
                        all_elements.append(nested_item)
                else:
                    print(f"  Adding as single element: {type(item)}")
                    all_elements.append(item)
        
        print(f"Final elements count: {len(all_elements)}")
        return VGroup(*all_elements)