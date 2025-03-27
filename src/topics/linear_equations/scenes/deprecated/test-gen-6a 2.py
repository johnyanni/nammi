"""Tutorial on expanding binomials using the FOIL method."""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.components.common.smart_tex import *
from src.components.common.quick_tip import QuickTip

# Template variables - EDIT THESE FOR EACH NEW EXAMPLE
EXPRESSION_TEXT = "(2m + 1)(3n - 4)"  # The expression to expand
EXPRESSION_COLOR = BLUE              # Color for the main expression

# Terms from first binomial
TERM_1_TEXT = "2m"  # First term of first binomial
TERM_2_TEXT = "1"   # Second term of first binomial

# Terms from second binomial
TERM_3_TEXT = "3n"  # First term of second binomial
TERM_4_TEXT = "4"   # Second term of second binomial (without sign)
TERM_4_SIGN = "-"   # Sign for second term of second binomial

# Expanded terms
EXPANDED_TERM_1 = "6mn"    # First term result (F in FOIL)
EXPANDED_TERM_2 = "-8m"    # Second term result (O in FOIL)
EXPANDED_TERM_3 = "3n"     # Third term result (I in FOIL)
EXPANDED_TERM_4 = "-4"     # Fourth term result (L in FOIL)

# Terms coloring
TERM_1_COLOR = RED      # Color for first term result
TERM_2_COLOR = BLUE     # Color for second term result
TERM_3_COLOR = RED      # Color for third term result
TERM_4_COLOR = GREEN    # Color for fourth term result

# Expanded expression
EXPANDED_EXPRESSION = "6mn - 8m + 3n - 4"  # The complete expanded expression
HAS_LIKE_TERMS = False                      # Whether there are like terms to combine
FINAL_EXPRESSION = "6mn - 8m + 3n - 4"      # Final answer after combining like terms

# UI settings
TITLE_TEXT = "Expand & Simplify"
TITLE_FONT_SIZE = 32
EXPRESSION_SCALE = 0.9
ARROW_COLOR = RED
TIP_LENGTH = 0.3
BACKGROUND_COLOR = "#121212"
FOIL_COLOR = GREEN

# Voiceovers
INTRO_VOICEOVER = """
    Let's explore how to expand and simplify the following binomial expression using the FOIL method.
    The FOIL method is a handy rule for multiplying two binomials. The F stands for first terms,
    The O stands for outside terms, the I stands for inside terms and the L stands for last terms.
    We'll apply this method on the following expression.
"""
TERM_1_VOICEOVER = "First, we multiply the first terms of each binomial, so 2 'm' times 3 n gives us the term 6 'm' n"
TERM_2_VOICEOVER = "Next, we multiply the outside terms; 2 'm' times negative 4 gives us the term negative 8 'm'"
TERM_3_VOICEOVER = "Now, we multiply the inside terms; 1 times 3 n gives us 3 n"
TERM_4_VOICEOVER = "Finally, we multiply the last terms; 1 times negative 4 gives us negative 4"
FINAL_VOICEOVER = "Our final step is to combine like terms, but since there are no like terms in this expression, the expression is already in its simplest form."

# Tips content
TIP_1_TEXT = "Step 1: Multiply the First term then the Outside term."
TIP_2_TEXT = "Step 2: Multiply the Inside term then the Last term."

