from manim import *
from src.components.common.base_scene import *
import numpy as np


class PythagoreanTheorem(MathTutorialScene):
    def construct(self):
        # Define high-contrast colors for visual clarity
        LEG_A_COLOR = BLUE      # 4 cm leg - bright blue
        LEG_B_COLOR = GREEN     # 6 cm leg - bright green  
        HYPOTENUSE_COLOR = RED  # hypotenuse - bright red
        TEXT_COLOR = WHITE      # labels - white for contrast
        
        # Colors for individual values in the solution
        VALUE_4_COLOR = BLUE
        VALUE_6_COLOR = GREEN
        VALUE_16_COLOR = PINK
        VALUE_36_COLOR = PURPLE
        VALUE_52_COLOR = YELLOW
        VALUE_RESULT_COLOR = RED
        
     
        
        # Step 2: Show Pythagorean theorem formula
        theorem_text = MathTex(
            r"{{a^2}} + {{b^2}} = {{c^2}}",
            font_size=36
        )
        theorem_text.to_edge(UP, buff=0.5)
        
        self.play(Write(theorem_text), run_time=2)
        self.wait(1)
        
        # Step 3: Substitute values with color coding
        substitution = MathTex(
            r"4^2 + 6^2 = c^2",
            font_size=36
        )
        substitution.move_to(theorem_text.get_center() + DOWN * 0.8)
        
        # Color code the values
        # substitution[0].set_color(VALUE_4_COLOR)
        # substitution[2].set_color(VALUE_6_COLOR)
        
        substitution_6 = self.find_element("6^2", substitution)
        
        self.play(Write(substitution_6))       
        
        
        # self.play(ReplacementTransform(theorem_text[0], substitution[0]))
        # self.play(ReplacementTransform(theorem_text[2], substitution[2]))

        
        
        # Step 4: Calculate squares with color coding
        calculation = MathTex(
            r"{{16}} + {{36}} = c^2",
            font_size=36
        )
        calculation.move_to(substitution.get_center() + DOWN * 0.8)
        
        # Color code the squared values
        calculation[0].set_color(VALUE_16_COLOR)
        calculation[2].set_color(VALUE_36_COLOR)
        
        self.play(Write(calculation), run_time=1.5)
        self.wait(1)
        
        # Step 5: Add the squares
        sum_result = MathTex(
            r"{{52}} = c^2",
            font_size=36
        )
        sum_result.move_to(calculation.get_center() + DOWN * 0.8)
        sum_result[0].set_color(VALUE_52_COLOR)
        
   

# To render this animation, save this file and run:
# manim -pql pythagorean_theorem.py PythagoreanTheorem
# Where:
#   -p : preview after rendering
#   -q : quality (l=low, m=medium, h=high)
#   -l : low quality for faster rendering during development