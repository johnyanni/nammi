from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class SQ2(MathTutorialScene):
    def construct(self):
        
        # Create all formulas - solving for 'a' when b=12 and c=13
        formula = MathTex(r"a^2 + b^2 = c^2").scale(MATH_SCALE)
        formula[0][:2].set_color(GREEN)      # a^2
        formula[0][3:5].set_color(BLUE)      # b^2
        formula[0][6:].set_color(RED)        # c^2
        
        rearranged = MathTex(r"a^2 = c^2 - b^2").scale(MATH_SCALE)
        rearranged[0][:2].set_color(GREEN)   # a^2
        rearranged[0][3:5].set_color(RED)    # c^2
        rearranged[0][6:].set_color(BLUE)    # b^2
        
        substitute = MathTex(r"a^2 = 13^2 - 12^2").scale(MATH_SCALE)
        substitute[0][:2].set_color(GREEN)   # a^2
        substitute[0][3:6].set_color(RED)    # 13^2
        substitute[0][7:].set_color(BLUE)    # 12^2
        
        calculation_step1 = MathTex(r"a^2 = 169 - 144").scale(MATH_SCALE)
        calculation_step1[0][:2].set_color(GREEN)   # a^2
        calculation_step1[0][3:6].set_color(RED)    # 169
        calculation_step1[0][7:].set_color(BLUE)    # 144
        
        calculation_step2 = MathTex(r"a^2 = 25").scale(MATH_SCALE)
        calculation_step2[0][:2].set_color(GREEN)   # a^2
        calculation_step2[0][3:].set_color(PURPLE)  # 25
        
        final_answer = MathTex(r"a = 5").scale(MATH_SCALE)
        final_answer[0][0].set_color(GREEN)         # a
        final_answer[0][2].set_color(PURPLE)        # 5
        
        # Position formulas
        VGroup(formula, rearranged, substitute, calculation_step1, 
               calculation_step2, final_answer).arrange(
            DOWN, aligned_edge=LEFT, buff=0.4
        ).to_edge(LEFT)
        
        # Create elements for ScrollManager with correct indexing
        elements = VGroup(
            # 0: Show original formula
            formula,
            
            # 1-7: Show rearranged formula piece by piece
            rearranged[0][:2],     # a^2
            rearranged[0][2],      # =
            rearranged[0][3:5],    # c^2
            rearranged[0][5],      # -
            rearranged[0][6:8],    # b^2
            
            # 6-12: Transform to substituted values
            substitute[0][:2],     # a^2
            substitute[0][2],      # =
            substitute[0][3:6],    # 13^2
            substitute[0][6],      # -
            substitute[0][7:10],   # 12^2
            
            # 11-16: Show calculated values
            calculation_step1[0][:2],    # a^2
            calculation_step1[0][2],     # =
            calculation_step1[0][3:6],   # 169
            calculation_step1[0][6],     # -
            calculation_step1[0][7:10],  # 144
            
            # 16-18: Show simplified result
            calculation_step2[0][:2],    # a^2
            calculation_step2[0][2],     # =
            calculation_step2[0][3:5],   # 25
            
            # 19-21: Show final answer
            final_answer[0][0],    # a
            final_answer[0][1],    # =
            final_answer[0][2],    # 5
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # ANIMATIONS
        
        # Show the original formula
        scroll_mgr.prepare_next(self)  # Index 0: Shows full formula
        self.wait(1)
        
        # Build rearranged formula piece by piece
        scroll_mgr.prepare_next(self)  # Index 1: a^2
        scroll_mgr.prepare_next(self)  # Index 2: =
        scroll_mgr.prepare_next(self)  # Index 3: c^2
        scroll_mgr.prepare_next(self)  # Index 4: -
        scroll_mgr.prepare_next(self)  # Index 5: b^2
        self.wait(1)
        
        # Transform to substituted values
        scroll_mgr.prepare_next(self)  # Index 6: a^2
        scroll_mgr.prepare_next(self)  # Index 7: =
        scroll_mgr.prepare_next(self)  # Index 8: 13^2
        scroll_mgr.prepare_next(self)  # Index 9: -
        scroll_mgr.prepare_next(self)  # Index 10: 12^2
        self.wait(1)
        
        # Show calculated values
        scroll_mgr.prepare_next(self)  # Index 11: a^2
        scroll_mgr.prepare_next(self)  # Index 12: =
        scroll_mgr.prepare_next(self)  # Index 13: 169
        scroll_mgr.prepare_next(self)  # Index 14: -
        scroll_mgr.prepare_next(self)  # Index 15: 144
        self.wait(1)
        
        # Show simplified result
        scroll_mgr.prepare_next(self)  # Index 16: a^2
        scroll_mgr.prepare_next(self)  # Index 17: =
        scroll_mgr.prepare_next(self)  # Index 18: 25
        self.wait(1)
        
        # Show final answer
        scroll_mgr.prepare_next(self)  # Index 19: a
        scroll_mgr.prepare_next(self)  # Index 20: =
        scroll_mgr.prepare_next(self)  # Index 21: 5
        
        self.wait(2)