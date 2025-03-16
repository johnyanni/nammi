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
        "slope": -4,             # The slope value
        "y_intercept": -3,       # The y-intercept value
        "formatted": "y=-4x-3",   # Formatted equation string
        "slope_indices": [2, 4],      # Position of "-4" in "y=-4x-3"
        "y_intercept_indices": [5, 7]  # Position of "-3" in "y=-4x-3"
    },
    "points": {
        "y_intercept_point": [0, -3],  # Coordinates of y-intercept point
        "second_point": [-1, 1]        # Coordinates of second point
    },
    "visual_ranges": {
        "axes_range": [-6, 6, 1],      # Range for axes: [min, max, step]
        "x_line_range": [-2, 1]        # X-range for plotting the line
    },
    "rise_run": {
        "rise_value": 4,               # Absolute value of rise
        "run_value": 1,                # Absolute value of run
        "rise_direction": "UP",        # Direction for rise: "UP" or "DOWN"
        "run_direction": "LEFT"        # Direction for run: "LEFT" or "RIGHT"
    },
    "tip": {
        "message": "When the slope (m) is negative we go up (rise) and then to the left (run)."
    },
    "colors": {
        "y_intercept_color": "YELLOW", 
        "slope_color": "BLUE",
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
        
        # Extract point coordinates
        start_coords = tuple(TEMPLATE_PARAMS["points"]["y_intercept_point"])
        end_coords = tuple(TEMPLATE_PARAMS["points"]["second_point"])
        
        # Extract rise/run values
        rise_value = TEMPLATE_PARAMS["rise_run"]["rise_value"]
        run_value = TEMPLATE_PARAMS["rise_run"]["run_value"]
        rise_direction = TEMPLATE_PARAMS["rise_run"]["rise_direction"]
        run_direction = TEMPLATE_PARAMS["rise_run"]["run_direction"]

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
        
        # Create run arrow based on parameters
        run_start_x = start_coords[0]
        run_start_y = end_coords[1]  # The y-coordinate of the end point
        
        if run_direction == "LEFT":
            run_arrows = Arrow(
                start=axes.c2p(run_start_x, run_start_y),
                end=axes.c2p(run_start_x - run_value, run_start_y),
                color=run_color,
                buff=0,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.4
            )
        else:  # RIGHT
            run_arrows = Arrow(
                start=axes.c2p(run_start_x, run_start_y),
                end=axes.c2p(run_start_x + run_value, run_start_y),
                color=run_color,
                buff=0,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.4
            )

        ###############################################################################
        # SECTION 6: TEXT LABELS AND OVERLAYS
        ###############################################################################
        # Create rise text label
        rise_text_group = self.create_text_with_background(
            f"\\text{{Rise}} = {rise_value}",
            text_color=rise_color
        ).scale(MATH_SCALE)
        rise_text_group.next_to(rise_arrows[1], LEFT, buff=0.5)
        
        # Create run text label
        run_text_group = self.create_text_with_background(
            f"\\text{{Run}} = {run_value}",
            text_color=run_color
        ).scale(MATH_SCALE)
        run_text_group.next_to(run_arrows, UP, buff=0.5)

        ###############################################################################
        # SECTION 7: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        # Problem statement split into two parts for better control
        problem_text_label = Tex("Graph:").scale(MATH_SCALE)
        problem_text_equation = MathTex(equation_str).scale(MATH_SCALE)
        problem_text_equation.next_to(problem_text_label, RIGHT)
        
        # Get absolute slope for text
        abs_slope = abs(slope)
        slope_sign = "negative " if slope < 0 else ""

        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_info_2_base = MathTex(f"\\text{{Slope }} (m) = ", color=slope_color).scale(MATH_SCALE)
        step1_info_3_base = MathTex(f"\\text{{Y-intercept }} (b) = ", color=y_intercept_color).scale(MATH_SCALE)
        
        # Step 2: Plot Y-intercept
        step2_title = Tex("Step 2: Plot Y-intercept").scale(TEXT_SCALE)
        step2_info = MathTex(f"\\text{{Plot point }} ({start_coords[0]}, {start_coords[1]})", color=y_intercept_color).scale(MATH_SCALE)

        # Step 3: Use Slope to Find Second Point
        step3_title = Tex("Step 3: Use Slope to Find Second Point").scale(TEXT_SCALE)
        
        # Format the slope fraction based on sign and value
        if slope < 0:
            slope_fraction = f"-\\frac{{{abs_slope}}}{{{run_value}}}"
        else:
            slope_fraction = f"\\frac{{{abs_slope}}}{{{run_value}}}"
            
        step3_info_1 = MathTex(f"\\text{{Slope }} = {slope} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}} = {slope_fraction}").scale(MATH_SCALE)
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
        SmartColorizeStatic(step3_info_1,
            {r"\text{rise}": rise_color, r"\text{run}": run_color, 
             f"{abs_slope}": rise_color, f"{run_value}": run_color}
        )

        ###############################################################################
        # SECTION 9: LAYOUT AND POSITIONING
        ###############################################################################
        # Organize step groups
        step1_group = self.create_step(step1_title, step1_info_1, step1_info_2_base, step1_info_3_base)
        step2_group = self.create_step(step2_title, step2_info)
        step3_group = self.create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5)
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
            step1_info_1, step1_info_2_base, step1_info_3_base,
            step2_title,
            step2_info,
            step3_title,
            step3_info_1, step3_info_2, step3_info_3, step3_info_4, step3_info_5,
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
        # SECTION 11: EQUATION ANALYSIS HELPERS
        ###############################################################################
        
        
        def find_slope_indices(equation_tex):
            """Find the indices of the slope coefficient in the MathTex object."""
            # Get the equation as a string
            eq_str = equation_str
            
            # Define patterns to look for based on common equation formats
            patterns = [
                # For equations like y = ax + b, capture just the number for positive values
                (r'y\s*=\s*\+?(\d+)x', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = -ax + b, capture the minus and the number for negative values
                (r'y\s*=\s*([-]\d+)x', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = b + ax, capture just the number for positive values
                (r'y\s*=\s*[-+]?\d+\s*\+\s*(\d+)x', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = b - ax, capture the minus and the number for negative values
                (r'y\s*=\s*[-+]?\d+\s*([-]\d+)x', lambda match: [match.start(1), match.end(1)])
            ]
            
            # Check each pattern
            import re
            for pattern, index_extractor in patterns:
                match = re.search(pattern, eq_str)
                if match:
                    indices = index_extractor(match)
                    if indices:
                        return indices
                        
            # Default indices if we can't determine them
            if slope < 0:
                # For negative slopes, include the minus sign
                if abs(slope) >= 10:
                    return [2, 5]  # For two-digit negative slopes like -10
                else:
                    return [2, 4]  # For single-digit negative slopes like -4
            else:
                # For positive slopes, don't include any plus sign
                if slope >= 10:
                    return [2, 4]  # For two-digit positive slopes like 10
                else:
                    return [2, 3]  # For single-digit positive slopes like 4



        def find_y_intercept_indices(equation_tex):
            """Find the indices of the y-intercept in the MathTex object."""
            # Get the equation as a string
            eq_str = equation_str
            
            # Define patterns to look for based on common equation formats
            patterns = [
                # For equations like y = ax + b, capture just the number for positive values
                (r'y\s*=\s*[-+]?\d+x\s*\+\s*(\d+)', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = ax - b, capture the minus and the number for negative values
                (r'y\s*=\s*[-+]?\d+x\s*([-]\d+)', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = b + ax, capture just the number for positive values
                (r'y\s*=\s*(\d+)\s*\+\s*[-+]?\d+x', lambda match: [match.start(1), match.end(1)]),
                
                # For equations like y = -b + ax, capture the minus and the number for negative values
                (r'y\s*=\s*([-]\d+)\s*[-+]\s*[-+]?\d+x', lambda match: [match.start(1), match.end(1)])
            ]
            
            # Check each pattern
            import re
            for pattern, index_extractor in patterns:
                match = re.search(pattern, eq_str)
                if match:
                    indices = index_extractor(match)
                    if indices:
                        return indices
                        
            # Default indices if we can't determine them
            if y_intercept < 0:
                # For negative y-intercepts, include the minus sign
                if abs(y_intercept) >= 10:
                    return [-3, None]  # For two-digit negative y-intercepts
                else:
                    return [-2, None]  # For single-digit negative y-intercepts
            else:
                # For positive y-intercepts, don't include any plus sign
                if y_intercept >= 10:
                    return [-2, None]  # For two-digit positive y-intercepts
                else:
                    return [-1, None]  # For single-digit positive y-intercepts

        ###############################################################################
        # SECTION 12: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover(f"Let's graph the linear equation {equation_str}."):
            self.play(Write(axes), Write(axes_labels))
            scroll_mgr.prepare_next(self)
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: We'll identify the key components of the equation."):
            scroll_mgr.prepare_next(self)

        with self.voiceover("This equation is in slope-intercept form: y equals mx plus b."):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        # Later in your animation sequence
        with self.voiceover(f"The coefficient of x is the slope. Here, m equals {slope_sign}{abs_slope}."):
            self.highlight_formula_component(step1_info_1, "m", slope_color)
            
            # Add step1_info_2_base to the scroll manager first
            scroll_mgr.prepare_next(self)
            
            # Get slope indices for the animation
            slope_indices = find_slope_indices(problem_text_equation)
            
            try:
                # If the indices exist, do the transformation animation
                if slope_indices and isinstance(slope_indices, list) and len(slope_indices) >= 2:
                    # Create a copy of the slope value from the equation
                    if slope_indices[1] is None:  # Handle the case where end index is None
                        slope_value = problem_text_equation[0][slope_indices[0]:].copy()
                    else:
                        slope_value = problem_text_equation[0][slope_indices[0]:slope_indices[1]].copy()
                    
                    slope_value.set_color(slope_color)
                    # Position it at the end of step1_info_2_base
                    slope_value.next_to(step1_info_2_base, RIGHT)
                    slope_value.align_to(step1_info_2_base, UP)  # Align along the top
                    slope_value.align_to(step1_info_2_base, DOWN)  # Then align along the bottom
                    
                    # Animate the transformation after the scroll manager has prepared step1_info_2_base
                    self.play(
                        ReplacementTransform(
                            problem_text_equation[0][slope_indices[0]:slope_indices[1]].copy(),
                            slope_value
                        )
                    )
                    
                    # Create the complete step1_info_2 for future reference
                    step1_info_2 = VGroup(step1_info_2_base, slope_value)
                else:
                    # Fallback: just indicate the base element
                    self.play(Indicate(step1_info_2_base))
                    step1_info_2 = step1_info_2_base
            except Exception as e:
                # If there's any error, just indicate the base element
                print(f"Animation fallback due to: {e}")
                self.play(Indicate(step1_info_2_base))
                step1_info_2 = step1_info_2_base
                
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"The constant term is the y-intercept. Here, b equals {y_intercept}."):
            self.highlight_formula_component(step1_info_1, "b", y_intercept_color)
            
            # Add step1_info_3_base to the scroll manager first
            scroll_mgr.prepare_next(self)
            
            # Get y-intercept indices for the animation
            y_intercept_indices = find_y_intercept_indices(problem_text_equation)
            
            try:
                # If the indices exist, do the transformation animation
                if y_intercept_indices and isinstance(y_intercept_indices, list) and len(y_intercept_indices) >= 1:
                    # Create a copy of the y-intercept value from the equation
                    if y_intercept_indices[1] is None:  # Handle the case where end index is None
                        y_intercept_value = problem_text_equation[0][y_intercept_indices[0]:].copy()
                    else:
                        y_intercept_value = problem_text_equation[0][y_intercept_indices[0]:y_intercept_indices[1]].copy()
                    
                    y_intercept_value.set_color(y_intercept_color)
                    # Position it at the end of step1_info_3_base
                    y_intercept_value.next_to(step1_info_3_base, RIGHT)
                    
                    # Animate the transformation
                    self.play(
                        ReplacementTransform(
                            problem_text_equation[0][y_intercept_indices[0]:y_intercept_indices[1] if y_intercept_indices[1] is not None else None].copy(),
                            y_intercept_value
                        )
                    )
                    
                    # Create the complete step1_info_3 for future reference
                    step1_info_3 = VGroup(step1_info_3_base, y_intercept_value)
                else:
                    # Fallback: just indicate the base element
                    self.play(Indicate(step1_info_3_base))
                    step1_info_3 = step1_info_3_base
            except Exception as e:
                # If there's any error, just indicate the base element
                print(f"Animation fallback due to: {e}")
                self.play(Indicate(step1_info_3_base))
                step1_info_3 = step1_info_3_base
                
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
            scroll_mgr.scroll_down(self, steps=1)
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"The slope {slope_sign}{abs_slope} can be expressed as a fraction: <bookmark mark='fraction'/> {slope_sign}{abs_slope} over {run_value}, which is the ratio of rise over run."):
            self.wait_until_bookmark("fraction")
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"Starting from our y-intercept at ({start_coords[0]}, {start_coords[1]}):"):
            scroll_mgr.prepare_next(self)
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"The rise is {rise_value} units {rise_direction.lower()}, because the slope is {slope_sign}{abs_slope}."):
            scroll_mgr.prepare_next(self)
        self.wait(COMPREHENSION_PAUSE)

        direction_explanation = f"We go {run_direction.lower()} because the slope is {'negative' if slope < 0 else 'positive'}."
        
        with self.voiceover(f"The run is {run_value} unit {run_direction.lower()}. <bookmark mark='run'/> {direction_explanation}"):
            scroll_mgr.prepare_next(self)
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover(f"Let's visualize this with arrows. Each arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"And this arrow shows our run of {run_value} unit to the {run_direction.lower()}."):
            self.play(GrowArrow(run_arrows))
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
        
        with self.voiceover(f"When the given slope is {slope_sign}{'positive' if slope > 0 else 'negative'}, our line will slant to the {slant_direction}. Conversely, a {'positive' if slope < 0 else 'negative'} slope will slant to the {opposite_slant}."):
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

        with self.voiceover(f"And extend the line in both directions <bookmark mark='extend'/> to complete our graph of {equation_str}."):
            scroll_mgr.prepare_next(self)
            self.play(
                ReplacementTransform(connecting_line, extended_line),
                FadeIn(start_tip),
                FadeIn(end_tip)
            )
            # Use a safe replacement animation that doesn't rely on specific indices
            self.play(ReplacementTransform(problem_text_equation.copy(), final_equation_group))
        self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(f"Notice how the {slope_sign}slope creates a line that {'falls' if slope < 0 else 'rises'} from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(extended_line, scale_factor=1.2))
        self.wait(COMPREHENSION_PAUSE)

        self.wait(STANDARD_PAUSE)