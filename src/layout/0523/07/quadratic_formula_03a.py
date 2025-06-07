from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip

config.verbosity = "ERROR"

class QuadraticFormula03a(MathTutorialScene):
    def construct(self):
        # ============================================
        # CONFIGURATION
        # ============================================
        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        # Problem parameters
        EQUATION = r"x - \frac{3}{x} = 4"
        A_VALUE = 1
        B_VALUE = -4
        C_VALUE = -3
        
        # ============================================
        # SECTION 1: HEADER (Standard Form & Formula)
        # ============================================
        quadratic_form_title = Tex("Standard Form").scale(LABEL_SCALE)
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(MATH_SCALE)
        
        quadratic_formula_title = Tex("Quadratic Formula").scale(LABEL_SCALE)
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(MATH_SCALE)
        
        # Group standard form elements
        quadratic_form_group = VGroup(
            quadratic_form_title,
            quadratic_form
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Group quadratic formula elements
        quadratic_formula_group = VGroup(
            quadratic_formula_title,
            quadratic_formula
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Combine both groups
        quadratic_group = VGroup(
            quadratic_form_group,
            quadratic_formula_group
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.7).to_corner(DR, buff=0.5).set_color(LIGHT_GRAY)
        
        # Create background rectangles
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
        
        # Color the coefficients in standard form
        quadratic_form_coefficients = self.parse_elements(quadratic_form,
            ('a', 'a', 0, A_COLOR),
            ('b', 'b', 0, B_COLOR),
            ('c', 'c', 0, C_COLOR)
        )
        
        # ============================================
        # SECTION 2: QUESTION
        # ============================================
        question_text = MathTex(rf"\text{{Solve using the quadratic formula:}} \; {EQUATION}").scale(LABEL_SCALE).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)
        
        # ============================================
        # SECTION 3: CLEAR FRACTIONS - MULTIPLY BY x
        # ============================================
        multiply_intro = Tex("First, clear the fraction by multiplying both sides by $x$:").scale(LABEL_SCALE)
        multiply_label = Tex("Multiply both sides by $x$").scale(LABEL_SCALE)
        multiply_annotation = self.create_annotated_equation(
            r"x - \frac{3}{x} = 4",
            r"\times x",
            r"\frac{3}{x}",
            "4"
        )
        multiply_result = MathTex(r"x^2 - 3 = 4x").scale(MATH_SCALE)
        
        multiply_group = VGroup(
            multiply_intro,
            multiply_label,
            multiply_annotation,
            multiply_result
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 4: REARRANGE TO STANDARD FORM
        # ============================================
        rearrange_label = Tex("Rearrange to get standard form:").scale(LABEL_SCALE)
        rearrange_step1 = MathTex(r"x^2 - 4x - 3 = 0").scale(MATH_SCALE)
        
        rearrange_group = VGroup(
            rearrange_label,
            rearrange_step1
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 5: IDENTIFY COEFFICIENTS
        # ============================================
        identify_label = Tex("Now, identify the coefficients:").scale(LABEL_SCALE)
        identify_equation = MathTex(r"x^2 - 4x - 3 = 0").scale(MATH_SCALE)
        
        identify_step = VGroup(
            identify_label,
            identify_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse coefficient positions in the equation
        coefficient_values_in_equation = self.parse_elements(identify_equation,
            ('a_value', 'x', 0, A_COLOR),  # a = 1 (implicit)
            ('b_value', '-4', 0, B_COLOR),
            ('c_value', '-3', 0, C_COLOR)
        )
        
        # Display coefficient values
        coefficient_display = MathTex(rf"a = {A_VALUE} \quad b = {B_VALUE} \quad c = {C_VALUE}").scale(MATH_SCALE)
        
        coefficient_labels = self.parse_elements(coefficient_display,
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
        
        coefficient_values = self.parse_elements(coefficient_display,
            ('a_value', str(A_VALUE), 0, A_COLOR),
            ('b_value', str(B_VALUE), 0, B_COLOR),
            ('c_value', str(C_VALUE), 0, C_COLOR)
        )
        
        # ============================================
        # SECTION 6: SHOW QUADRATIC FORMULA
        # ============================================
        show_formula_label = Tex("Use the quadratic formula to solve for $x$:").scale(LABEL_SCALE)
        show_formula_equation = MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        
        show_formula_step = VGroup(
            show_formula_label,
            show_formula_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 7: SUBSTITUTE VALUES
        # ============================================
        substitute_label = Tex("Substitute the coefficients into the formula:").scale(LABEL_SCALE)
        substitute_equation = MathTex(
            rf"x = \frac{{-({B_VALUE}) \pm \sqrt{{({B_VALUE})^2 - 4({A_VALUE})({C_VALUE})}}}}{{2({A_VALUE})}}"
        ).scale(MATH_SCALE)
        
        substitute_step = VGroup(
            substitute_label,
            substitute_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse substituted values (opacity 0 for animation)
        coefficient_values_in_formula = self.parse_elements(substitute_equation,
            ('b_in_frac', str(B_VALUE), 0, B_COLOR, 0),
            ('b_in_sqrt', str(B_VALUE), 1, B_COLOR, 0),
            ('a_in_4ac', str(A_VALUE), 2, A_COLOR, 0),
            ('c_in_4ac', str(C_VALUE), 0, C_COLOR, 0),
            ('a_in_denom', str(A_VALUE), -1, A_COLOR, 0)
        )
        
        # Create visible copies for animation
        visible_copies = VGroup()
        for name, element in coefficient_values_in_formula.items():
            visible_copy = element.copy().set_opacity(1)
            setattr(visible_copies, name, visible_copy)
            visible_copies.add(visible_copy)
        substitute_equation.add(visible_copies)
        
        # ============================================
        # SECTION 8: FIRST SIMPLIFICATION
        # ============================================
        # Calculate intermediate values
        B_SQUARED = B_VALUE ** 2
        FOUR_AC = 4 * A_VALUE * C_VALUE
        TWO_A = 2 * A_VALUE
        
        simplify1_label = Tex("Simplify the expression:").scale(LABEL_SCALE)
        simplify1_equation = MathTex(
            rf"x = \frac{{4 \pm \sqrt{{16 - (-12)}}}}{{2}}"
        ).scale(MATH_SCALE)
        
        simplify1_step = VGroup(
            simplify1_label,
            simplify1_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 9: SECOND SIMPLIFICATION
        # ============================================
        DISCRIMINANT = B_SQUARED - FOUR_AC
        
        simplify2_label = Tex("Continue simplifying:").scale(LABEL_SCALE)
        simplify2_equation = MathTex(
            rf"x = \frac{{4 \pm \sqrt{{28}}}}{{2}}"
        ).scale(MATH_SCALE)
        
        simplify2_step = VGroup(
            simplify2_label,
            simplify2_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Identify square root part for highlighting
        simplify2_sqrt = simplify2_equation[0][6:10]
        
        # ============================================
        # SECTION 10: SIMPLIFY SQUARE ROOT
        # ============================================
        sqrt_label = Tex("Simplify the square root:").scale(LABEL_SCALE)
        sqrt_intermediate = MathTex(r"\sqrt{28} = \sqrt{4 \times 7} = 2\sqrt{7}").scale(M_MATH_SCALE).set_color(LIGHT_GRAY)
        sqrt_result = MathTex(rf"x = \frac{{4 \pm 2\sqrt{{7}}}}{{2}}").scale(MATH_SCALE)
        
        sqrt_group = VGroup(
            sqrt_label,
            sqrt_intermediate,
            sqrt_result
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse square root simplification elements
        sqrt_parsing = self.parse_elements(sqrt_intermediate,
            ('sqrt_28', r'\sqrt{28}'),
            ('sqrt_28_solve', r'= \sqrt{4 \times 7} ='),
            ('sqrt_28_solved', r'2\sqrt{7}', 0, YELLOW),
        )
        sqrt_result_highlight = sqrt_result[0][6:10].set_color(YELLOW)
        
        # ============================================
        # SECTION 11: FINAL SIMPLIFICATION
        # ============================================
        final_label = Tex(r"\raggedright We can further simplify \\ by dividing throughout by 2").scale(LABEL_SCALE)
        final_equation = MathTex(
            rf"x = \frac{{4 \pm 2\sqrt{{7}}}}{{2}} = \frac{{4}}{{2}} \pm \frac{{2\sqrt{{7}}}}{{2}}"
        ).scale(MATH_SCALE)
        final_result = MathTex(r"x = 2 \pm \sqrt{7}").scale(MATH_SCALE)
        
        final_step = VGroup(
            final_label,
            final_equation,
            final_result
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse final simplification elements
        final_parsing = self.parse_elements(final_equation,
            ('first_frac', r'\frac{4}{2}', 0, LIGHT_GRAY),
            ('second_frac', r'\frac{2\sqrt{7}}{2}', 0, LIGHT_GRAY),
        )
        
        final_result_parsing = self.parse_elements(final_result,
            ('x=', 'x ='),
            ('first_frac_solved', '2'),
            ('plus_minus', r'\pm'),
            ('second_frac_solved', r'\sqrt{7}'),
        )
        
        # ============================================
        # SECTION 12: FINAL ANSWERS
        # ============================================
        # Calculate decimal approximations
        from math import sqrt
        SQRT_7 = sqrt(7)
        SOLUTION1_DECIMAL = 2 - SQRT_7
        SOLUTION2_DECIMAL = 2 + SQRT_7
        
        # Answer 1
        answer1_label = Tex("Solve for $x$:").scale(LABEL_SCALE)
        answer1_exact = MathTex(rf"x = 2 - \sqrt{{7}}").scale(MATH_SCALE)
        answer1_decimal = self.create_rect_group(
            MathTex(rf"x \approx {SOLUTION1_DECIMAL:.3f}").scale(MATH_SCALE),
            buff=0.15
        )
        answer1_group = VGroup(
            answer1_label,
            answer1_exact,
            answer1_decimal
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Answer 2
        answer2_label = Tex("Solve for $x$:").scale(LABEL_SCALE)
        answer2_exact = MathTex(rf"x = 2 + \sqrt{{7}}").scale(MATH_SCALE)
        answer2_decimal = self.create_rect_group(
            MathTex(rf"x \approx {SOLUTION2_DECIMAL:.3f}").scale(MATH_SCALE),
            buff=0.15
        )
        answer2_group = VGroup(
            answer2_label,
            answer2_exact,
            answer2_decimal
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Group answers side by side
        answer_group = VGroup(
            answer1_group,
            answer2_group
        ).arrange(RIGHT, aligned_edge=UP, buff=1.2)
        answer_group.to_edge(UP, buff=1.2).to_edge(RIGHT, buff=0.8)
        
        # ============================================
        # APPLY COLORS
        # ============================================
        self.apply_smart_colorize(
            [quadratic_formula, show_formula_equation],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        # ============================================
        # POSITION ALL SOLUTION STEPS
        # ============================================
        sol_steps = VGroup(
            multiply_group,
            rearrange_group,
            identify_step,
            coefficient_display,
            show_formula_step,
            substitute_step,
            simplify1_step,
            simplify2_step,
            sqrt_group,
            final_step
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sol_steps.next_to(question_text, DOWN, buff=0.2).align_to(question_text, LEFT)
        
        # ============================================
        # CREATE SCROLL ELEMENTS
        # ============================================
        # Define sections with clear comments
        sol_steps_elements = VGroup(
            # === MULTIPLY SECTION (4 elements) ===
            *multiply_group,
            
            # === REARRANGE SECTION (2 elements) ===
            *rearrange_group,
            
            # === IDENTIFY COEFFICIENTS SECTION (2 elements + 6 coefficient parts) ===
            *identify_step,
            *coefficient_labels.values(),
            *coefficient_values.values(),
            
            # === SHOW FORMULA SECTION (2 elements) ===
            *show_formula_step,
            
            # === SUBSTITUTE SECTION (2 elements + 5 visible copies) ===
            *substitute_step,
            *visible_copies,
            
            # === SIMPLIFICATION SECTION (4 elements) ===
            *simplify1_step,
            *simplify2_step,
            
            # === SQUARE ROOT SECTION (5 elements) ===
            sqrt_label,
            sqrt_parsing['sqrt_28'],
            sqrt_parsing['sqrt_28_solve'],
            sqrt_parsing['sqrt_28_solved'],
            sqrt_result,
            
            # === FINAL SIMPLIFICATION (6 elements) ===
            final_label,
            final_equation,
            final_result_parsing['x='],
            final_result_parsing['first_frac_solved'],
            final_result_parsing['plus_minus'],
            final_result_parsing['second_frac_solved']
        )
        
        scroll = ScrollManager(sol_steps_elements, scene=self)
        
        # ============================================
        # QUICK TIPS
        # ============================================
        
        tip_1 = QuickTip(r"When you have fractions in equations, multiply by the denominator to clear them")
        tip_1.to_corner(DL)
        
        # ============================================
        # ANIMATION SEQUENCE
        # ============================================
        
        # === INTRO: Show question and formulas ===
        with self.voiceover(
            text=f"""Let's solve this equation using the quadratic formula. 
            We have x minus 3 over x equals 4."""
        ) as tracker:
            self.play(Write(question_text, run_time=4))
            
        self.wait(1)
        
        with self.voiceover(
            text="""Here's the standard form of a quadratic equation, 
            where a, b, and c are coefficients."""
        ) as tracker:
            self.play(FadeIn(quadratic_form_bg, run_time=1))
            self.play(Write(quadratic_form_group, run_time=3))
        
        self.wait(1)
        
        with self.voiceover(
            text="""And this is the quadratic formula we'll use to solve for x."""
        ) as tracker:
            self.play(FadeIn(quadratic_formula_bg, run_time=1))
            self.play(Write(quadratic_formula_group, run_time=3))
        
        self.wait(1)
        
        # === STEP 1: Clear fractions ===
        with self.voiceover(
            text="""First, we need to clear the fraction to get a quadratic equation."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show intro
            self.play(FadeIn(tip_1, shift=UP))
            
        with self.voiceover(
            text="""Let's multiply both sides by x."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            
        self.wait(1)
        self.play(FadeOut(tip_1, shift=DOWN))
            
        with self.voiceover(
            text="""On the left side, x times x is x squared, and x times negative 3 over x is negative 3.
            On the right side, 4 times x is 4x."""
        ) as tracker:
            scroll.prepare_next(run_time=3)  # Show annotated equation
            
        with self.voiceover(
            text="""This gives us x squared minus 3 equals 4x."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show result
        
        self.wait(1)
        
        # === STEP 2: Rearrange to standard form ===
        with self.voiceover(
            text="""Now let's rearrange this into standard form by moving all terms to one side."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show rearrange label
            self.play(self.indicate(quadratic_form_group, scale_factor=1.2, run_time=3))
            
        with self.voiceover(
            text="""We subtract 4x from both sides to get x squared minus 4x minus 3 equals 0.
            <bookmark mark="A"/>
            Now we're in standard form!"""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show result
            self.wait_until_bookmark("A")
            self.play(self.indicate(quadratic_form_group, scale_factor=1.2, run_time=2))
        
        self.wait(1)
        total_in_view = scroll.current_position - scroll.last_in_view
        scroll.scroll_down(steps=total_in_view - 1, run_time=2)
        
        # === STEP 3: Identify coefficients ===
        with self.voiceover(
            text="""Now we identify the coefficients."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            scroll.prepare_next(run_time=2)  # Show equation
            scroll.prepare_next(steps=3, run_time=3)  # Show coefficient labels
            
        with self.voiceover(
            text=f"""In our equation, the coefficient of x squared is {A_VALUE}."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['a'], run_time=2))
            scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'], run_time=1.5)
            
        with self.voiceover(
            text=f"""The coefficient of x is negative 4."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['b'], run_time=2))
            scroll.fade_in_from_target(
                coefficient_values_in_equation['b_value'], 
                coefficient_values['b_value'], 
                run_time=1.5
            )
            
        with self.voiceover(
            text=f"""And the constant term is negative 3."""
        ) as tracker:
            self.play(self.indicate(quadratic_form_coefficients['c'], run_time=2))
            scroll.fade_in_from_target(
                coefficient_values_in_equation['c_value'], 
                coefficient_values['c_value'], 
                run_time=1.5
            )
            
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)
        
        # === STEP 4: Show quadratic formula ===
        with self.voiceover(
            text="""Now we'll use the quadratic formula to solve for x."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            self.play(self.indicate(quadratic_formula_group, scale_factor=1.2, run_time=3))
            
        with self.voiceover(
            text="""Here's the formula with our color-coded coefficients."""
        ) as tracker:
            scroll.prepare_next(run_time=4)  # Show formula

        self.wait(1)
        
        # === STEP 5: Substitute values ===
        with self.voiceover(
            text="""Let's substitute our values into the formula."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            scroll.prepare_next(run_time=4)  # Show substituted formula
            
        with self.voiceover(
            text=f"""We replace b with negative 4, appearing twice in the formula."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['b_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac, run_time=1.5)
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt, run_time=1.5)
            
        with self.voiceover(
            text=f"""We replace a with {A_VALUE} in the 4ac term."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac, run_time=1.5)
            
        with self.voiceover(
            text=f"""C with negative 3."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['c_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac, run_time=1.5)
            
        with self.voiceover(
            text=f"""And a with {A_VALUE} again in the denominator."""
        ) as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom, run_time=1.5)
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)

        # === STEP 6: First simplification ===
        with self.voiceover(
            text="""Now let's simplify."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            
        with self.voiceover(
            text=f"""Negative of negative 4 is positive 4. 
            Negative 4 squared is 16. 
            4 times 1 times negative 3 is negative 12. 
            And 2 times 1 is 2."""
        ) as tracker:
            scroll.transform_from_copy(substitute_equation, simplify1_equation, run_time=2)
        
            self.play(
                FadeOut(
                quadratic_group,
                quadratic_formula_bg,
                quadratic_form_bg
                )
            )
        
        self.wait(1)
        scroll.scroll_down(steps=7, run_time=1)
        
        # === STEP 7: Second simplification ===
        with self.voiceover(
            text="""Continuing to simplify."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            
        with self.voiceover(
            text=f"""16 minus negative 12 is 16 plus 12, which equals 28."""
        ) as tracker:
            scroll.transform_from_copy(simplify1_equation, simplify2_equation, run_time=2)
        
        self.wait(1)
        scroll.scroll_down(steps=9, run_time=1.5)
        
        # === STEP 8: Square root simplification ===
        with self.voiceover(
            text=f"""Now we need to simplify the square root of 28."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            self.play(self.indicate(simplify2_sqrt, run_time=2))
            
        with self.voiceover(
            text=f"""We can factor 28 as 4 times 7."""
        ) as tracker:
            
            scroll.transform_from_copy(simplify2_sqrt, sqrt_parsing['sqrt_28'], run_time=2)
            scroll.prepare_next(run_time=2)  # Show factorization

        with self.voiceover(
            text="""Since the square root of 4 is 2, 
            we get 2 times the square root of 7."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show 2√7
            scroll.prepare_next(run_time=3)  # Show final formula with 2√7
        
        self.wait(1)
        scroll.scroll_down(steps=2, run_time=1.5)
        
        # === STEP 9: Final simplification ===
        with self.voiceover(
            text=f"""We can simplify further by dividing both terms in the numerator by 2."""
        ) as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            scroll.prepare_next(run_time=4)  # Show division steps
        
        with self.voiceover(
            text=f"""4 divided by 2 is 2."""
        ) as tracker:
            scroll.prepare_next(run_time=0.5)  # Show x=
            
            scroll.transform_from_copy(
                final_parsing['first_frac'], 
                final_result_parsing['first_frac_solved'], 
                run_time=3
            )
            scroll.prepare_next(run_time=0.5)  # Show ±
            
        with self.voiceover(
            text=f"""And 2 square root 7 divided by 2 is square root 7."""
        ) as tracker:
            scroll.transform_from_copy(
                final_parsing['second_frac'], 
                final_result_parsing['second_frac_solved'], 
                run_time=3
            )
            
        with self.voiceover(
            text="""So our solution is x equals 2 plus or minus square root 7."""
        ) as tracker:
            self.wait(1)
        
        self.wait(2)
        
        # === STEP 10: Final answers ===
        with self.voiceover(
            text="""This gives us two solutions."""
        ) as tracker:
            self.play(
                Write(answer1_label, run_time=2),
                Write(answer2_label, run_time=2)
            )
            
        with self.voiceover(
            text="""For the first solution, we subtract: 
            2 minus square root 7."""
        ) as tracker:
            self.play(
                TransformFromCopy(final_result, answer1_exact, run_time=2),
                TransformFromCopy(final_result, answer2_exact, run_time=2)
            )
            
        with self.voiceover(
            text=f"""Which equals approximately {SOLUTION1_DECIMAL:.3f}."""
        ) as tracker:
            self.play(Write(answer1_decimal, run_time=2))
            
        with self.voiceover(
            text=f"""For the second solution, we add: 
            2 plus square root 7, which equals approximately {SOLUTION2_DECIMAL:.3f}."""
        ) as tracker:
            self.play(Write(answer2_decimal, run_time=2))
            
        with self.voiceover(
            text="""And those are our two solutions!"""
        ) as tracker:
            self.wait(1)
        
        self.wait(3)