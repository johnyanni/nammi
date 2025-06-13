from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"



class QuadraticFormula01a(MathTutorialScene):
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
       
        
        sol3_step1 = VGroup(
            Tex("Use the quadratic formula to solve for x:").scale(LABEL_SCALE),
            MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        SmartColorizeStatic(sol3_step1[0], {"quad": B_COLOR, "x": C_COLOR, "e": YELLOW})
        
        self.add(sol3_step1[0])
        self.add(sol3_step1[1])