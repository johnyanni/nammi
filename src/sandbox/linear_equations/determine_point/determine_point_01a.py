from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.test_steps import TestSteps



SLOPE = -1
Y_INTERCEPT = 3                    
EQUATION_FORMATTED = "y = -x + 3"  


# Display and spoken representations
SLOPE_DISPLAY = "-"
SLOPE_SPOKEN = "minus"  
Y_INTERCEPT_DISPLAY = "3"  # without a sign
Y_INTERCEPT_SPOKEN = "three" # without a sign
SPOKEN_EQUATION = "y equals minus x plus three"

Y_INTERCEPT_SIGN = "-" if Y_INTERCEPT < 0 else "+"
Y_INTERCEPT_SIGN_SPOKEN = "negative" if Y_INTERCEPT < 0 else "plus"


# Point values
POINTS = [
    (3, 4),
    (2, 1),
]

# Coordinate points and visual ranges
X_RANGE = [-2, 6, 1]
Y_RANGE = [-1, 6, 1]
X_LINE_RANGE = [-1.5, 4.5]

# UI elements and styling
LINE_COLOR = "#00ccff"
POINT_COLOR = "#ff9500"
X_COLOR = "#36ff5a"
Y_COLOR = "#ff3366"

# Spacing
STEPS_BUFF = 0.70



