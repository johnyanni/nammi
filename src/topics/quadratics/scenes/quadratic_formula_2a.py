from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class QuadraticFormula2a(MathTutorialScene):

    def create_surrounding_rectangle(
            self,
            mobject,
            color="#9A48D0",
            corner_radius=0.1, buff=0.1
    ):
        return SurroundingRectangle(mobject, color=color, corner_radius=corner_radius, buff=buff)
        
    def create_labeled_step(
            self,
            label_text,
            expressions,
            color_map=None,
            label_color=GREY,
            label_scale=0.5,
            label_buff=0.2,
    ):
        label = Tex(label_text, color=label_color).scale(label_scale)
        exp_group = expressions
            
        if color_map:
            self.apply_smart_colorize(exp_group, color_map)
            
        return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)
    
    
    def construct(self):

        # Constants for scaling
        TEX_SCALE = 0.70

        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"
    
        # Indicate Animation
        INDICATION_COLOR = "#9A48D0"
        INDICATION_TIME = 2.0

        # Buffers
        WIDE_BUFF = 4.0
        MED_BUFF = 1.0

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        EQUATION_BG_WIDTH = 2
        EQUATION_BG_OPACITY = 0.25
        EQUATION_BG_radius = 0.3

        # Constants for timing
        QUICK_PAUSE = 0.5
        STANDARD_PAUSE = 1.0
        COMPREHENSION_PAUSE = 2.0

                        
        quadratic_equation = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        SmartColorizeStatic(quadratic_equation, {"2": X_COLOR})
        
        quadratic_equation_coefficients = Group(
            *[
                quadratic_equation[0][i] for i in [0, 3, 6]  # Indices of a, b, c
            ]
        )
                
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        quadratic_group = Group(
            quadratic_equation,
            quadratic_formula,
        ).arrange(buff=WIDE_BUFF).to_edge(UP)
        self.apply_smart_colorize(
            quadratic_group,
            {
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "a": A_COLOR,
            }
        )
        
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
        equation = MathTex("8x^2 - 8x - 3 = 0").scale(TEX_SCALE).next_to(quadratic_group, DOWN)
        SmartColorizeStatic(
            equation,
            {
                "x": X_COLOR,
                "2": X_COLOR,
            }
        )
        
        # Directly color coefficients based on reliable positions
        a_in_equation = equation[0][0].set_color(A_COLOR)  # First "8" is 'a'
        # The "-8" is 'b' (minus sign and second "8")
        b_in_equation = VGroup(equation[0][2], equation[0][3]).set_color(B_COLOR)
        # The "-3" is 'c' (second minus sign and "3")
        c_in_equation = VGroup(equation[0][5], equation[0][6]).set_color(C_COLOR)
        
        a = MathTex("a = 8", color=A_COLOR).scale(TEX_SCALE)
        a_value = a[0][2]  # Index of "8" in "a = 8"
        
        b = MathTex("b = -8", color=B_COLOR).scale(TEX_SCALE)
        b_value = VGroup(b[0][2], b[0][3])  # "-" and "8" in "b = -8"
        
        c = MathTex("c = -3", color=C_COLOR).scale(TEX_SCALE)
        c_value = VGroup(c[0][2], c[0][3])  # "-" and "3" in "c = -3"
        
        coefficients = Group(a, b, c).arrange(buff=MED_BUFF).next_to(equation, DOWN * 2)

        # Solution
        sol_step_1 = self.create_labeled_step(
            "Step 1: substitute the coefficients",
            MathTex(r"x = \frac{-(-8) \pm \sqrt{(-8)^2 - 4(8)(-3)}}{2(8)}").scale(TEX_SCALE)
        )
        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]
        step_1_fraction = step_1_exp[0][24]
        step_1_x_part = step_1_exp[0][0:2]  # "x ="
        
        # Components for animation (using direct indices)
        # Negative b parentheses
        step_1_par_part = VGroup(
            step_1_exp[0][2],  # "-"
            step_1_exp[0][3],  # "("
            step_1_exp[0][6],  # ")"
        )
        
        # "-8" inside first parentheses
        step_1_b_part = VGroup(
            step_1_exp[0][4],  # "-"
            step_1_exp[0][5],  # "8"
        )
        
        step_1_plus_minus_part = step_1_exp[0][7]  # "±"
        step_1_sqrt_part = step_1_exp[0][8:10]  # "sqrt{"
        
        # "(-8)^2" parts
        step_1_b_squared_part = VGroup(
            step_1_exp[0][10],  # "("
            step_1_exp[0][11],  # "-"
            step_1_exp[0][12],  # "8"
            step_1_exp[0][13],  # ")"
            step_1_exp[0][14],  # "^"
            step_1_exp[0][15],  # "2"
        )
        
        # "- 4" parts
        step_1_minus_four_part = VGroup(
            step_1_exp[0][16],  # "-"
            step_1_exp[0][17],  # "4"
        )
        
        # "a" and "c" parts with parentheses
        step_1_a_part = step_1_exp[0][18]  # "("
        step_1_a_val = step_1_exp[0][19]  # "8"
        step_1_a_close = step_1_exp[0][20]  # ")"
        
        step_1_c_part = VGroup(
            step_1_exp[0][21],  # "("
            step_1_exp[0][22],  # "-"
            step_1_exp[0][23],  # "3"
            step_1_exp[0][24],  # ")"
        )
        
        # Denominator parts
        step_1_two_part = step_1_exp[0][26]  # "2"
        step_1_den_a_part = VGroup(
            step_1_exp[0][27],  # "("
            step_1_exp[0][28],  # "8"
            step_1_exp[0][29],  # ")"
        )
                
        sol_step_2 = self.create_labeled_step(
            "Step 2: simplifying the expression",
            MathTex(r"x = \frac{8 \pm \sqrt{64 + 96}}{16}").scale(TEX_SCALE)
        )
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]
        
        # Step 2 components (using direct indices)
        step_2_x_part = step_2_exp[0][0:2]  # "x ="
        step_2_numerator_start = step_2_exp[0][3]  # First part after fraction line
        step_2_8_part = step_2_exp[0][3]  # "8"
        step_2_pm_part = step_2_exp[0][4]  # "±"
        step_2_sqrt_part = step_2_exp[0][5:7]  # "sqrt{"
        step_2_64_part = step_2_exp[0][7]  # "64"
        step_2_plus_part = step_2_exp[0][8]  # "+"
        step_2_96_part = step_2_exp[0][9]  # "96"
        step_2_sqrt_close = step_2_exp[0][10]  # "}"
        step_2_denominator = step_2_exp[0][12]  # "16"
                
        sol_step_3 = self.create_labeled_step(
            "Step 3: simplifying the square root",
            MathTex(r"x = \frac{8 \pm \sqrt{160}}{16}").scale(TEX_SCALE)
        )
        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]
        step_3_160_part = step_3_exp[0][7]  # "160"
        
        # Step 4: Simplify further by factoring out common factors from √160
        sol_step_4 = self.create_labeled_step(
            "Step 4: simplifying the radical",
            MathTex(r"x = \frac{8 \pm 4\sqrt{10}}{16}").scale(TEX_SCALE)
        )
        step_4_label, step_4_exp = sol_step_4[0], sol_step_4[1]
        
        # Step 5: Simplify the fraction
        sol_step_5 = self.create_labeled_step(
            "Step 5: simplifying the fraction",
            MathTex(r"x = \frac{1 \pm \sqrt{10}}{2}").scale(TEX_SCALE)
        )
        step_5_label, step_5_exp = sol_step_5[0], sol_step_5[1]
        
        self.apply_smart_colorize(
            [step_1_exp, step_2_exp, step_3_exp, step_4_exp, step_5_exp],
            {
                "x": X_COLOR,
                "8": A_COLOR,
                "-8": B_COLOR,
                "-3": C_COLOR,
            }
        )
        
        solution_steps = Group(
            sol_step_1,
            sol_step_2,
            sol_step_3,
            sol_step_4,
            sol_step_5
        ).arrange(DOWN, aligned_edge=LEFT)
        
        first_root = MathTex(r"x = \frac{1 + \sqrt{10}}{2}").scale(TEX_SCALE)
        first_root_dec = MathTex("x ≈ 2.082").scale(TEX_SCALE)
        first_root_group = Group(first_root, first_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_1, UP).to_edge(RIGHT)
        first_root_rec = self.create_surrounding_rectangle(first_root_dec)
        
        second_root = MathTex(r"x = \frac{1 - \sqrt{10}}{2}").scale(TEX_SCALE)
        second_root_dec = MathTex("x ≈ -0.582").scale(TEX_SCALE)
        second_root_group = Group(second_root, second_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_3, UP).to_edge(RIGHT)
        second_root_rec = self.create_surrounding_rectangle(second_root_dec)

        self.apply_smart_colorize(
            [first_root, first_root_dec, second_root, second_root_dec],
            {
                "x": X_COLOR,
            }
        )
        
        solution = Group(
            solution_steps,
            Group(
                first_root_group, second_root_group,
                first_root_rec, second_root_rec
            )
        ).arrange(buff=3.5).next_to(coefficients, DOWN * 1.5)

        # Tips
        tip_1 = QuickTip(r"The \textbf{quadratic formula} can quickly solve any quadratic equation")
        tip_2 = QuickTip("A quadratic equation ax² + bx + c = 0 always has exactly two solutions (which may be equal)")
        Group(tip_1, tip_2).to_corner(DL)

        # Animations
        def indicate(mobject, color=INDICATION_COLOR, run_time=INDICATION_TIME):
            return Indicate(mobject, color=color, run_time=INDICATION_TIME)
        
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
            self.play(indicate(equation))

            self.wait_until_bookmark("formula")
            self.play(indicate(quadratic_formula))

            self.wait_until_bookmark("quadratic")
            self.play(indicate(quadratic_equation))
            
            self.wait(QUICK_PAUSE)

        with self.voiceover(
                text="""
                First, let's <bookmark mark='coefficients' /> identify 'ay', 'b', and 'c'.
                'a' is the coefficient <bookmark mark='x_squared' /> of x squared. Here, it's <bookmark mark='a' /> 8.
                'b' is the coefficient <bookmark mark='x' /> of x. That is <bookmark mark='b' /> negative 8.
                And 'c' is the <bookmark mark='constant' /> constant term, which <bookmark mark='c' /> is negative 3.

                """
        ) as tracker:
            self.wait_until_bookmark("coefficients")
            self.play(
                FadeIn(a[0][:2], b[0][:2], c[0][:2])
            )

            self.wait_until_bookmark("x_squared")
            self.play(indicate(quadratic_equation_coefficients[0]))

            self.wait_until_bookmark("a")
            self.play(indicate(a_in_equation))
            self.play(FadeIn(a_value))

            self.wait_until_bookmark("x")
            self.play(indicate(quadratic_equation_coefficients[1]))

            self.wait_until_bookmark("b")
            self.play(indicate(b_in_equation))
            self.play(FadeIn(b_value))

            self.wait_until_bookmark("constant")
            self.play(indicate(quadratic_equation_coefficients[2]))

            self.wait_until_bookmark("c")
            self.play(indicate(c_in_equation))
            self.play(FadeIn(c_value))

            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Now, let's substitute these values into the quadratic formula.
                """
        ) as tracker:
            self.play(Write(step_1_label))

        with self.voiceover(
                text="""
                x equals negative 'b', <bookmark mark='negative_b' /> which is the negative of negative 8, so that's positive 8,
                <bookmark mark='plus_minus' /> plus or minus the square root of 'b' squared,
                <bookmark mark='b_squared' /> so negative 8 squared,
                <bookmark mark='minus_4' /> minus 4 times 'ay',
                which <bookmark mark='a_1' /> is 8, times 'c', <bookmark mark='c' /> which is negative 3,
                all divided <bookmark mark='two' /> by 2 times 'ay', which <bookmark mark='a_2' /> is 8.
                """
        ) as tracker:
            self.play(Write(step_1_x_part))
            self.play(Write(step_1_fraction))

            self.wait_until_bookmark("negative_b")
            self.play(Write(step_1_par_part))
            self.play(ReplacementTransform(b_value.copy(), step_1_b_part))

            self.wait_until_bookmark("plus_minus")
            self.play(Write(step_1_plus_minus_part))
            self.play(Write(step_1_sqrt_part))
            
            self.wait_until_bookmark("b_squared")
            self.play(Write(step_1_b_squared_part))
        
            self.wait_until_bookmark("minus_4")
            self.play(Write(step_1_minus_four_part))

            self.wait_until_bookmark("a_1")
            self.play(
                Write(step_1_a_part),
                ReplacementTransform(a_value.copy(), step_1_a_val),
                Write(step_1_a_close)
            )

            self.wait_until_bookmark("c")
            self.play(
                ReplacementTransform(c_value.copy(), step_1_c_part)
            )

            self.wait_until_bookmark("two")
            self.play(Write(step_1_two_part))

            self.wait_until_bookmark("a_2")
            self.play(
                Write(step_1_den_a_part)
            )
            
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(
                text="""
                Next, we simplify step by step: Negative 8 squared <bookmark mark='b_squared' /> equals 64.
                4 times 8 times negative 3 <bookmark mark='four_ac' /> equals plus 96. We get a plus here because the product of two negatives is positive.
                Finally, 2 times 8 <bookmark mark='den' /> equals 16. 
                """
        ) as tracker:
            self.play(Write(step_2_label))
            
            # Transform step 1 to step 2 (simple approach focusing on key parts)
            self.play(
                TransformFromCopy(step_1_x_part, step_2_x_part),
                TransformFromCopy(step_1_fraction, step_2_exp[0][2]),  # fraction bar
                FadeIn(step_2_numerator_start)  # "8" in numerator (replaces "-(-8)")
            )
            
            # Continue with plus-minus and sqrt
            self.play(
                TransformFromCopy(step_1_plus_minus_part, step_2_pm_part),
                TransformFromCopy(step_1_sqrt_part, step_2_sqrt_part)
            )
        
            self.wait_until_bookmark("b_squared")
            self.play(FadeIn(step_2_64_part))  # "64" (replaces (-8)²)
                
            self.wait_until_bookmark("four_ac")
            self.play(FadeIn(step_2_plus_part, step_2_96_part))  # "+" and "96" (replaces -4(8)(-3))
            
            self.wait_until_bookmark("den")
            self.play(FadeIn(step_2_denominator))  # "16" (replaces 2(8))

            self.wait(COMPREHENSION_PAUSE)
            
        with self.voiceover(
                text="""
                Next, we add 64 and 96 <bookmark mark='equation' /> which gives us 160 under the square root.
                """
        ) as tracker:
            self.play(Write(step_3_label))
            
            # Transform step 2 to step 3 (simple copy of the whole expression)
            self.play(TransformFromCopy(step_2_exp, step_3_exp))
            
            self.wait_until_bookmark("equation")
            # Highlight the 160 replacing 64 + 96
            self.play(Indicate(step_3_160_part, color=YELLOW))

            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                We can simplify the radical by factoring out 16, which gives us the square root of 160 equals 4 times the square root of 10.
                """
        ) as tracker:
            self.play(Write(step_4_label))
            self.play(TransformFromCopy(step_3_exp, step_4_exp))
            self.wait(STANDARD_PAUSE)
            
        with self.voiceover(
                text="""
                Now we can simplify the fraction by dividing both the numerator and denominator by 8.
                """
        ) as tracker:
            self.play(Write(step_5_label))
            self.play(TransformFromCopy(step_4_exp, step_5_exp))
            self.play(FadeIn(tip_2, shift=UP))
            self.wait(STANDARD_PAUSE)
        self.play(FadeOut(tip_2, shift=DOWN))

        with self.voiceover(
                text="""
                Since we're done simplifying, we'll write both solutions;
                one <bookmark mark='roots' /> with a plus and one with a minus.
                """
        ) as tracker:
            self.wait_until_bookmark("roots")
            self.play(
                TransformFromCopy(step_5_exp, first_root),
                TransformFromCopy(step_5_exp, second_root),
                run_time=2
            )
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                Finally, if we want decimal approximations: the first solution, with the plus, is <bookmark mark='root_1' /> approximately 2.082.

                The second solution, using the minus, is <bookmark mark='root_2' /> approximately -0.582.
                """
        ) as tracker:
            self.wait_until_bookmark("root_1")
            self.play(Write(first_root_dec))

            self.wait_until_bookmark("root_2")
            self.play(Write(second_root_dec))
            self.wait(QUICK_PAUSE)
            
        with self.voiceover(
                text="""
                So these are our two solutions for the equation 8x² - 8x - 3 = 0, derived using the quadratic formula.
                """
        ) as tracker:
            self.play(Create(first_root_rec), Create(second_root_rec), run_time=2)
            
        self.wait(5)