class FOILMethod(VoiceoverScene):
    """A tutorial that teaches how to expand binomials using the FOIL method."""

    def construct(self):
        # Setup scene settings

            
        self.set_speech_service(GTTSService())
        
        # Create title
        title = Text(TITLE_TEXT, font_size=TITLE_FONT_SIZE).to_edge(UP)
        
        # Create FOIL example
        example = MathTex(
            r"(a + b)(c + d) = \text{FOIL}"
        ).scale(EXPRESSION_SCALE).shift((DOWN + LEFT) * 3)
        SmartColorizeStatic(example, {"FOIL": FOIL_COLOR})
        
        # Get individual terms for arrows
        a = example[0][search_shape_in_text(example, MathTex("a"))[0]]
        b = example[0][search_shape_in_text(example, MathTex("b"))[0]]
        c = example[0][search_shape_in_text(example, MathTex("c"))[0]]
        d = example[0][search_shape_in_text(example, MathTex("d"))[0]]

        # Create arrows for FOIL demonstration
        arrow_a_to_c = CurvedArrow(a.get_top(), c.get_top(), angle=-TAU/4, tip_length=TIP_LENGTH)
        arrow_a_to_d = CurvedArrow(a.get_top(), d.get_top(), angle=-TAU/4, tip_length=TIP_LENGTH)
        arrow_b_to_c = CurvedArrow(b.get_bottom(), c.get_bottom(), angle=TAU/4, tip_length=TIP_LENGTH)
        arrow_b_to_d = CurvedArrow(b.get_bottom(), d.get_bottom(), angle=TAU/3, tip_length=TIP_LENGTH)

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
        expression = MathTex(EXPRESSION_TEXT, color=EXPRESSION_COLOR).scale(EXPRESSION_SCALE).next_to(title, DOWN * 4)
        
        # Highlight the operation symbols
        SmartColorizeStatic(
            expression,
            {
                "+": WHITE,
                "-": WHITE
            }
        )
        
        # Get individual terms for the expression
        term_2m = expression[0][search_shape_in_text(expression, MathTex(TERM_1_TEXT))[0]]
        term_1 = expression[0][search_shape_in_text(expression, MathTex(TERM_2_TEXT))[0]]
        term_3n = expression[0][search_shape_in_text(expression, MathTex(TERM_3_TEXT))[0]]
        term_4 = expression[0][search_shape_in_text(expression, MathTex(TERM_4_TEXT))[0]]

        # Create curved arrows for the FOIL operations
        arrow_2m_to_3n = CurvedArrow(
            term_2m.get_top(),
            term_3n.get_top(),
            angle=-TAU/4,
            tip_length=TIP_LENGTH,
            color=TERM_1_COLOR
        )
        
        arrow_2m_to_4 = CurvedArrow(
            term_2m.get_top(),
            term_4.get_top(),
            angle=-TAU/4,
            tip_length=TIP_LENGTH,
            color=TERM_2_COLOR
        )
        
        arrow_1_to_3n = CurvedArrow(
            term_1.get_bottom(),
            term_3n.get_bottom(),
            angle=TAU/4,
            tip_length=TIP_LENGTH,
            color=TERM_3_COLOR
        )
        
        arrow_1_to_4 = CurvedArrow(
            term_1.get_bottom(),
            term_4.get_bottom(),
            angle=TAU/3,
            tip_length=TIP_LENGTH,
            color=TERM_4_COLOR
        )

        # Create the expanded expression
        expanded_expression = MathTex(EXPANDED_EXPRESSION).scale(EXPRESSION_SCALE).next_to(expression, DOWN * 4)
        
        # Apply coloring to the expanded expression
        SmartColorizeStatic(
            expanded_expression,
            {
                EXPANDED_TERM_1: TERM_1_COLOR,
                EXPANDED_TERM_2.replace("-", ""): TERM_2_COLOR,  # Remove - when coloring
                EXPANDED_TERM_3: TERM_3_COLOR,
                EXPANDED_TERM_4.replace("-", ""): TERM_4_COLOR,  # Remove - when coloring
            }
        )
        
        # Get individual expanded terms
        expanded_term_1 = expanded_expression[0][search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_1))[0]]
        
        # For terms with signs, create a VGroup of the sign and term
        # Second term (Outside)
        if EXPANDED_TERM_2.startswith("-"):
            negative_index = search_shape_in_text(expanded_expression, MathTex("-"))[0]
            term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_2.replace("-", "")))[0]
            expanded_term_2 = VGroup(
                expanded_expression[0][negative_index],
                expanded_expression[0][term_index]
            )
        else:
            plus_index = search_shape_in_text(expanded_expression, MathTex("+"))[0]
            term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_2))[0]
            expanded_term_2 = VGroup(
                expanded_expression[0][plus_index],
                expanded_expression[0][term_index]
            )
            
        # Third term (Inside)
        if EXPANDED_TERM_3.startswith("-"):
            # Find the correct minus sign (the second one)
            minus_indices = search_shapes_in_text(expanded_expression, [MathTex("-")])
            if len(minus_indices) > 1:
                negative_index = minus_indices[1]
            else:
                negative_index = minus_indices[0]
            term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_3.replace("-", "")))[0]
            expanded_term_3 = VGroup(
                expanded_expression[0][negative_index],
                expanded_expression[0][term_index]
            )
        else:
            # Find the correct plus sign (the one before the third term)
            plus_indices = search_shapes_in_text(expanded_expression, [MathTex("+")])
            if len(plus_indices) > 0:
                plus_index = plus_indices[0]
                term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_3))[0]
                expanded_term_3 = VGroup(
                    expanded_expression[0][plus_index],
                    expanded_expression[0][term_index]
                )
            else:
                # Fallback if no plus sign found
                term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_3))[0]
                expanded_term_3 = expanded_expression[0][term_index]
        
        # Fourth term (Last)
        if EXPANDED_TERM_4.startswith("-"):
            # Find the last minus sign
            minus_indices = search_shapes_in_text(expanded_expression, [MathTex("-")])
            negative_index = minus_indices[-1]
            term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_4.replace("-", "")))[0]
            expanded_term_4 = VGroup(
                expanded_expression[0][negative_index],
                expanded_expression[0][term_index]
            )
        else:
            # Find the last plus sign
            plus_indices = search_shapes_in_text(expanded_expression, [MathTex("+")])
            if len(plus_indices) > 0:
                plus_index = plus_indices[-1]
                term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_4))[0]
                expanded_term_4 = VGroup(
                    expanded_expression[0][plus_index],
                    expanded_expression[0][term_index]
                )
            else:
                # Fallback if no plus sign found
                term_index = search_shape_in_text(expanded_expression, MathTex(EXPANDED_TERM_4.replace("-", "")))[0]
                expanded_term_4 = expanded_expression[0][term_index]
      
        # Create rectangle around the final expanded expression
        expanded_exp_rectangle = SurroundingRectangle(expanded_expression)

        # Create tips
        tip_1 = QuickTip(TIP_1_TEXT).to_corner(DL)
        SmartColorizeStatic(tip_1[1][0], {"Step 1:": BLACK})

        tip_2 = QuickTip(TIP_2_TEXT).to_corner(DL)
        SmartColorizeStatic(tip_2[1][0], {"Step 2:": BLACK})

        # Animation sequence
        self.add(title)
        with self.voiceover(text=INTRO_VOICEOVER):
            self.play(FadeIn(expression, example, arrow_a_to_c, arrow_a_to_d, arrow_b_to_c, arrow_b_to_d, foil_breakdown))

        with self.voiceover(TERM_1_VOICEOVER):
            self.play(GrowFromPoint(arrow_2m_to_3n, term_2m))
            self.play(Write(expanded_term_1))

        with self.voiceover(TERM_2_VOICEOVER):
            self.play(FadeIn(tip_1, shift=UP))
            self.play(GrowFromPoint(arrow_2m_to_4, term_2m))
            self.play(Write(expanded_term_2))
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(TERM_3_VOICEOVER):
            self.play(GrowFromPoint(arrow_1_to_3n, term_1))
            self.play(Write(expanded_term_3))

        with self.voiceover(TERM_4_VOICEOVER):
            self.play(GrowFromPoint(arrow_1_to_4, term_1), FadeIn(tip_2, shift=UP))
            self.play(Write(expanded_term_4))
        self.play(FadeOut(tip_2, shift=DOWN))

        with self.voiceover(text=FINAL_VOICEOVER):
            pass
        self.play(Create(expanded_exp_rectangle))

        with self.voiceover("So this is our final answer after expanding the expression."):
            pass
        self.wait(2)