from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class Pythagoras01a(MathTutorialScene):
    def construct(self):
        
        step1 = VGroup(
            Tex("Pythagoras' Theorem").scale(TEXT_SCALE),
            MathTex("c^2 = a^2 + b^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        step2 = VGroup(
            Tex("Substitute the values of a and b").scale(TEXT_SCALE),
            MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step3 = VGroup(
            Tex("Simplify").scale(TEXT_SCALE),
            MathTex(r"c^2 = 25 + 100").scale(MATH_SCALE),
            MathTex(r"c^2 = 125").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step4 = VGroup(
            Tex("Calculate the value of c").scale(TEXT_SCALE),
            MathTex(r"\sqrt{c^2} = \sqrt{125}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step5 = VGroup(
            Tex("Round to 2 decimal places testing: $a^2 + b^2 = c^2$").scale(TEXT_SCALE),
            MathTex(r"c = 11.18 \ \text{cm}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        self.apply_smart_colorize(
            [step1[1], step2[1], step3[1], step3[2], step4[1], step5[1]],
            {
                "c": YELLOW,
                "a^2": GREEN,
                "b^2": RED,
                "c^2": YELLOW,
                "5^2": GREEN,
                "10^2": RED,
                "25": GREEN,
                "100": RED,
                "125": YELLOW,
                "11.18": YELLOW,
            }
        )
        
        # Position formulas
        main = VGroup(step1, step2, step3, step4, step5).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)
        

        formula_c2_equals = self.find_element("c^2 =", step1[1])
        formula_a = self.find_element("a", step1[1])
        formula_a_squared = self.find_element("^2", step1[1], nth=1)
        formula_plus = self.find_element("+", step1[1])
        formula_b = self.find_element("b", step1[1])
        formula_b_squared = self.find_element("^2", step1[1], nth=2)
        
   
        sub_c2_equals = self.find_element("c^2 =", step2[1])
        sub_5 = self.find_element("5", step2[1])
        sub_5_squared = self.find_element("^2", step2[1], nth=1)
        sub_plus = self.find_element("+", step2[1])
        sub_10 = self.find_element("10", step2[1])
        sub_10_squared = self.find_element("^2", step2[1], nth=2)
        
        
        calc1_c2_equals = self.find_element("c^2 =", step3[1])
        calc1_25 = self.find_element("25", step3[1])
        calc1_plus = self.find_element("+", step3[1])
        calc1_100 = self.find_element("100", step3[1])
        
        calc2_c2_equals = self.find_element("c^2 =", step3[2])
        calc2_125 = self.find_element("125", step3[2])
        
        calc3_sqrt = step4[1][0][0:2]
        calc3_c2 = step4[1][0][2:4].set_color(YELLOW)
        calc3_equals = self.find_element("=", step4[1])
        calc3_sqrt2 = step4[1][0][5:7]
        calc3_125 = self.find_element("125", step4[1])
        
        calc4_c_equals = self.find_element("c =", step5[1])
        calc4_11_18 = self.find_element(r"11.18 \ \text{cm}", step5[1], color=YELLOW)
        
        
        # Create elements for ScrollManager
        elements = VGroup(
            step1[0],
            step1[1],
            
            step2[0],
            sub_c2_equals,
            sub_5,
            sub_5_squared,
            sub_plus,
            sub_10,
            sub_10_squared,
            
            step3[0],
            calc1_c2_equals,
            calc1_25,
            calc1_plus,
            calc1_100,
            
            calc2_c2_equals,
            calc2_125,
            
            step4[0],
            calc3_sqrt,
            calc3_c2,
            calc3_equals,
            calc3_sqrt2,
            calc3_125,
            
            step5[0],
            calc4_c_equals,
            calc4_11_18
        )
        
        # Create scroll manager with scene reference
        scroll_mgr = ScrollManager(elements, scene=self)
        
        # Step 1: Pythagoras' Theorem
        scroll_mgr.prepare_next()  # step1[0] - "Pythagoras' Theorem" label
        scroll_mgr.prepare_next()  # step1[1] - full formula
        
        # Step 2: Substitute values - CLEAN SYNTAX
        scroll_mgr.prepare_next()  # step2[0] - "Substitute the values" label
        scroll_mgr.transform_from_copy(formula_c2_equals, sub_c2_equals)
        scroll_mgr.transform_from_copy(formula_a, sub_5)
        scroll_mgr.transform_from_copy(formula_a_squared, sub_5_squared)
        scroll_mgr.transform_from_copy(formula_plus, sub_plus)
        scroll_mgr.transform_from_copy(formula_b, sub_10)
        scroll_mgr.transform_from_copy(formula_b_squared, sub_10_squared)
        
        # Step 3: Simplify - CLEAN SYNTAX
        scroll_mgr.prepare_next()  # step3[0] - "Simplify" label
        scroll_mgr.transform_from_copy(sub_c2_equals, calc1_c2_equals)
        scroll_mgr.transform_from_copy(VGroup(sub_5, sub_5_squared), calc1_25)
        scroll_mgr.transform_from_copy(sub_plus, calc1_plus)
        scroll_mgr.transform_from_copy(VGroup(sub_10, sub_10_squared), calc1_100)
        
        # Step 3 continued: c^2 = 125
        scroll_mgr.transform_from_copy(calc1_c2_equals, calc2_c2_equals)
        scroll_mgr.transform_from_copy(VGroup(calc1_25, calc1_plus, calc1_100), calc2_125)
        
        scroll_mgr.scroll_down(steps=2)
        
        # Step 4: Calculate c
        scroll_mgr.prepare_next()  # step4[0] - "Calculate the value of c" label
        scroll_mgr.prepare_next()  # calc3_sqrt
        scroll_mgr.transform_from_copy(calc2_c2_equals, calc3_c2)
        scroll_mgr.prepare_next()  # calc3_equals
        scroll_mgr.prepare_next()  # calc3_sqrt2
        scroll_mgr.transform_from_copy(calc2_125, calc3_125)
        
        scroll_mgr.scroll_down(steps=7)
        
        # Step 5: Final result
        scroll_mgr.prepare_next()  # step5[0] - "Round to 2 decimal places" label
        scroll_mgr.transform_from_copy(calc3_c2, calc4_c_equals)
        scroll_mgr.transform_from_copy(calc3_125, calc4_11_18)
        
        
        
        