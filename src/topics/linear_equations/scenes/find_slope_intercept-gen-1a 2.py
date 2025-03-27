"""Tutorial on finding the equation of a line in slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

# TEMPLATE PARAMETERS - Structured for finding the equation of a line
# ------------------------------------------------
TEMPLATE_PARAMS = {
    # Line details and final equation
    "line": {
        "slope": 2/3,                      # The slope value as a fraction or number
        "y_intercept": 1,                  # The y-intercept value as a number
        "final_equation": "y=\\frac{2}{3}x+1", # The final equation with LaTeX
    },
    
    # Points used to determine the line
    "points": {
        "point1": [0, 1],                  # First point coordinates [x, y]
        "point2": [3, 3],                  # Second point coordinates [x, y]
        "use_y_intercept": True,           # Whether point1 is the y-intercept
    },
    
    # Display and spoken representations
    "display": {
        "slope_display": "\\frac{2}{3}",   # How the slope appears in LaTeX
        "slope_spoken": "two thirds",      # How the slope should be spoken in voiceover
        "y_intercept_display": "1",        # How the y-intercept appears in LaTeX
        "y_intercept_spoken": "one",       # How the y-intercept should be spoken
        "final_equation_spoken": "y equals two thirds x plus one"  # Spoken version of final equation
    },
    
    # Rise and run values for slope calculation
    "rise_run": {
        "rise_value": 2,                   # Rise value (numerator of slope)
        "rise_spoken": "two",              # Spoken version of rise value
        "run_value": 3,                    # Run value (denominator of slope)
        "run_spoken": "three",             # Spoken version of run value
        "rise_direction": "UP",            # Direction for rise: "UP" or "DOWN"
        "run_direction": "RIGHT"           # Direction for run: "LEFT" or "RIGHT"
    },
    
    # Coordinate plane settings
    "geometry": {
        "axes_range": [-5, 5, 1],          # Range for axes: [min, max, step]
        "x_line_range": [-4, 4],           # X-range for drawing the line
    },
    
    # UI elements and styling
    "ui": {
        "tip_message": "When finding the slope, use the formula: slope = rise ÷ run",
        "point_color": "BLUE",            # Color for the points
        "slope_color": "GREEN",           # Color for slope elements
        "rise_color": "BLUE",             # Color for rise arrows
        "run_color": "RED",               # Color for run arrows
        "y_intercept_color": "YELLOW",    # Color for y-intercept elements
        "line_color": "WHITE"             # Color for the line
    },
    
    # Custom voiceover text (optional - will use defaults if not provided)
    "voiceover": {
        "intro": "Let's find the equation of the given line in slope-intercept form.",
        "step1": "Step 1: We need to find two points on the line to determine its equation.",
        "step2": "Step 2: We'll calculate the slope using these two points.",
        "step3": "Step 3: We'll identify the y-intercept.",
        "step4": "Step 4: Now we can write the equation in slope-intercept form: y = mx + b."
    }
}

class FindingLineEquation(MathTutorialScene):
    """A tutorial that teaches how to find the equation of a line in slope-intercept form."""

    def construct(self):
        ###############################################################################
        # SECTION 1: PARAMETER EXTRACTION AND PREPROCESSING
        ###############################################################################
        # Extract colors from parameters
        point_color = eval(TEMPLATE_PARAMS["ui"]["point_color"])
        slope_color = eval(TEMPLATE_PARAMS["ui"]["slope_color"])
        rise_color = eval(TEMPLATE_PARAMS["ui"]["rise_color"])
        run_color = eval(TEMPLATE_PARAMS["ui"]["run_color"])
        y_intercept_color = eval(TEMPLATE_PARAMS["ui"]["y_intercept_color"])
        line_color = eval(TEMPLATE_PARAMS["ui"]["line_color"])

        # Extract line parameters
        slope = TEMPLATE_PARAMS["line"]["slope"]
        y_intercept = TEMPLATE_PARAMS["line"]["y_intercept"]
        final_equation = TEMPLATE_PARAMS["line"]["final_equation"]
        
        # Extract points
        point1 = TEMPLATE_PARAMS["points"]["point1"]
        point2 = TEMPLATE_PARAMS["points"]["point2"]
        use_y_intercept = TEMPLATE_PARAMS["points"]["use_y_intercept"]
        
        # Extract display and spoken representations
        slope_display = TEMPLATE_PARAMS["display"]["slope_display"]
        slope_spoken = TEMPLATE_PARAMS["display"]["slope_spoken"]
        y_intercept_display = TEMPLATE_PARAMS["display"]["y_intercept_display"]
        y_intercept_spoken = TEMPLATE_PARAMS["display"]["y_intercept_spoken"]
        final_equation_spoken = TEMPLATE_PARAMS["display"]["final_equation_spoken"]
        
        # Extract coordinate points and visual ranges
        axes_range = TEMPLATE_PARAMS["geometry"]["axes_range"]
        x_line_range = TEMPLATE_PARAMS["geometry"]["x_line_range"]
        
        # Extract rise/run values
        rise_value = TEMPLATE_PARAMS["rise_run"]["rise_value"]
        rise_spoken = TEMPLATE_PARAMS["rise_run"]["rise_spoken"]
        run_value = TEMPLATE_PARAMS["rise_run"]["run_value"]
        run_spoken = TEMPLATE_PARAMS["rise_run"]["run_spoken"]
        rise_direction = TEMPLATE_PARAMS["rise_run"]["rise_direction"]
        run_direction = TEMPLATE_PARAMS["rise_run"]["run_direction"]

        # Extract voiceovers (with defaults)
        intro_voiceover = TEMPLATE_PARAMS["voiceover"].get("intro", 
            "Let's find the equation of the given line in slope-intercept form.")
        step1_voiceover = TEMPLATE_PARAMS["voiceover"].get("step1", 
            "Step 1: We need to find two points on the line to determine its equation.")
        step2_voiceover = TEMPLATE_PARAMS["voiceover"].get("step2", 
            "Step 2: We'll calculate the slope using these two points.")
        step3_voiceover = TEMPLATE_PARAMS["voiceover"].get("step3", 
            "Step 3: We'll identify the y-intercept.")
        step4_voiceover = TEMPLATE_PARAMS["voiceover"].get("step4", 
            "Step 4: Now we can write the equation in slope-intercept form: y = mx + b.")

        # Process fraction-related variables early
        def is_fraction_format(tex_string):
            """Check if a string is formatted as a LaTeX fraction."""
            return "\\frac{" in tex_string and "}{" in tex_string and "}" in tex_string

        # Determine if slope_display is already a fraction
        is_slope_fraction = is_fraction_format(slope_display)

        ###############################################################################
        # SECTION 2: COORDINATE PLANE AND LINE SETUP
        ###############################################################################
        # Create axes
        axes, axes_labels = self.create_axes(x_range=axes_range)

        # Create visual elements - the line and points
        dot1 = Dot(axes.c2p(*point1), color=point_color if not use_y_intercept else y_intercept_color, radius=0.15)
        dot2 = Dot(axes.c2p(*point2), color=point_color, radius=0.15)
        
        def line_function(x):
            return slope*x + y_intercept
        
        # Draw the line
        line = axes.plot(
            line_function, 
            x_range=x_line_range,
            color=line_color
        )
        
        # Point labels
        p1_label = MathTex(f"({point1[0]}, {point1[1]})", color=point_color if not use_y_intercept else y_intercept_color)
        p2_label = MathTex(f"({point2[0]}, {point2[1]})", color=point_color)
        
        # Position labels next to the points
        p1_label.next_to(dot1, DOWN + RIGHT, buff=0.2)
        p2_label.next_to(dot2, UP + RIGHT, buff=0.2)

        ###############################################################################
        # SECTION 3: RISE AND RUN ARROWS
        ###############################################################################
        # Determine the starting points for rise and run
        start_x = point1[0]
        start_y = point1[1]
        end_x = point2[0]
        end_y = point2[1]
        
        # Create rise arrows
        rise_arrows = []
        
        # Create rise arrows based on direction
        if rise_direction == "UP":
            for i in range(rise_value):
                arrow = Arrow(
                    start=axes.c2p(start_x, start_y + i),
                    end=axes.c2p(start_x, start_y + i + 1),
                    color=rise_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        else:  # DOWN
            for i in range(rise_value):
                arrow = Arrow(
                    start=axes.c2p(start_x, start_y - i),
                    end=axes.c2p(start_x, start_y - i - 1),
                    color=rise_color,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        
        # Group rise arrows
        rise_arrows_group = VGroup(*rise_arrows)
        
        # Create run arrows
        run_arrows = []
        run_start_x = start_x
        run_start_y = end_y  # The y-coordinate after the rise
        
        # Create run arrows based on direction
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
        
        # Group run arrows
        run_arrows_group = VGroup(*run_arrows)
        
        # Create rise and run labels
        rise_unit_text = "units" if rise_value > 1 else "unit"
        run_unit_text = "units" if run_value > 1 else "unit"
        
        rise_text = self.create_text_with_background(
            f"\\text{{Rise}} = {rise_value} {rise_direction.lower()}",
            text_color=rise_color
        ).scale(MATH_SCALE)
        
        run_text = self.create_text_with_background(
            f"\\text{{Run}} = {run_value} {run_direction.lower()}",
            text_color=run_color
        ).scale(MATH_SCALE)
        
        # Position rise and run text
        if len(rise_arrows) > 1:
            rise_text.next_to(rise_arrows_group, LEFT, buff=0.5)
        else:
            rise_text.next_to(rise_arrows[0], LEFT, buff=0.5)
            
        run_text.next_to(run_arrows_group, UP, buff=0.5)

        ###############################################################################
        # SECTION 4: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        problem_text = Tex("Find the equation of the given line in slope-intercept form.").scale(MATH_SCALE)

        # Step 1: Identify Points on the Line
        step1_title = Tex("Step 1: Identify Points on the Line").scale(TEXT_SCALE)
        step1_info_1 = Tex("We need two points on the line to find its equation").scale(MATH_SCALE)
        
        if use_y_intercept:
            step1_info_2 = MathTex(f"\\text{{Point 1: y-intercept }} ({point1[0]}, {point1[1]})", color=y_intercept_color).scale(MATH_SCALE)
        else:
            step1_info_2 = MathTex(f"\\text{{Point 1: }} ({point1[0]}, {point1[1]})", color=point_color).scale(MATH_SCALE)
            
        step1_info_3 = MathTex(f"\\text{{Point 2: }} ({point2[0]}, {point2[1]})", color=point_color).scale(MATH_SCALE)

        # Step 2: Calculate the Slope
        step2_title = Tex("Step 2: Calculate the Slope").scale(TEXT_SCALE)
        step2_info_1 = MathTex(r"\text{Slope } = \frac{\text{rise}}{\text{run}} = \frac{\text{change in }y}{\text{change in }x} = \frac{y_2 - y_1}{x_2 - x_1}").scale(MATH_SCALE)
        
        # Calculate the slope from the points
        slope_calc_text = f"\\text{{Slope }} = \\frac{{{point2[1]} - {point1[1]}}}{{{point2[0]} - {point1[0]}}}"
        
        # Add the calculation step if the slope is a fraction
        if is_slope_fraction:
            slope_calc_text += f" = {slope_display}"
        
        step2_info_2 = MathTex(slope_calc_text, color=slope_color).scale(MATH_SCALE)
        
        # Step 3: Find the Y-Intercept
        step3_title = Tex("Step 3: Find the Y-Intercept").scale(TEXT_SCALE)
        
        if use_y_intercept:
            # If point1 is on y-axis, we already have the y-intercept
            step3_info_1 = Tex(f"Since one of our points is on the y-axis, we can directly read the y-intercept").scale(MATH_SCALE)
            step3_info_2 = MathTex(f"\\text{{Y-intercept }} = {y_intercept_display}", color=y_intercept_color).scale(MATH_SCALE)
        else:
            # Otherwise, calculate y-intercept using point-slope formula
            step3_info_1 = Tex(f"To find the y-intercept, we substitute the slope and one point into the equation").scale(MATH_SCALE)
            y_int_calc = f"y - {point1[1]} = {slope_display}(x - {point1[0]})"
            step3_info_2 = MathTex(y_int_calc).scale(MATH_SCALE)
            
            # When x = 0, solve for y-intercept
            if point1[0] != 0:  # If point is not on y-axis
                y_int_solve = f"\\text{{When }} x = 0: y - {point1[1]} = {slope_display}(0 - {point1[0]})"
                step3_info_3 = MathTex(y_int_solve).scale(MATH_SCALE)
                
                # Final y-intercept calculation
                step3_info_4 = MathTex(f"\\text{{Y-intercept }} = {y_intercept_display}", color=y_intercept_color).scale(MATH_SCALE)
            else:
                # Just use the y-value directly if point is on y-axis
                step3_info_3 = MathTex(f"\\text{{Y-intercept }} = {y_intercept_display}", color=y_intercept_color).scale(MATH_SCALE)
                step3_info_4 = None
        
        # Step 4: Write the Final Equation
        step4_title = Tex("Step 4: Write the Equation in Slope-Intercept Form").scale(TEXT_SCALE)
        step4_info_1 = MathTex(r"y = mx + b").scale(MATH_SCALE)
        
        if y_intercept >= 0:
            sign = "+"
        else:
            sign = ""  # Negative sign is already included in y_intercept_display
            
        step4_info_2 = MathTex(f"y = {slope_display}x {sign} {y_intercept_display}").scale(MATH_SCALE)
        
        ###############################################################################
        # SECTION 5: EQUATION DISPLAY AND STYLING
        ###############################################################################
        
        # Color the variables in the slope formula
        SmartColorizeStatic(
            step2_info_1,
            {
                r"\text{rise}": rise_color, 
                r"\text{run}": run_color,
                r"\text{change in }y": rise_color,
                r"\text{change in }x": run_color,
                "y_2 - y_1": rise_color,
                "x_2 - x_1": run_color
            }
        )
        
        # Color the slope calculation
        change_y = f"{point2[1]} - {point1[1]}"
        change_x = f"{point2[0]} - {point1[0]}"
        
        SmartColorizeStatic(
            step2_info_2,
            {
                f"\\frac{{{change_y}}}{{{change_x}}}": slope_color,
                f"{slope_display}": slope_color
            }
        )
        
        # Color the m and b in the slope-intercept formula
        self.color_component(step4_info_1, "m", slope_color)
        self.color_component(step4_info_1, "b", y_intercept_color)
        
        # Color parts of the final equation
        SmartColorizeStatic(
            step4_info_2,
            {
                f"{slope_display}": slope_color,
                f"{y_intercept_display}": y_intercept_color
            }
        )
        
        ###############################################################################
        # SECTION 6: LAYOUT AND ORGANIZATION
        ###############################################################################
        # Create step groups
        step1_group = self.create_step(step1_title, step1_info_1, step1_info_2, step1_info_3)
        
        step2_group = self.create_step(step2_title, step2_info_1, step2_info_2)
        
        if use_y_intercept:
            step3_group = self.create_step(step3_title, step3_info_1, step3_info_2)
        else:
            if step3_info_4:
                step3_group = self.create_step(step3_title, step3_info_1, step3_info_2, step3_info_3, step3_info_4)
            else:
                step3_group = self.create_step(step3_title, step3_info_1, step3_info_2, step3_info_3)
                
        step4_group = self.create_step(step4_title, step4_info_1, step4_info_2)
        
        # Create the complete steps group
        steps_group = VGroup(
            problem_text,
            step1_group,
            step2_group,
            step3_group,
            step4_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Position the entire content
        steps_group.to_edge(LEFT, buff=0.6).to_edge(UP, buff=0.6)
        
        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title).set_color(GREY)
        
        ###############################################################################
        # SECTION 7: SCROLL MANAGER AND TIPS SETUP
        ###############################################################################
        
        # Flatten all steps for the scroll manager
        solution_steps = VGroup(
            problem_text,
            step1_title, step1_info_1, step1_info_2, step1_info_3,
            step2_title, step2_info_1, step2_info_2,
        )
        
        # Add step 3 components based on whether we're using y-intercept or not
        if use_y_intercept:
            solution_steps.add(step3_title, step3_info_1, step3_info_2)
        else:
            solution_steps.add(step3_title, step3_info_1, step3_info_2, step3_info_3)
            if step3_info_4:
                solution_steps.add(step3_info_4)
                
        # Add step 4 components
        solution_steps.add(step4_title, step4_info_1, step4_info_2)
        
        # Set up scroll manager
        scroll_mgr = ScrollManager(solution_steps)
        
        # Create quick tip
        tip_1 = QuickTip(
            TEMPLATE_PARAMS["ui"]["tip_message"],
            fill_opacity=1
        ).shift(DOWN * 2)
        
        # Create a formula highlight box
        final_eq_box = SurroundingRectangle(step4_info_2, color=YELLOW, buff=0.2)
        
        ###############################################################################
        # SECTION 8: ANIMATION SEQUENCE
        ###############################################################################
        # Initial setup
        with self.voiceover(intro_voiceover):
            self.play(
                Write(axes),
                Write(axes_labels),
                Create(line)
            )
            self.play(
                FadeIn(dot1),
                FadeIn(dot2),
                Write(p1_label),
                Write(p2_label)
            )
            scroll_mgr.prepare_next(self)  # Problem statement
        self.wait(STANDARD_PAUSE)
        
        # Step 1: Identify Points
        with self.voiceover(step1_voiceover):
            scroll_mgr.prepare_next(self)  # step1_title
            scroll_mgr.prepare_next(self)  # step1_info_1
            self.play(
                Indicate(dot1),
                Indicate(p1_label)
            )
            scroll_mgr.prepare_next(self)  # step1_info_2
            self.play(
                Indicate(dot2),
                Indicate(p2_label)
            )
            scroll_mgr.prepare_next(self)  # step1_info_3
        self.wait(STANDARD_PAUSE)
        
        # Step 2: Calculate Slope
        with self.voiceover(step2_voiceover):
            scroll_mgr.prepare_next(self)  # step2_title
            scroll_mgr.prepare_next(self)  # step2_info_1
            
            # Show rise arrows
            rise_unit_spoken = "units" if rise_value > 1 else "unit"
            with self.voiceover(f"Let's calculate the rise. From point 1 to point 2, we move {rise_spoken} {rise_unit_spoken} {rise_direction.lower()}."):
                for arrow in rise_arrows:
                    self.play(GrowArrow(arrow), run_time=0.5)
                self.play(Write(rise_text))
            
            # Show run arrows
            run_unit_spoken = "units" if run_value > 1 else "unit"
            with self.voiceover(f"And for the run, we move {run_spoken} {run_unit_spoken} {run_direction.lower()}."):
                for arrow in run_arrows:
                    self.play(GrowArrow(arrow), run_time=0.5)
                self.play(Write(run_text))
                self.play(FadeIn(tip_1, shift=UP))
            
            self.play(FadeOut(tip_1, shift=DOWN))
            scroll_mgr.prepare_next(self)  # step2_info_2
            
            with self.voiceover(f"So the slope is {slope_spoken}."):
                self.play(Indicate(step2_info_2, color=slope_color))
        self.wait(STANDARD_PAUSE)
        
        # Step 3: Find Y-Intercept
        with self.voiceover(step3_voiceover):
            scroll_mgr.scroll_down(self, steps=1)
            scroll_mgr.prepare_next(self)  # step3_title
            scroll_mgr.prepare_next(self)  # step3_info_1
            
            if use_y_intercept:
                with self.voiceover(f"Since our first point is on the y-axis at (0, {point1[1]}), we can directly read the y-intercept as {y_intercept_spoken}."):
                    scroll_mgr.prepare_next(self)  # step3_info_2
                    self.play(Indicate(dot1, color=y_intercept_color))
            else:
                with self.voiceover("We'll use the point-slope form to find the y-intercept."):
                    scroll_mgr.prepare_next(self)  # step3_info_2
                    
                y_int_voiceover = f"When x equals zero, we can solve for y to find the y-intercept."
                with self.voiceover(y_int_voiceover):
                    scroll_mgr.prepare_next(self)  # step3_info_3
                    
                if step3_info_4:
                    with self.voiceover(f"Simplifying, we get y-intercept equals {y_intercept_spoken}."):
                        scroll_mgr.prepare_next(self)  # step3_info_4
        self.wait(STANDARD_PAUSE)
        
        # Step 4: Write final equation
        final_eq_voiceover = f"Step 4: Now we can write the equation in slope-intercept form: y equals mx plus b."
        with self.voiceover(final_eq_voiceover):
            scroll_mgr.scroll_down(self, steps=2)
            scroll_mgr.prepare_next(self)  # step4_title
            scroll_mgr.prepare_next(self)  # step4_info_1
        
        with self.voiceover(f"Substituting our slope {slope_spoken} and y-intercept {y_intercept_spoken}, we get {final_equation_spoken}."):
            scroll_mgr.prepare_next(self)  # step4_info_2
            self.play(Create(final_eq_box))
        
        self.wait(END_PAUSE)