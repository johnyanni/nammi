"""Tutorial on expanding binomials using the FOIL method."""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.components.common.smart_tex import *
from src.components.common.quick_tip import QuickTip

# TEMPLATE PARAMETERS
TEMPLATE_PARAMS = {
    # Core expression values
    "expression": {
        "first_binomial": "2m + 1",       # First binomial expression
        "second_binomial": "3n - 4",      # Second binomial expression
        "formatted": "(2m + 1)(3n - 4)",  # Full formatted expression
    },
    
    # Terms to find in the expression
    "terms": {
        "first_term_1": "2m",            # First term of first binomial
        "second_term_1": "1",            # Second term of first binomial
        "first_term_2": "3n",            # First term of second binomial
        "second_term_2": "4",            # Second term of second binomial (without sign)
        "second_term_2_sign": "-",       # Sign of second term in second binomial
    },
    
    # FOIL calculation results
    "results": {
        "first": {
            "result": "6mn",             # First terms multiplied: (2m)(3n)
            "color": "RED",              # Color for this result term
            "voiceover": "First, we multiply the first terms of each binomial, so 2m times 3n gives us 6mn"
        },
        "outside": {
            "result": "-8m",             # Outside terms multiplied: (2m)(-4)
            "color": "BLUE",             # Color for this result term
            "voiceover": "Next, we multiply the outside terms; 2m times negative 4 gives us negative 8m"
        },
        "inside": {
            "result": "3n",              # Inside terms multiplied: (1)(3n)
            "color": "RED",              # Color for this result term
            "voiceover": "Now, we multiply the inside terms; 1 times 3n gives us 3n"
        },
        "last": {
            "result": "-4",              # Last terms multiplied: (1)(-4)
            "color": "GREEN",            # Color for this result term
            "voiceover": "Finally, we multiply the last terms; 1 times negative 4 gives us negative 4"
        }
    },
    
    # The expanded expression and final steps
    "expansion": {
        "expanded": "6mn - 8m + 3n - 4",  # The expanded expression
        "has_like_terms": False,          # Whether there are like terms to combine
        "final": "6mn - 8m + 3n - 4",     # The final answer (same if no like terms)
        "voiceover": "Our final step is to combine like terms, but since there are no like terms in this expression, the expression is already in its simplest form."
    },
    
    # UI elements and styling
    "ui": {
        "title": "Expand & Simplify",
        "title_font_size": 32,
        "expression_scale": 0.9,
        "arrow_color": "RED",
        "tip_length": 0.3,
        "foil_color": "GREEN"
    },
    
    # Tips content
    "tips": {
        "tip_1": "Step 1: Multiply the First term then the Outside term.",
        "tip_2": "Step 2: Multiply the Inside term then the Last term."
    },
    
    # Introduction voiceover
    "intro_voiceover": """
        Let's explore how to expand and simplify the following binomial expression using the FOIL method.
        The FOIL method is a handy rule for multiplying two binomials. The F stands for first terms,
        The O stands for outside terms, the I stands for inside terms and the L stands for last terms.
        We'll apply this method on the following expression.
    """
}

