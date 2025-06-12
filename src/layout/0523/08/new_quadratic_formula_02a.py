from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class NEWQuadraticFormula01(MathTutorialScene): 
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        
        
        
        
        
        # ============================================
        # SECTION 1: QUESTION
        # ============================================
        
        question_text = MathTex(r"\text{Solve using the quadratic formula:} \; 4(x+5)^2 = 48").scale(LABEL_SCALE).set_color(LIGHT_GRAY).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4)

        self.play(
            Write(question_text, run_time=3),  
        )
        
        self.wait(1)    
    
    
    
    
    
        # ============================================
        # SECTION 2: FORMULAS
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
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.5).to_corner(DR, buff=0.3).set_color(LIGHT_GRAY)
        
        # DEV MODE        
        # quadratic_form_coefficients = self.parse_elements(quadratic_form.formula,
        #     ('a', 'a', 0, A_COLOR),
        #     ('b', 'b', 0, B_COLOR),
        #     ('c', 'c', 0, C_COLOR)
        # )
        
        
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
                           
                   
                   

        
        
        


        # Steps
        scroll = ScrollManager(scene=self)
        scroll.set_position_target(question_text, DOWN, buff=0.3, align_edge=LEFT)
        
        
        
        
        
        
        
        # ============================================
        # SECTION 3: SOLUTION
        # ============================================
        
        
        
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
            scroll.create_math_tex(r"(x+5)^2 = 12", label="m_divide_by_4_result")
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
        scroll.scroll_down("ae_divide_both_sides_by_4")
        
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
            
        
        # ======== Step 4: Standard form: Identify coefficients ========
        
        identify_coefficients_step = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:", label="l_identify_coefficients"),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0", label="m_standard_form_equation")
        )
        
        coefficient_values_in_equation = self.parse_elements(
            scroll.get_by_label("m_standard_form_equation"),
            ('a_value', 'x', 0, A_COLOR),  
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR),
        )
        
        
        
        
        
           
        sol2_step2 = scroll.construct_step(
            scroll.create_math_tex(r"a = 1 \quad b = 10 \quad c = 13"),
            add_to_scroll=False
        )
        
        coefficient_labels = self.parse_elements(sol2_step2[0],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
                
        coefficient_values = self.parse_elements(sol2_step2[0],
            ('a_value', '1', 0, A_COLOR),
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )

        scroll.create_steps(coefficient_labels.values(), [None, None, "coefficient_c_label"], arrange=False)
        scroll.create_steps(coefficient_values.values(), arrange=False)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        sol3_step1 = scroll.construct_step(
            scroll.create_tex("Use the quadratic formula to solve for $x$:"),
            scroll.create_math_tex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", label="quadratic_formula")
        )
        
        sol3_step2 = scroll.construct_step(
            scroll.create_tex("Substitute the coefficients into the formula:"),
            scroll.create_math_tex(r"x = \frac{-(10) \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}"),
            add_to_scroll=False,
            arrange=False
        )
        
        coefficient_values_in_formula = self.parse_elements(sol3_step2[1],
            ('b_in_frac', '10', 0, B_COLOR, 0),
            ('b_in_sqrt', '10', 1, B_COLOR, 0),
            ('a_in_4ac', '1', 2, A_COLOR, 0),
            ('c_in_4ac', '13', 0, C_COLOR, 0),
            ('a_in_denom', '1', -1, A_COLOR, 0)
        )
        
        visible_copies = VGroup()

        for name, element in coefficient_values_in_formula.items():
            visible_copy = element.copy().set_opacity(1)
            setattr(visible_copies, name, visible_copy)
            visible_copies.add(visible_copy)
            
        sol3_step2[1].add(visible_copies)
        scroll.create_steps(sol3_step2, [None, "empty_formula"])
        scroll.create_steps(visible_copies, arrange=False)
        
        sol3_step3 = scroll.construct_step(
            scroll.create_tex("Simplify the expression:"),
            scroll.create_math_tex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}", label="simplified_expression")
        )
        
        sol3_step4 = scroll.construct_step(
            scroll.create_tex("Continue simplifying:"),
            scroll.create_math_tex(r"x = \frac{-10 \pm \sqrt{48}}{2}")
        )
        
        sol3_step4_sqrt = sol3_step4[1][0][6:10]

        sol3_step5 = scroll.construct_step(
            scroll.create_tex("Simplify the square root:"),
            scroll.create_math_tex(r"\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}"),
            add_to_scroll=False
        )
        
        sol3_step5_solving = self.parse_elements(sol3_step5[1],
            ('sqrt_48', r'\sqrt{48}'),
            ('sqrt_48_solve', r'= \sqrt{16 \times 3} ='),
            ('sqrt_48_solved', r'4\sqrt{3}', 0, YELLOW),
        )
        
        SmartColorizeStatic(sol3_step5[2], {r"4\sqrt{3}": YELLOW})
                
        scroll.create_step(sol3_step5[0], arrange=False)
        scroll.create_steps(sol3_step5_solving.values(), ["sqrt_48", "sqrt_48_solve", "sqrt_48_solved"], arrange=False)
        scroll.create_step(sol3_step5[2], "x_simplified_sqrt", arrange=False)
        
        sol3_step6 = scroll.construct_step(
            scroll.create_tex(r"\raggedright We can further simplify \\ by dividing throughout by 2"),
            scroll.create_math_tex(r"x = \frac{-10 \pm 4\sqrt{3}}{2} = \frac{-10}{2} \pm \frac{4\sqrt{3}}{2}"),
            scroll.create_math_tex(r"x = -5 \pm 2\sqrt{3}"),
            add_to_scroll=False
        )
        scroll.create_steps(sol3_step6[:-1], arrange=False)
        
        sol3_step6_solving = self.parse_elements(sol3_step6[1],
            ('first_frac', r'\frac{-10}{2}', 0, LIGHT_GRAY),  
            ('second_frac', r'\frac{4\sqrt{3}}{2}', 0, LIGHT_GRAY), 
        )
        
        sol3_step6_solved = self.parse_elements(sol3_step6[2],
            ('x=', 'x ='),
            ('first_frac_solved', '-5'), 
            ('plus_minus', r'\pm'),
            ('second_frac_solved', r'2\sqrt{3}'),  
        )
        scroll.create_steps(sol3_step6_solved.values(), ["x=", None, "plus_minus", None], arrange=False)
        
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
                
        # self.apply_smart_colorize(
        #     [quadratic_formula.formula, sol3_step1[1]],
        #     {
        #         "a": A_COLOR, 
        #         "b": B_COLOR, 
        #         "c": C_COLOR,
        #     }
        # )








        

        
        

        
        
        
        
        
        