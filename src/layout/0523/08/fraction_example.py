from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class Fraction(MathTutorialScene):
    def construct(self):

        equation = MathTex(r"\frac{2}{3} - \frac{3}{10} =")
        sol1 = MathTex(r"\frac{20 - 9}{30} =")
        sol2 = MathTex(r"\frac{11}{3}")

        sol1.set_color(RED)

        Group(sol1[0][0:2], sol1[0][3], sol1[0][5:7]).set_opacity(0)
        Group(sol1[0][2], sol1[0][-1]).set_color(WHITE)

        VGroup(equation, sol1).arrange(DOWN, aligned_edge=RIGHT, buff=0.8)
        sol2.next_to(sol1, RIGHT)
        little_10 = (
            MathTex("10", color=RED).scale(0.6).next_to(equation[0][0], LEFT, buff=0.2)
        )
        little_3 = (
            MathTex("3", color=RED).scale(0.6).next_to(equation[0][4], LEFT, buff=0.2)
        )

        copy = VGroup(equation[0][2], equation[0][6:8])

        self.play(Write(equation))
        self.play(Write(little_10))
        self.play(Write(little_3))
        self.play(Write(VGroup(sol1[0][2], sol1[0][4], sol1[0][-1])))
        self.play(
            AnimationGroup(
                FadeOut(little_10, target_position=equation[0][0]),
                FadeIn(sol1[0][0:2].set_opacity(1), target_position=equation[0][0]),
            )
        )
        self.play(
            AnimationGroup(
                FadeOut(little_3, target_position=equation[0][4]),
                FadeIn(sol1[0][3].set_opacity(1), target_position=equation[0][4]),
            )
        )
        self.play(TransformFromCopy(copy, sol1[0][5:7]))
        self.play(Write(sol2))
        self.play(Write(SurroundingRectangle(sol2, color=RED)))
        self.wait()
