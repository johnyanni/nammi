"""Simple template for solving quadratic equations using the quadratic formula."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.smart_tex import SmartColorizeStatic, search_shape_in_text
import math


class QuadraticFormula3a(MathTutorialScene):
    """A scene that demonstrates solving a quadratic equation using the quadratic formula."""
    
    def construct(self):
        # Define colors for consistent use
        A_COLOR = "#4ec9b0"  # Teal
        B_COLOR = "#ff79c6"  # Pink
        C_COLOR = "#00bfff"  # Light blue
        X_COLOR = "#ffb86c"  # Orange
        HIGHLIGHT_COLOR = "#9A48D0"  # Purple
        
        # Define the equation parameters
        a, b, c = 8, -8, -3
        equation_str = "8x^2 - 8x - 3 = 0"
        
        # Define animation durations
        STANDARD_TIME = 1.0
        QUICK_TIME = 0.5
        COMPREHENSION_TIME = 2.0
        
        # Define scaling and spacing
        TEX_SCALE = 0.7
        STEP_SCALE = 0.6  # Slightly smaller for steps to fit everything
        TIP_SHIFT = RIGHT * 5  # Position tips on the right side
        
        # Helper methods for calculations
        def get_simplified_sqrt(n):
            """Factor a square root into perfect square * remaining."""
            factor = 1
            i = 1
            while i * i <= n:
                if n % (i * i) == 0:
                    factor = i
                i += 1
            
            remaining = n // (factor * factor)
            return (factor, remaining)
        
        def get_gcd(*args):
            """Find the greatest common divisor of multiple numbers."""
            from math import gcd
            from functools import reduce
            
            # Filter out zeros and take absolute values
            numbers = [abs(n) for n in args if n != 0]
            
            if not numbers:
                return 1
            
            # Use reduce to apply gcd to multiple numbers
            return reduce(gcd, numbers)
        
        # Pre-calculate all the values we'll need throughout the scene
        b_squared = b * b
        four_ac = 4 * a * c
        discriminant = b_squared - four_ac
        first_term = -b
        denominator = 2 * a
        
        sqrt_discriminant = get_simplified_sqrt(discriminant)
        factor, remaining = sqrt_discriminant
        
        gcd_term = get_gcd(first_term, factor, denominator)
        simple_first = first_term // gcd_term
        simple_factor = factor // gcd_term if factor > 0 else 0
        simple_denom = denominator // gcd_term
        
        solution1_approx = (first_term + factor * math.sqrt(remaining)) / denominator
        solution1_rounded = round(solution1_approx, 3)
        
        solution2_approx = (first_term - factor * math.sqrt(remaining)) / denominator
        solution2_rounded = round(solution2_approx, 3)
        
        # Create all the expressions we'll need
        
        # Top formulas
        standard_form = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        self.apply_smart_colorize(
            [standard_form],
            {
                "a": A_COLOR,
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "2": X_COLOR
            }
        )
        
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        self.apply_smart_colorize(
            [quadratic_formula],
            {
                "x": X_COLOR,
                "a": A_COLOR,
                "b": B_COLOR,
                "c": C_COLOR
            }
        )
        
        # Group the formulas and position at the top
        formula_group = VGroup(standard_form, quadratic_formula).arrange(RIGHT, buff=2.0)
        formula_group.to_edge(UP, buff=0.2)  # Move higher to make more space
        
        # Add backgrounds to formulas
        standard_bg = SurroundingRectangle(
            standard_form, 
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.1,
            stroke_width=2,
            buff=0.3,
            corner_radius=0.2
        )
        
        formula_bg = SurroundingRectangle(
            quadratic_formula, 
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.1,
            stroke_width=2,
            buff=0.3,
            corner_radius=0.2
        )
        
        # Example equation
        equation = MathTex(equation_str).scale(TEX_SCALE)
        equation.next_to(formula_group, DOWN, buff=0.4)  # Reduce buffer
        
        # Create a smaller buffer for step spacing
        STEP_BUFF = 0.3
        
        # Coefficient labels
        a_label = MathTex(f"a = {a}", color=A_COLOR).scale(STEP_SCALE)
        a_label.next_to(equation, DOWN, buff=0.3).align_to(equation, LEFT)
        
        b_label = MathTex(f"b = {b}", color=B_COLOR).scale(STEP_SCALE)
        b_label.next_to(a_label, RIGHT, buff=0.8)
        
        c_label = MathTex(f"c = {c}", color=C_COLOR).scale(STEP_SCALE)
        c_label.next_to(b_label, RIGHT, buff=0.8)
        
        coeff_labels = VGroup(a_label, b_label, c_label)
        
        # Create container for all solution steps
        solution_steps = VGroup()
        
        # Step 1: Substitution
        step1_title = Tex("Step 1: Substituting Values").scale(STEP_SCALE)
        step1_title.next_to(coeff_labels, DOWN, buff=STEP_BUFF).align_to(equation, LEFT)
        
        substitution = MathTex(
            f"x = \\frac{{-({b}) \\pm \\sqrt{{({b})^2 - 4({a})({c})}}}}{{2({a})}}"
        ).scale(STEP_SCALE)
        substitution.next_to(step1_title, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Color parts of substitution
        self.apply_smart_colorize(
            [substitution],
            {
                "x": X_COLOR,
                f"{a}": A_COLOR,
                f"{b}": B_COLOR,
                f"{c}": C_COLOR
            }
        )
        
        step1_group = VGroup(step1_title, substitution)
        solution_steps.add(step1_group)
        
        # Step 2: Simplifying expression
        step2_title = Tex("Step 2: Simplifying the Expression").scale(STEP_SCALE)
        step2_title.next_to(substitution, DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        
        op_sign = "+" if four_ac < 0 else "-"
        simplified = MathTex(
            f"x = \\frac{{{first_term} \\pm \\sqrt{{{b_squared} {op_sign} {abs(four_ac)}}}}}{{{denominator}}}"
        ).scale(STEP_SCALE)
        simplified.next_to(step2_title, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # No need to color code the numbers here
        self.apply_smart_colorize(
            [simplified],
            {
                "x": X_COLOR
            }
        )
        
        step2_group = VGroup(step2_title, simplified)
        solution_steps.add(step2_group)
        
        # Step 3: Calculate discriminant
        step3_title = Tex("Step 3: Calculating the Discriminant").scale(STEP_SCALE)
        step3_title.next_to(simplified, DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        
        discriminant_expr = MathTex(
            f"x = \\frac{{{first_term} \\pm \\sqrt{{{discriminant}}}}}{{{denominator}}}"
        ).scale(STEP_SCALE)
        discriminant_expr.next_to(step3_title, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.apply_smart_colorize(
            [discriminant_expr],
            {
                "x": X_COLOR
            }
        )
        
        step3_group = VGroup(step3_title, discriminant_expr)
        solution_steps.add(step3_group)
        
        # Step 4: Simplify the square root if possible
        next_step_ref = discriminant_expr
        
        if factor != 1:  # If we can factor out something
            step4_title = Tex("Step 4: Simplifying the Square Root").scale(STEP_SCALE)
            step4_title.next_to(discriminant_expr, DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
            
            factored_expr = MathTex(
                f"x = \\frac{{{first_term} \\pm {factor}\\sqrt{{{remaining}}}}}{{{denominator}}}"
            ).scale(STEP_SCALE)
            factored_expr.next_to(step4_title, DOWN, aligned_edge=LEFT, buff=0.2)
            
            self.apply_smart_colorize(
                [factored_expr],
                {
                    "x": X_COLOR
                }
            )
            
            step4_group = VGroup(step4_title, factored_expr)
            solution_steps.add(step4_group)
            next_step_ref = factored_expr
        
        # Step 5: Simplify the fraction if possible
        if gcd_term > 1:
            step5_title = Tex("Step 5: Simplifying the Fraction").scale(STEP_SCALE)
            step5_title.next_to(next_step_ref, DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
            
            factor_str = f"{simple_factor}" if simple_factor > 1 else ""
            simplified_fraction = MathTex(
                f"x = \\frac{{{simple_first} \\pm {factor_str}\\sqrt{{{remaining}}}}}{{{simple_denom}}}"
            ).scale(STEP_SCALE)
            simplified_fraction.next_to(step5_title, DOWN, aligned_edge=LEFT, buff=0.2)
            
            self.apply_smart_colorize(
                [simplified_fraction],
                {
                    "x": X_COLOR
                }
            )
            
            step5_group = VGroup(step5_title, simplified_fraction)
            solution_steps.add(step5_group)
            final_expr = simplified_fraction
        else:
            final_expr = next_step_ref
        
        # Final solutions
        solutions_title = Tex("Final Solutions").scale(STEP_SCALE)
        solutions_title.next_to(final_expr, DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        
        # First solution (with plus)
        factor_str = f"{simple_factor}" if simple_factor > 1 else ""
        solution1_exact = MathTex(
            f"x = \\frac{{{simple_first} + {factor_str}\\sqrt{{{remaining}}}}}{{{simple_denom}}}"
        ).scale(STEP_SCALE)
        solution1_decimal = MathTex(f"x \\approx {solution1_rounded}").scale(STEP_SCALE)
        
        # Second solution (with minus)
        solution2_exact = MathTex(
            f"x = \\frac{{{simple_first} - {factor_str}\\sqrt{{{remaining}}}}}{{{simple_denom}}}"
        ).scale(STEP_SCALE)
        solution2_decimal = MathTex(f"x \\approx {solution2_rounded}").scale(STEP_SCALE)
        
        # Arrange solutions in a 2x2 grid for compactness
        solution_grid = VGroup(
            solution1_exact, solution1_decimal,
            solution2_exact, solution2_decimal
        ).arrange_in_grid(rows=2, cols=2, buff=0.4)
        solution_grid.next_to(solutions_title, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Only color the x and highlight the final answers
        self.apply_smart_colorize(
            [solution1_exact, solution2_exact],
            {
                "x": X_COLOR
            }
        )
        
        # Highlight the decimal approximations
        solution1_decimal[0][-len(str(solution1_rounded)):].set_color(HIGHLIGHT_COLOR)
        solution2_decimal[0][-len(str(solution2_rounded)):].set_color(HIGHLIGHT_COLOR)
        
        # Add final solutions to solution steps
        final_solutions_group = VGroup(solutions_title, solution_grid)
        solution_steps.add(final_solutions_group)
        
        # Arrange all steps in a vertical group with proper spacing
        solution_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        solution_steps.move_to(DOWN * 0.5)  # Center in the vertical space below equation
        
        # Add rectangles around the decimal solutions
        sol1_box = SurroundingRectangle(
            solution1_decimal, 
            color=HIGHLIGHT_COLOR,
            corner_radius=0.2,
            buff=0.1
        )
        
        sol2_box = SurroundingRectangle(
            solution2_decimal, 
            color=HIGHLIGHT_COLOR,
            corner_radius=0.2,
            buff=0.1
        )
        
        # Tips
        tip1 = QuickTip(
            "The ± symbol means we'll get two solutions: one with + and one with -"
        )
        tip1.shift(TIP_SHIFT)
        
        tip2 = None
        if b < 0:
            tip2 = QuickTip(
                f"When we apply the negative of a negative number (-({b})), we get a positive result: {first_term}"
            )
            tip2.shift(TIP_SHIFT)
        
        tip_final = QuickTip(
            "We can verify our solutions by substituting back into the original equation."
        )
        tip_final.shift(TIP_SHIFT)
        
        # Animation sequence with voiceovers
        
        # Start with the top formulas
        with self.voiceover("Let's solve this quadratic equation using the quadratic formula."):
            self.play(
                FadeIn(standard_form, standard_bg),
                FadeIn(quadratic_formula, formula_bg)
            )
            self.play(FadeIn(equation))
            self.play(Indicate(equation, color=HIGHLIGHT_COLOR))
            
        # Identify the coefficients
        with self.voiceover(f"First, we identify the coefficients. a equals {a}"):
            # Use search_shape_in_text to find and color 'a' in the equation
            a_index = search_shape_in_text(equation, MathTex("8"))[0]
            self.play(
                equation[0][a_index].animate.set_color(A_COLOR),
                FadeIn(a_label)
            )
        
        with self.voiceover(f"b equals {b}"):
            # Find the minus sign and 8 for coefficient b
            minus_index = search_shape_in_text(equation, MathTex("-"))[0]
            b_val_index = search_shape_in_text(equation, MathTex("8"))[1]  # Second 8
            b_term = VGroup(equation[0][minus_index], equation[0][b_val_index])
            
            self.play(
                b_term.animate.set_color(B_COLOR),
                FadeIn(b_label)
            )
        
        with self.voiceover(f"And c equals {c}"):
            # Find the second minus sign and 3 for coefficient c
            minus_index = search_shape_in_text(equation, MathTex("-"))[1]  # Second minus
            c_val_index = search_shape_in_text(equation, MathTex("3"))[0]
            c_term = VGroup(equation[0][minus_index], equation[0][c_val_index])
            
            self.play(
                c_term.animate.set_color(C_COLOR),
                FadeIn(c_label)
            )
        
        # Substitute values into formula
        with self.voiceover("Now that we've identified the coefficients, let's substitute them into the quadratic formula."):
            self.play(Indicate(
                quadratic_formula, 
                color=HIGHLIGHT_COLOR, 
                scale_factor=1.1
            ))
            self.wait(QUICK_TIME)
            
            self.play(Write(step1_title))
            self.play(Write(substitution))
            self.play(FadeIn(tip1))
            self.wait(STANDARD_TIME)
            self.play(FadeOut(tip1))
        
        # Simplify the expression
        with self.voiceover(f"First, we calculate the value inside the square root. ({b})² equals {b_squared}, and 4({a})({c}) equals {four_ac}."):
            self.play(Write(step2_title))
            self.play(Write(simplified))
            
            if tip2:
                self.play(FadeIn(tip2))
                self.wait(STANDARD_TIME)
                self.play(FadeOut(tip2))
        
        # Calculate the discriminant
        with self.voiceover(f"Adding {b_squared} and {four_ac}, we get {discriminant} under the square root."):
            self.play(Write(step3_title))
            self.play(Write(discriminant_expr))
        
        # Simplify the square root if possible
        if factor != 1:
            with self.voiceover(f"We can simplify the square root of {discriminant} as {factor} times the square root of {remaining}."):
                self.play(Write(step4_title))
                self.play(Write(factored_expr))
        
        # Simplify the fraction if possible
        if gcd_term > 1:
            with self.voiceover(f"We can simplify the fraction by dividing the numerator and denominator by {gcd_term}."):
                self.play(Write(step5_title))
                self.play(Write(simplified_fraction))
        
        # Show the solutions
        with self.voiceover(f"Using the plus sign, we get the first solution, x approximately equals {solution1_rounded}."):
            self.play(Write(solutions_title))
            self.play(Write(solution1_exact))
            self.play(Write(solution1_decimal), Create(sol1_box))
        
        with self.voiceover(f"Using the minus sign, we get the second solution, x approximately equals {solution2_rounded}."):
            self.play(Write(solution2_exact))
            self.play(Write(solution2_decimal), Create(sol2_box))
        
        # Final tip
        with self.voiceover("These are our two solutions to the quadratic equation. We can verify them by substituting back into the original equation."):
            self.play(FadeIn(tip_final))
            self.wait(COMPREHENSION_TIME)
            self.play(FadeOut(tip_final))