from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        random_formula = MathTex(r"\frac{350}{450}").scale(MATH_SCALE)
        random_formula.to_edge(LEFT)
        
        
        random_formula_2 = self.find_element(r"\frac{350}{450}", random_formula, color=RED)
        
        
        # self.show_indices(random_formula)
        
        #self.play(Write(random_formula_2))
        
        # Animate sequentially
        # self.play(Write(numerator))
        # self.play(Write(frac_bar))
        # self.play(Write(denominator))
        
        elements = VGroup(
            random_formula_2[0:3],
            random_formula_2[4:7],
            random_formula_2[3]
        )
        
        scroll_mgr = ScrollManager(elements)
        
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        
        
        
        
        
        