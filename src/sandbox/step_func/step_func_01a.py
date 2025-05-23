from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class StepFunc(MathTutorialScene):
    def construct(self):
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"
        
        # Starting equation
        starting_eq = self.create_smart_step(
            "Starting equation: Convert to standard quadratic form",
            MathTex("4(x+5)^2=48")
        )
        
        # Step 1: Divide both sides by 4
        step1_annotated = self.create_annotated_equation(
            "4(x+5)^2=48", 
            r"\div 4", 
            "4", "48", 
            color=GREEN
        )
        
        step1 = self.create_smart_step(
            "Step 1: Divide both sides by 4",
            step1_annotated,
            MathTex("(x+5)^2=12")
        )
        
        # Step 2: Expand the squared term
        step2 = self.create_smart_step(
            "Step 2: Expand the squared term",
            MathTex("x^2 + 10x + 25 = 12")
        )
        
        step2_extend = MathTex("x^2 + 10x + 25 = 12").scale(MATH_SCALE).set_color(RED)
        
        # Step 3: Subtract 12 from both sides
        step3_annotated = self.create_annotated_equation(
            "x^2 + 10x + 25 = 12",
            r"-12",
            "25", "12",
            color=RED
        )
        
        step3 = self.create_smart_step(
            "Step 3: Subtract 12 from both sides",
            step3_annotated,
            MathTex("x^2 + 10x + 13 = 0")
        )
        
        # Step 4: Identify coefficients
        step4 = self.create_smart_step(
            "Step 4: Identify coefficients for quadratic formula",
            MathTex("a = 1, \\quad b = 10, \\quad c = 13"),
            color_map={
                "a": A_COLOR,
                "1": A_COLOR,
                "b": B_COLOR, 
                "10": B_COLOR,
                "c": C_COLOR,
                "13": C_COLOR
            }
        )
        
        # Create the equation and rectangle together
        formula_eq = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(MATH_SCALE)
        formula_rect = self.create_surrounding_rectangle(formula_eq)
        formula_with_rect = VGroup(formula_rect, formula_eq)  # Rectangle behind equation

        step5 = self.create_smart_step(
            "Step 5: Apply the quadratic formula",
            formula_with_rect,  # Use the grouped version
            MathTex(r"x = \frac{-10 \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}"),
            color_map={
                "b": B_COLOR,
                "10": B_COLOR,
                "a": A_COLOR,
                "1": A_COLOR,
                "c": C_COLOR,
                "13": C_COLOR
            }
        )
        
        original_equation = MathTex(r"f(x) = x^2 + 2x + 1").scale(TEX_SCALE)
        factored_equation = MathTex(r"= (x + 1)^2").scale(TEX_SCALE)
        
        # Create an arrow
        arrow = Arrow(LEFT, RIGHT, color=YELLOW, buff=0.2)
        
        # Create a custom horizontal layout
        horizontal_arrangement = VGroup(
            original_equation,
            arrow,
            factored_equation
        ).arrange(RIGHT, buff=0.5)
        
        step6 = self.create_smart_step(
            "Step 6: Factor the quadratic expression",
            horizontal_arrangement
        )
        
        # Position all steps
        all_steps = VGroup(starting_eq, step1, step2,step2_extend, step3, step4, step5, step6)
        
        all_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        all_steps.to_edge(UP, buff=0.5).to_edge(LEFT, buff=1)
        
        # Unpack for ScrollManager using the new approach
        all_elements = self.unpack_steps_for_scroll_manager(starting_eq, step1, step2, step2_extend, step3, step4, step5, step6)
        
        
        # Create ScrollManager
        scroll_mgr = ScrollManager(all_elements)
        
        # Animations with automatic annotation detection
        # Starting equation
        scroll_mgr.prepare_next(self)  # Starting equation label
        scroll_mgr.prepare_next(self)  # Starting equation
        
        # Step 1 - Divide by 4 (annotated equation will be auto-detected)
        scroll_mgr.prepare_next(self)  # Step 1 label
        scroll_mgr.prepare_next(self)  # Annotated equation (auto-detected!)
        scroll_mgr.prepare_next(self)  # Result equation
        scroll_mgr.scroll_down(self, steps=2)
        
        # Step 2 - Expand
        scroll_mgr.prepare_next(self)  # Step 2 label
        scroll_mgr.prepare_next(self)  # Expanded equation
        scroll_mgr.prepare_next(self)  # Expanded equation
        scroll_mgr.scroll_down(self, steps=3)
        
        # Step 3 - Subtract 12 (annotated equation will be auto-detected)
        scroll_mgr.prepare_next(self)  # Step 3 label
        scroll_mgr.prepare_next(self)  # Annotated equation (auto-detected!)
        scroll_mgr.prepare_next(self)  # Result equation
        scroll_mgr.scroll_down(self, steps=2)
        
        # Step 4 - Identify coefficients
        scroll_mgr.prepare_next(self)  # Step 4 label
        scroll_mgr.prepare_next(self)  # Coefficients
        scroll_mgr.scroll_down(self, steps=3)
        
        # Step 5 - Apply quadratic formula
        scroll_mgr.prepare_next(self)  # Step 5 label
        scroll_mgr.prepare_next(self)  # Generic formula
        scroll_mgr.prepare_next(self)  # Generic formula
        scroll_mgr.prepare_next(self)  # Substituted formula
        
        self.wait(2)
        
        scroll_mgr.prepare_next(self)  # Step 5 label
        scroll_mgr.prepare_next(self)  # Generic formula
        scroll_mgr.prepare_next(self)  # Substituted formula
        scroll_mgr.prepare_next(self)  # Step 5 label