from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ2(MathTutorialScene):
    def construct(self):
        
        # Create formulas - solving for c when a=8 and b=6
        formula = MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE)

        substitute = MathTex(r"c^2 = 8^2 + 6^2").scale(MATH_SCALE)

        calculation_step1 = MathTex(r"c^2 = 64 + 36").scale(MATH_SCALE)

        calculation_step2 = MathTex(r"c^2 = 100", color=YELLOW).scale(MATH_SCALE)
        
        calculation_step3 = MathTex(r"\sqrt{c^2} = \sqrt{100}", color=YELLOW).scale(MATH_SCALE)
        
        calculation_step4 = MathTex(r"c = 10 \ \text{cm}", color=YELLOW).scale(MATH_SCALE)
        
        # Apply colors
        self.apply_smart_colorize(
            [formula, substitute, calculation_step1],
            {
                "c": YELLOW,
                "a^2": GREEN,
                "b^2": RED,
                "c^2": YELLOW,
                "8^2": GREEN,
                "6^2": RED,
                "64": GREEN,
                "36": RED,
            }
        )
        
        # Position formulas
        main = VGroup(formula, substitute, calculation_step1, calculation_step2, calculation_step3, calculation_step4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        ).to_edge(LEFT)
        
        #self.show_vgroup_indices(main)
        
        # Find elements - Formula parts
        formula_c2_equals = self.find_element("c^2 =", formula)
        formula_a = self.find_element("a", formula)
        formula_a_squared = self.find_element("^2", formula, nth=1)
        formula_plus = self.find_element("+", formula)
        formula_b = self.find_element("b", formula)
        formula_b_squared = self.find_element("^2", formula, nth=2)
        
        # Substitute parts
        sub_c2_equals = self.find_element("c^2 =", substitute)
        sub_8 = self.find_element("8", substitute)
        sub_8_squared = self.find_element("^2", substitute, nth=1)
        sub_plus = self.find_element("+", substitute)
        sub_6 = self.find_element("6", substitute)
        sub_6_squared = self.find_element("^2", substitute, nth=2)
        
        # Calculation step 1 parts
        calc1_c2_equals = self.find_element("c^2 =", calculation_step1)
        calc1_64 = self.find_element("64", calculation_step1)
        calc1_plus = self.find_element("+", calculation_step1)
        calc1_36 = self.find_element("36", calculation_step1)
        
        # Calculation step 2 parts
        calc2_c2_equals = self.find_element("c^2 =", calculation_step2)
        calc2_100 = self.find_element("100", calculation_step2)
        
        # Calculation step 3 parts (sqrt handling)
        calc3_sqrt = calculation_step3[0][0:2]      # First sqrt symbol and bar
        calc3_c2 = calculation_step3[0][2:4]        # c^2 inside sqrt
        calc3_equals = calculation_step3[0][4]      # equals sign
        calc3_sqrt2 = calculation_step3[0][5:7]     # Second sqrt symbol and bar
        calc3_100 = self.find_element("100", calculation_step3)      # 100 inside sqrt
        
        # Calculation step 4 parts
        calc4_c_equals = self.find_element("c =", calculation_step4)
        calc4_10_cm = calculation_step4[0][2:]      # "10 cm" - using slicing for text
        
        # Create elements for ScrollManager
        elements = VGroup(
            formula,           # Index 0 - full formula
            
            sub_c2_equals,     # Index 1
            sub_8,             # Index 2
            sub_8_squared,     # Index 3
            sub_plus,          # Index 4
            sub_6,             # Index 5
            sub_6_squared,     # Index 6
            
            calc1_c2_equals,   # Index 7
            calc1_64,          # Index 8
            calc1_plus,        # Index 9
            calc1_36,          # Index 10
            
            calc2_c2_equals,   # Index 11
            calc2_100,         # Index 12
            
            calc3_sqrt,        # Index 13  
            calc3_c2,          # Index 14
            calc3_equals,      # Index 15 (equals between sqrts)
            calc3_sqrt2,       # Index 16
            calc3_100,         # Index 17
            
            calc4_c_equals,    # Index 18
            calc4_10_cm        # Index 19
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # ANIMATIONS
        scroll_mgr.prepare_next(self)  # Index 0: formula
        self.wait(0.5)
        
        # Substitute values
        scroll_mgr.fade_in_from_target(self, formula_c2_equals)      # c^2 =
        scroll_mgr.fade_in_from_target(self, formula_a)             # a → 8
        scroll_mgr.fade_in_from_target(self, formula_a_squared)     # ^2
        scroll_mgr.fade_in_from_target(self, formula_plus)          # +
        scroll_mgr.fade_in_from_target(self, formula_b)             # b → 6
        scroll_mgr.fade_in_from_target(self, formula_b_squared)     # ^2
        self.wait(0.5)
        
        # Calculate squares
        scroll_mgr.fade_in_from_target(self, sub_c2_equals)                    # c^2 =
        scroll_mgr.fade_in_from_target(self, VGroup(sub_8, sub_8_squared))    # 8^2 → 64
        scroll_mgr.fade_in_from_target(self, sub_plus)                        # +
        scroll_mgr.fade_in_from_target(self, VGroup(sub_6, sub_6_squared))    # 6^2 → 36
        self.wait(0.5)
        
        # Add the values
        scroll_mgr.fade_in_from_target(self, calc1_c2_equals)                           # c^2 =
        scroll_mgr.fade_in_from_target(self, VGroup(calc1_64, calc1_plus, calc1_36))   # 64 + 36 → 100
        self.wait(0.5)
        
        # Show sqrt setup
        scroll_mgr.prepare_next(self)  # sqrt symbol
        scroll_mgr.fade_in_from_target(self, calc2_c2_equals)  # c^2
        scroll_mgr.prepare_next(self)  # equals
        scroll_mgr.prepare_next(self)  # sqrt symbol
        scroll_mgr.fade_in_from_target(self, calc2_100)  # 100
        self.wait(0.5)
        
        # Final answer
        scroll_mgr.fade_in_from_target(self, calc3_c2)    # c (from c^2 under sqrt)
        scroll_mgr.fade_in_from_target(self, calc3_100)   # 10 (from 100 under sqrt)
        
        self.wait(2)