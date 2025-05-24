from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        step1 = VGroup(
            Tex("Given").scale(0.6),
            MathTex(r"\text{adjacent} = 6").scale(TEX_SCALE),
            MathTex(r"\text{hypotenuse} = 10").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        adjacent_value = self.find_element("6", step1[1], color=BLUE)
        hypotenuse_value = self.find_element("10", step1[2], color=RED)
        

                
        step2 = VGroup(
            Tex("Cos Ratio").scale(0.6),
            MathTex(r"x = \frac{adj}{hyp}").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        
        adjacent = self.find_element("adj", step2[1], color=BLUE)
        hypotenuse = self.find_element("hyp", step2[1], color=RED)
        
        
        
        
        
        step3 = VGroup(
            Tex("Substitute").scale(0.6),
            MathTex(r"x = \frac{6}{10}").scale(TEX_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.apply_smart_colorize(
            [step1[1], step1[2], step2[1], step3[1]],
            {
                "adjacent": BLUE,
                "hypotenuse": RED,
                "x": GREEN,
                "6": BLUE,
                "10": RED
            }
        )


        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        steps.to_edge(UP, buff=0.5)

        six = MathTex("6").scale(TEX_SCALE).set_color(BLUE)
        six.move_to(adjacent)  # Position it where "adj" is

        # Transform adj to 6
        # self.add(steps)

        
    
        self.play(Write(step1[0]))
        self.play(Write(step1[1]))
        self.play(Write(step1[2]))
        
        self.play(Write(step2[0]))
        self.play(Write(step2[1]))

        
        self.play(ReplacementTransform(adjacent, six))
        
        self.play(Write(step3[0]))
        
        self.play(Write(step3[1]))


    
