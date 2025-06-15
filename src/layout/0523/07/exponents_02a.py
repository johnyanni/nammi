from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip

config.verbosity = "ERROR"

class ExponentsAddition01(MathTutorialScene):
    def construct(self):
        # ============================================
        # CONFIGURATION
        # ============================================
        BASE_COLOR = "#47e66c"      # Green for bases
        EXPONENT_COLOR = "#ff79c6"  # Pink for exponents
        RESULT_COLOR = "#00bfff"    # Blue for results
        OPERATION_COLOR = "#f1fa8c" # Yellow for operations
        
        # Problem parameters
        PROBLEM = r"2 \times 2^7 \times 2^4"
        BASE = 2
        EXPONENTS = [1, 7, 4]  # Note: first 2 has implicit exponent of 1
        
        # ============================================
        # SECTION 1: HEADER (Rules Reference)
        # ============================================
        exponent_rule_title = Tex("Exponent Multiplication Rule").scale(LABEL_SCALE)
        exponent_rule = MathTex(r"a^m \times a^n = a^{m+n}").scale(MATH_SCALE)
        
        expanded_form_title = Tex("Expanded Form").scale(LABEL_SCALE)
        expanded_example = MathTex(r"2^3 = 2 \times 2 \times 2").scale(S_MATH_SCALE)
        
        # Group rule elements
        rule_group = VGroup(
            exponent_rule_title,
            exponent_rule
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Group expanded form elements
        expanded_group = VGroup(
            expanded_form_title,
            expanded_example
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Combine both groups
        reference_group = VGroup(
            rule_group,
            expanded_group
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.7).to_corner(DR, buff=0.5).set_color(LIGHT_GRAY)
        
        # Create background rectangles
        rule_bg = SurroundingRectangle(
            rule_group,
            buff=0.25,
            fill_opacity=0.02,
            fill_color=WHITE,
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1,
            corner_radius=0.1
        )
        
        expanded_bg = SurroundingRectangle(
            expanded_group,
            buff=0.25,
            fill_opacity=0.02,
            fill_color=WHITE,
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1,
            corner_radius=0.1
        )
        
        # Color the rule components
        self.apply_smart_colorize(
            [exponent_rule, expanded_example],
            {
                "a": BASE_COLOR,
                "m": EXPONENT_COLOR,
                "n": EXPONENT_COLOR,
                "2": BASE_COLOR,
                "3": EXPONENT_COLOR,
                r"\times": OPERATION_COLOR
            }
        )
        
        # ============================================
        # SECTION 2: QUESTION
        # ============================================
        question_text = MathTex(rf"\text{{Simplify:}} \; {PROBLEM}").scale(LABEL_SCALE).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4).set_color(LIGHT_GRAY)
        
        # ============================================
        # SECTION 3: IDENTIFY SAME BASE
        # ============================================
        identify_intro = Tex("First, identify that all terms have the same base:").scale(LABEL_SCALE)
        identify_equation = MathTex(rf"2 \times 2^7 \times 2^4").scale(MATH_SCALE)
        
        identify_step = VGroup(
            identify_intro,
            identify_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse and color bases
        bases_in_equation = self.parse_elements(identify_equation,
            ('base1', '2', 0, BASE_COLOR),
            ('base2', '2', 1, BASE_COLOR),
            ('base3', '2', 2, BASE_COLOR),
            ('exp1', '7', 0, EXPONENT_COLOR),
            ('exp2', '4', 0, EXPONENT_COLOR)
        )
        
        # ============================================
        # SECTION 4: REWRITE WITH EXPLICIT EXPONENTS
        # ============================================
        rewrite_label = Tex("Rewrite the first term with an explicit exponent:").scale(LABEL_SCALE)
        rewrite_equation = MathTex(rf"2^1 \times 2^7 \times 2^4").scale(MATH_SCALE)
        
        rewrite_step = VGroup(
            rewrite_label,
            rewrite_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        source_exponents = self.parse_elements(rewrite_equation,
            ('exp1', '1', 0),
            ('exp7', '7', 0),
            ('exp4', '4', 0)
        )
        
        source_exponents_group = VGroup(
            *source_exponents.values()
        )
        
        # Color the rewritten equation
        self.apply_smart_colorize(
            [rewrite_equation],
            {
                "2": BASE_COLOR,
                "1": EXPONENT_COLOR,
                "7": EXPONENT_COLOR,
                "4": EXPONENT_COLOR,
                r"\times": OPERATION_COLOR
            }
        )
        
        # ============================================
        # SECTION 5: APPLY THE RULE
        # ============================================
        apply_label = Tex("Apply the multiplication rule for same bases:").scale(LABEL_SCALE)
        apply_formula = MathTex(r"a^m \times a^n \times a^p = a^{m+n+p}").scale(M_MATH_SCALE).set_color(LIGHT_GRAY)
        apply_equation = MathTex(r"2^{1+7+4}").scale(MATH_SCALE)
        
        apply_step = VGroup(
            apply_label,
            apply_formula,
            apply_equation
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Parse the exponent addition
        exponent_sum = self.parse_elements(apply_equation,
            ('base', '2', 0, BASE_COLOR),
            ('exp_sum', '^{1+7+4}', 0, EXPONENT_COLOR)
        )
        
        target_positions = self.parse_elements(apply_equation,
            ('target1', '1', 0),
            ('target7', '7', 0),
            ('target4', '4', 0)
        )
        
        target_positions_group = VGroup(
            *target_positions.values()
        )
        
        # ============================================
        # SECTION 6: CALCULATE THE SUM
        # ============================================
        calc_label = Tex("Add the exponents:").scale(LABEL_SCALE)
        calc_intermediate = MathTex(r"1 + 7 + 4 = 12").scale(M_MATH_SCALE).set_color(EXPONENT_COLOR)
        calc_result = MathTex(rf"2^{{12}}").scale(MATH_SCALE)
        
        calc_step = VGroup(
            calc_label,
            calc_intermediate,
            calc_result
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Color the final result
        final_result = self.parse_elements(calc_result,
            ('base', '2', 0, BASE_COLOR),
            ('exponent', '12', 0, RESULT_COLOR)
        )
        
        # ============================================
        # SECTION 7: EXPANDED VERIFICATION (Optional)
        # ============================================
        verify_label = Tex("We can verify by counting factors:").scale(LABEL_SCALE)
        verify_expansion = MathTex(
            r"2 \times \underbrace{2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2}_{7 \text{ times}} \times \underbrace{2 \times 2 \times 2 \times 2}_{4 \text{ times}}"
        ).scale(S_MATH_SCALE)
        verify_count = MathTex(r"= \underbrace{2 \times 2 \times ... \times 2}_{12 \text{ times}} = 2^{12}").scale(M_MATH_SCALE)
        
        verify_step = VGroup(
            verify_label,
            verify_expansion,
            verify_count
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # ============================================
        # SECTION 8: FINAL ANSWER
        # ============================================
        answer_label = Tex("Therefore:").scale(LABEL_SCALE)
        answer_original = MathTex(rf"2 \times 2^7 \times 2^4 = 2^{{12}}").scale(MATH_SCALE)
        answer_value = self.create_rect_group(
            MathTex(rf"2^{{12}} = 4,096").scale(MATH_SCALE),
            buff=0.15
        )
        
        answer_group = VGroup(
            answer_label,
            answer_original,
            answer_value
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Color the answer
        self.apply_smart_colorize(
            [answer_original, answer_value[0]],
            {
                "2": BASE_COLOR,
                "7": EXPONENT_COLOR,
                "4": EXPONENT_COLOR,
                "12": RESULT_COLOR,
                "4,096": RESULT_COLOR,
                r"\times": OPERATION_COLOR
            }
        )
        
        # ============================================
        # POSITION ALL SOLUTION STEPS
        # ============================================
        sol_steps = VGroup(
            identify_step,
            rewrite_step,
            apply_step,
            calc_step,
            verify_step,
            answer_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sol_steps.next_to(question_text, DOWN, buff=0.2).align_to(question_text, LEFT)
        
        # ============================================
        # CREATE SCROLL ELEMENTS
        # ============================================
        sol_steps_elements = VGroup(
            # === IDENTIFY SECTION ===
            *identify_step,
            
            # === REWRITE SECTION ===
            *rewrite_step,
            
            # === APPLY RULE SECTION ===
            *apply_step,
            
            # === CALCULATE SECTION ===
            *calc_step,
            
            # === VERIFY SECTION ===
            *verify_step,
            
            # === ANSWER SECTION ===
            *answer_group
        )
        
        scroll = ScrollManager(sol_steps_elements, scene=self)
        
        # ============================================
        # QUICK TIPS
        # ============================================
        tip_1 = QuickTip(
            r"Remember: $a = a^1$. Any number without an exponent has an implicit exponent of 1",
            color_map={"a": BASE_COLOR, "1": EXPONENT_COLOR}
        )
        tip_1.to_corner(DR)
        
        tip_2 = QuickTip(
            r"This only works when the bases are the same! $2^3 \times 3^2$ cannot be simplified this way"
        )
        tip_2.to_corner(DR)
        
        # ============================================
        # ANIMATION SEQUENCE
        # ============================================
        
        # === INTRO: Show question and rules ===
        with self.voiceover(
            text="""Let's learn how to multiply terms with exponents when they have the same base. 
            We need to simplify 2 times 2 to the seventh times 2 to the fourth."""
        ) as tracker:
            self.play(Write(question_text, run_time=4))
            
        self.wait(1)
        
        with self.voiceover(
            text="""Here's the key rule: when multiplying powers with the same base, 
            we add the exponents."""
        ) as tracker:
            self.play(FadeIn(rule_bg, run_time=1))
            self.play(Write(rule_group, run_time=3))
        
        self.wait(1)
        
        with self.voiceover(
            text="""Remember that exponents tell us how many times to multiply the base by itself."""
        ) as tracker:
            self.play(FadeIn(expanded_bg, run_time=1))
            self.play(Write(expanded_group, run_time=3))
        
        self.wait(1)
        
        # === STEP 1: Identify same base ===
        with self.voiceover(
            text="""First, let's identify that all terms have the same base of 2."""
        ) as tracker:
            scroll.prepare_next(run_time=2)
            scroll.prepare_next(run_time=2)
            
        with self.voiceover(
            text="""Notice that every term has a base of 2. <bookmark mark='A'/>
            This means we can use our multiplication rule."""
        ) as tracker:
            self.wait_until_bookmark("A")
            # Create highlights for bases
            base_highlights = VGroup()
            for base in [bases_in_equation['base1'], bases_in_equation['base2'], bases_in_equation['base3']]:
                highlight = self.create_surrounding_rectangle(base, color=BASE_COLOR)
                base_highlights.add(highlight)
            
            self.play(Create(base_highlights), run_time=2)
            self.wait(1)
            self.play(FadeOut(base_highlights))
        
        self.wait(1)
        
        # === STEP 2: Rewrite with explicit exponents ===
        with self.voiceover(
            text="""Any number without an exponent actually has an exponent of 1."""
        ) as tracker:
            self.play(FadeIn(tip_1, shift=UP))
            scroll.prepare_next(run_time=2)
            
        with self.voiceover(
            text="""So we can rewrite our first 2 as 2 to the power of 1."""
        ) as tracker:
            scroll.prepare_next(run_time=3)
            # Highlight the change
            self.play(self.indicate(rewrite_equation[0][0:2], color=EXPONENT_COLOR, run_time=2))
        
        self.wait(1)
        self.play(FadeOut(tip_1, shift=DOWN))
        
        # === STEP 3: Apply the rule ===
        with self.voiceover(
            text="""Now we can apply our multiplication rule for same bases."""
        ) as tracker:
            scroll.prepare_next(run_time=2)
            self.play(self.indicate(rule_group, scale_factor=1.2, run_time=2))
            
        with self.voiceover(
            text="""When we multiply powers with the same base, we keep the base 
            and add all the exponents together."""
        ) as tracker:
            scroll.prepare_next(run_time=2)
            scroll.prepare_next(run_time=3)
            
        # Animate the exponents coming together
        with self.voiceover(
            text="""So we get 2 to the power of 1 plus 7 plus 4."""
        ) as tracker:
            
            # self.play(self.indicate(source_exponents_group, color=YELLOW, run_time=5))
            
            for x in [source_exponents['exp1'], source_exponents['exp7'], source_exponents['exp4']]:
                self.play(self.indicate(x, color=YELLOW, run_time=2))
            
            # copies = VGroup(
            #     source_exponents['exp1'].copy(),
            #     source_exponents['exp7'].copy(),
            #     source_exponents['exp4'].copy()
            # )

            # # Animate them
            # self.play(
            #     copies[0].animate.move_to(target_positions['target1'].get_center()),
            #     copies[1].animate.move_to(target_positions['target7'].get_center()),
            #     copies[2].animate.move_to(target_positions['target4'].get_center()),
            #     run_time=2
            # )
            
            # self.play(
            #     ReplacementTransform(source_exponents['exp1'].copy(), target_positions['target1']),
            #     ReplacementTransform(source_exponents['exp7'].copy(), target_positions['target7']),
            #     ReplacementTransform(source_exponents['exp4'].copy(), target_positions['target4']),
            #     run_time=1.5
            # )

            scroll.replacement_transform_copy(
                source_exponents['exp1'],
                target_positions['target1']
            )
            
            scroll.replacement_transform_copy(
                source_exponents['exp7'],
                target_positions['target7']
            )
            
            scroll.replacement_transform_copy(
                source_exponents['exp4'],
                target_positions['target4']
            )
        
            #Fade out the copies
            # self.play(FadeOut(source_exponents.values()))
            

            
            
            #self.play(source_exponents_group.copy().animate.move_to(target_positions_group.get_center()))
            
            # self.play(
            #     TransformFromCopy(source_exponents['exp1'], target_positions['target1']),
            #     TransformFromCopy(source_exponents['exp7'], target_positions['target7']),
            #     TransformFromCopy(source_exponents['exp4'], target_positions['target4']),
            #     run_time=1.5
            # )
            
            # self.play(FadeIn(target_positions['target1'], target_position=source_exponents['exp1']))

        
            # scroll.fade_in_from_target(source_exponents['exp1'], target_positions['target1'])
            # scroll.fade_in_from_target(source_exponents['exp7'], target_positions['target7'])
            # scroll.fade_in_from_target(source_exponents['exp4'], target_positions['target4'])
            
            
            
            
            # # Create copies of exponents
            # exp_copies = VGroup(
            #     MathTex("1").scale(MATH_SCALE).set_color(EXPONENT_COLOR),
            #     MathTex("7").scale(MATH_SCALE).set_color(EXPONENT_COLOR),
            #     MathTex("4").scale(MATH_SCALE).set_color(EXPONENT_COLOR)
            # )
            
            # # Position them at original locations
            # exp_copies[0].move_to(rewrite_equation[0][1])
            # exp_copies[1].move_to(rewrite_equation[0][4])
            # exp_copies[2].move_to(rewrite_equation[0][6])
            
            # # # Animate them moving to the sum
            # # self.play(
            # #     TransformFromCopy(rewrite_equation[0][1], exp_copies[0]),
            # #     TransformFromCopy(rewrite_equation[0][4], exp_copies[1]),
            # #     TransformFromCopy(rewrite_equation[0][6], exp_copies[2]),
            # #     run_time=1.5
            # # )
            
            # self.play(
            #     exp_copies[0].animate.move_to(apply_equation[0][1]),
            #     exp_copies[1].animate.move_to(apply_equation[0][3]),
            #     exp_copies[2].animate.move_to(apply_equation[0][5]),
            #     run_time=1.5
            # )
            
            # self.play(FadeOut(exp_copies))
        
        self.wait(1)
        scroll.scroll_down(steps=2, run_time=1)
        
        # === STEP 4: Calculate the sum ===
        # with self.voiceover(
        #     text="""Now let's add the exponents: 1 plus 7 plus 4 equals 12."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=2)
        #     scroll.prepare_next(run_time=2)
            
        # with self.voiceover(
        #     text="""So our answer is 2 to the power of 12."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=2)
        #     self.play(final_result['exponent'].animate.set_color(RESULT_COLOR), run_time=1)
        
        # self.wait(1)
        
        # # === STEP 5: Verification (Optional) ===
        # with self.voiceover(
        #     text="""Let's verify this makes sense by thinking about what exponents mean."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=2)
            
        # with self.voiceover(
        #     text="""We have 1 factor of 2, then 7 factors of 2, then 4 factors of 2."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=3)
            
        # with self.voiceover(
        #     text="""That's a total of 12 factors of 2, which is 2 to the power of 12."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=3)
        
        # self.wait(1)
        # scroll.scroll_down(steps=4, run_time=1)
        
        # # === STEP 6: Final answer ===
        # with self.voiceover(
        #     text="""Therefore, our final answer is 2 to the power of 12."""
        # ) as tracker:
        #     self.play(
        #         FadeOut(reference_group),
        #         FadeOut(rule_bg),
        #         FadeOut(expanded_bg)
        #     )
        #     scroll.prepare_next(run_time=2)
        #     scroll.prepare_next(run_time=3)
            
        # with self.voiceover(
        #     text="""If we calculate this value, 2 to the 12th power equals 4,096."""
        # ) as tracker:
        #     scroll.prepare_next(run_time=3)
            
        # with self.voiceover(
        #     text="""Remember, this method only works when all the bases are the same!"""
        # ) as tracker:
        #     self.play(FadeIn(tip_2, shift=UP))
        #     self.wait(2)
            
        # self.wait(3)