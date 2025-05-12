from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager
from src.components.common.trig_helper import *


class TrigRatiosSolvingForASide01a(MathTutorialScene):
    def create_triangle(self, A, B, C):
        triangle = Polygon(A, B, C, color=WHITE)
        right_angle = Angle.from_three_points(C, A, B, elbow=True)       
        angle = Angle.from_three_points(B, C, A, radius=0.8, color=WHITE)
        return triangle, right_angle, angle
    
    def construct(self):
        
        # Create triangle vertices
        A = 2 * LEFT + 2 * UP
        B = 0.2 * RIGHT + 2 * UP  
        C = 2 * LEFT + 2 * DOWN      
        triangle, right_angle, angle = self.create_triangle(A, B, C)

        # Create theta components
        theta_sign_position = get_normal(angle.get_end(), angle.get_start(), length=0.4)      
        theta_sign = MathTex(r"\theta", color=BLUE).move_to(theta_sign_position.get_end())  
        
        theta_position = get_normal(B, C, proportion=0.4, length=1.1, angle=40*DEGREES)
        theta = MathTex(r"20 ^\circ 32'", color=BLUE).move_to(theta_position.get_end())
        theta_arrow = curved_arrow_to_angle(theta, angle, start_direction='left', radius=-PI/2, buff_from_mob=0.2)

        # Create adjacent and opposite labels
        adj_position = Line(A, C).point_from_proportion(0.4)
        adj_length = Tex(r"28cm", color=RED).next_to(adj_position, LEFT, buff=0.3)
        adj_label = Tex(r"Adj", color=RED).scale(0.5).next_to(adj_length, DOWN, buff=0.2)

        opp_position = get_normal(A, B, length=0.7)
        opp_length = MathTex(r"x", color=GREEN).move_to(opp_position.get_end())
        opp_label = Tex(r"Opp", color=GREEN).scale(0.5).next_to(opp_length, DOWN, buff=0.2)

        # Group all triangle elements
        all_elements = VGroup(
            triangle, right_angle, angle,
            theta_sign, theta, theta_arrow,
            adj_length, adj_label,
            opp_length, opp_label
        ).move_to(ORIGIN).shift(UP)

        # Create SOH-CAH-TOA elements
        soh = Tex(r"SOH", color=BLUE).scale(TEXT_SCALE)
        cah = Tex(r"CAH", color=BLUE).scale(TEXT_SCALE)
        toa = Tex(r"TOA", color=BLUE).scale(TEXT_SCALE)
        sct = VGroup(soh, cah, toa).arrange(RIGHT, aligned_edge=LEFT, buff=2.5).to_edge(DOWN)

        # Create TOA expansions
        toa_lst = ["Tan", "Opp", "Adj"]
        expansions = get_expanded_expression(toa, toa_lst)
        sct_with_expansions = VGroup(sct, *expansions)

         # Create solution steps
        title = Tex(r"Given:", color=WHITE).scale(TEXT_SCALE)
        theta_eq = MathTex(r"\theta = 20^\circ 32'", color=BLUE).scale(MATH_SCALE)
        adj_eq = MathTex(r"\text{Adjacent} = 28\text{ cm}", color=RED).scale(MATH_SCALE)

        ratio_text = Tex(r"Use the tangent ratio:", color=WHITE).scale(TEXT_SCALE)
        ratio_eq = MathTex(r"\tan \theta = \frac{\text{Opposite}}{\text{Adjacent}}").scale(MATH_SCALE)
        subs_eq = MathTex(r"\tan(20^\circ 32') = \frac{x}{28}").scale(MATH_SCALE)

        mult_text = Tex(r"Multiply by 28:", color=WHITE).scale(TEXT_SCALE)
        mult_step = MathTex(r"28 \cdot \tan(20^\circ 32') = 28 \cdot \frac{x}{28}").scale(MATH_SCALE)
        mult_simp = MathTex(r"28 \cdot \tan(20^\circ 32') = x").scale(MATH_SCALE)

        decimal_text = Tex(r"Convert to decimal:", color=WHITE).scale(TEXT_SCALE)
        
        # Create DMS step components with Tex
        dms_parts = VGroup(
            Tex(r"tan", color=WHITE),
            Tex(r"20", color=BLUE),
            Tex(r"DMS", color=YELLOW),
            Tex(r"32", color=BLUE),
            Tex(r"DMS", color=YELLOW),
            Tex(r"=", color=WHITE),
            Tex(r"0.374513", color=WHITE)
        ).scale(MATH_SCALE)

        # Arrange parts with even spacing
        dms_parts.arrange(RIGHT, buff=0.4)
        
        # Create yellow boxes around specific terms
        dms_box = SurroundingRectangle(dms_parts[2], color=YELLOW, buff=0.1)  # Get reference height from first DMS
        boxes = VGroup(
            SurroundingRectangle(dms_parts[0], color=YELLOW, buff=0.1).stretch_to_fit_height(dms_box.height),
            SurroundingRectangle(dms_parts[2], color=YELLOW, buff=0.1),
            SurroundingRectangle(dms_parts[4], color=YELLOW, buff=0.1),
            SurroundingRectangle(dms_parts[5], color=YELLOW, buff=0.1).stretch_to_fit_height(dms_box.height)
        )

        dms_group = VGroup(dms_parts, boxes)

        therefore = Tex(r"Therefore:", color=WHITE).scale(TEXT_SCALE)
        final_step = MathTex(r"x = 28 \cdot 0.374513").scale(MATH_SCALE)
        final_ans = MathTex(r"x = 10.49\text{ cm}").scale(MATH_SCALE)

        # Group all solution steps
        solution_steps = VGroup(
            title, theta_eq, adj_eq,
            ratio_text, ratio_eq, subs_eq,
            mult_text, mult_step, mult_simp,
            decimal_text, dms_group,
            therefore, final_step, final_ans
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(LEFT, buff=1).to_edge(UP, buff=0.7)

        # Apply colors
        color_map = {
            r"\theta": BLUE,
            r"\tan": BLUE,
            r"20^\circ 32'": BLUE,
            "10.49": GREEN,
            "28": RED,
            "x": GREEN,
            r"\text{Opposite}": GREEN,
            r"\text{Adjacent}": RED,
        }

        math_steps = [theta_eq, adj_eq, ratio_eq, subs_eq, mult_step, 
                     mult_simp, final_step, final_ans]
        for step in math_steps:
            SmartColorizeStatic(step, color_map)

        # Create ScrollManager
        scroll_manager = ScrollManager(solution_steps)

        # Animation sequence
        with self.voiceover(text="Let's solve this right triangle step by step."):
            self.play(Create(triangle))
            self.play(Create(right_angle))
            self.play(Create(angle))
  
        with self.voiceover(text="Here we have an angle theta measuring 20 degrees and 32 minutes."):
            self.play(Write(theta_sign))
            self.play(Write(theta))
            self.play(Create(theta_arrow))
        
        with self.voiceover(text="The adjacent side is 28 centimeters long, and we need to find the length x of the opposite side."):
            self.play(Write(adj_length), Write(adj_label))
            self.play(Write(opp_length), Write(opp_label))
            self.wait(0.5)

        with self.voiceover(text="Let's move our triangle to the side to make space for our solution."):
            self.play(all_elements.animate.shift(4 * RIGHT).scale(0.9), run_time=1)
            self.wait(0.5)

        with self.voiceover(text="Since we have the adjacent side and need the opposite, we'll use the tangent ratio from SOH CAH TOA."):
            self.play(Write(soh))
            self.play(Write(cah))
            self.play(Write(toa))
            for expansion in expansions:
                self.play(Create(expansion[0]), Write(expansion[1]))
            self.wait(0.5)
        
        self.play(sct_with_expansions.animate.scale(0.5/0.7).to_edge(DOWN), run_time=1)

        # Solution steps with voiceover tracking
        with self.voiceover(text="Let's start with our given values."):
            scroll_manager.prepare_next(self)  # Given
            scroll_manager.prepare_next(self)  # theta_eq
            scroll_manager.prepare_next(self)  # adj_eq
            self.wait(0.5)

        with self.voiceover(text="Using the tangent ratio, which is opposite over adjacent."):
            scroll_manager.scroll_down(self, steps=1)
            scroll_manager.prepare_next(self)  # ratio_text
            scroll_manager.prepare_next(self)  # tan_ratio
            self.wait(0.5)

        with self.voiceover(text="Let's substitute our angle of 20 degrees 32 minutes, and replace opposite with x and adjacent with 28."):
            scroll_manager.prepare_next(self)  # tan with values
            self.wait(1)
        
        with self.voiceover(text="To isolate x, multiply both sides by 28."):
            scroll_manager.scroll_down(self, steps=2)
            scroll_manager.prepare_next(self)  # Multiply by 28
            scroll_manager.prepare_next(self)  # Multiplication step
            scroll_manager.prepare_next(self)  # Simplified equation
            self.wait(0.5)

        # Calculator evaluation steps
        with self.voiceover(text="Now we can evaluate tangent of 20 degrees 32 minutes on our calculator."):
            scroll_manager.scroll_down(self, steps=2)
            scroll_manager.prepare_next(self)  # Convert to decimal text
            self.wait(0.3)
        
        # Separate DMS step explanation
        with self.voiceover(text="Use DMS mode to handle degrees and minutes."):
            scroll_manager.prepare_next(self)  # DMS step
            self.wait(0.5)

        with self.voiceover(text="Finally, multiply by 28 to get our answer."):
            scroll_manager.scroll_down(self, steps=2)
            scroll_manager.prepare_next(self)  # Therefore
            scroll_manager.prepare_next(self)  # Final calculation
            scroll_manager.prepare_next(self)  # Answer
            self.wait(0.5)

         # Final confirmation
        with self.voiceover(text="So the opposite side of our triangle is 10.49 centimeters long."):
            self.wait(1)
            

        self.wait(2)