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
        # GIVEN EQUATION AND SETUP - NEW EQUATION
        ###############################################################################
        
        question_title_group = VGroup(
            Tex("Solve using the quadratic formula:").scale(0.6),
            MathTex("4(x+5)^2=48").scale(0.6)
        )
        
        question_title_group.arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)
        
        
        
        ###############################################################################
        # SECTION 2: SOLVING THE EQUATION
        ###############################################################################
        
        
        ########################################## STEP 1 Before #######################
        # step1_label = Tex("Get the equation in standard form", color="#DBDBDB").scale(TEXT_SCALE)
        # step1_expr = MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        # step1 = VGroup(step1_label, step1_expr).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)
        
        step1_list = [
            "Get the equation in standard form",
            MathTex("4(x+5)^2=48")
        ]

        ########################################## STEP 2 Before #######################
        # step2_label = Tex("Divide both sides by 4", color="#DBDBDB").scale(TEXT_SCALE)
        # step2_expr1 = self.create_annotated_expression(
        #     "4(x+5)^2=48", 
        #     annotations=[(r"\div 4", "4", "48", GREEN)]
        # )

        # step2_expr2 = MathTex("(x+5)^2=12").scale(TEX_SCALE)
        
        # # Group the expressions
        # step2_exprs = VGroup(step2_expr1, step2_expr2).arrange(DOWN, buff=ELEMENT_BUFF)
        # step2 = VGroup(step2_label, step2_exprs).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)

        step2_list = [
            "Divide both sides by 4",
            MathTex("4(x+5)^2=48"),
            Annotation(r"\div 4", "4", "48", color = GREEN),
            MathTex("(x+5)^2=12")
        ]

        ########################################## STEP 3 Before #######################
        # step3_label = Tex("Expand the squared term", color="#DBDBDB").scale(TEXT_SCALE)
        # step3_expr1 = MathTex("x^2 + 10x + 25 = 12").scale(TEX_SCALE)
        # step3 = VGroup(step3_label, step3_expr1).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)

        step3_list = [
            "Expand the squared term",
            MathTex("x^2 + 10x + 25 = 12")
        ]

        ########################################## STEP 4 Before #######################
        # step4_label = Tex("Subtract 12 from both sides", color="#DBDBDB").scale(TEXT_SCALE)
        # step4_expr1 = self.create_annotated_expression(
        #     "x^2 + 10x + 25 = 12",
        #     annotations=[("-12", "25", "12", RED)]
        # )
        # step4_expr2 = MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)
        # step4_exprs = VGroup(step4_expr1, step4_expr2).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        # step4 = VGroup(step4_label, step4_exprs).arrange(DOWN, aligned_edge=LEFT, buff=LABEL_BUFFER)
        
        step4_list = [
            "Subtract 12 from both sides",
            MathTex("x^2 + 10x + 25 = 12"),
            # annotation automatically follows the preceeding expression 
            Annotation(
               "-12",
                self.find_element_lazy("25"),
                self.find_element_lazy("12"),
                color=RED,
            ),
            MathTex("x^2 + 10x + 13 = 0")
        ]


        # solution = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
            
        solution = self.create_ordered_steps(step1_list, step2_list, step3_list, step4_list)
        solution.next_to(question_title_group, DOWN, buff=0.8).align_to(question_title_group, LEFT)

        step1, step2, step3, step4 = solution
        # solution.arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        print(len(step2))
        step2_annotation = step2[2]
        step4_annotation = step4[2]
        # step2_annotation = step2_expr1[2]  # The annotation part is the third element in the group
        # Step 4 annotations (subtraction of 12)
        # Extract the annotation terms from step4_expr1
        # step4_annotation = step4_expr1[2]  # The annotation part is the third element in the group
        self.add(step2[3])
        # self.add(step2_annotation)
        # self.add(step4_annotation)
        # Create individual step elements for ScrollManager including annotations
        pre_ordered_steps = VGroup(
            # step1_label, step1_expr,
            # step2_label, step2_expr1[0],  # Main expression from step2_expr1
            # step2_annotation,             # Annotation from step2_expr1
            # step2_expr2,
            # step3_label, step3_expr1,
            # step4_label, step4_expr1[0],  # Main expression from step4_expr1
            # step4_annotation,             # Annotation from step4_expr1
            # step4_expr2
            *step1,
            *step2,
            *step3,
            *step4,
        )
        
        pre_scroll_mgr = ScrollManager(pre_ordered_steps)
        
        
         ###############################################################################
        # IDENTIFY COEFFICIENTS
        ###############################################################################
        
        mid_sol_step_0 = self.create_labeled_step(
            "Label the coefficients",
            MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)
        )
        
        mid_sol_step_0_label, mid_sol_step_0_exp = mid_sol_step_0[0], mid_sol_step_0[1]
        
        # Find elements in equation to highlight
        a_in_q_equation = self.find_element("1", mid_sol_step_0_exp, color=A_COLOR)  # Coefficient of x²
        b_in_q_equation = self.find_element("10", mid_sol_step_0_exp, color=B_COLOR)      
        c_in_q_equation = self.find_element("13", mid_sol_step_0_exp, color=C_COLOR)      

        # Create coefficient labels
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        b = MathTex("b = 10", color=B_COLOR).scale(TEX_SCALE)
        c = MathTex("c = 13", color=C_COLOR).scale(TEX_SCALE)

        # Extract coefficient values
        a_value = self.find_element("1", a)
        b_value = self.find_element("10", b)
        c_value = self.find_element("13", c)

        a_label = self.find_element("a =", a, as_group=True)
        b_label = self.find_element("b =", b, as_group=True)
        c_label = self.find_element("c =", c, as_group=True)

        # Arrange coefficients horizontally
        coefficients = VGroup(a, b, c).arrange(RIGHT, buff=0.6)

        mid_solution_steps = VGroup(
            mid_sol_step_0,
            coefficients
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        mid_solution_steps.next_to(question_title_group, DOWN, buff=0.8).align_to(question_title_group, LEFT)

        ###############################################################################
        # SOLVING THE EQUATION WITH QUADRATIC FORMULA
        ###############################################################################       

        sol_step_0 = self.create_labeled_step(
            "Use the quadratic formula",
            MathTex(r"x \quad = \quad \frac{ \ -b \pm \sqrt{ \ b^2 \ - \ 4ac \ }}{2a}").scale(TEX_SCALE)
        )

        step_0_label, step_0_exp = sol_step_0[0], sol_step_0[1]

        sol_step_1 = self.create_labeled_step(
            "Step 1: Substitute the coefficients",
            MathTex(r"x = \frac{-(10) \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}").scale(TEX_SCALE)
        )

        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]

        sol_step_2 = self.create_labeled_step(
            "Step 2: Simplify the expression",
            MathTex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}").scale(TEX_SCALE)
        )

        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]

        sol_step_3 = self.create_labeled_step(
            "Step 3: Continue simplifying",
            MathTex(r"x = \frac{-10 \pm \sqrt{48}}{2}").scale(TEX_SCALE)
        )

        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]

        sol_step_4 = self.create_labeled_step(
            "Step 4: Simplify the square root",
            MathTex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}").scale(TEX_SCALE)
        )

        step_4_label, step_4_exp = sol_step_4[0], sol_step_4[1]

        sol_step_5 = self.create_labeled_step(
            "Step 5: Simplify the fraction",
            MathTex(r"x = -5 \pm 2\sqrt{3}").scale(TEX_SCALE)
        )

        step_5_label, step_5_exp = sol_step_5[0], sol_step_5[1]

        # Create final solution display
        first_root = MathTex(r"x = -5 + 2\sqrt{3}").scale(TEX_SCALE)
        first_root_dec = MathTex(r"x \approx -1.54").scale(TEX_SCALE)
        first_root_group = VGroup(first_root, first_root_dec).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        second_root = MathTex(r"x = -5 - 2\sqrt{3}").scale(TEX_SCALE)
        second_root_dec = MathTex(r"x \approx -8.46").scale(TEX_SCALE)
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
        b_in_frac = self.find_element("10", step_1_exp, nth=0, opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("10", step_1_exp, nth=1, opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("1", step_1_exp, nth=2, opacity=0, color=A_COLOR)
        c_in_4ac = self.find_element("13", step_1_exp, nth=0, opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("1", step_1_exp, nth=-1, opacity=0, color=A_COLOR)

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

        solution_steps.next_to(mid_solution_steps, DOWN, buff=0.6)
        solution_steps.align_to(mid_solution_steps, LEFT)

        # ordered_steps = VGroup(
        #     step4_expr2, mid_sol_step_0_label,
        #     a_label, b_label, c_label, a_value, b_value, c_value,
        #     step_0_label, step_0_exp,
        #     step_1_label, step_1_exp,
        #     *substitution,
        #     step_2_label, step_2_exp,
        #     step_3_label, step_3_exp,
        #     step_4_label, step_4_exp,
        #     step_5_label, step_5_exp
        # )

        # scroll_mgr = ScrollManager(ordered_steps)
        # scroll_mgr.start_position = ordered_steps[1].copy()
        
        ###############################################################################
        # ANIMATIONS
        ###############################################################################

        # Setup the reference formula and standard form
        self.play(
            FadeIn(
                quadratic_group,
                quadratic_form_bg,
                quadratic_formula_bg
            )
        )
        
        self.play(Write(question_title_group))
        
        pre_scroll_mgr.prepare_next(self)  # Shows step1_label
        pre_scroll_mgr.prepare_next(self)  # Shows step1_expr

        pre_scroll_mgr.prepare_next(self)  # Shows step2_label
        pre_scroll_mgr.prepare_next(self)  # Shows main expression (step2_expr1[0])
        
        self.play(FadeIn(step2_annotation))
        pre_scroll_mgr.current_position += 1  # Manually update position
        
        pre_scroll_mgr.prepare_next(self)  # Shows step2_expr2
        
        pre_scroll_mgr.scroll_down(self, steps=2)

        pre_scroll_mgr.prepare_next(self)  # Shows step3_label
        pre_scroll_mgr.prepare_next(self)  # Shows step3_expr1
        
        pre_scroll_mgr.scroll_down(self, steps=3)

        pre_scroll_mgr.prepare_next(self)  # Shows step4_label
        pre_scroll_mgr.prepare_next(self)  # Shows step4_expr1
        self.play(FadeIn(step4_annotation))
        pre_scroll_mgr.current_position += 1  # Manually update position
        pre_scroll_mgr.prepare_next(self)  # Shows step4_expr2
        
        self.play(FadeOut(solution))
        
        # scroll_mgr.prepare_next(self)

        
        # # Replace with labeled equation
        # scroll_mgr.replace_in_place(self, 0, mid_sol_step_0_exp, move_new_content=False)      
        
        

        # # Show label for coefficient step
        # scroll_mgr.prepare_next(self)
        
        # # Show a, b, c labels
        # scroll_mgr.prepare_next(self, steps=3)

        # # Animate each coefficient identification with highlighting
        # self.play(self.indicate(quad_form_a))
        # scroll_mgr.fade_in_from_target(self, a_in_q_equation)  # Fades in a_value from quad_form_a

        # self.play(self.indicate(quad_form_b))
        # scroll_mgr.fade_in_from_target(self, b_in_q_equation)  # Fades in b_value from quad_form_b

        # self.play(self.indicate(quad_form_c))
        # scroll_mgr.fade_in_from_target(self, c_in_q_equation)  # Fades in c_value from quad_form_c

        # # Show quadratic formula step
        # scroll_mgr.prepare_next(self)  # Shows step_0_label
        # scroll_mgr.prepare_next(self)  # Shows step_0_exp

        # # Show substitution step
        # scroll_mgr.prepare_next(self)  # Shows step_1_label
        # scroll_mgr.prepare_next(self)  # Shows step_1_exp

        # # Animate coefficient substitutions
        # scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_frac from b_value
        # scroll_mgr.fade_in_from_target(self, b_value)  # Fades in visible_b_sqrt from b_value
        # scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_4ac from a_value
        # scroll_mgr.fade_in_from_target(self, a_value)  # Fades in visible_a_denom from a_value
        # scroll_mgr.fade_in_from_target(self, c_value)  # Fades in visible_c_4ac from c_value
        
        # # Scroll to keep in view
        # scroll_mgr.scroll_down(self, steps=2)

        # # Show initial simplification
        # scroll_mgr.prepare_next(self)  # Shows step_2_label
        # scroll_mgr.prepare_next(self)  # Shows step_2_exp
        
        # # Scroll as needed
        # scroll_mgr.scroll_down(self, steps=8)
                
        # # Continue simplification
        # scroll_mgr.prepare_next(self)  # Shows step_3_label
        # scroll_mgr.prepare_next(self)  # Shows step_3_exp
        
        # # Scroll to keep in view
        # scroll_mgr.scroll_down(self, steps=7)
        
        # # Show square root simplification
        # scroll_mgr.prepare_next(self)  # Shows step_4_label
        # scroll_mgr.prepare_next(self)  # Shows step_4_exp
        
        # scroll_mgr.scroll_down(self, steps=2)
        
        # # Show final simplification
        # scroll_mgr.prepare_next(self)  # Shows step_5_label
        # scroll_mgr.prepare_next(self)  # Shows step_5_exp
        
        # self.wait(2)
        
        # # Show the first solution
        # self.play(ReplacementTransform(step_5_exp.copy(), first_root))
        # self.play(ReplacementTransform(step_5_exp.copy(), second_root))
        
        # self.wait(2)
        
        # # Show decimal approximations
        # self.play(Write(first_root_dec))
        # self.play(Write(second_root_dec))
        
        # self.wait(2)
        
        # # Highlight final answers
        # self.play(Create(first_root_rec), Create(second_root_rec), run_time=2)
        
        self.wait(2)