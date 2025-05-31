from manim import *

class CrossingLines(Scene):
    def construct(self):
        # Example 1: Simple X with numbers at corners
        # Define the endpoints
        top_left = UP * 0.6 + LEFT * 1
        top_right = UP * 0.6 + RIGHT * 1
        bottom_left = DOWN * 0.6 + LEFT * 1
        bottom_right = DOWN * 0.6 + RIGHT * 1
        
        # Create the diagonal lines
        line1 = Line(top_left, bottom_right, color=BLUE, stroke_width=4)
        line2 = Line(top_right, bottom_left, color=RED, stroke_width=4)
        
        # Create numbers for each endpoint
        num1 = MathTex("1", font_size=36).next_to(top_left, UP + LEFT, buff=0.2)
        num2 = MathTex("2", font_size=36).next_to(top_right, UP + RIGHT, buff=0.2)
        num3 = MathTex("3", font_size=36).next_to(bottom_left, DOWN + LEFT, buff=0.2)
        num4 = MathTex("4", font_size=36).next_to(bottom_right, DOWN + RIGHT, buff=0.2)
        
        # Animate
        self.play(Create(line1), Create(line2))
        self.play(Write(num1), Write(num2), Write(num3), Write(num4))
        self.wait()


class CrossingLinesWithDots(Scene):
    def construct(self):
        # Example 2: With dots at endpoints
        # Define the endpoints
        points = {
            "A": UP * 2.5 + LEFT * 3,
            "B": UP * 2.5 + RIGHT * 3,
            "C": DOWN * 2.5 + LEFT * 3,
            "D": DOWN * 2.5 + RIGHT * 3
        }
        
        # Create lines
        line_AC_BD = Line(points["A"], points["D"], color=GREEN, stroke_width=5)
        line_BC_AD = Line(points["B"], points["C"], color=PURPLE, stroke_width=5)
        
        # Create dots at endpoints
        dots = {}
        for name, point in points.items():
            dots[name] = Dot(point, color=YELLOW, radius=0.08)
        
        # Create labels with numbers
        labels = {
            "A": MathTex("5", font_size=40, color=WHITE).next_to(points["A"], UP, buff=0.2),
            "B": MathTex("10", font_size=40, color=WHITE).next_to(points["B"], UP, buff=0.2),
            "C": MathTex("15", font_size=40, color=WHITE).next_to(points["C"], DOWN, buff=0.2),
            "D": MathTex("20", font_size=40, color=WHITE).next_to(points["D"], DOWN, buff=0.2)
        }
        
        # Animate
        self.play(Create(line_AC_BD), Create(line_BC_AD))
        self.play(*[Create(dot) for dot in dots.values()])
        self.play(*[Write(label) for label in labels.values()])
        self.wait()


class CrossingLinesCoordinates(Scene):
    def construct(self):
        # Example 3: With coordinate labels
        # Create a coordinate system backdrop (optional)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": GREY, "stroke_width": 2},
            tips=False
        )
        axes.set_opacity(0.3)
        
        # Define endpoints with specific coordinates
        p1 = axes.c2p(-3, 2)    # Top left
        p2 = axes.c2p(3, 2)      # Top right
        p3 = axes.c2p(-3, -2)    # Bottom left
        p4 = axes.c2p(3, -2)     # Bottom right
        
        # Create crossing lines
        diagonal1 = Line(p1, p4, color=BLUE_B, stroke_width=6)
        diagonal2 = Line(p2, p3, color=RED_B, stroke_width=6)
        
        # Create coordinate labels
        coord1 = MathTex("(-3, 2)", font_size=28).next_to(p1, UP + LEFT, buff=0.15)
        coord2 = MathTex("(3, 2)", font_size=28).next_to(p2, UP + RIGHT, buff=0.15)
        coord3 = MathTex("(-3, -2)", font_size=28).next_to(p3, DOWN + LEFT, buff=0.15)
        coord4 = MathTex("(3, -2)", font_size=28).next_to(p4, DOWN + RIGHT, buff=0.15)
        
        # Find and mark intersection point
        intersection = diagonal1.get_center()  # For symmetric diagonals, center is intersection
        intersection_dot = Dot(intersection, color=YELLOW, radius=0.1)
        intersection_label = MathTex("(0, 0)", font_size=28, color=YELLOW).next_to(intersection, UR, buff=0.2)
        
        # Animate
        self.play(FadeIn(axes))
        self.play(Create(diagonal1), Create(diagonal2))
        self.play(
            Write(coord1), Write(coord2), 
            Write(coord3), Write(coord4)
        )
        self.play(Create(intersection_dot), Write(intersection_label))
        self.wait()


