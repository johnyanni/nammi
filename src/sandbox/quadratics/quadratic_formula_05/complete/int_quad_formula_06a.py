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
        
 
        
        
        pre_sol_step_0 = self.create_multi_exp_labeled_step(
            "Get the equation in standard form",
            MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        )
        
        pre_sol_step_0_label, pre_sol_step_0_exp = pre_sol_step_0[0], pre_sol_step_0[1]
        
        step_1_exp1 = MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        div_4 = self.add_annotations(
            r"\div 4",
            self.find_element("4", step_1_exp1),
            self.find_element("48", step_1_exp1),
            color=GREEN
        )
        
        step_1_annotated = VGroup(step_1_exp1, div_4).arrange(DOWN, aligned_edge=LEFT, buff=0)
        
        pre_sol_step_1 = self.create_multi_exp_labeled_step(
            "Divide both sides by 4",
            step_1_annotated,
            MathTex("(x+5)^2=12").scale(TEX_SCALE)
        )
        
        pre_sol_step_1_label = pre_sol_step_1[0]
        pre_sol_step_1_exp1 = pre_sol_step_1[1][0][0]  
        pre_sol_step_1_annotation = pre_sol_step_1[1][0][1]
        pre_sol_step_1_exp2 = pre_sol_step_1[1][1]
        
        
        no1 = MathTex("12").scale(TEX_SCALE)
        no2 = MathTex("15").scale(TEX_SCALE)
        
        grouped = VGroup(no1, no2).arrange(DOWN, aligned_edge=LEFT, buff=1.8)
        

        
        pre_sol_step_2 = self.create_multi_exp_labeled_step(
            "Expand the squared term",
            grouped
        )
        
        pre_sol_step_2_label = pre_sol_step_2[0]
        pre_sol_step_2_exp = pre_sol_step_2[1][0]  # First expression
        
        pre_sol_step_3 = self.create_multi_exp_labeled_step(
            "Subtract 12 from both sides",
            MathTex("x^2 + 10x + 25 = 12").scale(TEX_SCALE)
        )
        
        pre_sol_step_3_label, pre_sol_step_3_exp = pre_sol_step_3[0], pre_sol_step_3[1]
        
        final_equation = MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)
        

        
        subtract_12 = self.add_annotations(
            "-12",
            self.find_element("25", pre_sol_step_3_exp[0]),
            self.find_element("12", pre_sol_step_3_exp[0]),
            color=RED,
        )

        pre_solution_steps = VGroup(
            pre_sol_step_0,
            pre_sol_step_1,
            pre_sol_step_2,
            VGroup(pre_sol_step_3, subtract_12),
            final_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)

       
        
        
        # Step 1: Expand and rewrite in standard form
        self.add(pre_solution_steps)
