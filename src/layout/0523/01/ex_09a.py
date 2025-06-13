from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        # step1 = VGroup(
        #     Tex("Given").scale(0.6),
        #     MathTex(r"x=\frac{350^2}{x}").scale(TEX_SCALE)
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # step1_350 = self.find_element("350^2", step1[1], color=RED)
        
        # step2 = VGroup(
        #     Tex("Substitute").scale(0.6),
        #     MathTex(r"y=35 + 0").scale(TEX_SCALE)
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # step2_350 = self.find_element("35 + 0", step2[1], color=GREEN)
        
        
        # steps = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        # steps.to_edge(UP, buff=0.5)
        
        # self.play(Write(step1[0]))
        # self.play(Write(step1[1]))
        # self.play(Write(step2[0]))
        # self.play(ReplacementTransform(step1[1].copy(), step2[1]))
        
        

        # show_formula_equation = MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        
        # part1 = self.find_element("b", show_formula_equation, nth=1, color=RED)
        # self.add(part1)
        
        
        test = MathTex(r"x = 5^{3+5}").scale(MATH_SCALE)
        
        part55 = self.find_element(r"3", test, color=YELLOW)
        self.play(Write(test))
        self.add(part55)
        
        # simplify2_label = Tex("Continue simplifying:").scale(LABEL_SCALE)
        # simplify2_equation = MathTex(
        #     rf"x = \frac{{3^2 \pm \sqrt{{45}}}}{{-2}}"
        # ).scale(MATH_SCALE)
        
        # simplify2_step = VGroup(
        #     simplify2_label,
        #     simplify2_equation
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # example = MathTex(r"x = 3x^2 + 3^2 + b^2 = 500").scale(MATH_SCALE).next_to(simplify2_equation, RIGHT, buff=1)
        
        # self.play(Write(simplify2_label))
        # self.play(Write(simplify2_equation))
        
        # self.play(Write(example))
        
        
        # simplify2_sqrt = self.parse_elements(simplify2_equation,
        #     ('sqrt_45', r"\sqrt{45}")
        # )
        
        # part2 = self.find_element(r"3^2", simplify2_equation, color=RED)
        # self.add(part2)
        
        
        # example = MathTex(r"x = 3x^2 + 3^2 + b^2").scale(MATH_SCALE)
        
        # part3 = self.find_element("b^2", example, color=RED)
        # self.add(part3)



        
        
        
        
        