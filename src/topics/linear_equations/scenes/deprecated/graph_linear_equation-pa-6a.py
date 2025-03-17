"""Tutorial on graphing linear equations using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

# TEMPLATE PARAMETERS - These would be filled by AI or manually changed
# ------------------------------------------------
TEMPLATE_PARAMS = {
    "equation": {
        "slope": 0.25,                      # The slope value as a number (1/4)
        "slope_display": "\\frac{1}{4}",    # How the slope appears in LaTeX
        "slope_spoken": "one-fourth",       # How the slope should be spoken in voiceover
        "y_intercept": -3,                  # The y-intercept value as a number
        "y_intercept_display": "-3",        # How the y-intercept appears in LaTeX
        "y_intercept_spoken": "negative three",  # How the y-intercept should be spoken
        "formatted": "y=-3+\\frac{1}{4}x",  # Full equation with LaTeX
        "spoken": "y equals negative three plus one-fourth x",  # Spoken version for voiceover
        "slope_indices": [-4, -1],            # Index of the fraction in the MathTex object
        "y_intercept_indices": [2, 4],      # Index of the y-intercept in the MathTex object 
        "step1_info2_value_indices": [-3, None],  # Target indices in step1_info_2 for "\\frac{1}{4}"
        "step1_info3_value_indices": [-2, None]   # Target indices in step1_info_3 for "-3"
    },
    "points": {
        "y_intercept_point": [0, -3],       # Coordinates of y-intercept point
        "second_point": [4, -2]             # Coordinates of second point (rise 1, run 4)
    },
    "visual_ranges": {
        "axes_range": [-6, 6, 1],           # Range for axes: [min, max, step]
        "x_line_range": [-4, 5]             # X-range for plotting the line
    },
    "rise_run": {
        "rise_value": 1,                    # Absolute value of rise
        "rise_spoken": "one",               # Spoken version of rise value
        "run_value": 4,                     # Absolute value of run
        "run_spoken": "four",               # Spoken version of run value
        "rise_direction": "UP",             # Direction for rise: "UP" or "DOWN"
        "run_direction": "RIGHT"            # Direction for run: "LEFT" or "RIGHT"
    },
    "tip": {
        "message": "When the slope (m) is positive we go up (rise) and then to the right (run)."
    },
    "colors": {
        "y_intercept_color": "YELLOW", 
        "slope_color": "GREEN",
        "rise_color": "BLUE",
        "run_color": "RED",
        "line_color": "WHITE"
    }
}

class LinearEquationsGraphLinearEquation(MathTutorialScene):
    """A tutorial that teaches how to graph a linear equation using slope-intercept form."""

    def construct(self):
        ###############################################################################
        # SECTION 1: COLOR DEFINITIONS AND CONSTANTS
        ###############################################################################
        # Extract colors from parameters
        y_intercept_color = eval(TEMPLATE_PARAMS["colors"]["y_intercept_color"])
        slope_color = eval(TEMPLATE_PARAMS["colors"]["slope_color"])
        rise_color = eval(TEMPLATE_PARAMS["colors"]["rise_color"])
        run_color = eval(TEMPLATE_PARAMS["colors"]["run_color"])
        line_color = eval(TEMPLATE_PARAMS["colors"]["line_color"])

        # Extract equation parameters
        slope = TEMPLATE_PARAMS["equation"]["slope"]
        y_intercept = TEMPLATE_PARAMS["equation"]["y_intercept"]
        equation_str = TEMPLATE_PARAMS["equation"]["formatted"]
        slope_display = TEMPLATE_PARAMS["equation"]["slope_display"]
        y_intercept_display = TEMPLATE_PARAMS["equation"]["y_intercept_display"]
        spoken_equation = TEMPLATE_PARAMS["equation"]["spoken"]
        slope_spoken = TEMPLATE_PARAMS["equation"]["slope_spoken"]
        y_intercept_spoken = TEMPLATE_PARAMS["equation"]["y_intercept_spoken"]
        
        # Extract point coordinates
        start_coords = tuple(TEMPLATE_PARAMS["points"]["y_intercept_point"])
        end_coords = tuple(TEMPLATE_PARAMS["points"]["second_point"])
        
        # Extract rise/run values
        rise_value = TEMPLATE_PARAMS["rise_run"]["rise_value"]
        rise_spoken = TEMPLATE_PARAMS["rise_run"]["rise_spoken"]
        run_value = TEMPLATE_PARAMS["rise_run"]["run_value"]
        run_spoken = TEMPLATE_PARAMS["rise_run"]["run_spoken"]
        rise_direction = TEMPLATE_PARAMS["rise_run"]["rise_direction"]
        run_direction = TEMPLATE_PARAMS["rise_run"]["run_direction"]

        # Get source and target indices
        slope_src_start, slope_src_end = TEMPLATE_PARAMS["equation"]["slope_indices"]
        y_intercept_src_start, y_intercept_src_end = TEMPLATE_PARAMS["equation"]["y_intercept_indices"]
        slope_tgt_start, slope_tgt_end = TEMPLATE_PARAMS["equation"]["step1_info2_value_indices"]
        y_intercept_tgt_start, y_intercept_tgt_end = TEMPLATE_PARAMS["equation"]["step1_info3_value_indices"]

        ###############################################################################
        # SECTION 2: COORDINATE PLANE SETUP
        ###############################################################################
        # Create axes
        axes, axes_labels = self.create_axes(x_range=TEMPLATE_PARAMS["visual_ranges"]["axes_range"])

        ###############################################################################
        # SECTION 3: POINTS AND LINE SETUP
        ###############################################################################
        # Create visual elements
        dot_start = Dot(axes.c2p(*start_coords), color=y_intercept_color, radius=0.15)
        dot_end = Dot(axes.c2p(*end_coords), color=WHITE, radius=0.15)
        
        def line_function(x):
            return slope*x + y_intercept  # Our equation based on parameters

        # For the initial segment connecting just the two points
        point1 = axes.c2p(start_coords[0], start_coords[1])
        point2 = axes.c2p(end_coords[0], end_coords[1])
        
        connecting_line = Line(
            start=point1,
            end=point2,
            color=line_color
        )

        ###############################################################################
        # SECTION 4: EXTENDED LINE AND TIPS
        ###############################################################################
        # For the extended line showing the full graph
        x_range = TEMPLATE_PARAMS["visual_ranges"]["x_line_range"]
        extended_line = axes.plot(
            line_function, 
            x_range=x_range,
            color=line_color
        )

        # Add tips to the extended line
        start_point = axes.c2p(x_range[0], line_function(x_range[0]))
        end_point = axes.c2p(x_range[1], line_function(x_range[1]))

        start_tip = ArrowTriangleFilledTip(color=line_color, length=0.2)
        end_tip = ArrowTriangleFilledTip(color=line_color, length=0.2)

        # Position tips at the ends with fixed angles
        angle = angle_of_vector([1, slope])
        start_tip.move_to(start_point)
        start_tip.rotate(angle)
        end_tip.move_to(end_point)
        end_tip.rotate(angle + PI)
        
        extended_line_group = VGroup(extended_line, start_tip, end_tip)

        ###############################################################################
        # SECTION 5: RISE AND RUN ARROWS
        ###############################################################################
       # Create rise arrows based on parameters
        rise_arrows = []
        
        # Determine start position for rise arrows
        rise_start_x = start_coords[0]
        rise_start_y = start_coords[1]
        
        # Create rise arrows based on direction
        if rise_direction == "UP":
            for i in range(rise_value):
                arrow = Arrow(
                    start=axes.c2p(rise_start_x, rise_start_y + i),
                    end=axes.c2p(rise_start_x, rise_start_y + i + 1),
                    color=rise_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        else:  # DOWN
            for i in range(rise_value):
                arrow = Arrow(
                    start=axes.c2p(rise_start_x, rise_start_y - i),
                    end=axes.c2p(rise_start_x, rise_start_y - i - 1),
                    color=rise_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        
        run_arrows = []  # Initialize as a list instead of a single arrow
        run_start_x = start_coords[0]
        run_start_y = end_coords[1]  # The y-coordinate of the end point
        

        if run_direction == "LEFT":
            for i in range(run_value):
                arrow = Arrow(
                    start=axes.c2p(run_start_x - i, run_start_y),
                    end=axes.c2p(run_start_x - i - 1, run_start_y),
                    color=run_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                run_arrows.append(arrow)
        else:  # RIGHT
            for i in range(run_value):
                arrow = Arrow(
                    start=axes.c2p(run_start_x + i, run_start_y),
                    end=axes.c2p(run_start_x + i + 1, run_start_y),
                    color=run_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                run_arrows.append(arrow)

        ###############################################################################
        # SECTION 6: TEXT LABELS AND OVERLAYS
        ###############################################################################
        # Create rise text label
        rise_text_group = self.create_text_with_background(
            f"\\text{{Rise}} = {rise_value}",
            text_color=rise_color
        ).scale(MATH_SCALE)
        rise_text_group.next_to(rise_arrows[0], LEFT, buff=0.5)
        
        # Create run text label
        run_text_group = self.create_text_with_background(
            f"\\text{{Run}} = {run_value}",
            text_color=run_color
        ).scale(MATH_SCALE)
        run_text_group.next_to(run_arrows[0], UP, buff=0.5)

        ###############################################################################
        # SECTION 7: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        # Create the problem text with explicit parts for better control
        problem_text_label = Tex("Graph:").scale(MATH_SCALE)
        problem_text_equation = MathTex(equation_str).scale(MATH_SCALE)
        problem_text_equation.next_to(problem_text_label, RIGHT)
        
        # Get absolute slope for text
        abs_slope = abs(slope)
        slope_sign = "negative " if slope < 0 else ""

        # Step 1: Identify Components
        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_info_2 = MathTex(f"\\text{{Slope }} (m) = {slope_display}", color=slope_color).scale(MATH_SCALE)
        step1_info_3 = MathTex(f"\\text{{Y-intercept }} (b) = {y_intercept_display}", color=y_intercept_color).scale(MATH_SCALE)
        
        # Step 2: Plot Y-intercept
        step2_title = Tex("Step 2: Plot Y-intercept").scale(TEXT_SCALE)
        step2_info = MathTex(f"\\text{{Plot point }} ({start_coords[0]}, {start_coords[1]})", color=y_intercept_color).scale(MATH_SCALE)

        # Step 3: Use Slope to Find Second Point
        step3_title = Tex("Step 3: Use Slope to Find Second Point").scale(TEXT_SCALE)

        # More robust check if slope_display is a fraction (better than just checking for "\frac")
        def is_fraction_format(tex_string):
            # Check for \frac command with properly paired braces
            return "\\frac{" in tex_string and "}{" in tex_string and tex_string.endswith("}")

        # Determine if slope_display is already a fraction
        is_fraction = is_fraction_format(slope_display)

        # Create the appropriate equation based on whether slope_display is a fraction
        if is_fraction:
            # If slope_display is already a fraction, use it directly
            step3_info_1 = MathTex(f"\\text{{Slope }} = {slope_display} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)
        else:
            # If slope_display is not a fraction, display it as one (with denominator 1)
            # Handle both numeric and symbolic expressions
            try:
                # Try to interpret as a number
                slope_number = float(slope_display.replace("\\", ""))
                if slope_number < 0:
                    # For negative slopes, remove the negative sign and place it outside the fraction
                    converted_slope_display = f"-\\frac{{{slope_display.replace('-', '')}}}{{{1}}}"
                else:
                    # For positive slopes
                    converted_slope_display = f"\\frac{{{slope_display}}}{{{1}}}"
            except ValueError:
                # For symbolic expressions that aren't simple numbers
                if slope_display.startswith("-"):
                    # For negative symbolic expressions
                    converted_slope_display = f"-\\frac{{{slope_display[1:]}}}{{{1}}}"
                else:
                    # For positive symbolic expressions
                    converted_slope_display = f"\\frac{{{slope_display}}}{{{1}}}"
            
            step3_info_1 = MathTex(f"\\text{{Slope }} = {slope_display} = {converted_slope_display} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)

        step3_info_pre2 = MathTex(f"\\frac{{\\text{{rise}}}}{{\\text{{run}}}} = \\frac{{{rise_value}}}{{{run_value}}}").scale(MATH_SCALE) 
        step3_info_2 = MathTex(f"\\text{{From }} ({start_coords[0]}, {start_coords[1]})\\text{{:}}").scale(MATH_SCALE)
        step3_info_3 = MathTex(f"\\text{{Rise }} {rise_value} \\text{{ units {rise_direction}}}", color=rise_color).scale(MATH_SCALE)
        step3_info_4 = MathTex(f"\\text{{Run }} {run_value} \\text{{ unit {run_direction}}}", color=run_color).scale(MATH_SCALE)
        step3_info_5 = MathTex(f"\\text{{Second point: }} ({end_coords[0]}, {end_coords[1]})").scale(MATH_SCALE)

        # Step 4: Draw Line
        step4_title = Tex("Step 4: Draw Line Through Points").scale(TEXT_SCALE)
        step4_info_1 = MathTex(f"\\text{{Connect points }} ({start_coords[0]}, {start_coords[1]}) \\text{{ and }} ({end_coords[0]}, {end_coords[1]})").scale(MATH_SCALE)
        step4_info_2 = MathTex(r"\text{Extend line in both directions}").scale(MATH_SCALE)

        ###############################################################################
        # SECTION 8: FINAL EQUATION AND STYLING
        ###############################################################################
        final_equation = problem_text_equation.copy()
        final_equation.next_to(start_point, LEFT + DOWN, buff=0.7)  
        final_equation_group = self.create_text_with_background(final_equation, text_color=slope_color, border_color=slope_color)

        self.color_component(step1_info_1, "m", slope_color)
        self.color_component(step1_info_1, "b", y_intercept_color)
        SmartColorizeStatic(
            step3_info_1,
            {r"\text{rise}": rise_color, r"\text{run}": run_color, 
             f"{slope_display}": slope_color},   
        )
        SmartColorizeStatic(
            step3_info_pre2,
            {f"{rise_value}": rise_color, f"{run_value}": run_color},
        )

        ###############################################################################
        # SECTION 9: LAYOUT AND POSITIONING
        ###############################################################################
        # Organize step groups
        step1_group = self.create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        step2_group = self.create_step(step2_title, step2_info)
        step3_group = self.create_step(step3_title, step3_info_1, step3_info_pre2, step3_info_2, step3_info_3, step3_info_4, step3_info_5)
        step4_group = self.create_step(step4_title, step4_info_1, step4_info_2)
        
        steps_group = VGroup(
            VGroup(problem_text_label, problem_text_equation),
            step1_group,
            step2_group,
            step3_group,
            step4_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title).set_color(GREY)

        # Position the entire content
        steps_group.to_edge(LEFT, buff=0.6).to_edge(UP, buff=0.6)

        ###############################################################################
        # SECTION 10: SCROLL MANAGER AND UI SETUP
        ###############################################################################
        # Set up solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text_label,
            problem_text_equation,
            step1_title,
            step1_info_1,
            step1_info_2,
            step1_info_3,
            step2_title,
            step2_info,
            step3_title,
            step3_info_1, step3_info_pre2, step3_info_2, step3_info_3, step3_info_4, step3_info_5,
            step4_title,
            step4_info_1, step4_info_2
        )
        
        scroll_mgr = ScrollManager(solution_steps)
        
        tip_1 = QuickTip(
            TEMPLATE_PARAMS["tip"]["message"],
            fill_opacity=1
        ).shift(DOWN * 2)
        
        black_screen = SlopeOverlay()

        ###############################################################################
        # SECTION 11: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover(f"Let's graph the linear equation {spoken_equation}."):
            self.play(Write(axes), Write(axes_labels))
            scroll_mgr.prepare_next(self)
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: We'll identify the key components of the equation."):
            scroll_mgr.prepare_next(self)

        with self.voiceover("This equation is in slope-intercept form: y equals mx plus b."):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        # Animation for the slope
        with self.voiceover(f"The coefficient of x is the slope. Here, m equals {slope_spoken}."):
            self.highlight_formula_component(step1_info_1, "m", slope_color)
            
            # Prepare next with specifically calculated slice
            scroll_mgr.prepare_next(self, slice(0, slope_tgt_start))
            
            # Do the transformation with the parameterized indices
            try:
                self.play(ReplacementTransform(
                    problem_text_equation[0][slope_src_start:slope_src_end].copy(), 
                    step1_info_2[0][slope_tgt_start:slope_tgt_end]
                ))
            except Exception as e:
                print(f"Animation fallback due to: {e}")
                # If there's an error with indices, just indicate the text
                self.play(Indicate(step1_info_2))
                
        self.wait(COMPREHENSION_PAUSE)

        # Animation for the y-intercept
        with self.voiceover(f"The constant term is the y-intercept. Here, b equals {y_intercept_spoken}."):
            self.highlight_formula_component(step1_info_1, "b", y_intercept_color)
            
            # Prepare next with specifically calculated slice
            scroll_mgr.prepare_next(self, slice(0, y_intercept_tgt_start))
            
            # Do the transformation with the parameterized indices
            try:
                if y_intercept_src_end is None:  # Handle case where it goes to the end
                    self.play(ReplacementTransform(
                        problem_text_equation[0][y_intercept_src_start:].copy(), 
                        step1_info_3[0][y_intercept_tgt_start:y_intercept_tgt_end]
                    ))
                else:
                    self.play(ReplacementTransform(
                        problem_text_equation[0][y_intercept_src_start:y_intercept_src_end].copy(), 
                        step1_info_3[0][y_intercept_tgt_start:y_intercept_tgt_end]
                    ))
            except Exception as e:
                print(f"Animation fallback due to: {e}")
                # If there's an error with indices, just indicate the text
                self.play(Indicate(step1_info_3))
                
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"At the y-intercept, x equals 0, <bookmark mark='plot'/> so we plot the point ({start_coords[0]}, {start_coords[1]})."):
            scroll_mgr.prepare_next(self)
            self.wait_until_bookmark("plot")
            self.play(Indicate(dot_start))
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 3: Now we'll use the slope to find a second point on the line."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"The slope {slope_spoken} can be expressed as a fraction: {slope_spoken} over {run_spoken}, which is the ratio of rise over run."):
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"Starting from our y-intercept at ({start_coords[0]}, {start_coords[1]}):"):
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"The rise is {rise_spoken} units {rise_direction.lower()}, because the slope is {slope_spoken}."):
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        direction_explanation = f"We go {run_direction.lower()} because the slope is {'negative' if slope < 0 else 'positive'}."
        
        with self.voiceover(f"The run is {run_spoken} unit {run_direction.lower()}. {direction_explanation}"):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover(f"Let's visualize this with arrows. Each arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"And this arrow shows our run of {run_spoken} unit to the {run_direction.lower()}."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.play(Write(run_text_group))
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(f"This gives us our second point <bookmark mark='second'/> at ({end_coords[0]}, {end_coords[1]})."):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
            self.wait_until_bookmark("second")
            self.play(Indicate(dot_end))
        self.wait(STANDARD_PAUSE)
        
        # Determine slant direction based on slope
        slant_direction = "left" if slope < 0 else "right"
        opposite_slant = "right" if slope < 0 else "left"
        
        with self.voiceover(f"When the given slope is {'negative' if slope < 0 else 'positive'}, our line will slant to the {slant_direction}. Conversely, a {'positive' if slope < 0 else 'negative'} slope will slant to the {opposite_slant}."):
            self.play(FadeIn(black_screen))

        with self.voiceover("Step 4: Finally, we'll draw a straight line through these two points."):
            self.play(FadeOut(black_screen))
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"We connect the points ({start_coords[0]}, {start_coords[1]}) and ({end_coords[0]}, {end_coords[1]})."):
            self.play(Write(connecting_line))
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"And extend the line in both directions <bookmark mark='extend'/> to complete our graph of {spoken_equation}."):
            scroll_mgr.prepare_next(self)
            self.play(
                ReplacementTransform(connecting_line, extended_line),
                FadeIn(start_tip),
                FadeIn(end_tip)
            )
            # Use a safe replacement animation that doesn't rely on specific indices
            self.play(ReplacementTransform(problem_text_equation.copy(), final_equation_group))
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"Notice how the {'negative' if slope < 0 else 'positive'} slope creates a line that {'falls' if slope < 0 else 'rises'} from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(extended_line, scale_factor=1.2))
        self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE)