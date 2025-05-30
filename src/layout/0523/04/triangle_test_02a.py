from manim import *
from src.components.common.triangle import Triangle

class TriangleShowcase(Scene):
    def construct(self):
        # Example 1: Basic 3-4-5 triangle
        triangle1 = Triangle(
            a="3",
            b="4",
            c="5",
            unknown="c",  # This would be used in the actual problem solving
            right_angle_position="bottom_left",
            label_scale=0.5,
            triangle_scale=0.6
        )
        t1 = triangle1.triangle().shift(LEFT * 4 + UP * 2)
        
        # Example 2: Triangle with angle
        triangle2 = Triangle(
            a="5",
            b="12",
            c="13",
            alpha=r"22.6^\circ",
            unknown="alpha",
            right_angle_position="bottom_right",
            label_scale=0.5,
            triangle_scale=0.4
        )
        t2 = triangle2.triangle().shift(RIGHT * 2 + UP * 2)
        
        # Example 3: Triangle with both angles
        triangle3 = Triangle(
            a="8",
            b="15",
            c="17",
            alpha=r"\alpha",
            beta=r"\beta",
            unknown="c",
            right_angle_position="top_left",
            label_scale=0.5,
            triangle_scale=0.3
        )
        t3 = triangle3.triangle().shift(LEFT * 4 + DOWN * 2)
        
        # Example 4: Triangle with height
        triangle4 = Triangle(
            a="6",
            b="8",
            c="10",
            h="4.8",
            alpha=r"36.87^\circ",
            unknown="h",
            right_angle_position="perpendicular_foot",
            label_scale=0.5,
            triangle_scale=0.5
        )
        t4 = triangle4.triangle().shift(RIGHT * 2 + DOWN * 2)
        
        # Add all triangles
        self.add(t1, t2, t3, t4)
        
        # Add labels
        self.add(Text("Basic Triangle", font_size=16).next_to(t1, UP))
        self.add(Text("With Angle", font_size=16).next_to(t2, UP))
        self.add(Text("With Variables", font_size=16).next_to(t3, UP))
        self.add(Text("With Height", font_size=16).next_to(t4, UP))
        
        self.wait()


class AnimatedTriangleDemo(Scene):
    def construct(self):
        # Create a triangle that we'll modify
        triangle = Triangle(
            a="a",
            b="b",
            c="c",
            unknown="c",
            right_angle_position="bottom_left",
            label_scale=0.6,
            triangle_scale=1.0,
            indicate_alpha_with_arrow=False,
            indicate_beta_with_arrow=False
        )
        
        # Get the triangle visual
        t = triangle.triangle()
        self.add(t)
        self.wait()
        
        # Create different orientations
        orientations = ["bottom_right", "top_right", "top_left", "bottom_left"]
        
        for orientation in orientations[1:]:
            new_triangle = Triangle(
                a="a",
                b="b",
                c="c",
                unknown="c",
                right_angle_position=orientation,
                label_scale=0.6,
                triangle_scale=1.0,
                indicate_alpha_with_arrow=False,
                indicate_beta_with_arrow=False
            )
            
            self.play(Transform(t, new_triangle.triangle()))
            self.wait(0.5)
        
        self.wait()


class TriangleWithSolution(Scene):
    def construct(self):
        # Create a triangle problem
        triangle = Triangle(
            a=None,  # Unknown
            b="5",
            c="13",
            alpha=r"\theta",
            unknown="a",
            right_angle_position="bottom_left",
            solution_prec=2,
            label_scale=0.6,
            triangle_scale=0.8
        )
        
        # Display the triangle
        t = triangle.triangle()
        t.to_edge(UP)
        self.add(t)
        
        # Get the solution steps
        steps = triangle.get_steps()
        
        # Display solution steps
        step_mobjects = VGroup()
        for i, step in enumerate(steps):
            step_tex = MathTex(step).scale(0.7)
            step_mobjects.add(step_tex)
        
        step_mobjects.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step_mobjects.next_to(t, DOWN, buff=0.5)
        
        # Animate the solution
        for step in step_mobjects:
            self.play(Write(step))
            self.wait(0.5)
        
        # Highlight the final answer
        final_answer_box = SurroundingRectangle(
            step_mobjects[-1], 
            color=YELLOW, 
            buff=0.1
        )
        self.play(Create(final_answer_box))
        
        self.wait(2)


class ExploreTriangleFeatures(Scene):
    def construct(self):
        # Show all the features of the Triangle class
        
        # Feature 1: Color mapping
        triangle1 = Triangle(
            a="3",
            b="4",
            c="5",
            alpha=r"36.87^\circ",
            beta=r"53.13^\circ",
            unknown="c",
            right_angle_position="bottom_left",
            label_scale=0.5,
            triangle_scale=0.6,
            color_map={
                "hyp": GREEN,
                "opp": RED,
                "adj": BLUE,
                "angle": YELLOW,
            }
        )
        
        # Feature 2: With arrows pointing to angles
        triangle2 = Triangle(
            a="a",
            b="b",
            c="c",
            alpha=r"\alpha",
            beta=r"\beta",
            unknown="a",
            indicate_alpha_with_arrow=True,
            indicate_beta_with_arrow=True,
            right_angle_position="bottom_left",
            label_scale=0.5,
            triangle_scale=0.6
        )
        
        t1 = triangle1.triangle().shift(LEFT * 3)
        t2 = triangle2.triangle().shift(RIGHT * 3)
        
        self.add(t1, t2)
        self.add(Text("With Colors", font_size=16).next_to(t1, UP))
        self.add(Text("With Arrows", font_size=16).next_to(t2, UP))
        
        self.wait()