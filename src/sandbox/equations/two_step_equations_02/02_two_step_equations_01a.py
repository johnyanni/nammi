from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.solve_equation import *
from sympy import symbols, Eq, solve, simplify, parse_expr



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

FOOTNOTE_SCALE = 0.5

"""
To write fractions, write the fraction before the variable:
- 2/3x (not 2x/3)
"""
# equation_str = "-y/3-4=3"
# equation_str = "0.3x-4.3=2"
# equation_str = "-260 - 40n = 400"
# equation_str = "6.3 = 2.1z"
# equation_str = "2n = -4n + 12"
# equation_str = "-3n + 12 = -11 + 2n"
# equation_str = "-3 + 12n = -11n + 2"
equation_str = "4/5x - 9 = -1"

steps = {}
all_components = {}
solve_linear_equation(equation_str.replace(" ", ""), steps, all_components)


class SolvingLinearEquationTemplate(MathTutorialScene):
    def process_for_transform(self, transform_list):
        sources, targets = transform_list
        processed_sources = []
        processed_targets = []

        for source, target in zip(sources, targets):
            if not (source and target):
                continue
            
            source_len, target_len = len(source), len(target)

            if source_len == target_len:
                processed_sources.append(source)
                processed_targets.append(target)
            else:
                # Trim the longer sequence to match the shorter one
                min_len = min(source_len, target_len)
                processed_sources.append(source[1:] if source_len > min_len else source)
                processed_targets.append(target[1:] if target_len > min_len else target)

        return [processed_sources, processed_targets]

    def apply_equation_coloring(self, equation, equation_str, components, variable_name):
        left_var = components.get("var_terms_left", None)
        right_var = components.get("var_terms_right", None)
        left_const = components.get("const_terms_left", None)
        right_const = components.get("const_terms_right", None)
        variable = components.get("variable", None)
        solution = components.get("solution", None)
        
        components_idx = find_all_substring_slices(equation_str)
        try:
            equation[0][components_idx[left_var][0]].set_color(COEFF_COLOR)
        except:
            pass
        try:
            equation[0][components_idx[right_var][0]].set_color(COEFF_COLOR)
        except:
            pass
        try:
            equation[0][components_idx[left_const][0]].set_color(CONSTANT_COLOR)
        except:
            pass
        try:
            equation[0][components_idx[right_const][0]].set_color(CONSTANT_COLOR)
        except: 
            pass
        try:
            equation[0][components_idx[solution][0]].set_color(WHITE)
        except: 
            pass
        
        SmartColorizeStatic(equation, {variable_name: VARIABLE_COLOR})

    def add_annotations(self, equation, equation_str, term_added, left_term_idx, right_term_idx):
        terms = VGroup(*[MathTex(rf"{to_latex(term_added)}").scale(FOOTNOTE_SCALE) for _ in range(2)])

        variable_name = get_variable_name(equation_str)

        equation_type = find_equation_structure(equation_str, variable_name)["type"]

        for term in terms:
            if equation_type in [1, 2]:
                idx = str(term_added).index(variable_name)
                term[0][idx].set_color(VARIABLE_COLOR)
                term[0][:idx].set_color(COEFF_COLOR)
                term[0][idx+1:].set_color(COEFF_COLOR) # For fractions, color before and after the variable
            elif equation_type == 3:
                term.set_color(CONSTANT_COLOR)
            elif equation_type == 4:
                term.set_color(COEFF_COLOR)

        terms[0].next_to(equation[0][left_term_idx], DOWN)
        terms[1].next_to(equation[0][right_term_idx], DOWN)
        if terms[0].get_y() < terms[1].get_y():
            terms[1].align_to(terms[0], DOWN)
        else:
            terms[0].align_to(terms[1], DOWN)

        return terms

    def get_components(self, equation, equation_str, components):
        components_idx = find_all_substring_slices(equation_str)

        left_var_str = components.get("var_terms_left", None)
        right_var_str = components.get("var_terms_right", None)
        left_const_str = components.get("const_terms_left", None)
        right_const_str = components.get("const_terms_right", None)
        equal_sign = equation_str.index("=")
        
        try:
            left_var_idx = components_idx[left_var_str][0]
            left_var = equation[0][left_var_idx]
        except:
            left_var_idx = None
            left_var = None
        try:
            right_var_idx = components_idx[right_var_str][0]
            right_var = equation[0][right_var_idx]
        except:
            right_var_idx = None
            right_var = None
        
        try:
            left_const_idx = components_idx[left_const_str][0]
            left_const = equation[0][left_const_idx]
        except:
            left_const_idx = None
            left_const = None

        try:
            right_const_idx = components_idx[right_const_str][0]
            right_const = equation[0][right_const_idx]
        except:
            right_const_idx = None
            right_const = None

        return {
            "str": (left_var_str, right_var_str, left_const_str, right_const_str),
            "idx": (left_var_idx, right_var_idx, left_const_idx, right_const_idx),
            "display": (left_var, right_var, left_const, right_const),
            "equal_sign": equation[0][equal_sign]
        }
        
    def type_1_voiceover(
            self,
            equation,
            equation_str,
            components,
            eqn_type,
            eqn_format,
            next_equation,
            next_equation_str,
            next_components
    ):
        # Current equation data
        components_dict = self.get_components(equation, equation_str, components)

        left_var_str, right_var_str, left_const_str, right_const_str = components_dict["str"]
        left_var_idx, right_var_idx, left_const_idx, right_const_idx = components_dict["idx"]
        left_var, right_var, left_const, right_const = components_dict["display"]
        equal_sign = components_dict["equal_sign"]

        # Next equation data
        next_components_dict = self.get_components(next_equation, next_equation_str, next_components)

        next_left_var_str, next_right_var_str, next_left_const_str, next_right_const_str = next_components_dict["str"]
        next_left_var_idx, next_right_var_idx, next_left_const_idx, next_right_const_idx = next_components_dict["idx"]
        next_left_var, next_right_var, next_left_const, next_right_const = next_components_dict["display"]
        next_equal_sign = next_components_dict["equal_sign"]

        # Transform list
        transform_list = self.process_for_transform([
            [left_const, right_const, equal_sign],
            [next_left_const, next_right_const, next_equal_sign]
        ])
        
        # Move variables annotations
        if eqn_type == 2 and eqn_format in [1, 2]:
            variable_added = add_opposite_sign(left_var_str)
        else:
            variable_added = add_opposite_sign(right_var_str)
        annotations = self.add_annotations(equation, equation_str, variable_added, left_var_idx, right_var_idx)

        # Shift the next equation if the variable_added is a fraction
        if "/" in variable_added:
            next_equation.next_to(annotations, DOWN, buff=0.65)

        # Animation        
        self.play(FadeIn(equation))
        
        # Add/substract
        self.play(
            FadeIn(annotations[0])
        )
        self.wait()
        self.play(
            FadeIn(annotations[1])
        )
        self.wait()

        # Transform to next equation
        self.play(
            *[
                ReplacementTransform(source.copy(), target)
                for source, target in zip(*transform_list)
                if source and target
            ],
        )
        self.play(FadeIn(*[term for term in [next_left_var, next_right_var] if term]),)
        
    def type_3_voiceover(
            self,
            equation,
            equation_str,
            components,
            eqn_type,
            eqn_format,
            next_equation,
            next_equation_str,
            next_components,
            order
    ):
        # Current equation data
        components_dict = self.get_components(equation, equation_str, components)

        left_var_str, right_var_str, left_const_str, right_const_str = components_dict["str"]
        left_var_idx, right_var_idx, left_const_idx, right_const_idx = components_dict["idx"]
        left_var, right_var, left_const, right_const = components_dict["display"]
        equal_sign = components_dict["equal_sign"]
        
        # Next equation data
        next_components_dict = self.get_components(next_equation, next_equation_str, next_components)

        next_left_var_str, next_right_var_str, next_left_const_str, next_right_const_str = next_components_dict["str"]
        next_left_var_idx, next_right_var_idx, next_left_const_idx, next_right_const_idx = next_components_dict["idx"]
        next_left_var, next_right_var, next_left_const, next_right_const = next_components_dict["display"]
        next_equal_sign = next_components_dict["equal_sign"]

        # Transform list
        transform_list = self.process_for_transform([
            [left_var, right_var, equal_sign],
            [next_left_var, next_right_var, next_equal_sign]
        ])
                                                    
        
        # Move constants annotations
        if eqn_format in [1, 2]:
            constant_added = add_opposite_sign(left_const_str)
        else:
            constant_added = add_opposite_sign(right_const_str)
        annotations = self.add_annotations(equation, equation_str, constant_added, left_const_idx, right_const_idx)

        # Shift the next equation if the constant_added is a fraction
        if "/" in constant_added:
            next_equation.next_to(annotations, DOWN, buff=0.65)

        if order == 1:
            self.play(FadeIn(equation))
            self.wait()
        self.play(FadeIn(annotations))
        self.wait()
        # Transform to next equation
        self.play(
            *[
                ReplacementTransform(source.copy(), target)
                for source, target in zip(*transform_list)
                if source and target
            ],
        )
        self.play(FadeIn(*[term for term in [next_left_const, next_right_const] if term]),)

    def type_4_voiceover(
            self,
            equation,
            equation_str,
            components,
            eqn_type,
            eqn_format,
            next_equation,
            next_equation_str,
            next_components,
            order
    ):
        # Current equation data
        components_idx = find_all_substring_slices(equation_str)

        variable_name = get_variable_name(equation_str)
        if eqn_format == 2:
            # variable_term = constant
            variable_term_str = components.get("var_terms_left", None)
            const_str = components.get("const_terms_right", None)
            
            
            variable_term_idx = components_idx[variable_term_str][0]
            const_idx = components_idx[const_str][0]
            
            variable_term = equation[0][variable_term_idx]
            const = equation[0][const_idx]
        elif eqn_format == 1:
            variable_term_str = components.get("var_terms_right", None)
            const_str = components.get("const_terms_left", None)
            
            variable_term_idx = components_idx[variable_term_str][0]
            const_idx = components_idx[const_str][0]
            
            variable_term = equation[0][variable_term_idx]
            const = equation[0][const_idx]

        if "/" in variable_term_str:
            coeff_str = parse_expr(variable_term_str, transformations=T[:6]).coeff(variable_name)
            divide_str = f"\\times {get_reciprocal(coeff_str)}"
        else:
            coeff_str = format_solution(parse_expr(variable_term_str, transformations=T[:6]).coeff(variable_name))
            divide_str = f"\\div {coeff_str}"
    
        variable = equation[0][search_shape_in_text(equation, MathTex(variable_name))[0]]
        equal_sign = equation[0][equation_str.index("=")]

        # Next equation data
        next_equation_components = find_all_substring_slices(next_equation_str)
        solution_str = all_components["solution"]["solution"]
        
        next_variable = next_equation[0][next_equation_components[variable_name][0]]
        next_equal = next_equation[0][next_equation_str.index("=")]
        solution = next_equation[0][next_equation_components[solution_str][0]]
        
        # Divide annotations
        annotations = self.add_annotations(equation, equation_str, divide_str, variable_term_idx, const_idx)

        # Shift the next equation if the divide_str is a fraction
        if "/" in divide_str:
            next_equation.next_to(annotations, DOWN, buff=0.65)

        if order == 1:
            self.play(FadeIn(equation))
            self.wait()
        self.play(FadeIn(annotations))
        self.wait()
        # Transform to next equation
        self.play(
            *[
                ReplacementTransform(source.copy(), target)
                for source, target in zip([variable, equal_sign], [next_variable, next_equal])
                if source and target
            ],
        )
        self.play(FadeIn(solution))

    def solution_voiceover(self, equation):
        self.play(FadeIn(equation))
    
    def construct(self):
        # Title and Operations
        title = Tex("Solve.", color=TITLE_COLOR).to_corner(UL)
        operations_plus_minus = MathTex(r"+ \Longleftrightarrow -")
        operations_mul_div = MathTex(r"\times \Longleftrightarrow \div")
        operations = VGroup(operations_plus_minus, operations_mul_div).arrange(buff=1).to_edge(DOWN, buff=1).scale(2)
        
        # Apply coloring to each operation separately
        self.apply_smart_colorize(
            operations_plus_minus,
            {
                "+": PLUS_COLOR,
                "-": MINUS_COLOR,
                r"\Longleftrightarrow": ARROW_COLOR
            }
        )
        
        self.apply_smart_colorize(
            operations_mul_div,
            {
                r"\times": TIMES_COLOR,
                r"\div": DIVISION_COLOR,
                r"\Longleftrightarrow": ARROW_COLOR
            }
        )

        # Equations 
        equations = {label: MathTex(fr"{to_latex(equation)}").scale(MATH_SCALE) for label, equation in reversed(steps.items())}
        equations_group = VGroup(*list(equations.values())).arrange(DOWN, buff=1).to_edge(UP, buff=1)
        variable_name = get_variable_name(equation_str)

        # Colors
        for equation in equations:
            try:
                self.apply_equation_coloring(equations[equation], steps[equation], all_components[equation], variable_name)
            except:
                pass

        self.play(FadeIn(title, operations))
        for i, equation in enumerate(equations):
            order = i + 1
            if equation == "solution":
                continue

            equation_structure = find_equation_structure(steps[equation], variable_name)
            equation_type, equation_format = equation_structure["type"], equation_structure["format"]
            next_equation = get_next_key(equations, equation)
            if equation_type == 1 or equation_type == 2:
                self.type_1_voiceover(
                    equations[equation], steps[equation], all_components[equation], equation_type, equation_format,
                    equations[next_equation], steps[next_equation], all_components[next_equation]
                )
            elif equation_type == 3:
                self.type_3_voiceover(
                    equations[equation], steps[equation], all_components[equation], equation_type, equation_format,
                    equations[next_equation], steps[next_equation], all_components[next_equation], order
                )
            elif equation_type == 4:
                self.type_4_voiceover(
                    equations[equation], steps[equation], all_components[equation], equation_type, equation_format,
                    equations[next_equation], steps[next_equation], all_components[next_equation], order
                )

        self.play(Create(self.create_surrounding_rectangle(equations["solution"])))
        
        self.wait(5)