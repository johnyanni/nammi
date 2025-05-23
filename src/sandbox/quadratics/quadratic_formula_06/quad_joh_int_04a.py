from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormulaLIST(MathTutorialScene):
    def construct(self):
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
        
        # Problem statement with better organization
        question_title = Tex("Solve using the quadratic formula:").scale(TEXT_SCALE)
        question_equation = MathTex("-x^2 - 3x = - 9").scale(MATH_SCALE)
        
        question_group = VGroup(question_title, question_equation).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1)
        question_group.to_edge(UP, buff=0.3).to_edge(LEFT, buff=0.7)

        self.add(question_group)
        
        # Large label, small equations
        step2 = self.create_smart_step(
            "LARGE HEADER",
            MathTex("tiny = equation"),
            MathTex("another = tiny"),
            
            label_scale=1.2,                    # Large label
            content_scales=[0.4, 0.4]          # Small equations
        )

        # Normal label, mixed equation sizes
        step3 = self.create_smart_step(
            "Step 3: Mixed sizes",
            MathTex("BIG"),                     # Huge
            MathTex("normal"),                  # Default
            MathTex("small"),                   # Tiny
            
            label_scale=0.6,                    # Normal label
            content_scales=[2.0, None, 0.3]    # Huge, default, tiny
        )

        # No label case
        step4 = self.create_smart_step(
            MathTex("equation1"),               # content_scales[0] = 1.5
            MathTex("equation2"),               # content_scales[1] = 0.8
            
            content_scales=[1.5, 0.8]          # No label_scale needed
        )
        
        steps = VGroup(step2, step3, step4)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        steps.to_edge(UP, buff=0.3).to_edge(LEFT, buff=0.7)
        
        self.add(steps)
        
        