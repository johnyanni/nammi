from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        step1 = VGroup(
            Tex("Given").scale(0.6),
            MathTex(r"\text{adjacent} = 6").scale(TEX_SCALE),
            MathTex(r"\text{hypotenuse} = 10").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        adjacent_value = self.find_element("6", step1[1], color=BLUE)
        hypotenuse_value = self.find_element("10", step1[2], color=RED)
        

                
        step2 = VGroup(
            Tex("Cos Ratio").scale(0.6),
            MathTex(r"x = \frac{adj}{hyp}").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        
        adjacent = self.find_element("adj", step2[1], color=BLUE)
        hypotenuse = self.find_element("hyp", step2[1], color=RED)
        
        
        
        
        
        step3 = VGroup(
            Tex("Substitute").scale(0.6),
            MathTex(r"x = \frac{6}{10}").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        step3_adj = self.find_element("6", step3[1], color=BLUE)
        step3_hyp = self.find_element("10", step3[1], color=RED)
        
        
        
        
        self.apply_smart_colorize(
            [step1[1], step1[2], step2[1], step3[1]],
            {
                "adjacent": BLUE,
                "hypotenuse": RED,
                "x": GREEN,
                "6": BLUE,
                "10": RED
            }
        )


        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.to_edge(UP, buff=0.5)

        
        elements = VGroup(
            step1[0],
            step1[1],
            step1[2],
            step2[0],
            step2[1],
            step3[0],
            step3_adj,
            step3_hyp,
        )
        
        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        
        
        scroll_mgr.fade_in_from_target(self, adjacent_value)
        scroll_mgr.fade_in_from_target(self, hypotenuse_value)
        
        





    
