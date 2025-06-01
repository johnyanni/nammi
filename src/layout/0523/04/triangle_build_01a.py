from manim import *
import numpy as np
from math import sqrt, asin, acos, atan, radians, degrees

class DynamicTriangle:
    """Enhanced Triangle class that creates triangles with actual custom proportions."""
    
    def __init__(
        self,
        a=None,      # Side length (not just label)
        b=None,      # Side length (not just label)
        c=None,      # Side length (not just label)
        alpha=None,  # Angle in degrees or radians
        beta=None,   # Angle in degrees or radians
        scale=1.0,   # Overall scale factor
        position=ORIGIN,
        right_angle_position="bottom_left",
        show_labels=True,
        show_angles=True,
        label_scale=0.5,
        label_shift=0.3,
        angle_radius=0.5,
        color=WHITE,
        color_map=None
    ):
        self.a = self._extract_number(a) if a else None
        self.b = self._extract_number(b) if b else None
        self.c = self._extract_number(c) if c else None
        self.alpha = self._extract_angle(alpha) if alpha else None
        self.beta = self._extract_angle(beta) if beta else None
        
        # Labels for display
        self.a_label = str(a) if a else None
        self.b_label = str(b) if b else None
        self.c_label = str(c) if c else None
        self.alpha_label = alpha if alpha else None
        self.beta_label = beta if beta else None
        
        self.scale = scale
        self.position = position
        self.right_angle_position = right_angle_position
        self.show_labels = show_labels
        self.show_angles = show_angles
        self.label_scale = label_scale
        self.label_shift = label_shift
        self.angle_radius = angle_radius
        self.color = color
        self.color_map = color_map or {
            "a": RED, "b": BLUE, "c": GREEN, "angle": YELLOW
        }
        
        # Calculate missing values
        self._calculate_triangle()
        self._triangle = self._build()
    
    def _extract_number(self, value):
        """Extract numeric value from string or return number directly."""
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            # Remove units and extract number
            import re
            match = re.search(r'[\d.]+', value)
            if match:
                return float(match.group())
        return None
    
    def _extract_angle(self, angle):
        """Extract angle in radians from various formats."""
        if isinstance(angle, (int, float)):
            return float(angle)
        if isinstance(angle, str):
            # Check for degree symbol
            if "°" in angle or "\\circ" in angle:
                import re
                match = re.search(r'[\d.]+', angle)
                if match:
                    return radians(float(match.group()))
        return None
    
    def _calculate_triangle(self):
        """Calculate missing sides and angles using trigonometry."""
        # If we have two sides, calculate the third using Pythagorean theorem
        if self.a and self.b and not self.c:
            self.c = sqrt(self.a**2 + self.b**2)
            if not self.c_label:
                self.c_label = f"{self.c:.2f}"
        elif self.a and self.c and not self.b:
            self.b = sqrt(self.c**2 - self.a**2)
            if not self.b_label:
                self.b_label = f"{self.b:.2f}"
        elif self.b and self.c and not self.a:
            self.a = sqrt(self.c**2 - self.b**2)
            if not self.a_label:
                self.a_label = f"{self.a:.2f}"
        
        # Calculate angles if we have all sides
        if self.a and self.b and self.c:
            if not self.alpha:
                self.alpha = atan(self.a / self.b)
                if not self.alpha_label:
                    self.alpha_label = f"{degrees(self.alpha):.1f}°"
            if not self.beta:
                self.beta = atan(self.b / self.a)
                if not self.beta_label:
                    self.beta_label = f"{degrees(self.beta):.1f}°"
        
        # If we still don't have all sides, use default 3-4-5
        if not all([self.a, self.b, self.c]):
            self.a = self.a or 3
            self.b = self.b or 4
            self.c = self.c or 5
    
    def _build(self):
        """Build the triangle with actual proportions."""
        # Create vertices based on actual side lengths
        A = ORIGIN
        B = self.b * RIGHT
        C = self.a * UP
        
        # Create the triangle
        triangle = Polygon(A, B, C, color=self.color, stroke_width=3)
        
        # Apply rotation based on right angle position
        rotation_map = {
            "top_right": PI,
            "top_left": -PI / 2,
            "bottom_right": PI / 2,
            "bottom_left": 0,
        }
        triangle.rotate(rotation_map[self.right_angle_position])
        
        # Create group
        triangle_group = VGroup(triangle)
        
        # Get rotated vertices
        A, B, C = triangle.get_vertices()
        
        # Add right angle marker
        right_angle = Angle.from_three_points(B, A, C, elbow=True, radius=0.3)
        triangle_group.add(right_angle)
        
        # Add side labels
        if self.show_labels:
            # Helper function to add centered label
            def add_side_label(start, end, label, color):
                if label:
                    mid_point = (start + end) / 2
                    direction = end - start
                    perp = np.array([-direction[1], direction[0], 0])
                    perp = perp / np.linalg.norm(perp) * self.label_shift
                    
                    label_mob = MathTex(label).scale(self.label_scale)
                    label_mob.move_to(mid_point + perp)
                    label_mob.set_color(color)
                    triangle_group.add(label_mob)
            
            # Add labels based on orientation
            if self.right_angle_position == "bottom_left":
                add_side_label(A, C, self.a_label, self.color_map["a"])  # Vertical
                add_side_label(A, B, self.b_label, self.color_map["b"])  # Horizontal
                add_side_label(B, C, self.c_label, self.color_map["c"])  # Hypotenuse
            # Add other orientations as needed...
        
        # Add angle labels
        if self.show_angles and (self.alpha_label or self.beta_label):
            if self.alpha_label:
                alpha_angle = Angle.from_three_points(C, B, A, radius=self.angle_radius)
                alpha_label = MathTex(self.alpha_label).scale(self.label_scale * 0.8)
                angle_point = B + self.angle_radius * 0.7 * normalize(
                    normalize(A - B) + normalize(C - B)
                )
                alpha_label.move_to(angle_point)
                alpha_label.set_color(self.color_map["angle"])
                triangle_group.add(alpha_angle, alpha_label)
            
            if self.beta_label:
                beta_angle = Angle.from_three_points(A, C, B, radius=self.angle_radius)
                beta_label = MathTex(self.beta_label).scale(self.label_scale * 0.8)
                angle_point = C + self.angle_radius * 0.7 * normalize(
                    normalize(B - C) + normalize(A - C)
                )
                beta_label.move_to(angle_point)
                beta_label.set_color(self.color_map["angle"])
                triangle_group.add(beta_angle, beta_label)
        
        # Apply scale and position
        triangle_group.scale(self.scale)
        triangle_group.move_to(self.position)
        
        return triangle_group
    
    def triangle(self):
        """Return the triangle VGroup."""
        return self._triangle


