from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class QuadraticFormula2(MathTutorialScene):
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
        
        
        q_equation = MathTex("2x^2 - 5x - 3 = 0").scale(TEX_SCALE).to_edge(UP, buff=0.6)
        
        
        a_in_q_equation = self.find_element("2", q_equation, color=A_COLOR)      
        b_in_q_equation = self.find_element("-5", q_equation, color=B_COLOR)      
        c_in_q_equation = self.find_element("-3", q_equation, color=C_COLOR)      

        
        # Create coefficient labels
        a = MathTex("a = 2", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = -5", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = -3", color=C_COLOR).scale(TEX_SCALE)
        
        a_value = self.find_element("2", a)
        b_value = self.find_element("-5", b)
        c_value = self.find_element("-3", c)
        
        coefficients = Group(a, b, c).arrange(buff=1).next_to(q_equation, DOWN * 1.5)
        
        
        
        
        ###############################################################################
        # SOLVING THE EQUATION
        ###############################################################################       
        
        sol_step_0 = self.create_labeled_step(
            "Use the quadratic formula",
            MathTex(r"x \quad = \quad \frac{ \ -b \pm \sqrt{ \ b^2 \ - \ 4ac \ }}{2a}").scale(TEX_SCALE)
        )
        
        step_0_label, step_0_exp = sol_step_0[0], sol_step_0[1]

        
        sol_step_1 = self.create_labeled_step(
            "Step 1: Substitute the coefficients",
            MathTex(r"x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(2)(-3)}}{2(2)}").scale(TEX_SCALE)
        )

        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]  # Get the actual MathTex object

        sol_step_2 = self.create_labeled_step(
            "Step 2: Simplify the expression",
            MathTex(r"x = \frac{5 \pm \sqrt{25 + 24}}{4}").scale(TEX_SCALE)
        )
        
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]

        # Find all coefficient values
        b_in_frac = self.find_element("-5", step_1_exp, nth=0, opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("-5", step_1_exp, nth=1, opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("2", step_1_exp, nth=1, opacity=0, color=A_COLOR)  
        c_in_4ac = self.find_element("-3", step_1_exp, opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("2", step_1_exp, nth=-1, opacity=0, color=A_COLOR)  
        



        self.apply_smart_colorize(
            [quadratic_group, step_0_exp],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        


        
        solution_steps = Group(
            sol_step_0,
            sol_step_1,
            sol_step_2
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
        self.play(Write(step_0_exp))

        self.play(Write(step_1_label)) 
        self.play(Write(step_1_exp))
        
        # Do your coefficient transformations
        self.play(ReplacementTransform(b_value.copy(), b_in_frac.copy().set_opacity(1)))
        self.play(ReplacementTransform(b_value.copy(), b_in_sqrt.copy().set_opacity(1)))
        self.play(ReplacementTransform(a_value.copy(), a_in_4ac.copy().set_opacity(1)))
        self.play(ReplacementTransform(a_value.copy(), a_in_denom.copy().set_opacity(1)))
        self.play(ReplacementTransform(c_value.copy(), c_in_4ac.copy().set_opacity(1)))


        # Write sol_step_2
        self.play(Write(step_2_label))
        self.play(Write(step_2_exp))
        
        
        
        
        self.wait(2)