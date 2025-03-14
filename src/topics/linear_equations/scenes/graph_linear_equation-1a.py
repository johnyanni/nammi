"""Tutorial on graphing linear equations using slope-intercept form."""
"""new features"""
from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

class LinearEquationsGraphLinearEquation(MathTutorialScene):
    """A tutorial that teaches how to graph a linear equation using slope-intercept form."""

    def construct(self):
        # Define colors (these are specific to this tutorial)
        y_intercept_color = YELLOW
        slope_color = BLUE
        rise_color = BLUE
        run_color = RED

        # Create axes
        axes, axes_labels = self.create_axes()

        # Create visual elements
        start_coords = (0, -3)
        end_coords = (-1, 1)
        
        dot_start = Dot(axes.c2p(*start_coords), color=y_intercept_color, radius=0.15)
        dot_end = Dot(axes.c2p(*end_coords), color=WHITE, radius=0.15)
        
        
        def line_function(x):
            return -4*x - 3  # Our equation: y = -4x - 3

        # For the initial segment connecting just the two points
        # Instead of using axes.plot, let's create a Line object directly for better control
        point1 = axes.c2p(start_coords[0], start_coords[1])  # (0, -3)
        point2 = axes.c2p(end_coords[0], end_coords[1])      # (-1, 1)
        connecting_line = Line(
            start=point1,
            end=point2,
            color=BLUE
        )

        # For the extended line showing the full graph
        extended_line = axes.plot(
            line_function, 
            x_range=[-2, 1],  # This range can be adjusted as needed
            color=BLUE
        )

        # Add tips to the extended line with fixed orientation
        start_point = axes.c2p(-2, line_function(-2))
        end_point = axes.c2p(1, line_function(1))

        start_tip = ArrowTriangleFilledTip(color=BLUE, length=0.2)
        end_tip = ArrowTriangleFilledTip(color=BLUE, length=0.2)

        # Position tips at the ends with fixed angles
        start_tip.move_to(start_point)
        start_tip.rotate(angle_of_vector([1, -4]))  # Add PI to point in opposite direction
        end_tip.move_to(end_point)
        end_tip.rotate(angle_of_vector([1, -4])+ PI)
        
        
        extended_line_group = VGroup(extended_line, start_tip, end_tip)
        
        
        
        
        
        
        
        # Create rise arrows
        rise_arrows = []
        for i in range(4):
            start_y = -3 + i
            arrow = Arrow(
                start=axes.c2p(0, start_y),
                end=axes.c2p(0, start_y + 1),
                color=rise_color,
                buff=0,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.4
            )
            rise_arrows.append(arrow)
        
        # Create run arrow
        run_arrows = Arrow(
            start=axes.c2p(0, 1),
            end=axes.c2p(-1, 1),
            color=run_color,
            buff=0,
            stroke_width=10,
            max_tip_length_to_length_ratio=0.4
        )
        
        # Create rise text label
        rise_text_group = self.create_text_with_background(
            r"\text{Rise} = 4",
            text_color=rise_color
        ).scale(MATH_SCALE)
        rise_text_group.next_to(rise_arrows[1], LEFT, buff=0.5)
        
        # Create run text label
        
        run_text_group = self.create_text_with_background(
            r"\text{Run} = 1",
            text_color=run_color
        ).scale(MATH_SCALE)
        run_text_group.next_to(run_arrows[1], UP, buff=0.5)
        



        # Problem statement
        problem_text = MathTex(r"\text{Graph: } y = -4x - 3").scale(MATH_SCALE)
        
        # Step 1: Identify Components
        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_info_2 = MathTex(r"\text{Slope } (m) = -4", color=slope_color).scale(MATH_SCALE)
        step1_info_3 = MathTex(r"\text{Y-intercept } (b) = -3", color=y_intercept_color).scale(MATH_SCALE)
        
        # Step 2: Plot Y-intercept
        step2_title = Tex("Step 2: Plot Y-intercept").scale(TEXT_SCALE)
        step2_info = MathTex(r"\text{Plot point } (0, -3)", color=y_intercept_color).scale(MATH_SCALE)

        # Step 3: Use Slope to Find Second Point
        step3_title = Tex("Step 3: Use Slope to Find Second Point").scale(TEXT_SCALE)
        step3_info_1 = MathTex(r"\text{Slope } = -4 = \frac{\text{rise}}{\text{run}} = -\frac{4}{1}").scale(MATH_SCALE)
        step3_info_2 = MathTex(r"\text{From } (0, -3)\text{:}").scale(MATH_SCALE)
        step3_info_3 = MathTex(r"\text{Rise } 4 \text{ units UP}", color=rise_color).scale(MATH_SCALE)
        step3_info_4 = MathTex(r"\text{Run } 1 \text{ unit LEFT}", color=run_color).scale(MATH_SCALE)
        step3_info_5 = MathTex(r"\text{Second point: } (-1, 1)").scale(MATH_SCALE)

        # Step 4: Draw Line
        step4_title = Tex("Step 4: Draw Line Through Points").scale(TEXT_SCALE)
        step4_info_1 = MathTex(r"\text{Connect points } (0, -3) \text{ and } (-1, 1)").scale(MATH_SCALE)
        step4_info_2 = MathTex(r"\text{Extend line in both directions}").scale(MATH_SCALE)
        
        final_equation = MathTex(r"y = -4x - 3").scale(MATH_SCALE)
        final_equation.next_to(start_point, LEFT + DOWN, buff=0.7)  # Position with both LEFT and DOWN buffs
        final_equation_boxed_group = self.create_equation_box(final_equation, color=slope_color)
        
        
        self.color_component(step1_info_1, "m", slope_color)
        self.color_component(step1_info_1, "b", y_intercept_color)
        SmartColorizeStatic(step3_info_1,
            {r"\text{rise}": rise_color, r"\text{run}": run_color, "4": rise_color, "1": run_color}
        )
        

        # Organize step groups
        step1_group = self.create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        step2_group = self.create_step(step2_title, step2_info)
        step3_group = self.create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5)
        step4_group = self.create_step(step4_title, step4_info_1, step4_info_2)
        
        # Create steps group with problem text
        steps_group = VGroup(
            problem_text,
            step1_group,
            step2_group,
            step3_group,
            step4_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title).set_color(GREY)

        # Position the entire content
        steps_group.to_edge(LEFT, buff=0.6).to_edge(UP, buff=0.6)

        # Set up solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text,
            step1_title,
            step1_info_1, step1_info_2, step1_info_3,
            step2_title,
            step2_info,
            step3_title,
            step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5,
            step4_title,
            step4_info_1, step4_info_2
        )
        
        scroll_mgr = ScrollManager(solution_steps)
        
        tip_1 = QuickTip(
            "When the slope (m) is negative we go up (rise) and then to the left (run).",
            fill_opacity=1
        ).shift(DOWN * 2)
        
        black_screen = SlopeOverlay()

        # Animation sequence with voiceovers
        with self.voiceover("Let's graph the linear equation y equals negative 4x minus 3."):
            self.play(Write(axes), Write(axes_labels))
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: We'll identify the key components of the equation."):
            scroll_mgr.prepare_next(self)

        with self.voiceover("This equation is in slope-intercept form: y equals mx plus b."):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("The coefficient of x is the slope. Here, m equals negative 4."):
            self.highlight_formula_component(step1_info_1, "m", slope_color)
            scroll_mgr.prepare_next(self)
            self.play(ReplacementTransform(problem_text[0][8:10].copy(), step1_info_2[0][-2:]))
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("The constant term is the y-intercept. Here, b, equals negative 3."):
            self.highlight_formula_component(step1_info_1, "b", y_intercept_color)
            scroll_mgr.prepare_next(self)
            self.play(ReplacementTransform(problem_text[0][-2:].copy(), step1_info_3[0][-2:]))
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover("At the y-intercept, x equals 0, <bookmark mark='plot'/> so we plot the point (0, -3)."):
            scroll_mgr.prepare_next(self)
            self.wait_until_bookmark("plot")
            self.play(Indicate(dot_start))
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 3: Now we'll use the slope to find a second point on the line."):
            scroll_mgr.scroll_down(self, steps=1)
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("The slope negative 4 can be expressed as a fraction: <bookmark mark='fraction'/> negative 4 over 1, which is the ratio of rise over run."):
            self.wait_until_bookmark("fraction")
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Starting from our y-intercept at (0, -3):"):
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover("The rise is 4 units up, because the slope is negative 4."):
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("The run is 1 unit to the left. <bookmark mark='run'/> We go left because the slope is negative."):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Let's visualize this with arrows. Each green arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)

        with self.voiceover("And the red arrow shows our run of 1 unit to the left."):
            self.play(GrowArrow(run_arrows))
            self.play(Write(run_text_group))
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover("This gives us our second point <bookmark mark='second'/> at (-1, 1)."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
            self.wait_until_bookmark("second")
            self.play(Indicate(dot_end))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("When the given slope is negative, our line will slant to the left. Conversly, a positive slope will slant to the right."):
            self.play(FadeIn(black_screen))

        with self.voiceover("Step 4: Finally, we'll draw a straight line through these two points."):
            self.play(FadeOut(black_screen))
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("We connect the points (0, -3) and (-1, 1)."):
            self.play(Write(connecting_line))
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover("And extend the line in both directions <bookmark mark='extend'/> to complete our graph of y equals negative 4x minus 3."):
            scroll_mgr.prepare_next(self)
            self.play(
                ReplacementTransform(connecting_line, extended_line),
                FadeIn(start_tip),
                FadeIn(end_tip)
            )
            self.play(ReplacementTransform(problem_text[0][7:], final_equation_boxed_group))
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Notice how the negative slope creates a line that falls from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(extended_line, scale_factor=1.2))
        self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE)  # Test change to demonstrate branching
