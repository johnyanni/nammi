from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


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

FOOTNOTE_SCALE = 0.7

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

class SolveForN(MathTutorialScene):
    def construct(self):
        # Constants
        EQUATION_SPACING = 1.3
        
        # Title and Operations
        title = Tex("Solve for n", color=TITLE_COLOR).to_corner(UL)
        
        # Create equations and manually set colors
        equation = MathTex("4n - 26 = -2").scale(TEX_SCALE)
        step_1 = MathTex("4n = 24").scale(TEX_SCALE)
        solution = MathTex("n = 6").scale(TEX_SCALE)
        
        # Apply colors using the existing smart colorize method from the parent class
        self.apply_smart_colorize(
            [equation, step_1, solution],
            {
                "4": COEFF_COLOR,
                "n": VARIABLE_COLOR,
                "-": CONSTANT_COLOR,  
                "26": CONSTANT_COLOR, 
                "2": CONSTANT_COLOR,
                "6": CONSTANT_COLOR,
                "24": CONSTANT_COLOR,
            }
        )
        

        
        # Arrange and position equations
        equation_group = VGroup(equation, step_1, solution).arrange(DOWN, buff=EQUATION_SPACING)
        equation_group.to_edge(UP, buff=1)
        
        
        # Create solution box
        solution_rec = SurroundingRectangle(solution, buff=0.2, color=WHITE)
        
        
        
        minus_26 = self.find_element("26", equation)
        minus_2 = self.find_element("2", equation, nth=-1)  # Last occurrence of "2"
        add_26 = add_annotations("+26", minus_26, minus_2, color=CONSTANT_COLOR)
        
        
         # Annotations using the add_annotations helper function
        step_1_four = self.find_element("4", step_1)
        step_1_twenty_four = self.find_element("24", step_1)
        div_4 = add_annotations(r"\div 4", step_1_four, step_1_twenty_four, color=COEFF_COLOR)
        
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
            r"\textbf{Step 1}: Add 26 to both sides to eliminate -26",
            color_map={"26": CONSTANT_COLOR}
        ).to_corner(DR)
        
        tip_3 = QuickTip(
            r"\textbf{Step 2}: Divide both sides by 4 to isolate n",
            color_map={"4": COEFF_COLOR, "n": VARIABLE_COLOR}
        ).to_corner(DL)
        
        
# Animation with voiceover
        with self.voiceover(
            text="""
            Let's solve <bookmark mark='equation' /> this equation for n.
            We have 4n minus 26 equals negative 2.
            
            To solve for n, we need to get it by itself on one side of the equation.
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
            Step 1: We need to eliminate the negative 26 on the left side.
            <bookmark mark='tip_in' /> To do this, we'll add 26 to both sides of the equation.
            
            <bookmark mark='add' /> Adding 26 to negative 26 gives us 0, which cancels out.
            On the right side, negative 2 plus 26 equals 24.
            
            <bookmark mark='result' /> So now we have 4n equals 24.
            """
        ) as tracker:
            self.wait_until_bookmark("tip_in")
            self.play(FadeIn(tip_2, shift=UP))
            
            self.wait_until_bookmark("add")
            self.play(FadeIn(add_26), run_time=1.5)
            
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
            Step 2: Now we need to isolate n.
            <bookmark mark='tip_in' /> Since n is being multiplied by 4, we'll divide both sides by 4.
            
            <bookmark mark='divide' /> 4n divided by 4 leaves us with just n.
            And 24 divided by 4 equals 6.
            
            <bookmark mark='solution' /> Therefore, n equals 6.
            """
        ) as tracker:
            self.wait_until_bookmark("tip_in")
            self.play(FadeIn(tip_3, shift=UP))
            
            self.wait_until_bookmark("divide")
            self.play(FadeIn(div_4), run_time=1.5)
            
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
            n equals 6 is our final answer.
            """
        ) as tracker:
            self.play(Create(solution_rec), run_time=1.5)
        
        # Final pause at the end
        self.wait(3)