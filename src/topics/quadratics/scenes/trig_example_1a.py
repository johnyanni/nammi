from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class RightTriangleTrigonometry(MathTutorialScene):
    def construct(self):
        # Constants for scaling
        TEX_SCALE = 0.70
        
        # Color Definitions
        HYPOTENUSE_COLOR = "#FF5757"  # Red
        ADJACENT_COLOR = "#4CA1FF"    # Blue
        OPPOSITE_COLOR = "#51B965"    # Green
        ANGLE_COLOR = "#FFBF00"       # Amber
        
        # Create a right-angled triangle
        # Use (0,0) as the origin (bottom-left corner)
        origin = np.array([0, 0, 0])
        adjacent_point = np.array([5, 0, 0])  # 5 units right
        opposite_point = np.array([5, 3, 0])  # 5 units right, 3 units up
        
        # Calculate actual hypotenuse length
        hypotenuse_length = np.linalg.norm(opposite_point - origin)
        
        # Create the triangle
        triangle = Polygon(
            origin, adjacent_point, opposite_point, 
            color=WHITE, fill_color=GREY, fill_opacity=0.2
        )
        
        # Create the sides
        adjacent_side = Line(origin, adjacent_point, color=ADJACENT_COLOR)
        opposite_side = Line(adjacent_point, opposite_point, color=OPPOSITE_COLOR)
        hypotenuse_side = Line(origin, opposite_point, color=HYPOTENUSE_COLOR)
        
        # Mark the right angle
        right_angle_size = 0.5
        right_angle = Polygon(
            adjacent_point + np.array([-right_angle_size, 0, 0]),
            adjacent_point,
            adjacent_point + np.array([0, right_angle_size, 0]),
            color=WHITE
        )
        
        # Mark the angle θ
        angle_radius = 0.7
        angle_arc = Arc(
            start_angle=0,
            angle=np.arcsin(3/hypotenuse_length),
            radius=angle_radius,
            color=ANGLE_COLOR
        )
        
        # Label for the angle θ
        theta_label = MathTex(r"\theta", color=ANGLE_COLOR).scale(0.8)
        theta_label.next_to(angle_arc, RIGHT, buff=0.1)
        theta_label.shift(DOWN * 0.2)
        
        # Labels for the sides
        adjacent_label = MathTex("25", color=ADJACENT_COLOR).scale(0.8)
        adjacent_label.next_to(adjacent_side, DOWN, buff=0.2)
        
        hypotenuse_label = MathTex("x", color=HYPOTENUSE_COLOR).scale(0.8)
        hypotenuse_label.move_to(
            hypotenuse_side.get_center() + normalize(np.array([-1, 1, 0])) * 0.4
        )
        
        # Create a group for the triangle and its components
        triangle_group = VGroup(
            triangle, 
            adjacent_side, opposite_side, hypotenuse_side,
            right_angle, angle_arc, theta_label,
            adjacent_label, hypotenuse_label
        ).scale(1.2).to_edge(LEFT).shift(UP)
        
        # Create the formulas according to your specific request
        # First, show the general formula: theta = hypotenuse/adjacent
        general_formula = MathTex(
            r"\theta = \frac{\text{hypotenuse}}{\text{adjacent}}"
        ).scale(TEX_SCALE)
        
        # Next, show the formula with variables: theta = x/25
        variable_formula = MathTex(
            r"\theta = \frac{x}{25}"
        ).scale(TEX_SCALE)
        
        # Apply colorization
        self.apply_smart_colorize(
            [general_formula, variable_formula],
            {
                r"\theta": ANGLE_COLOR,
                "hypotenuse": HYPOTENUSE_COLOR,
                "adjacent": ADJACENT_COLOR,
                "x": HYPOTENUSE_COLOR,
                "25": ADJACENT_COLOR,
            }
        )
        
        # Position the formulas
        formulas = VGroup(general_formula, variable_formula).arrange(DOWN, buff=0.8).to_edge(RIGHT)
        
        # Function to get specific parts of an equation
        def find_element(pattern, exp, nth=0):
            indices = search_shape_in_text(exp, MathTex(pattern))
            if not indices or nth >= len(indices):
                return None
            return exp[0][indices[nth]]
        
        # Get the x and 25 in the variable formula for replacement transforms
        x_in_formula = find_element("x", variable_formula)
        adjacent_in_formula = find_element("25", variable_formula)
        
        # Create title
        title = Text("Relationship Between Angle and Sides", font_size=36)
        title.to_edge(UP)
        
        # Create note about the formula
        note = Text("(Using the reciprocal of cosine)", font_size=24, color=YELLOW)
        note.next_to(variable_formula, DOWN, buff=0.5)
        
        # ANIMATIONS
        
        # Show the title
        self.play(Write(title))
        self.wait(1)
        
        # Show the triangle
        self.play(
            Create(triangle),
            Create(adjacent_side),
            Create(opposite_side),
            Create(hypotenuse_side),
            Create(right_angle),
        )
        self.wait(1)
        
        # Show the angle and labels
        self.play(
            Create(angle_arc),
            Write(theta_label)
        )
        self.wait(1)
        
        # Show the side labels
        self.play(
            Write(adjacent_label),
            Write(hypotenuse_label)
        )
        self.wait(1)
        
        # Show the general formula
        self.play(Write(general_formula))
        self.wait(1)
        
        # Show the variable formula template (without values)
        self.play(FadeIn(variable_formula[0][0:2]))
        self.play(FadeIn(variable_formula[0][3]))
        self.wait(1)
        
        # Animate the hypotenuse value (x) moving to the formula
        self.play(
            ReplacementTransform(
                hypotenuse_label.copy(),
                x_in_formula,
                path_arc=PI/2,
                run_time=1.5
            )
        )
        self.wait(0.5)
        
        # Animate the adjacent value (25) moving to the formula
        self.play(
            ReplacementTransform(
                adjacent_label.copy(),
                adjacent_in_formula,
                path_arc=-PI/2,
                run_time=1.5
            )
        )
        self.wait(1)
        
        # Add explanatory text
        explanation = Text(
            "In this triangle, the angle θ equals the hypotenuse divided by the adjacent side", 
            font_size=24
        )
        explanation.next_to(variable_formula, DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(1)
        
        # Add the note
        self.play(Write(note))
        self.wait(2)
        
        # Final conclusions
        conclusion = Text(
            "This relationship helps us find unknown sides or angles in right triangles", 
            font_size=24
        )
        conclusion.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(3)