from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class QuadraticFormulaScrollManager(MathTutorialScene):
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
        
        # Step 4: Identify coefficients for quadratic formula
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
        
        # Step 5: Apply quadratic formula
        step5 = self.create_smart_step(
            "Step 5: Apply the quadratic formula",
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
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
        
        # Step 6: Simplify under the radical
        step6 = self.create_smart_step(
            "Step 6: Simplify under the radical",
            MathTex(r"x = \frac{-10 \pm \sqrt{100 - 52}}{2}"),
            MathTex(r"x = \frac{-10 \pm \sqrt{48}}{2}")
        )
        
        # Step 7: Simplify the square root
        step7 = self.create_smart_step(
            "Step 7: Simplify the square root",
            MathTex(r"\sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt{3}"),
            MathTex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}")
        )
        
        # Step 8: Final simplification
        step8 = self.create_smart_step(
            "Step 8: Factor and simplify",
            MathTex(r"x = \frac{2(-5 \pm 2\sqrt{3})}{2}"),
            MathTex(r"x = -5 \pm 2\sqrt{3}")
        )
        
        # Final answer
        final_answer = self.create_smart_step(
            "Final Answer:",
            MathTex(r"x = -5 + 2\sqrt{3} \quad \text{or} \quad x = -5 - 2\sqrt{3}"),
            MathTex(r"x \approx -1.54 \quad \text{or} \quad x \approx -8.46")
        )
        
        
        step1_annotated_group = VGroup(
            step1[1][0][0],  # equation
            step1[1][0][1]   # annotation
        )
        
        steps = VGroup(starting_eq, step1, step2, step3, step4, step5, step6, step7, step8, final_answer).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create ordered_steps with individual elements
        ordered_steps = VGroup(
            # Starting equation elements
            starting_eq[0],                     # Label
            starting_eq[1],                     # Equation
            
            # Step 1 elements
            step1[0],                          # Label
            step1[1],                    # Annotated equation (annotation part)
            step1[2],                       # Result equation
            
            # Step 2 elements
            step2[0],                          # Label
            step2[1],                          # Equation
            
            # Step 3 elements
            step3[0],                          # Label
            step3[1][0][0],                    # Annotated equation (equation part)
            step3[1][0][1],                    # Annotated equation (annotation part)
            step3[1][1],                       # Result equation
            
            # Step 4 elements
            step4[0],                          # Label
            step4[1],                          # Coefficients equation
            
            # Step 5 elements
            step5[0],                          # Label
            step5[1][0],                       # Generic formula
            step5[1][1],                       # Substituted formula
            
            # Step 6 elements
            step6[0],                          # Label
            step6[1][0],                       # First simplification
            step6[1][1],                       # Second simplification
            
            # Step 7 elements
            step7[0],                          # Label
            step7[1][0],                       # Square root explanation
            step7[1][1],                       # Result with simplified radical
            
            # Step 8 elements
            step8[0],                          # Label
            step8[1][0],                       # Factoring step
            step8[1][1],                       # Final simplified form
            
            # Final answer elements
            final_answer[0],                   # Label
            final_answer[1][0],                # Exact answers
            final_answer[1][1]                 # Decimal approximations
        )
        
        # Position at top left
        ordered_steps.to_edge(UP, buff=0.5).to_edge(LEFT, buff=1)
        
        # Create ScrollManager
        scroll_mgr = ScrollManager(ordered_steps)
        
        # Animations with ScrollManager
        # Starting equation
        scroll_mgr.prepare_next(self)  # Starting equation label
        scroll_mgr.prepare_next(self)  # Starting equation
        
        # Step 1 - Divide by 4
        scroll_mgr.prepare_next(self)  # Step 1 label
        scroll_mgr.prepare_next(self)  # Annotated equation
        scroll_mgr.prepare_next(self)  # Result equation
        scroll_mgr.scroll_down(self, steps=2)  # Scroll to keep in view
        
        # Step 2 - Expand
        scroll_mgr.prepare_next(self)  # Step 2 label
        scroll_mgr.prepare_next(self)  # Expanded equation
        scroll_mgr.scroll_down(self, steps=2)
        
        # # Step 3 - Subtract 12
        # scroll_mgr.prepare_next(self)  # Step 3 label
        # scroll_mgr.prepare_next(self)  # Annotated equation
        # scroll_mgr.prepare_next(self)  # Annotation
        # scroll_mgr.prepare_next(self)  # Result equation
        # scroll_mgr.scroll_down(self, steps=2)
        
        # # Step 4 - Identify coefficients
        # scroll_mgr.prepare_next(self)  # Step 4 label
        # scroll_mgr.prepare_next(self)  # Coefficients
        # scroll_mgr.scroll_down(self, steps=2)
        
        # # Step 5 - Apply quadratic formula
        # scroll_mgr.prepare_next(self)  # Step 5 label
        # scroll_mgr.prepare_next(self)  # Generic formula
        # scroll_mgr.prepare_next(self)  # Substituted formula
        # scroll_mgr.scroll_down(self, steps=3)
        
        # # Step 6 - Simplify under radical
        # scroll_mgr.prepare_next(self)  # Step 6 label
        # scroll_mgr.prepare_next(self)  # First simplification
        # scroll_mgr.prepare_next(self)  # Second simplification
        # scroll_mgr.scroll_down(self, steps=3)
        
        # # Step 7 - Simplify square root
        # scroll_mgr.prepare_next(self)  # Step 7 label
        # scroll_mgr.prepare_next(self)  # Square root explanation
        # scroll_mgr.prepare_next(self)  # Result with simplified radical
        # scroll_mgr.scroll_down(self, steps=3)
        
        # # Step 8 - Final simplification
        # scroll_mgr.prepare_next(self)  # Step 8 label
        # scroll_mgr.prepare_next(self)  # Factoring step
        # scroll_mgr.prepare_next(self)  # Final simplified form
        # scroll_mgr.scroll_down(self, steps=3)
        
        # # Final answer
        # scroll_mgr.prepare_next(self)  # Final answer label
        # scroll_mgr.prepare_next(self)  # Exact answers
        # scroll_mgr.prepare_next(self)  # Decimal approximations
        
        # self.wait(2)