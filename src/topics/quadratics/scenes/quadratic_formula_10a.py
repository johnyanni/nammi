from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class QuadraticFormula(MathTutorialScene):
    def construct(self):
        # Constants for scaling
        TEX_SCALE = 0.70

        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Buffers
        WIDE_BUFF = 4.0
        MED_BUFF = 1.0

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        EQUATION_BG_WIDTH = 2
        EQUATION_BG_OPACITY = 0.25
        EQUATION_BG_radius = 0.3

        # Create the generic quadratic equation
        quadratic_equation = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        SmartColorizeStatic(quadratic_equation, {"2": X_COLOR})
        
        # Find the coefficients in the general equation
        quad_a = quadratic_equation[0][0]  # 'a' is typically first character
        quad_b = quadratic_equation[0][4]  # 'b' is typically at position 4
        quad_c = quadratic_equation[0][8]  # 'c' is typically at position 8
        
        # Create the quadratic formula
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        
        # Arrange the quadratic equation and formula
        quadratic_group = Group(
            quadratic_equation,
            quadratic_formula
        ).arrange(buff=WIDE_BUFF).to_edge(UP)
        
        # Apply smart colorization
        self.apply_smart_colorize(
            quadratic_group,
            {
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "a": A_COLOR,
            }
        )
        
        # Create background rectangles
        quadratic_equation_bg = SurroundingRectangle(
            quadratic_equation,
            buff=0.2,
            corner_radius=EQUATION_BG_radius,
            fill_opacity=EQUATION_BG_OPACITY,
            fill_color=EQUATION_BG_FILL,  
            stroke_color=EQUATION_BG_STROKE, 
            stroke_width=EQUATION_BG_WIDTH
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula,
            buff=0.2,
            corner_radius=EQUATION_BG_radius,
            fill_opacity=EQUATION_BG_OPACITY,
            fill_color=EQUATION_BG_FILL,  
            stroke_color=EQUATION_BG_STROKE, 
            stroke_width=EQUATION_BG_WIDTH
        )

        # Example Quadratic Equation
        equation = MathTex("1x^2 + 11x + 20 = 0").scale(TEX_SCALE).next_to(quadratic_group, DOWN)
        SmartColorizeStatic(
            equation,
            {
                "x": X_COLOR,
                "2": X_COLOR,
            }
        )
        
        # Find the values in the example equation
        a_in_equation = equation[0][search_shape_in_text(equation, MathTex("1"))[0]].set_opacity(0)
        b_in_equation = equation[0][search_shape_in_text(equation, MathTex("11"))[0]].set_color(B_COLOR)
        c_in_equation = equation[0][search_shape_in_text(equation, MathTex("20"))[0]].set_color(C_COLOR)
        
        # Create coefficient labels
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        a_value = a[0][search_shape_in_text(a, MathTex("1"))[0]]
        
        b = MathTex("b = 11", color=B_COLOR).scale(TEX_SCALE)
        b_value = b[0][search_shape_in_text(b, MathTex("11"))[0]]
        
        c = MathTex("c = 20", color=C_COLOR).scale(TEX_SCALE)
        c_value = c[0][search_shape_in_text(c, MathTex("20"))[0]]
        
        # Group the coefficients
        coefficients = Group(a, b, c).arrange(buff=MED_BUFF).next_to(equation, DOWN * 2)

        # Step 1: Create with variables (use parentheses for better formatting)
        step_1_with_vars = MathTex(r"x = \frac{-(b) \pm \sqrt{(b)^2 - 4(a)(c)}}{2(a)}").scale(TEX_SCALE)
        
        # Explicitly color the variables
        SmartColorizeStatic(step_1_with_vars, {"a": A_COLOR, "b": B_COLOR, "c": C_COLOR, "x": X_COLOR})
        
        # Prepare the variables
        a_var = MathTex("a", color=A_COLOR).scale(TEX_SCALE)
        b_var = MathTex("b", color=B_COLOR).scale(TEX_SCALE)
        c_var = MathTex("c", color=C_COLOR).scale(TEX_SCALE)
        
        # Find the 'a', 'b', and 'c' parts in the formula
        a_locs = []
        b_locs = []
        c_locs = []
        
        # Find indices using search_shapes_in_text
        a_indices = search_shapes_in_text(step_1_with_vars, [MathTex("a")])
        for idx in a_indices:
            a_locs.append(step_1_with_vars[0][idx])
        
        b_indices = search_shapes_in_text(step_1_with_vars, [MathTex("b")])
        for idx in b_indices:
            b_locs.append(step_1_with_vars[0][idx])
        
        c_indices = search_shapes_in_text(step_1_with_vars, [MathTex("c")])
        for idx in c_indices:
            c_locs.append(step_1_with_vars[0][idx])
            
        # Create the step with label
        sol_step_1 = self.create_labeled_step(
            "Step 1: substitute the coefficients",
            step_1_with_vars
        )
        step_1_label, step_1_exp = sol_step_1
        
        # Step 1 with values - complete version after substitution
        step_1_with_values = MathTex(r"x = \frac{-(11) \pm \sqrt{(11)^2 - 4(1)(20)}}{2(1)}").scale(TEX_SCALE)
        SmartColorizeStatic(
            step_1_with_values,
            {
                "1": A_COLOR,
                "11": B_COLOR,
                "20": C_COLOR,
                "x": X_COLOR,
            }
        )
        step_1_with_values.move_to(step_1_with_vars)
                
        # STEP 2: Simplifying - just create the full equation
        sol_step_2 = self.create_labeled_step(
            "Step 2: simplifying the expression",
            MathTex(r"x = \frac{-11 \pm \sqrt{121 - 80}}{2}").scale(TEX_SCALE)
        )
        step_2_label, step_2_exp = sol_step_2
        
        # Find parts to highlight in step 2
        step_2_121_idx = search_shape_in_text(step_2_exp, MathTex("121"))[0]
        step_2_80_idx = search_shape_in_text(step_2_exp, MathTex("80"))[0]
        step_2_2_indices = search_shape_in_text(step_2_exp, MathTex("2"))
        step_2_2_idx = step_2_2_indices[-1] if step_2_2_indices else 0  # Last occurrence
        
        # STEP 3: Final simplification
        sol_step_3 = self.create_labeled_step(
            "Step 3: simplifying the square root",
            MathTex(r"x = \frac{-11 \pm \sqrt{41}}{2}").scale(TEX_SCALE)
        )
        step_3_label, step_3_exp = sol_step_3
        
        # Find 41 for highlighting in step 3
        step_3_41_idx = search_shape_in_text(step_3_exp, MathTex("41"))[0]
        
        # Apply smart colorization to steps 2 and 3
        self.apply_smart_colorize(
            [step_2_exp, step_3_exp],
            {
                "x": X_COLOR,
                "11": B_COLOR,
                "121": WHITE,
                "41": WHITE,
            }
        )
        
        # Group all solution steps
        solution_steps = Group(
            sol_step_1,
            sol_step_2,
            sol_step_3
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Create solutions
        first_root = MathTex(r"x = \frac{-11 + \sqrt{41}}{2}").scale(TEX_SCALE)
        first_root_dec = MathTex("x = -2.298").scale(TEX_SCALE)
        first_root_group = Group(first_root, first_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_1, UP).to_edge(RIGHT)
        first_root_rec = self.create_surrounding_rectangle(first_root_dec)
        
        second_root = MathTex(r"x = \frac{-11 - \sqrt{41}}{2}").scale(TEX_SCALE)
        second_root_dec = MathTex("x = -8.702").scale(TEX_SCALE)
        second_root_group = Group(second_root, second_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_3, UP).to_edge(RIGHT)
        second_root_rec = self.create_surrounding_rectangle(second_root_dec)

        # Apply coloring to roots
        self.apply_smart_colorize(
            [first_root, first_root_dec, second_root, second_root_dec],
            {
                "x": X_COLOR,
                "11": B_COLOR
            }
        )
        
        # Arrange the full solution
        solution = Group(
            solution_steps,
            Group(
                first_root_group, second_root_group,
                first_root_rec, second_root_rec
            )
        ).arrange(buff=3.5).next_to(coefficients, DOWN * 1.5)

        # Create tips
        tip_1 = QuickTip(r"The \textbf{quadratic formula} is faster than completing the square in many cases")
        tip_2 = QuickTip("Writing the answer in decimal format is not entirely necessary")
        Group(tip_1, tip_2).to_corner(DL)

        # ANIMATION SEQUENCES
        # Introduction
        with self.voiceover(
                text="""
                In this exercise, we are trying to find the solutions to <bookmark mark='equation' /> this quadratic equation using <bookmark mark='formula' /> the quadratic formula.

                The good thing is that our equation is already in <bookmark mark='quadratic' /> the standard quadratic form.
                That means we can easily pick out the values for 'a', 'b', and 'c' and plug them straight into the formula.
                """
        ) as tracker:
            self.play(
                FadeIn(
                    quadratic_group,
                    equation,
                    quadratic_equation_bg,
                    quadratic_formula_bg
                )
            )

            self.wait_until_bookmark("equation")
            self.play(self.indicate(equation))

            self.wait_until_bookmark("formula")
            self.play(self.indicate(quadratic_formula))

            self.wait_until_bookmark("quadratic")
            self.play(self.indicate(quadratic_equation))
            
            self.wait(QUICK_PAUSE)

        # Coefficient identification
        with self.voiceover(
                text="""
                First, let's <bookmark mark='coefficients' /> identify 'ay', 'b', and 'c'.
                'a' is the coefficient <bookmark mark='x_squared' /> of x squared. Here, it's <bookmark mark='a' /> just 1.
                'b' is the coefficient <bookmark mark='x' /> of x. That is <bookmark mark='b' /> just 11.
                And 'c' is the <bookmark mark='constant' /> constant term, which <bookmark mark='c' /> is 20.
                """
        ) as tracker:
            self.wait_until_bookmark("coefficients")
            self.play(
                FadeIn(a[0][:2], b[0][:2], c[0][:2])
            )

            self.wait_until_bookmark("x_squared")
            self.play(self.indicate(quad_a))

            self.wait_until_bookmark("a")
            self.play(FadeIn(a_value, target_position=a_in_equation), run_time=2)

            self.wait_until_bookmark("x")
            self.play(self.indicate(quad_b))

            self.wait_until_bookmark("b")
            self.play(FadeIn(b_value, target_position=b_in_equation), run_time=2)

            self.wait_until_bookmark("constant")
            self.play(self.indicate(quad_c))

            self.wait_until_bookmark("c")
            self.play(FadeIn(c_value, target_position=c_in_equation), run_time=2)

            self.wait(COMPREHENSION_PAUSE)

        # Step 1: Start with formula with variables
        with self.voiceover(
                text="""
                Now, let's substitute these values into the quadratic formula.
                """
        ) as tracker:
            # Show the step 1 label and the formula with variables
            self.play(Write(step_1_label))
            self.play(Write(step_1_exp))

        # Step 1: Substitution of values - alternative approach using Transform+FadeOut
        with self.voiceover(
                text="""
                x equals negative 'b', <bookmark mark='negative_b' /> which is negative 11,
                <bookmark mark='plus_minus' /> plus or minus the square root of 'b' squared,
                <bookmark mark='b_squared' /> so 11 squared,
                <bookmark mark='minus_4' /> minus 4 times 'ay',
                which <bookmark mark='a_1' /> is one, times 'c', <bookmark mark='c' /> which is 20,
                all divided <bookmark mark='two' /> by 2 times 'ay', which <bookmark mark='a_2' /> is one.
                """
        ) as tracker:
            # For negative b part
            self.wait_until_bookmark("negative_b")
            if len(b_locs) > 0:
                # Create a copy of 11 from the value
                b_val_copy = b_value.copy()
                # Position it over the b
                b_val_copy.move_to(b_locs[0])
                # Fade out the b and fade in the 11
                self.play(
                    FadeOut(b_locs[0], scale=0.5),
                    FadeIn(b_val_copy, scale=1.5),
                    run_time=1
                )
                # Replace the b with 11 in our tracking
                b_locs[0] = b_val_copy

            self.wait_until_bookmark("plus_minus")
            # No replacement here
            pass
            
            self.wait_until_bookmark("b_squared")
            # Replace second b with 11
            if len(b_locs) > 1:
                b_val_copy2 = b_value.copy()
                b_val_copy2.move_to(b_locs[1])
                self.play(
                    FadeOut(b_locs[1], scale=0.5),
                    FadeIn(b_val_copy2, scale=1.5),
                    run_time=1
                )
                b_locs[1] = b_val_copy2
            
            self.wait_until_bookmark("minus_4")
            # No replacement here
            pass

            self.wait_until_bookmark("a_1")
            # Replace first a with 1
            if len(a_locs) > 0:
                a_val_copy = a_value.copy()
                a_val_copy.move_to(a_locs[0])
                self.play(
                    FadeOut(a_locs[0], scale=0.5),
                    FadeIn(a_val_copy, scale=1.5),
                    run_time=1
                )
                a_locs[0] = a_val_copy

            self.wait_until_bookmark("c")
            # Replace c with 20
            if len(c_locs) > 0:
                c_val_copy = c_value.copy()
                c_val_copy.move_to(c_locs[0])
                self.play(
                    FadeOut(c_locs[0], scale=0.5),
                    FadeIn(c_val_copy, scale=1.5),
                    run_time=1
                )
                c_locs[0] = c_val_copy

            self.wait_until_bookmark("two")
            # No replacement here
            pass

            self.wait_until_bookmark("a_2")
            # Replace second a with 1
            if len(a_locs) > 1:
                a_val_copy2 = a_value.copy()
                a_val_copy2.move_to(a_locs[1])
                self.play(
                    FadeOut(a_locs[1], scale=0.5),
                    FadeIn(a_val_copy2, scale=1.5),
                    run_time=1
                )
                a_locs[1] = a_val_copy2
            
            # After all individual replacements, transition to the clean version
            self.play(
                ReplacementTransform(step_1_exp, step_1_with_values),
                run_time=1
            )
            
            # Update our reference for the next steps
            step_1_exp = step_1_with_values
            
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        # Step 2: Simplifying
        with self.voiceover(
                text="""
                Next, we simplify step by step: 11 squared <bookmark mark='b_squared' /> equals 121.
                negative 4 times 1 times 20 <bookmark mark='four_ac' /> equals negative 80.
                Finally, 2 times 1 <bookmark mark='den' /> equals 2. 
                """
        ) as tracker:
            self.play(Write(step_2_label))
            
            # Write the full equation
            self.play(FadeIn(step_2_exp))
            
            # Highlight specific parts
            self.wait_until_bookmark("b_squared")
            self.play(Indicate(step_2_exp[0][step_2_121_idx]))
                
            self.wait_until_bookmark("four_ac")
            self.play(Indicate(step_2_exp[0][step_2_80_idx]))
            
            self.wait_until_bookmark("den")
            self.play(Indicate(step_2_exp[0][step_2_2_idx]))

            self.wait(COMPREHENSION_PAUSE)
            
        # Step 3: Final simplification
        with self.voiceover(
                text="""
                And finally, 121 minus 80 <bookmark mark='equation' /> gives us 41.
                """
        ) as tracker:
            self.play(Write(step_3_label))
            
            # Write the full equation
            self.play(FadeIn(step_3_exp))
            
            # Highlight the 41
            self.wait_until_bookmark("equation")
            self.play(Indicate(step_3_exp[0][step_3_41_idx]))

            self.wait(COMPREHENSION_PAUSE)

        # Solution forms
        with self.voiceover(
                text="""
                Since we can't simplify the square root of 41 further, we'll keep it exact.
                But we'll write both solutions;
                one <bookmark mark='roots' /> with a plus and one with a minus.
                """
        ) as tracker:
            self.wait_until_bookmark("roots")
            self.play(
                ReplacementTransform(step_3_exp[0].copy(), first_root[0]),
                ReplacementTransform(step_3_exp[0].copy(), second_root[0]),
                run_time=2
            )
            self.wait(STANDARD_PAUSE)

        # Decimal approximations
        with self.voiceover(
                text="""
                Finally, if we want decimal approximations: the first solution, with the plus, is <bookmark mark='root_1' /> about -2.298.

                The second solution, using the minus, is <bookmark mark='root_2' /> about -8.702.
                """
        ) as tracker:
            self.wait_until_bookmark("root_1")
            self.play(Write(first_root_dec))
            self.play(FadeIn(tip_2, shift=UP))

            self.wait_until_bookmark("root_2")
            self.play(Write(second_root_dec))
            self.wait(QUICK_PAUSE)
        self.play(FadeOut(tip_2, shift=DOWN))
            
        # Conclusion
        with self.voiceover(
                text="""
                So these are the actual solutions using the quadratic formula.
                """
        ) as tracker:
            self.play(Create(first_root_rec), Create(second_root_rec), run_time=2)
            
        self.wait(5)