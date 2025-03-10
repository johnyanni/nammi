"""Tutorial on finding equations of lines using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

class LinearEquationsFindSlopeIntercept(MathTutorialScene):
    """A tutorial that teaches how to find the equation of a line using slope-intercept form."""
    
    def construct(self):
        # Define colors (these are specific to this tutorial)
        y_intercept_color = YELLOW
        slope_color = GREEN
        rise_color = BLUE
        run_color = RED
        point_color = PINK

        # Create axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_ticks": True,
                "numbers_to_exclude": [0],
                "tip_length": 0.2,
                "tip_width": 0.2,
                "font_size": SMALL_FONT,
            },
            tips=True
        ).to_edge(RIGHT)

        axes_labels = VGroup(
            axes.get_x_axis_label("x"),
            axes.get_y_axis_label("y")
        )

        # Create the line y = (1/2)x + 1
        line = Line(
            start=axes.c2p(-6, -2),
            end=axes.c2p(6, 4),
            color=WHITE,
            stroke_width=3
        ).add_tip(
            at_start=True, 
            tip_length=0.2,
            tip_shape=ArrowTriangleFilledTip
        ).add_tip(
            tip_length=0.2,
            tip_shape=ArrowTriangleFilledTip
        )
        
        # Create our key points
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
        
        # Create equation label
        equation_label = MathTex(r"y = \frac{1}{2}x + 1").scale(MATH_SCALE)
        equation_label.next_to(axes.c2p(3, 0), UP, buff=0.4)
        equation_label.shift(RIGHT * 8)  # Start off-screen
        
        bg_rect = SurroundingRectangle(
            equation_label, 
            color=slope_color,
            fill_color="#121212",
            fill_opacity=0.8,
            buff=0.2,
            corner_radius=0.2
        )
        
        equation_group = VGroup(bg_rect, equation_label)
        
        black_screen = SlopeOverlay()

        # Problem statement
        problem_text = MathTex(r"\text{Find the equation of the given line.}").scale(MATH_SCALE)

        # Step 1: Identify two points on the line
        step1_title = Tex("Step 1: Identify Points on the Line").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Find the y-intercept where the line crosses the y-axis}").scale(MATH_SCALE)
        step1_info_2 = MathTex(r"\text{Y-intercept: } (0, 1)", color=y_intercept_color).scale(MATH_SCALE)
        step1_info_3 = MathTex(r"\text{Select another point: } (4, 3)", color=point_color).scale(MATH_SCALE)

        # Step 2: Calculate the Slope
        step2_title = Tex("Step 2: Calculate the Slope").scale(TEXT_SCALE)
        step2_info_1 = MathTex(r"\text{Slope } = \frac{\text{rise}}{\text{run}}").scale(MATH_SCALE)
        step2_info_2 = MathTex(r"\text{Slope } = \frac{2}{4} = \frac{1}{2}").scale(MATH_SCALE)
        
        # Step 3: Determine the equation using the slope-intercept form
        step3_title = Tex("Step 3: Write the Equation in Slope-Intercept Form").scale(TEXT_SCALE)
        step3_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step3_info_2 = MathTex(
            r"\text{Where } ",
            r"m",
            r" = \text{ slope and } ",
            r"b",
            r" = \text{ y-intercept}"
        ).scale(MATH_SCALE)
        step3_info_2[1].set_color(slope_color)  # Color 'm'
        step3_info_2[3].set_color(y_intercept_color)  # Color 'b'
        step3_info_3 = MathTex(r"m = \frac{1}{2}", color=slope_color).scale(MATH_SCALE)
        step3_info_4 = MathTex(r"b = 1", color=y_intercept_color).scale(MATH_SCALE)
        
        
        # Set up color mapping for elements
        m_char = step3_info_1[0][search_shape_in_text(step3_info_1, MathTex("m"))[0]]
        m_char.set_color(slope_color)

        b_char = step3_info_1[0][search_shape_in_text(step3_info_1, MathTex("b"))[0]]
        b_char.set_color(y_intercept_color)
        
        
        # Step 4: Write the Final Equation
        step4_title = Tex("Step 4: Write the Final Equation").scale(TEXT_SCALE)
        step4_info_0 = MathTex(r"y = mx + b").scale(MATH_SCALE)
        step4_info = MathTex(r"y = \frac{1}{2}x + 1").scale(MATH_SCALE)
    
        color_map_slope = {
            r"\text{rise}": rise_color,
            r"\text{run}": run_color,
            "1": y_intercept_color,
            "2": (rise_color, [0]),
            "4": run_color,
            r"\frac{1}{2}": slope_color,
            "m": slope_color,
            "b": y_intercept_color,
        }
        
        color_map_group = [step2_info_1, step2_info_2, step4_info, step4_info_0,]
        
        apply_smart_colorize(color_map_group, color_map_slope)
        
        # QuickTip
        tip_1 = QuickTip(
            "The slope measures how much the line rises or falls as we move from left to right.",
            fill_opacity=1
        ).shift(DOWN * 2)
        
 

        # Organize step groups
        step1_group = create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        step2_group = create_step(step2_title, step2_info_1, step2_info_2)
        step3_group = create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4)
        step4_group = create_step(step4_title, step4_info_0, step4_info)
        
        steps_group = VGroup(step1_group, step2_group, step3_group, step4_group).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title).set_color(GREY)

        # Position problem_text above the first step 
        problem_text.next_to(step1_title, UP, buff=0.4, aligned_edge=LEFT)

        # Create the combined group for everything
        all_content = VGroup(problem_text, steps_group)

        # Position the entire content
        all_content.to_edge(LEFT, buff=0.6).to_edge(UP, buff=0.6)

        # Set up solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text,
            step1_title,
            step1_info_1, step1_info_2, step1_info_3,
            step2_title,
            step2_info_1, step2_info_2,
            step3_title,
            step3_info_1, step3_info_2, step3_info_3, step3_info_4,
            step4_title, step4_info_0, step4_info
        )
        
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
                self.play(GrowArrow(arrow), run_time=0.8)
            self.wait(STANDARD_PAUSE)
            
        with self.voiceover("And the run between our points."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
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

        with self.voiceover("Where m is the slope and b is the y-intercept."):
            m_vertical_arrow = Arrow(
                start=m_char.get_top() + UP * 0.8,
                end=m_char.get_top() + UP * 0.10,
                buff=0.05,
                color=slope_color,
                stroke_width=6,
                tip_shape=ArrowTriangleFilledTip,
                max_tip_length_to_length_ratio=0.4
            )

            b_vertical_arrow = Arrow(
                start=b_char.get_top() + UP * 0.8,
                end=b_char.get_top() + UP * 0.10,
                buff=0.05,
                color=y_intercept_color,
                stroke_width=6,
                tip_shape=ArrowTriangleFilledTip,
                max_tip_length_to_length_ratio=0.4
            )
        
            self.play(GrowArrow(m_vertical_arrow))
            self.play(Indicate(m_char, color=slope_color, scale_factor=1.8))
            
            scroll_mgr.prepare_next(self)
            
            self.play(GrowArrow(b_vertical_arrow))
            self.play(Indicate(b_char, color=y_intercept_color, scale_factor=1.8))
            
            self.wait(STANDARD_PAUSE)
            self.play(FadeOut(m_vertical_arrow), FadeOut(b_vertical_arrow))

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
            self.play(
                equation_group.animate.next_to(axes.c2p(-3, 1), UP, buff=0.4),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("And there we have it! The equation of our line is y equals one-half x plus 1."):
            self.play(Indicate(equation_label, scale_factor=1.1))
            self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE) 