from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


# class ExtendedScrollManager(ScrollManager):
#     def prepare_replacement_from(self, scene, source, target_index=None, run_time=None):
#         """Prepares a ReplacementTransform from source to the next element."""
#         if target_index is None:
#             target_index = self.current_position
            
#         if target_index >= len(self.equations):
#             return
            
#         target = self.equations[target_index]
#         run_time_dict = {} if run_time is None else {"run_time": run_time}
        
#         scene.play(ReplacementTransform(source.copy(), target), **run_time_dict)
#         self.current_position = target_index + 1
        
#     def prepare_transform_from(self, scene, source, target_index=None, run_time=None):
#         """Prepares a Transform from source to the next element."""
#         if target_index is None:
#             target_index = self.current_position
            
#         if target_index >= len(self.equations):
#             return
            
#         target = self.equations[target_index]
#         run_time_dict = {} if run_time is None else {"run_time": run_time}
        
#         scene.play(Transform(source, target), **run_time_dict)
#         self.current_position = target_index + 1

class RotatedCircumscribe(Circumscribe):
    def __init__(self, *args, angle: float = 0, **kwargs):
        super().__init__(*args, **kwargs) 
        frame = self.animations[0].mobject
        frame.rotate(angle, about_point=frame.get_center())
        

class PythagorasTheoremEnhanced(MathTutorialScene):
    def construct(self):
        triangle = Polygon(
            [-2.5, -1, 0],
            [2.5, -1, 0],
            [-2.5, 1.5, 0],
            stroke_width=0,  # No outline
            fill_color=BLUE,  # Semi-transparent blue fill
            fill_opacity=0.3,
        )

        side_a = Line(
            triangle.get_vertices()[0],
            triangle.get_vertices()[2],
            color=GREEN,
            stroke_width=6,
        )
        side_b = Line(
            triangle.get_vertices()[0],
            triangle.get_vertices()[1],
            color=RED,
            stroke_width=6,
        )
        hypotenuse = Line(
            triangle.get_vertices()[2],
            triangle.get_vertices()[1],
            color=YELLOW,
            stroke_width=6,
        )

        label_a = (
            MathTex("a = 5\\,\\text{cm}", color=GREEN)
            .scale(0.54)
            .next_to(side_a, LEFT, buff=0.4)
        )
        label_b = (
            MathTex("b = 10\\,\\text{cm}", color=RED)
            .scale(0.54)
            .next_to(side_b, DOWN, buff=0.4)
        )
        label_c = (
            MathTex("c = ?", color=YELLOW)
            .scale(0.54)
            .rotate(hypotenuse.get_angle())
            .next_to(hypotenuse.get_center(), UP, buff=0.3)
        )
        triangle_all = VGroup(
            side_a, side_b, hypotenuse, triangle, label_a, label_b, label_c
        ).center()
        triangle_shifted = triangle_all.copy().to_edge(LEFT, buff=2)
        
        label_c_res = (
            MathTex(r"c = 11.18 \; \text{cm}", color=YELLOW)
            .scale(0.54)
            .rotate(triangle_shifted[2].get_angle())
            .next_to(triangle_shifted[2].get_center(), UP, buff=0.1)
        )
        
        triangle_with_sides = VGroup(side_a, side_b, hypotenuse, triangle)

        formula = (
            MathTex("c^2 = a^2 + b^2")
            .scale(0.54)
            .next_to(triangle_all, UR, buff=0.2)
            .align_to(side_a, UP)
        )
        formula[0][:2].set_color(YELLOW)
        formula[0][3:5].set_color(GREEN)
        formula[0][6:].set_color(RED)

        formula_small = formula.copy().to_edge(RIGHT, buff=2)
        formula_small[0][:2].set_color(YELLOW)
        formula_small[0][3:5].set_color(GREEN)
        formula_small[0][6:].set_color(RED)

        VGroup(formula_small, triangle_shifted).center().shift(LEFT)
        black_box = (
            Rectangle(height=10, width=10, color=BLACK, fill_opacity=1)
            .next_to(formula_small, UP, buff=0.05)
            .set_z_index(1)
        )
        self.add(black_box)
        # Step 4: Substitute the known values
        substitute = (
            MathTex("c^2 = 5^2 + 10^2")
            .scale(0.54)
            .next_to(formula_small, DOWN, aligned_edge=LEFT)
        )
        substitute[0][:2].set_color(YELLOW)
        substitute[0][3:5].set_color(GREEN)
        substitute[0][6:].set_color(RED)

        # Step 5: Simplify the squares
        calculation_step1 = (
            MathTex("c^2 = 25 + 100")
            .scale(0.54)
            .next_to(substitute, DOWN, aligned_edge=LEFT)
        )
        calculation_step1[0][:2].set_color(YELLOW)
        calculation_step1[0][3:5].set_color(GREEN)
        calculation_step1[0][6:].set_color(RED)

        calculation_step2 = (
            MathTex("c^2 = 125", color=YELLOW)
            .scale(0.54)
            .next_to(calculation_step1, DOWN, aligned_edge=LEFT)
        )

        solve_step = (
            MathTex("c = \\sqrt{125} = 5\\sqrt{5}")
            .scale(0.54)
            .set_color(YELLOW)
            .next_to(calculation_step2, DOWN, aligned_edge=LEFT)
        )

        result_approx = (
            MathTex("c \\approx 11.18\\,\\text{cm}")
            .scale(0.54)
            .set_color(YELLOW)
            .next_to(solve_step, DOWN, aligned_edge=LEFT)
        )
        
        result_approx_surround = SurroundingRectangle(result_approx, buff=0.1, color=YELLOW)
        

        scrollable_group = VGroup(
            formula_small,
            substitute,
            calculation_step1,
            calculation_step2,
            solve_step,
            result_approx,
            result_approx_surround
        )
        
        verification_title = Text("Verification:", color=WHITE).scale(0.44).next_to(scrollable_group.copy().shift(UP*1.5), DOWN, aligned_edge=LEFT, buff=0.7)
        verification_calc = MathTex(r"c^2 \approx 124.99 = 25 + 100").scale(0.54).next_to(verification_title, DOWN, buff=0.5)
        
        verification_calc[0][:2].set_color(YELLOW)
        verification_calc[0][10:13].set_color(GREEN)
        verification_calc[0][13:].set_color(RED)
        
        black_box_layer = FullScreenRectangle(color=BLACK, fill_opacity=0.8).set_z_index(1)
        black_box_fadeout = FullScreenRectangle(color=BLACK, fill_opacity=1).set_z_index(3)
        
        # Create all elements that will be shown in sequence
        elements = VGroup(
            # Triangle elements
            side_b,
            side_a, 
            hypotenuse,
            triangle,
            label_a,
            label_b,
            label_c,
            
            # Formula elements
            formula[0][0],      # c
            formula[0][1:3],    # ^2 =
            formula[0][3],      # a
            formula[0][4:6],    # ^2 +
            formula[0][6:],     # b^2
            
            # Substitute elements
            substitute[0][:3],   # c^2 =
            substitute[0][3],    # 5
            substitute[0][4],    # ^2
            substitute[0][5],    # +
            substitute[0][6:8],  # 10
            substitute[0][-1],   # ^2
            
            # Calculation steps
            calculation_step1,
            calculation_step2,
            
            # Solve steps
            solve_step[0][0],     # c
            solve_step[0][1],     # =
            solve_step[0][2:4],   # sqrt{
            solve_step[0][4:7],   # 125}
            solve_step[0][7:],    # = 5sqrt{5}
            
            # Result
            result_approx,
            result_approx_surround,
            label_c_res[0][:2],
            label_c_res[0][2:],
            
            # Verification
            verification_title,
            verification_calc,
            
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements)
        
        # Now let's add a helper method to ScrollManager for replacement transforms
        def transform_from_target(self, scene, source, target_index, run_time=None):
            """Performs a ReplacementTransform from source to the element at target_index."""
            if target_index >= len(self.equations):
                return
            
            target = self.equations[target_index]
            scene.play(ReplacementTransform(source.copy(), target), 
                      run_time=run_time if run_time else 1)
            self.current_position = target_index + 1
            
        # Bind the method to scroll_mgr
        import types
        scroll_mgr.transform_from_target = types.MethodType(transform_from_target, scroll_mgr)
        
        '''
        ======= ANIMATION =======
        '''
        
        # First voiceover section - triangle creation
        with self.voiceover(text="""We are solving a problem involving a right-angled triangle.""") as tracker:
            scroll_mgr.prepare_next(self, animation_type=Write)  # side_b
            scroll_mgr.prepare_next(self, animation_type=Write)  # side_a
            scroll_mgr.prepare_next(self, animation_type=Write)  # hypotenuse
            scroll_mgr.prepare_next(self, animation_type=FadeIn) # triangle
            
        # Labels section
        with self.voiceover(text="""Side a is 5 centimeters<bookmark mark='b'/>, side b is 10 centimeters, and we need to find the hypotenuse<bookmark mark='c'/>, c.""") as tracker:
            scroll_mgr.prepare_next(self)  # label_a
            scroll_mgr.prepare_next(self)  # label_b
            scroll_mgr.prepare_next(self)  # label_c
            
        # Formula creation with transforms
        with self.voiceover(text="""To solve this, we use the Pythagorean <bookmark mark='c'/>Theorem: c squared equals a squared plus b squared.""") as tracker:
            # Transform c from label to formula
            scroll_mgr.transform_from_target(self, label_c[0][0], 7)  # c in formula
            scroll_mgr.prepare_next(self)  # ^2 =
            
            # Transform a
            scroll_mgr.transform_from_target(self, label_a[0][0], 9)  # a in formula
            scroll_mgr.prepare_next(self)  # ^2 +
            
            # Transform b
            scroll_mgr.transform_from_target(self, label_b[0][0], 11) # b^2
            
        # Circumscribe animations
        with self.voiceover(text="""Here, side a is equal <bookmark mark='a'/>to five centimeters, side b is equal<bookmark mark='b'/> to ten centimeters, and the hypotenuse<bookmark mark='c'/> c is unknown.""") as tracker:
            self.play(Circumscribe(label_a, color=GREEN))
            self.play(Circumscribe(label_b, color=RED))
            self.play(RotatedCircumscribe(label_c, angle=hypotenuse.get_angle(), color=YELLOW))
            
        # Substitution section
        with self.voiceover(text="""Substituting the values<bookmark mark='c'/> of a and b, we calculate c squared <bookmark mark='5'/>equals <bookmark mark='10'/>five squared plus ten squared.""") as tracker:
            # Move triangle and transform formula
            self.play(
                triangle_all.animate.to_edge(LEFT, buff=2),
                ReplacementTransform(formula, formula_small),
            )
            
            # Now continue with substitution
            scroll_mgr.transform_from_target(self, formula_small[0][:3], 12)  # c^2 =
            scroll_mgr.transform_from_target(self, label_a[0][2], 13)         # 5
            scroll_mgr.transform_from_target(self, formula_small[0][4], 14)   # ^2
            scroll_mgr.prepare_next(self)                                      # +
            scroll_mgr.transform_from_target(self, label_b[0][2:4], 16)       # 10
            scroll_mgr.transform_from_target(self, formula_small[0][-1], 17)  # ^2
            
        # Calculation steps
        with self.voiceover(text="""Five squared equals twenty-five, and ten squared equals one hundred.""") as tracker:
            scroll_mgr.transform_from_target(self, substitute[0][:], 18)  # calculation_step1
            
        with self.voiceover(text="""Adding these together, we find that c squared equals one hundred and twenty-five.""") as tracker:
            scroll_mgr.prepare_next(self)  # calculation_step2
            
        # Solve steps
        with self.voiceover(text="""To find c, we take the<bookmark mark='sqrt'/> square root of one hundred and twenty-five. This simplifies <bookmark mark='simplify'/>to five times the square root of five.""") as tracker:
            # Complex transform for solve_step
            scroll_mgr.transform_from_target(self, calculation_step2[0][0], 20)    # c
            scroll_mgr.transform_from_target(self, calculation_step2[0][2], 21)    # =
            scroll_mgr.prepare_next(self)                                           # sqrt{
            scroll_mgr.transform_from_target(self, calculation_step2[0][3:], 23)   # 125}
            scroll_mgr.prepare_next(self)                                           # = 5sqrt{5}
            
        # Result section
        with self.voiceover(text="""Approximating the square root, we find that<bookmark mark='approx'/> c is approximately eleven point one eight centimeters.""") as tracker:
            scroll_mgr.prepare_next(self)  # result_approx
            scroll_mgr.prepare_next(self)  # result_approx_surround
            
            # Transform label_c to label_c_res
            self.play(
                Transform(label_c[0][0:2], scroll_mgr.equations[27]),
                FadeOut(label_c[0][2]),
                ReplacementTransform(result_approx[0][2:].copy(), scroll_mgr.equations[28])
            )
            scroll_mgr.current_position = 29
            
        # Verification section
        with self.voiceover(text="""Now, let's verify our answer by <bookmark mark='substitute'/>substituting it back into the Pythagorean Theorem.""") as tracker:
            self.play(scrollable_group.animate.shift(UP * 1.5))
            scroll_mgr.prepare_next(self)  # verification_title
            scroll_mgr.prepare_next(self)  # verification_calc
            
        with self.voiceover(text="""This calculation shows that the hypotenuse is verified as correct.""") as tracker:
            scroll_mgr.prepare_next(self, animation_type=FadeIn)  # black_box_layer                    # tick
            scroll_mgr.prepare_next(self, animation_type=FadeIn)  # black_box_fadeout
            
        self.wait()  
        
            
        # Verification section
        with self.voiceover(text="""Now, let's verify our answer by <bookmark mark='substitute'/>substituting it back into the Pythagorean Theorem.""") as tracker:
            self.play(scrollable_group.animate.shift(UP * 1.5))
            scroll_mgr.prepare_next(self)  # verification_title
            scroll_mgr.prepare_next(self)  # verification_calc
