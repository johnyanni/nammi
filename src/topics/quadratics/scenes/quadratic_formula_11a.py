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

                        
        quadratic_equation = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        SmartColorizeStatic(quadratic_equation, {"2": X_COLOR})
        
        quadratic_equation_coefficients = Group(
            *[
                quadratic_equation[0][group] for group in
                search_shapes_in_text(quadratic_equation, [MathTex("a"), MathTex("b"), MathTex("c")])
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
        equation = MathTex("1x^2 + 11x + 20 = 0").scale(TEX_SCALE).next_to(quadratic_group, DOWN)
        SmartColorizeStatic(
            equation,
            {
                "x": X_COLOR,
                "2": X_COLOR,
            }
        )
        a_in_equation = equation[0][search_shape_in_text(equation, MathTex("1"))[0]].set_opacity(0)
        b_in_equation = equation[0][search_shape_in_text(equation, MathTex("11"))[0]].set_color(B_COLOR)
        c_in_equation = equation[0][search_shape_in_text(equation, MathTex("20"))[0]].set_color(C_COLOR)
        
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        a_value = a[0][search_shape_in_text(a, MathTex("1"))[0]]
        
        b = MathTex("b = 11", color=B_COLOR).scale(TEX_SCALE)
        b_value = b[0][search_shape_in_text(b, MathTex("11"))[0]]
        
        c = MathTex("c = 20", color=C_COLOR).scale(TEX_SCALE)
        c_value = c[0][search_shape_in_text(c, MathTex("20"))[0]]
        
        coefficients = Group(a, b, c).arrange(buff=MED_BUFF).next_to(equation, DOWN * 2)

        # Solution Step 1 - Cleaner approach
        # Create step 1 equation
        step_1_tex = r"x = \frac{-(11) \pm \sqrt{(11)^2 - 4(1)(20)}}{2(1)}"
        sol_step_1 = self.create_labeled_step(
            "Step 1: substitute the coefficients",
            MathTex(step_1_tex).scale(TEX_SCALE)
        )
        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]

        # Helper function to find elements in the equation
        def find_element(pattern, exp=step_1_exp, nth=0, as_group=False):
            indices = search_shape_in_text(exp, MathTex(pattern))
            if not indices or nth >= len(indices):
                return None
            if as_group:
                return VGroup(exp[0][indices[nth]])
            return exp[0][indices[nth]]

        def find_elements(pattern, exp=step_1_exp, as_group=True):
            indices = search_shape_in_text(exp, MathTex(pattern))
            if not indices:
                return None
            elements = [exp[0][idx] for idx in indices]
            return VGroup(*elements) if as_group else elements

        # Find basic elements
        step_1_fraction = step_1_exp[0][24]  # Known index for fraction
        step_1_x_part = find_element("x =")
        step_1_plus_minus_part = find_element(r"\pm")
        step_1_sqrt_part = VGroup(step_1_exp[0][8:10])  # Known indices for sqrt
        step_1_two_part = find_element("2", nth=2)

        # Find parentheses groups
        step_1_par_part = VGroup(
            # Group 1: -(11)
            VGroup(
                find_element("-"), 
                find_element("(", nth=0), 
                find_element(")", nth=0)
            ),
            # Group 2: (11)^2
            VGroup(
                find_element("(", nth=1), 
                find_element(")", nth=1),
                find_element("2", nth=0)
            ),
            # Group 3: (1)(20)
            VGroup(
                find_element("(", nth=2), 
                find_element(")", nth=2),
                find_element("(", nth=3), 
                find_element(")", nth=3)
            ),
            # Group 4: (1) in denominator
            VGroup(
                find_element("(", nth=4), 
                find_element(")", nth=4)
            )
        )

        # Find coefficient values
        step_1_b_part = find_elements("11")
        step_1_minus_four_part = VGroup(find_element("-", nth=1), find_element("4"))
        step_1_a_part = VGroup(
            find_element("1", nth=4),
            find_element("1", nth=5)
        )
        step_1_c_part = find_element("20")
        
        # Solution Step 2        
        sol_step_2 = self.create_labeled_step(
            "Step 2: simplifying the expression",
            MathTex(r"x = \frac{-11 \pm \sqrt{121 - 80}}{2}").scale(TEX_SCALE)
        )
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]
        
        # Helper function to find elements in step 2
        def find_step2_element(pattern, nth=0):
            return find_element(pattern, exp=step_2_exp, nth=nth)
            
        def find_step2_elements(pattern):
            return find_elements(pattern, exp=step_2_exp)
        
        step_2_fraction = step_2_exp[0][14]
        step_2_x_part = find_step2_element("x =")
        step_2_b_part = VGroup(
            VGroup(
                find_step2_element("-"),
                find_step2_element("11")
            ),
            find_step2_element("121")
        )
        step_2_plus_minus_part = find_step2_element(r"\pm")
        step_2_sqrt_part = VGroup(step_2_exp[0][6:8])
        step_2_4ac_part = VGroup(
            find_step2_element("-", nth=1),
            find_step2_element("80")
        )
        step_2_two_part = find_step2_element("2", nth=1)

        step_2_transform_index = [
            [0, 1, 2, 4, 5, 7, 8, 9, 24],
            [0, 1, 2, 3, 4, 5, 6, 7, 14]
        ]
        
        # Solution Step 3       
        sol_step_3 = self.create_labeled_step(
            "Step 3: simplifying the square root",
            MathTex(r"x = \frac{-11 \pm \sqrt{41}}{2}").scale(TEX_SCALE)
        )
        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]
        
        # Helper function to find elements in step 3
        def find_step3_element(pattern, nth=0):
            return find_element(pattern, exp=step_3_exp, nth=nth)
            
        step_3_41_index = search_shape_in_text(step_3_exp, MathTex("41"))[0]
        step_3_41_part = step_3_exp[0][step_3_41_index]
        step_3_transform_index = [
            [0, 1, 2, 3, 4, 5, 6, 7, 14, 15],
            [0, 1, 2, 3, 4, 5, 6, 7, 10, 11]
        ]
        
        self.apply_smart_colorize(
            [step_1_exp, step_2_exp, step_3_exp],
            {
                "x": X_COLOR,
                "1": A_COLOR,
                "20": C_COLOR,
                "121": WHITE,
                "41": WHITE,
                "11": B_COLOR,
            }
        )
        
        solution_steps = Group(
            sol_step_1,
            sol_step_2,
            sol_step_3
        ).arrange(DOWN, aligned_edge=LEFT)
        
        first_root = MathTex(r"x = \frac{-11 + \sqrt{41}}{2}").scale(TEX_SCALE)
        first_root_dec = MathTex("x = -2.298").scale(TEX_SCALE)
        first_root_group = Group(first_root, first_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_1, UP).to_edge(RIGHT)
        first_root_rec = self.create_surrounding_rectangle(first_root_dec)
        
        second_root = MathTex(r"x = \frac{-11 - \sqrt{41}}{2}").scale(TEX_SCALE)
        second_root_dec = MathTex("x = -8.702").scale(TEX_SCALE)
        second_root_group = Group(second_root, second_root_dec).arrange(DOWN, aligned_edge=LEFT).align_to(sol_step_3, UP).to_edge(RIGHT)
        second_root_rec = self.create_surrounding_rectangle(second_root_dec)

        self.apply_smart_colorize(
            [first_root, first_root_dec, second_root, second_root_dec],
            {
                "x": X_COLOR,
                "11": B_COLOR
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
        tip_1 = QuickTip(r"The \textbf{quadratic formula} is faster than completing the square in many cases")
        tip_2 = QuickTip("Writing the answer in decimal format is not entirely necessary")
        Group(tip_1, tip_2).to_corner(DL)

        # Animations
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
            self.play(self.indicate(quadratic_equation_coefficients[0]))

            self.wait_until_bookmark("a")
            self.play(FadeIn(a_value, target_position=a_in_equation), run_time=2)

            self.wait_until_bookmark("x")
            self.play(self.indicate(quadratic_equation_coefficients[1]))

            self.wait_until_bookmark("b")
            self.play(FadeIn(b_value, target_position=b_in_equation), run_time=2)

            self.wait_until_bookmark("constant")
            self.play(self.indicate(quadratic_equation_coefficients[2]))

            self.wait_until_bookmark("c")
            self.play(FadeIn(c_value, target_position=c_in_equation), run_time=2)

            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text="""
                Now, let's substitute these values into the quadratic formula.
                """
        ) as tracker:
            self.play(Write(step_1_label))

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
            self.play(Write(step_1_x_part), Write(step_1_fraction))

            self.wait_until_bookmark("negative_b")
            self.play(Write(step_1_par_part[0]))
            self.play(ReplacementTransform(b_value.copy(), step_1_b_part[0]))

            self.wait_until_bookmark("plus_minus")
            self.play(Write(step_1_plus_minus_part))
            self.play(Write(step_1_sqrt_part))
            
            self.wait_until_bookmark("b_squared")
            self.play(
                Write(step_1_par_part[1]),
            )
            self.play(ReplacementTransform(b_value.copy(), step_1_b_part[1]))
        
            
            self.wait_until_bookmark("minus_4")
            self.play(
                Write(step_1_minus_four_part),
                Write(step_1_par_part[2]),
            )

            self.wait_until_bookmark("a_1")
            self.play(
                ReplacementTransform(a_value.copy(), step_1_a_part[0])
            )

            self.wait_until_bookmark("c")
            self.play(
                ReplacementTransform(c_value.copy(), step_1_c_part)
            )

            self.wait_until_bookmark("two")
            self.play(
                Write(step_1_two_part),
                Write(step_1_par_part[3]),
            )

            self.wait_until_bookmark("a_2")
            self.play(
                ReplacementTransform(a_value.copy(), step_1_a_part[1])
            )
            
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(
                text="""
                Next, we simplify step by step: 11 squared <bookmark mark='b_squared' /> equals 121.
                negative 4 times 1 times 20 <bookmark mark='four_ac' /> equals negative 80.
                Finally, 2 times 1 <bookmark mark='den' /> equals 2. 
                """
        ) as tracker:
            self.play(Write(step_2_label))
            self.play(
                *[
                    FadeTransform(step_1_exp[0][i][:].copy(), step_2_exp[0][j][:])
                    if i == 8 or i == 9 else
                    ReplacementTransform(step_1_exp[0][i][:].copy(), step_2_exp[0][j][:])
                    for i, j in zip(*step_2_transform_index)
                ]
            )
        
            self.wait_until_bookmark("b_squared")
            self.play(FadeIn(step_2_b_part[1]))
                
            self.wait_until_bookmark("four_ac")
            self.play(FadeIn(step_2_4ac_part))
            
            self.wait_until_bookmark("den")
            self.play(FadeIn(step_2_two_part))

            self.wait(COMPREHENSION_PAUSE)
            
        with self.voiceover(
                text="""
                And finally, 121 minus 80 <bookmark mark='equation' /> gives us 41.
                """
        ) as tracker:
            self.play(Write(step_3_label))
            self.play(
                *[
                    ReplacementTransform(step_2_exp[0][i].copy(), step_3_exp[0][j])
                    for i, j in zip(*step_3_transform_index)
                ]
            )
            
            self.wait_until_bookmark("equation")
            self.play(FadeIn(step_3_41_part))

            self.wait(COMPREHENSION_PAUSE)

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
            
        with self.voiceover(
                text="""
                So these are the actual solutions using the quadratic formula.
                """
        ) as tracker:
            self.play(Create(first_root_rec), Create(second_root_rec), run_time=2)
            
        self.wait(5)