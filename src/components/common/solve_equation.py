from sympy import Symbol, parse_expr, Eq, solve, Rational
from sympy.parsing.sympy_parser import T
import re

def get_reciprocal(value):
    if isinstance(value, (int, float)):
        return Rational(1, value)
    else:
        return 1 / value

def get_next_key(dictionary, current_key):
    keys = list(dictionary.keys())
    if current_key in keys:
        current_index = keys.index(current_key)
        if current_index + 1 < len(keys):  # Check if next key exists
            next_key = keys[current_index + 1]
            return next_key
    return None  # If no next key exists

def to_latex(expr_str):
    latex_expr = re.sub(
        r"(\d+|[a-zA-Z\(\)][a-zA-Z0-9\(\)]*(?:\^[0-9]+)?)/(\d+|[a-zA-Z\(\)][a-zA-Z0-9\(\)]*(?:\^[0-9]+)?)",
        r"\\frac{\1}{\2}",
        expr_str
    )
    
    return latex_expr


def find_all_substring_slices(equation, substrings=None):
    """
    Decomposes an equation string into its terms and returns their slices.
    
    Args:
        equation (str): The equation string (e.g., "-2n-2=-20")
    
    Returns:
        dict: Dictionary with terms as keys and slice objects as values
    """
    # Find the position of the equal sign
    eq_idx = equation.index('=')
    
    # Split into left and right sides
    left_side = equation[:eq_idx]
    right_side = equation[eq_idx + 1:]
    
    # Pattern to match terms:
    # - Optional + or - sign
    # - Digits followed by a letter (variable term) OR just digits (constant)
    pattern = r'([+-]?((\d*\.?\d*[a-zA-Z]?|\d+\.?\d*)(/\d*\.?\d*[a-zA-Z]?)?))'
    
    terms_dict = {}
    
    # Parse left side
    for match in re.finditer(pattern, left_side):
        term = match.group()
        start, end = match.span()
        terms_dict[term] = [slice(start, end)]
    
    # Parse right side (adjust indices for original string)
    for match in re.finditer(pattern, right_side):
        term = match.group()
        start, end = match.span()
        # Offset by position after '='
        original_start = start + eq_idx + 1
        original_end = end + eq_idx + 1
        terms_dict[term] = [slice(original_start, original_end)]
    
    return terms_dict

def get_equation_data(equation_str, variable_name):
    if "=" not in equation_str:
        raise ValueError("Equation must contain an equals sign (=)")

    left_side, right_side = equation_str.split("=")
    left_side = left_side.strip()
    right_side = right_side.strip()

    # Create symbolic variable
    var = Symbol(variable_name)
    
    # Parse both sides of the equation
    try:
        lhs = parse_expr(left_side, transformations=T[:6])
        rhs = parse_expr(right_side, transformations=T[:6])
    except Exception as e:
        raise ValueError(f"Error parsing equation: {e}")

    return (var, lhs, rhs)


def equation_formatted(equation):
    # Step 1: Remove all spaces and asterisks
    formatted_str = str(equation).replace("*", "").replace(" ", "")
    
    # Step 2: Convert patterns like "2x/3" → "2/3x"
    formatted_str = re.sub(
        r"(\d+)([a-zA-Z])/(\d+)",  # Matches "2x/3"
        r"\1/\3\2",                # Rewrites as "2/3x"
        formatted_str
    )
    
    return formatted_str

def add_sign(expression):
    expression = str(expression)
    new_expression = expression
    if expression[0] != "-":
        new_expression = "+" + expression
    return new_expression

def add_opposite_sign(expression):
    expression = str(expression)
    new_expression = expression
    if expression[0] != "-":
        new_expression = "-"
        if expression[0] == "+":
            new_expression += expression[1:]
        else:
            new_expression += expression
    else:
        new_expression = "+" + expression[1:]
        
    return new_expression


