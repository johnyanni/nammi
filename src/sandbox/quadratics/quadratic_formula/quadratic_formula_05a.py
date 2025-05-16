from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class QuadraticFormula05(MathTutorialScene):
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
        
        
        
        
        ###############################################################################
        # SOLVING THE EQUATION
        ###############################################################################       
        
        sol_step_0 = self.create_labeled_step(
            "Use the quadratic formula",
            MathTex(r"x \ = \ \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        )
        
        step_0_label, step_0_exp = sol_step_0
        step_0_exp = step_0_exp[0]

        
        sol_step_1 = self.create_labeled_step(
            "Step 1: Substitute the coefficients",
            MathTex(r"x = \frac{-(11) \pm \sqrt{(11)^2 - 4(1)(20)}}{2(1)}").scale(TEX_SCALE)
        )
        
        step_1_label, step_1_exp_group = sol_step_1
        step_1_exp = step_1_exp_group[0]  # Get the actual MathTex object
        
        
        formula_template = MathTex(r"x = \frac{-(\phantom{11}) \pm \sqrt{(\phantom{11})^2 - 4(\phantom{1})(\phantom{20})}}{2(\phantom{1})}").scale(TEX_SCALE)
        
        formula_template.move_to(step_1_exp.get_center())


        # ---- COEFFICIENT VALUES (SEPARATE) ----
        # Get all instances of coefficients separately
        step_1_b_parts = self.find_elements("11", step_1_exp, as_group=False)
        step_1_a_parts = self.find_elements("1", step_1_exp, as_group=False)
        step_1_c_part = self.find_element("20", step_1_exp)

        # Specifically name each coefficient by its position for clarity
        b_in_fraction = step_1_b_parts[0]  # The 11 in -(11)
        b_in_sqrt = step_1_b_parts[1]      # The 11 in (11)^2

        a_in_4ac = step_1_a_parts[4]       # The 1 in 4(1)(20)
        a_in_denominator = step_1_a_parts[5]  # The 1 in 2(1)

        c_in_4ac = step_1_c_part           # The 20 in 4(1)(20)





        
        
        
        
        
        
        
        
        self.apply_smart_colorize(
            [step_0_exp],
            {
                "x": X_COLOR,
                "1": A_COLOR,
                "20": C_COLOR,
                "121": WHITE,
                "41": WHITE,
                "11": B_COLOR,
                "b": B_COLOR,
                "c": C_COLOR,
                "a": A_COLOR,
            }
        )
        
        solution_steps = Group(
            sol_step_1
        ).arrange(DOWN, aligned_edge=LEFT)
        
        solution_steps.next_to(coefficients, DOWN * 2.5)
  
        
        ###############################################################################
        # ANIMATIONS
        ###############################################################################
        
        self.play(
            FadeIn(
                quadratic_group,
                quadratic_form_bg,
                quadratic_formula_bg
            )
        )
        
        self.play(Write(q_equation))        
        
        self.play(
            FadeIn(a[0][:2], b[0][:2], c[0][:2])
        )
        
        self.play(self.indicate(quad_form_a))
        
        self.play(FadeIn(a_value, target_position=a_in_q_equation), run_time=2)
        
        self.play(self.indicate(quad_form_b))
        
        self.play(FadeIn(b_value, target_position=b_in_q_equation), run_time=2)
        
        self.play(self.indicate(quad_form_c))
        
        self.play(FadeIn(c_value, target_position=c_in_q_equation), run_time=2)

        self.play(Write(step_0_label))

        
        
        
        # Animate the template appearing
        self.play(Write(formula_template), run_time=2)
        self.wait(0.5)

        # At this point, the entire formula with empty spaces is showing
        # Now we can animate substituting each coefficient

        # Substitute b values
        self.play(self.indicate(b))  # Highlight b = 11
        self.play(ReplacementTransform(b_value.copy(), b_in_fraction), run_time=1.5)
        self.play(ReplacementTransform(b_value.copy(), b_in_sqrt), run_time=1.5)

        # Substitute a values
        self.play(self.indicate(a))  # Highlight a = 1
        self.play(ReplacementTransform(a_value.copy(), a_in_4ac), run_time=1.5)
        self.play(ReplacementTransform(a_value.copy(), a_in_denominator), run_time=1.5)

        # Substitute c value
        self.play(self.indicate(c))  # Highlight c = 20
        self.play(ReplacementTransform(c_value.copy(), c_in_4ac), run_time=1.5)