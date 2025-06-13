from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic
from src.components.common.custom_axes_2 import CustomAxes
from src.components.common.quick_tip import QuickTip

config.verbosity = "ERROR"

class TrigGraph(MathTutorialScene):

    def construct(self):
        

        
        # Constants
        TEX_SCALE = 0.65
        EQ_VBUFF = 0.35
        STANDARD_EQ_HBUFF = 0.2
        WIDE_EQ_HBUFF = 0.75
        
        LABEL_SCALE = 0.5
        LABEL_COLOR = GREY
        LABEL_BUFF = 0.2

        GRAPH_COLOR = PURPLE
        A_COLOR = BLUE
        B_COLOR = TEAL
        P_COLOR = PINK
        X_COLOR = GOLD
        Y_COLOR = PURPLE
        
        # Constants for timing
        QUICK_PAUSE = 0.5
        STANDARD_PAUSE = 1.0
        COMPREHENSION_PAUSE = 2.0

        INDICATION_TIME = 2.0
        
        
        def create_labeled_step(
                label_text,
                expressions,
                color_map=None,
                label_color=LABEL_COLOR,
                label_scale=LABEL_SCALE,
                label_buff=LABEL_BUFF,
                eq_hbuff=STANDARD_EQ_HBUFF,
                tex_scale=TEX_SCALE
        ):
            label = Tex(label_text, color=label_color).scale(label_scale)
            exp_group = VGroup(*[MathTex(exp).scale(tex_scale) for exp in expressions])
            exp_group.arrange(RIGHT, buff=eq_hbuff)
            
            if color_map:
                self.apply_smart_colorize(exp_group, color_map)
            
            return VGroup(label, exp_group).arrange(DOWN, aligned_edge=LEFT, buff=label_buff)


        # Axes Configuration
        axes = CustomAxes(
            x_range=[-2*PI, 5*PI, PI],
            y_range=[-4, 4, 1],
            x_length=8,
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": np.arange(-3, 4)
            }
        ).to_edge(RIGHT)

        x_pos = [x for x in np.arange(PI, 5*PI, PI)]
        x_vals = [
            MathTex(r"\pi"),
            MathTex(r"2\pi"),
            MathTex(r"3\pi"),
            MathTex(r"4\pi"),
            MathTex(r"5\pi"),
        ]
       
        x_dict = dict(zip(x_pos, x_vals))
        axes.add_coordinates(x_dict)

        axes_labels = axes.coordinate_labels
        axes_labels.set_opacity(0)
        label_pi, label_2pi, label_3pi, label_4pi  = axes_labels[0]
                
        graph = axes.plot(lambda x: 3 * np.sin(x / 2), x_range=[0, 4*PI], color=GRAPH_COLOR)
        graph_points = VGroup(
            *[
                Dot(axes.c2p(point[0], point[1]), color=RED) for point in [
                    (0, 0), 
                    (PI, 3),
                    (2*PI, 0),
                    (3*PI, -3),
                    (4*PI, 0)
                ]
            ]
        ).set_z_index(1)

        small_axes = Axes(
            x_range=[-4*PI, 4*PI, PI],
            tips=False,
            axis_config={"include_ticks": False}
        ).set_color(BLUE)
        graph_pattern = small_axes.plot(lambda x: -np.cos(x) + 1, color=RED)

        pattern = VGroup(small_axes, graph_pattern).scale(0.25)
        pattern.next_to(axes.get_x_axis(), UP).shift(RIGHT * 2 + UP)

        period_line = Line(
            start=axes.c2p(0, -3.2),
            end=axes.c2p(4*PI, -3.2),
            color=GREEN
        )

        v_lines = VGroup(
            *[
                axes.get_line_from_axis_to_point(0, axes.c2p(point[0], point[1]))
                for point in [(0, -3.2), (4*PI, -3.2)]
            ]
        ).set_z_index(1).set_color(GREEN)

        # Text Explanations
        amplitude_def = Tex(
            "Amplitude: The vertical distance from the middle\\\\to the maximum of the curve.", 
            tex_environment="flushleft",
            color=A_COLOR
        ).scale(TEX_SCALE - 0.05)
        
        period_def = Tex(
            "Period: The horizontal distance needed\\\\for one complete cycle of the curve.", 
            tex_environment="flushleft",
            color=P_COLOR
        ).scale(TEX_SCALE - 0.05)

        def_group = Group(amplitude_def, period_def).arrange(DOWN, aligned_edge=LEFT, buff=0.65).to_edge(LEFT)
        
        # Equations
        x_range = MathTex(r"0 \le x \le 4\pi").scale(TEX_SCALE)
        x_range.next_to(axes.get_y_axis().get_bottom(), LEFT * 2)
        
        general_eqn = MathTex(r"y = a\sin{(bx)}").scale(TEX_SCALE)
        a_in_eqn = general_eqn[0][search_shape_in_text(general_eqn, MathTex("a"))[0]]
        b_in_eqn = general_eqn[0][search_shape_in_text(general_eqn, MathTex("b"))[0]]
        
        p_formula = MathTex(r"P = \frac{2\pi}{b}").scale(TEX_SCALE)

        eqn_group = VGroup(general_eqn, p_formula).arrange(buff=WIDE_EQ_HBUFF)
        eqn_group.next_to(axes.get_y_axis().get_top(), LEFT * 2)
        
        y = MathTex(r"y = 3\sin{\Big(\frac{x}{2}\Big)}").scale(TEX_SCALE)
        SmartColorizeStatic(y, {"2": B_COLOR})

        a_in_y = y[0][search_shape_in_text(y, MathTex("3"))[0]]
        b_in_y = y[0][search_shape_in_text(y, MathTex("2"))[0]]
                        
        step_1 = create_labeled_step(
            "Extract $b$ from equation",
            [
                r"b = \frac{1}{2}"
            ],
            {r"b = \frac{1}{2}": B_COLOR}
        )
        step_1_label, b = step_1[0], step_1[1]
        
        step_2 = create_labeled_step(
            "Extract $a$ from equation",
            [
                "a = 3"
            ],
            {"a = 3": A_COLOR}
        )
        step_2_label, a = step_2[0], step_2[1]

        step_3 = create_labeled_step(
            "Substitute $b$ into period formula",
            [
                r"P = \frac{2\pi}{\frac{1}{2}}"
            ],
        )
        step_3_label, p_with_value = step_3[0], step_3[1][0]

        step_4 = create_labeled_step(
            "Simplify",
            [
                r"P = 4\pi"
            ]
        )
        step_4_label, p_final_result = step_4[0], step_4[1][0]

        self.apply_smart_colorize(
            [p_formula, p_with_value, p_final_result],
            {
                "P": P_COLOR,
                "b": B_COLOR,
                r"\frac{1}{2}": B_COLOR
            }
        )

        self.apply_smart_colorize(
            [general_eqn, y, x_range],
            {
                "a": A_COLOR,
                "3": A_COLOR,
                "b": B_COLOR,
                "2": B_COLOR,
                "x": X_COLOR,
                r"\sin": Y_COLOR,
                r"\Big(": Y_COLOR,
                r"\Big)": Y_COLOR,
                "(": Y_COLOR,
                ")": Y_COLOR,
                "y =": Y_COLOR,
            }
        )

        left_group = VGroup(
            y,
            step_1,
            step_2,
            step_3,
            step_4
        ).arrange(DOWN, aligned_edge=LEFT, buff=EQ_VBUFF).to_edge(LEFT)
        
        # Tips
        tip_1 = QuickTip(
            "$b$ is the coefficient or number in front of $x$"
        )

        tip_2 = QuickTip(
            "$a$ represents amplitude and can be found at the front of the trigonometric function"
        )

        tip_3 = QuickTip(
            "$P$ represents period - the horizontal length of the smallest repeating unit"
        )

        Group(tip_1, tip_2, tip_3).to_corner(DR)
        
        # ---------------- Animations ----------------
        with self.voiceover(
                text="""
                In this video, we're going to learn how to graph the trigonometric function
                <bookmark mark='indicate' /> y equals 3 sine x over 2 without using a calculator.
                
                We'll only need to understand two key elements that will make graphing the function straightforward.
                """
        ) as tracker:
            self.play(
                FadeIn(axes, p_formula, x_range, general_eqn, y)
            )

            self.wait_until_bookmark("indicate")
            self.play(Indicate(y, run_time=INDICATION_TIME))

        with self.voiceover(
                text="""
                The first element is the amplitude. <bookmark mark='explain' /> The amplitude represents the distance from the
                middle value to the maximum value of the curve. It determines how "tall" the graph will be.
                """
        ) as tracker:
            self.wait_until_bookmark("explain")
            self.play(Write(amplitude_def), run_time=3)
            self.wait(QUICK_PAUSE)

        with self.voiceover(
                text="""
                The second element is <bookmark mark='explain' /> the period of the function. As we know, trignometric functions are periodic.

                For sine functions, the formula for calculating the period is <bookmark mark='indicate_1' /> two pi over b,
                where <bookmark mark='indicate_2' /> b is the coefficient in front of x in the function.
                """
        ) as tracker:
            self.wait_until_bookmark("explain")
            self.play(Write(period_def), run_time=3)

            self.wait_until_bookmark("indicate_1")
            self.play(Indicate(p_formula))

            self.wait_until_bookmark("indicate_2")
            self.play(Indicate(b_in_eqn, run_time=INDICATION_TIME))
            
            self.wait(QUICK_PAUSE)
        self.play(FadeOut(def_group))
            
        with self.voiceover(
                text="""
                In our function, we can see that the number in front of x is <bookmark mark='indicate' /> a half,
                so b equals <bookmark mark='b' /> 1 over 2.
                """
        ) as tracker:
            self.wait_until_bookmark("indicate")
            self.play(Indicate(b_in_y, run_time=INDICATION_TIME))
            
            self.wait_until_bookmark("b")
            self.play(
                Write(step_1),
                FadeIn(tip_1, shift=UP)
            )
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_1, shift=DOWN))

        with self.voiceover(
                text="""
                As we said, the amplitude is the distance from the middle value to the maximum value of the curve.
                The amplitude is usually a positive value, even though you'll see that there are negative number below the x axis.
                """
        ) as tracker:
            pass

        with self.voiceover(
                text="""
                The amplitude here is the number <bookmark mark='indicate' /> in front of the trig function of sine.
                Thus, in our function "a" <bookmark mark='a' /> equals three.
                """
        ) as tracker:
            self.wait_until_bookmark("indicate")
            self.play(Indicate(a_in_eqn, run_time=INDICATION_TIME))
            
            self.wait_until_bookmark("a")
            self.play(
                Write(step_2),
                FadeIn(tip_2, shift=UP),
                Indicate(a_in_y, run_time=INDICATION_TIME)
            )
            self.wait(COMPREHENSION_PAUSE)
        self.play(FadeOut(tip_2, shift=DOWN))

        with self.voiceover(
                text="""
                Let's now work out the period. Since <bookmark mark='indicate_1' /> b equals 1 over 2, the period will equal
                <bookmark mark='p' /> two pi over half.
                Two divided by half is four, so <bookmark mark='p_final' /> p equals 4 pi.

                We can see that 4 pi is in the range of x, which is from <bookmark mark='indicate_2' /> 0 to 4 pi.
                """
        ) as tracker:
            self.wait_until_bookmark("indicate_1")
            self.play(Indicate(b, run_time=INDICATION_TIME))
            
            self.wait_until_bookmark("p")
            self.play(
                Write(step_3),
                FadeIn(tip_3, shift=UP)
            )

            self.wait_until_bookmark("p_final")
            self.play(FadeOut(tip_3, shift=DOWN))
            self.play(Write(step_4))

            self.wait_until_bookmark("indicate_2")
            self.play(Indicate(x_range, run_time=INDICATION_TIME))
            
            self.wait(STANDARD_PAUSE)
        

        with self.voiceover(
                text="""
                To make the drawing easier, we know that the sine looks <bookmark mark='pattern' /> like a repeated pattern.
                """
        ) as tracker:
            self.wait_until_bookmark("pattern")
            self.play(
                Write(pattern),
                run_time=2
            )
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                So as we know the period is 4 pi, let's break it down into four quarters.
                This way, we can clearly see where the curve cuts the x axis, where it peaks,
                and where it reaches the minimum value.
                """
        ) as tracker:
            pass

        with self.voiceover(
                text="""
                Let's now break the period down into four parts.
                """
        ) as tracker:
            for label in [label_4pi, label_pi, label_2pi, label_3pi]:
                self.play(
                    label.animate.set_opacity(1),
                    FocusOn(label)
                )
                
        with self.voiceover(
                text="""
                As we know, the sine function starts at <bookmark mark='point_1' /> 0 and 0.
                It will go up until it reaches the maximum value of the function, or the amplitude which is <bookmark mark='point_2' /> 3.

                Then it will go down and cut at the middle, so if the period is 4 pi, it will cut at the middle, which is <bookmark mark='point_3' /> 2 pi.
                
                Then it will go down until it reaches the minimum value at 3 pi. The minimum value is negative the amplitude, so <bookmark mark='point_4' /> negative 3.
                
                Then it will go up to the same spot that it began with, at <bookmark mark='point_5' /> 4 pi, so it starts and finishes at the same spot.
                """
        ) as tracker:

            for i in range(5):
                self.wait_until_bookmark(f"point_{i + 1}")
                self.play(
                    FadeIn(graph_points[i]),
                    FocusOn(graph_points[i])
                )
            self.wait(STANDARD_PAUSE)
        self.play(Write(graph), rate_func=linear, run_time=3)
        
        with self.voiceover(
                text="""
                That is one period and then it continues to repeat itself.
                And that's it! We were able to graph a trignometric function only using two properties.
                """
        ) as tracker:
            self.play(Write(v_lines))
            self.play(Write(period_line))
    
        self.wait(5)
        
        # Add this after the last self.wait(5) line
        
        # Transformation Section
        with self.voiceover(
                text="""
                Now let's see what happens when we change the value of b from <bookmark mark='highlight_old_b' /> one half 
                to <bookmark mark='highlight_new_b' /> one. This will transform our function from y equals 3 sine x over 2 
                to <bookmark mark='show_new_eq' /> y equals 3 sine x.
                """
        ) as tracker:
            # Create new equation
            y_transformed = MathTex(r"y = 3\sin{(x)}").scale(TEX_SCALE)
            SmartColorizeStatic(y_transformed, {"3": A_COLOR, "x": X_COLOR, r"\sin": Y_COLOR, "(": Y_COLOR, ")": Y_COLOR, "y =": Y_COLOR})
            y_transformed.move_to(y)
            
            self.wait_until_bookmark("highlight_old_b")
            self.play(Indicate(b_in_y, color=YELLOW, run_time=INDICATION_TIME))
            
            self.wait_until_bookmark("highlight_new_b")
            # Create new b value
            b_new = MathTex(r"b = 1").scale(TEX_SCALE)
            SmartColorizeStatic(b_new, {"b = 1": B_COLOR})
            b_new.move_to(b)
            
            self.wait_until_bookmark("show_new_eq")
            self.play(
                Transform(y, y_transformed),
                Transform(b, b_new)
            )
            self.wait(STANDARD_PAUSE)

        with self.voiceover(
                text="""
                With b equals 1, let's calculate the new period. <bookmark mark='show_calc' /> P equals 2 pi over 1, 
                which simplifies to <bookmark mark='show_result' /> P equals 2 pi.
                
                Notice that the period is now <bookmark mark='compare' /> half of what it was before. 
                Let's watch how this affects our graph.
                """
        ) as tracker:
            # Update period calculation
            p_with_value_new = MathTex(r"P = \frac{2\pi}{1}").scale(TEX_SCALE)
            p_final_result_new = MathTex(r"P = 2\pi").scale(TEX_SCALE)
            
            SmartColorizeStatic(p_with_value_new, {"P": P_COLOR, "1": B_COLOR})
            SmartColorizeStatic(p_final_result_new, {"P": P_COLOR})
            
            p_with_value_new.move_to(p_with_value)
            p_final_result_new.move_to(p_final_result)
            
            self.wait_until_bookmark("show_calc")
            self.play(Transform(p_with_value, p_with_value_new))
            
            self.wait_until_bookmark("show_result")
            self.play(Transform(p_final_result, p_final_result_new))
            
            self.wait_until_bookmark("compare")
            self.play(
                Indicate(p_final_result, run_time=INDICATION_TIME),
                Indicate(step_4, run_time=INDICATION_TIME)
            )

        with self.voiceover(
                text="""
                As we transform the graph, watch how the curve <bookmark mark='start_transform' /> compresses horizontally. 
                The amplitude stays the same at 3, but now one complete cycle happens in just <bookmark mark='highlight_period' /> 2 pi 
                instead of 4 pi.
                
                The key points now occur at <bookmark mark='show_points' /> 0, pi over 2, pi, 3 pi over 2, and 2 pi.
                """
        ) as tracker:
            # Create new graph
            graph_new = axes.plot(lambda x: 3 * np.sin(x), x_range=[0, 4*PI], color=GRAPH_COLOR)
            
            # New graph points for y = 3sin(x)
            graph_points_new = VGroup(
                *[
                    Dot(axes.c2p(point[0], point[1]), color=RED) for point in [
                        (0, 0), 
                        (PI/2, 3),
                        (PI, 0),
                        (3*PI/2, -3),
                        (2*PI, 0),
                        (5*PI/2, 3),
                        (3*PI, 0),
                        (7*PI/2, -3),
                        (4*PI, 0)
                    ]
                ]
            ).set_z_index(1)
            
            # New period line
            period_line_new = Line(
                start=axes.c2p(0, -3.2),
                end=axes.c2p(2*PI, -3.2),
                color=GREEN
            )
            
            v_lines_new = VGroup(
                *[
                    axes.get_line_from_axis_to_point(0, axes.c2p(point[0], point[1]))
                    for point in [(0, -3.2), (2*PI, -3.2)]
                ]
            ).set_z_index(1).set_color(GREEN)
            
            self.wait_until_bookmark("start_transform")
            
            # Animate the transformation
            self.play(
                Transform(graph, graph_new),
                Transform(graph_points, graph_points_new[:5]),  # Show first 5 points
                Transform(period_line, period_line_new),
                Transform(v_lines, v_lines_new),
                run_time=3
            )
            
            self.wait_until_bookmark("highlight_period")
            self.play(Indicate(period_line, run_time=INDICATION_TIME))
            
            self.wait_until_bookmark("show_points")
            # Add labels for new key points
            new_labels = VGroup(
                MathTex(r"\frac{\pi}{2}").scale(0.5).next_to(axes.c2p(PI/2, 0), DOWN),
                MathTex(r"\frac{3\pi}{2}").scale(0.5).next_to(axes.c2p(3*PI/2, 0), DOWN)
            )
            self.play(Write(new_labels))

        with self.voiceover(
                text="""
                Notice how the graph now completes <bookmark mark='indicate_cycles' /> two full cycles in the same space 
                where it previously completed just one cycle. This demonstrates how the b value directly controls 
                the period of the sine function.
                
                The smaller the period, the more compressed the graph becomes horizontally, and the more cycles 
                fit within a given interval.
                """
        ) as tracker:
            self.wait_until_bookmark("indicate_cycles")
            # Show the remaining points to emphasize two cycles
            self.play(FadeIn(graph_points_new[5:]))
            
            # Highlight both cycles
            cycle1_box = SurroundingRectangle(
                VGroup(graph_points_new[0], graph_points_new[4]), 
                color=YELLOW, 
                buff=0.3
            )
            cycle2_box = SurroundingRectangle(
                VGroup(graph_points_new[4], graph_points_new[8]), 
                color=YELLOW, 
                buff=0.3
            )
            
            self.play(Create(cycle1_box))
            self.wait(QUICK_PAUSE)
            self.play(Transform(cycle1_box, cycle2_box))
            self.wait(QUICK_PAUSE)
            self.play(FadeOut(cycle1_box))

        self.wait(5)