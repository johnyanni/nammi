from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

# Import our components
from components.common.scroll_manager import ScrollManager
from components.common.quick_tip import QuickTip
from components.common.smart_tex import *

class ProbabilityVennDiagram(VoiceoverScene):
    def construct(self):
        # Configure for preview
        config.preview = True
        config["preview"] = True
        config.background_color = "#121212"  # Set background color in config
        
        self.set_speech_service(
            AzureService(
                voice="en-US-DerekMultilingualNeural",
                prosody={
                    "rate": "-15%",  # This makes it 20% slower
                }
            )
        )
        self.camera.background_color = "#121212"






         # Constants
        LEFT_CIRCLE_COLOR = BLUE  # For "D" and "Dogs"
        RIGHT_CIRCLE_COLOR = RED  # For "C" and "Cats"
        INTERSECTION_COLOR = YELLOW  # For "D & C"
        SAMPLE_COLOR = GREEN  # For "50"
        
        TEX_SCALE = 0.7
        
        
        
        # Constants for timing
        QUICK_PAUSE = 0.5
        STANDARD_PAUSE = 1.0
        COMPREHENSION_PAUSE = 2.0
        



        ADD_RULE_COLOR_MAP = {
            "A": LEFT_CIRCLE_COLOR,
            "B": RIGHT_CIRCLE_COLOR,
            r"A \text{ and } B": INTERSECTION_COLOR
        }

        add_rule_formula = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(0.6)
        SmartColorizeStatic(
            add_rule_formula,
            ADD_RULE_COLOR_MAP
        )

        add_rule_box = SurroundingRectangle(add_rule_formula, buff=0.2, corner_radius=0.1)
        add_rule = VGroup(add_rule_formula, add_rule_box)
        




        # Venn Diagram
        left_circle = Circle(radius=1.5, color=LEFT_CIRCLE_COLOR).shift(LEFT)
        right_circle = Circle(radius=1.5, color=RIGHT_CIRCLE_COLOR).shift(RIGHT)
        left_label = Tex("Dogs", color=LEFT_CIRCLE_COLOR).scale(TEX_SCALE).next_to(left_circle, UP).shift(LEFT * 0.5)
        right_label = Tex("Cats", color=RIGHT_CIRCLE_COLOR).scale(TEX_SCALE).next_to(right_circle, UP).shift(RIGHT * 0.5)
        intersection = Intersection(left_circle, right_circle, color=INTERSECTION_COLOR, fill_opacity=0.5)

        intersection_label = Tex("9", color=BLACK).move_to(intersection)
        left_circle_label = Tex("26", color=LEFT_CIRCLE_COLOR).move_to(left_circle).shift(LEFT * 0.5)
        right_circle_label = Tex("8", color=RIGHT_CIRCLE_COLOR).move_to(right_circle).shift(RIGHT * 0.5)

        sample = MathTex(r"\text{Total} = 50 \text{ homes }", color=SAMPLE_COLOR).scale(TEX_SCALE).next_to(right_circle, DOWN * 2)

        full_venn = VGroup(
            left_circle, right_circle, intersection,
            left_label, right_label,
            left_circle_label, right_circle_label, intersection_label,
            sample
        )

        right_section = VGroup(
            add_rule,
            full_venn
        ).arrange(DOWN, buff=0.4, aligned_edge=RIGHT)

        right_section.to_edge(RIGHT, buff=0.6).to_edge(UP, buff=0.6)


    
    
        # Tips
        tip_1 = QuickTip(
            "Not mutually exclusive means that both events can occur simultaneously",
            fill_opacity=1
        ).shift(DOWN * 2)


       # First, create standard spacing constants
        TEXT_SCALE = 0.5
        MATH_SCALE = 0.6
        
        problem_text = Tex(
            "Q. In a neighborhood survey of 50 homes,\\\\",
            "35 homes have dogs, 17 homes have cats,\\\\",
            "and 9 homes have both pets.\\\\",
            "What is the probability that a randomly\\\\",
            "selected home has either a dog or a cat?"
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(TEXT_SCALE).to_edge(LEFT, buff=0.7).to_edge(UP, buff=0.7)

        # Create all individual steps
        step1_title = Tex("Step 1: Given Information").scale(TEXT_SCALE)
        step1_info_1 = MathTex(r"\text{Total homes} = 50", color=SAMPLE_COLOR).scale(MATH_SCALE)
        step1_info_2 = MathTex(r"\text{Homes with dogs (D)} = 35", color=LEFT_CIRCLE_COLOR).scale(MATH_SCALE)
        step1_info_3 = MathTex(r"\text{Homes with cats (C)} = 17", color=RIGHT_CIRCLE_COLOR).scale(MATH_SCALE)
        step1_info_4 = MathTex(r"\text{Homes with both (D) and (C)} = 9", color=INTERSECTION_COLOR).scale(MATH_SCALE)

        step2_title = Tex("Step 2: Addition Rule of Probability").scale(TEXT_SCALE)
        step2_formula = MathTex(r"\text{P(Dog or Cat)} = P(D) + P(C) - P(D \text{ and } C)").scale(MATH_SCALE)

        step3_title = Tex("Step 3: Calculate").scale(TEXT_SCALE)
        step3_calc_1 = MathTex(r"\text{P(Dog or Cat)} = \frac{35}{50} + \frac{17}{50} - \frac{9}{50}").scale(MATH_SCALE)
        step3_calc_2 = MathTex(r"\text{P(Dog or Cat)} = \frac{35 + 17 - 9}{50}").scale(MATH_SCALE)
        step3_calc_3 = MathTex(r"\text{P(Dog or Cat)} = \frac{43}{50}").scale(MATH_SCALE)

        step4_title = Tex("Step 4: Verify with Venn Diagram").scale(TEXT_SCALE)
        step4_calc_1 = MathTex(r"\text{Dogs only} = 35 - 9 = 26").scale(MATH_SCALE)
        step4_calc_2 = MathTex(r"\text{Cats only} = 17 - 9 = 8").scale(MATH_SCALE)
        step4_calc_3 = MathTex(r"\text{Both} = 9").scale(MATH_SCALE)
        step4_calc_4 = MathTex(r"\text{Total with either} = 26 + 8 + 9 = 43").scale(MATH_SCALE)

        final_answer = MathTex(
            r"P(\text{Dog or Cat}) = \frac{43}{50}"
        ).scale(MATH_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        
        
        COLOR_MAP = {
            r"\text{Dog}": LEFT_CIRCLE_COLOR,
            r"\text{Cat}": RIGHT_CIRCLE_COLOR,
            "D": LEFT_CIRCLE_COLOR,
            "C": RIGHT_CIRCLE_COLOR,
            r"D \text{ and } C": INTERSECTION_COLOR,
            "50": SAMPLE_COLOR,
            "35": LEFT_CIRCLE_COLOR,
            "17": RIGHT_CIRCLE_COLOR,
            "9": INTERSECTION_COLOR,
            "26": LEFT_CIRCLE_COLOR,
            "8": RIGHT_CIRCLE_COLOR,
            r"\text{Dogs only}": LEFT_CIRCLE_COLOR,
            r"\text{Cats only}": RIGHT_CIRCLE_COLOR,
            r"\text{Both}": INTERSECTION_COLOR,
            r"\text{Total with either}": SAMPLE_COLOR
        }
        
        # After creating all the math elements but before grouping, apply colors
        math_steps = [
            step2_formula,
            step3_calc_1, step3_calc_2, step3_calc_3,
            step4_calc_1, step4_calc_2, step4_calc_3, step4_calc_4,
            final_answer
        ]

        # Apply colors to all math elements
        for step in math_steps:
            SmartColorizeStatic(step, COLOR_MAP)
        
        
        COLOR_MAP2 = {
            "50": SAMPLE_COLOR,
            "35": LEFT_CIRCLE_COLOR,
            "17": RIGHT_CIRCLE_COLOR,
            "9": INTERSECTION_COLOR,
            "26": LEFT_CIRCLE_COLOR,
            "8": RIGHT_CIRCLE_COLOR,
        }
        
        # After creating all the math elements but before grouping, apply colors
        second_steps = [
            step4_calc_1, step4_calc_2, step4_calc_3, step4_calc_4
        ]

        # Apply colors to all math elements
        for second_step in second_steps:
            SmartColorizeStatic(second_step, COLOR_MAP2)
            
        

        step1_group = VGroup(
            step1_title, 
            step1_info_1, step1_info_2, step1_info_3, step1_info_4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step2_group = VGroup(
            step2_title,
            step2_formula
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        step3_group = VGroup(
            step3_title,
            step3_calc_1, step3_calc_2, step3_calc_3
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        step4_group = VGroup(
            step4_title,
            step4_calc_1, step4_calc_2, step4_calc_3, step4_calc_4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Arrange groups vertically with larger buffer
        groups = VGroup(step1_group, step2_group, step3_group, step4_group, final_answer).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        
        # Now create solution_steps using the positioned elements
        solution_steps = VGroup(
            step1_title, 
            step1_info_1, step1_info_2, step1_info_3, step1_info_4,
            step2_title,
            step2_formula,
            step3_title,
            step3_calc_1, step3_calc_2, step3_calc_3,
            step4_title,
            step4_calc_1, step4_calc_2, step4_calc_3, step4_calc_4,
            final_answer
        )

        # Position the entire solution
        solution_steps.to_edge(LEFT, buff=0.7).to_edge(UP, buff=0.7)

        # Create scroll manager with our solution steps
        scroll_mgr = ScrollManager(solution_steps)
        
        # Display problem with voiceover
        with self.voiceover(
            text="""In a neighborhood survey of 50 homes, 35 homes have dogs, 
            17 homes have cats, and 9 homes have both pets. 
            What is the probability that a randomly selected home has either a dog or a cat?"""
        ):
            self.play(FadeIn(problem_text))
            self.wait(0.5)  # Small pause after fade in
            
        with self.voiceover("This venn diagram will represent two sets: homes with dogs and homes with cats."):
            self.play(Succession(
                Create(left_circle),
                FadeIn(left_label),
                Create(right_circle),
                FadeIn(right_label),
                Write(sample)
            ))
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("Since some homes can have both pets, we have an overlapping region shown in yellow."):
            self.play(
                Create(intersection),
                intersection.animate.set_fill(opacity=0.5),
                run_time=1.5
            )
            self.wait(STANDARD_PAUSE)
        
        # Addition Rule Introduction
        with self.voiceover("We want to find the probability of a home having dogs or cats. <bookmark mark='rule'/> We can use the addition rule."):
            self.wait_until_bookmark("rule")
            self.play(Write(add_rule))
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("This rule is important because our sets <bookmark mark='overlap'/> overlap."):
            self.wait_until_bookmark("overlap")
            self.play(Indicate(intersection, scale_factor=1.2))
            self.wait(QUICK_PAUSE)
        
        # Step 1: Given Information
        with self.voiceover("Let's start with what we know."):
            self.play(FadeOut(problem_text))
            self.wait(0.5)
            scroll_mgr.prepare_next(self)  # step1_title
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("From our survey of 50 homes..."):
            scroll_mgr.prepare_next(self)  # step1_info_1
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("35 homes have dogs..."):
            scroll_mgr.prepare_next(self)  # step1_info_2
            self.play(Indicate(left_circle))
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("17 homes have cats..."):
            scroll_mgr.prepare_next(self)  # step1_info_3
            self.play(Indicate(right_circle))
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("And 9 homes have both pets."):
            scroll_mgr.prepare_next(self)  # step1_info_4
            self.play(Indicate(intersection))
            self.wait(STANDARD_PAUSE)
        
        # Step 2: Addition Rule Application
        with self.voiceover("Now, let's use the addition rule to find the probability of a home having either pet. <bookmark mark='tip_1'/> Notice these events are not mutually exclusive."):
            scroll_mgr.prepare_next(self)  # step2_title
            self.play(Indicate(add_rule))
            self.wait_until_bookmark("tip_1")
            self.play(FadeIn(tip_1, shift=UP))
            self.wait(4)
            self.play(FadeOut(tip_1, shift=DOWN))
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("According to the rule, we add the individual probabilities and subtract their overlap."):
            scroll_mgr.prepare_next(self)  # step2_formula
            self.wait(COMPREHENSION_PAUSE)
        
        # Step 3: Calculations
        with self.voiceover("Let's plug in our values."):
            scroll_mgr.prepare_next(self)  # step3_title
            self.wait(QUICK_PAUSE)
        
        with self.voiceover("We have 35 out of 50 homes with dogs, plus 17 out of 50 with cats..."):
            scroll_mgr.prepare_next(self)  # step3_calc_1
            scroll_mgr.scroll_down(self, steps=5)
            self.wait(COMPREHENSION_PAUSE)
        
        with self.voiceover("But we've counted the 9 homes with both pets twice, so we subtract them once."):
            self.play(
                Indicate(intersection),
                intersection.animate.set_fill(opacity=0.8)
            )
            self.wait(COMPREHENSION_PAUSE)
            scroll_mgr.prepare_next(self)  # step3_calc_2
        
        with self.voiceover("This gives us 43 out of 50 homes."):
            scroll_mgr.prepare_next(self)  # step3_calc_3
            self.wait(COMPREHENSION_PAUSE)
        
        # Step 4: Verification with Diagram
        with self.voiceover("Let's verify this using our Venn diagram."):
            scroll_mgr.prepare_next(self)  # step4_title
            scroll_mgr.scroll_down(self, steps=4)
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("26 homes have only dogs..."):
            scroll_mgr.prepare_next(self)  # step4_calc_1
            self.play(Indicate(left_circle_label))
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("8 homes have only cats..."):
            scroll_mgr.prepare_next(self)  # step4_calc_2
            self.play(Indicate(right_circle_label))
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("9 homes have both pets..."):
            scroll_mgr.prepare_next(self)  # step4_calc_3
            self.play(Indicate(intersection_label))
            self.wait(STANDARD_PAUSE)
        
        with self.voiceover("Adding these up: 26 plus 8 plus 9 equals 43 homes total."):
            scroll_mgr.prepare_next(self)  # step4_calc_4
            self.wait(STANDARD_PAUSE)
        
        # Final Answer
        with self.voiceover("Therefore, the probability of a randomly selected home having either a dog or a cat is 43 out of 50."):
            scroll_mgr.prepare_next(self)  # final_answer
            self.play(Create(SurroundingRectangle(final_answer, buff=0.2)))
            self.wait(COMPREHENSION_PAUSE)
        
        # Final pause for comprehension
        self.wait(2)