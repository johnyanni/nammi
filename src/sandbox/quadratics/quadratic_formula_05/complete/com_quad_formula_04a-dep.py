from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"




class QuadraticFormula(MathTutorialScene):
    def construct(self):
        
        
    
        
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
        ANNOTATION_SPACING = 0.7


        # Step 1: Get the equation in standard form
        step1 = self.create_labeled_step_with_annotations(
            "Get the equation in standard form",
            ["4(x+5)^2=48"]
        )
        
        # Step 2: Divide both sides by 4
        step2 = self.create_labeled_step_with_annotations(
            "Divide both sides by 4",
            ["4(x+5)^2=48", "(x+5)^2=12"],
            annotations=[
                (r"\div 4", "4", "48", GREEN)
            ]
        )
        
        # Step 3: Expand the squared term
        step3 = self.create_labeled_step_with_annotations(
            "Expand the squared term",
            ["x^2 + 10x + 25 = 12"]
        )
        
        # Step 4: Subtract 12 from both sides
        step4 = self.create_labeled_step_with_annotations(
            "Subtract 12 from both sides",
            ["x^2 + 10x + 25 = 12", "x^2 + 10x + 13 = 0"],
            annotations=[
                ("-12", "25", "12", RED)
            ]
        )
        
        # Arrange all steps vertically
        solution = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        solution.to_edge(UP, buff=0.1).to_edge(LEFT, buff=1)
        
        # Animation sequence
        self.play(Write(step1.label))
        self.play(Write(step1.expressions[0]))
        self.wait()

        self.play(Write(step2.label))  # Step 2 label
        self.play(Write(step2.expressions[0]))  # Step 2 first expression (without annotations)
        self.play(FadeIn(step2.annotations[0]))  # Step 2 annotations
        self.play(Write(step2.expressions[1]))  # Step 2 second expression
        self.wait()

        self.play(Write(step3.label))
        self.play(Write(step3.expressions[0]))
        self.wait()

        self.play(Write(step4.label))
        self.play(Write(step4.expressions[0]))
        self.play(FadeIn(step4.annotations[0]))
        self.play(Write(step4.expressions[1]))