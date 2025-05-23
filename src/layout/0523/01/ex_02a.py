from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        step1 = VGroup(
            Tex("Step 1: Subtract 2").scale(0.6),
            self.create_annotated_equation(
                "2x + 2 = 10",
                "-2",
                "2", "10",
                nth_from=0,
                color=RED
            ),
            MathTex("4x = 8").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)  # Equal spacing everywhere

        # For ScrollManager
        elements = VGroup(
            step1[0],  # Label
            step1[1],  # Annotated equation (VGroup)
            step1[2]   # Regular equation
        )

        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  # Shows equation, then annotations
        scroll_mgr.prepare_next(self)  # Shows final equation
        
    



    
