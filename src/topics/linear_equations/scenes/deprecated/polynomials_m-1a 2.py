"""Tutorial on graphing the rational function y = (3x+6)/(x+2) using long division to convert to standard form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.styles.constants import *
import numpy as np

class FullScreenOverlay(VGroup):
    """Base class for full screen overlays with text and optional content."""

    def __init__(
            self,
            body_text,
            background_color="#121212",
            text_color=WHITE,
            fill_opacity=0.95,
            font_size=40,
            show_examples=False,
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
        
        if show_examples:
            # Create positive example
            pos_tex = MathTex(r"a > 0: y = \frac{1}{x-h} + k", color=GREEN)
            pos_graph = self.create_example_graph(pos_tex, sign=1)
            
            # Create negative example
            neg_tex = MathTex(r"a < 0: y = \frac{-1}{x-h} + k", color=RED)
            neg_graph = self.create_example_graph(neg_tex, sign=-1)
            
            # Position examples
            example_group = VGroup(
                VGroup(pos_tex, pos_graph),
                VGroup(neg_tex, neg_graph)
            ).arrange(DOWN, buff=1.5).center().shift(DOWN * 0.5)
            
            self.add(example_group)
        
        # Center the entire group
        self.center()
    
    def create_example_graph(self, title, sign=1):
        """Create a small example graph with asymptotes."""
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": True},
            tips=False
        )
        
        # Add asymptotes
        v_asymptote = DashedLine(
            start=axes.c2p(0, -3),
            end=axes.c2p(0, 3),
            color=RED,
            dash_length=0.1
        )
        
        h_asymptote = DashedLine(
            start=axes.c2p(-3, 0),
            end=axes.c2p(3, 0),
            color=GREEN,
            dash_length=0.1
        )
        
        # Add curve based on sign
        def func(x):
            if abs(x) < 0.1:  # Avoid division near asymptote
                return np.nan
            return sign * (1/x)
        
        left_curve = axes.plot(
            func, x_range=[-3, -0.2],
            color=BLUE, stroke_width=2
        )
        
        right_curve = axes.plot(
            func, x_range=[0.2, 3],
            color=BLUE, stroke_width=2
        )
        
        # Highlight quadrants based on sign
        if sign > 0:
            # For positive, highlight 1st and 3rd quadrants
            q1 = Polygon(
                axes.c2p(0, 0), axes.c2p(3, 0), 
                axes.c2p(3, 3), axes.c2p(0, 3),
                fill_color=BLUE, fill_opacity=0.2, stroke_width=0
            )
            q3 = Polygon(
                axes.c2p(0, 0), axes.c2p(-3, 0), 
                axes.c2p(-3, -3), axes.c2p(0, -3),
                fill_color=BLUE, fill_opacity=0.2, stroke_width=0
            )
            return VGroup(axes, v_asymptote, h_asymptote, left_curve, right_curve, q1, q3)
        else:
            # For negative, highlight 2nd and 4th quadrants
            q2 = Polygon(
                axes.c2p(0, 0), axes.c2p(-3, 0), 
                axes.c2p(-3, 3), axes.c2p(0, 3),
                fill_color=BLUE, fill_opacity=0.2, stroke_width=0
            )
            q4 = Polygon(
                axes.c2p(0, 0), axes.c2p(3, 0), 
                axes.c2p(3, -3), axes.c2p(0, -3),
                fill_color=BLUE, fill_opacity=0.2, stroke_width=0
            )
            return VGroup(axes, v_asymptote, h_asymptote, left_curve, right_curve, q2, q4)

class CustomAxes(Axes):
    """Custom axes that allow easy coordinate setup."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class GraphingRationalFunction(MathTutorialScene):
    """A tutorial that teaches how to graph the rational function y = (3x+6)/(x+2)."""
    
    
    
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
    
    def apply_smart_colorize(self, elements, color_map):
        """Apply SmartColorizeStatic to a list of elements using the given color map"""
        for element in elements:
            SmartColorizeStatic(element, color_map)

    def create_surrounding_rectangle(
            self,
            mobject,
            color="#9A48D0",
            corner_radius=0.1, buff=0.15
    ):
        return SurroundingRectangle(mobject, color=color, corner_radius=corner_radius, buff=buff)
    
    def construct(self):


        
        # Constants for scaling
        TEX_SCALE = 0.70
        AXES_SCALE = 0.65

        # Quadrant
        QUADRANT_COLOR = BLUE 
        QUADRANT_OPACITY = 0.2

        # Axes
        ASYMPTOTE_COLOR = RED
        POINT_COLOR = "#FF4081"
        POINT_RADIUS = 0.12

        # Graph
        GRAPH_COLOR = PURPLE
        
        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        EQUATION_BG_WIDTH = 2
        EQUATION_BG_OPACITY = 0.1
        EQUATION_BG_RADIUS = 0.3

        # Indicate Animation
        INDICATION_COLOR = "#9A48D0"
        INDICATION_TIME = 2.0

        # Equation Colors
        DIVISOR_COLOR = "#FF7043"  # Orange-red for divisor (x + 2)
        DIVIDEND_COLOR = "#4DB6AC"  # Teal for dividend (3x + 6)
        REMAINDER_COLOR = "#FFD54F"  # Amber for remainder (0)
        A_COLOR = "#FFD54F"  # Same as remainder
        K_COLOR = "#64B5F6"  # Light blue for k value (3)
        STEP_COLOR = "#90A4AE" # Blue-Gray for steps
        
        EQ_VBUFF = 0.35
        STANDARD_EQ_HBUFF = 0.2
        WIDE_EQ_HBUFF = 0.75
        
        LABEL_SCALE = 0.5
        LABEL_COLOR = GREY
        LABEL_BUFF = 0.2
            
        # Constants for timing
        QUICK_PAUSE = 0.5
        STANDARD_PAUSE = 1.0
        COMPREHENSION_PAUSE = 2.0

        

        def create_labeled_step(
                label_text,
                expressions,
                color_map=None,
                label_color=LABEL_COLOR,
                label_scale=LABEL_SCALE,
                label_buff=LABEL_BUFF,
                eq_hbuff=STANDARD_EQ_HBUFF,
                tex_scale=TEX_SCALE
        ):
            label = Tex(label_text, color=label_color).scale(label_scale)
            exp_group = expressions
            
            if color_map:
                self.apply_smart_colorize(exp_group, color_map)
            
            return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)

        # Axes 
        axes = CustomAxes(
            x_range=[-4, 4],
            y_range=[-2, 6],
            x_length=8,
            y_length=9,
        ).scale(AXES_SCALE).to_corner(UR).shift(UP * 0.2)
        axes.add_coordinates(range(-4, 5), range(-2, 7))

        v_asymptote = DashedLine(
            start=axes.c2p(-2, -2),
            end=axes.c2p(-2, 6),
            color=ASYMPTOTE_COLOR
        )

        h_asymptote = DashedLine(
            start=axes.c2p(-4, 3),
            end=axes.c2p(4, 3),
            color=ASYMPTOTE_COLOR
        )

        # Create quadrants for later use
        first_quadrant = Polygon(
            axes.c2p(-2, 3),
            axes.c2p(4, 3),
            axes.c2p(4, 6),
            axes.c2p(-2, 6),
            fill_opacity=QUADRANT_OPACITY,
            fill_color=QUADRANT_COLOR,
            stroke_width=0
        )

        third_quadrant = Polygon(
            axes.c2p(-4, -2),
            axes.c2p(-2, -2),
            axes.c2p(-2, 3),
            axes.c2p(-4, 3),
            fill_opacity=QUADRANT_OPACITY,
            fill_color=QUADRANT_COLOR,
            stroke_width=0
        )

        # Sample points
        point1 = Dot(axes.c2p(-3, 0), color=POINT_COLOR, radius=POINT_RADIUS)
        point2 = Dot(axes.c2p(0, 3), color=POINT_COLOR, radius=POINT_RADIUS)
        point3 = Dot(axes.c2p(1, 3), color=POINT_COLOR, radius=POINT_RADIUS)
        
        # Function and graph
        def func(x):
            if abs(x + 2) < 0.1:  # Avoid division near asymptote
                return np.nan
            return 3 + 0 / (x + 2)  # y = 3x+6 / x+2 = 3 + 0/(x+2)

        left_x_range = [-4, -2.2]
        right_x_range = [-1.8, 4]

        left_graph = axes.plot(
            func,
            x_range=left_x_range,
            discontinuities=[-2],
            dt=0.1,
            color=GRAPH_COLOR
        )

        right_graph = axes.plot(
            func,
            x_range=right_x_range,
            discontinuities=[-2],
            dt=0.1,
            color=GRAPH_COLOR
        )

        graph = VGroup(left_graph, right_graph)
        
        # Equations
        general_form = VGroup(
            MathTex(r"y = \frac{a}{x - h} + k"),
            MathTex("Y = k"),
            MathTex("X = h")
        ).arrange(buff=WIDE_EQ_HBUFF).scale(TEX_SCALE).to_edge(DOWN).shift(RIGHT * 0.7)

        self.apply_smart_colorize(
            general_form,
            {
                "x - h": DIVISOR_COLOR,
                "a": A_COLOR,
                "k": K_COLOR,
                "h": DIVISOR_COLOR,
            }
        )

        y_callout = self.create_callout("Horizontal Asymptote", general_form[1], animate=False)
        x_callout = self.create_callout("Vertical Asymptote", general_form[2], animate=False)
        
        equation_bg = SurroundingRectangle(
            general_form,
            buff=0.2,
            corner_radius=EQUATION_BG_RADIUS,
            fill_opacity=EQUATION_BG_OPACITY,
            fill_color=EQUATION_BG_FILL,  
            stroke_color=EQUATION_BG_STROKE, 
            stroke_width=EQUATION_BG_WIDTH
        )

        general_form_group = VGroup(general_form, equation_bg)

        example_func = MathTex(r"y = \frac{3x + 6}{x + 2}").scale(TEX_SCALE)
        example_func_num = example_func[0][search_shape_in_text(example_func, MathTex("3x + 6"))[0]].set_color(DIVIDEND_COLOR)
        example_func_den = example_func[0][search_shape_in_text(example_func, MathTex("x + 2"))[0]].set_color(DIVISOR_COLOR)
        
        blank_screen = FullScreenOverlay("Effect of the sign of a", show_examples=True)
        
        # Step 1: Long division
        division_setup = MathTex(r"x + 2\ \overline{\strut \smash{)}\ 3x + 6\ }")
        division_symbol = division_setup[0][3:5] 
        divisor = division_setup[0][search_shape_in_text(division_setup, MathTex("x + 2"))[0]].set_color(DIVISOR_COLOR)
        dividend = division_setup[0][search_shape_in_text(division_setup, MathTex("3x + 6"))[0]].set_color(DIVIDEND_COLOR)
        
        division_step_1 = MathTex("-(3x + 6)").next_to(division_setup, DOWN).shift(RIGHT * 0.6).set_color(STEP_COLOR)
        division_step_1_3x = division_step_1[0][search_shape_in_text(division_step_1, MathTex("3x"))[0]]
        division_step_1_6 = VGroup(
            division_step_1[0][search_shape_in_text(division_step_1, MathTex("+"))[0]],
            division_step_1[0][search_shape_in_text(division_step_1, MathTex("6"))[0]]
        )
        division_step_1_rem = VGroup(
            *[
                division_step_1[0][group]
                for group in search_shapes_in_text(division_step_1, [MathTex("-("), MathTex(")")])
            ]
        )

        hline = Line(division_step_1.get_left(), division_step_1.get_right(), stroke_width=1.5).next_to(division_step_1, DOWN)

        zero = MathTex("0").match_x(division_step_1_3x)
        zero2 = MathTex("0").match_x(division_step_1_6)
        division_step_2 = VGroup(zero, zero2).set_color(STEP_COLOR).next_to(hline, DOWN)
        
        division_step_2_arrow = MathTex(r"\longrightarrow").next_to(division_step_2, RIGHT)
        quotient = MathTex("3", color=K_COLOR).next_to(division_setup, UP)
        
        remainder = MathTex("r = 0", color=REMAINDER_COLOR).next_to(division_step_2_arrow, RIGHT * 1.5)
        remainder_rec = self.create_surrounding_rectangle(remainder)
        remainder_group = VGroup(remainder, remainder_rec)
        
        division_steps = VGroup(
            division_symbol,
            divisor,
            dividend,
            quotient,
            division_step_1_3x,
            division_step_1_6,
            division_step_1_rem,
            hline,
            zero,
            zero2, 
            division_step_2_arrow,
            remainder,
            remainder_rec
        ).scale(TEX_SCALE)

        step_1 = create_labeled_step(
            "Step 1: Do the long division",
            division_steps,
        )
        step_1_label = step_1[0]

        # Step 2: Write in simplified form
        simplified_y = MathTex(r"y = \frac{0}{x + 2} + 3").scale(TEX_SCALE)
        SmartColorizeStatic(
            simplified_y,
            {
                "0": A_COLOR,
                "x + 2": DIVISOR_COLOR,
                "3": K_COLOR
            }
        )
        simplified_y_term_1 = simplified_y[0][search_shape_in_text(simplified_y, MathTex("y ="))[0]]
        simplified_y_term_2 = simplified_y[0][search_shape_in_text(simplified_y, MathTex(r"\frac{0}{x + 2}"))[0]]
        simplified_y_term_3 = VGroup(
            simplified_y[0][search_shape_in_text(simplified_y, MathTex("+"))[0]],
            simplified_y[0][search_shape_in_text(simplified_y, MathTex("3"))[0]]
        )

        # Final simplified form (since remainder is 0)
        final_y = MathTex(r"y = 3").scale(TEX_SCALE * 1.2)
        final_y[0][2].set_color(K_COLOR)  # Color the "3"
        
        simplified_y_rec = self.create_surrounding_rectangle(simplified_y)
        simplified_y_group = VGroup(simplified_y, simplified_y_rec)
        
        final_y_rec = self.create_surrounding_rectangle(final_y)
        final_y_group = VGroup(final_y, final_y_rec)
        
        simplification_group = VGroup(simplified_y_group, final_y_group).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        step_2 = create_labeled_step(
            "Step 2: Write $y$ in simplified form",
            simplification_group
        )
        step_2_label = step_2[0]

        # Step 3: Calculate Asymptotes
        x_asymptote = MathTex("x = -2", color=DIVISOR_COLOR).scale(TEX_SCALE)
        y_asymptote = MathTex("y = 3", color=K_COLOR).scale(TEX_SCALE)
        asymptotes = VGroup(x_asymptote, y_asymptote).arrange(buff=1).next_to(simplification_group, DOWN * 2)

        asymptote_note = MathTex(r"\text{Note: When $a = 0$, $y = k$ is a horizontal line}").scale(TEXT_SCALE)
        asymptote_note.next_to(asymptotes, DOWN, buff=0.5)
        self.apply_smart_colorize(
            [asymptote_note],
            {
                "a = 0": A_COLOR,
                "y = k": K_COLOR
            }
        )

        step_3 = create_labeled_step(
            "Step 3: Calculate asymptotes",
            VGroup(asymptotes, asymptote_note)
        )
        step_3_label = step_3[0]

        # Step 4: Calculate Points on Graph
        # Since our function simplifies to y = 3, all points have y = 3 except at x = -2
        point_1_step_1 = MathTex(r"y = \frac{0}{-3 + 2} + 3")
        point_1_step_2 = MathTex(r"= \frac{0}{-1} + 3")
        point_1_step_3 = MathTex("= 0 + 3")
        point_1_final_result = MathTex("y = 3", color=POINT_COLOR)
        point_1_final_result_rec = self.create_surrounding_rectangle(point_1_final_result)
        
        point_1_steps = VGroup(
            point_1_step_1,
            point_1_step_2,
            point_1_step_3,
            VGroup(point_1_final_result, point_1_final_result_rec)
        ).scale(TEX_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF)
        point_1_step_2.shift(RIGHT * 0.3)
        point_1_step_3.shift(RIGHT * 0.3)

        self.apply_smart_colorize(
            point_1_steps,
            {
                "0": A_COLOR,
                "3": K_COLOR,
                "-3 + 2": DIVISOR_COLOR
            }
        )
        
        point_2_step_1 = MathTex(r"y = \frac{0}{0 + 2} + 3")
        point_2_step_2 = MathTex(r"= \frac{0}{2} + 3")
        point_2_step_3 = MathTex("= 0 + 3")
        point_2_final_result = MathTex("y = 3", color=POINT_COLOR)
        point_2_final_result_rec = self.create_surrounding_rectangle(point_2_final_result)

        point_2_steps = VGroup(
            point_2_step_1,
            point_2_step_2,
            point_2_step_3,
            VGroup(point_2_final_result, point_2_final_result_rec)
        ).scale(TEX_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF)
        point_2_step_2.shift(RIGHT * 0.3)
        point_2_step_3.shift(RIGHT * 0.3)

        self.apply_smart_colorize(
            point_2_steps,
            {
                "0": A_COLOR,
                "3": K_COLOR,
                "0 + 2": DIVISOR_COLOR
            }
        )
        
        point_3_step_1 = MathTex(r"y = \frac{0}{1 + 2} + 3")
        point_3_step_2 = MathTex(r"= \frac{0}{3} + 3")
        point_3_step_3 = MathTex("= 0 + 3")
        point_3_final_result = MathTex("y = 3", color=POINT_COLOR)
        point_3_final_result_rec = self.create_surrounding_rectangle(point_3_final_result)

        point_3_steps = VGroup(
            point_3_step_1,
            point_3_step_2,
            point_3_step_3,
            VGroup(point_3_final_result, point_3_final_result_rec)
        ).scale(TEX_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF)
        point_3_step_2.shift(RIGHT * 0.3)
        point_3_step_3.shift(RIGHT * 0.3)

        self.apply_smart_colorize(
            point_3_steps,
            {
                "0": A_COLOR,
                "3": K_COLOR,
                "1 + 2": DIVISOR_COLOR
            }
        )
        
        points_group = VGroup(point_1_steps, point_2_steps, point_3_steps).arrange(buff=WIDE_EQ_HBUFF)
        
        step_4 = create_labeled_step(
            "Step 4: Calculate some points on the curve",
            points_group
        )
        step_4_label = step_4[0]
        
        equations_group = VGroup(
            example_func,
            step_1, 
            step_2,
            step_3,
            step_4,
        ).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF).to_corner(UL)

        ordered_steps = VGroup(
            example_func,
            step_1_label,
            *division_steps,
            
            step_2_label,
            simplified_y_term_1,
            simplified_y_term_2,
            simplified_y_term_3,
            simplified_y_rec,
            final_y,
            final_y_rec,
            
            step_3_label,
            x_asymptote,
            y_asymptote,
            asymptote_note,

            step_4_label,
            point_1_step_1,
            point_1_step_2,
            point_1_step_3,
            point_1_final_result,
            point_1_final_result_rec,
            point_2_step_1,
            point_2_step_2,
            point_2_step_3,
            point_2_final_result,
            point_2_final_result_rec,
            point_3_step_1,
            point_3_step_2,
            point_3_step_3,
            point_3_final_result,
            point_3_final_result_rec
        )

        scroll = ScrollManager(ordered_steps)
        steps_to_scroll = len(division_steps) + 2
        
        # ---------------- Tips ----------------
        tip_1 = QuickTip("This is simply long division as in other chapters.")
        tip_2 = QuickTip("Note that $a$ is the remainder and $k$ is the quotient")
        tip_3 = QuickTip("$x = -2$ is a vertical asymptote since $y$ will be undefined at that point.")
        tip_4 = QuickTip("Since the remainder is 0, our function simplifies to $y = 3$, which is a horizontal line.")
        tip_5 = QuickTip("When $a = 0$, the function becomes a horizontal line with no vertical asymptote behavior.")

        Group(tip_1, tip_2, tip_3, tip_4, tip_5).to_corner(DR)
        
        # ---------------- Animations ----------------
        def indicate(mobject, color=INDICATION_COLOR, run_time=INDICATION_TIME):
            return Indicate(mobject, color=color, run_time=INDICATION_TIME)
        
        with self.voiceover(
                text="""
                In this video, we'll explore how to graph the rational function y equals three x plus six, divided by x plus two.
                """
        ) as tracker:
            self.play(FadeIn(axes, general_form_group))
            scroll.prepare_next(self)
            self.wait(QUICK_PAUSE)

        with self.voiceover("Let's examine this rational function.") as tracker:
            self.play(indicate(example_func))
            self.wait(QUICK_PAUSE)
            
        with self.voiceover(
                text="""
                To graph it effectively, we first need to transform it into this <bookmark mark='format' /> format:
                y equals "a" over x minus h plus k.

                This format represents a hyperbola, and once we have it, we can easily identify the asymptotes,
                details, and key characteristics that will help us create an accurate graph.
                """
        ) as tracker:
            self.wait_until_bookmark("format")
            self.play(indicate(general_form_group))
            self.wait(QUICK_PAUSE)

        with self.voiceover(
                text="""
                Our first step is to divide <bookmark mark='num' /> the numerator into <bookmark mark='den' /> the denominator, which is the polynomial you see here.
                """
        ) as tracker:
            self.wait_until_bookmark("num")
            self.play(indicate(example_func_num))

            self.wait_until_bookmark("den")
            self.play(indicate(example_func_den))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Next, we'll rearrange our our result into <bookmark mark='format' /> this format.
                Finally, we'll use this information to graph our rational function.
                """
        ) as tracker:
            self.wait_until_bookmark("format")
            self.play(indicate(general_form_group))
            self.wait(QUICK_PAUSE)

        with self.voiceover(
                text="""
                Now, we will do the division.
                We start by recognizing that our divisor <bookmark mark='divisor' /> is x plus 2,
                and we're dividing it into our <bookmark mark='poly' /> polynomial, 3x plus 6.
                """
        ) as tracker:
            scroll.prepare_next(self, steps=2)
            
            self.wait_until_bookmark("divisor")
            scroll.fade_in_from_target(self, example_func_den, run_time=2)

            self.wait_until_bookmark("poly")
            scroll.fade_in_from_target(self, example_func_num, run_time=2)

            self.play(FadeIn(tip_1, shift=UP))
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(
                text="""
                The division process is as follows; we divide, multiply, then subtract, then divide, multiply, subtract
                and so forth until we reach the end, which is a remainder or might be zero.
                """
        ) as tracker:
            pass

        with self.voiceover(
                text="""
                First, we divide: x divides into 3x to <bookmark mark='quotient' /> give us three.
                """
        ) as tracker:
            self.wait_until_bookmark("quotient")
            scroll.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Now let's multiply: <bookmark mark='multiply' /> three multiplied by x <bookmark mark='result' /> equals 3x
                """
        ) as tracker:
            self.wait_until_bookmark("multiply")
            self.play(indicate(quotient), indicate(divisor[0]))

            self.wait_until_bookmark("result")
            scroll.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)
                
        with self.voiceover(
                text="""
                And three multiplied by positive two
                <bookmark mark='result' /> equals positive six.
                """
        ) as tracker:
            self.play(indicate(quotient), indicate(divisor[1:]))

            self.wait_until_bookmark("result")
            scroll.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)
            
        with self.voiceover(
                text="""
                Now <bookmark mark='subtract' /> let's subtract.
                <bookmark mark='result_1' /> 3x minus 3x equals zero,
                <bookmark mark='result_2' /> 6 minus 6 equals 0.
                """
        ) as tracker:
            self.wait_until_bookmark("subtract")
            scroll.prepare_next(self, steps=2)

            self.wait_until_bookmark("result_1")
            self.play(indicate(dividend[:2]), indicate(division_step_1_3x))
            scroll.prepare_next(self)
            
            self.wait_until_bookmark("result_2")
            self.play(indicate(dividend[2:]), indicate(division_step_1_6))
            scroll.prepare_next(self)

            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                That means we have no remainder. <bookmark mark='remainder' /> 
                Therefore, our remainder <bookmark mark='remainder_value' /> is zero.
                """
        ) as tracker:
            self.wait_until_bookmark("remainder")
            scroll.prepare_next(self, steps=2)

            self.wait_until_bookmark("remainder_value")
            scroll.prepare_next(self)

            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Now we will take our answer from <bookmark mark='long_div' /> the long division
                and put it into the <bookmark mark='format' /> standard format.

                a is the remainder, which <bookmark mark='remainder' /> equals zero.
                x minus h is the divisor, which <bookmark mark='divisor' /> is x plus two.
                k is the quotient, which <bookmark mark='quotient' /> equals 3.
                """
        ) as tracker:
            self.wait_until_bookmark("long_div")
            self.play(indicate(division_steps))

            self.wait_until_bookmark("format")
            self.play(indicate(general_form_group))

            scroll.prepare_next(self, steps=3)
            self.play(FadeIn(tip_2, shift=UP))

            self.wait_until_bookmark("remainder")
            scroll.fade_in_from_target(self, zero, run_time=2)
            
            self.wait_until_bookmark("divisor")
            scroll.fade_in_from_target(self, divisor, run_time=2)

            self.wait_until_bookmark("quotient")
            self.play(FadeOut(tip_2, shift=DOWN))
            scroll.fade_in_from_target(self, quotient, run_time=2)
            scroll.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Let's substitute these values into our standard form.
                We get <bookmark mark='substitution' /> y equals zero over x plus two, plus 3.
                
                But since <bookmark mark='numerator' /> the numerator is zero, this simplifies to <bookmark mark='simplified' /> just y equals 3.
                """
        ) as tracker:
            self.wait_until_bookmark("substitution")
            self.play(FadeIn(simplified_y_group))
            
            self.wait_until_bookmark("numerator")
            self.play(indicate(simplified_y_term_2))
            
            self.wait_until_bookmark("simplified")
            scroll.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Now this is an interesting result! Our rational function has simplified to a constant function.
                This happened because the numerator is perfectly divisible by the denominator, leaving no remainder.
                """
        ) as tracker:
            self.play(indicate(final_y))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Now let's identify our asymptotes.
                We <bookmark mark='h_asy' /> have y equals k as our horizontal asymptote, which is y equals 3.
                And we <bookmark mark='v_asy' /> typically have x equals h as our vertical asymptote, which would be x equals negative 2.
                """
        ) as tracker:
            scroll.scroll_down(self, steps=steps_to_scroll)
            scroll.prepare_next(self)

            self.wait_until_bookmark("h_asy")
            y_callout.show()
            
            self.wait_until_bookmark("v_asy")
            y_callout.hide()
            x_callout.show()
            
            self.wait(STANDARD_PAUSE)
            x_callout.hide()
            
        with self.voiceover(
                text="""
                For our function, we have a vertical asymptote at <bookmark mark='v_asymptote' /> x equals negative 2,
                because this would make the denominator zero in our original function.
                
                However, it's important to note that <bookmark mark='note' /> since our function simplifies to y equals 3,
                this actually means we have a horizontal line at y equals 3 with a hole at x equals negative 2.
                """
        ) as tracker:
            self.wait_until_bookmark("v_asymptote")
            scroll.prepare_next(self)
            self.play(FadeIn(tip_3, shift=UP))
            
            self.wait_until_bookmark("note")
            self.play(FadeOut(tip_3, shift=DOWN))
            scroll.prepare_next(self, steps=2)
            self.play(indicate(asymptote_note))
            self.play(FadeIn(tip_4, shift=UP))
            
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_4, shift=DOWN))

        with self.voiceover(
                text="""
                Let's draw a <bookmark mark='v_line' /> vertical dotted line at x equals negative 2 representing where we have a hole in our function.
                And let's draw a <bookmark mark='h_line' /> horizontal line at y equals 3 representing our simplified function.
                """
        ) as tracker:
            self.wait_until_bookmark("v_line")
            self.play(Write(v_asymptote), run_time=2)
            
            self.wait_until_bookmark("h_line")
            self.play(Write(h_asymptote), run_time=2)
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Before we proceed to graphing, let's <bookmark mark='overlay' /> understand the significance of the sign of 'a' in our standard form.

                When 'a' is positive, the hyperbola branches will appear in the first and third quadrants relative to the asymptotes. This means one branch appears above and to the right of the intersection of the asymptotes, while the other branch appears below and to the left.

                If 'a' is negative, the hyperbola branches will instead appear in the second and fourth quadrants as shown.
                """
        ) as tracker:
            self.wait_until_bookmark("overlay")
            self.play(FadeIn(blank_screen))
        self.play(FadeOut(blank_screen))

        with self.voiceover(
                text="""
                However, in our function, 'a' is zero which means we don't have the typical hyperbola shape at all.
                <bookmark mark='tip' /> Instead, we have a horizontal line.
                """
        ) as tracker:
            self.wait_until_bookmark("tip")
            self.play(FadeIn(tip_5, shift=UP))
            self.wait(STANDARD_PAUSE)
        self.play(FadeOut(tip_5, shift=DOWN))

        with self.voiceover(
                text="""
                Let's calculate a few points to confirm our function is indeed a horizontal line.
                For <bookmark mark='point1' /> x equals negative 3, we get y equals 3.
                """
        ) as tracker:
            scroll.prepare_next(self)
            
            self.wait_until_bookmark("point1")
            scroll.prepare_next(self)
            self.play(FadeIn(point1))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                For <bookmark mark='point2' /> x equals 0, we again get y equals 3.
                """
        ) as tracker:
            self.wait_until_bookmark("point2")
            scroll.prepare_next(self)
            self.play(FadeIn(point2))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                And for <bookmark mark='point3' /> x equals 1, we once again get y equals 3.
                """
        ) as tracker:
            self.wait_until_bookmark("point3")
            scroll.prepare_next(self)
            self.play(FadeIn(point3))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Now we can draw our graph.
                It's simply <bookmark mark='graph' /> a horizontal line at y equals 3, 
                with a <bookmark mark='hole' /> hole at x equals negative 2.
                
                This is quite different from our typical rational function graphs!
                """
        ) as tracker:
            self.wait_until_bookmark("graph")
            self.play(Create(left_graph), Create(right_graph), run_time=3)
            
            self.wait_until_bookmark("hole")
            hole_point = Dot(axes.c2p(-2, 3), color=RED, radius=POINT_RADIUS, fill_opacity=0)
            hole_point_border = Circle(radius=0.1, color=RED).move_to(axes.c2p(-2, 3))
            self.play(Create(hole_point_border))
            
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Let's review what happened. Our original function <bookmark mark='original' /> y equals 3x plus 6 divided by x plus 2
                was able to be simplified through long division.
                
                We found that <bookmark mark='quotient' /> the quotient is 3 and there is no remainder,
                which means our function <bookmark mark='final' /> simplifies to y equals 3.
                
                This is a special case of rational functions where the numerator is perfectly divisible by the denominator,
                resulting in a polynomial function - in this case, a constant function.
                
                The only important feature to remember is the <bookmark mark='hole' /> hole at x equals negative 2,
                which exists because this input value is undefined in the original rational function.
                """
        ) as tracker:
            self.wait_until_bookmark("original")
            self.play(indicate(example_func))
            
            self.wait_until_bookmark("quotient")
            self.play(indicate(quotient), indicate(remainder))
            
            self.wait_until_bookmark("final")
            self.play(indicate(final_y))
            
            self.wait_until_bookmark("hole")
            self.play(indicate(hole_point_border))
            
            self.wait(COMPREHENSION_PAUSE)
            
        self.wait(3)