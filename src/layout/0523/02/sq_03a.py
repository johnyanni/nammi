from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ1(MathTutorialScene):
    def construct(self):
        
        
        test = VGroup(
            MathTex(r"c^2 = \sqrt{25} + 100").scale(MATH_SCALE),
            MathTex(r"c^2 = 5 + 100").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Create all formulas
        formula = MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE)
        formula[0][:2].set_color(YELLOW)
        formula[0][3:5].set_color(GREEN)
        formula[0][6:].set_color(RED)
        
        substitute = MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        substitute[0][:2].set_color(YELLOW)
        substitute[0][3:5].set_color(GREEN)
        substitute[0][6:].set_color(RED)
        
        calculation_step1 = MathTex(r"c^2 = \sqrt{25} + 100").scale(MATH_SCALE)
        calculation_step1[0][:2].set_color(YELLOW)
        calculation_step1[0][3:5].set_color(GREEN)
        calculation_step1[0][5:].set_color(RED)
        
        calculation_step2 = MathTex(r"c^2 = 125", color=YELLOW).scale(MATH_SCALE)
        
        # Position formulas
        VGroup(test,formula, substitute, calculation_step1, calculation_step2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(LEFT)
        
        # Find elements using find_element - SIMPLIFIED
        # Formula parts
        formula_c2_equals = self.find_element("c^2 =", formula)
        formula_a = self.find_element("a", formula)
        formula_a_squared = self.find_element("^2", formula, nth=1)
        formula_plus = self.find_element("+", formula)
        formula_b = self.find_element("b", formula)
        formula_b_squared = self.find_element("^2", formula, nth=2)
        
        # Substitute parts - SIMPLIFIED
        sub_c2_equals = self.find_element("c^2 =", substitute, as_group=True)
        sub_5 = self.find_element("5", substitute)
        sub_5_squared = self.find_element("^2", substitute, nth=1)
        sub_plus = self.find_element("+", substitute)
        sub_10 = self.find_element("10", substitute)
        sub_10_squared = self.find_element("^2", substitute, nth=2)
        
        # Calculation step 1 parts - SIMPLIFIED
        calc1_c2_equals = self.find_element("c^2 =", calculation_step1)
        calc_sqrt = calculation_step1[0][3:5]
        # calc_sqrt = self.find_element("sqrt", calculation_step1)
        
        calc1_25 = self.find_element("25", calculation_step1)
        calc1_plus = self.find_element("+", calculation_step1)
        calc1_100 = self.find_element("100", calculation_step1)
        
        # Create elements for ScrollManager
        elements = VGroup(
            test[0],
            test[1],
            formula,  # Index 0 - full formula
            
            # Substitute equation parts
            sub_c2_equals,     # Index 1: c^2 =
            sub_5,             # Index 2: 5
            sub_5_squared,     # Index 3: ^2
            sub_plus,          # Index 4: +
            sub_10,            # Index 5: 10
            sub_10_squared,    # Index 6: ^2
            
            # Calculation step 1 parts
            calc1_c2_equals,   # Index 7: c^2 =
            calc_sqrt,
            calc1_25,          # Index 8: 25
            calc1_plus,        # Index 9: +
            calc1_100,         # Index 10: 100
            
            # Calculation step 2
            calculation_step2,  # Index 11
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # ANIMATIONS
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)  # Shows formula
        # Show the original formula
        scroll_mgr.prepare_next(self)  # Shows formula
        
        self.wait(1)

        scroll_mgr.prepare_next(self)  # Shows formula
        scroll_mgr.prepare_next(self)  # Shows formula
        scroll_mgr.prepare_next(self)  # Shows formula
        scroll_mgr.prepare_next(self)  # Shows formula
        scroll_mgr.prepare_next(self)  # Shows formula
        scroll_mgr.prepare_next(self)  # Shows formula
        
        # Transform formula parts to substitute equation
        # c^2 = stays the same
        # scroll_mgr.fade_in_from_target(self, formula_c2_equals)
        
        # # a -> 5
        # scroll_mgr.fade_in_from_target(self, formula_a)
        
        # # First ^2
        # scroll_mgr.fade_in_from_target(self, formula_a_squared)
        
        # # +
        # scroll_mgr.fade_in_from_target(self, formula_plus)
        
        # # b -> 10
        # scroll_mgr.fade_in_from_target(self, formula_b)
        
        # # Second ^2
        # scroll_mgr.fade_in_from_target(self, formula_b_squared)
        
        self.wait(1)
        
        # Transform substitute to calculation_step1
        # c^2 = stays
        scroll_mgr.fade_in_from_target(self, sub_c2_equals)
        
        scroll_mgr.prepare_next(self)
        
        # 5^2 -> 25
        scroll_mgr.fade_in_from_target(self, VGroup(sub_5, sub_5_squared))
        
        # + stays
        scroll_mgr.fade_in_from_target(self, sub_plus)
        
        # 10^2 -> 100
        scroll_mgr.fade_in_from_target(self, VGroup(sub_10, sub_10_squared))
        
        self.wait(1)
        
        # Transform calculation_step1 to calculation_step2
        # c^2 = 25 + 100 -> c^2 = 125
        scroll_mgr.fade_in_from_target(self, calculation_step1)
        
        self.wait(2)