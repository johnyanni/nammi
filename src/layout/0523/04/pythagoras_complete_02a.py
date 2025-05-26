from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ3(MathTutorialScene):
    def construct(self):
        
        # Step 1: Original formula
        step1 = VGroup(
            Tex("Pythagoras' Theorem").scale(TEXT_SCALE),
            MathTex("c^2 = a^2 + b^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 2: Rearrange to solve for a
        step2 = VGroup(
            Tex("Rearrange to solve for a").scale(TEXT_SCALE),
            MathTex(r"a^2 = c^2 - b^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 3: Substitute values (c=17, b=15)
        step3 = VGroup(
            Tex("Substitute c = 17 and b = 15").scale(TEXT_SCALE),
            MathTex(r"a^2 = 17^2 - 15^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 4: Calculate squares
        step4 = VGroup(
            Tex("Calculate the squares").scale(TEXT_SCALE),
            MathTex(r"a^2 = 289 - 225").scale(MATH_SCALE),
            MathTex(r"a^2 = 64").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 5: Find square root
        step5 = VGroup(
            Tex("Calculate the value of a").scale(TEXT_SCALE),
            MathTex(r"\sqrt{a^2} = \sqrt{64}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Step 6: Final answer
        step6 = VGroup(
            Tex("Final answer").scale(TEXT_SCALE),
            MathTex(r"a = 8 \ \text{cm}").scale(MATH_SCALE)
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
                "17": RED,
                "15": BLUE,
                "8": GREEN,
                "17^2": RED,
                "15^2": BLUE,
                "289": RED,
                "225": BLUE,
                "64": GREEN,
            }
        )
        
        # Position formulas
        main = VGroup(step1, step2, step3, step4, step5, step6).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(UP, buff=0.3).to_edge(LEFT, buff=1)
        
        # FIRST: Let me check indices
        # self.show_flattened_indices(step1, step2, step3, step4, step5, step6)
        # return  # Exit early to see indices
        
        # Find elements - Step 1 (original formula)
        formula_c2 = self.find_element("c^2", step1[1])
        formula_equals = self.find_element("=", step1[1])
        formula_a2 = self.find_element("a^2", step1[1])
        formula_plus = self.find_element("+", step1[1])
        formula_b2 = self.find_element("b^2", step1[1])
        
        # Step 2 (rearranged) - separate only what changes in next step
        rearr_a2 = self.find_element("a^2", step2[1])  # Stays as a^2 in next step
        rearr_equals = self.find_element("=", step2[1])
        rearr_c = self.find_element("c", step2[1])      # Will change to 17
        rearr_c_squared = self.find_element("^2", step2[1], nth=1)
        rearr_minus = self.find_element("-", step2[1])
        rearr_b = self.find_element("b", step2[1])      # Will change to 15
        rearr_b_squared = self.find_element("^2", step2[1], nth=2)
        
        # Step 3 (substituted values)
        sub_a2_equals = self.find_element("a^2 =", step3[1])
        sub_17 = self.find_element("17", step3[1])
        sub_17_squared = self.find_element("^2", step3[1], nth=1)
        sub_minus = self.find_element("-", step3[1])
        sub_15 = self.find_element("15", step3[1])
        sub_15_squared = self.find_element("^2", step3[1], nth=2)
        
        # Step 4 (calculated squares)
        calc1_a2_equals = self.find_element("a^2 =", step4[1])
        calc1_289 = self.find_element("289", step4[1])
        calc1_minus = self.find_element("-", step4[1])
        calc1_225 = self.find_element("225", step4[1])
        
        calc2_a2_equals = self.find_element("a^2 =", step4[2])
        calc2_64 = self.find_element("64", step4[2])
        
        # Step 5 (square root)
        calc3_sqrt = step5[1][0][0:2]  # sqrt symbol and bar
        calc3_a2 = step5[1][0][2:4].set_color(GREEN)    # a^2 - set color!
        calc3_equals = self.find_element("=", step5[1])
        calc3_sqrt2 = step5[1][0][5:7]  # second sqrt
        calc3_64 = self.find_element("64", step5[1])
        
        # Step 6 (final answer)
        final_a = self.find_element("a", step6[1])
        final_equals = self.find_element("=", step6[1])
        final_8_cm = step6[1][0][2:].set_color(GREEN)  # "8 cm" - using slicing for text
        
        # Create elements for ScrollManager
        elements = VGroup(
            # Step 1 - Original formula
            step1[0],              # Index 0: step1[0] - "Pythagoras' Theorem" label
            step1[1],              # Index 1: step1[1] - c^2 = a^2 + b^2 formula
            
            # Step 2 - Rearranged formula
            step2[0],              # Index 2: step2[0] - "Rearrange to solve for a" label
            rearr_a2,              # Index 3: rearr_a2 - a^2 term
            rearr_equals,          # Index 4: rearr_equals - equals sign
            VGroup(rearr_c, rearr_c_squared),  # Index 5: rearr_c,rearr_c_squared - c^2 term
            rearr_minus,           # Index 6: rearr_minus - minus sign
            VGroup(rearr_b, rearr_b_squared),  # Index 7: rearr_b,rearr_b_squared - b^2 term
            
            # Step 3 - Substituted values
            step3[0],              # Index 8: step3[0] - "Substitute c = 17 and b = 15" label
            sub_a2_equals,         # Index 9: sub_a2_equals - a^2 = part
            sub_17,                # Index 10: sub_17 - c → 17
            sub_17_squared,        # Index 11: sub_17_squared - ^2 for 17
            sub_minus,             # Index 12: sub_minus - minus sign
            sub_15,                # Index 13: sub_15 - b → 15
            sub_15_squared,        # Index 14: sub_15_squared - ^2 for 15
            
            # Step 4 - Calculated squares
            step4[0],              # Index 16: step4[0] - "Calculate the squares" label
            calc1_a2_equals,       # Index 17: calc1_a2_equals - a^2 = part
            calc1_289,             # Index 18: calc1_289 - 17^2 → 289
            calc1_minus,           # Index 19: calc1_minus - minus sign
            calc1_225,             # Index 20: calc1_225 - 15^2 → 225
            
            calc2_a2_equals,       # Index 21: calc2_a2_equals - a^2 = part
            calc2_64,              # Index 22: calc2_64 - 289 - 225 → 64
            
            # Step 5 - Square root
            step5[0],              # Index 23: step5[0] - "Calculate the value of a" label
            calc3_sqrt,            # Index 24: calc3_sqrt - first square root symbol
            calc3_a2,              # Index 25: calc3_a2 - a^2 under sqrt
            calc3_equals,          # Index 26: calc3_equals - equals sign
            calc3_sqrt2,           # Index 27: calc3_sqrt2 - second square root symbol
            calc3_64,              # Index 28: calc3_64 - 64 under sqrt
            
            # Step 6 - Final answer
            step6[0],              # Index 29: step6[0] - "Final answer" label
            final_a,               # Index 30: final_a - a term
            final_equals,          # Index 31: final_equals - equals sign
            final_8_cm             # Index 32: final_8_cm - 64 → 8 cm
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # Animate Step 1: Original formula
        scroll_mgr.prepare_next(self)  # Index 0: step1[0] - "Pythagoras' Theorem" label
        scroll_mgr.prepare_next(self)  # Index 1: step1[1] - c^2 = a^2 + b^2 formula
        
        # Animate Step 2: Rearrange
        scroll_mgr.prepare_next(self)  # Index 2: step2[0] - "Rearrange to solve for a" label
        scroll_mgr.fade_in_from_target(self, formula_a2)          # Index 3: rearr_a2 - a^2 term
        scroll_mgr.fade_in_from_target(self, formula_equals)      # Index 4: rearr_equals - equals sign
        scroll_mgr.fade_in_from_target(self, formula_c2)          # Index 5: rearr_c,rearr_c_squared - c^2 term
        scroll_mgr.fade_in_from_target(self, formula_plus)        # Index 6: rearr_minus - minus sign (transforms from +)
        scroll_mgr.fade_in_from_target(self, formula_b2)          # Index 7: rearr_b,rearr_b_squared - b^2 term
        
        # Animate Step 3: Substitute values
        scroll_mgr.prepare_next(self)  # Index 8: step3[0] - "Substitute c = 17 and b = 15" label
        scroll_mgr.transform_from_copy(self, VGroup(rearr_a2, rearr_equals))     # Index 9: sub_a2_equals - a^2 stays as a^2
        scroll_mgr.transform_from_copy(self, rearr_c)            # Index 10: sub_17 - c → 17
        scroll_mgr.transform_from_copy(self, rearr_c_squared)    # Index 11: sub_17_squared - ^2 for 17
        scroll_mgr.transform_from_copy(self, rearr_minus)        # Index 12: sub_minus - minus sign
        scroll_mgr.transform_from_copy(self, rearr_b)            # Index 13: sub_15 - b → 15
        scroll_mgr.transform_from_copy(self, rearr_b_squared)    # Index 14: sub_15_squared - ^2 for 15
        
        # Animate Step 4: Calculate squares
        scroll_mgr.prepare_next(self)  # Index 16: step4[0] - "Calculate the squares" label
        scroll_mgr.transform_from_copy(self, sub_a2_equals)       # Index 17: calc1_a2_equals - a^2 = part
        scroll_mgr.fade_in_from_target(self, VGroup(sub_17, sub_17_squared))  # Index 18: calc1_289 - 17^2 → 289
        scroll_mgr.transform_from_copy(self, sub_minus)           # Index 19: calc1_minus - minus sign
        scroll_mgr.fade_in_from_target(self, VGroup(sub_15, sub_15_squared))  # Index 20: calc1_225 - 15^2 → 225
        
        # Continue Step 4: a^2 = 64
        scroll_mgr.transform_from_copy(self, calc1_a2_equals)     # Index 21: calc2_a2_equals - a^2 = part
        scroll_mgr.fade_in_from_target(self, VGroup(calc1_289, calc1_minus, calc1_225))  # Index 22: calc2_64 - 289 - 225 → 64
        
        # Scroll if needed
        scroll_mgr.scroll_down(self, steps=3)
        
        # Animate Step 5: Square root
        scroll_mgr.prepare_next(self)  # Index 23: step5[0] - "Calculate the value of a" label
        scroll_mgr.prepare_next(self)  # Index 24: calc3_sqrt - first square root symbol
        scroll_mgr.transform_from_copy(self, calc2_a2_equals)     # Index 25: calc3_a2 - a^2 under sqrt
        scroll_mgr.prepare_next(self)  # Index 26: calc3_equals - equals sign
        scroll_mgr.prepare_next(self)  # Index 27: calc3_sqrt2 - second square root symbol
        scroll_mgr.transform_from_copy(self, calc2_64)            # Index 28: calc3_64 - 64 under sqrt
        
        # Animate Step 6: Final answer
        scroll_mgr.prepare_next(self)  # Index 29: step6[0] - "Final answer" label
        scroll_mgr.fade_in_from_target(self, VGroup(calc3_sqrt, calc3_a2))  # Index 30: final_a - a (from √a²)
        scroll_mgr.prepare_next(self)  # Index 31: final_equals - equals sign
        scroll_mgr.fade_in_from_target(self, VGroup(calc3_sqrt2, calc3_64))  # Index 32: final_8_cm - 64 → 8 cm
        
        self.wait(2)