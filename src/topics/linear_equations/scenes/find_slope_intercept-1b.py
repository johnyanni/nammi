"""Tutorial on finding equations of lines using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

class LinearEquationsFindSlopeIntercept1b(MathTutorialScene):
    """A tutorial that teaches how to find the equation of a line using slope-intercept form."""

    def construct(self):
        # Define colors (these are specific to this tutorial)
        y_intercept_color = YELLOW
        slope_color = GREEN
        rise_color = BLUE
        run_color = RED
        point_color = PINK

        # Create axes
        axes, axes_labels = self.create_axes()
        axes.to_edge(RIGHT)

        # Create the line y = (1/2)x + 1
        def line_function(x):
            return 0.5*x + 1  # Our equation: y = (1/2)x + 1

        # For the full line with tips
        extended_line = axes.plot(
            line_function, 
            x_range=[-6, 6],
            color=WHITE,
            stroke_width=3
        )
        
        # Add tips to the line
        start_point = axes.c2p(-6, line_function(-6))
        end_point = axes.c2p(6, line_function(6))
        
        start_tip = ArrowTriangleFilledTip(color=WHITE, length=0.2)
        end_tip = ArrowTriangleFilledTip(color=WHITE, length=0.2)
        
        # Position tips at the ends with fixed angles
        start_tip.move_to(start_point)
        start_tip.rotate(angle_of_vector([1, 0.5]))  # Use the slope angle
        end_tip.move_to(end_point)
        end_tip.rotate(angle_of_vector([1, 0.5]) + PI)  # Add PI to point in opposite direction
        
        # Group the line and tips
        line = VGroup(extended_line, start_tip, end_tip)
        
        # Create key points on the line
        y_intercept_point = Dot(axes.c2p(0, 1), color=y_intercept_color, radius=0.15)
        point1 = Dot(axes.c2p(0, 1), color=point_color, radius=0.15)
        point2 = Dot(axes.c2p(4, 3), color=point_color, radius=0.15)

        # Create rise arrows
        rise_arrows = []
        for i in range(2):
            start_y = 1 + i
            arrow = Arrow(
                start=axes.c2p(0, start_y),
                end=axes.c2p(0, start_y + 1),
                color=rise_color,
                buff=0,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.4
            )
            rise_arrows.append(arrow)
        
        # Create run arrows
        run_arrows = []
        for i in range(4):
            start_x = i
            arrow = Arrow(
                start=axes.c2p(start_x, 3),
                end=axes.c2p(start_x + 1, 3),
                color=run_color,
                buff=0,
                max_tip_length_to_length_ratio=0.4,
                max_stroke_width_to_length_ratio=10,
            )
            run_arrows.append(arrow)
        
        black_screen = SlopeOverlay()


        problem_text = Tex("Find the equation of the given line.").scale(MATH_SCALE)

        step1_title = Tex("Step 1: Identify Points on the Line").scale(TEXT_SCALE)
        step1_info_1 = Tex("Find the y-intercept where the line crosses the y-axis").scale(MATH_SCALE)
        step1_info_2 = MathTex(r"\text{Y-intercept: } (0, 1)", color=y_intercept_color).scale(MATH_SCALE)
        step1_info_3 = MathTex(r"\text{Select another point: } (4, 3)", color=point_color).scale(MATH_SCALE)

        step2_title = Tex("Step 2: Calculate the Slope").scale(TEXT_SCALE)
        step2_info_1 = MathTex(r"\text{Slope } = \frac{\text{rise}}{\text{run}}").scale(MATH_SCALE)
        step2_info_2 = MathTex(r"\text{Slope } = \frac{2}{4} = \frac{1}{2}").scale(MATH_SCALE)
        
        step3_title = Tex("Step 3: Write the Equation in Slope-Intercept Form").scale(TEXT_SCALE)
        step3_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step3_info_2 = MathTex(r"\text{Where } m \text{ = slope and } b \text{ = y-intercept}").scale(TEXT_SCALE)
        step3_info_3 = MathTex(r"m = \frac{1}{2}", color=slope_color).scale(MATH_SCALE)
        step3_info_4 = MathTex(r"b = 1", color=y_intercept_color).scale(MATH_SCALE)
        
        step4_title = Tex("Step 4: Write the Final Equation").scale(TEXT_SCALE)
        step4_info_1 = MathTex(r"y = mx + b").scale(MATH_SCALE)
        step4_info_2 = MathTex(r"y = \frac{1}{2}x + 1").scale(MATH_SCALE)
        
        final_equation = MathTex(r"y = -4x - 3").scale(MATH_SCALE)
        final_equation.next_to(start_point, LEFT + DOWN, buff=0.7)  # Position with both LEFT and DOWN buffs
        final_equation_boxed_group = self.create_equation_box(final_equation, color=slope_color)
        
        
        self.color_component(step3_info_1, "m", slope_color)
        self.color_component(step3_info_1, "b", y_intercept_color)
        
        # Define smart coloring for multiple elements
        smart_coloring = self.setup_smart_coloring({
            step2_info_1: [r"Slope", r"\text{rise}", r"\text{run}"],
            step2_info_2: [r"Slope", "2", "4", r"\frac{1}{2}"],
            step3_info_2: [r"m \text{ = slope", r"b \text{ = y-intercept"],
            step4_info_1: ["m", "b"],
            step4_info_2: [r"\frac{1}{2}", "1"]
        }, {
            "Slope": slope_color,
            "m": slope_color,
            "b": y_intercept_color,
            r"\text{rise}": rise_color,
            r"\text{run}": run_color,
            "2": rise_color,
            "4": run_color,
            r"\frac{1}{2}": slope_color,
            "1": y_intercept_color,
            r"m \text{ = slope": slope_color,
            r"b \text{ = y-intercept": y_intercept_color
        })
        
        # Apply all smart coloring at once
        self.apply_element_specific_coloring(smart_coloring)
        

        # Organize step groups
        step1_group = self.create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        step2_group = self.create_step(step2_title, step2_info_1, step2_info_2)
        step3_group = self.create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4)
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
            step2_info_1, step2_info_2,
            step3_title,
            step3_info_1, step3_info_2, step3_info_3, step3_info_4,
            step4_title,
            step4_info_1, step4_info_2
        )
        
        # QuickTip
        tip_1 = QuickTip(
            "The slope measures how much the line rises or falls as we move from left to right.",
            fill_opacity=1
        ).shift(DOWN * 2)
        
        scroll_mgr = ScrollManager(solution_steps)

        # Animation sequence with voiceovers
        with self.voiceover("Given a line on a coordinate plane, let's find its equation."):
            self.play(Write(axes), Write(axes_labels), Write(line))
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: First, we need to identify at least two points on the line."):
            scroll_mgr.prepare_next(self)

        with self.voiceover("Let's find the y-intercept, which is where the line crosses the y-axis."):
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("The y-intercept is at the point (0, 1)."):
            scroll_mgr.prepare_next(self)
            self.play(Indicate(y_intercept_point))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("We'll also select another point on the line. Let's use (4, 3)."):
            scroll_mgr.prepare_next(self)
            self.play(Indicate(point2))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 2: Now let's calculate the slope of the line."):
            scroll_mgr.scroll_down(self, steps=1)
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("The slope is the ratio of the rise to the run."):
            scroll_mgr.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("To visualize this, let's see the rise between our two points."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.wait(STANDARD_PAUSE)
            
        with self.voiceover("And the run between our points."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(STANDARD_PAUSE)
            
        with self.voiceover("Calculating the slope: The rise is 2 units, and the run is 4 units. So, the slope is two-fourths, which simplifies to one-half."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover("Step 3: Now we can write the equation using the slope-intercept form."):
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("The slope-intercept form of a line is y equals mx plus b."):
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Where m is the slope <break time=\"1s\"/> and b is the y-intercept."):
            self.highlight_formula_component(step3_info_1, "m", slope_color)
            scroll_mgr.prepare_next(self)
            self.highlight_formula_component(step3_info_1, "b", y_intercept_color)
            
        with self.voiceover("We found that the slope m equals one-half."):
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)
            
        with self.voiceover("When the given slope is positive, our line will slant to the right. Conversly, a negative slope will slant to the left."):
            self.play(FadeIn(black_screen))

        with self.voiceover("And the y-intercept, b equals 1."):
            self.play(FadeOut(black_screen))
            scroll_mgr.prepare_next(self)
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Step 4: Finally, let's write the complete equation of the line."):
            scroll_mgr.scroll_down(self, steps=3)
            scroll_mgr.prepare_next(self)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Substituting our values into the slope-intercept form, we get y equals one-half x plus 1."):
            scroll_mgr.prepare_next(self)
            scroll_mgr.prepare_next(self)
            self.play(ReplacementTransform(problem_text, final_equation_boxed_group))
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("And there we have it! The equation of our line is y equals one-half x plus 1."):
            self.play(Indicate(final_equation_boxed_group, scale_factor=1.2))
            self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE) 