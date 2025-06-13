from manim import *

# Configure for 9:16 ratio (vertical video)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 8.0
config.frame_width = 4.5

class BasicVerticalScene(Scene):
    def construct(self):
        # Create a circle at the top
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.5)
        circle.shift(UP * 2.5)
        
        # Create a square in the middle
        square = Square(side_length=2, color=RED, fill_opacity=0.5)
        # No shift needed - it's at the center by default
        
        # Create text at the bottom
        text = Text("9:16 Ratio Demo", font_size=36, color=GREEN)
        text.shift(DOWN * 2.5)
        
        # Add a title at the very top
        title = Text("Vertical Video", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(
            FadeIn(circle, shift=DOWN),
            run_time=1.5
        )
        
        self.play(
            SpinInFromNothing(square),
            run_time=1.5
        )
        
        self.play(
            Write(text),
            run_time=1.5
        )
        
        # Fun animations
        self.play(
            Rotate(circle, angle=2*PI),
            Rotate(square, angle=-2*PI),
            text.animate.scale(1.2).set_color(YELLOW),
            run_time=2
        )
        
        self.wait(1)
        
        # Final animation
        self.play(
            FadeOut(circle, shift=UP),
            FadeOut(square, scale=0.5),
            FadeOut(text, shift=DOWN),
            FadeOut(title),
            run_time=1.5
        )
        
        self.wait(0.5)