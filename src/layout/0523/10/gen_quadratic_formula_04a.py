from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"


class RQuadraticFormula04(MathTutorialScene): 
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
        
        question_text = MathTex(r"\text{Solve using the quadratic formula:} \; 2(x-1)^2 + 3x = x^2 + 4x + 5").scale(LABEL_SCALE).set_color(LIGHT_GRAY).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4)

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
        scroll.set_position_target(question_text, DOWN, buff=0.5, aligned_edge=LEFT) 
        
        
        
        
        
        
        # ===========================================================
        # STEP 1: EXPAND THE SQUARED TERM
        # ===========================================================
        
        s1_expand_step = scroll.construct_step(
            scroll.create_tex(r"First, expand $(x-1)^2$:", label="l_expand_squared"),
            scroll.create_math_tex(r"(x-1)^2 = (x-1)(x-1) = x^2 - 2x + 1", color=LIGHT_GRAY, scale=M_MATH_SCALE, label="m_expand_detail"),
            scroll.create_math_tex(r"2(x^2 - 2x + 1) + 3x = x^2 + 4x + 5", label="m_expand_result")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_expand_squared")
        scroll.prepare_next("m_expand_detail")
        scroll.prepare_next("m_expand_result")
        
        self.wait(1)
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 2: DISTRIBUTE THE 2
        # ===========================================================
        
        s2_distribute_step = scroll.construct_step(
            scroll.create_tex("Distribute the 2:", label="l_distribute_2"),
            scroll.create_math_tex(r"2x^2 - 4x + 2 + 3x = x^2 + 4x + 5", label="m_distribute_result")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_distribute_2")
        scroll.prepare_next("m_distribute_result")
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_expand_detail")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 3: COMBINE LIKE TERMS ON LEFT SIDE
        # ===========================================================
    
        s3_combine_left_step = scroll.construct_step(
            scroll.create_tex("Combine like terms on the left side:", label="l_combine_left"),
            scroll.create_math_tex(r"2x^2 - x + 2 = x^2 + 4x + 5", label="m_combine_left_result")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_combine_left")
        scroll.prepare_next("m_combine_left_result")
        
        self.wait(1)
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 4: MOVE ALL TERMS TO LEFT SIDE
        # ===========================================================
    
        s4_move_terms_step = scroll.construct_step(
            scroll.create_tex("Move all terms to the left side:", label="l_move_terms"),
            scroll.create_annotated_equation(
                r"2x^2 - x + 2 = x^2 + 4x + 5",
                r"-x^2 - 4x - 5",
                "2",
                "5",
                label="ae_move_terms"
            ),
            scroll.create_math_tex(r"2x^2 - x + 2 - x^2 - 4x - 5 = 0", label="m_move_terms_result")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_move_terms")
        scroll.prepare_next("ae_move_terms")
        scroll.prepare_next("m_move_terms_result")
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_combine_left_result")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===========================================================
        # STEP 5: COMBINE ALL LIKE TERMS
        # ===========================================================
    
        s5_final_combine_step = scroll.construct_step(
            scroll.create_tex("Combine all like terms:", label="l_final_combine"),
            scroll.create_math_tex(r"x^2 - 5x - 3 = 0", label="m_standard_form")
        )
        
        # ===========================================================
        
        scroll.prepare_next("l_final_combine")
        scroll.prepare_next("m_standard_form")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_standard_form")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>








        # # ===========================================================
        # # STEP 6: IDENTIFY COEFFICIENTS
        # # ===========================================================

        # s6_identify_coefficients_step = scroll.construct_step(
        #     scroll.create_tex("Now, identify the coefficients:"),
        #     scroll.create_math_tex(r"x^2 - 5x - 3 = 0"),
        #     scroll.create_math_tex(r"a = 1 \quad b = -5 \quad c = -3", scale=1.0),
        #     add_to_scroll=False,
        #     buff=0.3
        # )
        
        # coefficient_values_in_equation = self.parse_elements(s6_identify_coefficients_step[1],
        #     ('a_value', 'x', 0, A_COLOR),  
        #     ('b_value', '-5', 0, B_COLOR),
        #     ('c_value', '-3', 0, C_COLOR)
        # )
        
        # coefficient_labels = self.parse_elements(s6_identify_coefficients_step[2],
        #     ('a_label', 'a =', 0, A_COLOR),
        #     ('b_label', 'b =', 0, B_COLOR),
        #     ('c_label', 'c =', 0, C_COLOR)
        # )
                
        # coefficient_values = self.parse_elements(s6_identify_coefficients_step[2],
        #     ('a_value', '1', 0, A_COLOR),
        #     ('b_value', '-5', 0, B_COLOR),
        #     ('c_value', '-3', 0, C_COLOR)
        # )
        
        # scroll.create_steps(s6_identify_coefficients_step[:-1], ["l_identify_coefficients", "m_standard_form_equation"], arrange=False)
        # scroll.create_steps(coefficient_labels.values(), ["coefficient_a_label", "coefficient_b_label", "coefficient_c_label"], arrange=False)
        # scroll.create_steps(coefficient_values.values(), ["coefficient_a_value", "coefficient_b_value", "coefficient_c_value"], arrange=False)
        
        # # ===========================================================
        
        # scroll.prepare_next("l_identify_coefficients")
        # scroll.prepare_next("m_standard_form_equation")
        
        # scroll.prepare_next("coefficient_a_label")
        # scroll.prepare_next("coefficient_b_label")
        # scroll.prepare_next("coefficient_c_label")
        
        # self.play(self.indicate(quadratic_form_coefficients['a'], color=None))
        # scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])
        
        # self.play(self.indicate(quadratic_form_coefficients['b'], color=None))
        # scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])
        
        # self.play(self.indicate(quadratic_form_coefficients['c'], color=None))
        # scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])
        
        # self.wait(1)
        # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # scroll.scroll_down("m_standard_form_equation")
        # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>











        # # ===========================================================
        # # STEP 7: USE THE QUADRATIC FORMULA
        # # ===========================================================
        
        # s7_quadratic_formula_step = scroll.construct_step(
        #     scroll.create_tex(r"Use the \textbf{quadratic formula} to solve for $x$:", label="l_quadratic_formula"),
        #     scroll.create_math_tex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}", label="m_quadratic_formula")
        # )
        
        # coefficient_values_in_formula = self.parse_elements(s7_quadratic_formula_step[1],
        #     ('b', 'b', B_COLOR),
        #     ('a1', 'a', 0, A_COLOR),
        #     ('c', 'c', C_COLOR),
        #     ('a2', 'a', 1, A_COLOR)
        # )
        
        # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # scroll.prepare_next("l_quadratic_formula")
        # self.play(self.indicate(quadratic_formula.group, scale_factor=1.2))
        # scroll.prepare_next("m_quadratic_formula")
        
        # self.wait(1)
        
        
        
        
        
        
        
        
        
        
        # # ===========================================================
        # # STEP 8: SUBSTITUTE VALUES
        # # ===========================================================
        
        # s8_substitute_values_step = scroll.construct_step(
        #     scroll.create_tex(r"Substitute the coefficients into the formula:"),
        #     scroll.create_math_tex(r"x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(-3)}}{2(1)}"),
        #     add_to_scroll=False
        # )
        
        # substituted_values = self.parse_elements(s8_substitute_values_step[1],
        #     ('b_in_frac', '-5', 0, B_COLOR, 0),
        #     ('b_in_sqrt', '-5', 1, B_COLOR, 0),
        #     ('a_in_4ac', '1', 0, A_COLOR, 0),
        #     ('c_in_4ac', '-3', 0, C_COLOR, 0),
        #     ('a_in_denom', '1', -1, A_COLOR, 0)
        # )
        
        # visible_copies = VGroup()

        # for name, element in substituted_values.items():
        #     visible_copy = element.copy().set_opacity(1)
        #     setattr(visible_copies, name, visible_copy)
        #     visible_copies.add(visible_copy)
        
        # s8_substitute_values_step[1].add(visible_copies)
        
        # scroll.create_steps(s8_substitute_values_step, ["l_substitute_values", "m_empty_formula"], arrange=False)
        # scroll.create_steps(visible_copies, arrange=False)
        
        # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # scroll.prepare_next("l_substitute_values")
        # scroll.prepare_next("m_empty_formula")
        
        # self.play(
        #     self.indicate(coefficient_values['b_value'], color=None),
        #     self.indicate(coefficient_values_in_formula['b'], color=None)
        # )
        # scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac)
        # scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt)
        
        
        # self.play(
        #     self.indicate(coefficient_values['a_value'], color=None),
        #     self.indicate(coefficient_values_in_formula['a1'], color=None),
        # )
        # scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac)
    
            
        # self.play(
        #     self.indicate(coefficient_values['c_value'], color=None),
        #     self.indicate(coefficient_values_in_formula['c'], color=None)
        # )
        # scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac)
        
        
        # self.play(
        #     self.indicate(coefficient_values['a_value'], color=None),
        #     self.indicate(coefficient_values_in_formula['a2'], color=None)
        # )
        # scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom)
         
         
        # self.wait(1)
        # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # scroll.scroll_down("m_quadratic_formula")
        # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # # ===========================================================
        # # STEP 9: SIMPLIFY THE EXPRESSION
        # # ===========================================================
        
        # s9_simplify_step = scroll.construct_step(
        #     scroll.create_tex(r"Simplify the expression:", label="l_simplify_expression"),
        #     scroll.create_math_tex(r"x = \frac{5 \pm \sqrt{25 + 12}}{2}", label="m_simplify_expression")
        # )
        
        # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # scroll.prepare_next("l_simplify_expression")
        # scroll.prepare_next("m_simplify_expression")
        
        # self.wait(1)

        
        
        
        
        
        
        
        
        # # ===========================================================
        # # STEP 10: CONTINUE SIMPLIFYING
        # # ===========================================================
        
        # s10_simplify2_step = scroll.construct_step(
        #     scroll.create_tex(r"Continue simplifying:", label="l_simplify_expression_2"),
        #     scroll.create_math_tex(r"x = \frac{5 \pm \sqrt{37}}{2}", label="m_simplify_expression_2")
        # )
        
        # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # scroll.prepare_next("l_simplify_expression_2")
        # scroll.transform_from_copy("m_simplify_expression", "m_simplify_expression_2", run_time=2)
        
        # self.wait(1)
        
        
        
        
        
        # # ===========================================================
        # # FINAL ANSWERS
        # # ===========================================================
        
        # answer1_group = VGroup(
        #     Tex("Solve for $x$:").scale(LABEL_SCALE),
        #     MathTex(r"x = \frac{5 + \sqrt{37}}{2}").scale(MATH_SCALE),
        #     self.create_rect_group(
        #         MathTex(r"x = 5.541").scale(MATH_SCALE),
        #         buff=0.15
        #     )
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # answer2_group = VGroup(
        #     Tex("Solve for $x$:").scale(LABEL_SCALE),
        #     MathTex(r"x = \frac{5 - \sqrt{37}}{2}").scale(MATH_SCALE),
        #     self.create_rect_group(
        #         MathTex(r"x = -0.541").scale(MATH_SCALE),
        #         buff=0.15
        #     )
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        # answer_group = VGroup(
        #     answer1_group,
        #     answer2_group
        # ).arrange(RIGHT, aligned_edge=UP, buff=1.4)
        
        # answer_group.to_edge(UP, buff=1.2).to_edge(RIGHT, buff=0.8)
        
        # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # self.play(
        #     Write(answer1_group[0]),
        #     Write(answer2_group[0])
        # )
        
        # self.play(
        #     TransformFromCopy(s10_simplify2_step[1], answer1_group[1]),
        #     TransformFromCopy(s10_simplify2_step[1], answer2_group[1])
        # )

        # self.play(Write(answer1_group[2]))
        # self.play(Write(answer2_group[2]))
        
        # self.wait(2)