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
        question_equation = MathTex(r"x^2 + 11x + 20 = 0").scale(S_MATH_SCALE)
        question_group = VGroup(
            question_text, 
            question_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)
        
        
        sol2_step1 = VGroup(
            Tex("Identify the coefficients:").scale(LABEL_SCALE),
            MathTex(r"x^2 + 11x + 20 = 0").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        coefficient_values_in_equation = self.parse_elements(sol2_step1[1],
            ('a_value', 'x', 0, A_COLOR),  # Coefficient of x^2 is 1 (implicit)
            ('b_value', '11', 0, B_COLOR),
            ('c_value', '20', 0, C_COLOR)
        )
           
        
        sol2_step2 = VGroup(
            MathTex(r"a = 1 \quad b = 11 \quad c = 20").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        coefficient_labels = self.parse_elements(sol2_step2[0],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
        
        coefficient_values = self.parse_elements(sol2_step2[0],
            ('a_value', '1', 0, A_COLOR),
            ('b_value', '11', 0, B_COLOR),
            ('c_value', '20', 0, C_COLOR)
        )
        
        
        sol3_step1 = VGroup(
            Tex("Use the quadratic formula to solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step2 = VGroup(
            Tex("Substitute the coefficients into the formula:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-(11) \pm \sqrt{(11)^2 - 4(1)(20)}}{2(1)}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step3 = VGroup(
            Tex("Simplify the expression:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-11 \pm \sqrt{121 - 80}}{2}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4 = VGroup(
            Tex("Continue simplifying:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-11 \pm \sqrt{41}}{2}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4_sqrt = sol3_step4[1][0][6:10]
        
        
        # Final answers
        answer1_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-11 - \sqrt{41}}{2}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x \approx -8.70").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        answer2_group = VGroup(
            Tex("Solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-11 + \sqrt{41}}{2}").scale(MATH_SCALE),
            self.create_rect_group(
                MathTex(r"x \approx -2.30").scale(MATH_SCALE),
                buff=0.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        
        answer_group = VGroup(
            answer1_group,
            answer2_group
        ).arrange(RIGHT, aligned_edge=UP, buff=1.4)
        
        answer_group.next_to(quadratic_group, DOWN, buff=1)
        
        
        
        
        coefficient_values_in_formula = self.parse_elements(sol3_step2[1],
            ('b_in_frac', '11', 0, B_COLOR, 0),
            ('b_in_sqrt', '11', 1, B_COLOR, 0),
            ('a_in_4ac', '1', 2, A_COLOR, 0),
            ('c_in_4ac', '20', 0, C_COLOR, 0),
            ('a_in_denom', '1', -1, A_COLOR, 0)
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
            sol3_step4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sol_steps.next_to(question_group, DOWN, buff=0.4).align_to(question_group, LEFT)
        
        
        sol_steps_elements = VGroup(
            *sol2_step1,
            *coefficient_labels.values(),
            *coefficient_values.values(),
            *sol3_step1,
            *sol3_step2,
            *visible_copies,
            *sol3_step3,
            *sol3_step4
        )
        scroll = ScrollManager(sol_steps_elements, scene=self)
        
        
        
        
        # Initial setup
        with self.voiceover(
            text="""Let's solve this quadratic equation using the quadratic formula. 
            We have x squared plus 11x plus 20 equals 0."""
        ) as tracker:
            self.play(
                Write(question_group, run_time=4),
            )
        
        # Show standard form
        with self.voiceover(
            text="""Notice that this equation is already in standard form,
            where a, b, and c are coefficients."""
        ) as tracker:
            self.play(FadeIn(quadratic_form_bg, run_time=1))
            self.play(Write(quadratic_form_group, run_time=3))
            
        self.wait(1)
        
        # Show quadratic formula
        with self.voiceover(
            text="""We'll use the quadratic formula to find the values of x."""
        ) as tracker:
            self.play(FadeIn(quadratic_formula_bg, run_time=1))
            self.play(Write(quadratic_formula_group, run_time=3))
        
        self.wait(1)
        
        # Step 1a: Coefficient identification intro
        with self.voiceover(
            text="""Let's identify the coefficients in our equation."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Tex
            scroll.prepare_next(run_time=2)  # MathTex
            scroll.prepare_next(steps=3, run_time=3)  # Coefficient labels
            
        # Step 1b: Coefficient a
        with self.voiceover(
            text="""The coefficient of x squared is 1."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['a'], run_time=2))
            scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], 
                                     coefficient_values['a_value'], run_time=1.5)
            
        # Step 1c: Coefficient b
        with self.voiceover(
            text="""The coefficient of x is 11."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['b'], run_time=2))
            scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], 
                                     coefficient_values['b_value'], run_time=1.5)
            
        # Step 1d: Coefficient c
        with self.voiceover(
            text="""And the constant term is 20."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['c'], run_time=2))
            scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], 
                                     coefficient_values['c_value'], run_time=1.5)
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)
        self.wait(2)

        # Step 2a: Quadratic formula intro
        with self.voiceover(
            text="""Now we'll apply the quadratic formula."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Tex
            
        # Step 2b: Show formula
        with self.voiceover(
            text="""Here's the formula with our color-coded coefficients."""
        ) as tracker:
            scroll.prepare_next(run_time=3)  # Complex MathTex
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)
        self.wait(1)
        
        # Step 3a: Substitution intro
        with self.voiceover(
            text="""Let's substitute our values into the formula."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Tex
            scroll.prepare_next(run_time=4)  # Very complex MathTex
            
        # Step 3b: Substitute b
        with self.voiceover(
            text="""We replace b with 11, which appears twice in the formula."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['b_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac, run_time=1.5)
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt, run_time=1.5)
            
        # Step 3c: Substitute a in 4ac
        with self.voiceover(
            text="""We replace a with 1 in the 4ac term."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac, run_time=1.5)
            
        # Step 3d: Substitute c
        with self.voiceover(
            text="""C becomes 20."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['c_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac, run_time=1.5)
            
        # Step 3e: Substitute a in denominator
        with self.voiceover(
            text="""And a is 1 in the denominator."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom, run_time=1.5)
        
        self.wait(1)
        scroll.scroll_down(steps=6, run_time=2)
        self.wait(1)

        # Step 4: Simplification
        with self.voiceover(
            text="""Now let's simplify the expression."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Tex
            
        with self.voiceover(
            text="""Negative 11 remains negative 11. 
            11 squared is 121. 4 times 1 times 20 is 80. And 2 times 1 is 2."""
        ) as tracker:
            scroll.transform_from_copy(sol3_step2[1], sol3_step3[1], run_time=2)
        
        self.wait(1)
        scroll.scroll_down(steps=2, run_time=1)
        self.wait(1)
        
        # Step 5: Further simplification
        with self.voiceover(
            text="""Let's continue simplifying."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Tex
            
        with self.voiceover(
            text="""121 minus 80 equals 41."""
        ) as tracker:
            scroll.transform_from_copy(sol3_step3[1], sol3_step4[1], run_time=2)
        
        self.wait(1)
        
        # Note about square root
        with self.voiceover(
            text="""Notice that 41 is a prime number, so we cannot simplify the square root further."""
        ) as tracker:
            self.play(self.indicate(sol3_step4_sqrt, run_time=2))
        
        self.wait(2)
        
        # Final answers - Part 1
        with self.voiceover(
            text="""This gives us two solutions."""
        ) as tracker:
            self.play(
                Write(answer1_group[0], run_time=2),
                Write(answer2_group[0], run_time=2)
            )
            
        # Final answers - Part 2
        with self.voiceover(
            text="""For the first solution, we have x equals negative 11 minus square root of 41, all divided by 2."""
        ) as tracker:
            self.play(
                TransformFromCopy(sol3_step4[1], answer1_group[1], run_time=2)
            )
            
        # Final answers - Part 3
        with self.voiceover(
            text="""Which equals approximately negative 8.70."""
        ) as tracker:
            self.play(Write(answer1_group[2], run_time=2))
            
        # Final answers - Part 4
        with self.voiceover(
            text="""For the second solution, we have negative 11 plus square root of 41, divided by 2."""
        ) as tracker:
            self.play(
                TransformFromCopy(sol3_step4[1], answer2_group[1], run_time=2)
            )
            
        # Final answers - Part 5
        with self.voiceover(
            text="""Which equals approximately negative 2.30."""
        ) as tracker:
            self.play(Write(answer2_group[2], run_time=2))
            
        # Closing
        with self.voiceover(
            text="""And those are our two solutions to the quadratic equation!"""
        ) as tracker:
            self.wait(1)
        
        self.wait(3)  # Final pause