class TriangleExamples(Scene):
    def construct(self):
        # Example 1: Different sized triangles with actual proportions
        triangles = []
        
        # Small 3-4-5 triangle
        t1 = DynamicTriangle(
            a=3, b=4, c=5,
            scale=0.5,
            position=LEFT * 5 + UP * 2,
            show_angles=True
        )
        
        # Larger 5-12-13 triangle (different proportions)
        t2 = DynamicTriangle(
            a=5, b=12, c=13,
            scale=0.3,
            position=LEFT * 2 + UP * 2
        )
        
        # 8-15-17 triangle
        t3 = DynamicTriangle(
            a=8, b=15, c=17,
            scale=0.2,
            position=RIGHT * 2 + UP * 2
        )
        
        # Triangle specified by two sides (calculates hypotenuse)
        t4 = DynamicTriangle(
            a=6, b=8,  # c will be calculated as 10
            scale=0.4,
            position=LEFT * 5 + DOWN * 2
        )
        
        # Triangle with custom labels and units
        t5 = DynamicTriangle(
            a="7.5 cm", 
            b="10 cm", 
            c="12.5 cm",
            scale=0.3,
            position=LEFT * 2 + DOWN * 2
        )
        
        # Triangle with angles
        t6 = DynamicTriangle(
            a=4, b=4,  # Isosceles right triangle
            alpha="45°",
            beta="45°",
            scale=0.5,
            position=RIGHT * 2 + DOWN * 2
        )
        
        # Add all triangles
        for t in [t1, t2, t3, t4, t5, t6]:
            self.add(t.triangle())
        
        # Add descriptive labels
        self.add(Text("3-4-5", font_size=20).next_to(t1.triangle(), UP))
        self.add(Text("5-12-13", font_size=20).next_to(t2.triangle(), UP))
        self.add(Text("8-15-17", font_size=20).next_to(t3.triangle(), UP))
        self.add(Text("6-8-10", font_size=20).next_to(t4.triangle(), UP))
        self.add(Text("With Units", font_size=20).next_to(t5.triangle(), UP))
        self.add(Text("45-45-90", font_size=20).next_to(t6.triangle(), UP))
        
        self.wait()


class AnimatedTriangleSizes(Scene):
    def construct(self):
        # Start with a 3-4-5 triangle
        triangle = DynamicTriangle(a=3, b=4, c=5, scale=0.8)
        t = triangle.triangle()
        self.add(t)
        self.wait()
        
        # Transform to different sizes
        sizes = [
            (5, 12, 13),
            (8, 15, 17),
            (7, 24, 25),
            (9, 12, 15),
            (3, 4, 5)  # Back to original
        ]
        
        for a, b, c in sizes:
            new_triangle = DynamicTriangle(a=a, b=b, c=c, scale=0.8)
            self.play(Transform(t, new_triangle.triangle()))
            self.wait(0.5)
        
        self.wait()


# To run:
# manim -pql dynamic_triangles.py TriangleExamples
# manim -pql dynamic_triangles.py AnimatedTriangleSizes