from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormulaScrollManager(MathTutorialScene):
    def construct(self):
        
        step1 = self.create_smart_step(
            "Step 1: Start with equation",
            MathTex("4x + 8 = 20")
        )
        
        annotated_eq = self.create_annotated_equation(
            "4x + 8 = 20", "-8", "8", "20", color=GREEN
        )
        
        step2 = self.create_smart_step(
            "Step 2: Subtract 8 from both sides", 
            annotated_eq,
            MathTex("4x = 12")
        )
        
        steps = VGroup(step1, step2)
         # Position the elements AFTER unpacking
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        steps.to_edge(LEFT)
        
        # Unpack for ScrollManager
        all_elements = self.unpack_steps_for_scroll_manager(step1, step2)
        
        scroll_mgr = ScrollManager(all_elements)
        
        # Now this should work
        scroll_mgr.prepare_next(self)  # Step 1 label
        scroll_mgr.prepare_next(self)  # Step 1 equation
        scroll_mgr.prepare_next(self)  # Step 2 label
        scroll_mgr.prepare_next(self)  # Step 2 annotated equation
        scroll_mgr.prepare_next(self)  # Step 2 result equation