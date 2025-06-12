from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager_saved_1 import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class QuadraticFormula02(MathTutorialScene): 
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
               
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
                   
        question_text = Tex("Solve using the quadratic formula:").scale(LABEL_SCALE)
        question_equation = MathTex(r"4(x+5)^2 = 48").scale(S_MATH_SCALE)
        question_group = VGroup(
            question_text, 
            question_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)

        # Steps
        scroll = ScrollManager(scene=self)
        
        # Step 1: Divide both sides by 4
        sol1_step1 = scroll.construct_step(
            scroll.create_tex("First, get the equation in standard form:"),
            scroll.create_tex("Divide both sides by 4"),
            scroll.create_annotated_equation(
                r"4(x+5)^2 = 48",
                r"\div 4",
                "4",
                "48"
            ),
            scroll.create_math_tex(r"(x+5)^2 = 12", label="divided_by_4")
        )
        
        # Step 2: Expand the squared term
        sol1_step2 = scroll.construct_step(
            scroll.create_tex("Expand the squared term"),
            scroll.create_math_tex(r"(x+5)^2 = (x+5)(x+5)", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex("x^2 + 10x + 25 = 12", label="expand_squared_term")
        )
        
        # Step 3: Get in standard form
        sol1_step3 = scroll.construct_step(
            scroll.create_tex("Subtract 12 from both sides"),
            scroll.create_annotated_equation(
                r"x^2 + 10x + 25 = 12",
                "-12",
                "25",
                "12"
            ),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0", label="standard_form")
        )
        
        sol2_step1 = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:"),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0")
        )
        
        coefficient_values_in_equation = self.parse_elements(sol2_step1[1],
            ('a_value', 'x', 0, A_COLOR),  # Coefficient of x^2 is 1 (implicit)
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
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
                
        self.apply_smart_colorize(
            [quadratic_formula.formula, sol3_step1[1]],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )

        # Align the steps to the question
        sol_steps = scroll.get_arranged_equations()
        sol_steps.next_to(question_group, DOWN, buff=0.4).align_to(question_group, LEFT)

        # Initial setup animations
        self.play(
            Write(question_group, run_time=3),  # Write question and equation
        )
        
        self.wait(1)
        
        self.play(
            self.FadeInThenWrite(
                [quadratic_form.background, quadratic_formula.background],
                [quadratic_form.label, quadratic_formula.label, quadratic_form.formula, quadratic_formula.formula],
            )
        )
        
        # Step 1: Initial simplification
        # Animate: "First, get the equation in standard form:"
        scroll.prepare_next()
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))

        # Animate up to expanding the squared term
        scroll.prepare_next("expand_squared_term")
        
        # Scroll to keep content in view
        scroll.scroll_down("divided_by_4")

        # Animate up to standard form
        scroll.prepare_next("standard_form")
        scroll.scroll_down("standard_form")
        
        # Animate up to coefficient labels
        scroll.prepare_next("coefficient_c_label")
        
        # Animate coefficient highlighting and values
        # Fade in coefficient values with their corresponding equation elements
        self.play(self.indicate(quadratic_form_coefficients['a']))
        scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['b']))
        scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['c']))
        scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])

        scroll.scroll_down(steps=1)

        # Animate up to the quadratic formula
        scroll.prepare_next("quadratic_formula")
        
        # Scroll to keep formula in view
        scroll.scroll_down(steps=1)

        # Animate up to the empty quadratic formula
        scroll.prepare_next("empty_formula")
        
        # Animate coefficient substitutions with highlighting
        # Fade in each coefficient in its new position
        self.play(self.indicate(coefficient_values['b_value'], color=None))
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac)
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt)
        
        self.play(self.indicate(coefficient_values['a_value'], color=None))
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac)
        
        self.play(self.indicate(coefficient_values['c_value'], color=None))
        scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac)
        
        self.play(self.indicate(coefficient_values['a_value'], color=None))
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom)

        # Scroll to keep substitutions in view
        scroll.scroll_down("quadratic_formula")
        
        # Step 8: Initial simplification 
        # Animate: "Simplify the expression:"
        scroll.prepare_next()
        # Transform to simplified form
        scroll.transform_from_copy(sol3_step2[1], sol3_step3[1])
        
        # Scroll to keep simplification in view
        scroll.scroll_down("empty_formula")
        
        # Step 9: Further simplification (indices 24-25)
        # Animate: "Continue simplifying:"
        scroll.prepare_next()
        # Transform to next simplified form
        scroll.transform_from_copy(sol3_step3[1], sol3_step4[1])

        # Scroll to keep simplification in view
        scroll.scroll_down("simplified_expression")
        
        # Step 10: Square root simplification (indices 26-29)
        # Animate: "Simplify the square root:"
        scroll.prepare_next()
        
        # Highlight square root term
        self.play(self.indicate(sol3_step4_sqrt))
        
        # Transform square root simplification
        scroll.transform_from_copy(sol3_step4_sqrt, sol3_step5_solving['sqrt_48'])
        scroll.prepare_next("x_simplified_sqrt")
        
        # Scroll to keep square root simplification in view
        scroll.scroll_down("sqrt_48")
        
        # Step 11: Final simplification (indices 30-34)
        scroll.prepare_next("x=")
        
        # Transform to final simplified form
        scroll.transform_from_copy(sol3_step6_solving['first_frac'], sol3_step6_solved['first_frac_solved'])
        scroll.prepare_next("plus_minus")
        scroll.transform_from_copy(sol3_step6_solving['second_frac'], sol3_step6_solved['second_frac_solved'])

        # Final answers
        # Animate: "Solve for x:" labels
        self.play(
            Write(answer1_group[0]),
            Write(answer2_group[0])
        )
        
        # Transform to final answers
        self.play(
            TransformFromCopy(sol3_step6[2], answer1_group[1]),
            TransformFromCopy(sol3_step6[2], answer2_group[1])
        )
        
        # Show decimal approximations
        self.play(Write(answer1_group[2]))
        self.play(Write(answer2_group[2]))
        
        self.wait(2)