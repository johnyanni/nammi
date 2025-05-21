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
        
        setup_step = self.create_labeled_step_vertical_tex(
            "Goal: Write the equation in standard form",
            r"4(x+5)^2=48"
        )

        # Create step 1 with annotated equation
        step_1 = self.create_labeled_step_vertical_tex(
            "Divide both sides by 4",
            [
                self.create_annotated_equation(
                    r"4(x+5)^2=48",  # Equation text
                    r"\div 4",       # Annotation
                    "4", "48"
                ), 
                r"(x+5)^2=12"
            ]
        )

        step_2 = self.create_labeled_step_vertical_tex(
            "Expand the squared term",
            r"x^2 + 10x + 25 = 12"
        )

        step_3_annotated = self.create_annotated_equation(
                    r"x^2 + 10x + 25 = 12",  # Equation text
                    r"-12",                  # Annotation
                    "25", "12"               # Terms to annotate
                )
        
        # Create step 3 with annotated equation
        step_3 = self.create_labeled_step_vertical_tex(
            "Subtract 12 from both sides",
            [
                step_3_annotated, 
                r"x^2 + 10x + 13 = 0"
            ]
        )
        
        

        solution = VGroup(setup_step, step_1, step_2, step_3).arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        solution.next_to(question_group, DOWN, buff=0.3).align_to(question_group, LEFT)


        step_3_label = step_3[0]
        # step_3_exp1 = step_3[1][0][0]
        # step_3_exp1_annotation = step_3[1][0][1]
        # step_3_exp2 = step_3[1][1]
        
        self.play(Write(step_3_label))
        
        step_3_exp1 = step_3_annotated[0]
        step_3_exp1_annotation = step_3_annotated[1]
        
        self.play(Write(step_3_exp1))
        self.play(Write(step_3_exp1_annotation))
        
       