from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ2(MathTutorialScene):
    def construct(self):
        
        # Step 1: Original formula
        step1 = VGroup(
            Tex("Pythagoras' Theorem").scale(TEXT_SCALE),
            MathTex("c^2 = a^2 + b^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 2: Rearrange to solve for b
        step2 = VGroup(
            Tex("Rearrange to solve for b").scale(TEXT_SCALE),
            MathTex(r"b^2 = c^2 - a^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 3: Substitute values (c=169, a=120)
        step3 = VGroup(
            Tex("Substitute c = 169 and a = 120").scale(TEXT_SCALE),
            MathTex(r"b^2 = 169^2 - 120^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 4: Calculate squares
        step4 = VGroup(
            Tex("Calculate the squares").scale(TEXT_SCALE),
            MathTex(r"b^2 = 28561 - 14400").scale(MATH_SCALE),
            MathTex(r"b^2 = 14161").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 5: Find square root
        step5 = VGroup(
            Tex("Calculate the value of b").scale(TEXT_SCALE),
            MathTex(r"\sqrt{b^2} = \sqrt{14161}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 6: Final answer
        step6 = VGroup(
            Tex("Final answer").scale(TEXT_SCALE),
            MathTex(r"b = 119 \ \text{cm}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Apply colors
        self.apply_smart_colorize(
            [step1[1], step2[1], step3[1], step4[1], step4[2], step5[1], step6[1]],
            {
                "c": RED,
                "a": GREEN,
                "b": BLUE,
                "c^2": RED,
                "a^2": GREEN,
                "b^2": BLUE,
                "169": RED,
                "120": GREEN,
                "119": BLUE,
                "169^2": RED,
                "120^2": GREEN,
                "28561": RED,
                "14400": GREEN,
                "14161": BLUE,
            }
        )
        
        # Position formulas
        main = VGroup(step1, step2, step3, step4, step5, step6).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(UP, buff=0.3).to_edge(LEFT, buff=1)
        
        self.show_flattened_indices(*step1, *step2, *step3, *step4, *step5, *step6)
        
        # Find elements - Step 1 (original formula)
        formula_c2 = self.find_element("c^2", step1[1])
        formula_equals1 = self.find_element("=", step1[1])
        formula_a2 = self.find_element("a^2", step1[1])
        formula_plus = self.find_element("+", step1[1])
        formula_b2 = self.find_element("b^2", step1[1])
        
        # Step 2 (rearranged)
        rearr_b2 = self.find_element("b^2", step2[1])
        rearr_equals = self.find_element("=", step2[1])
        rearr_c2 = self.find_element("c^2", step2[1])
        rearr_minus = self.find_element("-", step2[1])
        rearr_a2 = self.find_element("a^2", step2[1])
        
        # Step 3 (substituted values)
        sub_b2_equals = self.find_element("b^2 =", step3[1])
        sub_169 = self.find_element("169", step3[1])
        sub_169_squared = self.find_element("^2", step3[1], nth=1)
        sub_minus = self.find_element("-", step3[1])
        sub_120 = self.find_element("120", step3[1])
        sub_120_squared = self.find_element("^2", step3[1], nth=2)
        
        # Step 4 (calculated squares)
        calc1_b2_equals = self.find_element("b^2 =", step4[1])
        calc1_28561 = self.find_element("28561", step4[1])
        calc1_minus = self.find_element("-", step4[1])
        calc1_14400 = self.find_element("14400", step4[1])
        
        calc2_b2_equals = self.find_element("b^2 =", step4[2])
        calc2_14161 = self.find_element("14161", step4[2])
        
        # Step 5 (square root)
        calc3_sqrt = step5[1][0][0:2]  # sqrt symbol and bar
        calc3_b2 = step5[1][0][2:5]    # b^2
        calc3_equals = self.find_element("=", step5[1])
        calc3_sqrt2 = step5[1][0][5:7]  # second sqrt
        calc3_14161 = self.find_element("14161", step5[1])
        
        # Step 6 (final answer)
        final_b_equals = self.find_element("b =", step6[1])
        final_119_cm = step6[1][0][2:]  # "119 cm" - using slicing for text
        
        # Create elements for ScrollManager
        elements = VGroup(
            # Step 1 - Original formula
            step1[0],              # Index 0: "Pythagoras' Theorem"
            step1[1],              # Index 1: c^2 = a^2 + b^2
            
            # Step 2 - Rearranged formula
            step2[0],              # Index 2: "Rearrange to solve for b"
            rearr_b2,              # Index 3: b^2
            rearr_equals,          # Index 4: =
            rearr_c2,              # Index 5: c^2
            rearr_minus,           # Index 6: -
            rearr_a2,              # Index 7: a^2
            
            # Step 3 - Substituted values
            step3[0],              # Index 8: "Substitute c = 169 and a = 120"
            sub_b2_equals,         # Index 9: b^2 =
            sub_169,               # Index 10: 169
            sub_169_squared,       # Index 11: ^2
            sub_minus,             # Index 12: -
            sub_120,               # Index 13: 120
            sub_120_squared,       # Index 14: ^2
            
            # Step 4 - Calculated squares
            step4[0],              # Index 15: "Calculate the squares"
            calc1_b2_equals,       # Index 16: b^2 =
            calc1_28561,           # Index 17: 28561
            calc1_minus,           # Index 18: -
            calc1_14400,           # Index 19: 14400
            
            calc2_b2_equals,       # Index 20: b^2 =
            calc2_14161,           # Index 21: 14161
            
            # Step 5 - Square root
            step5[0],              # Index 22: "Calculate the value of b"
            calc3_sqrt,            # Index 23: sqrt symbol
            calc3_b2,              # Index 24: b^2
            calc3_equals,          # Index 25: =
            calc3_sqrt2,           # Index 26: sqrt symbol
            calc3_14161,           # Index 27: 14161
            
            # Step 6 - Final answer
            step6[0],              # Index 28: "Final answer"
            final_b_equals,        # Index 29: b =
            final_119_cm           # Index 30: 119 cm
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # Animate Step 1: Original formula
        scroll_mgr.prepare_next(self)  # Index 0: step1[0] - "Pythagoras' Theorem"
        scroll_mgr.prepare_next(self)  # Index 1: step1[1] - c^2 = a^2 + b^2
        
        # Animate Step 2: Rearrange
        scroll_mgr.prepare_next(self)  # Index 2: step2[0] - "Rearrange to solve for b"
        scroll_mgr.transform_from_copy(self, formula_b2)      # Index 3: rearr_b2
        scroll_mgr.transform_from_copy(self, formula_equals1) # Index 4: rearr_equals
        scroll_mgr.transform_from_copy(self, formula_c2)      # Index 5: rearr_c2
        scroll_mgr.fade_in_from_target(self, formula_plus)    # Index 6: rearr_minus
        scroll_mgr.transform_from_copy(self, formula_a2)      # Index 7: rearr_a2
        
        # Animate Step 3: Substitute values
        scroll_mgr.prepare_next(self)  # Index 8: step3[0] - "Substitute c = 169 and a = 120"
        scroll_mgr.transform_from_copy(self, rearr_b2)        # Index 9: sub_b2_equals
        scroll_mgr.transform_from_copy(self, rearr_c2)        # Index 10: sub_169
        scroll_mgr.fade_in_from_target(self, rearr_c2)        # Index 11: sub_169_squared
        scroll_mgr.transform_from_copy(self, rearr_minus)     # Index 12: sub_minus
        scroll_mgr.fade_in_from_target(self, rearr_a2)        # Index 13: sub_120
        scroll_mgr.fade_in_from_target(self, rearr_a2)        # Index 14: sub_120_squared
        
        # Animate Step 4: Calculate squares
        scroll_mgr.prepare_next(self)  # Index 15: step4[0] - "Calculate the squares"
        scroll_mgr.transform_from_copy(self, sub_b2_equals)                    # Index 16: calc1_b2_equals
        scroll_mgr.transform_from_copy(self, VGroup(sub_169, sub_169_squared)) # Index 17: calc1_28561
        scroll_mgr.transform_from_copy(self, sub_minus)                        # Index 18: calc1_minus
        scroll_mgr.transform_from_copy(self, sub_120)                          # Index 19: calc1_14400
        
        # Continue Step 4: b^2 = 14161
        scroll_mgr.transform_from_copy(self, calc1_b2_equals)  # Index 20: calc2_b2_equals
        scroll_mgr.transform_from_copy(self, VGroup(calc1_28561, calc1_minus, calc1_14400))  # Index 21: calc2_14161
        
        # Scroll if needed
        scroll_mgr.scroll_down(self, steps=2)
        
        # Animate Step 5: Square root
        scroll_mgr.prepare_next(self)  # Index 22: step5[0] - "Calculate the value of b"
        scroll_mgr.prepare_next(self)  # Index 23: calc3_sqrt
        scroll_mgr.transform_from_copy(self, calc2_b2_equals)  # Index 24: calc3_b2
        scroll_mgr.prepare_next(self)  # Index 25: calc3_equals
        scroll_mgr.prepare_next(self)  # Index 26: calc3_sqrt2
        scroll_mgr.transform_from_copy(self, calc2_14161)     # Index 27: calc3_14161
        
        # Animate Step 6: Final answer
        scroll_mgr.prepare_next(self)  # Index 28: step6[0] - "Final answer"
        scroll_mgr.transform_from_copy(self, calc3_b2)     # Index 29: final_b_equals
        scroll_mgr.transform_from_copy(self, calc3_14161)  # Index 30: final_119_cm
        
        self.wait(2)