"""Tutorial on graphing linear equations using slope-intercept form - Simplified version."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

class LinearEquationsGraphLinearEquationB(MathTutorialScene):
    """A tutorial that teaches how to graph a linear equation using slope-intercept form."""
    
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
        start_coords = (0, -3)
        end_coords = (-1, 1)
        
        dot_start = Dot(axes.c2p(*start_coords), color=y_intercept_color, radius=0.15)
        dot_end = Dot(axes.c2p(*end_coords), color=WHITE, radius=0.15)
        
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
        run_arrow = Arrow(
            start=axes.c2p(0, 1),
            end=axes.c2p(-1, 1),
            color=run_color,
            buff=0,
            stroke_width=10,
            max_tip_length_to_length_ratio=0.4
        )
        
        # Create lines
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
        problem_minus_3 = problem_text[0][-1]  # Get the last character which is -3

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

        # Position everything
        problem_text.to_edge(UP, buff=0.5)
        problem_text.to_edge(LEFT, buff=0.5)
        
        # Define step spacing and maximum visible steps
        STEP_SPACING = 0.8  # Space between steps
        MAX_VISIBLE_STEPS = 3  # Maximum number of steps to show at once
        
        # Create a container for all steps
        steps_container = VGroup()
        
        # Function to position a step group
        def position_step_group(step_group, index):
            """Position a step group at the correct vertical position."""
            if index == 0:
                step_group.next_to(problem_text, DOWN, buff=0.5)
            else:
                step_group.next_to(steps_container[-1], DOWN, buff=STEP_SPACING)
            step_group.to_edge(LEFT, buff=0.5)
            return step_group
        
        # Function to update visible steps
        def update_visible_steps(new_step, index):
            """Update which steps are visible based on the current step index."""
            if index >= MAX_VISIBLE_STEPS:
                # Fade out the oldest visible step
                self.play(FadeOut(steps_container[0]))
                # Shift remaining steps up
                for i in range(1, len(steps_container)):
                    self.play(steps_container[i].animate.next_to(
                        steps_container[i-1] if i > 1 else problem_text,
                        DOWN,
                        buff=STEP_SPACING
                    ))
                # Remove the faded out step from container
                steps_container.remove(steps_container[0])
            
            # Add new step to container
            steps_container.add(new_step)
            return steps_container

        # Animation sequence with voiceovers
        with self.voiceover("Let's graph the linear equation y equals negative 4x minus 3."):
            self.play(Write(axes), Write(axes_labels))
            self.play(Write(problem_text))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: We'll identify the key components of the equation."):
            step1_group = VGroup(step1_title, step1_info_1, step1_info_2, step1_info_3)
            step1_group = position_step_group(step1_group, 0)
            self.play(Write(step1_group))
            steps_container.add(step1_group)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("This equation is in slope-intercept form: y equals mx plus b."):
            self.wait(STANDARD_PAUSE)

        with self.voiceover("The coefficient of x is the slope. Here, m equals negative 4."):
            self.highlight_formula_component(step1_info_1, "m", slope_color)
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("The constant term is the y-intercept. Here, b, equals negative 3."):
            self.highlight_formula_component(step1_info_1, "b", y_intercept_color)
            self.wait(COMPREHENSION_PAUSE)
            
            # Transform the -3 from problem_text to step1_info_3
            minus_3_copy = problem_minus_3.copy()
            step1_minus_3 = step1_info_3[0][-1]
            self.play(Transform(minus_3_copy, step1_minus_3))
            self.wait(COMPREHENSION_PAUSE)
            
            # Fade out problem text since we don't need it anymore
            self.play(FadeOut(problem_text))

        with self.voiceover("Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            step2_group = VGroup(step2_title, step2_info)
            step2_group = position_step_group(step2_group, 1)
            steps_container = update_visible_steps(step2_group, 1)
            self.play(FadeIn(step2_group))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("At the y-intercept, x equals 0, so we plot the point (0, -3)."):
            self.play(Indicate(dot_start))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 3: Now we'll use the slope to find a second point on the line."):
            step3_group = VGroup(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5)
            step3_group = position_step_group(step3_group, 2)
            steps_container = update_visible_steps(step3_group, 2)
            self.play(FadeIn(step3_group))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("The slope negative 4 can be expressed as a fraction: negative 4 over 1, which is the ratio of rise over run."):
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Starting from our y-intercept at (0, -3):"):
            self.wait(QUICK_PAUSE)

        with self.voiceover("The rise is 4 units up, because the slope is negative 4."):
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("The run is 1 unit to the left. We go left because the slope is negative."):
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Let's visualize this with arrows. Each green arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.wait(STANDARD_PAUSE)

        with self.voiceover("And the red arrow shows our run of 1 unit to the left."):
            self.play(GrowArrow(run_arrow))
            tip_1 = QuickTip(
                "When the slope (m) is negative we go up (rise) and then to the left (run).",
                fill_opacity=1
            ).shift(DOWN * 2)
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover("This gives us our second point at (-1, 1)."):
            self.play(Indicate(dot_end))
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("When the given slope is negative, our line will slant to the left. Conversely, a positive slope will slant to the right."):
            black_screen = SlopeOverlay()
            self.play(FadeIn(black_screen))

        with self.voiceover("Step 4: Finally, we'll draw a straight line through these two points."):
            self.play(FadeOut(black_screen))
            step4_group = VGroup(step4_title, step4_info_1, step4_info_2)
            step4_group = position_step_group(step4_group, 3)
            steps_container = update_visible_steps(step4_group, 3)
            self.play(FadeIn(step4_group))
            self.wait(STANDARD_PAUSE)

        with self.voiceover("We connect the points (0, -3) and (-1, 1)."):
            self.play(Write(pre_final_line))
            self.wait(QUICK_PAUSE)

        with self.voiceover("And extend the line in both directions to complete our graph of y equals negative 4x minus 3."):
            self.play(Write(final_line))
            # Create and position the final equation
            equation_label = MathTex(r"y = -4x - 3").scale(MATH_SCALE)
            bg_rect = SurroundingRectangle(
                equation_label, 
                color=BLUE,
                fill_color="#121212",
                fill_opacity=0.8,
                buff=0.2,
                corner_radius=0.2
            )
            equation_group = VGroup(bg_rect, equation_label)
            equation_group.next_to(axes.c2p(-5,1), UP, buff=0.4)
            self.play(
                FadeIn(equation_group),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover("Notice how the negative slope creates a line that falls from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(final_line, scale_factor=1.1))
            self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE) 