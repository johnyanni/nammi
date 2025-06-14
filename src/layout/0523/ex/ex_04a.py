from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class ProblematicExample(MathTutorialScene):
    def construct(self):
        scroll = ScrollManager(scene=self, global_arrangement=False)
        title = Tex("Steps").to_edge(UP)
        self.add(title)
        
        scroll.set_position_target(title, DOWN, LEFT, 0.5)
        
        # Add initial steps
        for i in range(1, 4):
            step = scroll.create_step(MathTex(f"Step {i}"))
            scroll.prepare_next()
        
        # Scroll up
        scroll.scroll_down(1)  # Step 1 disappears
        
        # Add new step - positioning issue!
        step4 = scroll.create_step(MathTex("Step 4"))
        # This positions based on Step 3's ORIGINAL position
        # Not its current position after scrolling
        
        scroll.prepare_next()  # Step 4 appears with wrong spacing