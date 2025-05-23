from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc(MathTutorialScene):
    def construct(self):
        
        
        eq3 = self.create_annotated_equation(
            "4x + 2 = 10",
            "-2",
            "2", "10",
            annotation_scale=0.5  # Smaller annotations
        )

        # Both custom
        eq4 = self.create_annotated_equation(
            "4x + 2 = 10",
            "-2",
            "2", "10",
            scale=1.2,
            annotation_scale=0.7
        )
    
        eq4.next_to(eq3, DOWN)
        
        steps = VGroup(eq3, eq4)
        
        scroll_manager = ScrollManager(steps)
        
        
        scroll_manager.prepare_next(self)
        scroll_manager.prepare_next(self)
        self.wait(1)
        
    

    
    
    
    