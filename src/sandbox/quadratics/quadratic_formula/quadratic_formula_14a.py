from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager
from src.components.common.math_indices import MathIndices

class QuadraticFormula3(MathTutorialScene):
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
        
        q_equation = MathTex("x^2 - 6x + 8 = 0").scale(TEX_SCALE).to_edge(UP, buff=0.6)
        
        a_in_q_equation = self.find_element("1", q_equation, color=A_COLOR)      
        b_in_q_equation = self.find_element("-6", q_equation, color=B_COLOR)      
        c_in_q_equation = self.find_element("8", q_equation, color=C_COLOR)      
        
        # Create coefficient labels
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = -6", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = 8", color=C_COLOR).scale(TEX_SCALE)
        
        a_value = self.find_element("1", a)
        b_value = self.find_element("-6", b)
        c_value = self.find_element("8", c)
        
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
            MathTex(r"x = \frac{-(-6) \pm \sqrt{(-6)^2 - 4(1)(8)}}{2(1)}").scale(TEX_SCALE)
        )
        
        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]
        
        sol_step_2 = self.create_labeled_step(
            "Step 2: Simplify the expression",
            MathTex(r"x = \frac{6 \pm \sqrt{36 - 32}}{2}").scale(TEX_SCALE)
        )
        
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]
        
        sol_step_3 = self.create_labeled_step(
            "Step 3: Continue simplifying",
            MathTex(r"x = \frac{6 \pm \sqrt{4}}{2}").scale(TEX_SCALE)
        )
        
        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]
        
        sol_step_4 = self.create_labeled_step(
            "Step 4: Find the two roots",
            MathTex(r"x = \frac{6 \pm 2}{2}").scale(TEX_SCALE)
        )
        
        step_4_label, step_4_exp = sol_step_4[0], sol_step_4[1]
        
        sol_step_5 = self.create_labeled_step(
            "Final solution",
            MathTex(r"x = \frac{6 + 2}{2} = 4 \ \text{or} \ x = \frac{6 - 2}{2} = 2").scale(TEX_SCALE)
        )
        
        step_5_label, step_5_exp = sol_step_5[0], sol_step_5[1]
        
        

        b_in_frac = self.find_element("-6", step_1_exp, context="x=-(-6)", opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("-6", step_1_exp, context="-6", opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("1", step_1_exp, context="4(1)", opacity=0, color=A_COLOR)
        c_in_4ac = self.find_element("8", step_1_exp, context=")(8)2", opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("1", step_1_exp, context="2(1)", opacity=0, color=A_COLOR)

        # 3. Create visible copies with the SAME initial positions
        visible_b_frac = b_in_frac.copy().set_opacity(1)
        visible_b_sqrt = b_in_sqrt.copy().set_opacity(1)
        visible_a_4ac = a_in_4ac.copy().set_opacity(1)
        visible_a_denom = a_in_denom.copy().set_opacity(1)
        visible_c_4ac = c_in_4ac.copy().set_opacity(1)

        # 4. Add these copies to step_1_exp NOW to maintain relative positioning
        substitution = VGroup(visible_b_frac, visible_b_sqrt, visible_a_4ac, visible_a_denom, visible_c_4ac)
        step_1_exp.add(*substitution)
        
        self.apply_smart_colorize(
            [quadratic_form, quadratic_formula, step_0_exp],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        solution_steps = VGroup(
            sol_step_0,
            sol_step_1,
            sol_step_2,
            sol_step_3,
            sol_step_4,
            sol_step_5
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(coefficients, DOWN * 2.5)
        

        math_indices = MathIndices()
        math_indices.display_indices(self, step_1_exp, "step_1_exp", display_duration=3)
        
        ordered_steps = VGroup(
            step_0_label, step_0_exp,
            step_1_label, step_1_exp,
            *substitution,
            step_2_label, step_2_exp,
            step_3_label, step_3_exp,
            step_4_label, step_4_exp,
            step_5_label, step_5_exp
        )
        scroll_mgr = ScrollManager(ordered_steps)
        

        
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
           
        
        # Then after showing step_0 and step_1:
        scroll_mgr.prepare_next(self)  # Shows step_0_label
        scroll_mgr.prepare_next(self)  # Shows step_0_exp
        scroll_mgr.prepare_next(self)  # Shows step_1_label
        scroll_mgr.prepare_next(self)  # Shows step_1_exp

        scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_frac from b_value
        scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_sqrt from b_value
        scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_4ac from a_value
        scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_denom from a_value
        scroll_mgr.fade_in_from_target(self, c_value)  # Fades in visible_c_4ac from c_value
    
        scroll_mgr.scroll_down(self, steps=2)
        
        
        # Display the next steps
        scroll_mgr.prepare_next(self)  # Shows sol_step_2
        scroll_mgr.prepare_next(self)  # Shows sol_step_3
        scroll_mgr.prepare_next(self)  # Shows sol_step_4
        scroll_mgr.prepare_next(self)  # Shows sol_step_5

        
        self.wait(2)