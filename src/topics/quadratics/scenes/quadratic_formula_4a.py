"""Simplified approach for quadratic formula substitution animation."""

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
        LEFT_EDGE_BUFF = 0.5  # Buffer from left edge of screen
        
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
        
        # Group the formulas and position at the top right
        formula_group = VGroup(standard_form, quadratic_formula).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        formula_group.to_edge(UP, buff=0.2).to_edge(RIGHT, buff=0.5)
        
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
        
        # Example equation - positioned at top left
        equation = MathTex(equation_str).scale(TEX_SCALE)
        equation.to_edge(UP, buff=0.2).to_edge(LEFT, buff=LEFT_EDGE_BUFF)
        
        # Coefficient labels - left aligned under equation
        a_label = MathTex(f"a = {a}", color=A_COLOR).scale(STEP_SCALE)
        a_label.next_to(equation, DOWN, buff=0.3).align_to(equation, LEFT)
        
        b_label = MathTex(f"b = {b}", color=B_COLOR).scale(STEP_SCALE)
        b_label.next_to(a_label, RIGHT, buff=0.8)
        
        c_label = MathTex(f"c = {c}", color=C_COLOR).scale(STEP_SCALE)
        c_label.next_to(b_label, RIGHT, buff=0.8)
        
        coeff_labels = VGroup(a_label, b_label, c_label)
        
        # Create containers for left and right columns
        left_column = VGroup()
        right_column = VGroup()
        
        # Step 1: Substitution
        step1_title = Tex("Step 1: Substituting Values").scale(STEP_SCALE)
        step1_title.align_to(equation, LEFT)
        
        # Create a formula with variables that will be replaced step by step
        # We'll create separate formula stages to facilitate the animation
        
        # Original formula with variables
        formula_stage1 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(STEP_SCALE)
        self.apply_smart_colorize(
            [formula_stage1],
            {
                "x": X_COLOR,
                "a": A_COLOR,
                "b": B_COLOR,
                "c": C_COLOR
            }
        )
        
        # Formula with b substituted
        formula_stage2 = MathTex(r"x = \frac{-(-8) \pm \sqrt{(-8)^2 - 4ac}}{2a}").scale(STEP_SCALE)
        self.apply_smart_colorize(
            [formula_stage2],
            {
                "x": X_COLOR,
                "a": A_COLOR,
                "c": C_COLOR,
                "-8": B_COLOR
            }
        )
        
        # Formula with b and a substituted
        formula_stage3 = MathTex(r"x = \frac{-(-8) \pm \sqrt{(-8)^2 - 4(8)c}}{2(8)}").scale(STEP_SCALE)
        self.apply_smart_colorize(
            [formula_stage3],
            {
                "x": X_COLOR,
                "8": A_COLOR,
                "-8": B_COLOR,
                "c": C_COLOR
            }
        )
        
        # Formula with all values substituted
        formula_stage4 = MathTex(r"x = \frac{-(-8) \pm \sqrt{(-8)^2 - 4(8)(-3)}}{2(8)}").scale(STEP_SCALE)
        self.apply_smart_colorize(
            [formula_stage4],
            {
                "x": X_COLOR,
                "8": A_COLOR,
                "-8": B_COLOR,
                "-3": C_COLOR
            }
        )
        
        # Position all stages at the same position
        for stage in [formula_stage1, formula_stage2, formula_stage3, formula_stage4]:
            stage.next_to(step1_title, DOWN, aligned_edge=LEFT, buff=0.2)
        
        step1_group = VGroup(step1_title, formula_stage1)
        left_column.add(step1_group)
        
        # Step 2: Simplifying expression
        step2_title = Tex("Step 2: Simplifying the Expression").scale(STEP_SCALE)
        step2_title.align_to(step1_title, LEFT)
        
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
        left_column.add(step2_group)
        
        # Step 3: Calculate discriminant
        step3_title = Tex("Step 3: Calculating the Discriminant").scale(STEP_SCALE)
        step3_title.align_to(step1_title, LEFT)
        
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
        left_column.add(step3_group)
        
        # Step 4: Simplify the square root if possible
        next_step_ref = discriminant_expr
        
        if factor != 1:  # If we can factor out something
            step4_title = Tex("Step 4: Simplifying the Square Root").scale(STEP_SCALE)
            step4_title.align_to(step1_title, LEFT)
            
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
            left_column.add(step4_group)
            next_step_ref = factored_expr
        
        # Step 5: Simplify the fraction if possible
        if gcd_term > 1:
            step5_title = Tex("Step 5: Simplifying the Fraction").scale(STEP_SCALE)
            step5_title.align_to(step1_title, LEFT)
            
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
            left_column.add(step5_group)
            final_expr = simplified_fraction
        else:
            final_expr = next_step_ref
        
        # Arrange left column vertically
        left_column.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        left_column.next_to(coeff_labels, DOWN, buff=0.4).align_to(equation, LEFT)
        
        # Final solutions - right column
        solutions_title = Tex("Final Solutions").scale(STEP_SCALE)
        
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
        
        # Arrange the solutions vertically
        solution1_group = VGroup(solution1_exact, solution1_decimal)
        solution1_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        solution2_group = VGroup(solution2_exact, solution2_decimal)
        solution2_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Add solutions to right column
        right_column.add(solutions_title)
        right_column.add(solution1_group)
        right_column.add(solution2_group)
        
        # Arrange right column
        right_column.arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        
        # Position right column exactly 2 units from left column
        right_column.next_to(left_column, RIGHT, buff=2.0)
        right_column.align_to(left_column, UP)
        
        # Create surrounding boxes for the decimal solutions
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
        
        # Add a tip at the bottom
        tip_final = QuickTip(
            "We can verify our solutions by substituting back into the original equation."
        )
        tip_final.next_to(solution2_group, DOWN, buff=0.5)
        
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
            self.play(Write(formula_stage1))
            
            # Extract the coefficient values for animation
            a_val = MathTex(str(a), color=A_COLOR).scale(STEP_SCALE)
            b_val = MathTex(str(b), color=B_COLOR).scale(STEP_SCALE)
            c_val = MathTex(str(c), color=C_COLOR).scale(STEP_SCALE)
            
            # Position values over their labels
            a_val.move_to(a_label[0][-1])
            b_val.move_to(b_label[0][-1])
            c_val.move_to(c_label[0][-1])
            
            # Show the coefficient values
            self.play(
                FadeIn(a_val),
                FadeIn(b_val),
                FadeIn(c_val)
            )
            
            # Substitute b first
            self.play(
                b_val.animate.next_to(formula_stage1, UP),
                run_time=0.8
            )
            self.play(
                ReplacementTransform(formula_stage1, formula_stage2),
                b_val.animate.scale(0),
                run_time=1
            )
            
            # Substitute a next
            self.play(
                a_val.animate.next_to(formula_stage2, UP),
                run_time=0.8
            )
            self.play(
                ReplacementTransform(formula_stage2, formula_stage3),
                a_val.animate.scale(0),
                run_time=1
            )
            
            # Substitute c last
            self.play(
                c_val.animate.next_to(formula_stage3, UP),
                run_time=0.8
            )
            self.play(
                ReplacementTransform(formula_stage3, formula_stage4),
                c_val.animate.scale(0),
                run_time=1
            )
        
        # Simplify the expression
        with self.voiceover(f"First, we calculate the value inside the square root. ({b})² equals {b_squared}, and 4({a})({c}) equals {four_ac}."):
            self.play(Write(step2_title))
            self.play(Write(simplified))
        
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
            self.play(Write(solution1_decimal))
            self.play(Create(sol1_box))
        
        with self.voiceover(f"Using the minus sign, we get the second solution, x approximately equals {solution2_rounded}."):
            self.play(Write(solution2_exact))
            self.play(Write(solution2_decimal))
            self.play(Create(sol2_box))
        
        # Final tip
        with self.voiceover("These are our two solutions to the quadratic equation. We can verify them by substituting back into the original equation."):
            self.play(FadeIn(tip_final))
            self.wait(COMPREHENSION_TIME)
            self.play(FadeOut(tip_final))