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
            MathTex(r"y=35 + 0").scale(TEX_SCALE),
            self.create_annotated_equation(
                r"5 + y = 35 + 0 + 5",
                "-5", 
                "5",
                "5",
                nth_to=-1, 
                color=GREEN
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        y_equals = self.find_element("y=", step2[1], color=BLUE, as_group=True)
        step2_350 = self.find_element("35 + 0", step2[1], color=GREEN, as_group=True)
        
        step3 = VGroup(
            Tex("Simplify").scale(0.6),
            MathTex(r"y=35").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        step3_35 = self.find_element("35", step3[1], color=GREEN, as_group=True)
        
        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.to_edge(UP, buff=0.5)
        
        elements = VGroup(
            step1[0],
            x_equals,
            step1_350,
            step2[0],
            y_equals,
            step2_350,
            step2[2],
            step2[2],
            step3[0],
            step3_35,
        )
        
        
        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        

        #scroll_mgr.transform_between(self, 2, 5)
        
        self.play(ReplacementTransform(step1_350.copy(), step2_350))
        scroll_mgr.current_position += 1  # Skip showing step2_350 normally
        
        scroll_mgr.prepare_next(self)
        
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)