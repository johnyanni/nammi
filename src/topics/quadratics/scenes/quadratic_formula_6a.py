from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class EquationParts:
    """Helper class to easily identify and reference parts of an equation for animation."""
    
    def __init__(self, equation, tex_scale=0.7):
        """Initialize with an equation.
        
        Args:
            equation: A MathTex object
            tex_scale: Scaling factor for new equations created
        """
        self.equation = equation
        self.parts = {}
        self.tex_scale = tex_scale
    
    def find_part(self, name, pattern, indices=None, color=None):
        """Find a part in the equation by pattern.
        
        Args:
            name: Name to reference this part by
            pattern: LaTeX pattern to search for
            indices: Specific occurrence indices if there are multiple matches
            color: Optional color to apply to this part
        
        Returns:
            self for method chaining
        """
        search_result = search_shape_in_text(self.equation, MathTex(pattern))
        
        if not search_result:
            print(f"Warning: Pattern '{pattern}' not found in equation")
            return self
        
        # If indices specified, get only those occurrences
        if indices is not None:
            if isinstance(indices, int):
                indices = [indices]  # Convert single index to list
            
            # Make sure we don't exceed available indices
            valid_indices = [i for i in indices if i < len(search_result)]
            if not valid_indices:
                print(f"Warning: Specified indices {indices} not found for pattern '{pattern}'")
                return self
                
            # Create VGroup of specified occurrences
            part = VGroup(*[self.equation[0][search_result[i]] for i in valid_indices])
        else:
            # If no specific indices, use the first occurrence
            part = self.equation[0][search_result[0]]
        
        # Apply color if specified
        if color:
            part.set_color(color)
        
        self.parts[name] = part
        return self
    
    def find_group(self, name, patterns, color=None):
        """Find a group of parts matching multiple patterns.
        
        Args:
            name: Name to reference this group by
            patterns: List of LaTeX patterns to search for
            color: Optional color to apply to this group
        
        Returns:
            self for method chaining
        """
        mobjects = []
        
        for pattern in patterns:
            search_result = search_shape_in_text(self.equation, MathTex(pattern))
            if search_result:
                mobjects.append(self.equation[0][search_result[0]])
        
        if not mobjects:
            print(f"Warning: None of the patterns in {patterns} found in equation")
            return self
            
        group = VGroup(*mobjects)
        
        # Apply color if specified
        if color:
            group.set_color(color)
            
        self.parts[name] = group
        return self
    
    def get_part(self, name):
        """Get a previously found part by name."""
        if name in self.parts:
            return self.parts[name]
        print(f"Warning: Part '{name}' not found")
        return None
    
    def create_from_formula(formula, a_val, b_val, c_val, tex_scale=0.7):
        """Factory method to create a substituted equation from the quadratic formula.
        
        Args:
            formula: The original quadratic formula template
            a_val: Value of coefficient a
            b_val: Value of coefficient b
            c_val: Value of coefficient c
            tex_scale: Scaling factor for the equation
            
        Returns:
            EquationParts object with the substituted equation
        """
        substituted = MathTex(
            f"x = \\frac{{-({b_val})" + 
            f" \\pm \\sqrt{{({b_val})^2 - 4({a_val})({c_val})}}}}{{2({a_val})}}"
        ).scale(tex_scale)
        
        return EquationParts(substituted, tex_scale)


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

        # Create the basic equations                   
        quadratic_equation = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        SmartColorizeStatic(quadratic_equation, {"2": X_COLOR})
        
        # Find coefficient parts for the general equation
        quad_eq_parts = EquationParts(quadratic_equation)
        quad_eq_parts.find_part("a", "a", color=A_COLOR)
        quad_eq_parts.find_part("b", "b", color=B_COLOR)
        quad_eq_parts.find_part("c", "c", color=C_COLOR)
        
        # Create the quadratic formula
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        
        # Arrange the equations
        quadratic_group = Group(
            quadratic_equation,
            quadratic_formula,
        ).arrange(buff=WIDE_BUFF).to_edge(UP)
        
        # Apply colors
        self.apply_smart_colorize(
            quadratic_group,
            {
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "a": A_COLOR,
            }
        )
        
        # Create backgrounds
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
        
        # Find coefficients in the example equation
        equation_parts = EquationParts(equation)
        equation_parts.find_part("a", "1", color=A_COLOR).get_part("a").set_opacity(0)
        equation_parts.find_part("b", "11", color=B_COLOR)
        equation_parts.find_part("c", "20", color=C_COLOR)
        
        # Create coefficient labels
        a_eq = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        a_parts = EquationParts(a_eq)
        a_parts.find_part("value", "1", color=A_COLOR)
        
        b_eq = MathTex("b = 11", color=B_COLOR).scale(TEX_SCALE)
        b_parts = EquationParts(b_eq)
        b_parts.find_part("value", "11", color=B_COLOR)
        
        c_eq = MathTex("c = 20", color=C_COLOR).scale(TEX_SCALE)
        c_parts = EquationParts(c_eq)
        c_parts.find_part("value", "20", color=C_COLOR)
        
        # Group the coefficients
        coefficients = Group(a_eq, b_eq, c_eq).arrange(buff=MED_BUFF).next_to(equation, DOWN * 2)

        # Step 1 - Create from template
        sol_step_1 = self.create_labeled_step(
            "Step 1: substitute the coefficients",
            MathTex(r"x = \frac{-(11) \pm \sqrt{(11)^2 - 4(1)(20)}}{2(1)}").scale(TEX_SCALE)
        )
        step_1_label, step_1_exp = sol_step_1[0], sol_step_1[1]
        
        # Find parts in step 1 equation
        step_1_parts = EquationParts(step_1_exp)
        step_1_parts.find_part("x_part", "x =")
        step_1_parts.find_part("fraction", r"\frac")
        
        # Find negative b part
        step_1_parts.find_group("negative_b", ["-", "(", "11", ")"])
        step_1_parts.find_part("b_value_1", "11", color=B_COLOR)
        
        # Find plus/minus and sqrt parts
        step_1_parts.find_part("plus_minus", r"\pm")
        step_1_parts.find_part("sqrt_part", r"\sqrt")
        
        # Find b squared part
        step_1_parts.find_group("b_squared", ["(", "11", ")", "^", "2"])
        step_1_parts.find_part("b_value_2", "11", color=B_COLOR)
        
        # Find the -4ac part
        step_1_parts.find_part("minus_sign", "-", indices=1)
        step_1_parts.find_part("four", "4")
        step_1_parts.find_group("minus_four", ["-", "4"])
        
        # Find the values of a and c
        step_1_parts.find_part("a_value_1", "1", indices=0, color=A_COLOR)
        step_1_parts.find_part("a_value_2", "1", indices=1, color=A_COLOR)
        step_1_parts.find_part("c_value", "20", color=C_COLOR)
        
        # Find the denominator parts
        step_1_parts.find_part("two_part", "2", indices=2)
        step_1_parts.find_group("denominator", ["2", "(", "1", ")"])
        
        # Create simplified steps
        sol_step_2 = self.create_labeled_step(
            "Step 2: simplifying the expression",
            MathTex(r"x = \frac{-11 \pm \sqrt{121 - 80}}{2}").scale(TEX_SCALE)
        )
        step_2_label, step_2_exp = sol_step_2[0], sol_step_2[1]
        
        # Create Step 3
        sol_step_3 = self.create_labeled_step(
            "Step 3: simplifying the square root",
            MathTex(r"x = \frac{-11 \pm \sqrt{41}}{2}").scale(TEX_SCALE)
        )
        step_3_label, step_3_exp = sol_step_3[0], sol_step_3[1]
        
        # Apply color to all steps
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
                FadeIn(a_eq[0][:2], b_eq[0][:2], c_eq[0][:2])
            )

            self.wait_until_bookmark("x_squared")
            self.play(self.indicate(quad_eq_parts.get_part("a")))

            self.wait_until_bookmark("a")
            self.play(FadeIn(a_parts.get_part("value"), 
                    target_position=equation_parts.get_part("a")), run_time=2)

            self.wait_until_bookmark("x")
            self.play(self.indicate(quad_eq_parts.get_part("b")))

            self.wait_until_bookmark("b")
            self.play(FadeIn(b_parts.get_part("value"), 
                    target_position=equation_parts.get_part("b")), run_time=2)

            self.wait_until_bookmark("constant")
            self.play(self.indicate(quad_eq_parts.get_part("c")))

            self.wait_until_bookmark("c")
            self.play(FadeIn(c_parts.get_part("value"), 
                    target_position=equation_parts.get_part("c")), run_time=2)

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
            self.play(
                Write(step_1_parts.get_part("x_part")), 
                Write(step_1_parts.get_part("fraction"))
            )

            self.wait_until_bookmark("negative_b")
            self.play(Write(step_1_parts.get_part("negative_b")))
            self.play(ReplacementTransform(b_parts.get_part("value").copy(), 
                                          step_1_parts.get_part("b_value_1")))

            self.wait_until_bookmark("plus_minus")
            self.play(Write(step_1_parts.get_part("plus_minus")))
            self.play(Write(step_1_parts.get_part("sqrt_part")))
            
            self.wait_until_bookmark("b_squared")
            self.play(Write(step_1_parts.get_part("b_squared")))
            self.play(ReplacementTransform(b_parts.get_part("value").copy(), 
                                          step_1_parts.get_part("b_value_2")))
        
            self.wait_until_bookmark("minus_4")
            self.play(
                Write(step_1_parts.get_part("minus_four"))
            )

            self.wait_until_bookmark("a_1")
            self.play(
                ReplacementTransform(a_parts.get_part("value").copy(), 
                                    step_1_parts.get_part("a_value_1"))
            )

            self.wait_until_bookmark("c")
            self.play(
                ReplacementTransform(c_parts.get_part("value").copy(), 
                                    step_1_parts.get_part("c_value"))
            )

            self.wait_until_bookmark("two")
            self.play(
                Write(step_1_parts.get_part("two_part"))
            )

            self.wait_until_bookmark("a_2")
            self.play(
                ReplacementTransform(a_parts.get_part("value").copy(), 
                                    step_1_parts.get_part("a_value_2"))
            )
            
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        # Steps 2 and 3 - Simplified approach as before
        with self.voiceover(
                text="""
                Next, we simplify step by step: 11 squared <bookmark mark='b_squared' /> equals 121.
                negative 4 times 1 times 20 <bookmark mark='four_ac' /> equals negative 80.
                Finally, 2 times 1 <bookmark mark='den' /> equals 2. 
                """
        ) as tracker:
            self.play(Write(step_2_label))
            
            # Simple fade in of the whole step 2 equation
            self.play(FadeIn(step_2_exp))
            
            # Find parts for indicators
            step_2_parts = EquationParts(step_2_exp)
            step_2_parts.find_part("b_squared", "121")
            step_2_parts.find_part("four_ac", "80")
            step_2_parts.find_part("denominator", "2")
            
            # Indicate the relevant parts at each bookmark
            self.wait_until_bookmark("b_squared")
            self.play(Indicate(step_2_parts.get_part("b_squared")))
                
            self.wait_until_bookmark("four_ac")
            self.play(Indicate(step_2_parts.get_part("four_ac")))
            
            self.wait_until_bookmark("den")
            self.play(Indicate(step_2_parts.get_part("denominator")))

            self.wait(COMPREHENSION_PAUSE)
            
        with self.voiceover(
                text="""
                And finally, 121 minus 80 <bookmark mark='equation' /> gives us 41.
                """
        ) as tracker:
            self.play(Write(step_3_label))
            
            # Simple fade in of the whole step 3 equation
            self.play(FadeIn(step_3_exp))
            
            # Find the 41 for indication
            step_3_parts = EquationParts(step_3_exp)
            step_3_parts.find_part("sqrt_value", "41")
            
            self.wait_until_bookmark("equation")
            self.play(Indicate(step_3_parts.get_part("sqrt_value")))

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