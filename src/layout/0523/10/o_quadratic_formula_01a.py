from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class OQuadraticFormula01(MathTutorialScene): 
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"

        # ============================================
        # SECTION 1: QUESTION
        # ============================================
        
        question_text = Tex("Solve using the quadratic formula:").scale(LABEL_SCALE)
        question_equation = MathTex(r"4(x+5)^2 = 48").scale(S_MATH_SCALE)
        question_group = VGroup(
            question_text, 
            question_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)

        self.play(
            Write(question_group, run_time=3),  # Write question and equation
        )
        
        self.wait(1)
        
        # ============================================
        # SECTION 2: HINTS
        # ============================================
        
        quadratic_form = self.create_labeled_formula(
            "Standard Form",
            r"ax^2 + bx + c = 0"
        )
        
        quadratic_formula = self.create_labeled_formula(
            "Quadratic Formula",
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        )
        
        quadratic_group = VGroup(
            quadratic_form.group,
            quadratic_formula.group
        ).arrange(RIGHT, aligned_edge=UP, buff=0.2).to_corner(UR, buff=0.2).set_color(LIGHT_GRAY)
        
        quadratic_form_coefficients = self.parse_elements(quadratic_form.formula,
            ('a', 'a', 0, A_COLOR),
            ('b', 'b', 0, B_COLOR),
            ('c', 'c', 0, C_COLOR)
        )

        self.play(
            self.FadeInThenWrite(
                [quadratic_form.background, quadratic_formula.background],
                [quadratic_form.label, quadratic_formula.label, quadratic_form.formula, quadratic_formula.formula],
            )
        )
        
        # =============================================
        # SECTION 3: SOLUTION STEPS
        # =============================================

        scroll = ScrollManager(scene=self, global_arrangement=False)
        scroll.set_position_target(question_group, DOWN, buff=0.3, aligned_edge=LEFT) 
        
        # ======== Step 1: Convert to standard form (divide by 4) ========
        divide_step = scroll.construct_step(
            scroll.create_tex("First, get the equation in standard form:", label="l_convert_to_standard_form"),
            scroll.create_tex("Divide both sides by 4", label="l_divide_both_sides_by_4"),
            scroll.create_annotated_equation(
                r"4(x+5)^2 = 48",
                r"\div 4",
                "4",
                "48",
                label="ae_divide_both_sides_by_4"
            ),
            scroll.create_math_tex(r"(x+5)^2 = 12", label="m_divide_by_4_result"),
        )
        
        scroll.prepare_next("l_convert_to_standard_form", run_time=5)
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        scroll.prepare_next("l_divide_both_sides_by_4")
        scroll.prepare_next("ae_divide_both_sides_by_4")
        scroll.prepare_next("m_divide_by_4_result")
        
        self.wait(1)
        
        # ======== Step 2: Expand the squared term (FOIL) ========
        expand_step = scroll.construct_step(
            scroll.create_tex("Expand the squared term:", label="l_expand_squared_term"),
            scroll.create_math_tex(r"(x+5)^2 = (x+5)(x+5)", label="m_expand_squared_term", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex("x^2 + 10x + 25 = 12", label="m_expand_squared_term_result")
        )
        
        scroll.prepare_next("l_expand_squared_term")
        scroll.prepare_next("m_expand_squared_term")
        scroll.prepare_next("m_expand_squared_term_result")
        
        
        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("m_divide_by_4_result")
        self.wait(1)
        
        # ======== Step 3: Get in standard form (subtract 12) ========
        subtract_step = scroll.construct_step(
            scroll.create_tex("Subtract 12 from both sides:", label="l_subtract_12_from_both_sides"),
            scroll.create_annotated_equation(
                r"x^2 + 10x + 25 = 12",
                "-12",
                "25",
                "12",
                label="ae_subtract_12_from_both_sides"
            ),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0", label="m_subtract_12_from_both_sides_result")
        )
        
        scroll.prepare_next("l_subtract_12_from_both_sides")
        scroll.prepare_next("ae_subtract_12_from_both_sides")
        scroll.prepare_next("m_subtract_12_from_both_sides_result")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        
        self.wait(1)
        
        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("m_subtract_12_from_both_sides_result")
        
        # ======== Step 4: Standard form: Identify coefficients ========
        identify_coefficients_step = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:"),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0"),
            scroll.create_math_tex(r"a = 1 \quad b = 10 \quad c = 13", scale=1.0),
            add_to_scroll=False,
        )
        
        coefficient_values_in_equation = self.parse_elements(
            identify_coefficients_step[1],
            ('a_value', 'x', 0, A_COLOR),  
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )

        coefficient_labels = self.parse_elements(
            identify_coefficients_step[2],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
                
        coefficient_values = self.parse_elements(
            identify_coefficients_step[2],
            ('a_value', '1', 0, A_COLOR),
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )
        
        scroll.create_steps(identify_coefficients_step[:-1], ["l_identify_coefficients", "m_standard_form_equation"], arrange=False)
        scroll.create_steps(coefficient_labels.values(), ["coefficient_a_label", "coefficient_b_label", "coefficient_c_label"], arrange=False)
        scroll.create_steps(coefficient_values.values(), arrange=False)
        
        # Animations
        scroll.prepare_next("l_identify_coefficients")
        scroll.prepare_next("m_standard_form_equation")
        
        scroll.prepare_next(steps=3, run_time=3)
        
        self.play(self.indicate(quadratic_form_coefficients['a']))
        scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['b']))
        scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['c']))
        scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])

        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("l_identify_coefficients")

        # ======== Step 5: Use the quadratic formula ========
        using_quadratic_formula_step = scroll.construct_step(
            scroll.create_tex("Use the quadratic formula to solve for $x$:", label="l_using_quadratic_formula"),
            scroll.create_math_tex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", label="standard_quadratic_formula")
        )
        
        self.apply_smart_colorize(
            [quadratic_formula.formula, using_quadratic_formula_step[1]],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
                
        # Animations
        scroll.prepare_next("l_using_quadratic_formula")
        scroll.prepare_next("standard_quadratic_formula")

        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("m_standard_form_equation")

        # ======== Step 6: Substitute into the quadratic formula ========
        substitution_step = scroll.construct_step(
            scroll.create_tex("Substitute the coefficients into the formula:", label="l_substitution"),
            scroll.create_math_tex(r"x = \frac{-(10) \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}", label="empty_formula"),
        )

        coefficient_values_in_formula = self.parse_elements(
            substitution_step[1],
            ('b_in_frac', '10', 0, B_COLOR, 0),
            ('b_in_sqrt', '10', 1, B_COLOR, 0),
            ('a_in_4ac', '1', 2, A_COLOR, 0),
            ('c_in_4ac', '13', 0, C_COLOR, 0),
            ('a_in_denom', '1', -1, A_COLOR, 0)
        )
    
        # Animations
        scroll.prepare_next("l_substitution")
        scroll.prepare_next("empty_formula")
        
        self.play(self.indicate(coefficient_values['b_value'], color=None))
        scroll.fade_in_from_target(coefficient_values["b_value"], coefficient_values_in_formula["b_in_frac"].set_opacity(1))
        scroll.fade_in_from_target(coefficient_values["b_value"], coefficient_values_in_formula["b_in_sqrt"].set_opacity(1))
        
        
        self.play(self.indicate(coefficient_values['a_value'], color=None))
        scroll.fade_in_from_target(coefficient_values["a_value"], coefficient_values_in_formula["a_in_4ac"].set_opacity(1))
        
        self.play(self.indicate(coefficient_values['c_value'], color=None))
        scroll.fade_in_from_target(coefficient_values["c_value"], coefficient_values_in_formula["c_in_4ac"].set_opacity(1))
        
        self.play(self.indicate(coefficient_values['a_value'], color=None))
        scroll.fade_in_from_target(coefficient_values["a_value"], coefficient_values_in_formula["a_in_denom"].set_opacity(1))

        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("standard_quadratic_formula")

        # ======== Step 7: First simplification ========
        first_simplification_step = scroll.construct_step(
            scroll.create_tex("Simplify the expression:", label="l_first_simplification"),
            scroll.create_math_tex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}", label="m_first_simplification")
        )

        # Animations
        scroll.prepare_next("l_first_simplification")
        scroll.transform_from_copy(substitution_step[1], first_simplification_step[1])

        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("empty_formula")

        # ======== Step 8: Second simplification ========
        second_simplification_step = scroll.construct_step(
            scroll.create_tex("Continue simplifying:", label="l_second_simplification"),
            scroll.create_math_tex(r"x = \frac{-10 \pm \sqrt{48}}{2}", label="m_second_simplification")
        )
        
        second_simplification_sqrt = second_simplification_step[1][0][search_shape_in_text(second_simplification_step[1], MathTex(r"\sqrt{48}"))[0]]
    
        # Animations
        scroll.prepare_next("l_second_simplification")
        scroll.transform_from_copy(first_simplification_step[1], second_simplification_step[1])
        
        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("m_first_simplification")

        # ======== Step 9: Simplify the square root ========
        simplify_sqrt_step = scroll.construct_step(
            scroll.create_tex("Simplify the square root:"),
            scroll.create_math_tex(r"\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}"),
            add_to_scroll=False
        )
        
        simplify_sqrt_solving = self.parse_elements(
            simplify_sqrt_step[1],
            ('sqrt_48', r'\sqrt{48}'),
            ('sqrt_48_solve', r'= \sqrt{16 \times 3} ='),
            ('sqrt_48_solved', r'4\sqrt{3}', 0, YELLOW),
        )
        
        SmartColorizeStatic(simplify_sqrt_step[2], {r"4\sqrt{3}": YELLOW})
                
        scroll.create_step(simplify_sqrt_step[0], label="l_simplify_sqrt", arrange=False)
        scroll.create_steps(simplify_sqrt_solving.values(), ["sqrt_48", "sqrt_48_solve", "sqrt_48_solved"], arrange=False)
        scroll.create_step(simplify_sqrt_step[2], label="m_simplified_sqrt_eqn", arrange=False)

        # Animations
        scroll.prepare_next("l_simplify_sqrt")
        self.play(self.indicate(second_simplification_sqrt))

        scroll.transform_from_copy(second_simplification_sqrt, simplify_sqrt_solving["sqrt_48"])
        scroll.prepare_next("sqrt_48_solve")
        scroll.prepare_next("sqrt_48_solved")
        scroll.prepare_next("m_simplified_sqrt_eqn")

        # >>>>>>>>>> SCROLL DOWN <<<<<<<<<<
        scroll.scroll_down("sqrt_48")
        
        
        
        # ======== Step 10: Third simplification: divide by 2 ========
        divide_by_2_step = scroll.construct_step(
            scroll.create_tex(r"\raggedright We can further simplify \\ by dividing throughout by 2"),
            scroll.create_math_tex(r"x = \frac{-10 \pm 4\sqrt{3}}{2} = \frac{-10}{2} \pm \frac{4\sqrt{3}}{2}"),
            scroll.create_math_tex(r"x = -5 \pm 2\sqrt{3}"),
            add_to_scroll=False
        )
        
        divide_by_2_solving = self.parse_elements(
            divide_by_2_step[1],
            ('first_frac', r'\frac{-10}{2}', 0, LIGHT_GRAY),  
            ('second_frac', r'\frac{4\sqrt{3}}{2}', 0, LIGHT_GRAY), 
        )
        
        divide_by_2_solved = self.parse_elements(
            divide_by_2_step[2],
            ('x=', 'x ='),
            ('first_frac_solved', '-5'), 
            ('plus_minus', r'\pm'),
            ('second_frac_solved', r'2\sqrt{3}'),  
        )
        
        scroll.create_steps(divide_by_2_step[:-1], ["l_divide_by_2", "m_divide_by_2", "m_divide_by_2_solved"], arrange=False)
        scroll.create_steps(divide_by_2_solved.values(), ["x=", None, "plus_minus", None], arrange=False)

        # Animations
        scroll.prepare_next("l_divide_by_2")
        scroll.prepare_next("x=")

        scroll.transform_from_copy(divide_by_2_solving["first_frac"], divide_by_2_solved["first_frac_solved"])
        scroll.prepare_next("plus_minus")
        scroll.transform_from_copy(divide_by_2_solving["second_frac"], divide_by_2_solved["second_frac_solved"])

        # ======== Step 11: Finals answers ========
        answer1_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = -5 - 2\sqrt{3}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = -8.464").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        answer2_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = -5 + 2\sqrt{3}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = -1.536").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        answer_group = VGroup(
            answer1_group,
            answer2_group
        ).arrange(RIGHT, aligned_edge=UP, buff=1.4)
        
        answer_group.next_to(quadratic_group, DOWN, buff=1)
        
        # Animations
        self.play(
            Write(answer1_group[0]),
            Write(answer2_group[0])
        )
        
        # Transform to final answers
        self.play(
            TransformFromCopy(divide_by_2_step[2], answer1_group[1]),
            TransformFromCopy(divide_by_2_step[2], answer2_group[1])
        )
        
        # Show decimal approximations
        self.play(Write(answer1_group[2]))
        self.play(Write(answer2_group[2]))
        
        self.wait(2)
