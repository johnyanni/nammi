"""Tutorial on graphing rational functions using long division to convert to hyperbola form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.styles.constants import *
import numpy as np

class GraphingRationalFunctionTutorial(MathTutorialScene):
    """A tutorial that teaches how to graph the rational function (4x-10)/(x-3)."""

    def construct(self):
        ###############################################################################
        # SECTION 1: DEFINE COLORS AND CONSTANTS
        ###############################################################################
        # Define colors for different parts of the solution
        numerator_color = BLUE
        denominator_color = RED
        quotient_color = GREEN
        remainder_color = ORANGE
        vertical_asymptote_color = RED
        horizontal_asymptote_color = GREEN
        function_color = WHITE
        point_color = YELLOW
        curve_color = BLUE

        # Define function parameters directly
        original_function = r"y = \frac{4x-10}{x-3}"
        hyperbola_form = r"y = 4 + \frac{2}{x-3}"
        
        # Define key features
        vertical_asymptote_value = 3
        vertical_asymptote_tex = "x = 3"
        horizontal_asymptote_value = 4
        horizontal_asymptote_tex = "y = 4"
        x_intercept_value = 2.5
        x_intercept_tex = "x = 2.5"
        y_intercept_value = 10/3
        y_intercept_tex = r"y = \frac{10}{3}"
        
        # Define ranges for graphing
        x_range = [-1, 8, 1]
        y_range = [-10, 10, 1]
        x_length = 7
        y_length = 7
        left_curve_range = [-1, 2.9]
        right_curve_range = [3.1, 8]
        
        # Define sample points for plotting
        points = [
            {"x": 0, "y": 3.33},   # y-intercept
            {"x": 1, "y": 3},
            {"x": 2, "y": 2},
            {"x": 2.5, "y": 0},    # x-intercept
            {"x": 4, "y": 6},
            {"x": 5, "y": 5}
        ]

        ###############################################################################
        # SECTION 2: COORDINATE PLANE SETUP
        ###############################################################################
        # Create axes
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

        ###############################################################################
        # SECTION 3: FUNCTION AND ASYMPTOTE SETUP
        ###############################################################################
        # Function to evaluate the rational function
        def rational_function(x):
            if abs(x - vertical_asymptote_value) < 0.1:  # Avoid division near asymptote
                return np.nan
            return (horizontal_asymptote_value + 2 / (x - vertical_asymptote_value))
        
        # Create vertical asymptote line
        vertical_asymptote_line = DashedLine(
            start=axes.c2p(vertical_asymptote_value, y_range[0]),
            end=axes.c2p(vertical_asymptote_value, y_range[1]),
            color=vertical_asymptote_color,
            stroke_width=2,
            dash_length=0.15
        )

        # Create horizontal asymptote line
        horizontal_asymptote_line = DashedLine(
            start=axes.c2p(x_range[0], horizontal_asymptote_value),
            end=axes.c2p(x_range[1], horizontal_asymptote_value),
            color=horizontal_asymptote_color,
            stroke_width=2,
            dash_length=0.15
        )
        
        # Create text labels for asymptotes
        vertical_asymptote_label = MathTex(
            vertical_asymptote_tex, 
            color=vertical_asymptote_color
        ).scale(0.7).next_to(vertical_asymptote_line, UP, buff=0.2)
        
        horizontal_asymptote_label = MathTex(
            horizontal_asymptote_tex, 
            color=horizontal_asymptote_color
        ).scale(0.7).next_to(horizontal_asymptote_line, RIGHT, buff=0.2)

        # Create left and right parts of the curve
        left_curve = axes.plot(
            rational_function,
            x_range=left_curve_range,
            color=curve_color,
            stroke_width=3
        )
        
        right_curve = axes.plot(
            rational_function,
            x_range=right_curve_range,
            color=curve_color,
            stroke_width=3
        )
        
        # Create the complete curve group
        curve_group = VGroup(left_curve, right_curve)
        
        ###############################################################################
        # SECTION 4: SAMPLE POINTS SETUP
        ###############################################################################
        # Create dots for important points
        point_dots = VGroup()
        point_labels = VGroup()
        
        for point in points:
            x, y = point["x"], point["y"]
            dot = Dot(axes.c2p(x, y), color=point_color, radius=0.08)
            label = MathTex(f"({x}, {y})", color=point_color).scale(0.6).next_to(dot, UP+RIGHT, buff=0.1)
            point_dots.add(dot)
            point_labels.add(label)
        
        # Highlight x and y intercepts
        x_intercept_dot = Dot(
            axes.c2p(x_intercept_value, 0), 
            color=YELLOW, 
            radius=0.1
        )
        
        y_intercept_dot = Dot(
            axes.c2p(0, y_intercept_value), 
            color=YELLOW, 
            radius=0.1
        )
        
        x_intercept_label = MathTex(
            x_intercept_tex, 
            color=YELLOW
        ).scale(0.7).next_to(x_intercept_dot, DOWN, buff=0.2)
        
        y_intercept_label = MathTex(
            y_intercept_tex, 
            color=YELLOW
        ).scale(0.7).next_to(y_intercept_dot, LEFT, buff=0.2)
        
        # Create a group for all graphical elements
        graph_elements = VGroup(
            axes, axes_labels,
            vertical_asymptote_line, horizontal_asymptote_line,
            vertical_asymptote_label, horizontal_asymptote_label,
            curve_group,
            point_dots, point_labels,
            x_intercept_dot, y_intercept_dot,
            x_intercept_label, y_intercept_label
        )

        ###############################################################################
        # SECTION 5: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        problem_text = Tex("Graph the rational function:").scale(TEXT_SCALE)
        problem_function = MathTex(original_function).scale(MATH_SCALE)
        
        # Step 1: Convert to Hyperbola Form using Long Division
        step1_title = Tex("Step 1: Convert to Hyperbola Form using Long Division").scale(TEXT_SCALE)
        step1_p1 = MathTex(r"\text{Divide the numerator by the denominator:}").scale(TEXT_SCALE)
        
        # Create the long division box
        long_div = MathTex(
            r"\begin{array}{r}" +
            r"4 \phantom{000000} \\" +
            r"\overline{)1x-3\phantom{0}4x-10\phantom{0}}" + r"\\" +
            r"\underline{4x-12\phantom{00}}" + r"\\" +
            r"2 \phantom{000000}" + r"\\" +
            r"\end{array}"
        ).scale(MATH_SCALE)
        
        # Identify components from long division
        step1_p2 = MathTex(r"\text{Quotient } = 4").scale(MATH_SCALE)
        step1_p3 = MathTex(r"\text{Remainder } = 2").scale(MATH_SCALE)
        step1_p4 = MathTex(r"\text{Divisor } = x-3").scale(MATH_SCALE)
        
        # Write in hyperbola form
        step1_p5 = MathTex(r"\text{Converting to hyperbola form:}").scale(TEXT_SCALE)
        step1_p6 = MathTex(original_function, r" = ", r"4", r" + ", r"\frac{2}{x-3}").scale(MATH_SCALE)
        
        # Step 2: Identify Key Features
        step2_title = Tex("Step 2: Identify Key Features").scale(TEXT_SCALE)
        step2_p1 = MathTex(r"\text{Domain: } x \neq 3").scale(MATH_SCALE)
        step2_p2 = MathTex(r"\text{Vertical Asymptote: } x = 3").scale(MATH_SCALE)
        step2_p3 = MathTex(r"\text{Horizontal Asymptote: } y = 4").scale(MATH_SCALE)
        
        # Step 3: Find Intercepts
        step3_title = Tex("Step 3: Find Intercepts").scale(TEXT_SCALE)
        step3_p1 = MathTex(r"\text{For x-intercept, set } y = 0:").scale(MATH_SCALE)
        step3_p2 = MathTex(r"4 + \frac{2}{x-3} = 0").scale(MATH_SCALE)
        step3_p3 = MathTex(r"\frac{2}{x-3} = -4").scale(MATH_SCALE)
        step3_p4 = MathTex(r"2 = -4(x-3)").scale(MATH_SCALE)
        step3_p5 = MathTex(r"2 = -4x+12").scale(MATH_SCALE)
        step3_p6 = MathTex(r"4x = 10").scale(MATH_SCALE)
        step3_p7 = MathTex(r"x = 2.5").scale(MATH_SCALE)
        
        step3_p8 = MathTex(r"\text{For y-intercept, set } x = 0:").scale(MATH_SCALE)
        step3_p9 = MathTex(r"y = 4 + \frac{2}{0-3}").scale(MATH_SCALE)
        step3_p10 = MathTex(r"y = 4 + \frac{2}{-3}").scale(MATH_SCALE)
        step3_p11 = MathTex(r"y = 4 - \frac{2}{3}").scale(MATH_SCALE)
        step3_p12 = MathTex(r"y = \frac{12-2}{3} = \frac{10}{3} \approx 3.33").scale(MATH_SCALE)
        
        # Step 4: Calculate Additional Points
        step4_title = Tex("Step 4: Calculate Additional Points").scale(TEXT_SCALE)
        step4_p1 = MathTex(r"\text{For } x = 1: y = 4 + \frac{2}{1-3} = 4 + \frac{2}{-2} = 4 - 1 = 3").scale(MATH_SCALE)
        step4_p2 = MathTex(r"\text{For } x = 2: y = 4 + \frac{2}{2-3} = 4 + \frac{2}{-1} = 4 - 2 = 2").scale(MATH_SCALE)
        step4_p3 = MathTex(r"\text{For } x = 4: y = 4 + \frac{2}{4-3} = 4 + \frac{2}{1} = 4 + 2 = 6").scale(MATH_SCALE)
        step4_p4 = MathTex(r"\text{For } x = 5: y = 4 + \frac{2}{5-3} = 4 + \frac{2}{2} = 4 + 1 = 5").scale(MATH_SCALE)
        
        # Step 5: Sketch the Graph
        step5_title = Tex("Step 5: Sketch the Graph").scale(TEXT_SCALE)
        step5_p1 = MathTex(r"\text{Plot the vertical asymptote: } x = 3").scale(MATH_SCALE)
        step5_p2 = MathTex(r"\text{Plot the horizontal asymptote: } y = 4").scale(MATH_SCALE)
        step5_p3 = MathTex(r"\text{Plot intercepts and calculated points}").scale(MATH_SCALE)
        step5_p4 = MathTex(r"\text{Draw the two branches of the hyperbola}").scale(MATH_SCALE)
        step5_p5 = MathTex(r"\text{Note: Left branch approaches } y = 4 \text{ as } x \to -\infty").scale(TEXT_SCALE)
        step5_p6 = MathTex(r"\text{and approaches } y = -\infty \text{ as } x \to 3^-").scale(TEXT_SCALE)
        step5_p7 = MathTex(r"\text{Right branch approaches } y = +\infty \text{ as } x \to 3^+").scale(TEXT_SCALE)
        step5_p8 = MathTex(r"\text{and approaches } y = 4 \text{ as } x \to +\infty").scale(TEXT_SCALE)

        ###############################################################################
        # SECTION 6: COLORING AND STYLING SETUP
        ###############################################################################
        # Apply colors to long division
        self.color_component(long_div, "4", quotient_color)
        self.color_component(long_div, "2", remainder_color)
        self.color_component(long_div, "x-3", denominator_color)
        self.color_component(long_div, "4x-10", numerator_color)
        
        # Apply colors to identified components
        self.color_component(step1_p2, "4", quotient_color)
        self.color_component(step1_p3, "2", remainder_color)
        self.color_component(step1_p4, "x-3", denominator_color)
        
        # Color hyperbola form
        self.color_component(step1_p6, "4", quotient_color)
        self.color_component(step1_p6, "2", remainder_color)
        self.color_component(step1_p6, "x-3", denominator_color)
        
        # Color domains and asymptotes - using direct index instead of search
        # Safer approach than using search_shape_in_text for complex expressions
        try:
            # Try the color_component method first
            self.color_component(step2_p1, "x \neq 3", denominator_color)
        except (IndexError, ValueError):
            # Fallback: color the entire expression 
            step2_p1.set_color(denominator_color)
            
        try:
            self.color_component(step2_p2, "x = 3", vertical_asymptote_color)
        except (IndexError, ValueError):
            # Extract the "x = 3" part if possible, otherwise color whole expression
            step2_p2[0][-5:].set_color(vertical_asymptote_color)
            
        try:
            self.color_component(step2_p3, "y = 4", horizontal_asymptote_color)
        except (IndexError, ValueError):
            # Extract the "y = 4" part if possible, otherwise color whole expression
            step2_p3[0][-5:].set_color(horizontal_asymptote_color)
        
        # Color intercepts
        self.color_component(step3_p7, "2.5", point_color)
        self.color_component(step3_p12, r"\frac{10}{3}", point_color)
        self.color_component(step3_p12, "3.33", point_color)
        
        # Color calculated points
        self.color_component(step4_p1, "3", point_color)
        self.color_component(step4_p2, "2", point_color)
        self.color_component(step4_p3, "6", point_color)
        self.color_component(step4_p4, "5", point_color)

        ###############################################################################
        # SECTION 7: LAYOUT AND POSITIONING
        ###############################################################################
        # Organize step groups
        problem_group = VGroup(problem_text, problem_function).arrange(RIGHT, buff=0.3)
        step1_group = self.create_step(step1_title, step1_p1, long_div, step1_p2, step1_p3, step1_p4, step1_p5, step1_p6)
        step2_group = self.create_step(step2_title, step2_p1, step2_p2, step2_p3)
        step3_group = self.create_step(step3_title, 
            step3_p1, step3_p2, step3_p3, step3_p4, step3_p5, step3_p6, step3_p7,
            step3_p8, step3_p9, step3_p10, step3_p11, step3_p12
        )
        step4_group = self.create_step(step4_title, step4_p1, step4_p2, step4_p3, step4_p4)
        step5_group = self.create_step(step5_title, step5_p1, step5_p2, step5_p3, step5_p4, 
                                      step5_p5, step5_p6, step5_p7, step5_p8)
        
        # Create steps group with problem text
        steps_group = VGroup(
            problem_group,
            step1_group,
            step2_group,
            step3_group,
            step4_group,
            step5_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title, step5_title).set_color(GREY)

        # Position the entire content
        steps_group.to_edge(LEFT, buff=0.6).to_edge(UP, buff=0.6)

        ###############################################################################
        # SECTION 8: SCROLL MANAGER AND UI ELEMENTS SETUP
        ###############################################################################
        # Set up solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text, problem_function,
            step1_title, step1_p1, long_div, step1_p2, step1_p3, step1_p4, step1_p5, step1_p6,
            step2_title, step2_p1, step2_p2, step2_p3,
            step3_title, 
            step3_p1, step3_p2, step3_p3, step3_p4, step3_p5, step3_p6, step3_p7,
            step3_p8, step3_p9, step3_p10, step3_p11, step3_p12,
            step4_title, step4_p1, step4_p2, step4_p3, step4_p4,
            step5_title, step5_p1, step5_p2, step5_p3, step5_p4, 
            step5_p5, step5_p6, step5_p7, step5_p8
        )
        
        # Create QuickTip
        tip_1 = QuickTip(
            "In hyperbola form y = h + k/(x-a), the horizontal asymptote is y = h and the vertical asymptote is x = a.",
            fill_opacity=1
        ).shift(DOWN * 3.5)
        
        scroll_mgr = ScrollManager(solution_steps)

        ###############################################################################
        # SECTION 9: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover("Let's graph the rational function y equals four x minus ten, divided by x minus three."):
            self.play(Write(problem_text), Write(problem_function))
            self.play(Create(axes), Write(axes_labels))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Step 1: We'll convert this function to hyperbola form using polynomial long division."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_title
        self.wait(QUICK_PAUSE)  

        with self.voiceover("We'll divide the numerator four x minus ten by the denominator x minus three."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p1
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Let's perform the long division."):
            scroll_mgr.prepare_next(self)  # Prepares: long_div
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("From our long division, we get a quotient of four."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p2
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("The remainder is two."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p3
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("And our divisor is x minus three."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p4
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Now we can convert our function to hyperbola form."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p5
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("The original function equals the quotient plus the remainder divided by the divisor: y equals four plus two divided by x minus three."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p6
            self.play(FadeIn(tip_1, shift=UP))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Step 2: Now let's identify the key features of our function based on its hyperbola form."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)  # Prepares: step2_title
            self.play(FadeOut(tip_1, shift=DOWN))
        self.wait(QUICK_PAUSE)  

        with self.voiceover("The domain is all real numbers except where the denominator equals zero, so x cannot equal 3."):
            scroll_mgr.prepare_next(self)  # Prepares: step2_p1
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("We have a vertical asymptote at x equals 3, where the denominator equals zero."):
            scroll_mgr.prepare_next(self)  # Prepares: step2_p2
            self.play(Create(vertical_asymptote_line), Write(vertical_asymptote_label))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("And a horizontal asymptote at y equals 4, which is the constant term in our hyperbola form."):
            scroll_mgr.prepare_next(self)  # Prepares: step2_p3
            self.play(Create(horizontal_asymptote_line), Write(horizontal_asymptote_label))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Step 3: Next, we'll find the intercepts of our function."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)  # Prepares: step3_title
        self.wait(QUICK_PAUSE)  

        with self.voiceover("For the x-intercept, we set y equal to zero and solve for x."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p1
        self.wait(STANDARD_PAUSE)  

        # Animation sequence for solving x-intercept
        with self.voiceover("We have:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p2
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Moving the 4 to the right side:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p3
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Multiplying both sides by x minus 3:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p4
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Distributing:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p5
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Rearranging to solve for x:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p6
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Therefore, the x-intercept is at x equals 2.5."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p7
            self.play(Create(x_intercept_dot), Write(x_intercept_label))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("For the y-intercept, we set x equal to zero and evaluate the function."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p8
        self.wait(STANDARD_PAUSE)  

        # Animation sequence for solving y-intercept
        with self.voiceover("Substituting x equals 0:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p9
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Simplifying:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p10
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Rewriting as subtraction:"):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p11
        self.wait(QUICK_PAUSE)  

        with self.voiceover("Therefore, the y-intercept is y equals ten thirds, which is approximately 3.33."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p12
            self.play(Create(y_intercept_dot), Write(y_intercept_label))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Step 4: Now, let's calculate some additional points to help us sketch the graph."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)  # Prepares: step4_title
        self.wait(QUICK_PAUSE)
        
        with self.voiceover("For x equals 1, y equals 3."):
            scroll_mgr.prepare_next(self)  # Prepares: step4_p1
            self.play(Indicate(point_dots[1]))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("For x equals 2, y equals 2."):
            scroll_mgr.prepare_next(self)  # Prepares: step4_p2
            self.play(Indicate(point_dots[2]))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("For x equals 4, y equals 6."):
            scroll_mgr.prepare_next(self)  # Prepares: step4_p3
            self.play(Indicate(point_dots[4]))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("For x equals 5, y equals 5."):
            scroll_mgr.prepare_next(self)  # Prepares: step4_p4
            self.play(Indicate(point_dots[5]))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Step 5: Finally, we'll sketch the graph based on our analysis."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)  # Prepares: step5_title
        self.wait(QUICK_PAUSE)
        
        with self.voiceover("We've already plotted the vertical asymptote at x equals 3."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p1
            self.play(Indicate(vertical_asymptote_line))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("And the horizontal asymptote at y equals 4."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p2
            self.play(Indicate(horizontal_asymptote_line))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("We've also plotted all our points, including the intercepts."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p3
            self.play(Indicate(point_dots), Indicate(x_intercept_dot), Indicate(y_intercept_dot))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Now, we'll draw the two branches of the hyperbola."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p4
        self.wait(QUICK_PAUSE)
        
        with self.voiceover("The left branch approaches y equals 4 as x approaches negative infinity."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p5
            self.play(Create(left_curve))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("And approaches negative infinity as x approaches 3 from the left."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p6
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("The right branch approaches positive infinity as x approaches 3 from the right."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p7
            self.play(Create(right_curve))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("And approaches y equals 4 as x approaches positive infinity."):
            scroll_mgr.prepare_next(self)  # Prepares: step5_p8
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Let's review all the key features of our rational function graph."):
            self.play(
                Indicate(horizontal_asymptote_line),
                Indicate(vertical_asymptote_line),
                run_time=2
            )
        self.wait(QUICK_PAUSE)
        
        with self.voiceover("Notice how both branches of the curve approach the horizontal asymptote y equals 4 as x moves away from the vertical asymptote."):
            self.play(
                Indicate(left_curve),
                Indicate(right_curve),
                run_time=2
            )
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("And observe how the curve crosses the x-axis at x equals 2.5 and the y-axis at y equals ten thirds."):
            self.play(
                Indicate(x_intercept_dot),
                Indicate(y_intercept_dot),
                run_time=2
            )
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("The hyperbola form y equals 4 plus 2 divided by x minus 3 clearly shows us that this is a vertically shifted hyperbola with a horizontal asymptote at y equals 4 and a vertical asymptote at x equals 3."):
            final_equation = MathTex(hyperbola_form, color=function_color).scale(MATH_SCALE*1.2)
            final_equation.to_edge(DOWN, buff=1)
            self.play(Write(final_equation))
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover("We've successfully graphed the rational function y equals four x minus ten divided by x minus three using the technique of long division to convert it to hyperbola form."):
            self.play(
                Indicate(final_equation),
                Indicate(curve_group),
                run_time=2
            )
        self.wait(END_PAUSE)