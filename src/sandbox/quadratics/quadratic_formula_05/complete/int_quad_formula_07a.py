from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormulaASTER(MathTutorialScene):
    def construct(self):
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
 
        
        
       # Step 0: Get the equation in standard form
        step0 = self.create_multi_exp_labeled_step_tex(
            "Get the equation in standard form",
            "4(x+5)^2=48"
        )

        step0_label, step0_eq = step0[0], step0[1]

        # Step 1: Divide both sides by 4
        step1 = self.create_multi_exp_labeled_step_tex(
            "Divide both sides by 4",
            self.create_annotated_equation(
                r"4(x+5)^2=48",  # Equation text
                r"\div 4",       # Annotation
                "4", "48",       # Terms to annotate
                color=GREEN      # Annotation color
            ),
            "(x+5)^2=12"        # Result equation string
        )

        step1_label = step1[0]
        step1_annotated_eq = step1[1][0]  # First expression (the annotated equation)
        step1_result_eq = step1[1][1]     # Second expression (the result)

        # Step 2: Expand the squared term
        step2 = self.create_multi_exp_labeled_step_tex(
            "Expand the squared term",
            "x^2 + 10x + 25 = 12"  # Expanded expression
        )

        step2_label = step2[0]
        step2_eq = step2[1][0]  # The equation

        # Step 3: Subtract 12 from both sides
        step3 = self.create_multi_exp_labeled_step_tex(
            "Subtract 12 from both sides",
            self.create_annotated_equation(
                r"x^2 + 10x + 25 = 12",  # Equation text
                r"-12",                  # Annotation
                "25", "12",              # Terms to annotate
                color=RED                # Annotation color
            ),
            "x^2 + 10x + 13 = 0"         # Result equation string
        )

        step3_label = step3[0]
        step3_annotated_eq = step3[1][0][0]  # The equation being annotated
        step3_annotation = step3[1][0][1]    # The annotation
        step3_result_eq = step3[1][1]        # The result equation

        # Arrange all steps vertically
        solution_steps = VGroup(
            step0,
            step1,
            step2,
            step3
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)

        # Add the steps to the scene
        self.add(solution_steps)

        
        