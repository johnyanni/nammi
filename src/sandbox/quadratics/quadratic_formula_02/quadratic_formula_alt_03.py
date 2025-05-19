"""Compatible implementation of the quadratic formula tutorial using your existing ScrollManager."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

class CompatibleQuadraticFormula(MathTutorialScene):
    def construct(self):
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        
        ANNOTATION_SPACING = 0.7

        ###############################################################################
        # SECTION 1: FORMULA/HELPERS 
        ###############################################################################

        # Create the generic quadratic equation
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE)
        
        # Find the coefficients in the general equation
        quad_form_a = quadratic_form[0][0]  # 'a' is typically first character
        quad_form_b = quadratic_form[0][4]  # 'b' is typically at position 4
        quad_form_c = quadratic_form[0][7]  # 'c' is typically at position 8
        
        # Create the quadratic formula
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        
        # Arrange the quadratic equation and formula
        quadratic_group = Group(
            quadratic_form,
            quadratic_formula
        ).arrange(RIGHT, aligned_edge=UP, buff=0.6).to_corner(UR, buff=0.6)
        
        quadratic_form_bg = SurroundingRectangle(
            quadratic_form,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        ###############################################################################
        # SECTION 2: PROBLEM AND STEPS SETUP - IMPROVED ORGANIZATION
        ###############################################################################
        
        # Problem statement with better organization
        question_title = Tex("Solve using the quadratic formula:").scale(0.6)
        problem_equation = MathTex("-x^2 - 3x = - 9").scale(0.6)
        question_group = VGroup(question_title, problem_equation).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1
        ).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)
        
        ###############################################################################
        # STEP 1: Rewrite in standard form
        ###############################################################################
        step1_title = self.create_labeled_step(
            "Step 1: Rewrite in standard form",
            MathTex("-x^2 - 3x = - 9").scale(TEX_SCALE)
        )
        
        step1_equation_final = MathTex("-x^2 - 3x + 9 = 0").scale(TEX_SCALE)
        
        # Add the annotations to show how we add 9 to both sides
        step1_annotations = self.add_annotations(
            "+9", 
            self.find_element("-3", step1_title[1]),
            self.find_element("-9", step1_title[1]),
            color=RED
        )
        
        step1_group = VGroup(step1_title, step1_annotations, step1_equation_final)

        ###############################################################################
        # STEP 2: Identify coefficients
        ###############################################################################
        step2_title = self.create_labeled_step(
            "Step 2: Identify coefficients",
            MathTex("-1x^2 - 3x + 9 = 0").scale(TEX_SCALE)
        )
        
        # Find elements in the equation to highlight
        a_in_equation = self.find_element("-1", step2_title[1], opacity=0, color=A_COLOR)
        b_in_equation = self.find_element("-3", step2_title[1], color=B_COLOR)      
        c_in_equation = self.find_element("9", step2_title[1], color=C_COLOR)      

        # Create coefficient labels
        coef_a = MathTex("a = -1", color=A_COLOR).scale(TEX_SCALE)
        coef_b = MathTex("b = -3", color=B_COLOR).scale(TEX_SCALE)
        coef_c = MathTex("c = 9", color=C_COLOR).scale(TEX_SCALE)

        # Extract coefficient values for animations
        a_value = self.find_element("-1", coef_a)
        b_value = self.find_element("-3", coef_b)
        c_value = self.find_element("9", coef_c)

        # Arrange coefficients horizontally
        coefficients = VGroup(coef_a, coef_b, coef_c).arrange(RIGHT, buff=0.6)
        
        step2_group = VGroup(step2_title, coefficients)

        ###############################################################################
        # STEP 3: Use the quadratic formula
        ###############################################################################
        step3_title = self.create_labeled_step(
            "Step 3: Use the quadratic formula",
            MathTex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE)
        )

        ###############################################################################
        # STEP 4: Substitute the coefficients
        ###############################################################################
        step4_title = self.create_labeled_step(
            "Step 4: Substitute the coefficients",
            MathTex(r"x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(-1)(9)}}{2(-1)}").scale(TEX_SCALE)
        )

        # Find elements in step4 for substitution animation
        b_in_frac = self.find_element("-3", step4_title[1], nth=0, opacity=0, color=B_COLOR)
        b_in_sqrt = self.find_element("-3", step4_title[1], nth=1, opacity=0, color=B_COLOR)
        a_in_4ac = self.find_element("-1", step4_title[1], nth=0, opacity=0, color=A_COLOR)
        c_in_4ac = self.find_element("9", step4_title[1], nth=0, opacity=0, color=C_COLOR)
        a_in_denom = self.find_element("-1", step4_title[1], nth=1, opacity=0, color=A_COLOR)

        # Create visible copies for animation
        visible_b_frac = b_value.copy().set_opacity(1)
        visible_b_sqrt = b_value.copy().set_opacity(1)
        visible_a_4ac = a_value.copy().set_opacity(1)
        visible_c_4ac = c_value.copy().set_opacity(1)
        visible_a_denom = a_value.copy().set_opacity(1)

        # Group substitution elements for easier handling
        substitution_elements = VGroup(
            visible_b_frac, visible_b_sqrt, visible_a_4ac, visible_a_denom, visible_c_4ac
        )

        ###############################################################################
        # STEP 5-7: Simplification Steps
        ###############################################################################
        step5_title = self.create_labeled_step(
            "Step 5: Simplify the expression",
            MathTex(r"x = \frac{3 \pm \sqrt{9 - 4(-1)(9)}}{-2}").scale(TEX_SCALE)
        )

        step6_title = self.create_labeled_step(
            "Step 6: Continue simplifying",
            MathTex(r"x = \frac{3 \pm \sqrt{9 + 36}}{-2}").scale(TEX_SCALE)
        )
        
        # Highlight discriminant in step 6
        discriminant = self.find_element("9 + 36", step6_title[1], color=YELLOW)

        step7_title = self.create_labeled_step(
            "Step 7: Calculate the square root",
            MathTex(r"x = \frac{3 \pm \sqrt{45}}{-2}").scale(TEX_SCALE)
        )

        step8_title = self.create_labeled_step(
            "Step 8: Evaluate the square root",
            MathTex(r"x = \frac{3 \pm 6.7082}{-2}").scale(TEX_SCALE)
        )

        ###############################################################################
        # FINAL SOLUTIONS
        ###############################################################################
        first_solution = MathTex(r"x_1 = \frac{3 + 6.7082}{-2} \approx -4.85").scale(TEX_SCALE)
        second_solution = MathTex(r"x_2 = \frac{3 - 6.7082}{-2} \approx 1.85").scale(TEX_SCALE)
        
        solutions_group = VGroup(first_solution, second_solution).arrange(
            DOWN, aligned_edge=LEFT, buff=0.8
        )
        
        # Create solution highlights
        first_solution_rect = SurroundingRectangle(
            first_solution, color="#9A48D0", 
            corner_radius=0.1, buff=0.2
        )
        
        second_solution_rect = SurroundingRectangle(
            second_solution, color="#9A48D0",
            corner_radius=0.1, buff=0.2
        )

        ###############################################################################
        # SECTION 3: APPLY SMART COLOR STYLING
        ###############################################################################
        
        # Apply coloring to formula components
        self.apply_smart_colorize(
            [quadratic_form, quadratic_formula, step3_title[1]],
            {
                "a": A_COLOR, 
                "b": B_COLOR, 
                "c": C_COLOR,
            }
        )
        
        ###############################################################################
        # SECTION 4: SET UP SCROLL MANAGER WITH IMPROVED ELEMENT GROUPING
        ###############################################################################
        
        # Create ordered elements with a clear, logical structure
        ordered_elements = VGroup(
            # Problem presentation
            question_title,
            problem_equation,
            
            # Step 1: Rewrite in standard form
            step1_title[0],                  # Label
            step1_title[1],                  # Original equation
            step1_equation_final,            # Final form
            
            # Step 2: Identify coefficients
            step2_title[0],                  # Label
            step2_title[1],                  # Equation in standard form
            coef_a,                          # a coefficient 
            coef_b,                          # b coefficient
            coef_c,                          # c coefficient
            
            # Step 3: Use formula
            step3_title[0],                  # Label
            step3_title[1],                  # Formula template
            
            # Step 4: Substitution
            step4_title[0],                  # Label
            step4_title[1],                  # With substituted values
            
            # Simplification steps
            step5_title[0], step5_title[1],  # Step 5
            step6_title[0], step6_title[1],  # Step 6
            step7_title[0], step7_title[1],  # Step 7
            step8_title[0], step8_title[1],  # Step 8
            
            # Final solutions
            first_solution,                  # First solution
            second_solution                  # Second solution
        )
        
        # Initialize ScrollManager with ordered elements
        scroll_mgr = ScrollManager(ordered_elements)
        
        ###############################################################################
        # SECTION 5: ANIMATIONS WITH IMPROVED FLOW AND TIMING
        ###############################################################################
        
        # Show the formula reference on top
        self.play(
            FadeIn(
                quadratic_group,
                quadratic_form_bg,
                quadratic_formula_bg
            )
        )
        
        # IMPROVED FEATURE 1: Show problem with better animation
        # Using compatible methods with your existing ScrollManager
        scroll_mgr.prepare_next(self)  # Show title
        scroll_mgr.prepare_next(self)  # Show problem equation
        
        # IMPROVED FEATURE 2: Show step 1 with better timing
        scroll_mgr.prepare_next(self)  # Show step1_title label
        scroll_mgr.prepare_next(self)  # Show original equation
        
        # Add annotations showing how we add 9 to both sides with a clearer animation
        self.play(FadeIn(step1_annotations), run_time=1.2)
        
        # Show the result of rearranging the equation
        scroll_mgr.prepare_next(self)  # Show final standard form
        
        # IMPROVED FEATURE 3: Transition to step 2 with smooth transformation
        self.play(
            FadeOut(step1_annotations),
            ReplacementTransform(step1_equation_final.copy(), step2_title[1])
        )
        
        # Show step 2 title
        scroll_mgr.prepare_next(self)  # Show step2 title
        scroll_mgr.prepare_next(self)  # Show equation
        
        # IMPROVED FEATURE 4: Better coefficient identification animation
        # First show just the "a = ", "b = ", "c = " placeholders
        self.play(
            FadeIn(coef_a[0][:2]),  # Just "a = "
            FadeIn(coef_b[0][:2]),  # Just "b = "
            FadeIn(coef_c[0][:2])   # Just "c = "
        )

        # Now introduce each coefficient value with a clear connection to the formula
        # Coefficient a
        self.play(self.indicate(quad_form_a, color=A_COLOR))
        scroll_mgr.prepare_next(self)  # Show full coefficient a
        
        # Connect a to the equation with a callout
        a_callout = Arrow(a_value.get_top(), a_in_equation.get_bottom(), buff=0.1, color=A_COLOR)
        self.play(GrowArrow(a_callout))
        self.wait(0.5)
        self.play(FadeOut(a_callout))

        # Coefficient b
        self.play(self.indicate(quad_form_b, color=B_COLOR))
        scroll_mgr.prepare_next(self)  # Show full coefficient b
        
        # Connect b to the equation with a callout
        b_callout = Arrow(b_value.get_top(), b_in_equation.get_bottom(), buff=0.1, color=B_COLOR)
        self.play(GrowArrow(b_callout))
        self.wait(0.5)
        self.play(FadeOut(b_callout))

        # Coefficient c
        self.play(self.indicate(quad_form_c, color=C_COLOR))
        scroll_mgr.prepare_next(self)  # Show full coefficient c
        
        # Connect c to the equation with a callout
        c_callout = Arrow(c_value.get_top(), c_in_equation.get_bottom(), buff=0.1, color=C_COLOR)
        self.play(GrowArrow(c_callout))
        self.wait(0.5)
        self.play(FadeOut(c_callout))
        
        # IMPROVED FEATURE 5: Better scrolling transition to formula application
        scroll_mgr.scroll_down(self, steps=3)  # Scroll down after identifying coefficients
        
        # Show the quadratic formula template
        scroll_mgr.prepare_next(self)  # Show formula label
        scroll_mgr.prepare_next(self)  # Show formula template
        
        # Show substitution title and prepared equation shell
        scroll_mgr.prepare_next(self)  # Show substitution title
        scroll_mgr.prepare_next(self)  # Show substitution equation
        
        # IMPROVED FEATURE 6: Better substitution animation with sequential highlighting
        
        # Create a tip to explain the substitution process
        sub_tip = QuickTip(
            "We substitute our coefficient values directly into the quadratic formula:\n"
            "• a = -1 is the coefficient of x²\n"
            "• b = -3 is the coefficient of x\n"
            "• c = 9 is the constant term"
        ).to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(sub_tip))
        self.wait(1.5)  # Give time to read the tip
        
        # Now animate each substitution with a slight pause between each
        # b in numerator
        self.play(
            FadeIn(visible_b_frac, target_position=b_in_frac.get_center()),
            run_time=0.8
        )
        self.wait(0.3)
        
        # b in square root
        self.play(
            FadeIn(visible_b_sqrt, target_position=b_in_sqrt.get_center()),
            run_time=0.8
        )
        self.wait(0.3)
        
        # a in 4ac
        self.play(
            FadeIn(visible_a_4ac, target_position=a_in_4ac.get_center()),
            run_time=0.8
        )
        self.wait(0.3)
        
        # c in 4ac
        self.play(
            FadeIn(visible_c_4ac, target_position=c_in_4ac.get_center()),
            run_time=0.8
        )
        self.wait(0.3)
        
        # a in denominator
        self.play(
            FadeIn(visible_a_denom, target_position=a_in_denom.get_center()),
            run_time=0.8
        )
        
        # Remove the tip
        self.play(FadeOut(sub_tip))
        
        # Add substitution elements to equation for positioning
        step4_title[1].add(*substitution_elements)
        
        # IMPROVED FEATURE 7: Smart scrolling for computation steps
        scroll_mgr.scroll_down(self, steps=3)  # Scroll after substitution
        
        # Prepare to show steps 5-8 with appropriate timing based on complexity
        # Step 5 - First simplification
        scroll_mgr.prepare_next(self)  # Show step 5 title
        scroll_mgr.prepare_next(self)  # Show step 5 equation
        self.wait(0.5)  # Give a brief pause
        
        # Step 6 - Second simplification
        scroll_mgr.scroll_down(self, steps=2)
        scroll_mgr.prepare_next(self)  # Show step 6 title
        scroll_mgr.prepare_next(self)  # Show step 6 equation
        
        # IMPROVED FEATURE 8: Highlight the discriminant with a helpful tip
        discriminant_tip = QuickTip(
            "The expression b² - 4ac is called the discriminant. "
            "Since 9 + 36 = 45 is positive, we'll have two real solutions.",
            color_map={"b² - 4ac": YELLOW, "9 + 36 = 45": YELLOW}
        ).to_edge(DOWN, buff=0.5)
        
        self.play(
            Indicate(discriminant, color=YELLOW, scale_factor=1.2),
            FadeIn(discriminant_tip)
        )
        self.wait(2)  # Give time to read
        self.play(FadeOut(discriminant_tip))
        
        # Step 7 - Finding square root
        scroll_mgr.scroll_down(self, steps=2)
        scroll_mgr.prepare_next(self)  # Show step 7 title
        scroll_mgr.prepare_next(self)  # Show step 7 equation
        
        # Step 8 - Approximating square root
        scroll_mgr.scroll_down(self, steps=2)  
        scroll_mgr.prepare_next(self)  # Show step 8 title
        scroll_mgr.prepare_next(self)  # Show step 8 equation
        
        # IMPROVED FEATURE 9: Better solution presentation
        scroll_mgr.scroll_down(self, steps=2)
        
        # Show solutions with individual animations (compatible with existing ScrollManager)
        scroll_mgr.prepare_next(self)  # Show first solution
        scroll_mgr.prepare_next(self)  # Show second solution
        
        # Add rectangles with a nice creation animation
        self.play(
            Create(first_solution_rect),
            Create(second_solution_rect),
            run_time=1.5
        )
        
        # IMPROVED FEATURE 10: Add a final QuickTip explaining the solutions
        final_tip = QuickTip(
            "The quadratic equation $-x^2 - 3x + 9 = 0$ has two solutions: "
            "$x \\approx -4.85$ and $x \\approx 1.85$. You can verify these "
            "by substituting them back into the original equation."
        ).next_to(solutions_group, DOWN, buff=0.8)
        
        self.play(FadeIn(final_tip))
        
        # Final pause to view the completed solution
        self.wait(2)