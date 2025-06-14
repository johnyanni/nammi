from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"


class RQuadraticFormula03(MathTutorialScene): 
    def construct(self):
        
        
        # =================================================================================
        # CONFIGURATION
        # =================================================================================

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        
        
        
        
        
        
        
        # =================================================================================
        # SECTION 1: QUESTION
        # =================================================================================
        
        question_text = MathTex(r"\text{Solve using the quadratic formula:} \; -x^2 - 3x = -9").scale(LABEL_SCALE).set_color(LIGHT_GRAY).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4)

        # ===========================================================

        self.play(
            Write(question_text, run_time=3),  
        )
        
        self.wait(1)    
    
    
    
    
    
    
    
    
    
        # =================================================================================
        # SECTION 2: FORMULAS
        # =================================================================================
        
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
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.2).to_corner(DR, buff=0.3).set_color(LIGHT_GRAY)
        
    
        quadratic_form_coefficients = self.parse_elements(quadratic_form.formula,
            ('a', 'a', 0, A_COLOR),
            ('b', 'b', 0, B_COLOR),
            ('c', 'c', 0, C_COLOR)
        )
        
        self.apply_smart_colorize([quadratic_formula.formula],
            {
                "a": A_COLOR,
                "b": B_COLOR,
                "c": C_COLOR
            }
        )
        
        # ===========================================================
        
        self.play(
            self.FadeInThenWrite(
                [quadratic_form.background],
                [quadratic_form.label, quadratic_form.formula],
            )
        )
        
        self.wait(1)
        
        self.play(
            self.FadeInThenWrite(
                [quadratic_formula.background], 
                [quadratic_formula.label, quadratic_formula.formula],
            )
        )
        
        self.wait(1)
                           
                           
                           
                           
                           
                           
                   

        
        # =================================================================================
        # SOLUTION STEPS [SCROLL]
        # =================================================================================
        
        # SCROLL SETUP
        # =================================================================================
        
        scroll = ScrollManager(scene=self, global_arrangement=False)
        scroll.set_position_target(question_text, DOWN, buff=0.3, aligned_edge=LEFT) 
        
        
        
        
        
        
        # ===========================================================
        # STEP 1: ADD 9 TO BOTH SIDES
        # ===========================================================
        
        s1_add_step = scroll.construct_step(
            scroll.create_tex(r"First, get the equation in \textbf{standard form}:", label="l_convert_to_standard_form"),
            scroll.create_tex(r"Add 9 to both sides", label="l_add_9_to_both_sides"),
            scroll.create_annotated_equation(
                r"-x^2 - 3x = -9",
                r"+9",
                "-3x",
                "-9",
                label="ae_add_9_to_both_sides"
            ),
            scroll.create_math_tex(r"-x^2 - 3x + 9 = 0", label="m_add_9_result")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_convert_to_standard_form")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        scroll.prepare_next("l_add_9_to_both_sides")
        scroll.prepare_next("ae_add_9_to_both_sides")
        scroll.prepare_next("m_add_9_result")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_add_9_result")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 2: IDENTIFY COEFFICIENTS
        # ===========================================================

        s2_identify_coefficients_step = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:"),
            scroll.create_math_tex(r"-x^2 - 3x + 9 = 0"),
            scroll.create_math_tex(r"a = -1 \quad b = -3 \quad c = 9", scale=1.0),
            add_to_scroll=False,
            buff=0.3
        )
        
        coefficient_values_in_equation = self.parse_elements(s2_identify_coefficients_step[1],
            ('a_value', '-', 0, A_COLOR),  # Just the minus sign for -x^2
            ('b_value', '-3', 0, B_COLOR),
            ('c_value', '9', 0, C_COLOR)
        )
        
        coefficient_labels = self.parse_elements(s2_identify_coefficients_step[2],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
                
        coefficient_values = self.parse_elements(s2_identify_coefficients_step[2],
            ('a_value', '-1', 0, A_COLOR),
            ('b_value', '-3', 0, B_COLOR),
            ('c_value', '9', 0, C_COLOR)
        )
        
        scroll.create_steps(s2_identify_coefficients_step[:-1], ["l_identify_coefficients", "m_standard_form_equation"], arrange=False)
        scroll.create_steps(coefficient_labels.values(), ["coefficient_a_label", "coefficient_b_label", "coefficient_c_label"], arrange=False)
        scroll.create_steps(coefficient_values.values(), ["coefficient_a_value", "coefficient_b_value", "coefficient_c_value"], arrange=False)
        
        # ===========================================================
        
        scroll.prepare_next("l_identify_coefficients")
        scroll.prepare_next("m_standard_form_equation")
        
        scroll.prepare_next("coefficient_a_label")
        scroll.prepare_next("coefficient_b_label")
        scroll.prepare_next("coefficient_c_label")
        
        self.play(self.indicate(quadratic_form_coefficients['a'], color=None))
        scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['b'], color=None))
        scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['c'], color=None))
        scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_standard_form_equation")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>











        # ===========================================================
        # STEP 3: USE THE QUADRATIC FORMULA
        # ===========================================================
        
        s3_quadratic_formula_step = scroll.construct_step(
            scroll.create_tex(r"Use the \textbf{quadratic formula} to solve for $x$:", label="l_quadratic_formula"),
            scroll.create_math_tex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}", label="m_quadratic_formula")
        )
        
        coefficient_values_in_formula = self.parse_elements(s3_quadratic_formula_step[1],
            ('b', 'b', B_COLOR),
            ('a1', 'a', 0, A_COLOR),
            ('c', 'c', C_COLOR),
            ('a2', 'a', 1, A_COLOR)
        )
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_quadratic_formula")
        self.play(self.indicate(quadratic_formula.group, scale_factor=1.2))
        scroll.prepare_next("m_quadratic_formula")
        
        self.wait(1)
        
        
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 4: SUBSTITUTE VALUES
        # ===========================================================
        
        s4_substitute_values_step = scroll.construct_step(
            scroll.create_tex(r"Substitute the coefficients into the formula:"),
            scroll.create_math_tex(r"x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(-1)(9)}}{2(-1)}"),
            add_to_scroll=False
        )
        
        substituted_values = self.parse_elements(s4_substitute_values_step[1],
            ('b_in_frac', '-3', 0, B_COLOR, 0),
            ('b_in_sqrt', '-3', 1, B_COLOR, 0),
            ('a_in_4ac', '-1', 0, A_COLOR, 0),
            ('c_in_4ac', '9', 0, C_COLOR, 0),
            ('a_in_denom', '-1', -1, A_COLOR, 0)
        )
        
        visible_copies = VGroup()

        for name, element in substituted_values.items():
            visible_copy = element.copy().set_opacity(1)
            setattr(visible_copies, name, visible_copy)
            visible_copies.add(visible_copy)
        
        s4_substitute_values_step[1].add(visible_copies)
        
        scroll.create_steps(s4_substitute_values_step, ["l_substitute_values", "m_empty_formula"], arrange=False)
        scroll.create_steps(visible_copies, arrange=False)
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_substitute_values")
        scroll.prepare_next("m_empty_formula")
        
        self.play(
            self.indicate(coefficient_values['b_value'], color=None),
            self.indicate(coefficient_values_in_formula['b'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac)
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt)
        
        
        self.play(
            self.indicate(coefficient_values['a_value'], color=None),
            self.indicate(coefficient_values_in_formula['a1'], color=None),
        )
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac)
    
            
        self.play(
            self.indicate(coefficient_values['c_value'], color=None),
            self.indicate(coefficient_values_in_formula['c'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac)
        
        
        self.play(
            self.indicate(coefficient_values['a_value'], color=None),
            self.indicate(coefficient_values_in_formula['a2'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom)
         
         
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_quadratic_formula")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 5: SIMPLIFY THE EXPRESSION
        # ===========================================================
        
        s5_simplify_step = scroll.construct_step(
            scroll.create_tex(r"Simplify the expression:", label="l_simplify_expression"),
            scroll.create_math_tex(r"x = \frac{3 \pm \sqrt{9 - 4 \cdot (-1) \cdot 9}}{-2}", label="m_simplify_expression")
        )
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_simplify_expression")
        scroll.prepare_next("m_simplify_expression")
        
        self.wait(1)

        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 6: CONTINUE SIMPLIFYING
        # ===========================================================
        
        s6_simplify2_step = scroll.construct_step(
            scroll.create_tex(r"Continue simplifying:", label="l_simplify_expression_2"),
            scroll.create_math_tex(r"x = \frac{3 \pm \sqrt{9 + 36}}{-2}", label="m_simplify_expression_2")
        )
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_simplify_expression_2")
        scroll.transform_from_copy("m_simplify_expression", "m_simplify_expression_2", run_time=2)
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_simplify_expression")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 7: SIMPLIFY FURTHER
        # ===========================================================
        
        s7_simplify3_step = scroll.construct_step(
            scroll.create_tex(r"Simplify the square root:", label="l_simplify_expression_3"),
            scroll.create_math_tex(r"x = \frac{3 \pm \sqrt{45}}{-2}", label="m_simplify_expression_3")
        )
        
        s7_sqrt_45 = self.parse_elements(s7_simplify3_step[1],
            ('sqrt_45', r'\sqrt{45}')
        )
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_simplify_expression_3")
        scroll.transform_from_copy("m_simplify_expression_2", "m_simplify_expression_3", run_time=2)
        
        self.wait(1)
        
        
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 8: SIMPLIFY THE SQUARE ROOT
        # ===========================================================
        
        s8_simplify_sqrt_step = scroll.construct_step(
            scroll.create_tex(r"Factor the square root:"),
            scroll.create_math_tex(r"\sqrt{45} = \sqrt{9 \times 5} = 3\sqrt{5}", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex(r"x = \frac{3 \pm 3\sqrt{5}}{-2}"),
            add_to_scroll=False
        )
        
        sqrt_45_parts = self.parse_elements(s8_simplify_sqrt_step[1],
            ('sqrt_45', r'\sqrt{45}'),
            ('sqrt_45_factor', r'= \sqrt{9 \times 5} ='),
            ('sqrt_45_result', r'3\sqrt{5}', 0, YELLOW),
        )
        
        SmartColorizeStatic(s8_simplify_sqrt_step[2], {r"3\sqrt{5}": YELLOW})
        
        scroll.create_step(s8_simplify_sqrt_step[0], "l_simplify_sqrt", arrange=False)
        scroll.create_steps(sqrt_45_parts.values(), ["sqrt_45", "sqrt_45_factor", "sqrt_45_result"], arrange=False)
        scroll.create_step(s8_simplify_sqrt_step[2], "m_simplify_sqrt_result_expression", arrange=False)
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        scroll.prepare_next("l_simplify_sqrt")
        self.play(self.indicate(s7_sqrt_45['sqrt_45']))
        scroll.transform_from_copy(s7_sqrt_45['sqrt_45'], sqrt_45_parts['sqrt_45'])
        scroll.prepare_next("sqrt_45_factor")
        scroll.prepare_next("sqrt_45_result")
        scroll.prepare_next("m_simplify_sqrt_result_expression")
        
        self.wait(1)
        
        
        
        
        
        # ===========================================================
        # FINAL ANSWERS
        # ===========================================================
        
        answer1_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{3 + 3\sqrt{5}}{-2}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = -4.854").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        answer2_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{3 - 3\sqrt{5}}{-2}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = 1.854").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        answer_group = VGroup(
            answer1_group,
            answer2_group
        ).arrange(RIGHT, aligned_edge=UP, buff=1.4)
        
        answer_group.to_edge(UP, buff=1.2).to_edge(RIGHT, buff=0.8)
        
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        self.play(
            Write(answer1_group[0]),
            Write(answer2_group[0])
        )
        
        self.play(
            TransformFromCopy(s8_simplify_sqrt_step[2], answer1_group[1]),
            TransformFromCopy(s8_simplify_sqrt_step[2], answer2_group[1])
        )

        self.play(Write(answer1_group[2]))
        self.play(Write(answer2_group[2]))
        
        self.wait(2)