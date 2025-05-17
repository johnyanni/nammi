from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

class QuadraticFormula4(MathTutorialScene):
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
        # GIVEN EQUATION AND SETUP - NEW EQUATION
        ###############################################################################
        
        # New equation: 2x² + 5x - 3 = 0
        q_equation = MathTex("2x^2 + 5x - 3 = 0").scale(TEX_SCALE).to_edge(UP, buff=0.6)
        
        a_in_q_equation = self.find_element("2", q_equation, color=A_COLOR)      
        b_in_q_equation = self.find_element("5", q_equation, color=B_COLOR)      
        c_in_q_equation = self.find_element("-3", q_equation, color=C_COLOR)      
        
        # Create coefficient labels with new values
        a = MathTex("a = 2", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = 5", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = -3", color=C_COLOR).scale(TEX_SCALE)
        
        a_value = self.find_element("2", a)
        b_value = self.find_element("5", b)
        c_value = self.find_element("-3", c)
        
        coefficients = Group(a, b, c).arrange(buff=1).next_to(q_equation, DOWN * 1.5)
        
        ###############################################################################
        # SOLVING THE EQUATION - WITH NEW VALUES
        ###############################################################################       
        
        sol_step_0 = self.create_labeled_step(
            "Use the quadratic formula",
            MathTex(r"x \quad = \quad \frac{ \ -b \pm \sqrt{ \ b^2 \ - \ 4ac \ }}{2a}").scale(TEX_SCALE)
        )
        
        step_0_label, step_0_exp = sol_step_0[0], sol_step_0[1]
        
        sol_step_1 = self.create_labeled_step(
            "Step 1: Substitute the coefficients",
            MathTex(r"x = \frac{-(5) \pm \sqrt{(5)^2 - 4(2)(-3)}}{2(2)}").scale(TEX_SCALE)
        )
        
        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]
        
        sol_step_2 = self.create_labeled_step(
            "Step 2: Simplify the expression",
            MathTex(r"x = \frac{-5 \pm \sqrt{25 - 4(2)(-3)}}{4}").scale(TEX_SCALE)
        )
        
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]
        
        sol_step_3 = self.create_labeled_step(
            "Step 3: Continue simplifying",
            MathTex(r"x = \frac{-5 \pm \sqrt{25 + 24}}{4}").scale(TEX_SCALE)
        )
        
        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]
        
        sol_step_4 = self.create_labeled_step(
            "Step 4: Calculate the square root",
            MathTex(r"x = \frac{-5 \pm \sqrt{49}}{4}").scale(TEX_SCALE)
        )
        
        step_4_label, step_4_exp = sol_step_4[0], sol_step_4[1]
        
        sol_step_5 = self.create_labeled_step(
            "Step 5: Find the two roots",
            MathTex(r"x = \frac{-5 \pm 7}{4}").scale(TEX_SCALE)
        )
        
        step_5_label, step_5_exp = sol_step_5[0], sol_step_5[1]
        
        sol_step_6 = self.create_labeled_step(
            "Final solution",
            MathTex(r"x = \frac{-5 + 7}{4} = \frac{1}{2} \ \text{or} \ x = \frac{-5 - 7}{4} = -3").scale(TEX_SCALE)
        )
        
        step_6_label, step_6_exp = sol_step_6[0], sol_step_6[1]
        
        # Find elements in step_1_exp to highlight and animate
        b_in_frac = self.find_element("5", step_1_exp, nth=0, opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("5", step_1_exp, nth=1, opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("2", step_1_exp, nth=1, opacity=0, color=A_COLOR)
        c_in_4ac = self.find_element("-3", step_1_exp, nth=0, opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("2", step_1_exp, nth=-1, opacity=0, color=A_COLOR)

        # Create visible copies with the same initial positions
        visible_b_frac = b_in_frac.copy().set_opacity(1)
        visible_b_sqrt = b_in_sqrt.copy().set_opacity(1)
        visible_a_4ac = a_in_4ac.copy().set_opacity(1)
        visible_a_denom = a_in_denom.copy().set_opacity(1)
        visible_c_4ac = c_in_4ac.copy().set_opacity(1)

        # Add these copies to step_1_exp to maintain relative positioning
        substitution = VGroup(visible_b_frac, visible_b_sqrt, visible_a_4ac, visible_a_denom, visible_c_4ac)
        step_1_exp.add(*substitution)
        
        # Apply coloring to formula components
        self.apply_smart_colorize(
            [quadratic_form, quadratic_formula, step_0_exp],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        # Arrange all solution steps
        solution_steps = VGroup(
            sol_step_0,
            sol_step_1,
            sol_step_2,
            sol_step_3,
            sol_step_4,
            sol_step_5,
            sol_step_6
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(coefficients, DOWN * 2.5)
        
        # Create ordered steps for scroll manager
        ordered_steps = VGroup(
            step_0_label, step_0_exp,
            step_1_label, step_1_exp,
            *substitution,
            step_2_label, step_2_exp,
            step_3_label, step_3_exp,
            step_4_label, step_4_exp,
            step_5_label, step_5_exp,
            step_6_label, step_6_exp
        )
        
        scroll_mgr = ScrollManager(ordered_steps)
        steps_to_scroll = len(substitution) + 2
        
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
           
        # Show step_0 and step_1
        scroll_mgr.prepare_next(self)  # Shows step_0_label
        scroll_mgr.prepare_next(self)  # Shows step_0_exp
        scroll_mgr.prepare_next(self)  # Shows step_1_label
        scroll_mgr.prepare_next(self)  # Shows step_1_exp

        # Animate the coefficient substitutions
        scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_frac from b_value
        scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_sqrt from b_value
        scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_4ac from a_value
        scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_denom from a_value
        scroll_mgr.fade_in_from_target(self, c_value)  # Fades in visible_c_4ac from c_value
    
        scroll_mgr.scroll_down(self, steps=2)
        
        # Show steps 2 and 3
        scroll_mgr.prepare_next(self)  # Shows step_2_label
        scroll_mgr.prepare_next(self)  # Shows step_2_exp
        scroll_mgr.prepare_next(self)  # Shows step_3_label
        scroll_mgr.prepare_next(self)  # Shows step_3_exp

        # Scroll again
        scroll_mgr.scroll_down(self, steps=steps_to_scroll)

        # Show steps 4 and 5
        scroll_mgr.prepare_next(self)  # Shows step_4_label
        scroll_mgr.prepare_next(self)  # Shows step_4_exp
        scroll_mgr.prepare_next(self)  # Shows step_5_label
        scroll_mgr.prepare_next(self)  # Shows step_5_exp
        
        # Final scroll and show solution
        scroll_mgr.scroll_down(self, steps=2)
        scroll_mgr.prepare_next(self)  # Shows step_6_label
        scroll_mgr.prepare_next(self)  # Shows step_6_exp
        
        self.wait(2)