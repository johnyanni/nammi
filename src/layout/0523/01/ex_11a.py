from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        step1 = VGroup(
            Tex("Given").scale(0.6),
            MathTex(r"x=350").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        x_equals = self.find_element("x=", step1[1], color=BLUE, as_group=True)
        step1_350 = self.find_element("350", step1[1], color=RED, as_group=True)
        
        
        step2 = VGroup(
            Tex("Substitute").scale(0.6),
            MathTex(r"y=35+0-5").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        y_equals = self.find_element("-5", step2[1], color=BLUE, as_group=True)
        

        
        steps = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.to_edge(UP, buff=0.5)
        
        self.add(steps)


        self.wait(1)
        
        self.play(Write(y_equals))
        
        