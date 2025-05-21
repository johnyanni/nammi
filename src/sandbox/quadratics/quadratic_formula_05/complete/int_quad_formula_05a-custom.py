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


        # step_3_label = step_3[0]
        # # step_3_exp1 = step_3[1][0][0]
        # # step_3_exp1_annotation = step_3[1][0][1]
        # # step_3_exp2 = step_3[1][1]
        
        # self.play(Write(step_3_label))
        
        # step_3_exp1 = step_3_annotated[0]
        # step_3_exp1_annotation = step_3_annotated[1]
        
        # self.play(Write(step_3_exp1))
        # self.play(Write(step_3_exp1_annotation))
        
       
       
       
       #PASTE
       
       
    #    # Initial step with equation
    #     step = self.create_labeled_step_vertical_tex(
    #         "Solving step-by-step",
    #         "x^2 - 4 = 0"
    #     )

    #     step_label = step[0]
    #     initial_eq = step[1][0]  # Get the equation from the step

    #     # Create target equations (but don't add to scene yet)
    #     eq2 = MathTex("x^2 = 4").scale(MATH_SCALE).arrange(aligned_edge=LEFT)
    #     eq3 = MathTex("x = \\pm 2").scale(MATH_SCALE).arrange(aligned_edge=LEFT)

    #     # Animation sequence
    #     self.play(TransformMatchingTex(initial_eq, eq2))
    #     # Update the equation in our step
    #     step[1][0] = eq2
    #     self.wait()
    #     self.play(TransformMatchingTex(eq2, eq3))
    #     # Update the equation in our step again
    #     step[1][0] = eq3
        
        
        
        
    #     # Create initial step with base equation
    #     step = self.create_labeled_step_vertical_tex(
    #         "Solve for x",
    #         "3x + 5 = 11"
    #     )

    #     step_label = step[0]
    #     base_eq = step[1][0]  # The equation

    #     # Create annotation to add later
    #     annotation = MathTex("-5").set_color(RED)
    #     term_5 = self.find_element("5", base_eq)
    #     annotation.next_to(term_5, DOWN)

    #     # Animation sequence
    #     self.play(FadeIn(annotation))
    #     new_eq = MathTex("3x = 6")
    #     self.play(
    #         TransformMatchingTex(base_eq, new_eq),
    #         FadeOut(annotation)
    #     )
    #     # Update the equation in our step
    #     step[1][0] = new_eq
        
        
        
        

        
        
        step1 = self.create_labeled_step_vertical_tex(
            "Step 1",
            "2x + 3y = 8"
        )

        step2 = self.create_labeled_step_vertical_tex(
            "Step 2",
            "5x - 2y = 7" 
        )

        # Arrange steps FIRST
        steps = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.add(steps)

        # THEN get the equations at their final positions
        eq1 = step1[1][0]
        eq2 = step2[1][0]

        # Find specific terms to connect at their final positions
        x_term1 = self.find_element("x", eq1)
        x_term2 = self.find_element("x", eq2)

        # Create the arrow connecting them at their final positions
        arrow = Arrow(
            x_term1.get_center(),
            x_term2.get_center(),
            buff=0.2
        ).set_color(YELLOW)

        # Now add the arrow
        self.add(arrow)