"""Tutorial on graphing linear equations using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.common.math_indices import MathIndices
from src.components.styles.constants import *
from fractions import Fraction

# TEMPLATE PARAMETERS - Restructured for clarity and better organization
# ------------------------------------------------
TEMPLATE_PARAMS = {
    # Core equation values
    "equation": {
        "slope": -4,                      # The slope value as a number
        "y_intercept": -3,                # The y-intercept value as a number
        "formatted": "y=-4x-3",           # Formatted equation with LaTeX
    },
    
    # Display and spoken representations
    "display": {
        "slope_display": "-4",            # How the slope appears in LaTeX
        "slope_spoken": "negative four",  # How the slope should be spoken in voiceover
        "y_intercept_display": "-3",      # How the y-intercept appears in LaTeX
        "y_intercept_spoken": "negative three",  # How the y-intercept should be spoken
        "spoken_equation": "y equals negative four x minus three",  # Spoken version for voiceover
    },
    
    # Animation indices for transformations
    "indices": {
        "slope_src_indices": [2, 4],          # Source indices in problem_text_equation for slope
        "slope_tgt_indices": [-2, None],  
        "y_intercept_src_indices": [-2, None], # Target indices in step1_info_2 for slope value
        "y_intercept_tgt_indices": [-2, None], # Target indices in step1_info_3 for y-intercept value
        "coord_src_indices": [-6, None],
        "coord_tgt_indices": [-6, None]
    },
    
    # Coordinate points and visual ranges
    "geometry": {
        "y_intercept_point": [0, -3],     # Coordinates of y-intercept point
        "second_point": [-1, 1],          # Coordinates of second point
        "axes_range": [-6, 6, 1],         # Range for axes: [min, max, step]
        "x_line_range": [-2, 1]           # X-range for plotting the line
    },
    
    # Rise and run values for slope visualization
    "rise_run": {
        "rise_value": 4,                  # Absolute value of rise
        "rise_spoken": "four",            # Spoken version of rise value
        "run_value": 1,                   # Absolute value of run
        "run_spoken": "one",              # Spoken version of run value
        "rise_direction": "UP",           # Direction for rise: "UP" or "DOWN"
        "run_direction": "LEFT"           # Direction for run: "LEFT" or "RIGHT"
    },
    
    # UI elements and styling
    "ui": {
        "tip_message": "When the slope (m) is negative we go up (rise) and then to the left (run).",
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
        # SECTION 1: PARAMETER EXTRACTION AND PREPROCESSING
        ###############################################################################
        # Extract colors from parameters
        y_intercept_color = eval(TEMPLATE_PARAMS["ui"]["y_intercept_color"])
        slope_color = eval(TEMPLATE_PARAMS["ui"]["slope_color"])
        rise_color = eval(TEMPLATE_PARAMS["ui"]["rise_color"])
        run_color = eval(TEMPLATE_PARAMS["ui"]["run_color"])
        line_color = eval(TEMPLATE_PARAMS["ui"]["line_color"])

        # Extract equation parameters
        slope = TEMPLATE_PARAMS["equation"]["slope"]
        y_intercept = TEMPLATE_PARAMS["equation"]["y_intercept"]
        equation_str = TEMPLATE_PARAMS["equation"]["formatted"]
        
        # Extract display and spoken representations
        slope_display = TEMPLATE_PARAMS["display"]["slope_display"]
        y_intercept_display = TEMPLATE_PARAMS["display"]["y_intercept_display"]
        spoken_equation = TEMPLATE_PARAMS["display"]["spoken_equation"]
        slope_spoken = TEMPLATE_PARAMS["display"]["slope_spoken"]
        y_intercept_spoken = TEMPLATE_PARAMS["display"]["y_intercept_spoken"]
        
        # Extract coordinate points and visual ranges
        start_coords = tuple(TEMPLATE_PARAMS["geometry"]["y_intercept_point"])
        end_coords = tuple(TEMPLATE_PARAMS["geometry"]["second_point"])
        axes_range = TEMPLATE_PARAMS["geometry"]["axes_range"]
        x_line_range = TEMPLATE_PARAMS["geometry"]["x_line_range"]
        
        # Extract rise/run values
        rise_value = TEMPLATE_PARAMS["rise_run"]["rise_value"]
        rise_spoken = TEMPLATE_PARAMS["rise_run"]["rise_spoken"]
        run_value = TEMPLATE_PARAMS["rise_run"]["run_value"]
        run_spoken = TEMPLATE_PARAMS["rise_run"]["run_spoken"]
        rise_direction = TEMPLATE_PARAMS["rise_run"]["rise_direction"]
        run_direction = TEMPLATE_PARAMS["rise_run"]["run_direction"]

        # Extract animation indices
        slope_src_start, slope_src_end = TEMPLATE_PARAMS["indices"]["slope_src_indices"]
        slope_tgt_start, slope_tgt_end = TEMPLATE_PARAMS["indices"]["slope_tgt_indices"]
        y_intercept_src_start, y_intercept_src_end = TEMPLATE_PARAMS["indices"]["y_intercept_src_indices"]
        y_intercept_tgt_start, y_intercept_tgt_end = TEMPLATE_PARAMS["indices"]["y_intercept_tgt_indices"]
        coord_src_start, coord_src_end = TEMPLATE_PARAMS["indices"]["coord_src_indices"]
        coord_tgt_start, coord_tgt_end = TEMPLATE_PARAMS["indices"]["coord_tgt_indices"]

        # Process fraction-related variables early
        def is_fraction_format(tex_string):
            """Check if a string is formatted as a LaTeX fraction."""
            return "\\frac{" in tex_string and "}{" in tex_string and "}" in tex_string

        # Determine if slope_display is already a fraction and prepare variables
        is_slope_fraction = is_fraction_format(slope_display)
        
        # For non-fraction slopes, prepare the converted fraction representation
        converted_slope_display = None
        if not is_slope_fraction:
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

        ###############################################################################
        # SECTION 2: COORDINATE PLANE SETUP
        ###############################################################################
        # Create axes
        axes, axes_labels = self.create_axes(x_range=axes_range)

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
        extended_line = axes.plot(
            line_function, 
            x_range=x_line_range,
            color=line_color
        )

        # Add tips to the extended line
        start_point = axes.c2p(x_line_range[0], line_function(x_line_range[0]))
        end_point = axes.c2p(x_line_range[1], line_function(x_line_range[1]))

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
        
        # Group rise arrows for consistent referencing
        rise_arrows_group = VGroup(*rise_arrows)
        
        # Create run arrows
        run_arrows = []
        run_start_x = start_coords[0]
        run_start_y = end_coords[1]  # The y-coordinate after the rise
        
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

        # Group run arrows for consistent referencing and text positioning
        run_arrows_group = VGroup(*run_arrows)

        ###############################################################################
        # SECTION 6: TEXT LABELS AND OVERLAYS
        ###############################################################################
        # Create rise text label
        rise_text_group = self.create_text_with_background(
            f"\\text{{Rise}} = {rise_value}",
            text_color=rise_color
        ).scale(MATH_SCALE)
        
        # Better positioning for rise text - centered if multiple arrows
        if len(rise_arrows) > 1:
            rise_text_group.next_to(rise_arrows_group, LEFT, buff=0.5)
        else:
            rise_text_group.next_to(rise_arrows[0], LEFT, buff=0.5)
        
        # Create run text label
        run_text_group = self.create_text_with_background(
            f"\\text{{Run}} = {run_value}",
            text_color=run_color
        ).scale(MATH_SCALE)
        
        # Better positioning for run text - centered if multiple arrows
        run_text_group.next_to(run_arrows_group, UP, buff=0.5)

        ###############################################################################
        # SECTION 7: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        # Create the problem text with explicit parts for better control
        problem_text_label = Tex("Graph:").scale(MATH_SCALE)
        problem_text_equation = MathTex(equation_str).scale(MATH_SCALE)
        problem_text_group = VGroup(problem_text_label, problem_text_equation).arrange(buff=0.2)
        
        # Get absolute slope for text
        abs_slope = abs(slope)
        slope_sign = "negative " if slope < 0 else ""

        # Step 1: Identify Components
        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_p1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_p2 = MathTex(f"\\text{{Slope }} (m) = {slope_display}", color=slope_color).scale(MATH_SCALE)
        step1_p3 = MathTex(f"\\text{{Y-intercept }} (b) = {y_intercept_display}", color=y_intercept_color).scale(MATH_SCALE)
        
        # Step 2: Plot Y-intercept
        step2_title = Tex("Step 2: Plot Y-intercept").scale(TEXT_SCALE)
        step2_p1 = MathTex(f"\\text{{Plot point }} ({start_coords[0]}, {start_coords[1]})", color=y_intercept_color).scale(MATH_SCALE)

        # Step 3: Use Slope to Find Second Point
        step3_title = Tex("Step 3: Use Slope to Find Second Point").scale(TEXT_SCALE)
        
        # Create the appropriate step3_p1 based on slope representation
        if is_slope_fraction:
            # If slope_display is already a fraction, use it directly
            step3_p1 = MathTex(f"\\text{{Slope }} = {slope_display} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)
        else:
            # If slope_display is not a fraction, include the converted fraction representation
            step3_p1 = MathTex(f"\\text{{Slope }} = {slope_display} = {converted_slope_display} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)
        
        # Remaining step 3 information
        step3_p2 = MathTex(f"\\text{{From }} ({start_coords[0]}, {start_coords[1]})", color=y_intercept_color).scale(MATH_SCALE)
        
        rise_unit_text = "units" if rise_value > 1 else "unit"
        run_unit_text = "units" if run_value > 1 else "unit"
        step3_p3 = MathTex(f"\\text{{Rise }} {rise_value} \\text{{ {rise_unit_text} {rise_direction}}} \\text{{ and }} \\text{{Run }} {run_value} \\text{{ {run_unit_text} {run_direction}}}").scale(TEXT_SCALE)
        step3_p4 = MathTex(f"\\text{{Second point: }} ({end_coords[0]}, {end_coords[1]})").scale(MATH_SCALE)

        # Step 4: Draw Line
        step4_title = Tex("Step 4: Draw Line Through Points").scale(TEXT_SCALE)
        step4_p1 = MathTex(f"\\text{{Connect points }} ({start_coords[0]}, {start_coords[1]}) \\text{{ and }} ({end_coords[0]}, {end_coords[1]})").scale(MATH_SCALE)
        step4_p2 = MathTex(r"\text{Extend line in both directions}").scale(TEXT_SCALE)

        ###############################################################################
        # SECTION 8: FINAL EQUATION AND STYLING
        ###############################################################################
        final_equation = problem_text_equation.copy()
        final_equation.next_to(start_point, LEFT + DOWN, buff=0.7)  
        
        final_equation_rect = SurroundingRectangle(final_equation, color=slope_color, buff=0.2)
        
        # Apply basic coloringrise_for_fraction = rise_value
        self.color_component(step1_p1, "m", slope_color)
        self.color_component(step1_p1, "b", y_intercept_color)
        
        SmartColorizeStatic(
            step3_p1,
            {
                r"\text{rise}": rise_color, 
                r"\text{run}": run_color, 
                f"{converted_slope_display}": slope_color,
                f"{slope_display}": slope_color
             }
        )
        
        SmartColorizeStatic(
            step3_p3,
            {
                r"\text{Rise}": rise_color, 
                r"\text{Run}": run_color, 
                f"{rise_value} \\text{{ {rise_unit_text} {rise_direction}}}": rise_color,
                f"{run_value} \\text{{ {run_unit_text} {run_direction}}}": run_color
             }
        )
        
        SmartColorizeStatic(
            step4_p1,
            {
                f"({start_coords[0]}, {start_coords[1]})": y_intercept_color
             }
        )

        ###############################################################################
        # SECTION 9: LAYOUT AND POSITIONING
        ###############################################################################
        # Organize step groups
        step1_group = self.create_step(step1_title, step1_p1, step1_p2, step1_p3)
        step2_group = self.create_step(step2_title, step2_p1)
        step3_group = self.create_step(step3_title, step3_p1, step3_p2, step3_p3, step3_p4)
        step4_group = self.create_step(step4_title, step4_p1, step4_p2)
        
        steps_group = VGroup(
            problem_text_group,
            step1_group,
            step2_group,
            step3_group,
            step4_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Set the title colors
        step_titles = VGroup(step1_title, step2_title, step3_title, step4_title).set_color(GREY)

        # Position the entire content
        steps_group.to_edge(LEFT, buff=0.4).to_edge(UP, buff=0.5)

        ###############################################################################
        # SECTION 10: SCROLL MANAGER AND UI SETUP
        ###############################################################################
        # Set up solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text_label,
            problem_text_equation,
            step1_title,
            step1_p1,
            step1_p2,
            step1_p3,
            step2_title,
            step2_p1,
            step3_title,
            step3_p1, step3_p2, step3_p3, step3_p4,
            step4_title,
            step4_p1, step4_p2
        )
        
        scroll_mgr = ScrollManager(solution_steps)
        
        tip_1 = QuickTip(
            TEMPLATE_PARAMS["ui"]["tip_message"],
            fill_opacity=1
        ).shift(DOWN * 2)
        
        black_screen = SlopeOverlay()

        ###############################################################################
        # SECTION 11: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover(f"Let's graph the linear equation {spoken_equation}."):
            self.play(Write(axes), Write(axes_labels))
            # Initial scroll preparation - Introducing the problem
            scroll_mgr.prepare_next(self)  # Step 0: Problem Introduction
            scroll_mgr.prepare_next(self)  # Step 0: Continuation of Problem Introduction
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 1: We'll identify the key components of the equation."):
            # Prepare for Step 1: Identifying Equation Components
            scroll_mgr.prepare_next(self)  # Step 1: Introducing Slope-Intercept Form
        
        with self.voiceover("This equation is in slope-intercept form: y equals mx plus b."):
            # Prepare for detailed explanation of slope-intercept form
            scroll_mgr.prepare_next(self)  # Step 1: Explaining y = mx + b
        self.wait(STANDARD_PAUSE)

        # Animation for the slope
        with self.voiceover(f"The coefficient of x is the slope. Here, m equals {slope_spoken}."):
            self.highlight_formula_component(step1_p1, "m", slope_color)
            
            # Prepare for highlighting the slope
            scroll_mgr.prepare_next(self, slice(0, slope_tgt_start))  # Step 1: Preparing Slope Transformation
            
            source_text = problem_text_equation[0][slope_src_start:slope_src_end].copy()
            target_text = step1_p2[0][slope_tgt_start:slope_tgt_end]
            
            # Perform the transformation animation
            self.play(ReplacementTransform(source_text, target_text))
                
        self.wait(STANDARD_PAUSE)

        # Animation for the y-intercept
        with self.voiceover(f"The constant term is the y-intercept. Here, b equals {y_intercept_spoken}."):
            self.highlight_formula_component(step1_p1, "b", y_intercept_color)
            
            # Prepare for y-intercept transformation
            scroll_mgr.prepare_next(self, slice(0, y_intercept_tgt_start))  # Step 1: Preparing Y-Intercept Transformation
            
            source_text = problem_text_equation[0][y_intercept_src_start:y_intercept_src_end].copy()
            target_text = step1_p3[0][y_intercept_tgt_start:y_intercept_tgt_end]

            self.play(ReplacementTransform(source_text, target_text))
                
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            # Prepare for y-intercept plotting step
            scroll_mgr.prepare_next(self)  # Step 2: Introducing Y-Intercept Plotting
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"At the y-intercept, x equals 0, so we plot the point ({start_coords[0]}, {start_coords[1]})."):
            # Prepare for specific y-intercept coordinates
            scroll_mgr.prepare_next(self)  # Step 2: Showing Y-Intercept Coordinates
            self.play(Indicate(dot_start))
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Step 3: Now we'll use the slope to find a second point on the line."):
            # Scroll down to Step 3
            scroll_mgr.scroll_down(self, steps=2)
            # Prepare for Step 3 introduction
            scroll_mgr.prepare_next(self)  # Step 3: Introducing Slope and Point Finding
        self.wait(STANDARD_PAUSE)

        # Use different voiceover text based on fraction representation
        if is_slope_fraction:
            with self.voiceover(f"The slope {slope_spoken} is the ratio of rise over run."):
                # Prepare for slope as a fraction
                scroll_mgr.prepare_next(self)  # Step 3: Explaining Slope as Fraction
        else:
            with self.voiceover(f"The slope {slope_spoken} can be expressed as a fraction: {slope_spoken} over {run_spoken}, which is the ratio of rise over run."):
                # Prepare for slope representation
                scroll_mgr.prepare_next(self)  # Step 3: Converting Slope to Fraction
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"Starting from our y-intercept at ({start_coords[0]}, {start_coords[1]}):"):
            # Prepare for coordinate transformation
            scroll_mgr.prepare_next(self, slice(0, coord_tgt_start))  # Step 3: Showing Starting Coordinates
            
            source_coords = step2_p1[0][coord_src_start:coord_src_end].copy()
            target_coords = step3_p2[0][coord_tgt_start:coord_tgt_end]
            
            # Perform the transformation for the coordinates
            self.play(ReplacementTransform(source_coords, target_coords))
            
        self.wait(STANDARD_PAUSE)

        rise_unit_spoken = "units" if rise_value > 1 else "unit"
        run_unit_spoken = "units" if run_value > 1 else "unit"
        direction_explanation = f"We go {run_direction.lower()} because the slope is {'negative' if slope < 0 else 'positive'}."
        
        with self.voiceover(f"The rise is {rise_spoken} {rise_unit_spoken} {rise_direction.lower()}, because the slope is {slope_spoken}. The run is {run_spoken} {run_unit_spoken} {run_direction.lower()}. {direction_explanation}"):
            # Prepare for rise and run explanation
            scroll_mgr.prepare_next(self)  # Step 3: Explaining Rise and Run
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover(f"Let's visualize this with arrows. Each arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)

        # Fixed voiceover text to match multiple arrows
        arrow_text = "these arrows show" if run_value > 1 else "this arrow shows"
        with self.voiceover(f"And {arrow_text} our run of {run_spoken} {run_unit_spoken} to the {run_direction.lower()}."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(run_text_group))
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(f"This gives us our second point at ({end_coords[0]}, {end_coords[1]})."):
            # Scroll down for second point
            scroll_mgr.scroll_down(self, steps=2)
            # Prepare for second point
            scroll_mgr.prepare_next(self)  # Step 3: Showing Second Point Coordinates
            self.play(Indicate(dot_end))
        self.wait(STANDARD_PAUSE)
        
        # Determine slant direction based on slope
        slant_direction = "left" if slope < 0 else "right"
        opposite_slant = "right" if slope < 0 else "left"
        
        with self.voiceover(f"When the given slope is {'negative' if slope < 0 else 'positive'}, our line will slant to the {slant_direction}. Conversely, a {'positive' if slope < 0 else 'negative'} slope will slant to the {opposite_slant}."):
            self.play(FadeIn(black_screen))

        with self.voiceover("Step 4: Finally, we'll draw a straight line through these two points."):
            self.play(FadeOut(black_screen))
            # Prepare for Step 4 introduction
            scroll_mgr.prepare_next(self)  # Step 4: Introducing Line Drawing
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"We connect the points ({start_coords[0]}, {start_coords[1]}) and ({end_coords[0]}, {end_coords[1]})."):
            self.play(Write(connecting_line))
            # Scroll down for connecting points
            scroll_mgr.scroll_down(self, steps=1)
            # Prepare for point connection
            scroll_mgr.prepare_next(self)  # Step 4: Showing Point Connection
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"And extend the line in both directions to complete our graph of {spoken_equation}."):
            # Prepare for line extension
            scroll_mgr.prepare_next(self)  # Step 4: Extending Line in Both Directions
            self.play(
                ReplacementTransform(connecting_line, extended_line),
                FadeIn(start_tip),
                FadeIn(end_tip)
            )
            # Use a safe replacement animation that doesn't rely on specific indices
            self.play(ReplacementTransform(problem_text_equation.copy(), final_equation))
            self.play(Create(final_equation_rect))
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"Notice how the {'negative' if slope < 0 else 'positive'} slope creates a line that {'falls' if slope < 0 else 'rises'} from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(extended_line, scale_factor=1.2))
        self.wait(STANDARD_PAUSE)