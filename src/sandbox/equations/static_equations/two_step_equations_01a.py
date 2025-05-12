from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip

FOOTNOTE_SCALE = 0.5

def add_annotations(term_added, left_term, right_term, color=None):
    terms = VGroup(*[MathTex(rf"{term_added}").scale(FOOTNOTE_SCALE) for _ in range(2)])
    if color:
        terms.set_color(color)
        
    terms[0].next_to(left_term, DOWN)
    terms[1].next_to(right_term, DOWN)
    if terms[0].get_y() < terms[1].get_y():
        terms[1].align_to(terms[0], DOWN)
    else:
        terms[0].align_to(terms[1], DOWN)

    return terms

# Colors
VARIABLE_COLOR  = "#BB88FF"
COEFF_COLOR     = "#FF8C42"
CONSTANT_COLOR  = "#43D9A2"
TITLE_COLOR     = "#FFFFFF"
PLUS_COLOR      = "#3DCFF4"
MINUS_COLOR     = "#FF5C57"
TIMES_COLOR     = "#D77BFF"
DIVISION_COLOR  = "#FF9AC1"
ARROW_COLOR     = "#A0A0A0"
STEP_COLOR      = "#FF9AC1"

class SolveForN(MathTutorialScene):
    def construct(self):
        # Constants
        EQUATIONS_BUFF = 1.3

        # Title and Operations
        title = Tex("Solve.", color=TITLE_COLOR).to_corner(UL)
        operations_plus_minus = MathTex(r"+ \Longleftrightarrow -")
        operations_mul_div = MathTex(r"\times \Longleftrightarrow \div")
        operations = VGroup(operations_plus_minus, operations_mul_div).arrange(buff=1).to_edge(DOWN, buff=1).scale(2)
        self.apply_smart_colorize(
            operations,
            {
                "+": PLUS_COLOR,
                "-": MINUS_COLOR,
                r"\times": TIMES_COLOR,
                r"\div": DIVISION_COLOR,
                r"\Longleftrightarrow": ARROW_COLOR
            }
        )

        # Equation Steps
        equation = MathTex("4n - 26 = -2").scale(MATH_SCALE)
        step_1 = MathTex("4n = 24").scale(MATH_SCALE)
        solution = MathTex("n = 6").scale(MATH_SCALE)
        
        equations = VGroup(equation, step_1, solution).arrange(DOWN, buff=EQUATIONS_BUFF).to_edge(UP, buff=1)
        solution_rec = self.create_surrounding_rectangle(solution)
        
        # Equation data
        variable_name = "n"
        left_var_term = "4n"
        left_const_term = "-26"
        right_const_term = "-2"
        const_added = "+ 26"
        new_const= "24"
        const_divided = r"\div 4"
        solution_val = "6"
        
        
        # Original equation terms and colors 
        eqn_var_term = equation[0][search_shape_in_text(equation, MathTex(fr"{left_var_term}"))[0]]
        eqn_left_const = VGroup(
            equation[0][search_shape_in_text(equation, MathTex(fr"{left_const_term[0]}"))[0]],
            equation[0][search_shape_in_text(equation, MathTex(fr"{left_const_term[1:]}"))[0]]
        )
        eqn_right_const = VGroup(
            equation[0][search_shape_in_text(equation, MathTex(fr"{right_const_term[0]}"))[1]],
            equation[0][search_shape_in_text(equation, MathTex(fr"{right_const_term[1:]}"))[1]]
        )
        equal_sign_1 = equation[0][search_shape_in_text(equation, MathTex("="))[0]]
        
        eqn_var_term.set_color(COEFF_COLOR)
        eqn_var_term[-1].set_color(VARIABLE_COLOR)
        eqn_left_const.set_color(CONSTANT_COLOR)
        eqn_right_const.set_color(CONSTANT_COLOR)

        # Step 1 terms and colors
        step_1_var_term = step_1[0][search_shape_in_text(step_1, MathTex(fr"{left_var_term}"))[0]]
        step_1_right_const = step_1[0][search_shape_in_text(step_1, MathTex(fr"{new_const}"))[0]]
        equal_sign_2 = step_1[0][search_shape_in_text(step_1, MathTex("="))[0]]
        
        step_1_var_term.set_color(COEFF_COLOR)
        step_1_var_term[-1].set_color(VARIABLE_COLOR)
        step_1_right_const.set_color(CONSTANT_COLOR)
        
        # Solution terms and colors
        solution_var_term = solution[0][search_shape_in_text(solution, MathTex(variable_name))[0]]
        solution_term= solution[0][search_shape_in_text(solution, MathTex(rf"{solution_val}"))[0]]
        equal_sign_3 = solution[0][search_shape_in_text(solution, MathTex("="))[0]]
        
        solution_var_term.set_color(VARIABLE_COLOR)
        solution_term.set_color(CONSTANT_COLOR)

        # Annotations
        term_added = add_annotations(const_added, eqn_left_const, eqn_right_const, CONSTANT_COLOR)
        term_divided = add_annotations(const_divided, step_1_var_term, step_1_right_const, COEFF_COLOR)

        # Transformations
        transform_list_1 = [
            [eqn_var_term, equal_sign_1],
            [step_1_var_term, equal_sign_2],
        ]
        fade_in_list_1 = [step_1_right_const]
        
        transform_list_2 = [
            [step_1_var_term[-1], equal_sign_2],
            [solution_var_term, equal_sign_3],
        ]
        fade_in_list_2 = [solution_term]
        
        # Tips
        tip_1 = QuickTip(
            "Get rid of plus/minus before multiply/divide",
            color_map={
                "plus": PLUS_COLOR,
                "minus": MINUS_COLOR,
                "multiply": TIMES_COLOR,
                "divide": DIVISION_COLOR,
            },
        ).to_corner(DR)
        
        tip_2 = QuickTip(
            r"\textbf{Step 1}: Get rid of $-26$ by adding $26$ to both sides",
            color_map={
                rf"{left_const_term}": CONSTANT_COLOR,
                rf"{left_const_term[1:]}": CONSTANT_COLOR,
            },
        ).to_corner(DR)
        tip_3 = QuickTip(
            r"\textbf{Step 2}: Get rid of $4$ by dividing both sides by $4$",
            color_map={
                "4": COEFF_COLOR,
            },

        ).to_corner(DL)
        
        self.play(FadeIn(title, operations, equation))
        self.wait()
        self.play(FadeIn(tip_1, shift=UP))
        self.wait()
        self.play(FadeOut(tip_1, shift=DOWN))
        self.wait()
        
        self.play(FadeIn(tip_2, shift=UP), self.indicate(operations[0]))
        self.wait()
        self.play(FadeIn(term_added))
        self.wait()
        self.play(FadeOut(tip_2, shift=DOWN))
        self.play(
            *[
                ReplacementTransform(source.copy(), target)
                for source, target in zip(*transform_list_1)
                if source and target
            ],
        )
        self.play(FadeIn(*fade_in_list_1))
        self.wait()

        self.play(FadeIn(tip_3, shift=UP), self.indicate(operations[1]))
        self.wait()
        self.play(FadeIn(term_divided))
        self.wait()
        self.play(FadeOut(tip_3, shift=DOWN))
        self.play(
            *[
                ReplacementTransform(source.copy(), target)
                for source, target in zip(*transform_list_2)
                if source and target
            ],
        )
        self.play(FadeIn(*fade_in_list_2))
        self.play(Create(solution_rec))
        self.wait(2)