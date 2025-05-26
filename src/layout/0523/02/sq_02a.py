from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ1(MathTutorialScene):
    def construct(self):
        
        # Create all formulas
        formula = MathTex(r"c^2 = a^2 + b^2").scale(MATH_SCALE)
        formula[0][:2].set_color(YELLOW)
        formula[0][3:5].set_color(GREEN)
        formula[0][6:].set_color(RED)
        
        substitute = MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        substitute[0][:2].set_color(YELLOW)
        substitute[0][3:5].set_color(GREEN)
        substitute[0][6:].set_color(RED)
        
        calculation_step1 = MathTex(r"c^2 = 25 + 100").scale(MATH_SCALE)
        calculation_step1[0][:2].set_color(YELLOW)
        calculation_step1[0][3:5].set_color(GREEN)
        calculation_step1[0][6:].set_color(RED)
        
        calculation_step2 = MathTex(r"c^2 = 125", color=YELLOW).scale(MATH_SCALE)
        
        # Position formulas
        VGroup(formula, substitute, calculation_step1, calculation_step2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(LEFT)
        
        # Create elements for ScrollManager
        # Breaking down substitute into parts that will be animated separately
        elements = VGroup(
            formula,  # Index 0 - full formula
            
            # Substitute equation parts (hidden initially)
            substitute[0][:3],    # Index 1: c^2 =
            substitute[0][3],     # Index 2: 5
            substitute[0][4],     # Index 3: ^2
            substitute[0][5],     # Index 4: +
            substitute[0][6:8],   # Index 5: 10
            substitute[0][-1],    # Index 6: ^2
            
            # Calculation step 1 parts
            calculation_step1[0][:3],   # Index 7: c^2 =
            calculation_step1[0][3:5],  # Index 8: 25
            calculation_step1[0][5],    # Index 9: +
            calculation_step1[0][6:],   # Index 10: 100
            
            # Calculation step 2
            calculation_step2,     # Index 11
        )
        
        
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # ANIMATIONS
        
        # Show the original formula
        scroll_mgr.prepare_next(self)  # Shows formula
        
        scroll_mgr.prepare_next(self)  # Shows c^2=
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)
        scroll_mgr.prepare_next(self)

        
        self.wait(1)
        
        # Optionally, transform substitute to calculation_step1
        # You would need to add more elements and animations here
        # following the same pattern