from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class Example01a(MathTutorialScene): 
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        
        sqrt_label = Tex("Simplify the square root:").scale(LABEL_SCALE)
        sqrt_intermediate = MathTex(r"\sqrt{45} = \sqrt{9^2 \times 5} = 3\sqrt{5}").scale(M_MATH_SCALE).set_color(LIGHT_GRAY)
        sqrt_result = MathTex(rf"x = \frac{{3 \pm 3\sqrt{{5^2}}}}{{-2}}").scale(MATH_SCALE)
        
        sqrt_group = VGroup(
            sqrt_label,
            sqrt_intermediate,
            sqrt_result
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        SmartColorizeStatic(sqrt_label, {"Simplify": RED, "r": YELLOW})
        
        # Parse square root simplification elements
        sqrt_parsing = self.parse_elements(sqrt_intermediate,
            ('sqrt_45', r'\sqrt{45}'),
            ('sqrt', r'\sqrt{45}', 0, BLUE, 1, slice(0, 2)),
            ('sqrt_num', r'9', 0, GREEN),
            ('sqrt_power', r'2', 0, RED),
            ('sqrt_45_solved', r'3\sqrt{5}', 0, YELLOW),
        )
        
        SmartColorizeStatic(sqrt_result, {r"5^2": YELLOW})
        
        
        self.add(sqrt_label)
        self.add(sqrt_parsing['sqrt_45'])
        self.add(sqrt_parsing['sqrt'])
        self.add(sqrt_parsing['sqrt_num'])
        self.add(sqrt_parsing['sqrt_power'])
        self.add(sqrt_parsing['sqrt_45_solved'])
        self.add(sqrt_result)

        
        
        
        
        
        