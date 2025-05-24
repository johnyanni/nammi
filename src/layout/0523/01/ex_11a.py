from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        x_equals = self.find_element("x=", step1[1], color=BLUE)
        step1_350 = self.find_element("350", step1[1], color=RED)
        
        step1 = VGroup(
            Tex("Given").scale(0.6),
            MathTex(r"x=350").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        
        
        step2 = VGroup(
            Tex("Substitute").scale(0.6),
            MathTex(r"y=35+0-5").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        y_equals = self.find_element("-5", step2[1], color=BLUE)
        

        
        steps = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.to_edge(UP, buff=0.5)
        
        # self.add(steps)


        elements = VGroup(
            step1[0],
            x_equals,
            step1_350,
            step2[0],
            y_equals,
        )
        
        self.wait(1)
        
        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        
        # self.play(Write(x_equals))
        # self.play(Write(step1_350))
        
        # self.play(Write(y_equals))
        
        