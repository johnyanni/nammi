"""Template for finding equations of lines using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

# ------------------------------------------------
# VARIABLES FOR FINDING LINE EQUATION - EDIT THESE FOR EACH NEW EXAMPLE
# ------------------------------------------------

# Core equation values and final result
SLOPE = 1/2                         # The slope value as a fraction
Y_INTERCEPT = 1                     # The y-intercept value as a number
FINAL_EQUATION = "y=\\frac{1}{2}x+1"  # Final equation with LaTeX

# Display and spoken representations
SLOPE_DISPLAY = "\\frac{1}{2}"      # How the slope appears in LaTeX
SLOPE_SPOKEN = "one half"           # How the slope should be spoken in voiceover
Y_INTERCEPT_DISPLAY = "1"           # How the y-intercept appears in LaTeX
Y_INTERCEPT_SPOKEN = "one"          # How the y-intercept should be spoken
FINAL_EQUATION_SPOKEN = "y equals one half x plus one"  # Spoken version of the final equation

# Coordinate points
POINT1 = [0, 1]                     # First point [x, y] - typically the y-intercept
POINT2 = [4, 3]                     # Second point [x, y]
USE_Y_INTERCEPT = True              # Whether point1 is the y-intercept

# Rise and run values for slope visualization
RISE_VALUE = 2                      # Simple rise value (numerator of slope after simplification)
RISE_SPOKEN = "two"                 # Spoken version of rise value
RUN_VALUE = 4                       # Simple run value (denominator of slope after simplification)
RUN_SPOKEN = "four"                 # Spoken version of run value
RISE_DIRECTION = "UP"               # Direction for rise: "UP" or "DOWN"
RUN_DIRECTION = "RIGHT"             # Direction for run: "LEFT" or "RIGHT"

# Coordinate plane settings
AXES_RANGE = [-6, 6, 1]             # Range for axes: [min, max, step]
X_LINE_RANGE = [-5, 5]              # X-range for plotting the line

# UI elements and styling
TIP_MESSAGE = "The slope measures how much the line rises or falls as we move from left to right."
Y_INTERCEPT_COLOR = YELLOW
SLOPE_COLOR = GREEN
RISE_COLOR = BLUE
RUN_COLOR = RED
POINT_COLOR = PINK
LINE_COLOR = WHITE

class FindSlopeInterceptFormTemplate(MathTutorialScene):
    """A tutorial that teaches how to find the equation of a line using slope-intercept form."""

    def construct(self):
        ###############################################################################
        # SECTION 1: COORDINATE PLANE SETUP
        ###############################################################################
        # Create axes
        axes, axes_labels = self.create_axes(x_range=AXES_RANGE)

        ###############################################################################
        # SECTION 2: LINE AND GRAPHICAL ELEMENTS
        ###############################################################################
        # Create the line y = mx + b
        def line_function(x):
            return SLOPE*x + Y_INTERCEPT  # Our equation based on parameters

        # For the full line with tips
        extended_line = axes.plot(
            line_function, 
            x_range=X_LINE_RANGE,
            color=LINE_COLOR,
            stroke_width=3
        )
        
        # Add tips to the line
        start_point = axes.c2p(X_LINE_RANGE[0], line_function(X_LINE_RANGE[0]))
        end_point = axes.c2p(X_LINE_RANGE[1], line_function(X_LINE_RANGE[1]))
        
        start_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.2)
        end_tip = ArrowTriangleFilledTip(color=LINE_COLOR, length=0.2)
        
        # Position tips at the ends with fixed angles
        angle = angle_of_vector([1, SLOPE])
        start_tip.move_to(start_point)
        start_tip.rotate(angle)
        end_tip.move_to(end_point)
        end_tip.rotate(angle + PI)  # Add PI to point in opposite direction
        
        # Group the line and tips
        line_group = VGroup(extended_line, start_tip, end_tip)

        ###############################################################################
        # SECTION 3: POINTS AND ARROWS FOR VISUALIZATION
        ###############################################################################
        # Create key points on the line
        if USE_Y_INTERCEPT:
            y_intercept_point = Dot(axes.c2p(*POINT1), color=Y_INTERCEPT_COLOR, radius=0.15)
            point1 = y_intercept_point
        else:
            y_intercept_point = Dot(axes.c2p(0, Y_INTERCEPT), color=Y_INTERCEPT_COLOR, radius=0.15)
            point1 = Dot(axes.c2p(*POINT1), color=POINT_COLOR, radius=0.15)
            
        point2 = Dot(axes.c2p(*POINT2), color=POINT_COLOR, radius=0.15)

        # Create rise arrows
        rise_arrows = []
        
        # Create rise arrows between points, adjusted for direction
        if RISE_DIRECTION == "UP":
            for i in range(RISE_VALUE):
                start_y = POINT1[1] + i
                arrow = Arrow(
                    start=axes.c2p(POINT1[0], start_y),
                    end=axes.c2p(POINT1[0], start_y + 1),
                    color=RISE_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        else:  # DOWN
            for i in range(RISE_VALUE):
                start_y = POINT1[1] - i
                arrow = Arrow(
                    start=axes.c2p(POINT1[0], start_y),
                    end=axes.c2p(POINT1[0], start_y - 1),
                    color=RISE_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4
                )
                rise_arrows.append(arrow)
        
        # Create run arrows
        run_arrows = []
        
        # Create run arrows based on direction
        if RUN_DIRECTION == "RIGHT":
            for i in range(RUN_VALUE):
                start_x = POINT1[0] + i
                arrow = Arrow(
                    start=axes.c2p(start_x, POINT2[1]),
                    end=axes.c2p(start_x + 1, POINT2[1]),
                    color=RUN_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4,
                )
                run_arrows.append(arrow)
        else:  # LEFT
            for i in range(RUN_VALUE):
                start_x = POINT1[0] - i
                arrow = Arrow(
                    start=axes.c2p(start_x, POINT2[1]),
                    end=axes.c2p(start_x - 1, POINT2[1]),
                    color=RUN_COLOR,
                    buff=0,
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.4,
                )
                run_arrows.append(arrow)
            
        ###############################################################################
        # SECTION 4: TEXT LABELS AND OVERLAYS
        ###############################################################################
        # Create rise text label
        rise_text_group = self.create_text_with_background(
            f"\\text{{Rise}} = {RISE_VALUE}",
            text_color=RISE_COLOR
        ).scale(MATH_SCALE)
        
        # Position rise text
        if len(rise_arrows) > 1:
            rise_arrows_group = VGroup(*rise_arrows)
            rise_text_group.next_to(rise_arrows_group, LEFT, buff=0.5)
        else:
            rise_text_group.next_to(rise_arrows[0], LEFT, buff=0.5)
        
        # Create run text label
        run_text_group = self.create_text_with_background(
            f"\\text{{Run}} = {RUN_VALUE}",
            text_color=RUN_COLOR
        ).scale(MATH_SCALE)
        
        # Position run text
        run_arrows_group = VGroup(*run_arrows)
        run_text_group.next_to(run_arrows_group, UP, buff=0.5)
        
        # Slope overlay for explaining slope direction
        slope_overlay = SlopeOverlay()

        ###############################################################################
        # SECTION 5: PROBLEM STATEMENT AND SOLUTION STEPS
        ###############################################################################
        problem_text = Tex("Find the equation of the given line.").scale(MATH_SCALE)

        # Step 1: Identify Points on the Line
        step1_title = Tex("Step 1: Identify Points on the Line").scale(TEXT_SCALE)
        
        if USE_Y_INTERCEPT:
            step1_p1 = Tex("Find the y-intercept where the line crosses the y-axis").scale(MATH_SCALE)
            step1_p2 = MathTex(f"\\text{{Y-intercept: }} ({POINT1[0]}, {POINT1[1]})", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)
        else:
            step1_p1 = Tex("Identify two points on the line").scale(MATH_SCALE)
            step1_p2 = MathTex(f"\\text{{Point 1: }} ({POINT1[0]}, {POINT1[1]})", color=POINT_COLOR).scale(MATH_SCALE)
            
        step1_p3 = MathTex(f"\\text{{{'Select another' if USE_Y_INTERCEPT else 'Point 2'} point: }} ({POINT2[0]}, {POINT2[1]})", color=POINT_COLOR).scale(MATH_SCALE)

        # Step 2: Calculate the Slope
        step2_title = Tex("Step 2: Calculate the Slope").scale(TEXT_SCALE)
        
        # Normal slope calculation
        step2_p1 = MathTex(r"\text{Slope } = \frac{\text{rise}}{\text{run}}").scale(MATH_SCALE)
        
        # Calculate rise and run from the coordinates
        rise = POINT2[1] - POINT1[1]
        run = POINT2[0] - POINT1[0]
        
        # Create slope calculation with simplification if needed
        if abs(rise) == RISE_VALUE and abs(run) == RUN_VALUE:
            # Direct calculation
            step2_p2 = MathTex(f"\\text{{Slope }} = \\frac{{{rise}}}{{{run}}} = {SLOPE_DISPLAY}").scale(MATH_SCALE)
        else:
            # Show simplification
            step2_p2 = MathTex(f"\\text{{Slope }} = \\frac{{{rise}}}{{{run}}} = \\frac{{{RISE_VALUE}}}{{{RUN_VALUE}}} = {SLOPE_DISPLAY}").scale(MATH_SCALE)
        
        # Step 3: Write the Equation in Slope-Intercept Form
        step3_title = Tex("Step 3: Write the Equation in Slope-Intercept Form").scale(TEXT_SCALE)
        
        step3_p1 = MathTex(r"\text{Slope-Intercept Form: } y = mx + b").scale(MATH_SCALE)
        step3_p2 = MathTex(r"\text{Where } m \text{ = slope and } b \text{ = y-intercept}").scale(TEXT_SCALE)
        step3_p3 = MathTex(f"m = {SLOPE_DISPLAY}", color=SLOPE_COLOR).scale(MATH_SCALE)
        
        if USE_Y_INTERCEPT:
            # Directly use the y-intercept if it's given
            step3_p4 = MathTex(f"b = {Y_INTERCEPT_DISPLAY}", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)
        else:
            # Calculate y-intercept using point-slope form
            step3_p4 = MathTex(f"b = {Y_INTERCEPT_DISPLAY}", color=Y_INTERCEPT_COLOR).scale(MATH_SCALE)
                
        # Step 4: Write the Final Equation
        step4_title = Tex("Step 4: Write the Final Equation").scale(TEXT_SCALE)
        
        step4_p1 = MathTex(r"y = mx + b").scale(MATH_SCALE)
        step4_p2 = MathTex(FINAL_EQUATION).scale(MATH_SCALE)
        
        
        step4_p1_var = step4_p1[0][search_shape_in_text(step4_p1, MathTex("y"))[0]].set_color(RED)
        
        self.add(step4_p1_var)
        
        # step4_p2_var = step4_p2[0][search_shape_in_text(step4_p2, MathTex(f"{SLOPE_DISPLAY}"))[0]].set_color(SLOPE_COLOR)
        
        step4_p2_var = self.color_component(step4_p2, SLOPE_DISPLAY, SLOPE_COLOR)
        
        step4_p2_var_2 = step4_p2[0][search_shape_in_text(step4_p2, MathTex(f"{Y_INTERCEPT_DISPLAY}"))[1]].set_color(Y_INTERCEPT_COLOR)
        
        self.add(step4_p2_var)
        self.add(step4_p2_var_2)
        

        ##############################################################################
        # SECTION 6: COLORING AND STYLING SETUP
        ##############################################################################
        
        # Define smart coloring for multiple elements
        smart_coloring = self.setup_smart_coloring({
            step2_p1: [r"Slope", r"\text{rise}", r"\text{run}"],
            step2_p2: [r"Slope", f"{rise}", f"{run}", f"{RISE_VALUE}", f"{RUN_VALUE}", SLOPE_DISPLAY],
            step3_p1: ["m","b"],
            step3_p2: [r"m \text{ = slope", r"b \text{ = y-intercept"],
            step4_p1: ["m", "b"],
            step4_p2: [Y_INTERCEPT_DISPLAY, SLOPE_DISPLAY]
        }, {
            "Slope": SLOPE_COLOR,
            "m": SLOPE_COLOR,
            "b": Y_INTERCEPT_COLOR,
            r"\text{rise}": RISE_COLOR,
            r"\text{run}": RUN_COLOR,
            f"{rise}": RISE_COLOR,
            f"{run}": RUN_COLOR,
            f"{RISE_VALUE}": RISE_COLOR,
            f"{RUN_VALUE}": RUN_COLOR,
            Y_INTERCEPT_DISPLAY: Y_INTERCEPT_COLOR,
            SLOPE_DISPLAY: SLOPE_COLOR,
            r"m \text{ = slope": SLOPE_COLOR,
            r"b \text{ = y-intercept": Y_INTERCEPT_COLOR
        })
        
        # Apply all smart coloring at once
        self.apply_element_specific_coloring(smart_coloring)


        ###############################################################################
        # SECTION 7: LAYOUT AND POSITIONING
        ###############################################################################
        # Create step groups
        step1_group = self.create_step(step1_title, step1_p1, step1_p2, step1_p3)
        step2_group = self.create_step(step2_title, step2_p1, step2_p2)
        step3_group = self.create_step(step3_title, step3_p1, step3_p2, step3_p3, step3_p4)
        step4_group = self.create_step(step4_title, step4_p1, step4_p2)
        
        # Create steps group with problem text
        steps_group = VGroup(
            problem_text,
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
        # SECTION 8: SCROLL MANAGER AND UI ELEMENTS SETUP
        ###############################################################################
        # Prepare all solution steps for the scroll manager
        solution_steps = VGroup(
            problem_text,
            step1_title,
            step1_p1, step1_p2, step1_p3,
            step2_title,
            step2_p1, step2_p2,
            step3_title,
            step3_p1, step3_p2, step3_p3, step3_p4,
            step4_title,
            step4_p1, step4_p2
        )
        
        # QuickTip
        tip_1 = QuickTip(
            TIP_MESSAGE,
            fill_opacity=1
        ).shift(DOWN * 2)
        
        # Initialize scroll manager
        scroll_mgr = ScrollManager(solution_steps)

        ###############################################################################
        # SECTION 9: ANIMATION SEQUENCE
        ###############################################################################
        # Animation sequence with voiceovers
        with self.voiceover("Given a line on a coordinate plane, let's find its equation."):
            self.play(Write(axes), Write(axes_labels), Write(line_group))
            scroll_mgr.prepare_next(self)  # Prepares: problem_text
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Step 1: First, we need to identify at least two points on the line."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_title
        self.wait(QUICK_PAUSE)  

        # Different voiceovers based on whether we're using the y-intercept
        if USE_Y_INTERCEPT:
            with self.voiceover("Let's find the y-intercept, which is where the line crosses the y-axis."):
                scroll_mgr.prepare_next(self)  # Prepares: step1_p1
            self.wait(STANDARD_PAUSE)  

            with self.voiceover(f"The y-intercept is at the point ({POINT1[0]}, {POINT1[1]})."):
                scroll_mgr.prepare_next(self)  # Prepares: step1_p2
                self.play(Indicate(y_intercept_point))
            self.wait(STANDARD_PAUSE)  
        else:
            with self.voiceover("Let's identify two points that lie on the line."):
                scroll_mgr.prepare_next(self)  # Prepares: step1_p1
            self.wait(STANDARD_PAUSE)  

            with self.voiceover(f"Our first point is ({POINT1[0]}, {POINT1[1]})."):
                scroll_mgr.prepare_next(self)  # Prepares: step1_p2
                self.play(Indicate(point1))
            self.wait(STANDARD_PAUSE)  

        with self.voiceover(f"We'll also {'select another' if USE_Y_INTERCEPT else 'use our second'} point on the line. Let's use ({POINT2[0]}, {POINT2[1]})."):
            scroll_mgr.prepare_next(self)  # Prepares: step1_p3
            self.play(Indicate(point2))
        self.wait(STANDARD_PAUSE)  

        with self.voiceover("Step 2: Now let's calculate the slope of the line."):
            scroll_mgr.scroll_down(self, steps=1)
            scroll_mgr.prepare_next(self)  # Prepares: step2_title
        self.wait(QUICK_PAUSE)  

        # Normal line case
        with self.voiceover("The slope is the ratio of the rise to the run."):
            scroll_mgr.prepare_next(self)  # Prepares: step2_p1
        self.wait(STANDARD_PAUSE)   

        with self.voiceover("To visualize this, let's see the rise between our two points."):
            for arrow in rise_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.play(Write(rise_text_group))
        self.wait(STANDARD_PAUSE)  
            
        with self.voiceover("And the run between our points."):
            for arrow in run_arrows:
                self.play(GrowArrow(arrow), run_time=1)
            self.play(Write(run_text_group))
            self.play(FadeIn(tip_1, shift=UP))
        self.wait(STANDARD_PAUSE)  
            
        # Customize the slope calculation narration based on whether simplification is needed
        rise = POINT2[1] - POINT1[1]
        run = POINT2[0] - POINT1[0]
        
        if abs(rise) == RISE_VALUE and abs(run) == RUN_VALUE:
            # Direct calculation
            with self.voiceover(f"Calculating the slope: The rise is {RISE_VALUE} units {'up' if rise > 0 else 'down'}, and the run is {RUN_VALUE} units {'right' if run > 0 else 'left'}. So, the slope is {RISE_VALUE} divided by {RUN_VALUE}, which is {SLOPE_SPOKEN}."):
                scroll_mgr.scroll_down(self, steps=2)
                scroll_mgr.prepare_next(self)  # Prepares: step2_p2
                self.play(FadeOut(tip_1, shift=DOWN))
        else:
            # With simplification
            with self.voiceover(f"Calculating the slope: The rise is {rise} units, and the run is {run} units. So, the slope is {rise} divided by {run}, which simplifies to {SLOPE_SPOKEN}."):
                scroll_mgr.scroll_down(self, steps=2)
                scroll_mgr.prepare_next(self)  # Prepares: step2_p2
                self.play(FadeOut(tip_1, shift=DOWN))
        self.wait(STANDARD_PAUSE)  

        # Animation sequence for the steps
        with self.voiceover("Step 3: Now we can write the equation using the slope-intercept form."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_title
        self.wait(QUICK_PAUSE) 

        with self.voiceover("The slope-intercept form of a line is y equals mx plus b."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p1
        self.wait(STANDARD_PAUSE)

        with self.voiceover("Where m is the slope <break time=\"1s\"/> and b is the y-intercept."):
            self.highlight_formula_component(step3_p1, "m", SLOPE_COLOR)
            scroll_mgr.prepare_next(self)  # Prepares: step3_p2
            self.highlight_formula_component(step3_p1, "b", Y_INTERCEPT_COLOR)
        self.wait(STANDARD_PAUSE)  
            
        with self.voiceover(f"We found that the slope m equals {SLOPE_SPOKEN}."):
            scroll_mgr.prepare_next(self)  # Prepares: step3_p3
        self.wait(STANDARD_PAUSE)  
            
        with self.voiceover(f"When the given slope is {'positive' if SLOPE > 0 else 'negative'}, our line will slant to the {'right' if SLOPE > 0 else 'left'}. Conversely, a {'negative' if SLOPE > 0 else 'positive'} slope will slant to the {'left' if SLOPE > 0 else 'right'}."):
            self.play(FadeIn(slope_overlay))
        self.wait(STANDARD_PAUSE)  

        y_intercept_explanation = ""
        if USE_Y_INTERCEPT:
            y_intercept_explanation = f"Since we already found the y-intercept, b equals {Y_INTERCEPT_SPOKEN}."
        else:
            y_intercept_explanation = f"To find the y-intercept, we substitute one of our points and the slope into the equation. This gives us b equals {Y_INTERCEPT_SPOKEN}."
            
        with self.voiceover(y_intercept_explanation):
            self.play(FadeOut(slope_overlay))
            scroll_mgr.prepare_next(self)  # Prepares: step3_p4
        self.wait(STANDARD_PAUSE)   

        with self.voiceover("Step 4: Finally, let's write the complete equation of the line."):
            scroll_mgr.scroll_down(self, steps=3)
            scroll_mgr.prepare_next(self)  # Prepares: step4_title
        self.wait(QUICK_PAUSE)   

        with self.voiceover(f"Substituting our values into the slope-intercept form, we get {FINAL_EQUATION_SPOKEN}."):
            scroll_mgr.prepare_next(self) # Prepares: step4_p1
            self.wait(1)
            scroll_mgr.prepare_next(self)  # Prepares: step4_p2
        self.wait(QUICK_PAUSE)  

        with self.voiceover(f"And there we have it! The equation of our line is {FINAL_EQUATION_SPOKEN}."):
            self.play(step4_p2.animate.scale(1.2))
        self.wait(END_PAUSE)