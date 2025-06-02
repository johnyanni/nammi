"""Base scene class for math tutorials with Azure voiceover setup."""

from manim import *
from fractions import Fraction
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from .smart_tex import *
from .custom_axes import CustomAxes

from functools import partial, partialmethod



# NEW SCALE VALUES

MATH_SCALE = 0.80
S_MATH_SCALE = 0.60


LABEL_SCALE = 0.60
TEXT_SCALE = 0.70

ANNOTATION_SCALE = 0.65








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

    # def create_step(self, title, *content, buff=0.3):
    #     """Create a vertical group of elements with consistent formatting.
        
    #     Args:
    #         title: Title mobject for the step
    #         *content: Variable number of content mobjects to include
    #         buff: Buffer space between elements
            
    #     Returns:
    #         VGroup containing the title and content arranged vertically
    #     """
    #     return VGroup(title, *content).arrange(DOWN, aligned_edge=LEFT, buff=buff) 

    

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

    def indicate(self, mobject, color=YELLOW, run_time=2.0, scale_factor=1.6):
        """Indicate a mobject with a color."""
        return Indicate(mobject, color=color, run_time=run_time, scale_factor=scale_factor)


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
    
    
    
    # In your MathTutorialScene class, add this method:

    def show_indices(self, mathtex_obj, label="", duration=3, font_size=14, 
                    label_color=WHITE, index_color=RED, show_console=True):
        """
        Display indices for each element in a MathTex object for debugging.
        
        Args:
            mathtex_obj: The MathTex object to analyze
            label: Optional label to show above (defaults to object's tex_string)
            duration: How long to show the indices (seconds)
            font_size: Size of index numbers
            label_color: Color of the label text
            index_color: Color of the index numbers
            show_console: Whether to print info to console
        
        Example:
            formula = MathTex("y = mx + b")
            self.show_indices(formula)  # Shows for 3 seconds
            
            # Or with custom label
            self.show_indices(formula, "My Formula", duration=5)
        """
        # Use tex_string as default label if none provided
        if not label and hasattr(mathtex_obj, 'tex_string'):
            label = mathtex_obj.tex_string
        
        # Add a header with the label text
        header = None
        if label:
            header = Text(label, font_size=24, color=label_color)
            header.to_edge(UP)
            self.add(header)
        
        # Create group for index labels
        index_labels_group = VGroup()
        
        # Handle different structures of MathTex
        if len(mathtex_obj.submobjects) > 0:
            submob = mathtex_obj[0]
            
            for i in range(len(submob)):
                char = submob[i]
                
                # Create index label
                index_label = Text(str(i), font_size=font_size, color=index_color)
                index_label.move_to(char.get_center() + UP * 0.3)
                
                # Add background for visibility
                bg = SurroundingRectangle(
                    index_label, 
                    color=BLUE, 
                    stroke_width=1, 
                    fill_color=BLACK,
                    fill_opacity=0.7,
                    buff=0.05
                )
                
                label_group = VGroup(bg, index_label)
                index_labels_group.add(label_group)
        
        # Ensure MathTex is visible
        if mathtex_obj not in self.mobjects:
            self.add(mathtex_obj)
        
        # Add the index labels
        self.add(index_labels_group)
        
        # Print to console if requested
        if show_console:
            print(f"\n{'='*50}")
            print(f"Indices for: {label}")
            print(f"{'='*50}")
            print(f"Total submobjects: {len(mathtex_obj.submobjects)}")
            
            if len(mathtex_obj.submobjects) > 0:
                submob = mathtex_obj[0]
                print(f"\nIndex mapping:")
                for i in range(min(len(submob), 20)):  # Limit to first 20
                    print(f"  [{i}] = {submob[i]}")
                
                if len(submob) > 20:
                    print(f"  ... and {len(submob) - 20} more elements")
            print(f"{'='*50}\n")
        
        # Wait and clean up
        self.wait(duration)
        self.remove(index_labels_group)
        if header:
            self.remove(header)



        
        
    def find_element(self, pattern, tex_obj, nth=0, color=None, opacity=None):
        """Simplified find_element that handles common cases.
        
        Args:
            pattern: The text pattern to search for (e.g., "x", "1", "-5", r"\frac{300}{400}")
            tex_obj: The MathTex or Tex object to search within
            nth: Which occurrence to return (0-based index)
            color: Optional color to set for the element
            opacity: Optional opacity to set for the element
        
        Returns:
            The matching element(s) - single VMobject or VGroup for multi-element patterns
            None if not found
        """
        
        # Handle negative numbers specially
        if pattern.startswith('-') and len(pattern) > 1:
            # Find minus sign and number separately
            minus_indices = search_shape_in_text(tex_obj, MathTex("-"))
            num_indices = search_shape_in_text(tex_obj, MathTex(pattern[1:]))
            
            # Look for adjacent pairs
            for minus_idx in minus_indices:
                for num_idx in num_indices:
                    # Check if they're next to each other
                    if hasattr(minus_idx, 'stop') and hasattr(num_idx, 'start'):
                        if minus_idx.stop == num_idx.start or minus_idx.stop + 1 == num_idx.start:
                            if nth == 0:  # Found our match
                                minus_element = tex_obj[0][minus_idx]
                                num_element = tex_obj[0][num_idx]
                                
                                # Set opacity on individual elements FIRST
                                if opacity is not None:
                                    minus_element.set_opacity(opacity)
                                    num_element.set_opacity(opacity)
                                
                                # Set color on individual elements
                                if color:
                                    minus_element.set_color(color)
                                    num_element.set_color(color)
                                
                                # THEN create the group
                                result = VGroup(minus_element, num_element)
                                
                                return result
                            nth -= 1
        
        # For everything else, use search_shape_in_text
        indices = search_shape_in_text(tex_obj, MathTex(pattern))
        
        if not indices or nth >= len(indices):
            print(f"Pattern '{pattern}' not found")
            return None
            
        # Return what search_shape_in_text found
        result = tex_obj[0][indices[nth]]
        if color: result.set_color(color)
        if opacity is not None:
            result.set_opacity(opacity)
        
        return result
        
    SHARED_MATH_ELEMENTS = [
        ('equals', '='),
        ('plus', '+', 0),      # First plus sign
        ('minus', '-', 0),     # First minus sign
    ]

    SHARED_COMPARISON_ELEMENTS = [
        ('equals', '='),
        ('less_than', '<'),
        ('greater_than', '>'),
        ('leq', r'\leq'),
        ('geq', r'\geq'),
    ]

    SHARED_ARITHMETIC_OPS = [
        ('plus', '+', 0),
        ('minus', '-', 0),
        ('times', r'\times', 0),
        ('divide', r'\div', 0),
    ]

    # For equations with equals and all basic operations
    SHARED_EQUATION_ELEMENTS = [
        ('equals', '='),
        ('plus', '+', 0),
        ('minus', '-', 0),
        ('times', r'\times', 0),
        ('divide', r'\div', 0),
    ]
        
        
    def parse_elements(self, equation, *patterns):
        """Parse multiple elements from an equation in one call.
        
        Args:
            equation: The MathTex object to parse
            *patterns: Variable number of tuples defining what to find:
                - (name, pattern): Basic pattern search
                - (name, pattern, nth): Pattern with nth occurrence (0-indexed)
                - (name, pattern, nth, color): Pattern with nth occurrence and color
                - (name, pattern, nth, color, opacity): Full options
            
        Returns:
            Dict of extracted elements with given names as keys
            
        Example:
            # Basic usage
            parts = self.parse_elements(equation,
                ('x', 'x'),
                ('equals', '='),
                ('zero', '0')
            )
            # Access as: parts['x'], parts['equals'], etc.
            
            # With shared elements
            parts = self.parse_elements(equation,
                ('x', 'x'),
                ('y', 'y'),
                *SHARED_MATH_ELEMENTS  # Adds equals, plus, minus
            )
            
            # With nth occurrence
            parts = self.parse_elements(equation,
                ('first_x', 'x', 0),   # First x
                ('second_x', 'x', 1),  # Second x
                ('squared', '^2', 1),  # Second ^2
            )
            
            # With color
            parts = self.parse_elements(equation,
                ('result', '42', 0, YELLOW),
                ('x', 'x', 0, BLUE, 0.5),  # With opacity
            )
        """
        results = {}
        
        for pattern_info in patterns:
            # Skip None patterns (allows conditional patterns)
            if pattern_info is None:
                continue
                
            name = pattern_info[0]
            pattern = pattern_info[1]
            
            # Build kwargs based on tuple length
            kwargs = {}
            if len(pattern_info) > 2:
                kwargs['nth'] = pattern_info[2]
            if len(pattern_info) > 3:
                kwargs['color'] = pattern_info[3]
            if len(pattern_info) > 4:
                kwargs['opacity'] = pattern_info[4]
                
            # Find the element
            element = self.find_element(pattern, equation, **kwargs)
            if element is not None:
                results[name] = element
            else:
                # Only warn for non-optional patterns
                if len(pattern_info) <= 2 or pattern_info[2] == 0:
                    print(f"Warning: Could not find pattern '{pattern}' for '{name}' in equation")
                
        return results
        
        
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
    
    
    
    
    
    
    #############################################################
    ######## ANNOTATIONS ############
    #############################################################
    
    
    def add_annotations(self, term_added, left_term, right_term, color=None, h_spacing=0, scale=ANNOTATION_SCALE):
        """Create annotations with customizable scale."""
        terms = VGroup(*[MathTex(rf"{term_added}").scale(scale) for _ in range(2)])
        if color:
            terms.set_color(color)

        terms[0].next_to(left_term, DOWN)
        terms[1].next_to(right_term, DOWN)

        # Apply horizontal spacing adjustment
        terms[0].shift(LEFT * h_spacing)
        terms[1].shift(RIGHT * h_spacing)

        if terms[0].get_y() < terms[1].get_y():
            terms[1].align_to(terms[0], DOWN)
        else:
            terms[0].align_to(terms[1], DOWN)

        return terms
    
    
    
    
    def create_annotated_equation(self, equation_text, annotation_text, from_term, to_term,
                                color=RED, scale=MATH_SCALE, annotation_scale=ANNOTATION_SCALE, 
                                nth_from=0, nth_to=0, h_spacing=0):
        """Create an equation with annotations as a single VGroup."""
        equation = MathTex(equation_text).scale(scale)
        
        from_element = self.find_element(from_term, equation, nth=nth_from)
        to_element = self.find_element(to_term, equation, nth=nth_to)

        if from_element is None or to_element is None:
            print(f"[WARN] Couldn't find: from='{from_term}' or to='{to_term}'")
            return equation

        # Use the existing add_annotations with scale parameter
        annotations = self.add_annotations(
            annotation_text, from_element, to_element, 
            color=color, h_spacing=h_spacing, scale=annotation_scale
        )

        result = VGroup(equation, *annotations)
        result._has_annotation = True
        
        return result
    
    
    
    def create_step(self, label_text, *elements, spacing=0.3):
        """Create a step with uniform spacing."""
        all_elements = [Tex(label_text).scale(0.6)]  # CREATES a label from the string
        all_elements.extend(elements)                 # Adds your elements after
        return VGroup(*all_elements).arrange(DOWN, aligned_edge=LEFT, buff=spacing)
    
    
    # def smart_unpack(self, *items):
    #     """Unpack VGroups by default, unless flagged to keep together."""
    #     unpacked = []
        
    #     for item in items:
    #         if isinstance(item, VGroup):
    #             # Check for keep-together flags
    #             if (hasattr(item, '_has_annotation') or 
    #                 hasattr(item, '_keep_together')):
    #                 unpacked.append(item)  # Keep together
    #             else:
    #                 unpacked.extend(item)  # DEFAULT: Unpack VGroups
    #         else:
    #             unpacked.append(item)
        
    #     return VGroup(*unpacked)
    
    
    
    def create_rect_group(self, mobject, rect_color="#9A48D0", corner_radius=0.1, 
                        buff=0.1, stroke_width=2, show_rect_first=False):
        """Create a rectangle group.
        
        Args:
            mobject: The object to surround with a rectangle
            rect_color: Color of the rectangle (default: "#9A48D0")
            corner_radius: Radius of corners (default: 0.1)
            buff: Buffer around the object (default: 0.1)
            stroke_width: Width of rectangle stroke (default: 2)
            show_rect_first: If True, rectangle appears before object (default: False)
        """
        rect = SurroundingRectangle(
            mobject, 
            color=rect_color,
            corner_radius=corner_radius,
            buff=buff,
            stroke_width=stroke_width
        )
        
        # Default: object first, then rectangle
        group = VGroup(rect, mobject) if show_rect_first else VGroup(mobject, rect)
        return group
    
    
    
    
    
    
    
    
    
        
    def show_vgroup_indices(self, vgroup):
        """Show indices for all MathTex objects in a VGroup with auto-generated labels.
        
        Usage:
            formulas = VGroup(formula, substitute, calculation_step1, calculation_step2)
            self.show_vgroup_indices(formulas)
        """
        print("\n" + "="*60)
        print("INDEX MAPPING FOR ALL MATHTEX OBJECTS")
        print("="*60)
        
        for i, tex_obj in enumerate(vgroup):
            if not isinstance(tex_obj, (MathTex, Tex)):
                continue
                
            # Auto-generate label from tex_string or use index
            if hasattr(tex_obj, 'tex_string'):
                # Truncate long formulas for readability
                label = tex_obj.tex_string[:30] + "..." if len(tex_obj.tex_string) > 30 else tex_obj.tex_string
            else:
                label = f"MathTex_{i}"
                
            print(f"\n[{i}] {label}")
            print("-" * 40)
            
            if hasattr(tex_obj, 'submobjects') and len(tex_obj.submobjects) > 0:
                submob = tex_obj[0]
                for j in range(len(submob)):
                    try:
                        element = submob[j]
                        elem_str = element.__class__.__name__
                        print(f"  [{j}] = {elem_str}")
                    except:
                        print(f"  [{j}] = <error>")
            
        print("\n" + "="*60 + "\n")



    def show_flattened_indices(self, *groups):
        """Show indices for all MathTex/Tex objects, flattening nested structures.
        
        Usage:
            self.show_flattened_indices(step1, step2, step3)
            # or
            self.show_flattened_indices(main)  # The VGroup containing all steps
        """
        print("\n" + "="*80)
        print("FLATTENED INDEX MAPPING (All MathTex/Tex objects)")
        print("="*80)
        
        all_objects = []
        labels = []
        
        def extract_math_objects(obj, prefix=""):
            """Recursively extract all MathTex/Tex objects."""
            if isinstance(obj, VGroup):
                for i, item in enumerate(obj):
                    new_prefix = f"{prefix}[{i}]" if prefix else f"item[{i}]"
                    extract_math_objects(item, new_prefix)
            elif isinstance(obj, (MathTex, Tex)):
                all_objects.append(obj)
                labels.append(prefix if prefix else "item")
        
        # Extract all objects
        for group in groups:
            extract_math_objects(group)
        
        # Display them
        for obj, label in zip(all_objects, labels):
            tex_str = obj.tex_string if hasattr(obj, 'tex_string') else str(obj)
            if len(tex_str) > 50:
                tex_str = tex_str[:47] + "..."
            
            print(f"\n{label}: {tex_str}")
            print("-" * 60)
            
            if hasattr(obj, 'submobjects') and len(obj.submobjects) > 0:
                submob = obj[0]
                for i in range(len(submob)):
                    elem = submob[i]
                    elem_type = elem.__class__.__name__
                    print(f"  [{i}] = {elem_type}")
        
        print("\n" + "="*80 + "\n")
        
        
    def create_strikethrough_line(self, target_mobject, color=RED, stroke_width=3):
        """Create a line that strikes through a mobject"""
        line = Line(
            start=target_mobject.get_left() + LEFT * 0.1,
            end=target_mobject.get_right() + RIGHT * 0.1,
            color=color,
            stroke_width=stroke_width
        )
        line.move_to(target_mobject.get_center())
        return line