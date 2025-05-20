from manim import *
from src.components.common.base_scene import *

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
        
        LABEL_BUFFER = 0.1
        ELEMENT_BUFF = 0.2  # Buffer between elements in a step
        STEP_BUFF = 0.7     # Buffer between steps
        
        
        ###############################################################################
        # SECTION 1: FORMULA/HELPERS 
        ###############################################################################

        # Create the generic quadratic equation
        quadratic_form_title = Tex("Standard Form").scale(TEXT_SCALE)
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        
        # Find the coefficients in the general equation
        quad_form_a = quadratic_form[0][0]  # 'a' is typically first character
        quad_form_b = quadratic_form[0][4]  # 'b' is typically at position 4
        quad_form_c = quadratic_form[0][7]  # 'c' is typically at position 8
        
        quadratic_form_group = Group(
            quadratic_form_title,
            quadratic_form
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        # Create the quadratic formula
        quadratic_formula_title = Tex("Quadratic Formula").scale(TEXT_SCALE)
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        
        quadratic_formula_group = Group(
            quadratic_formula_title,
            quadratic_formula
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        # Arrange the quadratic equation and formula
        quadratic_group = Group(
            quadratic_form_group,
            quadratic_formula_group
        ).arrange(RIGHT, aligned_edge=UP, buff=0.6).to_corner(UR, buff=0.6)
        
        quadratic_form_bg = SurroundingRectangle(
            quadratic_form_group,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula_group,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )

        
        ###############################################################################
        # SECTION 2: SOLVING THE EQUATION
        ###############################################################################
        
        
 
        step1_label = Tex("Get the equation in standard form", color="#DBDBDB").scale(TEXT_SCALE)
        step1_expr = MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        step1 = VGroup(step1_label, step1_expr).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)
        

        step2_label = Tex("Divide both sides by 4", color="#DBDBDB").scale(TEXT_SCALE)
        step2_expr1 = self.create_annotated_expression(
            "4(x+5)^2=48", 
            annotations=[(r"\div 4", "4", "48", GREEN)]
        )

        step2_expr2 = MathTex("(x+5)^2=12").scale(TEX_SCALE)
        
        # Group the expressions
        step2_exprs = VGroup(step2_expr1, step2_expr2).arrange(DOWN, buff=ELEMENT_BUFF)
        step2 = VGroup(step2_label, step2_exprs).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)
        

        step3_label = Tex("Expand the squared term", color="#DBDBDB").scale(TEXT_SCALE)
        step3_expr1 = MathTex("x^2 + 10x + 25 = 12").scale(TEX_SCALE)
        
        step3 = VGroup(step3_label, step3_expr1).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)
        

        step4_label = Tex("Subtract 12 from both sides", color="#DBDBDB").scale(TEXT_SCALE)
        step4_expr1 = self.create_annotated_expression(
            "x^2 + 10x + 25 = 12",
            annotations=[("-12", "25", "12", RED)]
        )
        
        step4_expr2 = MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)

        step4_exprs = VGroup(step4_expr1, step4_expr2).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        step4 = VGroup(step4_label, step4_exprs).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)

        solution = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        
        solution.to_edge(UP, buff=0.1).to_edge(LEFT, buff=1)
        
        self.add(solution)