from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip

config.verbosity = "ERROR"

class QuadraticFormula02a(MathTutorialScene):
    def construct(self):

            
            
        factor_equation = MathTex(
            rf"x = \frac{{2(-5 \pm 2\sqrt{{3}})}}{{2}} = -5 \pm 2\sqrt{{3}}")
        
        self.add(factor_equation)