class AnimatedCrossingLines(Scene):
    def construct(self):
        # Example 4: Animated version with moving numbers
        # Define corners
        corners = [
            UP * 2 + LEFT * 2,      # Top left
            UP * 2 + RIGHT * 2,     # Top right
            DOWN * 2 + LEFT * 2,    # Bottom left
            DOWN * 2 + RIGHT * 2    # Bottom right
        ]
        
        # Create lines
        line1 = Line(corners[0], corners[3], color=TEAL, stroke_width=5)
        line2 = Line(corners[1], corners[2], color=ORANGE, stroke_width=5)
        
        # Create number labels that will move
        numbers = []
        values = [42, 17, 89, 63]
        
        for i, (corner, value) in enumerate(zip(corners, values)):
            # Create number at center first
            num = MathTex(str(value), font_size=48, color=WHITE)
            num.move_to(ORIGIN)
            numbers.append(num)
            
            # Create target position
            if i < 2:  # Top corners
                target = corner + UP * 0.3
            else:  # Bottom corners
                target = corner + DOWN * 0.3
        
        # Animate
        # First show the numbers at center
        self.play(*[FadeIn(num) for num in numbers])
        self.wait(0.5)
        
        # Move numbers to corners while drawing lines
        self.play(
            Create(line1),
            Create(line2),
            numbers[0].animate.move_to(corners[0] + UP * 0.3 + LEFT * 0.3),
            numbers[1].animate.move_to(corners[1] + UP * 0.3 + RIGHT * 0.3),
            numbers[2].animate.move_to(corners[2] + DOWN * 0.3 + LEFT * 0.3),
            numbers[3].animate.move_to(corners[3] + DOWN * 0.3 + RIGHT * 0.3),
            run_time=2
        )
        
        # Highlight intersection
        intersection_dot = Dot(ORIGIN, color=YELLOW, radius=0.12)
        self.play(Create(intersection_dot))
        self.play(intersection_dot.animate.scale(1.5).set_opacity(0.5))
        self.play(intersection_dot.animate.scale(2/3).set_opacity(1))
        
        self.wait()


class CustomStyledCrossingLines(Scene):
    def construct(self):
        # Example 5: Custom styled with background and effects
        # Create background rectangle
        bg_rect = Rectangle(width=6, height=4.5, fill_opacity=0.1, fill_color=BLUE)
        
        # Define endpoints relative to rectangle
        tl = bg_rect.get_corner(UL)
        tr = bg_rect.get_corner(UR)
        bl = bg_rect.get_corner(DL)
        br = bg_rect.get_corner(DR)
        
        # Create dashed crossing lines
        line1 = DashedLine(tl, br, color=BLUE_C, stroke_width=4, dash_length=0.2)
        line2 = DashedLine(tr, bl, color=RED_C, stroke_width=4, dash_length=0.2)
        
        # Create circular backgrounds for numbers
        num_data = [
            (tl, "12", UL),
            (tr, "24", UR),
            (bl, "36", DL),
            (br, "48", DR)
        ]
        
        num_groups = []
        for pos, value, direction in num_data:
            # Create circle background
            circle = Circle(radius=0.3, fill_opacity=0.8, fill_color=DARK_GREY, stroke_color=WHITE)
            circle.next_to(pos, direction, buff=0)
            
            # Create number
            num = MathTex(value, font_size=32, color=WHITE)
            num.move_to(circle.get_center())
            
            num_groups.append(VGroup(circle, num))
        
        # Animate with style
        self.play(FadeIn(bg_rect))
        self.play(Create(line1), Create(line2), lag_ratio=0.5)
        self.play(*[FadeIn(group) for group in num_groups], lag_ratio=0.2)
        
        # Add intersection highlight
        intersection = line1.get_center()
        flash = Flash(intersection, color=YELLOW, flash_radius=0.5)
        self.play(flash)
        
        self.wait()


# To render any of these examples:
# manim -pql crossing_lines.py CrossingLines
# manim -pql crossing_lines.py CrossingLinesWithDots
# manim -pql crossing_lines.py CrossingLinesCoordinates
# manim -pql crossing_lines.py AnimatedCrossingLines
# manim -pql crossing_lines.py CustomStyledCrossingLines