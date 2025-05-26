from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ1(MathTutorialScene):
    def construct(self):
        
        
        formula = MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE)

        substitute = MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)

        calculation_step1 = MathTex(r"c^2 = 25 + 100").scale(MATH_SCALE)
        
        calculation_step2 = MathTex(r"c^2 = 125", color=YELLOW).scale(MATH_SCALE)
        
        calculation_step3 = MathTex(r"\sqrt{c^2} = \sqrt{125}", color=YELLOW).scale(MATH_SCALE)
        
        calculation_step4 = MathTex(r"c = 11.18 \ \text{cm}", color=YELLOW).scale(MATH_SCALE)
        
        self.apply_smart_colorize(
            [formula, substitute, calculation_step1],
            {
                "c": YELLOW,
                "a^2": GREEN,
                "b^2": RED,
                "c^2": YELLOW,
                "5^2": GREEN,
                "10^2": RED,
                "25": GREEN,
                "100": RED,
            }
        )
        
        #self.show_indices(calculation_step3)
        
        # Position formulas
        VGroup(formula, substitute, calculation_step1, calculation_step2, calculation_step3, calculation_step4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        ).to_edge(LEFT)
        

        formula_c2_equals = self.find_element("c^2 =", formula)
        formula_a = self.find_element("a", formula)
        formula_a_squared = self.find_element("^2", formula, nth=1)
        formula_plus = self.find_element("+", formula)
        formula_b = self.find_element("b", formula)
        formula_b_squared = self.find_element("^2", formula, nth=2)
        
   
        sub_c2_equals = self.find_element("c^2 =", substitute)
        sub_5 = self.find_element("5", substitute)
        sub_5_squared = self.find_element("^2", substitute, nth=1)
        sub_plus = self.find_element("+", substitute)
        sub_10 = self.find_element("10", substitute)
        sub_10_squared = self.find_element("^2", substitute, nth=2)
        
        
        calc1_c2_equals = self.find_element("c^2 =", calculation_step1)
        calc1_25 = self.find_element("25", calculation_step1)
        calc1_plus = self.find_element("+", calculation_step1)
        calc1_100 = self.find_element("100", calculation_step1)
        
        calc2_c2_equals = self.find_element("c^2 =", calculation_step2)
        calc2_125 = self.find_element("125", calculation_step2)
        
        calc3_sqrt = calculation_step3[0][0:2]
        calc3_c2 = calculation_step3[0][2:4]
        calc3_c2_equals = self.find_element("=", calculation_step3)
        calc3_sqrt2 = calculation_step3[0][5:7]
        calc3_125 = self.find_element("125", calculation_step3)
        
        calc4_c_equals = self.find_element("c =", calculation_step4)
        calc4_11_18 = self.find_element(r"11.18 \ \text{cm}", calculation_step4)
        
        
        
        # Create elements for ScrollManager
        elements = VGroup(
            formula,  # Index 0 - full formula
            
            sub_c2_equals,     # Index 1
            sub_5,             # Index 2
            sub_5_squared,     # Index 3
            sub_plus,          # Index 4
            sub_10,            # Index 5
            sub_10_squared,    # Index 6
            
            calc1_c2_equals,   # Index 7
            calc1_25,          # Index 8
            calc1_plus,        # Index 9
            calc1_100,         # Index 10
            
            calc2_c2_equals,   # Index 11
            calc2_125,         # Index 12
            
                
            calc3_sqrt,        # Index 13
            calc3_c2,          # Index 14
            calc3_c2_equals,   # Index 15
            calc3_sqrt2,       # Index 16
            calc3_125,         # Index 17
            
            calc4_c_equals,    # Index 18
            calc4_11_18        # Index 19
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        scroll_mgr.prepare_next(self) # Index 0: formula
        
        #substitute
        scroll_mgr.transform_from_copy(self, formula_c2_equals)
        scroll_mgr.transform_from_copy(self, formula_a)
        scroll_mgr.transform_from_copy(self, formula_a_squared)
        scroll_mgr.transform_from_copy(self, formula_plus)
        scroll_mgr.transform_from_copy(self, formula_b)
        scroll_mgr.transform_from_copy(self, formula_b_squared)
        
        #calculation_step1
        scroll_mgr.transform_from_copy(self, sub_c2_equals)
        scroll_mgr.transform_from_copy(self, VGroup(sub_5, sub_5_squared))
        scroll_mgr.transform_from_copy(self, sub_plus)
        scroll_mgr.transform_from_copy(self, VGroup(sub_10, sub_10_squared))
        
        #calculation_step2
        scroll_mgr.transform_from_copy(self, calc1_c2_equals)
        scroll_mgr.transform_from_copy(self, VGroup(calc1_25, calc1_plus, calc1_100))
        
        #calculation_step3
        scroll_mgr.prepare_next(self)
        scroll_mgr.transform_from_copy(self, calc2_c2_equals)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.transform_from_copy(self, calc2_125)
        
        # #calculation_step4
        scroll_mgr.transform_from_copy(self, calc3_c2_equals)
        scroll_mgr.transform_from_copy(self, calc3_125)
        