from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
import numpy as np

config.verbosity = "ERROR"




class DynamicTriangle(Scene):
    def construct(self):
        # Example 1: Triangle with sides a=3, b=4, c=5
        triangle1 = self.create_triangle(
            a="3",
            b="4", 
            c="5",
            alpha=r"\theta",
            scale=1.0,
            position=LEFT * 3
        )
        
        # Example 2: Triangle with angle 30° and two sides
        triangle2 = self.create_triangle(
            a="2.5",
            b="4.3",
            alpha=r"30^\circ",
            scale=0.8,
            position=RIGHT * 3
        )
        
        # Example 3: Triangle with hypotenuse and one angle
        triangle3 = self.create_triangle(
            c="6",
            beta=r"45^\circ",
            b="4.24",
            scale=1.2,
            position=UP * 2
        )
        
        self.add(triangle1, triangle2, triangle3)
        self.wait()
    
    def create_triangle(
        self,
        a=None,      # Side opposite to angle alpha
        b=None,      # Side opposite to angle beta  
        c=None,      # Hypotenuse
        alpha=None,  # Angle at vertex B
        beta=None,   # Angle at vertex C
        scale=1.0,
        position=ORIGIN,
        right_angle_position="bottom_left",  # Options: "bottom_left", "bottom_right", "top_left", "top_right"
        color=WHITE,
        label_scale=0.5,
        label_shift=0.3,
        show_labels=True,
        show_angles=True
    ):
        """Create a customizable right triangle."""
        
        # Base triangle vertices (right angle at A)
        A = ORIGIN
        B = 4 * RIGHT  # Base length
        C = 3 * UP     # Height
        
        # Create the triangle
        triangle = Polygon(A, B, C, color=color)
        
        # Apply rotation based on right angle position
        rotation_map = {
            "top_right": PI,
            "top_left": -PI / 2,
            "bottom_right": PI / 2,
            "bottom_left": 0,
        }
        triangle.rotate(rotation_map[right_angle_position])
        
        # Create a group to hold all components
        triangle_group = VGroup(triangle)
        
        # Get rotated vertices
        A, B, C = triangle.get_vertices()
        
        # Add right angle marker
        right_angle = Angle.from_three_points(B, A, C, elbow=True, radius=0.3)
        triangle_group.add(right_angle)
        
        # Add side labels if requested
        if show_labels:
            # Helper function to add a label to a side
            def add_side_label(start, end, label_text, label_color=WHITE):
                if label_text:
                    mid_point = (start + end) / 2
                    # Calculate perpendicular direction for label placement
                    direction = end - start
                    perp = np.array([-direction[1], direction[0], 0])
                    perp = perp / np.linalg.norm(perp) * label_shift
                    
                    label = MathTex(label_text).scale(label_scale)
                    label.move_to(mid_point + perp)
                    label.set_color(label_color)
                    triangle_group.add(label)
            
            # Add labels based on right angle position
            if right_angle_position == "bottom_left":
                add_side_label(A, C, a, RED)      # Vertical side
                add_side_label(A, B, b, BLUE)     # Horizontal side
                add_side_label(B, C, c, GREEN)    # Hypotenuse
            elif right_angle_position == "bottom_right":
                add_side_label(A, C, a, RED)      # Vertical side
                add_side_label(B, A, b, BLUE)     # Horizontal side
                add_side_label(C, B, c, GREEN)    # Hypotenuse
            elif right_angle_position == "top_left":
                add_side_label(C, A, a, RED)      # Vertical side
                add_side_label(A, B, b, BLUE)     # Horizontal side
                add_side_label(B, C, c, GREEN)    # Hypotenuse
            elif right_angle_position == "top_right":
                add_side_label(C, A, a, RED)      # Vertical side
                add_side_label(B, A, b, BLUE)     # Horizontal side
                add_side_label(C, B, c, GREEN)    # Hypotenuse
        
        # Add angle labels if requested
        if show_angles:
            angle_radius = 0.6
            angle_label_shift = 0.3
            
            if alpha:
                # Angle at vertex B
                alpha_angle = Angle.from_three_points(C, B, A, radius=angle_radius)
                alpha_label = MathTex(alpha).scale(label_scale * 0.8)
                # Position label inside the angle arc
                angle_point = B + angle_radius * 0.7 * normalize(
                    normalize(A - B) + normalize(C - B)
                )
                alpha_label.move_to(angle_point)
                alpha_label.set_color(YELLOW)
                triangle_group.add(alpha_angle, alpha_label)
            
            if beta:
                # Angle at vertex C
                beta_angle = Angle.from_three_points(A, C, B, radius=angle_radius)
                beta_label = MathTex(beta).scale(label_scale * 0.8)
                # Position label inside the angle arc
                angle_point = C + angle_radius * 0.7 * normalize(
                    normalize(B - C) + normalize(A - C)
                )
                beta_label.move_to(angle_point)
                beta_label.set_color(YELLOW)
                triangle_group.add(beta_angle, beta_label)
        
        # Apply scale and position
        triangle_group.scale(scale)
        triangle_group.move_to(position)
        
        return triangle_group


# Example scene to test different triangles
class TriangleExamples(Scene):
    def construct(self):
        # Create a grid of different triangles
        triangles = []
        
        # Row 1: Different sizes
        t1 = self.create_simple_triangle(a="3", b="4", c="5", scale=0.5, position=LEFT*5 + UP*2)
        t2 = self.create_simple_triangle(a="5", b="12", c="13", scale=0.3, position=LEFT*2 + UP*2)
        t3 = self.create_simple_triangle(a="8", b="15", c="17", scale=0.2, position=RIGHT*1 + UP*2)
        
        # Row 2: Different orientations
        t4 = self.create_simple_triangle(a="3", b="4", c="5", scale=0.5, 
                                       position=LEFT*5 + DOWN*0.5, 
                                       right_angle_position="bottom_right")
        t5 = self.create_simple_triangle(a="3", b="4", c="5", scale=0.5, 
                                       position=LEFT*2 + DOWN*0.5, 
                                       right_angle_position="top_left")
        t6 = self.create_simple_triangle(a="3", b="4", c="5", scale=0.5, 
                                       position=RIGHT*1 + DOWN*0.5, 
                                       right_angle_position="top_right")
        
        # Row 3: With angles
        t7 = self.create_simple_triangle(a="a", b="b", c="c", alpha=r"30^\circ", beta=r"60^\circ",
                                       scale=0.5, position=LEFT*5 + DOWN*3)
        t8 = self.create_simple_triangle(b="4", c="5", alpha=r"\alpha", 
                                       scale=0.5, position=LEFT*2 + DOWN*3)
        t9 = self.create_simple_triangle(a="3", c="5", beta=r"\beta",
                                       scale=0.5, position=RIGHT*1 + DOWN*3)
        
        # Add all triangles
        for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9]:
            self.add(t)
        
        # Add labels
        self.add(Text("Different Sizes", font_size=20).next_to(t2, UP, buff=1))
        self.add(Text("Different Orientations", font_size=20).next_to(t5, UP, buff=1))
        self.add(Text("With Angles", font_size=20).next_to(t8, UP, buff=1))
        
        self.wait()
    
    def create_simple_triangle(self, **kwargs):
        """Simplified triangle creation wrapper."""
        creator = DynamicTriangle()
        return creator.create_triangle(**kwargs)