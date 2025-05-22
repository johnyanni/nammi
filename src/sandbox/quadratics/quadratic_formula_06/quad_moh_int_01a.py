from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.annotation import Annotation

config.verbosity = "ERROR"

class QuadraticFormula(MathTutorialScene):
    def construct(self):
        # Constants
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
        # LABEL_BUFFER = 0.1
        # ELEMENT_BUFF = 0.2  # Buffer between elements in a step
        # STEP_BUFF = 0.7     # Buffer between steps
        
        
        # Problem statement with better organization
        question_title = Tex("Solve using the quadratic formula:").scale(TEXT_SCALE)
        question_equation = MathTex("4(x+5)^2=48").scale(MATH_SCALE)
        
        question_group = VGroup(question_title, question_equation).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1)
        question_group.to_edge(UP, buff=0.3).to_edge(LEFT, buff=0.7)

        self.add(question_group)
        
        
        
        
        step1_list = [
            "Get the equation in standard form",
            MathTex("4(x+5)^2=48")
        ]


        step2_list = [
            "Divide both sides by 4",
            MathTex("4(x+5)^2=48"),
            Annotation(r"\div 4", "4", "48", color = GREEN),
            MathTex("(x+5)^2=12")
        ]


        step3_list = [
            "Expand the squared term",
            MathTex("x^2 + 10x + 25 = 12")
        ]

        
        step4_list = [
            "Subtract 12 from both sides",
            MathTex("x^2 + 10x + 25 = 12"),
            
            Annotation(
               "-12",
                self.find_element_lazy("25"),
                self.find_element_lazy("12"),
                color=RED,
            ),
            MathTex("x^2 + 10x + 13 = 0")
        ]

            
        solution = self.create_ordered_steps(step1_list, step2_list, step3_list, step4_list)
        step1, step2, step3, step4 = solution
        
        solution.arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        solution.next_to(question_group, DOWN, buff=0.8).align_to(question_group, LEFT)

        
        
        
        
        
        print(len(step2))

        pre_ordered_steps = VGroup(
            *step1,
            *step2,
            *step3,
            *step4,
        )
        
        
        
        self.add(pre_ordered_steps)
        
        
        # pre_scroll_mgr = ScrollManager(pre_ordered_steps)
        
        # self.play(Write(question_title_group))
        
        # pre_scroll_mgr.prepare_next(self)  # Shows step1_label
        # pre_scroll_mgr.prepare_next(self)  # Shows step1_expr

        # pre_scroll_mgr.prepare_next(self)  # Shows step2_label
        # pre_scroll_mgr.prepare_next(self)  # Shows main expression (step2_expr1[0])
        
        # pre_scroll_mgr.prepare_next(self)  # Shows annotation (step2_expr1[2])
        
        # pre_scroll_mgr.prepare_next(self)  # Shows step2_expr2
        
        # pre_scroll_mgr.scroll_down(self, steps=2)

        # pre_scroll_mgr.prepare_next(self)  # Shows step3_label
        # pre_scroll_mgr.prepare_next(self)  # Shows step3_expr1
        
        # pre_scroll_mgr.scroll_down(self, steps=3)

        # pre_scroll_mgr.prepare_next(self)  # Shows step4_label
        # pre_scroll_mgr.prepare_next(self)  # Shows step4_expr1
        # pre_scroll_mgr.prepare_next(self)  # Shows main expression (step2_expr1[0])

        # pre_scroll_mgr.prepare_next(self)  # Shows step4_expr2
        
        # self.play(FadeOut(solution))
        