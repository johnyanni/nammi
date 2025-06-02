from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.common.slope_overlay import SlopeOverlay
from src.components.common.full_screen_overlay import FullScreenOverlay


class Asymptote(MathTutorialScene):
    
    def create_surrounding_rectangle(
            self,
            mobject,
            color="#9A48D0",
            corner_radius=0.1, buff=0.15
    ):
        return SurroundingRectangle(mobject, color=color, corner_radius=corner_radius, buff=buff)
    
    def construct(self):
        
        # Constants for scaling
        TEX_SCALE = 0.70
        AXES_SCALE = 0.65

        # Quadrant
        QUADRANT_COLOR = BLUE 
        QUADRANT_OPACITY = 0.2

        # Axes
        ASYMPTOTE_COLOR = RED
        POINT_COLOR = "#FF4081"
        POINT_RADIUS = 0.12

        # Graph
        GRAPH_COLOR = PURPLE
        
        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"
        EQUATION_BG_WIDTH = 2
        EQUATION_BG_OPACITY = 0.1
        EQUATION_BG_radius = 0.3

        # Indicate Animation
        INDICATION_COLOR = "#9A48D0"
        INDICATION_TIME = 2.0

        # Equation Colors
        DIVISOR_COLOR = "#FF7043"  # Orange-red for divisor (x - 3)
        DIVIDEND_COLOR = "#4DB6AC"  # Teal for dividend (4x - 10)
        REMAINDER_COLOR = "#FFD54F"  # Amber for remainder (2)
        A_COLOR = "#FFD54F"  # Same as remainder
        K_COLOR = "#64B5F6"  # Light blue for k value
        STEP_COLOR = "#90A4AE" # Blue-Gray for steps
        
        EQ_VBUFF = 0.35
        STANDARD_EQ_HBUFF = 0.2
        WIDE_EQ_HBUFF = 0.75
        
        LABEL_SCALE = 0.5
        LABEL_COLOR = GREY
        LABEL_BUFF = 0.2
            
        # Constants for timing
        QUICK_PAUSE = 0.5
        STANDARD_PAUSE = 1.0
        COMPREHENSION_PAUSE = 2.0

    

        # Axes 
        axes = CustomAxes(
            x_range=[-.5, 7, 1],
            y_range=[-.5, 8, 1],
            x_length=8,
            y_length=9,
        ).scale(AXES_SCALE).to_corner(UR).shift(UP * 0.2)
        axes.add_coordinates(range(0, 7), range(0, 8))

        v_asymptote = DashedLine(
            start=axes.c2p(3, -1.2),
            end=axes.c2p(3, 9),
            color=ASYMPTOTE_COLOR
        )

        h_asymptote = DashedLine(
            start=axes.c2p(-1, 4),
            end=axes.c2p(8, 4),
            color=ASYMPTOTE_COLOR
        )

        first_quadrant = Polygon(
            axes.c2p(3, 4),
            axes.c2p(8, 4),
            axes.c2p(8, 9),
            axes.c2p(3, 9),
            fill_opacity=QUADRANT_OPACITY,
            fill_color=QUADRANT_COLOR,
            stroke_width=0
        )

        third_quadrant = Polygon(
            axes.c2p(-0.5, -0.5),
            axes.c2p(3, -0.5),
            axes.c2p(3, 4),
            axes.c2p(-0.5, 4),
            fill_opacity=QUADRANT_OPACITY,
            fill_color=QUADRANT_COLOR,
            stroke_width=0
        )

        point1 = Dot(axes.c2p(2, 2), color=POINT_COLOR, radius=POINT_RADIUS)
        point2 = Dot(axes.c2p(4, 6), color=POINT_COLOR, radius=POINT_RADIUS)
        
        func = lambda x: 2 / (x - 3) + 4

        left_x_range = [-1, 2.6]
        right_x_range = [3.48, 7.5]

        left_graph = axes.plot(
            func,
            x_range=left_x_range,
            discontinuities=[3],
            dt=0.1,
            color=GRAPH_COLOR
        )

        right_graph = axes.plot(
            func,
            x_range=right_x_range,
            discontinuities=[3],
            dt=0.1,
            color=GRAPH_COLOR
        )

        graph = VGroup(left_graph, right_graph)
        
        # Equations
        general_form = VGroup(
            MathTex(r"y = \frac{a}{x - h} + k"),
            MathTex("Y = k"),
            MathTex("X = h")
        ).arrange(buff=WIDE_EQ_HBUFF).scale(TEX_SCALE).to_edge(DOWN).shift(RIGHT * 0.7)

        self.apply_smart_colorize(
            general_form,
            {
                "x - h": DIVISOR_COLOR,
                "a": A_COLOR,
                "k": K_COLOR,
                "h": DIVISOR_COLOR,
            }
        )

        y_callout = self.create_callout("Horizontal Asymptote", general_form[1], animate=False)
        x_callout = self.create_callout("Vertical Asymptote", general_form[2], animate=False)
        
        equation_bg = SurroundingRectangle(
            general_form,
            buff=0.2,
            corner_radius=EQUATION_BG_radius,
            fill_opacity=EQUATION_BG_OPACITY,
            fill_color=EQUATION_BG_FILL,  
            stroke_color=EQUATION_BG_STROKE, 
            stroke_width=EQUATION_BG_WIDTH
        )

        general_form_group = VGroup(general_form, equation_bg)

        example_func = MathTex(r"y = \frac{4x - 10}{x - 3}").scale(TEX_SCALE)
        example_func_den = example_func[0][search_shape_in_text(example_func, MathTex("4x - 10"))[0]].set_color(DIVIDEND_COLOR)
        example_func_num = example_func[0][search_shape_in_text(example_func, MathTex("x - 3"))[0]].set_color(DIVISOR_COLOR)
        
        blank_screen = FullScreenOverlay("Effect of the sign of a")
        
        # Step 1: Long division
        division_setup = MathTex(r"x - 3\ \overline{\strut \smash{)}\ 4x - 10\ }")
        division_symbol = division_setup[0][3:5] 
        divisor = division_setup[0][search_shape_in_text(division_setup, MathTex("x - 3"))[0]].set_color(DIVISOR_COLOR)
        dividend = division_setup[0][search_shape_in_text(division_setup, MathTex("4x - 10"))[0]].set_color(DIVIDEND_COLOR)

        
        division_step_1 = MathTex("-(4x - 12)").next_to(division_setup, DOWN).shift(RIGHT * 0.6).set_color(STEP_COLOR)
        division_step_1_4x = division_step_1[0][search_shape_in_text(division_step_1, MathTex("4x"))[0]]
        division_step_1_12 = VGroup(
            division_step_1[0][search_shape_in_text(division_step_1, MathTex("-"))[1]],
            division_step_1[0][search_shape_in_text(division_step_1, MathTex("12"))[0]]
        )
        division_step_1_rem = VGroup(
            *[
                division_step_1[0][group]
                for group in search_shapes_in_text(division_step_1, [MathTex("-("), MathTex(")")])
            ]
        )

        hline = Line(division_step_1.get_left(), division_step_1.get_right(), stroke_width=1.5).next_to(division_step_1, DOWN)

        zero = MathTex("0").match_x(division_step_1_4x)
        two = MathTex("2").match_x(division_step_1_12)
        division_step_2 = VGroup(zero, two).set_color(STEP_COLOR).next_to(hline, DOWN)
        
        division_step_2_arrow = MathTex(r"\longrightarrow").next_to(division_step_2, RIGHT)
        quotient = MathTex("4", color=K_COLOR).next_to(division_setup, UP)
        
        remainder = MathTex("r = 2", color=REMAINDER_COLOR).next_to(division_step_2_arrow, RIGHT * 1.5)
        remainder_rec = self.create_surrounding_rectangle(remainder)
        remainder_group = VGroup(remainder, remainder_rec)
        
        division_steps = VGroup(
            division_symbol,
            divisor,
            dividend,
            quotient,
            division_step_1_4x,
            division_step_1_12,
            division_step_1_rem,
            hline,
            zero,
            two, 
            division_step_2_arrow,
            remainder,
            remainder_rec
        ).scale(TEX_SCALE)

        step_1 = self.create_labeled_step(
            "Step 1: Do the long division",
            division_steps,
        )
        step_1_label = step_1[0]

        
        simplified_y = MathTex(r"x = \sqrt{45} = -2").scale(TEX_SCALE)
        SmartColorizeStatic(
            simplified_y,
            {
                "2": A_COLOR,
                "x - 3": DIVISOR_COLOR,
                "4": K_COLOR
            }
        )
        simplified_y_term_1 = simplified_y[0][search_shape_in_text(simplified_y, MathTex("x ="))[0]]
        simplified_y_term_2 = simplified_y[0][search_shape_in_text(simplified_y, MathTex(r"\sqrt{45}"))[0]]
        simplified_y_term_3 =VGroup(
            simplified_y[0][search_shape_in_text(simplified_y, MathTex("-"))[0]],
            simplified_y[0][search_shape_in_text(simplified_y, MathTex("2"))[0]]
        )
        

        
        scroll = ScrollManager(simplified_y_term_1)
        scroll.prepare_next(self)

        general_y = MathTex(r"y = \frac{1}{x}", color=RED).scale(TEX_SCALE).next_to(simplified_y, RIGHT * 3)
        
        simplified_y_rec = self.create_surrounding_rectangle(simplified_y)
        simplified_y_group = VGroup(simplified_y, simplified_y_rec, general_y)
        
        
        step_2 = self.create_labeled_step(
            "Step 2: Write $y$ in simplified form",
            simplified_y_group
        )
        step_2_label = step_2[0]

        # Step 3: Calculate Asymptotes
        x_asymptote = MathTex("x = 3", color=DIVISOR_COLOR).scale(TEX_SCALE)
        y_asymptote = MathTex("y = 4", color=K_COLOR).scale(TEX_SCALE)
        asymptotes = VGroup(x_asymptote, y_asymptote).arrange(buff=1).next_to(simplified_y_group, DOWN * 2)

        step_3 = self.create_labeled_step(
            "Step 3: Calculate asymptotes",
            asymptotes
        )
        step_3_label = step_3[0]

        # Step 4: Calculate Points on Graph
        point_1_step_1 = MathTex(r"y = \frac{2}{2 - 3} + 4")
        point_1_step_2 = MathTex(r"= \frac{2}{-1} + 4")
        point_1_step_3 = MathTex("= -2 + 4")
        point_1_final_result = MathTex("y = 2", color=POINT_COLOR)
        point_1_final_result_rec = self.create_surrounding_rectangle(point_1_final_result)
        
        point_1_steps = VGroup(
            point_1_step_1,
            point_1_step_2,
            point_1_step_3,
            VGroup(point_1_final_result, point_1_final_result_rec)
        ).scale(TEX_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF)
        point_1_step_2.shift(RIGHT * 0.3)
        point_1_step_3.shift(RIGHT * 0.3)

        self.apply_smart_colorize(
            point_1_steps,
            {
                "2": A_COLOR,
                "4": K_COLOR,
                "2 - 3": DIVISOR_COLOR,
                "-2": WHITE
            }
         )
        
        point_2_step_1 = MathTex(r"y = \frac{2}{4 - 3} + 4")
        point_2_step_2 = MathTex(r"= \frac{2}{1} + 4")
        point_2_step_3 = MathTex("= 2 + 4")
        point_2_final_result = MathTex("y = 6", color=POINT_COLOR)
        point_2_final_result_rec = self.create_surrounding_rectangle(point_2_final_result)

        point_2_steps = VGroup(
            point_2_step_1,
            point_2_step_2,
            point_2_step_3,
            VGroup(point_2_final_result, point_2_final_result_rec)
        ).scale(TEX_SCALE).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF)
        point_2_step_2.shift(RIGHT * 0.3)
        point_2_step_3.shift(RIGHT * 0.3)

        self.apply_smart_colorize(
            point_2_steps,
            {
                "2": A_COLOR,
                "4": K_COLOR,
                "4 - 3": DIVISOR_COLOR,
                "= 2": WHITE
            }
        )
        
        points_group = VGroup(point_1_steps, point_2_steps).arrange(buff=WIDE_EQ_HBUFF)
        
        step_4 = self.create_labeled_step(
            "Step 4: Calculate some points on the curve",
            points_group
        )
        step_4_label = step_4[0]
        
        equations_group = VGroup(
            example_func,
            step_1, 
            step_2,
            step_3,
            step_4,
        ).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF).to_corner(UL)

        ordered_steps = VGroup(
            example_func,
            step_1_label,
            *division_steps,
            
            step_2_label,
            simplified_y_term_1,
            simplified_y_term_2[1],
            simplified_y_term_2[0],
            simplified_y_term_2[2:],
            simplified_y_term_3,
            simplified_y_rec,
            general_y,
            
            step_3_label,
            x_asymptote,
            y_asymptote,

            step_4_label,
            point_1_step_1,
            point_1_step_2,
            point_1_step_3,
            point_1_final_result,
            point_1_final_result_rec,
            point_2_step_1,
            point_2_step_2,
            point_2_step_3,
            point_2_final_result,
            point_2_final_result_rec
        )

        scroll = ScrollManager(ordered_steps)
        steps_to_scroll = len(division_steps) + 2
        # ---------------- Tips ----------------
        tip_1 = QuickTip("This is simply long division as in other chapters.")
        tip_2 = QuickTip("Note that $a$ is the remainder and $k$ is the quotient")
        tip_3 = QuickTip("$x = 3$ is an asymptote since $y$ will be undefined at that point.")
        tip_4 = QuickTip("$x$ will not yield a value if $y = 4$")

        Group(tip_1, tip_2, tip_3, tip_4).to_corner(DR)
        
        # ---------------- Animations ----------------
        def indicate(mobject, color=INDICATION_COLOR, run_time=INDICATION_TIME):
            return Indicate(mobject, color=color, run_time=INDICATION_TIME)
        
        # with self.voiceover(
        #         text="""
        #         In this video, we'll explore how to graph rational functions using polynomials and long division.
        #         """
        # ) as tracker:
        #     self.play(FadeIn(axes, general_form_group))
        #     scroll.prepare_next(self)
        #     self.wait(QUICK_PAUSE)

        # with self.voiceover("Let's examine this rational function.") as tracker:
        #     self.play(indicate(example_func))
        #     self.wait(QUICK_PAUSE)
            
        # with self.voiceover(
        #         text="""
        #         To graph it effectively, we first need to transform it into this <bookmark mark='format' /> format:
        #         y equals "a" over x minus h plus k.

        #         This format represents a hyperbola, and once we have it, we can easily identify the asymptotes,
        #         details, and key characteristics that will help us create an accurate graph.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("format")
        #     self.play(indicate(general_form_group))
        #     self.wait(QUICK_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Our first step is to divide <bookmark mark='den' /> the numerator into <bookmark mark='num' /> the denominator, which is the polynomial you see here.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("den")
        #     self.play(indicate(example_func_den))

        #     self.wait_until_bookmark("num")
        #     self.play(indicate(example_func_num))
        #     self.wait(STANDARD_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Next, we'll rearrange our our result into <bookmark mark='format' /> this format.
        #         Finally, we'll use this information to graph our rational function.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("format")
        #     self.play(indicate(general_form_group))
        #     self.wait(QUICK_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now, we will do the division.
        #         We start by recognizing that our divisor <bookmark mark='divisor' /> is x minus 3,
        #         and we're dividing it into our <bookmark mark='poly' /> polynomial, 4x minus 10.
        #         """
        # ) as tracker:
        #     scroll.prepare_next(self, steps=2)
            
        #     self.wait_until_bookmark("divisor")
        #     scroll.fade_in_from_target(self, example_func_num, run_time=2)

        #     self.wait_until_bookmark("poly")
        #     scroll.fade_in_from_target(self, example_func_den, run_time=2)

        #     self.play(FadeIn(tip_1, shift=UP))
        #     self.wait(COMPREHENSION_PAUSE)
        # self.play(FadeOut(tip_1, shift=DOWN))

        # with self.voiceover(
        #         text="""
        #         The division process is as follows; we divide, multiply, then subtract, then divide, multiply, subtract
        #         and so forth until we reach the end, which is a remainder or might be zero.
        #         """
        # ) as tracker:
        #     pass

        # with self.voiceover(
        #         text="""
        #         First, we divide: x divides into 4x to <bookmark mark='quotient' /> give us four.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("quotient")
        #     scroll.prepare_next(self)
        #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now let's multiply: <bookmark mark='multiply' /> four multiplied by x <bookmark mark='result' /> equals 4x
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("multiply")
        #     self.play(indicate(quotient), indicate(divisor[0]))

        #     self.wait_until_bookmark("result")
        #     scroll.prepare_next(self)
        #     self.wait(COMPREHENSION_PAUSE)
                
        # with self.voiceover(
        #         text="""
        #         And four multiplied by negative three
        #         <bookmark mark='result' /> equals negative twelve.
        #         """
        # ) as tracker:
        #     self.play(indicate(quotient), indicate(divisor[1:]))

        #     self.wait_until_bookmark("result")
        #     scroll.prepare_next(self)
        #     self.wait(COMPREHENSION_PAUSE)
            
        # with self.voiceover(
        #         text="""
        #         Now <bookmark mark='subtract' /> let's subtract.
        #         <bookmark mark='result_1' /> 4x minus 4x equals zero,
        #         <bookmark mark='result_2' /> -10 minus -12 equals 2.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("subtract")
        #     scroll.prepare_next(self, steps=2)

        #     self.wait_until_bookmark("result_1")
        #     self.play(indicate(dividend[:2]), indicate(division_step_1_4x))
        #     scroll.prepare_next(self)
            
        #     self.wait_until_bookmark("result_1")
        #     self.play(indicate(dividend[2:]), indicate(division_step_1_12))
        #     scroll.prepare_next(self)

        #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         As we can see, we can't <bookmark mark='divide' /> divide 2 by x
        #         because the divisor's power is higher than the power of the remainder, so we can't continue.
        #         Therefore, our remainder <bookmark mark='remainder' /> is two.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("divide")
        #     self.play(indicate(two), indicate(divisor[0]))

        #     self.wait_until_bookmark("remainder")
        #     scroll.prepare_next(self, steps=2)
        #     scroll.prepare_next(self)

        #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now we will take our answer from <bookmark mark='long_div' /> the long division
        #         and put it into the <bookmark mark='format' /> standard format.

        #         a is the remainder, which <bookmark mark='remainder' /> equals two.
        #         x minus h is the divisor, which <bookmark mark='divisor' /> is x minus three.
        #         k is the quotient, which <bookmark mark='quotient' /> equals 4.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("long_div")
        #     self.play(indicate(division_steps))

        #     self.wait_until_bookmark("format")
        #     self.play(indicate(general_form_group))

        #     scroll.prepare_next(self, steps=3)
        #     self.play(FadeIn(tip_2, shift=UP))

        #     self.wait_until_bookmark("remainder")
        #     scroll.fade_in_from_target(self, two, run_time=2)
            
        #     self.wait_until_bookmark("divisor")
        #     scroll.fade_in_from_target(self, divisor, run_time=2)

        #     self.wait_until_bookmark("quotient")
        #     self.play(FadeOut(tip_2, shift=DOWN))
        #     scroll.fade_in_from_target(self, quotient, run_time=2)
        #     scroll.prepare_next(self)
        #     self.wait(COMPREHENSION_PAUSE)

            
        # # with self.voiceover(
        # #         text="""
        # #         a is the remainder, which <bookmark mark='remainder' /> equals two.
        # #         x minus h is the divisor, which <bookmark mark='divisor' /> is x minus three.
        # #         k is the quotient, which <bookmark mark='quotient' /> equals 4.
        # #         """
        # # ) as tracker:
        # #     self.wait_until_bookmark("remainder")
        # #     scroll.fade_in_from_target(self, two, run_time=2)
            
        # #     self.wait_until_bookmark("divisor")
        # #     scroll.fade_in_from_target(self, divisor, run_time=2)

        # #     self.wait_until_bookmark("quotient")
        # #     scroll.fade_in_from_target(self, quotient, run_time=2)
        # #     scroll.prepare_next(self)
        # #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         So this is how we're going to graph our hyperbola.
        #         For reference, the basic hyperbola has the <bookmark mark='basic_form' /> form y equals 1 over x,
        #         and our function is similar with a constant over x minus three.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("basic_form")
        #     scroll.prepare_next(self)
        #     self.wait(QUICK_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now let's identify our asymptotes.
        #         We <bookmark mark='h_asy' /> have y equals k as our horizontal asymptote, parallel to the x axis.
        #         And we <bookmark mark='v_asy' /> have x equals h as our vertical asymptote, parallel to the y axis.
        #         """
        # ) as tracker:
        #     scroll.scroll_down(self, steps=steps_to_scroll)
        #     scroll.prepare_next(self)

        #     self.wait_until_bookmark("h_asy")
        #     # self.play(indicate(general_form[1]))
        #     y_callout.show()
            
        #     self.wait_until_bookmark("v_asy")
        #     #self.play(indicate(general_form[2]))
        #     y_callout.hide()
        #     x_callout.show()
            
        #     self.wait(STANDARD_PAUSE)
        #     x_callout.hide()
        # with self.voiceover(
        #         text="""
        #         For our function, the first asymptote is <bookmark mark='first_asy' /> at x equals 3.
        #         We can't have x equals 3 in our function because that would make the denominator zero, and 2 divided by 0 is undefined.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("first_asy")
        #     scroll.prepare_next(self)

        #     self.play(FadeIn(tip_3, shift=UP))
        #     self.wait(COMPREHENSION_PAUSE)
        # self.play(FadeOut(tip_3, shift=DOWN))

        # with self.voiceover(
        #         text="""
        #         Now, let's draw a <bookmark mark='line' /> vertical dotted line at x equals 3 representing the vertical asymptote.
        #         Remember, a hyperbola approaches its asymptotes but never touches them.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("line")
        #     self.play(Write(v_asymptote), run_time=2)
        #     self.wait(STANDARD_PAUSE)

        # with self.voiceover(
        #         text="""
        #         The second asymptote is <bookmark mark='v_asy' /> at y equals 4 which comes <bookmark mark='plus_4' /> from the plus 4 in our equation.
        #         Now, let's draw a <bookmark mark='line' /> horizontal dotted line at y equals 4.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("v_asy")
        #     scroll.prepare_next(self)
        #     self.play(FadeIn(tip_4, shift=UP))
            
        #     self.wait_until_bookmark("plus_4")
        #     self.play(indicate(simplified_y_term_3))

        #     self.wait_until_bookmark("line")
        #     self.play(FadeOut(tip_4, shift=DOWN))
        #     self.play(Write(h_asymptote), run_time=2)
            
        #     self.wait(STANDARD_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Before we proceed to graphing, let's <bookmark mark='overlay' /> understand the significance of the sign of 'a' in our standard form.

        #         When 'a' is positive, the hyperbola branches will appear in the first and third quadrants relative to the asymptotes. This means one branch appears above and to the right of the intersection of the asymptotes, while the other branch appears below and to the left.

        #         If 'a' is negative, the hyperbola branches will instead appear in the second and fourth quadrants as shown.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("overlay")
        #     self.play(FadeIn(blank_screen))
        # self.play(FadeOut(blank_screen))

        # with self.voiceover(
        #         text="""
        #         In our function, 'a' is positive which means the curves are going to be <bookmark mark='quadrant' /> in the first and third quadrant.
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("quadrant")
        #     self.play(FadeIn(first_quadrant, third_quadrant))
        #     self.wait(STANDARD_PAUSE)

        # with self.voiceover(
        #         text="""
        #         To enhance our graph, let's plot a couple of points to confirm where the curve should be.
        #         Let's <bookmark mark='step_1' /> try x equals 2.
        #         Two minus three <bookmark mark='step_2' /> equals negative 1.
        #         Two over negative one <bookmark mark='step_3' /> equals -2.
        #         Finally, negative two plus four <bookmark mark='step_4' /> equals 2.
        #         So at <bookmark mark='point' /> x equals 2, y is 2.
        #         """
        # ) as tracker:
        #     scroll.prepare_next(self) # Label
            
        #     for step in ["step_1", "step_2", "step_3", "step_4"]:
        #         self.wait_until_bookmark(step)
        #         scroll.prepare_next(self)
        #     scroll.prepare_next(self) # Surrounding Rectangle

        #     self.wait_until_bookmark("point")
        #     self.play(FadeIn(point1))
            
        #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now let's try a point on the other side of the vertical asymptote.
        #         Let's <bookmark mark='step_1' /> x equals 4.
        #         four minus three <bookmark mark='step_2' /> equals 1.
        #         Two over one <bookmark mark='step_3' /> equals 2.
        #         Finally, two plus four <bookmark mark='step_4' /> equals 6.
        #         So at <bookmark mark='point' /> x equals 4, y is 6.
        #         """
        # ) as tracker:
        #     for step in ["step_1", "step_2", "step_3", "step_4"]:
        #         self.wait_until_bookmark(step)
        #         scroll.prepare_next(self)
        #     scroll.prepare_next(self) # Surrounding Rectangle

        #     self.wait_until_bookmark("point")
        #     self.play(FadeIn(point2))
            
        #     self.wait(COMPREHENSION_PAUSE)

        # with self.voiceover(
        #         text="""
        #         Now we can draw the curves of our hyperbola.
        #         They will approach closer and closer to the asymptotes but will never touch them.

        #         Let's draw <bookmark mark='top' /> the top curve connecting to 4 and 6.

        #         Then let's draw <bookmark mark='bottom' /> the bottom curve connecting to 2 and 2
        #         and also approaching but never touching the asymptotes.

        #         You could calculate and plot more points if you wish, to make your graph more accurate, but basically, this is our hyperbola.

        #         So The graph you see here is y equals 2 over x minus 3, plus 4
        #         """
        # ) as tracker:
        #     self.wait_until_bookmark("top")
        #     self.play(Create(right_graph), run_time=3, rate_func=linear)

        #     self.wait_until_bookmark("bottom")
        #     self.play(Create(left_graph), run_time=3, rate_func=linear)

        #     self.wait(COMPREHENSION_PAUSE)
        # self.wait(5)