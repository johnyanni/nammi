from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormulaScrollManager(MathTutorialScene):
    def construct(self):
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"
        
        step1 = self.create_scrollable_step(
            "Step 1: Divide both sides by 4",
            MathTex("4(x+5)^2 = 48"),
            Annotation(r"\div 4", "4", "48", color=GREEN),
            MathTex("(x+5)^2 = 12")
        )
        
        
        scroll_mgr = ScrollManager(VGroup(
            step1[0],    # label
            step1[1],    # equation + annotation group
            step1[2]     # simplified equation
        ))
        
        self.add(step1)
        
        
        scroll_mgr.prepare_next(self)  
        scroll_mgr.prepare_next(self)  
        scroll_mgr.prepare_next(self)  


        