def find_equation_structure(equation_str, variable_name):
        """
        Possible equation formats - multiple variables, multiple constants (type 1):
        - constant + variable = variable + constant -> format 1
        - constant + variable = constant + variable -> format 2
        - variable + constant = variable + constant -> format 3
        - variable + constant = constant + variable -> format 4

        Possible equation formats - multiple variables, single constant (type 2):
        - constant + variable = variable -> format 1
        - variable + constant = variable -> format 2
 
        - variable = constant + variable -> format 3
        - variable = variable + constant -> format 4

        Possible equation formats - single variable, multiple constants (type 3):
        - constant + variable = constant -> format 1
        - variable + constant = constant -> format 2
        
        - constant = constant + variable -> format 3
        - constant = variable + constant -> format 4
        
        Possible equation formats - single variable, single constant:
        - constant = variable
        - variable = constant
        """
        var, lhs, rhs = get_equation_data(equation_str, variable_name)
        var_terms_left = lhs.coeff(var) * var
        const_terms_left = lhs - var_terms_left
        var_terms_right = rhs.coeff(var) * var
        const_terms_right = rhs - var_terms_right

        multiple_variables = bool(var_terms_right and var_terms_left)
        multiple_constants = bool(const_terms_right and const_terms_left)

        # Find positions of variables and constants

        equal_sign_position = equation_str.index("=")
        try:
            lhs_var_positions = equation_str.index(equation_formatted(var_terms_left))
            lhs_before_equal = lhs_var_positions != 0 and (lhs_var_positions < equal_sign_position)
        except:
            pass

        try:
            rhs_var_positions = equation_str.index(equation_formatted(var_terms_right))
            rhs_after_equal = (rhs_var_positions == equal_sign_position + 1)
        except:
            pass

        type, format = None, None
        if multiple_variables and multiple_constants:
            type = 1
            if lhs_before_equal and rhs_after_equal:
                format = 1
            elif lhs_before_equal:
                format = 2
            elif rhs_after_equal:
                format = 3
            else:
                format = 4
            return {"type": type, "format": format}

        # Type 2: multiple variables, single constant
        """
        - constant + variable = variable -> format 1
        - variable + constant = variable -> format 2

        - variable = variable + constant -> format 3
        - variable = constant + variable -> format 4
        """
        if multiple_variables:
            type = 2
            if rhs == var_terms_right:
                format = 1 if lhs_before_equal else 2
            elif lhs == var_terms_left:
                format = 3 if rhs_after_equal else 4
            return {"type": type, "format": format}

        # Type 3: single variable, multiple constants
        """
        Possible equation formats - single variable, multiple constants (type 3):
        - constant + variable = constant -> format 1
        - variable + constant = constant -> format 2
        
        - constant = variable + constant -> format 3
        - constant = constant + variable -> format 4
        """
        if multiple_constants:
            type = 3
            if rhs == const_terms_right:
                format = 1 if lhs_before_equal else 2
            elif lhs == const_terms_left:
                format = 3 if rhs_after_equal else 4
            return {"type": type, "format": format}

        # Type 4: single variable, single constant
        """
        Possible equation formats - single variable, single constant (type 4):
        - constant = variable -> format 1
        - variable = constant -> format 2
        """
        format = 1 if var_terms_right else 2
        return {"type": 4, "format": format}
        
