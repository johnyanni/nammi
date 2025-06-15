from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

class ProblematicExample(MathTutorialScene):
    def construct(self):
        
        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        
        step5 = MathTex(r"x^2 - 5x - 3 = 0").scale(MATH_SCALE).to_edge(LEFT, buff=0.4).to_edge(UP, buff=0.5)
        
        self.play(Write(step5))
        
        self.wait(1)
        
        
        # =================================================================================
        # SOLUTION STEPS [SCROLL]
        # =================================================================================




        scroll = ScrollManager(scene=self, global_arrangement=False)
        scroll.set_position_target(step5, DOWN, buff=0.3, aligned_edge=LEFT)

        step1 = scroll.construct_step(
            scroll.create_tex(r"First, expand $(x-1)^2$:", label="l_expand_squared"),
            scroll.create_math_tex(r"(x-1)^2 = (x-1)(x-1) = x^2 - 2x + 1", label="m_expand_detail"),
            scroll.create_math_tex(r"2(x^2 - 2x + 1) + 3x = x^2 + 4x + 5", label="m_expand_result"),
            scroll.create_math_tex(r"2(x^2 - 2x + 1) + 3x = x^2 + 4x + 5", label="m_expand_result2"),
            scroll.create_math_tex(r"2(x^2 - 2x + 1) + 3x = x^2 + 4x + 5", label="m_expand_result3")
        )

       
        # Animate
        scroll.prepare_next("l_expand_squared")
        scroll.prepare_next("m_expand_detail")
        scroll.prepare_next("m_expand_result")
        scroll.prepare_next("m_expand_result2")
        scroll.prepare_next("m_expand_result3")


        step2 = scroll.construct_step(
            scroll.create_tex("Distribute the 2:", label="l_distribute_2"),
            scroll.create_math_tex(r"2x^2 - 4x + 2 + 3x = x^2 + 4x + 5", label="m_distribute_result"),
            arrange=False
        ).next_to(step1, DOWN, buff=1).set_x(0)

        # step2.next_to(step1, RIGHT, buff=2)
        

        scroll.prepare_next("l_distribute_2")
        scroll.prepare_next("m_distribute_result")
        
        scroll.scroll_down("l_distribute_2")
        
        self.wait(1)
        
        
        
        s6_identify_coefficients_step = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:"),
            scroll.create_math_tex(r"x^2 - 5x - 3 = 0"),
            scroll.create_math_tex(r"a = 1 \quad b = -5 \quad c = -3", scale=1.0),
            add_to_scroll=False
        )
        
        coefficient_values_in_equation = self.parse_elements(s6_identify_coefficients_step[1],
            ('a_value', 'x', 0, A_COLOR),  
            ('b_value', '-5', 0, B_COLOR),
            ('c_value', '-3', 0, C_COLOR)
        )
        
        coefficient_labels = self.parse_elements(s6_identify_coefficients_step[2],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
                
        coefficient_values = self.parse_elements(s6_identify_coefficients_step[2],
            ('a_value', '1', 0, A_COLOR),
            ('b_value', '-5', 0, B_COLOR),
            ('c_value', '-3', 0, C_COLOR)
        )
        
        scroll.create_steps(s6_identify_coefficients_step[:-1], ["l_identify_coefficients", "m_standard_form_equation"], arrange=False)
        scroll.create_steps(coefficient_labels.values(), ["coefficient_a_label", "coefficient_b_label", "coefficient_c_label"], arrange=False)
        scroll.create_steps(coefficient_values.values(), ["coefficient_a_value", "coefficient_b_value", "coefficient_c_value"], arrange=False)
        
        # s6_identify_coefficients_step.next_to(step2, RIGHT, buff=2)
        
        # s6_identify_coefficients_step.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        # # Use the scroll manager's tracking - this is what add_to_arrangement does!
        # s6_identify_coefficients_step.next_to(
        #     scroll.get_current_visible_eqn(),  # This returns the last equation added
        #     RIGHT, 
        #     buff=0.5,
        #     aligned_edge=LEFT
        # )
        
        # ===========================================================
        
        self.add(SurroundingRectangle(step2, color=RED))
        self.add(SurroundingRectangle(s6_identify_coefficients_step, color=BLUE))
        
        scroll.prepare_next("l_identify_coefficients")
        scroll.prepare_next("m_standard_form_equation")
        
        scroll.prepare_next("coefficient_a_label")
        scroll.prepare_next("coefficient_b_label")
        scroll.prepare_next("coefficient_c_label")
        

        scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])

        scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])

        scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_standard_form_equation")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>