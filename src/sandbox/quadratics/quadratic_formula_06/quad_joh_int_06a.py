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

        # Step 2: Expand the squared term
        step2 = self.create_smart_step(
            "Step 2: Expand the squared term",
            MathTex("x^2 + 10x + 25 = 12")
        )

        # Step 3: Subtract 12 from both sides
        step3_annotated = self.create_annotated_equation(
            "x^2 + 10x + 25 = 12",
            r"-12",
            "25", "12",
            color=RED
        )

        step3 = self.create_smart_step(
            "Step 3: Subtract 12 from both sides",
            step3_annotated,
            MathTex("x^2 + 10x + 13 = 0")
        )

        # Step 4: Identify coefficients for quadratic formula
        step4 = self.create_smart_step(
            "Step 4: Identify coefficients for quadratic formula",
            MathTex("a = 1, \\quad b = 10, \\quad c = 13"),
            color_map={
                "a": A_COLOR,
                "1": A_COLOR,
                "b": B_COLOR, 
                "10": B_COLOR,
                "c": C_COLOR,
                "13": C_COLOR
            }
        )

        # Step 5: Apply quadratic formula
        step5 = self.create_smart_step(
            "Step 5: Apply the quadratic formula",
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
            MathTex(r"x = \frac{-10 \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}"),
            color_map={
                "b": B_COLOR,
                "10": B_COLOR,
                "a": A_COLOR,
                "1": A_COLOR,
                "c": C_COLOR,
                "13": C_COLOR
            }
        )

        # Step 6: Simplify under the radical
        step6 = self.create_smart_step(
            "Step 6: Simplify under the radical",
            MathTex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}"),
            MathTex(r"x = \frac{-10 \pm \sqrt{48}}{2}")
        )

        # Step 7: Simplify the square root
        step7 = self.create_smart_step(
            "Step 7: Simplify the square root",
            MathTex(r"\sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt{3}"),
            MathTex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}")
        )

        # Step 8: Final simplification
        step8 = self.create_smart_step(
            "Step 8: Factor and simplify",
            MathTex(r"x = \frac{2(-5 \pm 2\sqrt{3})}{2}"),
            MathTex(r"x = -5 \pm 2\sqrt{3}")
        )

        # Final answer
        final_answer = self.create_smart_step(
            "Final Answer:",
            MathTex(r"x = -5 + 2\sqrt{3} \quad \text{or} \quad x = -5 - 2\sqrt{3}"),
            MathTex(r"x \approx -1.54 \quad \text{or} \quad x \approx -8.46")
        )

        # Arrange all steps
        solution = VGroup(
            starting_eq,
            step1,
            step2, 
            step3,
            step4,
            step5,
            step6,
            step7,
            step8,
            final_answer
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        solution.to_edge(LEFT, buff=1).to_edge(UP, buff=0.5)
        self.add(solution)