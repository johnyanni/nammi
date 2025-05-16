from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


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

       

        ###############################################################################
        # SECTION 1: FORMULA/HELPERS 
        ###############################################################################

        # Create the generic quadratic equation
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE).to_corner(UL, buff=0.6)
        SmartColorizeStatic(quadratic_form, {"2": X_COLOR})
        
        # Find the coefficients in the general equation
        quad_form_a = quadratic_form[0][0]  # 'a' is typically first character
        quad_form_b = quadratic_form[0][4]  # 'b' is typically at position 4
        quad_form_c = quadratic_form[0][7]  # 'c' is typically at position 8
        
        # Create the quadratic formula
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE).to_corner(UR, buff=0.6)
        
        
        
        # Arrange the quadratic equation and formula
        quadratic_group = Group(
            quadratic_form,
            quadratic_formula
        )
        
        self.apply_smart_colorize(
            quadratic_group,
            {
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "a": A_COLOR,
            }
        )
        
        quadratic_form_bg = SurroundingRectangle(
            quadratic_form,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        
        ###############################################################################
        # GIVEN EQUATION AND SETUP
        ###############################################################################
        
        
        q_equation = MathTex("1x^2 + 11x + 20 = 0").scale(TEX_SCALE).to_edge(UP, buff=0.6)
        
        SmartColorizeStatic(
            q_equation,
            {
                "x": X_COLOR,
                "2": X_COLOR,
            }
        )
        
        a_in_q_equation = self.find_element("1", q_equation, opacity=0)
        b_in_q_equation = self.find_element("11", q_equation, color=B_COLOR)
        c_in_q_equation = self.find_element("20", q_equation, color=C_COLOR)
        
        
        # Create coefficient labels
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = 11", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = 20", color=C_COLOR).scale(TEX_SCALE)
        
        a_value = self.find_element("1", a)
        b_value = self.find_element("11", b)
        c_value = self.find_element("20", c)
        
        coefficients = Group(a, b, c).arrange(buff=1).next_to(q_equation, DOWN * 1.5)
        
        
        
        
        placeholder_template = r"x = \frac{-(\Box) \pm \sqrt{(\Box)^2 - 4(\Box)(\Box)}}{2(\Box)}"
        sol_step_1 = self.create_labeled_step(
            "Step 1: Substitute the coefficients",
            MathTex(placeholder_template).scale(TEX_SCALE)
        )

        step_1_label, step_1_exp_group = sol_step_1
        step_1_exp = step_1_exp_group[0]  # Get the actual MathTex object

        # Find all box placeholders
        box_placeholders = self.find_elements(r"\Box", step_1_exp)

        # Make the placeholders more transparent but not completely invisible
        for placeholder in box_placeholders:
            placeholder.set_opacity(0.2)  # Slightly visible to help with positioning

        # Create the values with appropriate styling
        b_value_fraction = MathTex("11").scale(TEX_SCALE).set_color(B_COLOR).move_to(box_placeholders[0])
        b_value_sqrt = MathTex("11").scale(TEX_SCALE).set_color(B_COLOR).move_to(box_placeholders[1])
        a_value_4ac = MathTex("1").scale(TEX_SCALE).set_color(A_COLOR).move_to(box_placeholders[2])
        c_value_4ac = MathTex("20").scale(TEX_SCALE).set_color(C_COLOR).move_to(box_placeholders[3])
        a_value_denominator = MathTex("1").scale(TEX_SCALE).set_color(A_COLOR).move_to(box_placeholders[4])

        # Animations
        self.play(Write(step_1_label))
        self.play(Write(step_1_exp))
        self.wait(0.5)

        # Now make the placeholders completely invisible
        for placeholder in box_placeholders:
            placeholder.set_opacity(0)

        self.play(FadeIn(b_value_fraction))
        self.wait(0.2)
        self.play(FadeIn(b_value_sqrt))
        self.wait(0.2)
        self.play(FadeIn(a_value_4ac))
        self.wait(0.2)
        self.play(FadeIn(c_value_4ac))
        self.wait(0.2)
        self.play(FadeIn(a_value_denominator))