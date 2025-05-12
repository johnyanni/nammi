from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from sympy import symbols, Eq, solve, simplify, parse_expr



# Equation
EQUATION = "4n - 26 = -2"
VARIABLE = "n"

# Colors
VARIABLE_COLOR = "#9C7BFF"      
COEFF_COLOR = "#FF6B8B"         
LEFT_CONSTANT_COLOR = "#4ECDC4" 
RIGHT_CONSTANT_COLOR = "#FF8C64" 
TITLE_COLOR = "#E6E6FA"      
PLUS_COLOR = "#5DADE2"       
MINUS_COLOR = "#FF7D63"      
TIMES_COLOR = "#827DD1"      
DIVISION_COLOR = "#F78FB3"   
ARROW_COLOR = "#D5DBDB"



class TwoStepEquations01a(MathTutorialScene):
    def TransformThenWrite(self, source, target, transform_index, write_index=None):
        self.play(
            *[
                ReplacementTransform(source[0][i].copy(), target[0][j])
                for i, j in zip(*transform_index)
                if type(i) in [int, slice] and type(j) in [int, slice]
            ],
        )

        if write_index:
            self.play(
                *[
                    Write(target[0][i])
                    for i in write_index
                ]
            )
    
    def construct(self):
        # Title and Operations
        self.title = Tex("Solve.", color=TITLE_COLOR).to_corner(UL)
        operations_plus_minus = MathTex(r"+ \Longleftrightarrow -")
        operations_mul_div = MathTex(r"\times \Longleftrightarrow \div")
        self.operations = VGroup(operations_plus_minus, operations_mul_div).arrange(buff=1).to_edge(DOWN, buff=1).scale(2)
        self.apply_smart_colorize(
            self.operations,
            {
                "+": PLUS_COLOR,
                "-": MINUS_COLOR,
                r"\times": TIMES_COLOR,
                r"\div": DIVISION_COLOR,
                r"\Longleftrightarrow": ARROW_COLOR
            }
        )
        
        self.solve_equation(EQUATION, VARIABLE)
        self.wait(5)
        
    def solve_equation(self, equation, variable_name="x"):
        left, right = equation.split("=")
        left = left.strip()
        right = right.strip()

        variable = symbols(variable_name)
        eq_left = parse_expr(left, transformations="all")
        eq_right = parse_expr(right, transformations="all")
        equation = Eq(eq_left, eq_right)

        solution = solve(equation, variable)[0]

        equation_tex = MathTex(f"{left} = {right}")
        
        # Identify coefficients and constants
        coefficient = eq_left.coeff(variable)
        constants_left = eq_left - coefficient * variable
        constants_right = eq_right

        # Move constants to the right side
        new_right = constants_right - constants_left
        new_right_simplified = simplify(new_right)

        # Create the next step
        steps = []
        if constants_left != 0:
            operation = ""
            if constants_left > 0:
                operation = f"- {constants_left}"
            else:
                operation = f"+ {-constants_left}"
            step1_tex = MathTex(f"{{{operation}}} {{{operation}}}").scale(MATH_SCALE_SMALL)
            if coefficient == -1:
                coefficient_tex = "-"
            elif coefficient == 1:
                coefficient_tex = ""
            else:
                coefficient_tex = f"{coefficient}"
            step1_result = MathTex(f"{coefficient_tex}{variable_name} = {new_right_simplified}")
            
            steps.extend([step1_tex, step1_result])

        # Divide by coefficient
        if coefficient != 1:
            step2_tex = MathTex(fr"{{\div {coefficient}}} {{\div {coefficient}}}").scale(MATH_SCALE_SMALL)
            step2_result = MathTex(f"{variable_name} = {solution}")
            steps.extend([step2_tex, step2_result])
        
        solution_steps = VGroup(
            equation_tex,
            *steps
        ).scale(MATH_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(UP)
        self.apply_smart_colorize(
            solution_steps,
            {
                #variable_name: VARIABLE_COLOR,
                coefficient_tex: COEFF_COLOR,
                f"{abs(constants_left)}": LEFT_CONSTANT_COLOR,
                f"{right}": RIGHT_CONSTANT_COLOR,
                f"{new_right_simplified}": WHITE,
                "+": PLUS_COLOR,
                "-": MINUS_COLOR,
                r"\times": TIMES_COLOR,
                r"\div": DIVISION_COLOR,
            }
        )
        
        # Use shape-based transformation for precise control
        equation_left_side_idx = search_shape_in_text(equation_tex, MathTex(left))[0]
        equation_right_side_idx = search_shape_in_text(equation_tex, MathTex(right))[-1]
        equation_equal_idx = search_shape_in_text(equation_tex, MathTex("="))[0]
        equation_coeff_idx = search_shape_in_text(equation_tex, MathTex(coefficient_tex))[0]
        equation_variable_idx = search_shape_in_text(equation_tex, MathTex(variable_name))[0]
        equation_constants_left_idx = slice(equation_variable_idx.stop, equation_equal_idx.start)

        step1_tex_operation_idx = search_shape_in_text(step1_tex, MathTex(operation))
        
        step1_result_coeff_idx = search_shape_in_text(step1_result, MathTex(coefficient_tex))
        if step1_result_coeff_idx:
            step1_result_coeff_idx = step1_result_coeff_idx[0]
            
        step1_result_variable_idx = search_shape_in_text(step1_result, MathTex(variable_name))[0]
        step1_result_right_idx = search_shape_in_text(step1_result, MathTex(new_right_simplified))[-1]
        step1_result_equal_idx = search_shape_in_text(step1_result, MathTex("="))[0]

        equation_step1_transform_index = [
            [equation_coeff_idx, equation_variable_idx, equation_equal_idx],
            [step1_result_coeff_idx, step1_result_variable_idx, step1_result_equal_idx]
        ]

        step1_step2_transform_index = [
            [step1_result_variable_idx, step1_result_equal_idx],
            [0, 1]
        ]

        if coefficient != 1:
            step2_tex_operation_idx = search_shape_in_text(step2_tex, MathTex(fr"\div {coefficient}"))
        
        
        # Place the cancelling and division operation below the equation 
        step1_tex[0][step1_tex_operation_idx[0]].next_to(equation_tex[0][equation_constants_left_idx], DOWN)
        step1_tex[0][step1_tex_operation_idx[0]][0].match_x(equation_tex[0][equation_constants_left_idx][0])
        step1_tex[0][step1_tex_operation_idx[0]][1:].match_x(equation_tex[0][equation_constants_left_idx][1:])
        step1_tex[0][step1_tex_operation_idx[1]].next_to(equation_tex[0][equation_right_side_idx], DOWN, aligned_edge=LEFT)

        if coefficient != 1:
            step2_tex[0][step2_tex_operation_idx[0]].next_to(step1_result[0][step1_result_variable_idx], DOWN, aligned_edge=RIGHT)
            step2_tex[0][step2_tex_operation_idx[1]].next_to(step1_result[0][step1_result_right_idx], DOWN, aligned_edge=LEFT)


        # Tips
        step1_operation = "adding" if constants_left < 0 else "subtracting"
        
        tip_1 = QuickTip("Get rid of the plus/minus before the multiply/divide")
        tip_2 = QuickTip(
            fr"\textbf{{Step 1}}: get rid of the ${constants_left}$ by {step1_operation} ${abs(constants_left)}$ to both sides",
            color_map={
                f"{constants_left}": LEFT_CONSTANT_COLOR,
                f"{abs(constants_left)}": LEFT_CONSTANT_COLOR,
            }
        )

        tips = VGroup(tip_1, tip_2)
        if coefficient != 1:
            tip_3 = QuickTip(
                fr"\textbf{{Step 2}}: get rid of the ${coefficient}$ by dividing ${coefficient}$ from both sides",
                color_map={
                    f"{coefficient}": COEFF_COLOR,
                }
            )
            tips.add(tip_3)
        tip_4 = QuickTip(
            fr"\textbf{{Verify}}: substitute ${variable_name} = {solution}$ into the equation; ${coefficient} \times {solution} {'+' if constants_left > 0 else ''} {constants_left} = {constants_right}$",
            color_map={
                # variable_name: VARIABLE_COLOR,
                coefficient_tex: COEFF_COLOR,
                f"{abs(constants_left)}": LEFT_CONSTANT_COLOR,
                f"{right}": RIGHT_CONSTANT_COLOR,
                "+": PLUS_COLOR,
                "-": MINUS_COLOR,
                r"\times": TIMES_COLOR,
            }
        ).to_corner(DL)
        tips.to_corner(DR)
        tip_3.to_corner(DL)
        
        # Animations
        with self.voiceover("In this example, we are trying to solve the following <bookmark mark='equation' /> linear equation"):
            self.play(FadeIn(self.title, self.operations, equation_tex))
            self.wait_until_bookmark("equation")
            self.play(self.indicate(equation_tex))

        with self.voiceover(
                text=f"""
                Solving the equation means we need to <bookmark mark='n' /> identify 'n'.
                To solve, we need n by itself on one side of the equals sign and a number on the other side.

                To achieve this, we need to get rid of what's <bookmark mark='constants' /> around the variable n,
                so we will get rid of the {coefficient} and the {constants_left}. 
                """
        ):
            self.wait_until_bookmark("n")
            self.play(self.indicate(equation_tex[0][equation_variable_idx]))

            self.wait_until_bookmark("constants")
            self.play(
                self.indicate(equation_tex[0][equation_coeff_idx]),
                self.indicate(equation_tex[0][equation_constants_left_idx])
            )
            self.wait(STANDARD_PAUSE)

        with self.voiceover("Generally, we handle addition and subtraction before multiplication and division."):
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(STANDARD_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        operation_verb_spoken = "subtracting" if constants_left < 0 else "adding"
        operation_verb_standard_spoken = "subtract" if constants_left < 0 else "add"
        operation_noun_spoken = "subtraction" if constants_left < 0 else "addition"
        opposite_operation_noun_spoken = "addition" if constants_left < 0 else "subtraction"
        opposite_operation_verb_standard_spoken = "add" if constants_left < 0 else "subtract"
        verb_preposition = {
            "add": "to",
            "subtract": "from"
        }
        
        with self.voiceover(
                text=f"""
                In this equation, we are {operation_verb_spoken} {abs(constants_left)}, and to get rid of it,
                we use the opposite operation of {operation_noun_spoken}, which <bookmark mark='operation' /> is {opposite_operation_noun_spoken}.
                """
        ):
            self.wait_until_bookmark("operation")
            self.play(self.indicate(self.operations[0]))
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text=f"""
                Therefore, we are going to {opposite_operation_verb_standard_spoken} {abs(constants_left)} {verb_preposition[opposite_operation_verb_standard_spoken]} the {constants_left}.

                And if we {opposite_operation_verb_standard_spoken} {abs(constants_left)} {verb_preposition[opposite_operation_verb_standard_spoken]} one side of the equation, we must {opposite_operation_verb_standard_spoken} it {verb_preposition[opposite_operation_verb_standard_spoken]} the <bookmark mark='add' /> other side.
                """
        ):
            self.play(FadeIn(tip_2, shift=UP))

            self.wait_until_bookmark("add")
            self.play(Write(step1_tex))
            self.play(FadeOut(tip_2, shift=DOWN))
            self.wait(COMPREHENSION_PAUSE)

        operation_plus_minus_spoken = "plus" if constants_left < 0 else "minus"
        
        with self.voiceover(
                text=f"""
                Let's bring down <bookmark mark='left' /> the {coefficient}{variable_name}, and the {-constants_left} will cancel the {constants_left} giving us zero, and {constants_right} {operation_plus_minus_spoken} {abs(constants_left)} <bookmark mark='new_right' /> equals {new_right_simplified}
                """
        ):
            self.wait_until_bookmark("left")
            self.TransformThenWrite(equation_tex, step1_result, equation_step1_transform_index)

            self.wait_until_bookmark("new_right")
            self.play(Write(step1_result[0][step1_result_right_idx]))
            self.wait(COMPREHENSION_PAUSE)


        if coefficient == 1:
            with self.voiceover(f"Thus, we <bookmark mark='solution' /> have {variable_name} equals {solution} and we are done."):
                self.wait_until_bookmark("solution")
                self.play(
                    Create(self.create_surrounding_rectangle(solution_steps[-1]))
                )
                return

        with self.voiceover(
                text=f"""
                Now, we have {coefficient}{variable_name} equals {new_right_simplified} and to solve this we need to identify {variable_name}, so it must be alone in one side, therefore we need to get rid of <bookmark mark='coeff' /> the {coefficient}
                """
        ):
            self.wait_until_bookmark("coeff")
            self.play(self.indicate(step1_result[0][step1_result_coeff_idx]))
            self.wait(STANDARD_PAUSE)



        with self.voiceover(
                text=f"""
                We can get rid of the {coefficient} by doing the opposite operation.
                Since it's {coefficient} times {variable_name}, the opposite operation of times <bookmark mark='operation' /> is division.

                So now we are going to divide both sides <bookmark mark='divide' /> by {coefficient}.
                {coefficient} over {coefficient} is one, so we'll <bookmark mark='n' /> have {variable_name} alone in one side of the equal, and the other side will be {new_right_simplified} over {coefficient}, which <bookmark mark='solution' /> equals {solution}
                """
        ):
            self.wait_until_bookmark("operation")
            self.play(
                self.indicate(self.operations[1]),
                FadeIn(tip_3, shift=UP)
            )

            self.wait_until_bookmark("divide")
            self.play(FadeOut(tip_3, shift=DOWN))
            self.play(Write(step2_tex))

            self.wait_until_bookmark("n")
            self.TransformThenWrite(step1_result, step2_result, step1_step2_transform_index)

            self.wait_until_bookmark("solution")
            self.play(Write(step2_result[0][2:]))
            self.play(
                    Create(self.create_surrounding_rectangle(solution_steps[-1]))
            )
            self.wait(COMPREHENSION_PAUSE)

        with self.voiceover(
                text=f"""
                To make sure we are right, let's substitute {variable_name} equals {solution} into the <bookmark mark='equation' /> original equation.

                So we <bookmark mark='verification' /> have, {coefficient} times {solution} {'plus' if constants_left > 0 else ''} {constants_left} equals {constants_right}, which is correct.
                """
        ):
            self.play(FadeIn(tip_4, shift=UP))
            
            self.wait_until_bookmark("equation")
            self.play(self.indicate(equation_tex))

            self.wait_until_bookmark("verification")
            self.wait(COMPREHENSION_PAUSE)
            
        self.play(FadeOut(tip_4, shift=DOWN))
        
        with self.voiceover(f"There we have it, {variable_name} equals {solution}"):
            pass