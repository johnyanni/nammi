"""Tutorial on graphing linear equations using slope-intercept form."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.styles.constants import *

from manim import *

class TestIndicesWithLabels(Scene):
    def construct(self):
        # Create the MathTex expression
        expr = MathTex(r"m = \frac{-4}{1}")
        expr.scale(1.5)  # Make it bigger for better visibility
        
        # Get the number of submobjects
        n_parts = len(expr[0])
        print(f"Number of submobjects in expr[0]: {n_parts}")
        
        # Add tiny numbered labels to each part
        labels = VGroup()
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK]
        
        for i in range(n_parts):
            # Color the part
            expr[0][i].set_color(colors[i % len(colors)])
            
            # Create a small label with the index
            label = Text(str(i), font_size=16, color=WHITE)
            
            # Position it above the part
            label.next_to(expr[0][i], UP, buff=0.1)
            
            # Add a small circle around it for better visibility
            circle = Circle(radius=0.15, color=colors[i % len(colors)])
            circle.set_fill(BLACK, opacity=0.8)
            circle.move_to(label)
            
            # Group the label and circle
            label_group = VGroup(circle, label)
            labels.add(label_group)
        
        # Show the expression and labels
        self.add(expr, labels)
        self.wait(1)
        
        # Highlight each part sequentially with its index
        for i in range(n_parts):
            # Create annotation text
            annotation = Text(f"Index {i}", font_size=24)
            annotation.to_edge(DOWN, buff=0.5)
            
            self.play(
                Indicate(expr[0][i], scale_factor=1.5),
                FadeIn(annotation)
            )
            self.wait(0.5)
            self.play(FadeOut(annotation))
        