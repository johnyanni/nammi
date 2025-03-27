"""Tutorial on graphing the rational function y = (3x+6)/(x+2) without using ScrollManager."""

from manim import *
from src.components.common.base_scene import *
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

def SmartColorizeStatic(text, color_map):
    """Simple placeholder for SmartColorizeStatic function."""
    for pattern, color in color_map.items():
        # This is a simple implementation that won't handle complex cases
        try:
            text.set_color_by_tex(pattern, color)
        except:
            pass
    return text

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
        
        def indicate(mobject, color=INDICATION_COLOR, run_time=INDICATION_TIME):
            return Indicate(mobject, color=color, run_time=run_time)
        
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
        
        # Setup the coordinate axes
        axes = Axes(
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

        # Setup general form and background
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
        
        # Step 1: Problem statement
        example_func = MathTex(r"y = \frac{3x + 6}{x + 2}").scale(TEX_SCALE).to_corner(UL)
        example_func_num = example_func[0][3:8]  # Adjust indices as needed
        example_func_den = example_func[0][9:14]  # Adjust indices as needed
        example_func_num.set_color(DIVIDEND_COLOR)
        example_func_den.set_color(DIVISOR_COLOR)
        
        # Introduction
        with self.voiceover(
            text="""In this video, we'll explore how to graph the rational function y equals three x plus six, divided by x plus two."""
        ):
            self.play(FadeIn(axes, general_form_group))
            self.play(Write(example_func))
            
        with self.voiceover(text="Let's examine this rational function."):
            self.play(indicate(example_func))
            
        with self.voiceover(
            text="""To graph it effectively, we first need to transform it into this format: y equals "a" over x minus h plus k.
            
            This format represents a hyperbola, and once we have it, we can easily identify the asymptotes,
            details, and key characteristics that will help us create an accurate graph."""
        ):
            self.play(indicate(general_form_group))
            
        with self.voiceover(
            text="""Our first step is to divide the numerator into the denominator, which is the polynomial you see here."""
        ):
            self.play(indicate(example_func_num), indicate(example_func_den))
            
        # Step 2: Long division
        division_title = Tex("Step 1: Long Division").scale(LABEL_SCALE).to_corner(UL)
        
        division_setup = MathTex(r"x + 2\ \overline{\strut \smash{)}\ 3x + 6\ }").scale(TEX_SCALE)
        division_symbol = division_setup[0][3:5] 
        divisor = division_setup[0][0:3].set_color(DIVISOR_COLOR)
        dividend = division_setup[0][7:12].set_color(DIVIDEND_COLOR)
        
        division_step_1 = MathTex("-(3x + 6)").scale(TEX_SCALE).set_color(STEP_COLOR)
        division_step_1_3x = division_step_1[0][2:4]
        division_step_1_6 = division_step_1[0][5:7]
        
        hline = Line(
            start=ORIGIN, 
            end=RIGHT * division_step_1.width
        ).scale(TEX_SCALE)
        
        zero_zero = MathTex("0\\, \\, \\, \\, 0").scale(TEX_SCALE).set_color(STEP_COLOR)
        quotient = MathTex("3", color=K_COLOR).scale(TEX_SCALE)
        
        remainder = MathTex("r = 0", color=REMAINDER_COLOR).scale(TEX_SCALE)
        remainder_rec = self.create_surrounding_rectangle(remainder)
        
        # Arranging division steps
        division_steps = VGroup(
            division_setup,
            division_step_1,
            hline,
            zero_zero
        ).arrange(DOWN, aligned_edge=LEFT)
        
        quotient.next_to(division_setup, UP)
        remainder.next_to(zero_zero, RIGHT, buff=1.0)
        remainder_rec.move_to(remainder)
        
        # Group all division elements
        division_group = VGroup(
            division_title,
            division_steps,
            quotient,
            remainder,
            remainder_rec
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_corner(UL).shift(DOWN * 0.5)
        
        # Show long division
        with self.voiceover(text="Now, we will do the division."):
            self.play(FadeOut(example_func), FadeIn(division_title))
            self.play(Write(division_setup))
            
        with self.voiceover(
            text="""We start by recognizing that our divisor is x plus 2,
            and we're dividing it into our polynomial, 3x plus 6."""
        ):
            self.play(indicate(divisor), indicate(dividend))
            tip_1 = QuickTip("This is simply long division as in other chapters.").to_corner(DR)
            self.play(FadeIn(tip_1))
            self.wait(QUICK_PAUSE)
            self.play(FadeOut(tip_1))
            
        with self.voiceover(
            text="""First, we divide: x divides into 3x to give us three."""
        ):
            self.play(Write(quotient))
            
        with self.voiceover(
            text="""Now let's multiply: three multiplied by x equals 3x and three multiplied by positive two equals positive six."""
        ):
            self.play(indicate(quotient), indicate(divisor))
            self.play(Write(division_step_1))
            
        with self.voiceover(
            text="""Now let's subtract. 3x minus 3x equals zero, 6 minus 6 equals 0."""
        ):
            self.play(Write(hline), Write(zero_zero))
            
        with self.voiceover(
            text="""That means we have no remainder. Therefore, our remainder is zero."""
        ):
            self.play(Write(remainder), Write(remainder_rec))
            
        # Step 3: Standard form
        standard_form_title = Tex("Step 2: Write in Standard Form").scale(LABEL_SCALE)
        
        simplified_y = MathTex(r"y = \frac{0}{x + 2} + 3").scale(TEX_SCALE)
        SmartColorizeStatic(
            simplified_y,
            {
                "0": A_COLOR,
                "x + 2": DIVISOR_COLOR,
                "3": K_COLOR
            }
        )
        
        final_y = MathTex(r"y = 3").scale(TEX_SCALE * 1.2)
        final_y.set_color(K_COLOR)
        
        simplified_y_rec = self.create_surrounding_rectangle(simplified_y)
        final_y_rec = self.create_surrounding_rectangle(final_y)
        
        standard_form_group = VGroup(
            standard_form_title,
            simplified_y,
            simplified_y_rec,
            final_y,
            final_y_rec
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        with self.voiceover(
            text="""Now we will take our answer from the long division and put it into the standard format.
            
            a is the remainder, which equals zero.
            x minus h is the divisor, which is x plus two.
            k is the quotient, which equals 3."""
        ):
            # Clear the screen and show step 2
            self.play(FadeOut(division_group))
            standard_form_group.to_corner(UL)
            self.play(FadeIn(standard_form_title))
            
            tip_2 = QuickTip("Note that $a$ is the remainder and $k$ is the quotient").to_corner(DR)
            self.play(FadeIn(tip_2))
            self.play(Write(simplified_y), Write(simplified_y_rec))
            self.play(FadeOut(tip_2))
            
        with self.voiceover(
            text="""Let's substitute these values into our standard form.
            We get y equals zero over x plus two, plus 3.
            
            But since the numerator is zero, this simplifies to just y equals 3."""
        ):
            self.play(Write(final_y), Write(final_y_rec))
            
        # Step 4: Asymptotes
        asymptotes_title = Tex("Step 3: Identify Asymptotes").scale(LABEL_SCALE)
        
        x_asymptote_text = MathTex("x = -2", color=DIVISOR_COLOR).scale(TEX_SCALE)
        y_asymptote_text = MathTex("y = 3", color=K_COLOR).scale(TEX_SCALE)
        asymptotes_group = VGroup(x_asymptote_text, y_asymptote_text).arrange(RIGHT, buff=1.0)
        
        asymptote_note = MathTex(r"\text{Note: When }a = 0\text{, }y = k\text{ is a horizontal line}").scale(TEXT_SCALE)
        self.apply_smart_colorize(
            [asymptote_note],
            {
                "a = 0": A_COLOR,
                "y = k": K_COLOR
            }
        )
        
        asymptotes_complete = VGroup(
            asymptotes_title,
            asymptotes_group,
            asymptote_note
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        with self.voiceover(
            text="""Now let's identify our asymptotes.
            We typically have y equals k as our horizontal asymptote, which is y equals 3.
            And we typically have x equals h as our vertical asymptote, which would be x equals negative 2."""
        ):
            # Clear the screen and show step 3
            self.play(FadeOut(standard_form_group))
            asymptotes_complete.to_corner(UL)
            self.play(FadeIn(asymptotes_title, asymptotes_group))
            
            # Show callouts
            x_callout.show()
            self.wait(1)
            x_callout.hide()
            y_callout.show()
            self.wait(1)
            y_callout.hide()
            
        with self.voiceover(
            text="""For our function, we have a vertical asymptote at x equals negative 2,
            because this would make the denominator zero in our original function.
            
            However, it's important to note that since our function simplifies to y equals 3,
            this actually means we have a horizontal line at y equals 3 with a hole at x equals negative 2."""
        ):
            self.play(Write(asymptote_note))
            
            tip_3 = QuickTip("$x = -2$ is a vertical asymptote since $y$ will be undefined at that point.").to_corner(DR)
            self.play(FadeIn(tip_3))
            self.wait(STANDARD_PAUSE)
            self.play(FadeOut(tip_3))
            
            tip_4 = QuickTip("Since the remainder is 0, our function simplifies to $y = 3$, which is a horizontal line.").to_corner(DR)
            self.play(FadeIn(tip_4))
            self.wait(STANDARD_PAUSE)
            self.play(FadeOut(tip_4))
            
        with self.voiceover(
            text="""Let's draw a vertical dotted line at x equals negative 2 representing where we have a hole in our function.
            And let's draw a horizontal line at y equals 3 representing our simplified function."""
        ):
            self.play(Write(v_asymptote), Write(h_asymptote))
            
        # Step 5: Graph points
        points_title = Tex("Step 4: Calculate Points").scale(LABEL_SCALE)
        
        point1 = Dot(axes.c2p(-3, 3), color=POINT_COLOR, radius=POINT_RADIUS)
        point2 = Dot(axes.c2p(0, 3), color=POINT_COLOR, radius=POINT_RADIUS)
        point3 = Dot(axes.c2p(1, 3), color=POINT_COLOR, radius=POINT_RADIUS)
        
        point1_calc = MathTex(r"(-3, 3)").scale(TEX_SCALE).set_color(POINT_COLOR)
        point2_calc = MathTex(r"(0, 3)").scale(TEX_SCALE).set_color(POINT_COLOR)
        point3_calc = MathTex(r"(1, 3)").scale(TEX_SCALE).set_color(POINT_COLOR)
        
        points_list = VGroup(point1_calc, point2_calc, point3_calc).arrange(DOWN, buff=0.3)
        
        points_group = VGroup(
            points_title,
            points_list
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        with self.voiceover(
            text="""Let's calculate a few points to confirm our function is indeed a horizontal line.
            For x equals negative 3, we get y equals 3.
            For x equals 0, we again get y equals 3.
            And for x equals 1, we once again get y equals 3."""
        ):
            # Clear the screen and show step 4
            self.play(FadeOut(asymptotes_complete))
            points_group.to_corner(UL)
            self.play(FadeIn(points_title, points_list))
            
            # Show points on the graph
            self.play(FadeIn(point1))
            self.wait(QUICK_PAUSE)
            self.play(FadeIn(point2))
            self.wait(QUICK_PAUSE)
            self.play(FadeIn(point3))
            
        # Step 6: Draw the graph
        graph_title = Tex("Step 5: Draw the Graph").scale(LABEL_SCALE)
        
        # Function for the graph
        def func(x):
            if abs(x + 2) < 0.1:  # Avoid division near asymptote
                return np.nan
            return 3  # y = 3x+6 / x+2 = 3 + 0/(x+2) = 3
        
        left_x_range = [-4, -2.1]
        right_x_range = [-1.9, 4]
        
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
        
        # Create a hole at x = -2, y = 3
        hole_point = Dot(axes.c2p(-2, 3), color=RED, radius=POINT_RADIUS, fill_opacity=0)
        hole_point_border = Circle(radius=0.1, color=RED).move_to(axes.c2p(-2, 3))
        
        graph_text = MathTex(r"y = 3 \text{ with a hole at } x = -2").scale(TEX_SCALE)
        
        graph_group = VGroup(
            graph_title,
            graph_text
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        with self.voiceover(
            text="""Now we can draw our graph.
            It's simply a horizontal line at y equals 3, with a hole at x equals negative 2.
            
            This is quite different from our typical rational function graphs!"""
        ):
            # Clear the screen and show step 5
            self.play(FadeOut(points_group))
            graph_group.to_corner(UL)
            self.play(FadeIn(graph_title, graph_text))
            
            # Draw the graph
            self.play(Create(left_graph), Create(right_graph))
            self.play(Create(hole_point_border))
            
            tip_5 = QuickTip("When $a = 0$, the function becomes a horizontal line with no vertical asymptote behavior.").to_corner(DR)
            self.play(FadeIn(tip_5))
            self.wait(COMPREHENSION_PAUSE)
            self.play(FadeOut(tip_5))
            
        # Blank screen for special cases explanation
        blank_screen = FullScreenOverlay("Effect of the sign of a", show_examples=True)
        
        with self.voiceover(
            text="""Before we conclude, let's understand the significance of the sign of 'a' in our standard form.

            When 'a' is positive, the hyperbola branches will appear in the first and third quadrants relative to the asymptotes. This means one branch appears above and to the right of the intersection of the asymptotes, while the other branch appears below and to the left.

            If 'a' is negative, the hyperbola branches will instead appear in the second and fourth quadrants as shown.
            
            However, in our function, 'a' is zero which means we don't have the typical hyperbola shape at all. Instead, we have a horizontal line."""
        ):
            self.play(FadeIn(blank_screen))
            self.wait(STANDARD_PAUSE)
            self.play(FadeOut(blank_screen))
            
        # Conclusion
        conclusion_title = Tex("Summary").scale(LABEL_SCALE)
        
        summary_points = VGroup(
            Tex("• Original function: $y = \\frac{3x+6}{x+2}$"),
            Tex("• Long division: quotient = 3, remainder = 0"),
            Tex("• Simplified to $y = 3$ (horizontal line)"),
            Tex("• Hole at $x = -2$ (where denominator = 0)"),
            Tex("• Special case: When remainder = 0, no hyperbola")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE)
        
        conclusion_group = VGroup(
            conclusion_title,
            summary_points
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        with self.voiceover(
            text="""Let's review what happened. Our original function y equals 3x plus 6 divided by x plus 2
            was able to be simplified through long division.
            
            We found that the quotient is 3 and there is no remainder,
            which means our function simplifies to y equals 3.
            
            This is a special case of rational functions where the numerator is perfectly divisible by the denominator,
            resulting in a polynomial function - in this case, a constant function.
            
            The only important feature to remember is the hole at x equals negative 2,
            which exists because this input value is undefined in the original rational function."""
        ):
            # Clear the screen and show conclusion
            self.play(FadeOut(graph_group))
            conclusion_group.to_corner(UL)
            self.play(FadeIn(conclusion_title, summary_points))
            
            # Highlight the graph one more time
            self.play(Indicate(left_graph), Indicate(right_graph), Indicate(hole_point_border))
            
        # Final animation
        final_equation = MathTex(r"y = 3 \text{ (with a hole at } x = -2 \text{)}").scale(TEX_SCALE * 1.3)
        
        with self.voiceover(
            text="""This example shows us that not all rational functions result in hyperbolas.
            When the numerator is perfectly divisible by the denominator, we get a simpler function,
            but we must always check for values that make the denominator zero,
            as these will create holes in our graph."""
        ):
            self.play(FadeOut(conclusion_group))
            self.play(FadeIn(final_equation.to_edge(UP)))
            self.wait(3)