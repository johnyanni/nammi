from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip

config.verbosity = "ERROR"

class QuadraticFormula01a(MathTutorialScene):
    def construct(self):
        # ============================================
        # CONFIGURATION
        # ============================================
        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        # Problem parameters - CHANGE THESE FOR NEW EXAMPLES
        EQUATION = r"x^2 + 11x + 20 = 0"
        A_VALUE = 1
        B_VALUE = 11
        C_VALUE = 20
        
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
        
        # Combine both groups - Updated to match 02a layout
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
        # SECTION 3: IDENTIFY COEFFICIENTS
        # ============================================
        identify_label = Tex("Identify the coefficients:").scale(LABEL_SCALE)
        identify_equation = MathTex(EQUATION).scale(MATH_SCALE)
        
        identify_step = VGroup(
            identify_label,
            identify_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse coefficient positions in the equation
        coefficient_values_in_equation = self.parse_elements(identify_equation,
            ('a_value', 'x' if A_VALUE == 1 else str(A_VALUE), 0, A_COLOR),
            ('b_value', str(B_VALUE), 0, B_COLOR),
            ('c_value', str(C_VALUE), 0, C_COLOR)
        )
        
        # Display coefficient values
        coefficient_display = MathTex(
            rf"a = {A_VALUE} \quad b = {B_VALUE} \quad c = {C_VALUE}"
        ).scale(MATH_SCALE)
        
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
        # SECTION 4: SHOW QUADRATIC FORMULA
        # ============================================
        show_formula_label = Tex("Use the quadratic formula to solve for $x$:").scale(LABEL_SCALE)
        show_formula_equation = MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}").scale(MATH_SCALE)
        
        show_formula_step = VGroup(
            show_formula_label,
            show_formula_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 5: SUBSTITUTE VALUES
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
            ('a_in_4ac', str(A_VALUE), -2, A_COLOR, 0),
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
        # SECTION 6: SIMPLIFICATION STEP 1
        # ============================================
        # Calculate intermediate values
        B_SQUARED = B_VALUE ** 2
        FOUR_AC = 4 * A_VALUE * C_VALUE
        TWO_A = 2 * A_VALUE
        
        simplify1_label = Tex("Simplify the expression:").scale(LABEL_SCALE)
        simplify1_equation = MathTex(
            rf"x = \frac{{-{B_VALUE} \pm \sqrt{{{B_SQUARED} - {FOUR_AC}}}}}{{{TWO_A}}}"
        ).scale(MATH_SCALE)
        
        simplify1_step = VGroup(
            simplify1_label,
            simplify1_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 7: SIMPLIFICATION STEP 2
        # ============================================
        DISCRIMINANT = B_SQUARED - FOUR_AC
        
        simplify2_label = Tex("Continue simplifying:").scale(LABEL_SCALE)
        simplify2_equation = MathTex(
            rf"x = \frac{{-{B_VALUE} \pm \sqrt{{{DISCRIMINANT}}}}}{{2}}"
        ).scale(MATH_SCALE)
        
        simplify2_step = VGroup(
            simplify2_label,
            simplify2_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Identify square root part for potential highlighting
        simplify2_sqrt = simplify2_equation[0][6:10]
        
        # ============================================
        # SECTION 8: FINAL ANSWERS
        # ============================================
        # Calculate final values
        from math import sqrt
        SOLUTION1_DECIMAL = (-B_VALUE - sqrt(DISCRIMINANT)) / 2
        SOLUTION2_DECIMAL = (-B_VALUE + sqrt(DISCRIMINANT)) / 2
        
        # Answer 1
        answer1_label = Tex("Solve for $x$:").scale(LABEL_SCALE)
        answer1_exact = MathTex(rf"x = \frac{{-{B_VALUE} - \sqrt{{{DISCRIMINANT}}}}}{{2}}").scale(MATH_SCALE)
        answer1_decimal = self.create_rect_group(
            MathTex(rf"x \approx {SOLUTION1_DECIMAL:.2f}").scale(MATH_SCALE),
            buff=0.15
        )
        answer1_group = VGroup(
            answer1_label,
            answer1_exact,
            answer1_decimal
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Answer 2
        answer2_label = Tex("Solve for $x$:").scale(LABEL_SCALE)
        answer2_exact = MathTex(rf"x = \frac{{-{B_VALUE} + \sqrt{{{DISCRIMINANT}}}}}{{2}}").scale(MATH_SCALE)
        answer2_decimal = self.create_rect_group(
            MathTex(rf"x \approx {SOLUTION2_DECIMAL:.2f}").scale(MATH_SCALE),
            buff=0.15
        )
        answer2_group = VGroup(
            answer2_label,
            answer2_exact,
            answer2_decimal
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Group answers side by side - Updated positioning to match 02a
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
            identify_step,
            coefficient_display,
            show_formula_step,
            substitute_step,
            simplify1_step,
            simplify2_step
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sol_steps.next_to(question_text, DOWN, buff=0.2).align_to(question_text, LEFT)
        
        # ============================================
        # CREATE SCROLL ELEMENTS
        # ============================================
        # Define sections with clear comments
        sol_steps_elements = VGroup(
            # === IDENTIFY COEFFICIENTS SECTION (8 elements total) ===
            *identify_step,                    # 2 elements: label + equation
            *coefficient_labels.values(),      # 3 elements: a=, b=, c=
            *coefficient_values.values(),      # 3 elements: 1, 11, 20
            
            # === SHOW FORMULA SECTION (2 elements) ===
            *show_formula_step,                # 2 elements: label + formula
            
            # === SUBSTITUTE SECTION (7 elements) ===
            *substitute_step,                  # 2 elements: label + equation
            *visible_copies,                   # 5 elements: substituted values
            
            # === SIMPLIFICATION SECTION (4 elements) ===
            *simplify1_step,                   # 2 elements: label + equation
            *simplify2_step,                   # 2 elements: label + equation
        )
        
        scroll = ScrollManager(sol_steps_elements, scene=self)
        
        # ============================================
        # QUICK TIPS
        # ============================================
        
        tip_1 = QuickTip(r"The \textbf{quadratic formula} is faster than completing the square in many cases")
        tip_1.to_corner(DL)
        
        # ============================================
        # ANIMATION SEQUENCE
        # ============================================
        
        # === INTRO: Show question and formulas ===
        with self.voiceover(
            text=f"""Let's solve this quadratic equation using the quadratic formula. 
            We have x squared plus {B_VALUE}x plus {C_VALUE} equals 0."""
        ) as tracker:
            self.play(Write(question_text, run_time=4))
        
        self.wait(1)
        
        with self.voiceover(
            text="""Notice that this equation is already in standard form,
            where a, b, and c are coefficients."""
        ) as tracker:
            self.play(FadeIn(quadratic_form_bg, run_time=1))
            self.play(Write(quadratic_form_group, run_time=3))
        
        self.wait(1)
        
        with self.voiceover(
            text="""We'll use the quadratic formula to find the values of x."""
        ) as tracker:
            self.play(FadeIn(quadratic_formula_bg, run_time=1))
            self.play(Write(quadratic_formula_group, run_time=3))
        
        self.wait(1)
        
        # === STEP 1: Identify coefficients ===
        with self.voiceover(text="Let's identify the coefficients in our equation.") as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            scroll.prepare_next(run_time=2)  # Show equation
            scroll.prepare_next(steps=3, run_time=3)  # Show coefficient display
        
        # Animate coefficient a
        with self.voiceover(text=f"The coefficient of x squared is {A_VALUE}.") as tracker:
            self.play(self.indicate(quadratic_form_coefficients['a'], run_time=2))
            scroll.fade_in_from_target(
                coefficient_values_in_equation['a_value'], 
                coefficient_values['a_value'], 
                run_time=1.5
            )
        
        # Animate coefficient b
        with self.voiceover(text=f"The coefficient of x is {B_VALUE}.") as tracker:
            self.play(self.indicate(quadratic_form_coefficients['b'], run_time=2))
            scroll.fade_in_from_target(
                coefficient_values_in_equation['b_value'], 
                coefficient_values['b_value'], 
                run_time=1.5
            )
        
        # Animate coefficient c
        with self.voiceover(text=f"And the constant term is {C_VALUE}.") as tracker:
            self.play(self.indicate(quadratic_form_coefficients['c'], run_time=2))
            scroll.fade_in_from_target(
                coefficient_values_in_equation['c_value'], 
                coefficient_values['c_value'], 
                run_time=1.5
            )
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)  # Scroll past 1 element
        
        # === STEP 2: Show quadratic formula ===
        with self.voiceover(text="Now we'll apply the quadratic formula.") as tracker:
            self.play(FadeIn(tip_1, shift=UP))
            scroll.prepare_next(run_time=2)  # Show label
            self.play(self.indicate(quadratic_formula_group, scale_factor=1.2, run_time=3))
            
        self.wait(2)
        self.play(FadeOut(tip_1, shift=DOWN))
        
        with self.voiceover(text="Here's the formula with our color-coded coefficients.") as tracker:
            scroll.prepare_next(run_time=4)  # Show formula
        
        self.wait(1)
        
        # === STEP 3: Substitute values ===
        with self.voiceover(text="Let's substitute our values into the formula.") as tracker:
            scroll.prepare_next(run_time=2)  # Show label
            scroll.prepare_next(run_time=4)  # Show substituted formula
        
        # Animate b substitution
        with self.voiceover(text=f"We replace b with {B_VALUE}, appearing twice in the formula.") as tracker:
            self.play(self.indicate(coefficient_values['b_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac, run_time=1.5)
            scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt, run_time=1.5)
        
        # Animate a in 4ac
        with self.voiceover(text=f"We replace a with {A_VALUE} in the 4ac term.") as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac, run_time=1.5)
        
        # Animate c
        with self.voiceover(text=f"C with {C_VALUE}.") as tracker:
            self.play(self.indicate(coefficient_values['c_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac, run_time=1.5)
        
        # Animate a in denominator
        with self.voiceover(text=f"And a with {A_VALUE} again in the denominator.") as tracker:
            self.play(self.indicate(coefficient_values['a_value'], color=None, run_time=2))
            scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom, run_time=1.5)
        
        self.wait(1)
        scroll.scroll_down(steps=1, run_time=1)

        # === STEP 4: First simplification ===
        with self.voiceover(text="Now let's simplify.") as tracker:
            scroll.prepare_next(run_time=2)  # Show label
        
        with self.voiceover(
            text=f"""Negative {B_VALUE} remains negative {B_VALUE}. 
            {B_VALUE} squared is {B_SQUARED}. 
            4. times. {A_VALUE} times {C_VALUE} is {FOUR_AC}. 
            And 2 times {A_VALUE} is {TWO_A}."""
        ) as tracker:
            scroll.transform_from_copy(substitute_equation, simplify1_equation, run_time=2)
        
        # Fade out formula boxes like in 02a
        self.play(
            FadeOut(
                quadratic_group,
                quadratic_formula_bg,
                quadratic_form_bg
            )
        )
        
        self.wait(1)
        scroll.scroll_down(steps=7, run_time=1)
        
        # === STEP 5: Final simplification ===
        with self.voiceover(text="Continuing to simplify.") as tracker:
            scroll.prepare_next(run_time=2)  # Show label
        
        with self.voiceover(text=f"{B_SQUARED} minus {FOUR_AC} equals {DISCRIMINANT}.") as tracker:
            scroll.transform_from_copy(simplify1_equation, simplify2_equation, run_time=2)
        
        self.wait(1)
        
        # Note about prime discriminant (merged from 02a)
        if DISCRIMINANT in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            with self.voiceover(
                text=f"Notice that {DISCRIMINANT} is a prime number, "
                     "so we cannot simplify the square root further."
            ) as tracker:
                self.play(self.indicate(simplify2_sqrt, run_time=2))
        
        self.wait(2)
        
        # === STEP 6: Show final answers ===
        with self.voiceover(text="This gives us two solutions.") as tracker:
            self.play(
                Write(answer1_label, run_time=2),
                Write(answer2_label, run_time=2)
            )
        
        with self.voiceover(
            text=f"For the first solution, we subtract: "
                 f"negative {B_VALUE} minus square root of {DISCRIMINANT}, all divided by 2."
        ) as tracker:
            self.play(
                TransformFromCopy(simplify2_equation, answer1_exact, run_time=2),
                TransformFromCopy(simplify2_equation, answer2_exact, run_time=2)
            )
        
        with self.voiceover(text=f"Which equals approximately {SOLUTION1_DECIMAL:.2f}.") as tracker:
            self.play(Write(answer1_decimal, run_time=2))
        
        with self.voiceover(
            text=f"For the second solution, we add: "
                 f"negative {B_VALUE} plus square root of {DISCRIMINANT}, divided by 2. "
                 f"Which equals approximately {SOLUTION2_DECIMAL:.2f}."
        ) as tracker:
            self.play(Write(answer2_decimal, run_time=2))
        
        with self.voiceover(text="And those are our two solutions!") as tracker:
            self.wait(1)
        
        self.wait(3)