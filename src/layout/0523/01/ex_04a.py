from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        
        
        
        

        
        step1_label = Tex("Given Equation").scale(0.6)
        step1_exp = MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)
        
        a_in_q_equation = self.find_element("1", step1_exp, color=RED)  # Coefficient of x²
        b_in_q_equation = self.find_element("10", step1_exp, color=BLUE)      
        c_in_q_equation = self.find_element("13", step1_exp, color=GREEN)    
        
         # Create coefficient labels
        a = MathTex("a = 1", color=RED).scale(TEX_SCALE)
        b = MathTex("b = 10", color=BLUE).scale(TEX_SCALE)
        c = MathTex("c = 13", color=GREEN).scale(TEX_SCALE)
        coefficients = VGroup(a, b, c).arrange(RIGHT, buff=0.6)
        
        a_label = self.find_element("a =", a, as_group=True)
        b_label = self.find_element("b =", b, as_group=True)
        c_label = self.find_element("c =", c, as_group=True) 
        coefficient_labels = VGroup(a_label, b_label, c_label)

        # Extract coefficient values
        a_value = self.find_element("1", a)
        b_value = self.find_element("10", b)
        c_value = self.find_element("13", c)
        coefficient_values = VGroup(a_value, b_value, c_value)

        
        step1 = VGroup(
            step1_label,
            step1_exp,
            coefficients
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        
        
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
        
        


        


        
    



    
