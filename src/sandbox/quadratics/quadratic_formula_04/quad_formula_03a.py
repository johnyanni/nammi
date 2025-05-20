from manim import *
from src.components.common.base_scene import *

config.verbosity = "ERROR"

class QuadraticFormula(MathTutorialScene):
    def construct(self):
        # Constants
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
        ELEMENT_BUFF = 0.3  # Buffer between elements in a step
        STEP_BUFF = 0.5     # Buffer between steps
        
        # Step 1: Get the equation in standard form - No annotations needed
        step1_label = Tex("Get the equation in standard form", color="#DBDBDB").scale(TEXT_SCALE)
        step1_expr = MathTex("4(x+5)^2=48").scale(TEX_SCALE)
        step1 = VGroup(step1_label, step1_expr).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        
        # Step 2: Divide both sides by 4
        step2_label = Tex("Divide both sides by 4", color="#DBDBDB").scale(TEXT_SCALE)
        
        # Use create_annotated_expression for expressions with annotations
        step2_expr1 = self.create_annotated_expression(
            "4(x+5)^2=48", 
            annotations=[(r"\div 4", "4", "48", GREEN)]
        )
        
        # For expressions without annotations, use regular MathTex
        step2_expr2 = MathTex("(x+5)^2=12").scale(TEX_SCALE)
        
        # Group the expressions
        step2_exprs = VGroup(step2_expr1, step2_expr2).arrange(DOWN, buff=ELEMENT_BUFF)
        step2 = VGroup(step2_label, step2_exprs).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        
        # Step 3: Expand the squared term - No annotations needed
        step3_label = Tex("Expand the squared term", color="#DBDBDB").scale(TEXT_SCALE)
        step3_expr1 = MathTex("(x+5)^2=12").scale(TEX_SCALE)
        step3_expr2 = MathTex("x^2 + 10x + 25 = 12").scale(TEX_SCALE)
        
        # Group the expressions
        step3_exprs = VGroup(step3_expr1, step3_expr2).arrange(DOWN, buff=ELEMENT_BUFF)
        step3 = VGroup(step3_label, step3_exprs).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        
        # Step 4: Subtract 12 from both sides
        step4_label = Tex("Subtract 12 from both sides", color="#DBDBDB").scale(TEXT_SCALE)
        
        # Use create_annotated_expression for expressions with annotations
        step4_expr1 = self.create_annotated_expression(
            "x^2 + 10x + 25 = 12",
            annotations=[("-12", "25", "12", RED)]
        )
        
        # For expressions without annotations, use regular MathTex
        step4_expr2 = MathTex("x^2 + 10x + 13 = 0").scale(TEX_SCALE)
        
        # Group the expressions
        step4_exprs = VGroup(step4_expr1, step4_expr2).arrange(DOWN, buff=ELEMENT_BUFF)
        step4 = VGroup(step4_label, step4_exprs).arrange(DOWN, aligned_edge=LEFT, buff=ELEMENT_BUFF)
        
        # Arrange all steps vertically
        solution = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=STEP_BUFF)
        
        # Position the solution on the screen
        solution.to_edge(UP, buff=0.1).to_edge(LEFT, buff=1)
        
        # For debugging - show the bounding boxes
        # for step in [step1, step2, step3, step4]:
        #     step_box = SurroundingRectangle(step, stroke_color=WHITE, stroke_opacity=0.3)
        #     self.add(step_box)
        
        # ========== ANIMATIONS ==========
        # Store references for animations
        step2_expr = step2_expr1[1]  # The actual expression
        div_4_annotations = step2_expr1[2]  # The annotation VGroup
        
        step4_expr = step4_expr1[1]  # The actual expression
        subtract_12_annotations = step4_expr1[2]  # The annotation VGroup
        
        # Step 1 animations
        self.play(Write(step1_label))
        self.play(Write(step1_expr))
        self.wait(1)
        
        # Step 2 animations
        self.play(Write(step2_label))
        self.play(Write(step2_expr))
        self.wait(0.5)
        
        # Animate division annotation 
        self.play(FadeIn(div_4_annotations))
        self.wait(0.5)
        
        # Show the result of division
        self.play(Write(step2_expr2))
        self.wait(1)
        
        # Step 3 animations
        self.play(Write(step3_label))
        
        # Link to previous step
        self.play(ReplacementTransform(step2_expr2.copy(), step3_expr1))
        self.wait(0.5)
        
        # Show expanded expression
        self.play(Write(step3_expr2))
        self.wait(1)
        
        # Step 4 animations
        self.play(Write(step4_label))
        
        # Link to previous step
        self.play(ReplacementTransform(step3_expr2.copy(), step4_expr))
        self.wait(0.5)
        
        # Animate subtraction annotation
        self.play(FadeIn(subtract_12_annotations))
        self.wait(0.5)
        
        # Show the final result
        self.play(Write(step4_expr2))
        
        self.wait(2)