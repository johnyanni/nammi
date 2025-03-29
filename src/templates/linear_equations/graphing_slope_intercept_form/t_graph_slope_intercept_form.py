"""Template for graphing linear equations using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay

# ------------------------------------------------
# VARIABLES FOR LINEAR EQUATION GRAPHING - EDIT THESE FOR EACH NEW EXAMPLE
# ------------------------------------------------

# Core equation values
SLOPE = -3/4                        # The slope value as a fraction
Y_INTERCEPT = 3                     # The y-intercept value as a number
EQUATION_FORMATTED = "y=-\\frac{3}{4}x+3"  # Formatted equation with LaTeX

# Display and spoken representations
SLOPE_DISPLAY = "-\\frac{3}{4}"     # How the slope appears in LaTeX
SLOPE_SPOKEN = "negative three fourths"  # How the slope should be spoken in voiceover
Y_INTERCEPT_DISPLAY = "3"           # How the y-intercept appears in LaTeX
Y_INTERCEPT_SPOKEN = "three"        # How the y-intercept should be spoken
SPOKEN_EQUATION = "y equals negative three fourths x plus three"  # Spoken version for voiceover

# Animation indices for transformations
SLOPE_SRC_INDICES = [2, 6]          # Source indices in problem_text_equation for slope
SLOPE_TGT_INDICES = [-4, None]      # Target indices in step1_info_2 for slope value
Y_INTERCEPT_SRC_INDICES = [-1, None]  # Source indices in problem_text_equation for y-intercept
Y_INTERCEPT_TGT_INDICES = [-1, None]  # Target indices in step1_info_3 for y-intercept value
COORD_SRC_INDICES = [-5, None]
COORD_TGT_INDICES = [-5, None]

# Coordinate points and visual ranges
Y_INTERCEPT_POINT = [0, 3]          # Coordinates of y-intercept point
SECOND_POINT = [4, 0]               # Coordinates of second point (run 4, rise -3)
AXES_RANGE = [-4, 8, 1]             # Range for axes: [min, max, step]
X_LINE_RANGE = [-3.5, 7.5]          # X-range for plotting the line

# Rise and run values for slope visualization
RISE_VALUE = 3                      # Simple rise value (absolute value of slope numerator)
RISE_SPOKEN = "three"               # Spoken version of rise value
RUN_VALUE = 4                       # Simple run value (slope denominator)
RUN_SPOKEN = "four"                 # Spoken version of run value
RISE_DIRECTION = "DOWN"             # Direction for rise: "UP" or "DOWN"
RUN_DIRECTION = "RIGHT"             # Direction for run: "LEFT" or "RIGHT"

# UI elements and styling
TIP_MESSAGE = "When the slope (m) is negative, we go down (rise) and then to the right (run)."
Y_INTERCEPT_COLOR = YELLOW
SLOPE_COLOR = GREEN
RISE_COLOR = BLUE
RUN_COLOR = RED
LINE_COLOR = WHITE

class GraphSlopeInterceptFormTemplate(MathTutorialScene):
    """A tutorial that teaches how to graph a linear equation using slope-intercept form."""

    def construct(self):
        ###############################################################################
        # SECTION 1: SETUP AND PREPROCESSING
        ###############################################################################
        # Process fraction-related variables early
        def is_fraction_format(tex_string):
            """Check if a string is formatted as a LaTeX fraction."""
            return "\\frac{" in tex_string and "}{" in tex_string and "}" in tex_string

        # Determine if slope_display is already a fraction and prepare variables
        is_slope_fraction = is_fraction_format(SLOPE_DISPLAY)
        
        # For non-fraction slopes, prepare the converted fraction representation
        converted_slope_display = None
        if not is_slope_fraction:
            try:
                # Try to interpret as a number
                slope_number = float(SLOPE_DISPLAY.replace("\\", ""))
                if slope_number < 0:
                    # For negative slopes, remove the negative sign and place it outside the fraction
                    converted_slope_display = f"-\\frac{{{SLOPE_DISPLAY.replace('-', '')}}}{{{1}}}"
                else:
                    # For positive slopes
                    converted_slope_display = f"\\frac{{{SLOPE_DISPLAY}}}{{{1}}}"
            except ValueError:
                # For symbolic expressions that aren't simple numbers
                if SLOPE_DISPLAY.startswith("-"):
                    # For negative symbolic expressions
                    converted_slope_display = f"-\\frac{{{SLOPE_DISPLAY[1:]}}}{{{1}}}"
                else:
                    # For positive symbolic expressions
                    converted_slope_display = f"\\frac{{{SLOPE_DISPLAY}}}{{{1}}}"

        ###############################################################################
        # SECTION 2: COORDINATE PLANE SETUP
        ###############################################################################
        # Create axes
        axes, axes_labels = self.create_axes(x_range=AXES_RANGE)

        ###############################################################################
        # SECTION 3: POINTS AND LINE SETUP
        ###############################################################################
        # Create visual elements
        dot_start = Dot(axes.c2p(*Y_INTERCEPT_POINT), color=Y_INTERCEPT_COLOR, radius=0.15)
        dot_end = Dot(axes.c2p(*SECOND_POINT), color=WHITE, radius=0.15)
        
        def line_function(x):
            return SLOPE*x + Y_INTERCEPT  # Our equation based on variables

        # For the initial segment connecting just the two points
        point1 = axes.c2p(Y_INTERCEPT_POINT[0], Y_INTERCEPT_POINT[1])
        point2 = axes.c2p(SECOND_POINT[0], SECOND_POINT[1])
        
        connecting_line = Line(
            start=point1,
            end=point2,
            color=LINE_COLOR
        )

        ###############################################################################
        # SECTION 4: EXTENDED LINE AND TIPS
        ###############################################################################
        # For the extended line showing the full graph
        extended_line = axes.plot(
            line_function, 
            x_range=X_LINE_RANGE,
            color=LINE_COLOR
        )

        # Add tips to the extended line
        start_point = axes.c2p(X_LINE_RANGE[0], line_function(X_LINE_RANGE[0]))
        end_point = axes.c2p(X_LINE_RANGE[1], line_function(X_LINE_RANGE[1]))

        start_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.2)
        end_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.2)

        # Position tips at the ends with fixed angles
        angle = angle_of_vector([1, SLOPE])
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
        rise_start_x = Y_INTERCEPT_POINT[0]
        rise_start_y = Y_INTERCEPT_POINT[1]
        
        # Create rise arrows based on direction
        if RISE_DIRECTION == "UP":
            for i in range(RISE_VALUE):
                arrow = Arrow(
                    start=axes.c2p(rise_start_x, rise_start_y + i),
                    end=axes.c2p(rise_start_x, rise_start_y + i + 1),
                    color=RISE_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        else:  # DOWN
            for i in range(RISE_VALUE):
                arrow = Arrow(
                    start=axes.c2p(rise_start_x, rise_start_y - i),
                    end=axes.c2p(rise_start_x, rise_start_y - i - 1),
                    color=RISE_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        
        # Group rise arrows for consistent referencing
        rise_arrows_group = VGroup(*rise_arrows)
        
        # Create run arrows
        run_arrows = []
        run_start_x = Y_INTERCEPT_POINT[0]
        run_start_y = SECOND_POINT[1]  # The y-coordinate after the rise
        
        # Create run arrows based on direction
        if RUN_DIRECTION == "LEFT":
            for i in range(RUN_VALUE):
                arrow = Arrow(
                    start=axes.c2p(run_start_x - i, run_start_y),
                    end=axes.c2p(run_start_x - i - 1, run_start_y),
                    color=RUN_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                run_arrows.append(arrow)
        else:  # RIGHT
            for i in range(RUN_VALUE):
                arrow = Arrow(
                    start=axes.c2p(run_start_x + i, run_start_y),
                    end=axes.c2p(run_start_x + i + 1, run_start_y),
                    color=RUN_COLOR,
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
            f"\\text{{Rise}} = {RISE_VALUE}",
            text_color=RISE_COLOR
        ).scale(MATH_SCALE)
        
        # Better positioning for rise text - centered if multiple arrows
        if len(rise_arrows) > 1:
            rise_text_group.next_to(rise_arrows_group, LEFT, buff=0.5)
        else:
            rise_text_group.next_to(rise_arrows[0], LEFT, buff=0.5)
        
        # Create run text label
        run_text_group = self.create_text_with_background(
            f"\\text{{Run}} = {RUN_VALUE}",
            text_color=RUN_COLOR
        ).scale(MATH_SCALE)
        
        # Better positioning for run text - centered if multiple arrows
        run_text_group.next_to(run_arrows_group, UP, buff=0.5)

        ###############################################################################
        # SECTION 7: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        # Create the problem text with explicit parts for better control
        problem_text_label = Tex("Graph:").scale(MATH_SCALE)
        problem_text_equation = MathTex(EQUATION_FORMATTED).scale(MATH_SCALE)
        problem_text_group = VGroup(problem_text_label, problem_text_equation).arrange(buff=0.2)
        
        # Get absolute slope for text
        slope_sign = "negative " if SLOPE < 0 else ""

        # Step 1: Identify Components
        step1_title = Tex("Step 1: Identify Components").scale(TEXT_SCALE)
        step1_p1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step1_p2 = MathTex(f"\\text{{Slope }} (m) = {SLOPE_DISPLAY}", color=SLOPE_COLOR).scale(MATH_SCALE)
        step1_p3 = MathTex(f"\\text{{Y-intercept }} (b) = {Y_INTERCEPT_DISPLAY}", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)
        
        # Step 2: Plot Y-intercept
        step2_title = Tex("Step 2: Plot Y-intercept").scale(TEXT_SCALE)
        step2_p1 = MathTex(f"\\text{{Plot point }} ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]})", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)

        # Step 3: Use Slope to Find Second Point
        step3_title = Tex("Step 3: Use Slope to Find Second Point").scale(TEXT_SCALE)
        
        # Create the appropriate step3_p1 based on slope representation
        if is_slope_fraction:
            # If slope_display is already a fraction, use it directly
            step3_p1 = MathTex(f"\\text{{Slope }} = {SLOPE_DISPLAY} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)
        else:
            # If slope_display is not a fraction, include the converted fraction representation
            step3_p1 = MathTex(f"\\text{{Slope }} = {SLOPE_DISPLAY} = {converted_slope_display} = \\frac{{\\text{{rise}}}}{{\\text{{run}}}}").scale(MATH_SCALE)
        
        # Remaining step 3 information
        step3_p2 = MathTex(f"\\text{{From }} ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]})", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)
        
        rise_unit_text = "units" if RISE_VALUE > 1 else "unit"
        run_unit_text = "units" if RUN_VALUE > 1 else "unit"
        step3_p3 = MathTex(f"\\text{{Rise }} {RISE_VALUE} \\text{{ {rise_unit_text} {RISE_DIRECTION}}} \\text{{ and }} \\text{{Run }} {RUN_VALUE} \\text{{ {run_unit_text} {RUN_DIRECTION}}}").scale(TEXT_SCALE)
        step3_p4 = MathTex(f"\\text{{Second point: }} ({SECOND_POINT[0]}, {SECOND_POINT[1]})").scale(MATH_SCALE)

        # Step 4: Draw Line
        step4_title = Tex("Step 4: Draw Line Through Points").scale(TEXT_SCALE)
        step4_p1 = MathTex(f"\\text{{Connect points }} ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]}) \\text{{ and }} ({SECOND_POINT[0]}, {SECOND_POINT[1]})").scale(MATH_SCALE)
        step4_p2 = MathTex(r"\text{Extend line in both directions}").scale(TEXT_SCALE)

        ###############################################################################
        # SECTION 8: FINAL EQUATION AND STYLING
        ###############################################################################
        final_equation = problem_text_equation.copy()
        final_equation.next_to(start_point, LEFT + DOWN, buff=0.7)  
        
        final_equation_rect = SurroundingRectangle(final_equation, color=SLOPE_COLOR, buff=0.2)
        
        # Apply basic coloring
        self.color_component(step1_p1, "m", SLOPE_COLOR)
        self.color_component(step1_p1, "b", Y_INTERCEPT_COLOR)
        
        SmartColorizeStatic(
            step3_p1,
            {
                r"\text{rise}": RISE_COLOR, 
                r"\text{run}": RUN_COLOR, 
                f"{converted_slope_display}": SLOPE_COLOR,
                f"{SLOPE_DISPLAY}": SLOPE_COLOR
             }
        )
        
        SmartColorizeStatic(
            step3_p3,
            {
                r"\text{Rise}": RISE_COLOR, 
                r"\text{Run}": RUN_COLOR, 
                f"{RISE_VALUE} \\text{{ {rise_unit_text} {RISE_DIRECTION}}}": RISE_COLOR,
                f"{RUN_VALUE} \\text{{ {run_unit_text} {RUN_DIRECTION}}}": RUN_COLOR
             }
        )
        
        SmartColorizeStatic(
            step4_p1,
            {
                f"({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]})": Y_INTERCEPT_COLOR
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
            TIP_MESSAGE,
            fill_opacity=1
        ).shift(DOWN * 2)
        
        black_screen = SlopeOverlay()

        ###############################################################################
        # SECTION 11: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover(f"Let's graph the linear equation {SPOKEN_EQUATION}."):
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
        with self.voiceover(f"The coefficient of x is the slope. Here, m equals {SLOPE_SPOKEN}."):
            self.highlight_formula_component(step1_p1, "m", SLOPE_COLOR)
            
            # Prepare for highlighting the slope
            scroll_mgr.prepare_next(self, slice(0, SLOPE_TGT_INDICES[0]))  # Step 1: Preparing Slope Transformation
            
            source_text = problem_text_equation[0][SLOPE_SRC_INDICES[0]:SLOPE_SRC_INDICES[1]].copy()
            target_text = step1_p2[0][SLOPE_TGT_INDICES[0]:SLOPE_TGT_INDICES[1]]
            
            # Perform the transformation animation
            self.play(ReplacementTransform(source_text, target_text))
                
        self.wait(STANDARD_PAUSE)

        # Animation for the y-intercept
        with self.voiceover(f"The constant term is the y-intercept. Here, b equals {Y_INTERCEPT_SPOKEN}."):
            self.highlight_formula_component(step1_p1, "b", Y_INTERCEPT_COLOR)
            
            # Prepare for y-intercept transformation
            scroll_mgr.prepare_next(self, slice(0, Y_INTERCEPT_TGT_INDICES[0]))  # Step 1: Preparing Y-Intercept Transformation
            
            source_text = problem_text_equation[0][Y_INTERCEPT_SRC_INDICES[0]:Y_INTERCEPT_SRC_INDICES[1]].copy()
            target_text = step1_p3[0][Y_INTERCEPT_TGT_INDICES[0]:Y_INTERCEPT_TGT_INDICES[1]]

            self.play(ReplacementTransform(source_text, target_text))
                
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"Step 2: Let's plot the y-intercept, which is the point where the line crosses the y-axis."):
            # Prepare for y-intercept plotting step
            scroll_mgr.prepare_next(self)  # Step 2: Introducing Y-Intercept Plotting
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"At the y-intercept, x equals 0, so we plot the point ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]})."):
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
            with self.voiceover(f"The slope {SLOPE_SPOKEN} is the ratio of rise over run."):
                # Prepare for slope as a fraction
                scroll_mgr.prepare_next(self)  # Step 3: Explaining Slope as Fraction
        else:
            with self.voiceover(f"The slope {SLOPE_SPOKEN} can be expressed as a fraction: {SLOPE_SPOKEN} over {RUN_SPOKEN}, which is the ratio of rise over run."):
                # Prepare for slope representation
                scroll_mgr.prepare_next(self)  # Step 3: Converting Slope to Fraction
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"Starting from our y-intercept at ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]}):"):
            # Prepare for coordinate transformation
            scroll_mgr.prepare_next(self, slice(0, COORD_TGT_INDICES[0]))  # Step 3: Showing Starting Coordinates
            
            source_coords = step2_p1[0][COORD_SRC_INDICES[0]:COORD_SRC_INDICES[1]].copy()
            target_coords = step3_p2[0][COORD_TGT_INDICES[0]:COORD_TGT_INDICES[1]]
            
            # Perform the transformation for the coordinates
            self.play(ReplacementTransform(source_coords, target_coords))
            
        self.wait(STANDARD_PAUSE)

        rise_unit_spoken = "units" if RISE_VALUE > 1 else "unit"
        run_unit_spoken = "units" if RUN_VALUE > 1 else "unit"
        direction_explanation = f"We go {RUN_DIRECTION.lower()} because the slope is {'negative' if SLOPE < 0 else 'positive'}."
        
        with self.voiceover(f"The rise is {RISE_SPOKEN} {rise_unit_spoken} {RISE_DIRECTION.lower()}, because the slope is {SLOPE_SPOKEN}. The run is {RUN_SPOKEN} {run_unit_spoken} {RUN_DIRECTION.lower()}. {direction_explanation}"):
            # Prepare for rise and run explanation
            scroll_mgr.prepare_next(self)  # Step 3: Explaining Rise and Run
        self.wait(STANDARD_PAUSE)
        
        with self.voiceover(f"Let's visualize this with arrows. Each arrow represents 1 unit of our rise."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)

        # Fixed voiceover text to match multiple arrows
        arrow_text = "these arrows show" if RUN_VALUE > 1 else "this arrow shows"
        with self.voiceover(f"And {arrow_text} our run of {RUN_SPOKEN} {run_unit_spoken} to the {RUN_DIRECTION.lower()}."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(run_text_group))
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(f"This gives us our second point at ({SECOND_POINT[0]}, {SECOND_POINT[1]})."):
            # Scroll down for second point
            scroll_mgr.scroll_down(self, steps=2)
            # Prepare for second point
            scroll_mgr.prepare_next(self)  # Step 3: Showing Second Point Coordinates
            self.play(Indicate(dot_end))
        self.wait(STANDARD_PAUSE)
        
        # Determine slant direction based on slope
        slant_direction = "left" if SLOPE < 0 else "right"
        opposite_slant = "right" if SLOPE < 0 else "left"
        
        with self.voiceover(f"When the given slope is {'negative' if SLOPE < 0 else 'positive'}, our line will slant to the {slant_direction}. Conversely, a {'positive' if SLOPE < 0 else 'negative'} slope will slant to the {opposite_slant}."):
            self.play(FadeIn(black_screen))

        with self.voiceover("Step 4: Finally, we'll draw a straight line through these two points."):
            self.play(FadeOut(black_screen))
            # Prepare for Step 4 introduction
            scroll_mgr.prepare_next(self)  # Step 4: Introducing Line Drawing
        self.wait(QUICK_PAUSE)

        with self.voiceover(f"We connect the points ({Y_INTERCEPT_POINT[0]}, {Y_INTERCEPT_POINT[1]}) and ({SECOND_POINT[0]}, {SECOND_POINT[1]})."):
            self.play(Write(connecting_line))
            # Scroll down for connecting points
            scroll_mgr.scroll_down(self, steps=1)
            # Prepare for point connection
            scroll_mgr.prepare_next(self)  # Step 4: Showing Point Connection
        self.wait(STANDARD_PAUSE)

        with self.voiceover(f"And extend the line in both directions to complete our graph of {SPOKEN_EQUATION}."):
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

        with self.voiceover(f"Notice how the {'negative' if SLOPE < 0 else 'positive'} slope creates a line that {'falls' if SLOPE < 0 else 'rises'} from left to right, and the y-intercept determines where the line crosses the y-axis."):
            self.play(Indicate(extended_line, scale_factor=1.2))
        self.wait(STANDARD_PAUSE)