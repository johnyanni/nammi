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
        
        
        # Starting equation
        starting_eq = self.create_smart_step(
            "Starting equation: Convert to standard quadratic form",
            MathTex("4(x+5)^2=48")
        )

        # Step 1: Divide both sides by 4
        step1_annotated = self.create_annotated_equation(
            "4(x+5)^2=48", 
            r"\div 4", 
            "4", "48", 
            color=GREEN
        )

        step1 = self.create_smart_step(
            "Step 1: Divide both sides by 4",
            step1_annotated,
            MathTex("(x+5)^2=12")
        )

        # Step 2: Take square root of both sides
        step2_annotated = self.create_annotated_equation(
            "(x+5)^2=12",
            r"\sqrt{\phantom{x}}",
            "(x+5)^2", "12",
            color=BLUE
        )

        step2 = self.create_smart_step(
            "Step 2: Take square root of both sides",
            step2_annotated,
            MathTex("x+5 = \\pm\\sqrt{12}")
        )

        # Step 3: Simplify the square root
        step3 = self.create_smart_step(
            "Step 3: Simplify the square root",
            MathTex("\\sqrt{12} = \\sqrt{4 \\cdot 3} = 2\\sqrt{3}"),
            MathTex("x+5 = \\pm 2\\sqrt{3}")
        )

        # Step 4: Subtract 5 from both sides
        step4_annotated = self.create_annotated_equation(
            "x+5 = \\pm 2\\sqrt{3}",
            r"-5",
            "x+5", "\\pm 2\\sqrt{3}",
            color=RED
        )

        step4 = self.create_smart_step(
            "Step 4: Subtract 5 from both sides",
            step4_annotated,
            MathTex("x = -5 \\pm 2\\sqrt{3}")
        )

        # Final answer
        final_answer = self.create_smart_step(
            "Final Answer:",
            MathTex("x = -5 + 2\\sqrt{3} \\quad \\text{or} \\quad x = -5 - 2\\sqrt{3}"),
            MathTex("x \\approx -1.54 \\quad \\text{or} \\quad x \\approx -8.46")
        )

        # Arrange all steps
        solution = VGroup(
            starting_eq,
            step1,
            step2,
            step3,
            step4,
            final_answer
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        solution.to_edge(LEFT, buff=1).to_edge(UP, buff=0.5)
        self.add(solution)