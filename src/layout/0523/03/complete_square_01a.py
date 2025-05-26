from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ1(MathTutorialScene):
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
            MathTex(r"c = 11.18 \ \text{cm}", color=YELLOW).scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        self.apply_smart_colorize(
            [step1[1], step2[1], step3[1], step3[2], step4[1], step5[1], step5[0]],
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
        calc4_11_18 = self.find_element(r"11.18 \ \text{cm}", step5[1])
        
        
        # Create elements for ScrollManager
        elements = VGroup(
            step1[0],
            step1[1],# Index 0 - full formula
            
            step2[0],
            sub_c2_equals,     # Index 1
            sub_5,             # Index 2
            sub_5_squared,     # Index 3
            sub_plus,          # Index 4
            sub_10,            # Index 5
            sub_10_squared,    # Index 6
            
            step3[0],
            calc1_c2_equals,   # Index 7
            calc1_25,          # Index 8
            calc1_plus,        # Index 9
            calc1_100,         # Index 10
            
            calc2_c2_equals,   # Index 11
            calc2_125,         # Index 12
            
            step4[0],
            calc3_sqrt,        # Index 13
            calc3_c2,          # Index 14
            calc3_equals,      # Index 15
            calc3_sqrt2,       # Index 16
            calc3_125,         # Index 17
            
            step5[0],
            calc4_c_equals,    # Index 18
            calc4_11_18        # Index 19
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # Step 1: Pythagoras' Theorem
        scroll_mgr.prepare_next(self)  # step1[0] - "Pythagoras' Theorem" label
        scroll_mgr.prepare_next(self)  # step1[1] - full formula
        
        # Step 2: Substitute values
        scroll_mgr.prepare_next(self)  # step2[0] - "Substitute the values" label
        scroll_mgr.transform_from_copy(self, formula_c2_equals)  # sub_c2_equals
        scroll_mgr.transform_from_copy(self, formula_a)  # sub_5
        scroll_mgr.transform_from_copy(self, formula_a_squared)  # sub_5_squared
        scroll_mgr.transform_from_copy(self, formula_plus)  # sub_plus
        scroll_mgr.transform_from_copy(self, formula_b)  # sub_10
        scroll_mgr.transform_from_copy(self, formula_b_squared)  # sub_10_squared
        
        # Step 3: Simplify
        scroll_mgr.prepare_next(self)  # step3[0] - "Simplify" label
        scroll_mgr.transform_from_copy(self, sub_c2_equals)  # calc1_c2_equals
        scroll_mgr.transform_from_copy(self, VGroup(sub_5, sub_5_squared))  # calc1_25
        scroll_mgr.transform_from_copy(self, sub_plus)  # calc1_plus
        scroll_mgr.transform_from_copy(self, VGroup(sub_10, sub_10_squared))  # calc1_100
        
        # Step 3 continued: c^2 = 125
        scroll_mgr.transform_from_copy(self, calc1_c2_equals)  # calc2_c2_equals
        scroll_mgr.transform_from_copy(self, VGroup(calc1_25, calc1_plus, calc1_100))  # calc2_125
        
        scroll_mgr.scroll_down(self, steps=2)
        
        # Step 4: Calculate c
        scroll_mgr.prepare_next(self)  # step4[0] - "Calculate the value of c" label
        scroll_mgr.prepare_next(self)  # calc3_sqrt
        scroll_mgr.transform_from_copy(self, calc2_c2_equals)  # calc3_c2
        scroll_mgr.prepare_next(self)  # calc3_equals
        scroll_mgr.prepare_next(self)  # calc3_sqrt2
        scroll_mgr.transform_from_copy(self, calc2_125)  # calc3_125
        
        scroll_mgr.scroll_down(self, steps=7)
        
        # Step 5: Final result
        scroll_mgr.prepare_next(self)  # step5[0] - "Round to 2 decimal places" label
        scroll_mgr.transform_from_copy(self, calc3_c2)  # calc4_c_equals
        scroll_mgr.transform_from_copy(self, calc3_125)  # calc4_11_18
        