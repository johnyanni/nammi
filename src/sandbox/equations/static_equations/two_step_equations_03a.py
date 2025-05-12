from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


def add_annotations(term_added, left_term, right_term, color=None, h_spacing=0):
    terms = VGroup(*[MathTex(rf"{term_added}").scale(FOOTNOTE_SCALE) for _ in range(2)])
    if color:
        terms.set_color(color)
        
    terms[0].next_to(left_term, DOWN)
    terms[1].next_to(right_term, DOWN)
    
     # Apply horizontal spacing adjustment
    terms[0].shift(LEFT * h_spacing)  # Move left annotation further left
    terms[1].shift(RIGHT * h_spacing)  # Move right annotation further right
    
    
    if terms[0].get_y() < terms[1].get_y():
        terms[1].align_to(terms[0], DOWN)
    else:
        terms[0].align_to(terms[1], DOWN)

    return terms

FOOTNOTE_SCALE = 0.6

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

class SolveForY(MathTutorialScene):
    def construct(self):
        # Constants
        EQUATION_SPACING = 1.3
        
        # Title and Operations
        title = Tex("Solve for y", color=TITLE_COLOR).to_corner(UL)
        
        # Create equations and manually set colors
        equation = MathTex("-2y - 13 = -11").scale(TEX_SCALE)
        step_1 = MathTex("-2y = 2").scale(TEX_SCALE)
        solution = MathTex("y = -1").scale(TEX_SCALE)
        
        # Apply colors using the existing smart colorize method from the parent class
        self.apply_smart_colorize(
            [equation, step_1, solution],
            {
                "2": COEFF_COLOR,
                "y": VARIABLE_COLOR,
                "-": CONSTANT_COLOR,  
                "13": CONSTANT_COLOR, 
                "11": CONSTANT_COLOR,
                "1": CONSTANT_COLOR,
            }
        )
        
        # Arrange and position equations
        equation_group = VGroup(equation, step_1, solution).arrange(DOWN, buff=EQUATION_SPACING)
        equation_group.to_edge(UP, buff=1)
        
        # Create solution box
        solution_rec = SurroundingRectangle(solution, buff=0.2, color=WHITE)
        
        # Find elements for annotations
        minus_13 = self.find_element("13", equation)
        minus_11 = self.find_element("11", equation)
        add_13 = add_annotations("+13", minus_13, minus_11, color=CONSTANT_COLOR)
        
        # Annotations for step 2
        step_1_minus_2 = self.find_element("2", step_1, nth=0)  # First occurrence of "2" (the coefficient)
        step_1_positive_2 = self.find_element("2", step_1, nth=-1)  # Last occurrence of "2"
        div_neg2 = add_annotations(r"\div (-2)", step_1_minus_2, step_1_positive_2, color=COEFF_COLOR, h_spacing=0.6)
        
        # Tips
        tip_1 = QuickTip(
            "Get rid of plus/minus before multiply/divide",
            color_map={
                "plus": PLUS_COLOR,
                "minus": MINUS_COLOR,
                "multiply": TIMES_COLOR,
                "divide": DIVISION_COLOR
            }
        ).to_corner(DR)
        
        tip_2 = QuickTip(
            r"\textbf{Step 1}: Add 13 to both sides to eliminate -13",
            color_map={"13": CONSTANT_COLOR}
        ).to_corner(DR)
        
        tip_3 = QuickTip(
            r"\textbf{Step 2}: Divide both sides by -2 to isolate y",
            color_map={"2": COEFF_COLOR, "y": VARIABLE_COLOR}
        ).to_corner(DL)
        
        # Animation with voiceover
        with self.voiceover(
            text="""
            Let's solve <bookmark mark='equation' /> this equation for y.
            We have negative 2y minus 13 equals negative 11.
            
            To solve for y, we need to get it by itself on one side of the equation.
            We'll do this in two steps.
            """
        ) as tracker:
            self.play(FadeIn(title))
            self.wait_until_bookmark("equation")
            self.play(Write(equation))
        
        # Pause after introducing the equation
        self.wait(2)
        
        with self.voiceover(
            text="""
            When solving equations, it's important to remember that we should handle addition and subtraction before multiplication and division.
            <bookmark mark='tip_in' /> This helps us work through the problem systematically.
            """
        ) as tracker:
            self.wait_until_bookmark("tip_in")
            self.play(FadeIn(tip_1, shift=UP))
        
        # Pause to let students read the tip
        self.wait(3)
        self.play(FadeOut(tip_1, shift=DOWN))
        
        with self.voiceover(
            text="""
            Step 1: We need to eliminate the negative 13 on the left side.
            <bookmark mark='tip_in' /> To do this, we'll add 13 to both sides of the equation.
            
            <bookmark mark='add' /> Adding 13 to negative 13 gives us 0, which cancels out.
            On the right side, negative 11 plus 13 equals positive 2.
            
            <bookmark mark='result' /> So now we have negative 2y equals 2.
            """
        ) as tracker:
            self.wait_until_bookmark("tip_in")
            self.play(FadeIn(tip_2, shift=UP))
            
            self.wait_until_bookmark("add")
            self.play(FadeIn(add_13), run_time=1.5)
            
            self.wait_until_bookmark("result")
            self.play(
                FadeIn(step_1), 
                FadeOut(tip_2, shift=DOWN),
                run_time=2
            )
        
        # Comprehension pause after completing step 1
        self.wait(2)
        
        with self.voiceover(
            text="""
            Step 2: Now we need to isolate y.
            <bookmark mark='tip_in' /> Since y is being multiplied by negative 2, we'll divide both sides by negative 2.
            
            <bookmark mark='divide' /> Negative 2y divided by negative 2 leaves us with just y.
            And 2 divided by negative 2 equals negative 1.
            
            <bookmark mark='solution' /> Therefore, y equals negative 1.
            """
        ) as tracker:
            self.wait_until_bookmark("tip_in")
            self.play(FadeIn(tip_3, shift=UP))
            
            self.wait_until_bookmark("divide")
            self.play(FadeIn(div_neg2), run_time=1.5)
            
            self.wait_until_bookmark("solution")
            self.play(
                FadeIn(solution), 
                FadeOut(tip_3, shift=DOWN),
                run_time=2
            )
        
        # Quick pause before verification
        self.wait(1.5)
        
        with self.voiceover(
            text="""
            Let's verify our answer. 
            If y equals negative 1, then negative 2 times negative 1 is positive 2, minus 13 gives us negative 11.
            That matches the original equation, so our solution is correct!
            
            <bookmark mark='highlight' /> y equals negative 1 is our final answer.
            """
        ) as tracker:
            self.wait_until_bookmark("highlight")
            self.play(Create(solution_rec), run_time=1.5)
        
        # Final pause at the end
        self.wait(3)