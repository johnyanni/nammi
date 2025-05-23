from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        
        
        step1 = VGroup(
            Tex("Given Equation").scale(0.6),
            MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE),
            VGroup(
                MathTex("a = 1", color=RED).scale(TEX_SCALE),
                MathTex("b = 10", color=BLUE).scale(TEX_SCALE),
                MathTex("c = 13", color=GREEN).scale(TEX_SCALE)
            ).arrange(RIGHT, buff=0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        a_in_q_equation = self.find_element("1", step1[1], color=RED)  # Coefficient of x²
        b_in_q_equation = self.find_element("10", step1[1], color=BLUE)      
        c_in_q_equation = self.find_element("13", step1[1], color=GREEN)    
        
        a_label = self.find_element("a =", step1[2][0], as_group=True)
        b_label = self.find_element("b =", step1[2][1], as_group=True)
        c_label = self.find_element("c =", step1[2][2], as_group=True) 
        coefficient_labels = VGroup(a_label, b_label, c_label)

        # Extract coefficient values
        a_value = self.find_element("1", step1[2][0])
        b_value = self.find_element("10", step1[2][1])
        c_value = self.find_element("13", step1[2][2])
        coefficient_values = VGroup(a_value, b_value, c_value)
        
        
        
        elements = VGroup(
            step1[0],
            step1[1],
            *coefficient_labels,
            *coefficient_values
        )
        
        print(f"Total elements after unpacking: {len(elements)}")
        for i, elem in enumerate(elements):
            print(f"  Element {i}: {type(elem).__name__}")
            if hasattr(elem, 'tex_string'):
                print(f"    Content: {elem.tex_string}")
        
        
        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  #shows step1[1]
        
        scroll_mgr.prepare_next(self, steps=3)

        scroll_mgr.fade_in_from_target(self, a_in_q_equation)  # Fades in a_value from quad_form_a

        scroll_mgr.fade_in_from_target(self, b_in_q_equation)  # Fades in b_value from quad_form_b

        scroll_mgr.fade_in_from_target(self, c_in_q_equation)  # Fades in c_value from quad_form_c
        
        


        


        
    



    
