from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"


class StepFunc1(MathTutorialScene):
    def construct(self):
        
        
        example_func = MathTex(r"y = \frac{4x - 10}{x - 3}").scale(TEX_SCALE)
        # example_func_dem = example_func[0][search_shape_in_text(example_func, MathTex("4x - 10"))[0]].set_color(BLUE)
        # example_func_num = example_func[0][search_shape_in_text(example_func, MathTex("x - 3"))[0]].set_color(GREEN)
        
        example_func_num = self.find_element("x-3", example_func, color=GREEN, as_group=True)
        example_func_dem = self.find_element("4x-10", example_func, color=BLUE, as_group=True)
        


        new_ex = MathTex("x = 3").scale(MATH_SCALE)
        new_ex_start = self.find_element("x =", new_ex, color=BLUE, as_group=True)
        new_ex_value = self.find_element("3", new_ex, color=RED, as_group=True)
        
        
        
        answer = MathTex("x = 2").scale(MATH_SCALE)
        answer_rect = self.create_surrounding_rectangle(answer)
        answer_group = VGroup(answer, answer_rect)
        
        step = VGroup(
            Tex("Final Answer").scale(0.6),
            answer_group,
            example_func_num,
            new_ex
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)




        
        
        step1 = VGroup( 
            Tex("Final Answer").scale(0.6),
            new_ex_start,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        
        
        # Custom styling
        step2 = VGroup(
            Tex("Important Result").scale(0.6),
            self.create_rect_group(
                MathTex("y = mx + b").scale(MATH_SCALE),
                rect_color=YELLOW,
                corner_radius=0.2,
                buff=0.15,
                stroke_width=3
            ),
            MathTex("3 - 2x = 2x - 5").scale(1.2).set_color(RED),
            Tex("Add 2x to both sides").scale(0.6),
            self.create_annotated_equation(
                "3 - 2x = 2x - 5 - 2",
                "-3",
                "3",
                "2",
                nth_to=-1
            ),
            MathTex("2x = 2x - 8").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        steps = VGroup(step, step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        steps.to_edge(UP, buff=0.5)

        # With unpacking
        elements = VGroup(
            step[0],  # "Final Answer"
            step[1][0],
            step[1][1],# The entire rect group VGroup
            step[2],  # example_func_num
            step[3],
            
            step1[0], # "Final Answer"
            step1[1], # "x-3"
            
            step2[0], # "Important Result"
            step2[1], # The entire rect group VGroup
            step2[2], # "3 - 2x = 2x - 5"
            step2[3], # "Add 2x to both sides"
            step2[4], # annotated equation
            step2[5], # "2x = 2x - 8"
        )
        
        
        print(f"Total elements after unpacking: {len(elements)}")
        for i, elem in enumerate(elements):
            print(f"  Element {i}: {type(elem).__name__}")
            if hasattr(elem, 'tex_string'):
                print(f"    Content: {elem.tex_string}")
        
        
        scroll_mgr = ScrollManager(elements)
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  # Shows label
        scroll_mgr.prepare_next(self)  # Shows label
        
        scroll_mgr.prepare_next(self)  # Shows label
        # scroll_mgr.fade_in_from_target(self, example_func_num, run_time=2)
        scroll_mgr.prepare_next(self)  # Shows label


        


        
    



    