class FOILMethod(VoiceoverScene):
    """A tutorial that teaches how to expand binomials using the FOIL method."""

    def find_term(self, expression, term):
        """Helper function to safely find terms in expressions."""
        try:
            indices = search_shape_in_text(expression, MathTex(term))
            if indices and len(indices) > 0:
                return expression[0][indices[0]]
            else:
                # Fallback if term not found
                print(f"Warning: Term '{term}' not found in expression")
                return None
        except Exception as e:
            print(f"Error finding term '{term}': {e}")
            return None

    def get_safe_position(self, term_mobject, position="center"):
        """Get a safe position from a term, with fallbacks."""
        if term_mobject is None:
            # Return a default position as fallback
            return ORIGIN
            
        try:
            if position == "top":
                return term_mobject.get_top() + UP * 0.1
            elif position == "bottom":
                return term_mobject.get_bottom() + DOWN * 0.1
            else:  # center or default
                return term_mobject.get_center()
        except Exception as e:
            print(f"Error getting position: {e}")
            return ORIGIN

    def construct(self):
        # Setup scene settings
        self.set_speech_service(GTTSService())
        
        # Define constants from parameters
        EXP_SCALE = TEMPLATE_PARAMS["ui"]["expression_scale"]
        TIP_LENGTH = TEMPLATE_PARAMS["ui"]["tip_length"]
        ARROW_COLOR = eval(TEMPLATE_PARAMS["ui"]["arrow_color"])
        TITLE_FONT_SIZE = TEMPLATE_PARAMS["ui"]["title_font_size"]
        FOIL_COLOR = eval(TEMPLATE_PARAMS["ui"]["foil_color"])
        
        # Create title
        title = Text(TEMPLATE_PARAMS["ui"]["title"], font_size=TITLE_FONT_SIZE).to_edge(UP)
        
        # Create FOIL example
        example = MathTex(
            r"(a + b)(c + d) = \text{FOIL}"
        ).scale(EXP_SCALE).shift((DOWN + LEFT) * 3)
        SmartColorizeStatic(example, {"FOIL": FOIL_COLOR})
        
        # Get individual terms for arrows - using safe methods
        a = self.find_term(example, "a")
        b = self.find_term(example, "b")
        c = self.find_term(example, "c")
        d = self.find_term(example, "d")

        # Get positions for arrows, with safety checks
        a_pos = self.get_safe_position(a, "top") if a else LEFT * 1.5 + UP * 0.3
        b_pos = self.get_safe_position(b, "bottom") if b else LEFT * 0.8 + DOWN * 0.3
        c_pos = self.get_safe_position(c, "top") if c else RIGHT * 0.8 + UP * 0.3
        d_pos = self.get_safe_position(d, "bottom") if d else RIGHT * 1.5 + DOWN * 0.3

        # Create arrows for FOIL demonstration
        arrow_a_to_c = CurvedArrow(a_pos, c_pos, angle=-TAU/4, tip_length=TIP_LENGTH)
        arrow_a_to_d = CurvedArrow(a_pos, d_pos, angle=-TAU/4, tip_length=TIP_LENGTH)
        arrow_b_to_c = CurvedArrow(b_pos, c_pos, angle=TAU/4, tip_length=TIP_LENGTH)
        arrow_b_to_d = CurvedArrow(b_pos, d_pos, angle=TAU/3, tip_length=TIP_LENGTH)

        VGroup(arrow_a_to_c, arrow_a_to_d, arrow_b_to_c, arrow_b_to_d).set_color(ARROW_COLOR)

        # Create FOIL breakdown
        foil_breakdown = VGroup(
            *[
                Text(t, font_size=26)
                for t in ["First", "Outside", "Inside", "Last"]
            ]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(example, UP * 1.5).shift(RIGHT * 2.5)

        for t in foil_breakdown:
            t[0].set_color(FOIL_COLOR)
            
        # Create the expression to be expanded
        expression = MathTex(TEMPLATE_PARAMS["expression"]["formatted"], color=BLUE).scale(EXP_SCALE).next_to(title, DOWN * 4)
        
        # Highlight the operation symbols
        SmartColorizeStatic(
            expression,
            {
                "+": WHITE,
                "-": WHITE
            }
        )
        
        # Find the terms in our specific expression using safe methods
        term_first_1 = self.find_term(expression, TEMPLATE_PARAMS["terms"]["first_term_1"])
        term_second_1 = self.find_term(expression, TEMPLATE_PARAMS["terms"]["second_term_1"])
        term_first_2 = self.find_term(expression, TEMPLATE_PARAMS["terms"]["first_term_2"])
        
        # Search for the second term of second binomial (may need special handling for negative terms)
        second_term_2 = TEMPLATE_PARAMS["terms"]["second_term_2"]
        term_second_2 = self.find_term(expression, second_term_2)
        
        # Get positions for our expression's terms
        term1_pos = self.get_safe_position(term_first_1, "top") if term_first_1 else LEFT * 2 + UP * 0.5
        term2_pos = self.get_safe_position(term_first_2, "top") if term_first_2 else RIGHT * 0.5 + UP * 0.5
        term3_pos = self.get_safe_position(term_second_1, "bottom") if term_second_1 else LEFT * 2 + DOWN * 0.5
        term4_pos = self.get_safe_position(term_second_2, "bottom") if term_second_2 else RIGHT * 0.5 + DOWN * 0.5
        
        # Create arrows for our specific FOIL operations
        arrow_first = CurvedArrow(
            term1_pos,
            term2_pos,
            angle=-TAU/4,
            tip_length=TIP_LENGTH,
            color=eval(TEMPLATE_PARAMS["results"]["first"]["color"])
        )
        
        arrow_outside = CurvedArrow(
            term1_pos,
            term4_pos,
            angle=-TAU/4,
            tip_length=TIP_LENGTH,
            color=eval(TEMPLATE_PARAMS["results"]["outside"]["color"])
        )
        
        arrow_inside = CurvedArrow(
            term3_pos,
            term2_pos,
            angle=TAU/4,
            tip_length=TIP_LENGTH,
            color=eval(TEMPLATE_PARAMS["results"]["inside"]["color"])
        )
        
        arrow_last = CurvedArrow(
            term3_pos,
            term4_pos,
            angle=TAU/3,
            tip_length=TIP_LENGTH,
            color=eval(TEMPLATE_PARAMS["results"]["last"]["color"])
        )
        
        # Create the expanded expression
        expanded_expression = MathTex(TEMPLATE_PARAMS["expansion"]["expanded"]).scale(EXP_SCALE).next_to(expression, DOWN * 4)
        
        # Color the expanded terms
        color_dict = {}
        for key, value in TEMPLATE_PARAMS["results"].items():
            color_dict[value["result"]] = eval(value["color"])
            
        # Apply coloring to the expanded expression
        SmartColorizeStatic(expanded_expression, color_dict)
        
        # Parse the expanded expression to find individual terms
        expanded_terms = []
        
        # Helper function to extract terms from expanded expression
        def extract_term(expression, term_text, is_first=False):
            try:
                # For the first term, just look for the term itself without a sign
                if is_first:
                    term_shapes = search_shape_in_text(expression, MathTex(term_text))
                    if term_shapes and len(term_shapes) > 0:
                        return expression[0][term_shapes[0]]
                    return None
                
                # For other terms, need to include the sign
                sign = "+" if term_text[0] != "-" else "-"
                term = term_text if term_text[0] != "-" else term_text[1:]
                
                # Find the sign and term separately
                sign_shapes = search_shape_in_text(expression, MathTex(sign))
                term_shapes = search_shape_in_text(expression, MathTex(term))
                
                if sign_shapes and term_shapes and len(sign_shapes) > 0 and len(term_shapes) > 0:
                    sign_mobject = expression[0][sign_shapes[0]]
                    term_mobject = expression[0][term_shapes[0]]
                    return VGroup(sign_mobject, term_mobject)
                
                return None
            except Exception as e:
                print(f"Error extracting term {term_text}: {e}")
                return None
        
        # Extract terms from the expanded expression
        expanded_parts = TEMPLATE_PARAMS["expansion"]["expanded"].split(" ")
        
        # First term is special (no sign)
        first_term = extract_term(expanded_expression, expanded_parts[0], is_first=True)
        if first_term:
            expanded_terms.append(first_term)
        
        # Process remaining terms with their signs
        current_term = ""
        for i in range(1, len(expanded_parts)):
            if expanded_parts[i] in ["+", "-"]:
                if current_term:
                    term = extract_term(expanded_expression, current_term)
                    if term:
                        expanded_terms.append(term)
                current_term = expanded_parts[i] + " "
            else:
                current_term += expanded_parts[i] + " "
        
        # Don't forget the last term
        if current_term:
            term = extract_term(expanded_expression, current_term.strip())
            if term:
                expanded_terms.append(term)
        
        # If we couldn't extract terms properly, use a fallback approach
        if not expanded_terms or len(expanded_terms) < 2:
            print("Warning: Could not extract terms properly. Using fallback.")
            expanded_terms = [
                expanded_expression[0][search_shape_in_text(expanded_expression, MathTex(TEMPLATE_PARAMS["results"]["first"]["result"]))[0]],
                expanded_expression[0][search_shape_in_text(expanded_expression, MathTex(TEMPLATE_PARAMS["results"]["outside"]["result"].replace("-", "")))[0]],
                expanded_expression[0][search_shape_in_text(expanded_expression, MathTex(TEMPLATE_PARAMS["results"]["inside"]["result"].replace("-", "")))[0]],
                expanded_expression[0][search_shape_in_text(expanded_expression, MathTex(TEMPLATE_PARAMS["results"]["last"]["result"].replace("-", "")))[0]]
            ]
        
        # Create rectangle around the final expanded expression
        expanded_exp_rectangle = SurroundingRectangle(expanded_expression)

        # Create tips
        tip_1 = QuickTip(TEMPLATE_PARAMS["tips"]["tip_1"]).to_corner(DL)
        SmartColorizeStatic(tip_1[1][0], {"Step 1:": BLACK})

        tip_2 = QuickTip(TEMPLATE_PARAMS["tips"]["tip_2"]).to_corner(DL)
        SmartColorizeStatic(tip_2[1][0], {"Step 2:": BLACK})

        # Animation sequence
        self.add(title)
        with self.voiceover(text=TEMPLATE_PARAMS["intro_voiceover"]):
            self.play(FadeIn(expression, example, arrow_a_to_c, arrow_a_to_d, arrow_b_to_c, arrow_b_to_d, foil_breakdown))

        # Extract terms based on the expansion parameters
        # Each term needs its own extraction and handling to ensure we don't miss anything
        result_terms = []
        
        # Try to find each result term
        for i, key in enumerate(["first", "outside", "inside", "last"]):
            result = TEMPLATE_PARAMS["results"][key]["result"]
            
            # For first term, don't look for a sign
            if i == 0:
                shapes = search_shape_in_text(expanded_expression, MathTex(result))
                if shapes and len(shapes) > 0:
                    result_terms.append(expanded_expression[0][shapes[0]])
                else:
                    # Fallback
                    print(f"Warning: Could not find term {result}. Using fallback.")
                    result_terms.append(expanded_expression)
            else:
                # For other terms, include the sign if present
                sign = "+" if not result.startswith("-") else "-"
                term = result if not result.startswith("-") else result[1:]
                
                sign_shapes = search_shapes_in_text(expanded_expression, [MathTex(sign)])
                term_shapes = search_shape_in_text(expanded_expression, MathTex(term))
                
                if len(sign_shapes) > i-1 and len(term_shapes) > 0:
                    sign_mobject = expanded_expression[0][sign_shapes[i-1]]
                    term_mobject = expanded_expression[0][term_shapes[0]]
                    result_terms.append(VGroup(sign_mobject, term_mobject))
                else:
                    # Fallback
                    print(f"Warning: Could not find term {result}. Using fallback.")
                    dummy = MathTex(result).scale(EXP_SCALE)
                    dummy.next_to(expanded_expression, DOWN * 0.5)
                    dummy.set_opacity(0)
                    self.add(dummy)
                    result_terms.append(dummy)

        # Animation sequence
        with self.voiceover(TEMPLATE_PARAMS["results"]["first"]["voiceover"]):
            self.play(GrowFromPoint(arrow_first, term1_pos))
            self.play(Write(result_terms[0]))

        with self.voiceover(TEMPLATE_PARAMS["results"]["outside"]["voiceover"]):
            self.play(FadeIn(tip_1, shift=UP))
            self.play(GrowFromPoint(arrow_outside, term1_pos))
            self.play(Write(result_terms[1]))
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(TEMPLATE_PARAMS["results"]["inside"]["voiceover"]):
            self.play(GrowFromPoint(arrow_inside, term3_pos))
            self.play(Write(result_terms[2]))

        with self.voiceover(TEMPLATE_PARAMS["results"]["last"]["voiceover"]):
            self.play(GrowFromPoint(arrow_last, term3_pos), FadeIn(tip_2, shift=UP))
            self.play(Write(result_terms[3]))
        self.play(FadeOut(tip_2, shift=DOWN))

        with self.voiceover(text=TEMPLATE_PARAMS["expansion"]["voiceover"]):
            pass
        self.play(Create(expanded_exp_rectangle))

        with self.voiceover("So this is our final answer after expanding the expression."):
            pass
        self.wait(2)