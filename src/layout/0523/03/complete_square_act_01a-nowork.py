from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class Square1(MathTutorialScene):
    def construct(self):
        
        step1 = VGroup(
            Tex("Complete square").scale(TEXT_SCALE),
            MathTex("k^5 - 4k = 2k + 50").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        horizontal_arrangement = VGroup(
            MathTex(r"\left( \frac{-6}{2} \right)^2").scale(MATH_SCALE),
            Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW, buff=0.1),
            MathTex(r"= (-3)^2").scale(MATH_SCALE)
        ).arrange(RIGHT, buff=0.5)
        
        equation = MathTex("k^2 - 6k = 18").scale(1.5)
        annotations = self.add_annotations("-2k", 
                                 self.find_element("6k", equation),
                                 self.find_element("18", equation),
                                 color=RED)

        
        
        
        step2 = VGroup(
            Tex("Complete square").scale(TEXT_SCALE),
            equation,
            annotations,
            MathTex("k^2 - 6k = 18").scale(1.5),
            horizontal_arrangement
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        
        # Apply colors
        self.apply_smart_colorize(
            [step1[1], step2[1], step2[1][0], step2[2], step2[3][0]],
            {
                "k": BLUE,
                "k^2": BLUE,
                "4k": RED,
                "2k": RED,
                "18": GREEN,
                "-6": BLUE,
            }
        )
        
        # Position formulas
        main = VGroup(step1, step2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(UP, buff=0.3).to_edge(LEFT, buff=1)
        
        # # Find elements - Step 1
        # formula_k2 = self.find_element("k^2", step1[1])
        # formula_minus = self.find_element("-", step1[1])
        # formula_4k = self.find_element("4k", step1[1])
        # formula_equals = self.find_element("=", step1[1])
        # formula_2k = self.find_element("2k", step1[1])
        # formula_plus = self.find_element("+", step1[1])
        # formula_18 = self.find_element("18", step1[1])
        
        # # Step 2
        # rearr_k2 = self.find_element("k^2", step2[1])
        # rearr_minus1 = self.find_element("-", step2[1], nth=1)
        # rearr_4k = self.find_element("4k", step2[1])
        # rearr_minus2 = self.find_element("-", step2[1], nth=2)
        # rearr_2k = self.find_element("2k", step2[1])
        # rearr_equals = self.find_element("=", step2[1])
        # rearr_18 = self.find_element("18", step2[1])
        
        # Create elements for ScrollManager
        elements = VGroup(
            # Step 1 - Original equation
            step1[0],              # Index 0: step1[0] - "Complete square" label
            step1[1],              # Index 1: step1[1] - k^2 - 4k = 2k + 18 equation
            
            # Step 2 - Move terms to left
            step2[0],              # Index 3: step2[0] - "Move all terms to left side" label
            step2[1],              # Index 4: step2[1] - k^2 - 4k - 2k = 18 equation
            *step2[2],
            step2[3],
            *step2[4]
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # Animate Step 1: Original equation
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
        
        
        
        
        self.wait(2)