class DeterminePoint01a(MathTutorialScene):

    def construct(self):
        ###############################################################################
        # SECTION 1: LINE GRAPH 
        ###############################################################################
        axes, axes_labels = self.create_axes(x_range=X_RANGE, y_range=Y_RANGE)
        
        def line_equation(x):
            return SLOPE * x + Y_INTERCEPT
        
        line_graph = axes.plot(
            line_equation, 
            x_range=X_LINE_RANGE,
            color=BLUE
        )

        # Add tips to the line
        start_point = axes.c2p(X_LINE_RANGE[0], line_equation(X_LINE_RANGE[0]))
        end_point = axes.c2p(X_LINE_RANGE[1], line_equation(X_LINE_RANGE[1]))

        start_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.3)
        end_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.3)

        # Position tips at the ends with fixed angles
        angle = angle_of_vector([1, SLOPE])
        start_tip.move_to(start_point)
        start_tip.rotate(angle)
        end_tip.move_to(end_point)
        end_tip.rotate(angle + PI)
        
        line_group = VGroup(line_graph, start_tip, end_tip)
        
        ###############################################################################
        # SECTION 2: EQUATION AND POINTS SETUP
        ###############################################################################
        equation = MathTex(EQUATION_FORMATTED).scale(MATH_SCALE).to_corner(UL)
        equation_equal_sign = equation[0][1]
        equation_slope = equation[0][search_shape_in_text(equation, MathTex(SLOPE_DISPLAY))[0]]
        equation_y_intercept_sign = equation[0][search_shape_in_text(equation, MathTex(Y_INTERCEPT_SIGN))[-1]] 
        equation_y_intercept = equation[0][search_shape_in_text(equation, MathTex(Y_INTERCEPT_DISPLAY))[-1]]
        
        SmartColorizeStatic(
            equation,
            {
                "y": Y_COLOR,
                "x": X_COLOR,
            }
        )
        
        points_text = VGroup()
        for point in POINTS:
            point_x, point_y = point
            point_label = MathTex(f"({point_x}, {point_y})").scale(MATH_SCALE)
            SmartColorizeStatic(
                point_label,
                {
                    f"{point[0]}": X_COLOR,
                    f"{point[1]}": Y_COLOR
                }
            )
            points_text.add(point_label)
        points_text.arrange(buff=0.5).next_to(equation, RIGHT * 10)

        # Label x and y of the points
        points_x_value = VGroup()
        points_y_value = VGroup()
        x_labels = VGroup()
        y_labels = VGroup()
        point_status = VGroup()
        for point_text, point in zip(points_text, POINTS):
            point_x = point_text[0][search_shape_in_text(point_text, MathTex(point[0]))[0]]
            point_y = point_text[0][search_shape_in_text(point_text, MathTex(point[1]))[-1]]
            
            x_label = MathTex("x", color=X_COLOR).scale(MATH_SCALE_SMALL).next_to(point_x, UP, aligned_edge=DOWN)
            y_label = MathTex("y", color=Y_COLOR).scale(MATH_SCALE_SMALL).next_to(point_y, UP, aligned_edge=DOWN)

            if line_equation(point[0]) == point[1]:
                point_status.add(MathTex(r"\checkmark", color=GREEN).scale(1).next_to(point_text, DOWN * 0.75))
            else:
                point_status.add(MathTex(r"\times", color=RED).scale(1).next_to(point_text, DOWN * 0.75))
            
            x_labels.add(x_label)
            y_labels.add(y_label)
            points_x_value.add(point_x)
            points_y_value.add(point_y)
                
        points_on_graph = VGroup()
        lines_to_points = VGroup()
        for point in POINTS:
            point_x, point_y = point
            point_coords = axes.c2p(point_x, point_y)
            point_dot = Dot(point_coords, color=POINT_COLOR)
            
            points_on_graph.add(point_dot)
            lines_to_points.add(axes.get_lines_to_point(axes.c2p(point_x, point_y)).set_color(GREEN))
            
        ###############################################################################
        # SECTION 3: TESTING POINTS
        ###############################################################################
        
        y_intercept_sign = "+" if Y_INTERCEPT > 0 else ""
        times = "\\times" if abs(SLOPE) != 1 else ""
        
        test_points_equations = VGroup()
        for point in POINTS:
            point_x, point_y = point
            result = "=" if line_equation(point_x) == point_y else "\\ne"
            
            test_step1 = MathTex(
                fr"{point_y} ={SLOPE_DISPLAY} {times} {point_x} {y_intercept_sign} {Y_INTERCEPT}"
            ).scale(MATH_SCALE)

            y_value = line_equation(point_x)
            if int(y_value) == y_value:
                y_value = int(y_value)
                
            test_step2 = MathTex(
                fr"{point_y} {result} {y_value}"
            ).scale(MATH_SCALE)

            steps = TestSteps(
                test_step1, test_step2,
                SLOPE_DISPLAY, Y_INTERCEPT_DISPLAY,
                title=f"Point $({point_x}, {point_y})$",
                title_scale=TEXT_SCALE,
                label_scale=TEXT_SCALE
            )

            steps.get_component("step_1_y").set_color(Y_COLOR)
            steps.get_component("step_2_y").set_color(Y_COLOR)
            steps.get_component("x").set_color(X_COLOR)

            test_points_equations.add(steps)
            
        test_points_equations.arrange(DOWN, aligned_edge=LEFT, buff=STEPS_BUFF).align_to(equation, LEFT).shift(DOWN/3)

        # Color points in the title
        for test, point in zip(test_points_equations, POINTS):
            SmartColorizeStatic(
                test.title,
                {
                    f"{point[0]}": X_COLOR,
                    f"{point[1]}": Y_COLOR,
                }
            )        
        
        ###############################################################################
        # SECTION 4: TIPS
        ###############################################################################
        test_results = dict()
        for point in POINTS:
            point_x, point_y = point
            test_results[f"({point_x}, {point_y})"] = line_equation(point_x) == point_y
                        
        tip_messages = [f"Simply plug in $x = {POINTS[0][0]}$ and $y = {POINTS[0][1]}$"]
        for point, result in test_results.items():
            satisfied = "" if result else "not"
            lies = "" if result else "doesn't"
            message = f"The equation is {satisfied} satisfied, so ${point}$ {lies} lies on the line"
            tip_messages.append(message)

        tips = VGroup()
        tip_1 = QuickTip(
            tip_messages[0],
            fill_opacity=1,
            color_map={
                str(POINTS[0][0]): X_COLOR,
                str(POINTS[0][1]): Y_COLOR,
            }
        )

        tips.add(tip_1)
        for message, point in zip(tip_messages[1:], POINTS):
            point_x, point_y = point

            tip = QuickTip(
                message,
                fill_opacity=1,
                color_map={
                    str(point_x): X_COLOR,
                    str(point_y): Y_COLOR,
                }
            )

            tips.add(tip)
        tips.to_corner(DR)

        ###############################################################################
        # SECTION 5: ANIMATION SEQUENCE
        ###############################################################################
        point_order = ["first", "second", "third", "fourth", "fifth"]
        
        with self.voiceover("In this video, we're going to check if certain points satisfy a given line equation"):
            self.play(FadeIn(equation, axes, axes_labels, line_group, points_text))

        with self.voiceover(f"We have the <bookmark mark='equation' /> equation {SPOKEN_EQUATION} already graphed, and we'll be testing {len(POINTS)} specific points"):
            self.wait_until_bookmark("equation")
            self.play(self.indicate(equation))

        # Indicate the points
        for j, point in enumerate(POINTS):
            if j == len(POINTS) - 1:
                with self.voiceover(f"and {point[0]}, {point[1]}"):
                    self.play(self.indicate(points_text[j]))
                break
                
            with self.voiceover(f"{point[0]}, {point[1]}"):
                self.play(self.indicate(points_text[j]))

        with self.voiceover("Instead of testing by plotting, we'll use algebra to verify whether these points lie on the line. Let's get started!"):
            pass

        for i, point in enumerate(POINTS):
            point_x, point_y = point
            with self.voiceover(f"Let's test our {point_order[i]} point; {point}"):
                self.play(self.indicate(points_text[i]))
                self.play(Write(test_points_equations[i].title))
                
            if i == 0:
                with self.voiceover(
                        text=f"""
                        We'll substitute x equals {point_x} and y equals {point_y} into our equation, then see if both sides of the equation are equal.
                        If they are, the point satisfies the equation and lies on the line.
                        After that, we'll repeat the same steps with the rest of the points.
                        """
                ):
                    pass
            
            with self.voiceover(f"We're going to substitute x equals {point_x} and y equals {point_y} into our equation"):
                self.play(FadeIn(x_labels[i], y_labels[i]))

            with self.voiceover(f"First, let's plug y <bookmark mark='y' /> equals {point_y} into the equation"):
                self.play(Write(test_points_equations[i].step_1_label))

                if i == 0:
                    self.play(FadeIn(tips[0], shift=UP))

                self.wait_until_bookmark("y")
                self.play(
                    ReplacementTransform(points_y_value[i].copy(), test_points_equations[i].get_component("step_1_y")),
                )

                self.wait(STANDARD_PAUSE)
            if i == 0:
                self.play(FadeOut(tips[0], shift=DOWN))

            with self.voiceover(f"Next, let's bring <bookmark mark='slope' /> down the {SLOPE_SPOKEN}"):
                self.wait_until_bookmark("slope")
                self.play(
                    ReplacementTransform(equation_equal_sign.copy(), test_points_equations[i].get_component("step_1_equal_sign")),
                    ReplacementTransform(equation_slope.copy(), test_points_equations[i].get_component("slope")),
                )


            times = test_points_equations[i].get_component("times")
            with self.voiceover(f"Now, we'll plug in x <bookmark mark='x' /> equals {point_x}"):
                self.wait_until_bookmark("x")

                if times:
                    self.play(Write(times))
                self.play(
                    ReplacementTransform(points_x_value[i].copy(), test_points_equations[i].get_component("x")),
                )
                self.wait(STANDARD_PAUSE)

            with self.voiceover(f"Finally, let's add <bookmark mark='y_intercept' /> the {Y_INTERCEPT_SIGN_SPOKEN} {Y_INTERCEPT_SPOKEN}"):
                self.wait_until_bookmark("y_intercept")
                self.play(
                    ReplacementTransform(equation_y_intercept_sign.copy(), test_points_equations[i].get_component("y_intercept_sign")),
                    ReplacementTransform(equation_y_intercept.copy(), test_points_equations[i].get_component("y_intercept"))
                )

                self.wait(COMPREHENSION_PAUSE)
                
            with self.voiceover(f"Let's now simplify the right-hand side to test if both sides are equal"):
                self.play(Write(test_points_equations[i].step_2_label))
                self.wait(QUICK_PAUSE)

            with self.voiceover(f"Bring down the {point_y}"):
                self.play(
                    ReplacementTransform(
                        test_points_equations[i].get_component("step_1_y").copy(),
                        test_points_equations[i].get_component("step_2_y"),
                    )
                )
                self.wait(QUICK_PAUSE)
                
            point_result = line_equation(point_x)
            point_result = int(point_result) if int(point_result) == point_result else point_result

            times_spoken = "" if abs(SLOPE) == 1 else "times"

            with self.voiceover(f"Now, {SLOPE_SPOKEN} {times_spoken} {point_x} {Y_INTERCEPT_SIGN_SPOKEN} {Y_INTERCEPT_SPOKEN} <bookmark mark='result' /> equals {point_result}"):
                self.wait_until_bookmark("result")
                self.play(Write(test_points_equations[i].get_component("step_2_right_side")))
                self.wait(STANDARD_PAUSE)
            
            if point_result != point_y:
                result_spoken = f"These values aren't equal! So the point {point} doesn't satisfy our equation"
                graph_spoken = "If we look closely, we can see that the point is indeed far away from the line."
                final_result = f"This confirms our work - the point {point} doesn't lie on the line {SPOKEN_EQUATION}"
            else:
                result_spoken = f"Both sides are equal! So the point {point} satisfies our equation"
                graph_spoken = "As we can see, the point is on the line"
                final_result = f"This confirms our work - the point {point} lies on the line {SPOKEN_EQUATION}"
                
            with self.voiceover(result_spoken):
                self.play(Write(test_points_equations[i].get_component("step_2_equal_sign")))

            self.play(FadeIn(tips[i + 1], shift=UP))
            self.play(Create(self.create_surrounding_rectangle(test_points_equations[i].step_2)))
            self.play(Write(point_status[i]))

            self.wait(COMPREHENSION_PAUSE)

            with self.voiceover("Let's visualize this point on the graph"):
                self.play(FadeOut(tips[i + 1], shift=DOWN))

            point_direction = "up" if point_y > 0 else "down"
            with self.voiceover(f"Find {point_x} on the x-axis, then go {point_direction} to the {point_y} on the y-axis") as tracker:
                self.play(
                    Create(lines_to_points[i]),
                    rate_func=linear,
                    run_time=tracker.duration
                )
                self.wait(COMPREHENSION_PAUSE)

            with self.voiceover("That puts the point <bookmark mark='point' /> right here"):
                self.wait_until_bookmark("point")
                self.play(FadeIn(points_on_graph[i]))
                self.play(FadeOut(lines_to_points[i]))

            with self.voiceover(graph_spoken):
                pass

            with self.voiceover(final_result):
                pass
            self.wait(COMPREHENSION_PAUSE)
        self.wait(5)