"""Tutorial on graphing linear equations using slope-intercept form."""

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

        # Create visual elements
        dot_start = Dot(axes.c2p(0, -3), color=y_intercept_color, radius=0.15)
        dot_end = Dot(axes.c2p(-1, 1), color=WHITE, radius=0.15)
        
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
        
        run_arrow = Arrow(
            start=axes.c2p(0, 1),
            end=axes.c2p(-1, 1),
            color=run_color,
            buff=0,
            stroke_width=10,
            max_tip_length_to_length_ratio=0.4
        )
        
        pre_final_line = Line(
            start=axes.c2p(0, -3),
            end=axes.c2p(-1, 1),
            color=BLUE
        )
        
        final_line = Line(
            start=axes.c2p(-2, 5),
            end=axes.c2p(1, -7),
            color=BLUE
        ).add_tip(
            at_start=True, 
            tip_length=0.2,
            tip_shape=ArrowTriangleFilledTip
        ).add_tip(
            tip_length=0.2,
            tip_shape=ArrowTriangleFilledTip
        )

        # Problem statement
        problem_text = MathTex(r"\text{Graph: } y = -4x - 3").scale(MATH_SCALE)

        # Step 1: Identify Components
        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_info_2 = MathTex(r"\text{Slope } (m) = -4", color=slope_color).scale(MATH_SCALE)
        step1_info_3 = MathTex(r"\text{Y-intercept } (b) = -3", color=y_intercept_color).scale(MATH_SCALE)
        
        m_char = step1_info_1[0][search_shape_in_text(step1_info_1, MathTex("m"))[0]]
        m_char.set_color(slope_color)

        b_char = step1_info_1[0][search_shape_in_text(step1_info_1, MathTex("b"))[0]]
        b_char.set_color(y_intercept_color)
    
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
        
        # final equation
        equation_label = MathTex(r"y = -4x - 3").scale(MATH_SCALE)
        equation_label.next_to(axes.c2p(-5, 1), UP, buff=0.4)
        equation_label.shift(RIGHT * 8)
        
        bg_rect = SurroundingRectangle(
            equation_label, 
            color=BLUE,
            fill_color="#121212",
            fill_opacity=0.8,
            buff=0.2,
            corner_radius=0.2
        )
        
        equation_group = VGroup(bg_rect, equation_label)

        # Organize step groups
        step1_group = create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        step2_group = create_step(step2_title, step2_info)
        step3_group = create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5)
        step4_group = create_step(step4_title, step4_title, step4_info_1, step4_info_2)
        
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
            step2_info,
            step3_title,
            step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5,
            step4_title,
            step4_info_1, step4_info_2
        )
        
        scroll_mgr = ScrollManager(solution_steps)
        
        color_map = {
            r"\text{rise}": rise_color,
            r"\text{run}": run_color,
            "4": rise_color,
            "1": run_color,
        }
        
        color_step_group = [step3_info_1]
        apply_smart_colorize(color_step_group, color_map)
        
        tip_1 = QuickTip(
            "When the slope (m) is negative we go up (rise) and then to the left (run).",
            fill_opacity=1
        ).shift(DOWN * 2)
        
        black_screen = SlopeOverlay()

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
            self.play(GrowArrow(m_vertical_arrow))
            scroll_mgr.prepare_next(self)
            self.play(Indicate(m_char, color=slope_color, scale_factor=1.8))
            self.wait(STANDARD_PAUSE)
            self.play(FadeOut(m_vertical_arrow))

        with self.voiceover("The constant term is the y-intercept. Here, b, equals negative 3."):
            self.play(GrowArrow(b_vertical_arrow))
            scroll_mgr.prepare_next(self)
            self.play(Indicate(b_char, color=y_intercept_color, scale_factor=1.8))
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            scroll_mgr.prepare_next(self)
            self.wait(QUICK_PAUSE)
            self.play(FadeOut(b_vertical_arrow))

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
            
        with self.voiceover("Let's visualize this with arrows. <bookmark mark='arcs'/> Each green arrow represents 1 unit of our rise."):
            self.wait_until_bookmark("arcs")
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("And the red arrow shows our run of 1 unit to the left."):
            self.play(GrowArrow(run_arrow))
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
            self.play(Write(pre_final_line))
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
            self.wait(QUICK_PAUSE)

        with self.voiceover("And extend the line in both directions <bookmark mark='extend'/> to complete our graph of y equals negative 4x minus 3."):
            scroll_mgr.prepare_next(self)
            self.play(Write(final_line))
            self.play(
                equation_group.animate.next_to(axes.c2p(-5,1), UP, buff=0.4),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("This <bookmark mark='summary'/> Notice how the negative slope creates a line that falls from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.wait_until_bookmark("summary")
            self.play(Indicate(final_line, scale_factor=1.1))
            self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE)