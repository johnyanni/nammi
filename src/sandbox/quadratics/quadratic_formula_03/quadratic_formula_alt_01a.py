from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

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
        
        ANNOTATION_SPACING = 0.7

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
        # GIVEN EQUATION AND SETUP - NEW EQUATION
        ###############################################################################
        
        question_title_group = VGroup(
            Tex("Solve using the quadratic formula:").scale(0.6),
            MathTex("-x^2 - 3x = - 9").scale(0.6)
        )
        
        question_title_group.arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)
        
        
        
        
        
        
        
        
        pre_sol_step_0 = self.create_labeled_step(
            "Rewrite in standard quadratic form",
            MathTex("-x^2 - 3x = - 9").scale(TEX_SCALE)
        )
        
        pre_sol_step_0_label, pre_sol_step_0_exp = pre_sol_step_0[0], pre_sol_step_0[1]
        
        final_equation = MathTex("-x^2 - 3x + 9 = 0").scale(TEX_SCALE)

        
        pre_solution_steps = VGroup(
            pre_sol_step_0,
            final_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=ANNOTATION_SPACING).next_to(question_title_group, DOWN, buff=0.5).align_to(question_title_group, LEFT)
        
        # Add the annotations to given_equation
        add_9 = self.add_annotations(
            "+9", 
            self.find_element("-3", pre_sol_step_0_exp),
            self.find_element("-9", pre_sol_step_0_exp),
            color=RED
        )
        
        pre_solution = Group(pre_sol_step_0, add_9)
        
        

        
        


        mid_sol_step_0 = self.create_labeled_step(
            "Label the coefficients",
            MathTex("-x^2 - 3x + 9 = 0").scale(TEX_SCALE)
        )
        
        mid_sol_step_0_label, mid_sol_step_0_exp = mid_sol_step_0[0], mid_sol_step_0[1]
        
        # Find elements in q_equation to highlight
        a_in_q_equation = self.find_element("-", mid_sol_step_0_exp, color=A_COLOR)  # Implied coefficient of x²
        b_in_q_equation = self.find_element("-3", mid_sol_step_0_exp, color=B_COLOR)      
        c_in_q_equation = self.find_element("9", mid_sol_step_0_exp, color=C_COLOR)      

        # Create coefficient labels
        a = MathTex("a = -1", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = -3", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = 9", color=C_COLOR).scale(TEX_SCALE)

        # Extract coefficient values
        a_value = self.find_element("-1", a)
        b_value = self.find_element("-3", b)
        c_value = self.find_element("9", c)

        a_label = self.find_element("a =", a, as_group=True)
        b_label = self.find_element("b =", b, as_group=True)
        c_label = self.find_element("c =", c, as_group=True)

        # Arrange coefficients horizontally
        coefficients = VGroup(a, b, c).arrange(RIGHT, buff=0.6)

        mid_solution_steps = VGroup(
            mid_sol_step_0,
            coefficients
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        mid_solution_steps.next_to(question_title_group, DOWN, buff=0.4)
        mid_solution_steps.align_to(question_title_group, LEFT)


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
            MathTex(r"x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(-1)(9)}}{2(-1)}").scale(TEX_SCALE)
        )

        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]

        sol_step_2 = self.create_labeled_step(
            "Step 2: Simplify the expression",
            MathTex(r"x = \frac{3 \pm \sqrt{9 - 4(-1)(9)}}{-2}").scale(TEX_SCALE)
        )

        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]

        sol_step_3 = self.create_labeled_step(
            "Step 3: Continue simplifying",
            MathTex(r"x = \frac{3 \pm \sqrt{9 + 36}}{-2}").scale(TEX_SCALE)
        )

        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]

        sol_step_4 = self.create_labeled_step(
            "Step 4: Calculate the square root",
            MathTex(r"x = \frac{3 \pm \sqrt{45}}{-2}").scale(TEX_SCALE)
        )

        step_4_label, step_4_exp = sol_step_4[0], sol_step_4[1]

        sol_step_5 = self.create_labeled_step(
            "Step 5: Find the two roots",
            MathTex(r"x = \frac{3 \pm 6.7082}{-2}").scale(TEX_SCALE)
        )

        step_5_label, step_5_exp = sol_step_5[0], sol_step_5[1]

        
        first_root = MathTex(r"x = \frac{3 + 6.7082}{-2}").scale(TEX_SCALE)
        first_root_dec = MathTex(r"x \approx -4.85").scale(TEX_SCALE)
        first_root_group = VGroup(first_root, first_root_dec).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        second_root = MathTex(r"x = \frac{3 - 6.7082}{-2}").scale(TEX_SCALE)
        second_root_dec = MathTex(r"x \approx 1.85").scale(TEX_SCALE)
        second_root_group = VGroup(second_root, second_root_dec).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Arrange the groups vertically
        root_steps = VGroup(
            first_root_group,
            second_root_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        
        # Position the entire group
        root_steps.next_to(quadratic_group, DOWN, buff=0.6)

        first_root_rec = self.create_surrounding_rectangle(first_root_dec)
        second_root_rec = self.create_surrounding_rectangle(second_root_dec)
        

        # Find elements in step_1_exp to highlight and animate
        b_in_frac = self.find_element("-3", step_1_exp, nth=0, opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("-3", step_1_exp, nth=1, opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("-1", step_1_exp, nth=0, opacity=0, color=A_COLOR)
        c_in_4ac = self.find_element("9", step_1_exp, nth=0, opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("-1", step_1_exp, nth=1, opacity=0, color=A_COLOR)

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
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        solution_steps.next_to(mid_solution_steps, DOWN, buff=0.4)
        solution_steps.align_to(mid_solution_steps, LEFT)

        ordered_steps = VGroup(
            final_equation, mid_sol_step_0_label,
            a_label, b_label, c_label, a_value, b_value, c_value,
            step_0_label, step_0_exp,
            step_1_label, step_1_exp,
            *substitution,
            step_2_label, step_2_exp,
            step_3_label, step_3_exp,
            step_4_label, step_4_exp,
            step_5_label, step_5_exp
        )

        scroll_mgr = ScrollManager(ordered_steps)
        scroll_mgr.start_position = ordered_steps[1].copy()
        
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
        
        self.play(Write(question_title_group))
        self.play(Write(pre_sol_step_0_label))
        self.play(Write(pre_sol_step_0_exp))
        self.play(FadeIn(add_9))

        # final_equation
        scroll_mgr.prepare_next(self)

        self.play(FadeOut(pre_solution))

        # replace with mid_sol_step_0_exp
        scroll_mgr.replace_in_place(self, 0, mid_sol_step_0_exp, move_new_content=False)      

        # mid_sol_step_0_label
        scroll_mgr.prepare_next(self)
        
        # a =   b =   c =
        scroll_mgr.prepare_next(self, steps=3)

        # Animate the coefficient
        self.play(self.indicate(quad_form_a))
        scroll_mgr.fade_in_from_target(self, a_in_q_equation)  # Fades in a_value from quad_form_a

        self.play(self.indicate(quad_form_b))
        scroll_mgr.fade_in_from_target(self, b_in_q_equation)  # Fades in a_value from quad_form_b

        self.play(self.indicate(quad_form_c))
        scroll_mgr.fade_in_from_target(self, c_in_q_equation)  # Fades in a_value from quad_form_c

        # Show step_0 and step_1
        scroll_mgr.prepare_next(self)  # Shows step_0_label
        scroll_mgr.prepare_next(self)  # Shows step_0_exp

        # scroll mid_sol_step_0_label mid_sol_step_0_exp
        

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
        
         # scroll step_0_exp, step_0_label, labels, and coefficients
        scroll_mgr.scroll_down(self, steps=8)
                
        scroll_mgr.prepare_next(self)  # Shows step_3_label
        scroll_mgr.prepare_next(self)  # Shows step_3_exp
        
        # Scroll the substitution with step_1_exp and step_1_label
        scroll_mgr.scroll_down(self, steps=7)
        
        # Show steps 4 and 5
        scroll_mgr.prepare_next(self)  # Shows step_4_label
        scroll_mgr.prepare_next(self)  # Shows step_4_exp
        
        scroll_mgr.scroll_down(self, steps=2)
        
        scroll_mgr.prepare_next(self)  # Shows step_5_label
        scroll_mgr.prepare_next(self)  # Shows step_5_exp
        

        self.wait(2)
        
        
        self.play(ReplacementTransform(step_5_exp.copy(), first_root))
        self.play(ReplacementTransform(step_5_exp.copy(), second_root))
        
        self.wait(2)
        
        self.play(Write(first_root_dec))
        self.play(Write(second_root_dec))
        
        self.wait(2)
        
        self.play(Create(first_root_rec), Create(second_root_rec), run_time=2)
        
        