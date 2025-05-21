from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

class Example08(MathTutorialScene):
    def construct(self):
 
 
        
        
           # Create some mathematical expressions
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
        
        ##############################################
        # APPROACH 1: Using create_labeled_step_vertical_tex
        ##############################################
        
        # Method 1A: Pass the VGroup directly (with preserve_arrangement=True)
        # Note: This may not work as expected
        step_1a = self.create_labeled_step_vertical_tex(
            "Method 1A: Pass VGroup directly with True",
            horizontal_arrangement,
            preserve_arrangement=True
        )
        
        # Method 1B: Pass the VGroup in a list (recommended approach)
        step_1b = self.create_labeled_step_vertical_tex(
            "Method 1B: Pass VGroup in a list",
            [horizontal_arrangement]
        )
        
        # Method 1C: Recreate the arrangement inside
        step_1c = self.create_labeled_step_vertical_tex(
            "Method 1C: Recreate arrangement in a list",
            [
                VGroup(
                    original_equation.copy(),
                    arrow.copy(),
                    factored_equation.copy()
                ).arrange(RIGHT, buff=0.5)
            ]
        )
        
        ##############################################
        # APPROACH 2: Using create_multi_exp_labeled_step_tex
        ##############################################
        
        # Method 2A: Pass the VGroup directly
        step_2a = self.create_multi_exp_labeled_step_tex(
            "Method 2A: Pass VGroup directly",
            horizontal_arrangement.copy()
        )
        
        # Method 2B: Recreate the arrangement inside
        horizontal_2b = VGroup(
            original_equation.copy(),
            arrow.copy(),
            factored_equation.copy()
        ).arrange(RIGHT, buff=0.5)
        
        step_2b = self.create_multi_exp_labeled_step_tex(
            "Method 2B: Recreate arrangement inline",
            horizontal_2b
        )
        
        # Arrange and show all approaches
        all_steps = VGroup(
            step_1a, step_1b, step_1c,
            step_2a, step_2b
        ).arrange(DOWN, buff=1).scale(0.8)
        
        #self.add(all_steps)
        
        # Add explanatory labels
        approach_1 = Tex("APPROACH 1: vertical").next_to(step_1a, UP, buff=0.5)
        approach_1.set_color(BLUE)
        
        approach_2 = Tex("APPROACH 2: multi").next_to(step_2a, UP, buff=0.5)
        approach_2.set_color(GREEN)
        
        #self.add(approach_1, approach_2)
        
        
        
                # Create some MathTex objects
        eq1 = MathTex(r"a^2").scale(TEX_SCALE)
        eq2 = MathTex(r"+").scale(TEX_SCALE)
        eq3 = MathTex(r"b^2").scale(TEX_SCALE)
        eq4 = MathTex(r"=").scale(TEX_SCALE)
        eq5 = MathTex(r"c^2").scale(TEX_SCALE)

        # Create a custom horizontal arrangement
        horizontal_equation = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(RIGHT, buff=0.2)

        # Add another equation below with specific positioning
        eq6 = MathTex(r"\text{(Pythagorean Theorem)}").scale(TEX_SCALE * 0.8)

        # Create a complete arrangement
        complete_arrangement = VGroup(horizontal_equation, eq6).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Now let's try both function approaches:

        # APPROACH 1: Using create_multi_exp_labeled_step (variadic parameter)
        step1 = self.create_multi_exp_labeled_step_tex(
            "Using variadic parameter approach:",
            complete_arrangement  # This is passed as a single argument
        )
        
        #self.add(step1)
        
        
        
        
            # Point 1 calculations
        point_1 = self.create_multi_exp_labeled_step_tex(
            "When x = 3:",
            r"y = \frac{2}{2 - 3} + 4",
            r"= \frac{2}{-1} + 4", 
            r"= -2 + 4",
            r"y = 2",
            exps_buff=0.4
        )
        
        # Apply right shifts to steps 2 and 3
        point_1[1][1].shift(RIGHT * 0.3)  # Second expression (= 2/-1 + 4)
        point_1[1][2].shift(RIGHT * 0.3)  # Third expression (= -2 + 4)
        
        # Create rectangle around the final result
        point_1_final_result_rec = self.create_surrounding_rectangle(point_1[1][3])
        point_1[1][3].add(point_1_final_result_rec)
        
        # Point 2 calculations
        point_2 = self.create_multi_exp_labeled_step_tex(
            "When x = 4:",
            r"y = \frac{2}{4 - 3} + 4",
            r"= \frac{2}{1} + 4",
            r"= 2 + 4",
            r"y = 6"
        )
        
        # Apply right shifts to steps 2 and 3
        point_2[1][1].shift(RIGHT * 0.3)  # Second expression (= 2/1 + 4)
        point_2[1][2].shift(RIGHT * 0.3)  # Third expression (= 2 + 4)
        
        # Create rectangle around the final result
        point_2_final_result_rec = self.create_surrounding_rectangle(point_2[1][3])
        point_2[1][3].add(point_2_final_result_rec)
        
        # Create point labels
        point_1_label = point_1[0]
        point_2_label = point_2[0]
        
        # Remove labels from individual points to arrange them side by side
        point_1.remove(point_1_label)
        point_2.remove(point_2_label)
        
        # Arrange points side by side
        points_group = VGroup(point_1[0], point_2[0]).arrange(buff=4)
        
        # Create the final step with combined title
        step_4 = self.create_labeled_step(
            "Step 4: Calculate some points on the curve",
            points_group
        )
        
        self.add(step_4)
        
        
        
        elements = VGroup(
            MathTex("x^2"),
            MathTex("+"),
            MathTex("2x"),
            MathTex("= 0")
        )

        # Arrange them horizontally with proper spacing
        elements.arrange(RIGHT, buff=0.2)

        # Create the step with the pre-arranged elements
        step = self.create_multi_exp_labeled_step_tex(
            "Custom positioning",
            elements
        )
        
        
       # self.add(step)
        
        
        
        
        horizontal_step = self.create_multi_exp_labeled_step_horizontal_tex(
            "Factored form",
            "x =", "-5", r"\pm", r"\sqrt{-13}",
            color_map={
                r"-5": BLUE,
                r"\sqrt{-13}": GREEN
            }
        )

        # For a more complex example with pre-created MathTex objects:
        radical = MathTex(r"\sqrt{-13}").set_color(GREEN)
        horizontal_step2 = self.create_multi_exp_labeled_step_horizontal_tex(
            "Complex solution",
            "x =", "-5", r"\pm", radical, "i"
        )
        
        #self.add(horizontal_step)
        #self.add(horizontal_step2)
        
        
        