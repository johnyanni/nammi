from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormula02(MathTutorialScene):
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
        question_equation = MathTex(r"4(x+5)^2 = 48").scale(S_MATH_SCALE)
        question_group = VGroup(
            question_text, 
            question_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)
        
    
        # Step 1: Divide both sides by 4
        sol1_step1 = VGroup(
            Tex("First, get the equation in standard form:").scale(LABEL_SCALE),
            Tex("Divide both sides by 4").scale(LABEL_SCALE),
            self.create_annotated_equation(
                r"4(x+5)^2 = 48",
                r"\div 4",
                "4",
                "48"
            ),
            MathTex(r"(x+5)^2 = 12").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 2: Expand the squared term
        sol1_step2 = VGroup(
            Tex("Expand the squared term:").scale(LABEL_SCALE),
            MathTex(r"(x+5)^2 = (x+5)(x+5)").scale(M_MATH_SCALE).set_color(LIGHT_GRAY),
            MathTex(r"x^2 + 10x + 25 = 12").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Step 3: Get in standard form
        sol1_step3 = VGroup(
            Tex("Subtract 12 from both sides").scale(LABEL_SCALE),
            self.create_annotated_equation(
                r"x^2 + 10x + 25 = 12",
                "-12",
                "25",
                "12"
            ),
            MathTex(r"x^2 + 10x + 13 = 0").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        

        
        sol2_step1 = VGroup(
            Tex("Now, identify the coefficients:").scale(LABEL_SCALE),
            MathTex(r"x^2 + 10x + 13 = 0").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        coefficient_values_in_equation = self.parse_elements(sol2_step1[1],
            ('a_value', 'x', 0, A_COLOR),  # Coefficient of x^2 is 1 (implicit)
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )
           
        
        sol2_step2 = VGroup(
            MathTex(r"a = 1 \quad b = 10 \quad c = 13").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

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
        
        
        sol3_step1 = VGroup(
            Tex("Use the quadratic formula to solve for $x$:").scale(LABEL_SCALE),
            MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step2 = VGroup(
            Tex("Substitute the coefficients into the formula:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-(10) \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step3 = VGroup(
            Tex("Simplify the expression:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4 = VGroup(
            Tex("Continue simplifying:").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-10 \pm \sqrt{48}}{2}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step4_sqrt = sol3_step4[1][0][6:10]
        
        sol3_step5 = VGroup(
            Tex("Simplify the square root:").scale(LABEL_SCALE),
            MathTex(r"\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}").scale(M_MATH_SCALE).set_color(LIGHT_GRAY),
            MathTex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}").scale(MATH_SCALE)    
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        sol3_step5_solving = self.parse_elements(sol3_step5[1],
            ('sqrt_48', r'\sqrt{48}'),
            ('sqrt_48_solve', r'= \sqrt{16 \times 3} ='),
            ('sqrt_48_solved', r'4\sqrt{3}', 0, YELLOW),
        )
        sol3_step5_2_sqrt = sol3_step5[2][0][6:10].set_color(YELLOW)
        
        
        
        
        # Step 6: Final simplification
        sol3_step6 = VGroup(
            Tex(r"\raggedright We can further simplify \\ by dividing throughout by 2").scale(LABEL_SCALE),
            MathTex(r"x = \frac{-10 \pm 4\sqrt{3}}{2} = \frac{-10}{2} \pm \frac{4\sqrt{3}}{2}").scale(MATH_SCALE),
            MathTex(r"x = -5 \pm 2\sqrt{3}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
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
        
        
        
        self.apply_smart_colorize(
            [quadratic_formula, sol3_step1[1]],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        
        
        
        
        sol_steps = VGroup(
            sol1_step1,
            sol1_step2,
            sol1_step3,
            sol2_step1,
            sol2_step2,
            sol3_step1,
            sol3_step2,
            sol3_step3,
            sol3_step4,
            sol3_step5,
            sol3_step6
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sol_steps.next_to(question_group, DOWN, buff=0.4).align_to(question_group, LEFT)
        
        
        sol_steps_elements = VGroup(
            *sol1_step1,
            *sol1_step2,
            *sol1_step3,
            *sol2_step1,
            *coefficient_labels.values(),
            *coefficient_values.values(),
            *sol3_step1,
            *sol3_step2,
            *visible_copies,
            *sol3_step3,
            *sol3_step4,
            sol3_step5[0],
            sol3_step5_solving['sqrt_48'],
            sol3_step5_solving['sqrt_48_solve'],
            sol3_step5_solving['sqrt_48_solved'],
            sol3_step5[2],
            sol3_step6[0],
            sol3_step6[1],
            sol3_step6_solved['x='],
            sol3_step6_solved['first_frac_solved'],
            sol3_step6_solved['plus_minus'],
            sol3_step6_solved['second_frac_solved']
        )
        scroll = ScrollManager(sol_steps_elements, scene=self)
        
        
        
        
        # Initial setup animations with voiceover
        with self.voiceover(
            text="""Let's solve this quadratic equation using the quadratic formula. We have 4 times the quantity x plus 5 squared equals 48."""
        ) as tracker:
            self.play(
                Write(question_group, run_time=4),  # Increased from 3
            )
        
        with self.voiceover(
            text="""Here's the standard form of a quadratic equation, 
            where a, b, and c are coefficients."""
        ) as tracker:
            self.play(FadeIn(quadratic_form_bg, run_time=1.5))
            self.play(Write(quadratic_form_group, run_time=3))
            
        self.wait(1)
        
        
        with self.voiceover(
            text="""And this is the quadratic formula we'll use to solve for x."""
        ) as tracker:
            self.play(FadeIn(quadratic_formula_bg, run_time=1.5))
            self.play(Write(quadratic_formula_group, run_time=2))
        
        self.wait(1)
        
        
        
        # Step 1: Initial simplification
        with self.voiceover(
            text="""First, we need to get our equation into standard form. 
            <bookmark mark="A"/>Let's divide both sides by 4 to simplify. 
            <bookmark mark="B"/>We divide 4 by 4 to get 1, and 48 by 4 to get 12. 
            <bookmark mark="C"/>This gives us x plus 5 squared equals 12."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "First, get the equation..."
            self.wait_until_bookmark("A")
            self.play(self.indicate(quadratic_form_group, scale_factor=1.2, run_time=1.5))
            scroll.prepare_next(run_time=1.5)  # "Divide both sides by 4"
            
            self.wait_until_bookmark("B")
            scroll.prepare_next(run_time=2)  # Annotated equation
            
            self.wait_until_bookmark("C")
            scroll.prepare_next(run_time=1.5)  # Result
        
        self.wait(2)
        
        # Step 2: Expand squared term
        with self.voiceover(
            text="""Now let's expand the squared term. 
            <bookmark mark="A"/>X plus 5 squared means x plus 5 times x plus 5. 
            <bookmark mark="B"/>Using FOIL, we get x squared plus 10x plus 25 equals 12."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Expand the squared term:"
            
            self.wait_until_bookmark("A")
            scroll.prepare_next(run_time=2)  # Expansion visualization
            
            self.wait_until_bookmark("B")
            scroll.prepare_next(run_time=2)  # Final expanded form
        
        self.wait(1)
        scroll.scroll_down(steps=3, run_time=1.5)
        self.wait(1)
        
        # Step 3: Standard form conversion
        with self.voiceover(
            text="""To get standard form, we need everything on one side equal to zero. 
            <bookmark mark="A"/>Let's subtract 12 from both sides. 
            <bookmark mark="B"/>This gives us x squared plus 10x plus 13 equals 0. 
            Now we're in standard form!"""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Subtract 12 from both sides"
            
            self.wait_until_bookmark("A")
            scroll.prepare_next(run_time=2)  # Annotated subtraction
            
            self.wait_until_bookmark("B")
            scroll.prepare_next(run_time=2)  # Final standard form
        
        self.wait(1)
        total_in_view = scroll.current_position - scroll.last_in_view
        scroll.scroll_down(self, steps=total_in_view - 1, run_time=1.5)
        self.wait(1)
        
        # Step 4: Coefficient identification
        with self.voiceover(
            text="""Now we identify the coefficients. 
            <bookmark mark="A"/>In our equation, the coefficient of x squared is 1, 
            <bookmark mark="B"/>the coefficient of x is 10, 
            <bookmark mark="C"/>and the constant term is 13."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Now, identify..."
            scroll.prepare_next(run_time=1.5)  # Equation
            scroll.prepare_next(steps=3, run_time=2)  # Coefficient display

            self.wait_until_bookmark("A")
            self.play(self.indicate(quadratic_form_coefficients['a'], run_time=1.5))
            scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'], run_time=1)
            
            self.wait_until_bookmark("B")
            self.play(self.indicate(quadratic_form_coefficients['b'], run_time=1.5))
            scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'], run_time=1)
            
            self.wait_until_bookmark("C")
            self.play(self.indicate(quadratic_form_coefficients['c'], run_time=1.5))
            scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'], run_time=1)
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)
        self.wait(2)

        # Step 6: Quadratic formula introduction
        with self.voiceover(
            text="""Now we'll use the quadratic formula to solve for x. 
            <bookmark mark="A"/>Here's the formula with our color-coded coefficients."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Use the quadratic formula..."
            
            self.wait_until_bookmark("A")
            scroll.prepare_next(run_time=2.5)  # Formula display (complex formula)
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)
        self.wait(1)
        
        # Step 7: Coefficient substitution
        with self.voiceover(
            text="""Let's substitute our values into the formula. 
            <bookmark mark="A"/>We replace b with 10, appearing twice in the formula. 
            <bookmark mark="B"/>We replace a with 1 in the 4ac term, 
            <bookmark mark="C"/>c with 13, 
            <bookmark mark="D"/>and a with 1 again in the denominator."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Substitute the coefficients..."
            scroll.prepare_next(run_time=2.5)  # Substituted formula
            
            self.wait_until_bookmark("A")
            self.play(self.indicate(coefficient_values['b_value'], color=None, run_time=1.5))
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac, run_time=1.2)
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt, run_time=1.2)
            
            self.wait_until_bookmark("B")
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=1.5))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac, run_time=1.2)
            
            self.wait_until_bookmark("C")
            self.play(self.indicate(coefficient_values['c_value'], color=None, run_time=1.5))
            scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac, run_time=1.2)
            
            self.wait_until_bookmark("D")
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=1.5))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom, run_time=1.2)
        
        self.wait(1)
        scroll.scroll_down(steps=8, run_time=2)
        self.wait(1)

        # Step 8: Initial simplification
        with self.voiceover(
            text="""Now let's simplify. <bookmark mark="A"/>Negative 10 stays as negative 10. 
            10 squared is 100. 4 times 1 times 13 is 52. And 2 times 1 is 2."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Simplify the expression:"
            
            self.wait_until_bookmark("A")
            scroll.transform_from_copy(sol3_step2[1], sol3_step3[1], run_time=2.5)
        
        self.wait(1)
        scroll.scroll_down(steps=2, run_time=1)
        self.wait(1)
        
        # Step 9: Further simplification
        with self.voiceover(
            text="""Continuing to simplify, <bookmark mark="A"/>100 minus 52 equals 48."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Continue simplifying:"
            
            self.wait_until_bookmark("A")
            scroll.transform_from_copy(sol3_step3[1], sol3_step4[1], run_time=2)
        
        self.wait(1)
        scroll.scroll_down(steps=7, run_time=1.5)
        self.wait(1)
        
        # Step 10: Square root simplification
        with self.voiceover(
            text="""<bookmark mark="A"/>Now we need to simplify the square root of 48. 
            <bookmark mark="B"/>We can factor 48 as 16 times 3. 
            <bookmark mark="C"/>Since the square root of 16 is 4, 
            we get 4 times the square root of 3."""
        ) as tracker:
            scroll.prepare_next(run_time=1.5)  # "Simplify the square root:"
            
            self.wait_until_bookmark("A")
            self.play(self.indicate(sol3_step4_sqrt, run_time=2))
            
            self.wait_until_bookmark("B")
            scroll.transform_from_copy(sol3_step4_sqrt, sol3_step5_solving['sqrt_48'], run_time=1.5)
            scroll.prepare_next(run_time=1.5)  # Show factorization
            
            self.wait_until_bookmark("C")
            scroll.prepare_next(run_time=1.5)  # Show 4√3
            scroll.prepare_next(run_time=2)  # Show final formula with 4√3
        
        self.wait(1)
        scroll.scroll_down(steps=4, run_time=1.5)
        self.wait(1)
        
        # Step 11: Final simplification
        with self.voiceover(
            text="""We can simplify further by dividing both terms in the numerator by 2. 
            <bookmark mark="A"/>Negative 10 divided by 2 is negative 5. 
            <bookmark mark="B"/>And 4 square root 3 divided by 2 is 2 square root 3. 
            <bookmark mark="C"/>So our solution is x equals negative 5 plus or minus 2 square root 3."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # "We can further simplify..."
            scroll.prepare_next(run_time=2.5)  # Division steps
            
            scroll.prepare_next(run_time=0.5) # Show =
            self.wait_until_bookmark("A")
            scroll.transform_from_copy(sol3_step6_solving['first_frac'], sol3_step6_solved['first_frac_solved'], run_time=1.5)
            scroll.prepare_next(run_time=0.5)  # Show ±
            
            self.wait_until_bookmark("B")
            scroll.transform_from_copy(sol3_step6_solving['second_frac'], 
                                     sol3_step6_solved['second_frac_solved'], run_time=1.5)
        
        self.wait(2)
        
        # Final answers
        with self.voiceover(
            text="""<bookmark mark="A"/>This gives us two solutions. 
            <bookmark mark="B"/>For the first solution, we subtract: 
            negative 5 minus 2 square root 3, which equals approximately negative 8.464. 
            <bookmark mark="C"/>For the second solution, we add: 
            negative 5 plus 2 square root 3, which equals approximately negative 1.536. 
            <bookmark mark="D"/>And those are our two solutions!"""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(
                Write(answer1_group[0], run_time=1.5),
                Write(answer2_group[0], run_time=1.5)
            )
            
            self.wait_until_bookmark("B")
            self.play(
                TransformFromCopy(sol3_step6[2], answer1_group[1], run_time=2),
                TransformFromCopy(sol3_step6[2], answer2_group[1], run_time=2)
            )
            
            self.wait_until_bookmark("C")
            self.play(Write(answer1_group[2], run_time=2))
            
            self.wait_until_bookmark("D")
            self.play(Write(answer2_group[2], run_time=2))
        
        self.wait(3)  # Final pause