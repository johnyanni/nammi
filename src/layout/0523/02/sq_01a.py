from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"



        

class SQ1(MathTutorialScene):

    def construct(self):
        
        example = VGroup(
            MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE),
            MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        example[0][0][:2].set_color(YELLOW)
        example[1][0][:2].set_color(GREEN)
        
        #self.find_element("c^2", example[0], color=RED, as_group=True)
        
        
        
        formula = MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE)
        formula[0][:2].set_color(YELLOW)
        formula[0][3:5].set_color(GREEN)
        formula[0][6:].set_color(RED)
        
        formula_c2_equals = self.find_element("c^2 =", formula)
        
        
        substitute = MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        substitute[0][:2].set_color(YELLOW)
        substitute[0][3:5].set_color(GREEN)
        substitute[0][6:].set_color(RED)
        
        
        calculation_step1 = MathTex(r"c^2 = 25 + 100").scale(MATH_SCALE)
        calculation_step1[0][:2].set_color(YELLOW)
        calculation_step1[0][3:5].set_color(GREEN)
        calculation_step1[0][6:].set_color(RED)
        
        calculation_step2 = MathTex(r"c^2 = 125", color=YELLOW).scale(MATH_SCALE)
        
        solve_step = MathTex(r"c = \sqrt{125} = 5\sqrt{5}").scale(MATH_SCALE)
        solve_step[0][:2].set_color(YELLOW)
        solve_step[0][2:4].set_color(GREEN)
        solve_step[0][4:7].set_color(RED)
        solve_step[0][7].set_color(BLUE)
        solve_step[0][8].set_color(PINK)
        solve_step[0][9:11].set_color(GREEN)
        solve_step[0][11].set_color(RED)
        
        

        
        result_approx = MathTex(r"c \approx 11.18 \ \text{cm}").scale(MATH_SCALE)
        
        steps = VGroup(example, formula, substitute, calculation_step1, calculation_step2, solve_step, result_approx).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # self.add(steps)

        self.play(Write(formula_c2_equals))
        self.play(Write(formula))
        
        self.play(ReplacementTransform(formula[0][:3].copy(), substitute[0][:3]))
        self.play(ReplacementTransform(formula[0][3].copy(), substitute[0][3]))
        self.play(ReplacementTransform(formula[0][4].copy(), substitute[0][4]))
        self.play(ReplacementTransform(formula[0][5].copy(), substitute[0][5]))
        self.play(ReplacementTransform(formula[0][6:7].copy(), substitute[0][6:8]))
        self.play(ReplacementTransform(formula[0][-1].copy(), substitute[0][-1]))
        
        
        # self.play(ReplacementTransform(formula[0][3:5], substitute[0][3:5]))
        # self.play(ReplacementTransform(formula[0][6:], substitute[0][6:]))
        
        # self.play(ReplacementTransform(substitute[0][:2], calculation_step1[0][:2]))
        # self.play(ReplacementTransform(substitute[0][3:5], calculation_step1[0][3:5]))
        # self.play(ReplacementTransform(substitute[0][6:], calculation_step1[0][6:]))


        
        
        