def format_equation(lhs, rhs, var, structure: dict):
        """
        Formats the new equation based on the format type.
        """
        var_terms_left = lhs.coeff(var) * var
        const_terms_left = lhs - var_terms_left
        
        var_terms_right = rhs.coeff(var) * var
        const_terms_right = rhs - var_terms_right        

        new_var_terms_left = equation_formatted(var_terms_left - var_terms_right)
        new_var_terms_right = equation_formatted(var_terms_right - var_terms_left)

        new_const_terms_left = format_solution(const_terms_left - const_terms_right)
        new_const_terms_right = format_solution(const_terms_right - const_terms_left)

        const_terms_left = format_solution(const_terms_left)
        const_terms_right = format_solution(const_terms_right)
        
        components = {}
        type, format = structure["type"], structure["format"]
        if type == 1:
            components["var_terms_left"] = equation_formatted(var_terms_left)
            components["var_terms_right"] = equation_formatted(var_terms_right)
            components["const_terms_left"] = equation_formatted(const_terms_left)
            components["const_terms_right"] = equation_formatted(const_terms_right)

            # Add + sign to positive components
            if format == 1 or format == 3: components["const_terms_right"] = add_sign(components["const_terms_right"])
            if format == 2 or format == 4: components["var_terms_right"] = add_sign(components["var_terms_right"])
            
            if format == 1 or format == 2:
                # constant + variable = constant
                new_var_terms_left = add_sign(new_var_terms_left)
                components["var_terms_left"] = add_sign(components["var_terms_left"])
                new_equation = f"{const_terms_left}{new_var_terms_left} = {const_terms_right}"
            elif format == 3 or format == 4:
                # variable + constant = constant
                const_terms_left = add_sign(const_terms_left)
                components["const_terms_left"] = add_sign(components["const_terms_left"])
                new_equation = f"{new_var_terms_left}{const_terms_left} = {const_terms_right}"
        elif type == 2:
            components["var_terms_left"] = equation_formatted(var_terms_left)
            components["var_terms_right"] = equation_formatted(var_terms_right)

            if format == 1 or format == 2:
                # constant = variable
                new_equation = f"{const_terms_left} = {new_var_terms_right}"
                components["const_terms_left"] = equation_formatted(const_terms_left)
            elif format == 3 or format == 4:
                # variable = constant
                new_equation = f"{new_var_terms_left} = {const_terms_right}"
                components["const_terms_right"] = equation_formatted(const_terms_right)
                
            # Add + to positive terms
            if format == 1: components["var_terms_left"] = add_sign(components["var_terms_left"])
            if format == 2: components["const_terms_left"] = add_sign(components["const_terms_left"])
            if format == 3: components["const_terms_right"] = add_sign(components["const_terms_right"])
            if format == 4: components["var_terms_right"] = add_sign(components["var_terms_right"])
            
        elif type == 3:
            components["const_terms_left"] = equation_formatted(const_terms_left)
            components["const_terms_right"] = equation_formatted(const_terms_right)
            
            if format == 1 or format == 2:
                # variable = constant
                new_equation = f"{new_var_terms_left} = {new_const_terms_right}"
                components["var_terms_left"] = equation_formatted(var_terms_left)
            elif format == 3 or format == 4:
                # constant = variable
                new_equation = f"{new_const_terms_left} = {new_var_terms_right}"
                components["var_terms_right"] = equation_formatted(var_terms_right)

            # Add + the positive terms
            if format == 1: components["var_terms_left"] = add_sign(components["var_terms_left"])
            if format == 2: components["const_terms_left"] = add_sign(components["const_terms_left"])
            if format == 3: components["const_terms_right"] = add_sign(components["const_terms_right"])
            if format == 4: components["var_terms_right"] = add_sign(components["var_terms_right"])

        elif type == 4:
            # Type 4: single variable, single constant
            """
            Possible equation formats - single variable, single constant (type 4):
            - constant = variable -> format 1
            - variable = constant -> format 2
            """
            if format == 1:
                coeff = var_terms_right.coeff(var)
                new_equation = f"{format_solution(parse_expr(const_terms_left) / coeff)} = {var}"

                components["const_terms_left"] = equation_formatted(const_terms_left)
                components["var_terms_right"] = equation_formatted(var_terms_right)
            elif format == 2:
                coeff = var_terms_left.coeff(var)
                new_equation = f"{var} = {format_solution(parse_expr(const_terms_right) / coeff)}"
                
                components["const_terms_right"] = equation_formatted(const_terms_right)
                components["var_terms_left"] = equation_formatted(var_terms_left)

        return (equation_formatted(new_equation), components)

def format_solution(solution, decimal_places=2):
    """
    Formats the solution to a specified number of decimal places.
    """
    if solution == int(solution):
        return str(solution)
    else:
        formatted_solution = "{0:.{1}f}".format(solution, decimal_places)
        # Remove trailing zeros and optional decimal point
        if '.' in formatted_solution:
            formatted_solution = formatted_solution.rstrip('0').rstrip('.') if '.' in formatted_solution else formatted_solution
        return formatted_solution

def get_variable_name(equation_str):
    variables = re.findall(r'[a-zA-Z]', equation_str)
    if variables:
        variable_name = variables[0]
    else:
        raise ValueError("No variable found in equation and none provided")
    return variable_name

def solve_linear_equation(equation_str, steps: dict, components: dict):
    equation_str = str(equation_str).replace(" ", "")

    # Find variable name
    variable_name = get_variable_name(equation_str)
    
    var, lhs, rhs = get_equation_data(equation_str, variable_name)
    
    # Create the equation
    equation = Eq(lhs, rhs)

    # Solve the equation
    solution = format_solution(solve(equation, var)[0])
    if not solution:
        return {"status": "no_solution", "message": "No solution found"}

    solution_eqn_1 = f"{variable_name}={solution}"
    solution_eqn_2 = f"{solution}={variable_name}"

    if equation_str in [solution_eqn_1, solution_eqn_2]:
        steps["solution"] = equation_str

        components["solution"] = {"variable": variable_name, "solution": solution}
        return equation_str
    
    
    equation_structure = find_equation_structure(equation_str, variable_name)
    new_equation_str, type_components = format_equation(lhs, rhs, var, equation_structure)
    equation_type = equation_structure["type"]

    solve_linear_equation(new_equation_str, steps, components)
        
    if equation_type == 1 or equation_type == 2:
        steps["move_variables"] = equation_str
        components["move_variables"] = type_components
    elif equation_type == 3:
        steps["move_constants"] = equation_str
        components["move_constants"] = type_components
    elif equation_type == 4:
        steps["divide"] = equation_str
        components["divide"] = type_components
