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
        
        
        
        
        setup_step = self.create_labeled_step_vertical_tex(
            "Goal: Write the equation in standard form",
            r"4(x+5)^2=48"
        )
        
        
        step_1_exp1 = MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        
        step_1_exp1_annotations = self.add_annotations(
            r"\div 4",
            self.find_element("4", step_1_exp1),
            self.find_element("48", step_1_exp1)
        )
        
        step_1_exp1_annotated = VGroup(step_1_exp1, step_1_exp1_annotations)
        
        
        step_1 = self.create_labeled_step_vertical_tex(
            "Divide both sides by 4",
            [
                step_1_exp1_annotated, 
                r"(x+5)^2=12"
            ]
        )
        
        step_2 = self.create_labeled_step_vertical_tex(
            "Expand the squared term",
            r"x^2 + 10x + 25 = 12"
        )
        
        step_3_exp1 = MathTex("x^2 + 10x + 25 = 12").scale(TEX_SCALE)
        
        step_3_exp1_annotations = self.add_annotations(
            r"-12",
            self.find_element("25", step_3_exp1),
            self.find_element("12", step_3_exp1)
        )
        
        step_3_exp1_annotated = VGroup(step_3_exp1, step_3_exp1_annotations)
        
        step_3 = self.create_labeled_step_vertical_tex(
            "Subtract 12 from both sides",
            [
                step_3_exp1_annotated, 
                r"x^2 + 10x + 13 = 0"
            ]
        )
        
        solution = VGroup(setup_step, step_1, step_2, step_3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.add(solution)
        
        

