from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager


config.verbosity = "ERROR"

class Example03a(MathTutorialScene):
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
       
       
       
        scroll = ScrollManager(scene=self)
       
        
        eq1 = MathTex(r"\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}").scale(MATH_SCALE)
        x_plus_5 = MathTex("x+5").scale(MATH_SCALE).set_color(LIGHT_GRAY)
        
        group = VGroup(eq1, x_plus_5).arrange(RIGHT, buff=1)

        # Then use them directly
        sol3_step5 = scroll.construct_step(
            scroll.create_tex("Simplify the square root:"),
            (group, None),
            scroll.create_math_tex(r"x = \frac{-10 \pm 4\sqrt{3}}{2}"),
            add_to_scroll=False
        )

        # scroll.create_steps([sol3_step5[0], *group, sol3_step5[2]], ["l_simplify_sqrt", "m_simplify_sqrt", "m_empty_formula", "m_simplify_sqrt_result"], arrange=False)
        
        scroll.create_step(sol3_step5[0], arrange=False)
        scroll.create_steps(group, arrange=False)
        scroll.create_step(sol3_step5[2], arrange=False)
        
        
        sol_steps = scroll.get_arranged_equations()
        
        
        
        scroll.prepare_next()
        scroll.prepare_next()
        self.wait(3)
        # scroll.fade_in_from_target(eq1, x_plus_5)
        scroll.transform_from_copy(eq1, x_plus_5, run_time=2)
        scroll.prepare_next()
        
        