from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormula03(MathTutorialScene):
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
       
        
        quadratic_form_title = Tex("Standard Form").scale(LABEL_SCALE)
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(MATH_SCALE)
        
        quadratic_formula_title = Tex("Quadratic Formula").scale(LABEL_SCALE)
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(MATH_SCALE)
        
        
        quadratic_form_group = VGroup(
            quadratic_form_title,
            quadratic_form
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        quadratic_formula_group = VGroup(
            quadratic_formula_title,
            quadratic_formula
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        quadratic_group = VGroup(
            quadratic_form_group,
            quadratic_formula_group
        ).arrange(RIGHT, aligned_edge=UP, buff=0.7).to_corner(UR, buff=0.5).set_color(LIGHT_GRAY)
        
        
        quadratic_form_bg = SurroundingRectangle(
            quadratic_form_group,
            buff=0.25,
            fill_opacity=0.02,
            fill_color=WHITE,
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1,
            corner_radius=0.1
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula_group,
            buff=0.25,
            fill_opacity=0.02,
            fill_color=WHITE,
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1,
            corner_radius=0.1
        )
        
        
        quadratic_form_coefficients = self.parse_elements(quadratic_form,
            ('a', 'a', 0, A_COLOR),
            ('b', 'b', 0, B_COLOR),
            ('c', 'c', 0, C_COLOR)
        )
        
        
        question_text = Tex("Solve using the quadratic formula:").scale(LABEL_SCALE)
        question_equation = MathTex(r"8x^2 - 8x - 3 = 0").scale(S_MATH_SCALE)
        question_group = VGroup(
            question_text, 
            question_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)
        
    
        
        sol2_step1 = VGroup(
            Tex("Identify the coefficients:").scale(LABEL_SCALE),
            MathTex(r"8x^2 - 8x - 3 = 0").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        coefficient_values_in_equation = self.parse_elements(sol2_step1[1],
            ('a_value', '8', 0, A_COLOR),
            ('b_value', '-8', 0, B_COLOR),
            ('c_value', '-3', 0, C_COLOR)
        )
           
        
        sol2_step2 = VGroup(
            MathTex(r"a = 8 \quad b = -8 \quad c = -3").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        coefficient_labels = self.parse_elements(sol2_step2[0],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
        
        coefficient_values = self.parse_elements(sol2_step2[0],
            ('a_value', '8', 0, A_COLOR),
            ('b_value', '-8', 0, B_COLOR),
            ('c_value', '-3', 0, C_COLOR)
        )
        
        coefficient_labels_group = VGroup(*coefficient_labels.values())
        coefficient_values_group = VGroup(*coefficient_values.values())
        
        
        sol3_step1 = VGroup(
            Tex("Use the quadratic formula to solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step2 = VGroup(
            Tex("Substitute the coefficients into the formula:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-(-8) \pm \sqrt{(-8)^2 - 4(8)(-3)}}{2(8)}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step3 = VGroup(
            Tex("Simplify the expression:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{8 \pm \sqrt{64 + 96}}{16}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4 = VGroup(
            Tex("Continue simplifying:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{8 \pm \sqrt{160}}{16}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4_sqrt = sol3_step4[1][0][4:9].set_color(YELLOW)
        
        
        sol3_step5 = VGroup(
            Tex("Simplify the square root:").scale(LABEL_SCALE),
            MathTex(r"\sqrt{160} = \sqrt{16 \times 10} = 4\sqrt{10}").scale(MATH_SCALE),
            MathTex(r"x = \frac{8 \pm 4\sqrt{10}}{16}").scale(MATH_SCALE)    
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step5_1_sqrt = sol3_step5[1][0][:5]
        sol3_step5_1_sqrt_solve = sol3_step5[1][0][5:]
        sol3_step5_1_sqrt_ans = sol3_step5[1][0][-5:].set_color(YELLOW)
        sol3_step5_2_sqrt = sol3_step5[2][0][4:9].set_color(YELLOW)
        
        # Step 6: Final simplification
        sol3_step6 = VGroup(
            Tex("We can divide throughout by 4").scale(LABEL_SCALE),
            MathTex(r"x = \frac{8 \pm 4\sqrt{10}}{16} = \frac{8}{16} \pm \frac{4\sqrt{10}}{16}").scale(MATH_SCALE),
            MathTex(r"x = \frac{1}{2} \pm \frac{\sqrt{10}}{4}").scale(MATH_SCALE),
            MathTex(r"x = \frac{2 \pm \sqrt{10}}{4}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        

        
        answer1_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{2 - \sqrt{10}}{4}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = -0.291").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        answer2_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{2 + \sqrt{10}}{4}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x = 1.291").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        
        answer_group = VGroup(
            answer1_group,
            answer2_group
        ).arrange(RIGHT, aligned_edge=UP, buff=1.4)
        
        answer_group.next_to(quadratic_group, DOWN, buff=1)
        
        
        
        
        coefficient_values_in_formula = self.parse_elements(sol3_step2[1],
            ('b_in_frac', '-8', 0, B_COLOR, 0),
            ('b_in_sqrt', '-8', 1, B_COLOR, 0),
            ('a_in_4ac', '8', 2, A_COLOR, 0),
            ('c_in_4ac', '-3', 0, C_COLOR, 0),
            ('a_in_denom', '8', -1, A_COLOR, 0)
        )
        
        visible_copies = VGroup()

        for name, element in coefficient_values_in_formula.items():
            visible_copy = element.copy().set_opacity(1)
            setattr(visible_copies, name, visible_copy)
            visible_copies.add(visible_copy)

        sol3_step2[1].add(visible_copies)
        
        
        
        self.apply_smart_colorize(
            [quadratic_formula, sol3_step1[1]],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        
        
        
        
        sol_steps = VGroup(
            sol2_step1,
            sol2_step2,
            sol3_step1,
            sol3_step2,
            sol3_step3,
            sol3_step4,
            sol3_step5,
            sol3_step6
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        sol_steps.next_to(question_group, DOWN, buff=0.4).align_to(question_group, LEFT)
        
        
        sol_steps_elements = VGroup(
            *sol2_step1,
            *coefficient_labels_group,
            *coefficient_values_group,
            *sol3_step1,
            *sol3_step2,
            *visible_copies,
            *sol3_step3,
            *sol3_step4,
            sol3_step5[0],
            sol3_step5_1_sqrt,
            sol3_step5_1_sqrt_solve,
            sol3_step5[2],
            *sol3_step6
        )
        sol_steps_scroll = ScrollManager(sol_steps_elements, scene=self)
        
        
        
        
        self.play(
            Write(question_group, run_time=3),
        )
        
        self.wait(1)
        
        self.play(
            FadeIn(
                quadratic_form_bg,
                quadratic_formula_bg
            ),
            Write(quadratic_group, run_time=3)
        )
        
        
        

    
        # Step 1: Already in standard form
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        
        sol_steps_scroll.prepare_next(steps=3)
        
        sol_steps_scroll.fade_in_from_target(coefficient_values_in_equation['a_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values_in_equation['b_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values_in_equation['c_value'])

        
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        
        sol_steps_scroll.scroll_down(steps=1)
        
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        
        sol_steps_scroll.fade_in_from_target(coefficient_values['b_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values['b_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values['a_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values['c_value'])
        sol_steps_scroll.fade_in_from_target(coefficient_values['a_value'])
        
        sol_steps_scroll.scroll_down(steps=8)

        sol_steps_scroll.prepare_next()
        sol_steps_scroll.transform_from_copy(sol3_step2[1], sol3_step3[1])
        
        sol_steps_scroll.scroll_down(steps=2)
        
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.transform_from_copy(sol3_step3[1], sol3_step4[1])
        
        sol_steps_scroll.scroll_down(steps=7)
        
        
        
        sol_steps_scroll.prepare_next()
        
        self.play(self.indicate(sol3_step4_sqrt))
        
        sol_steps_scroll.transform_from_copy(sol3_step4_sqrt, sol3_step5_1_sqrt)
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        
        sol_steps_scroll.scroll_down(steps=4)
        
        # Additional step for final simplification
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        sol_steps_scroll.prepare_next()
        
        sol_steps_scroll.prepare_next()
        
        
        self.play(
            Write(answer1_group[0]),
            Write(answer2_group[0])
        )
        
        self.play(
            TransformFromCopy(sol3_step6[3], answer1_group[1]),
            TransformFromCopy(sol3_step6[3], answer2_group[1])
        )
        
        self.play(Write(answer1_group[2]))
        self.play(Write(answer2_group[2]))
        
        self.wait(2)