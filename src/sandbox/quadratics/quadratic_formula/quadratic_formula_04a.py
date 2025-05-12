from manim import *
from src.components.common.base_scene import *
from src.components.common.quick_tip import QuickTip


class QuadraticFormula(MathTutorialScene):
    def construct(self):
        
        # Color Definitions
        A_COLOR = "#4ec9b0"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        X_COLOR = "#ffb86c"

        # Equation Background
        EQUATION_BG_FILL = "#3B1C62"
        EQUATION_BG_STROKE = "#9A48D0"

       

        ###############################################################################
        # SECTION 1: FORMULA/HELPERS 
        ###############################################################################

        # Create the generic quadratic equation
        quadratic_form = MathTex(r"ax^2 + bx + c = 0").scale(TEX_SCALE).to_corner(UL, buff=0.6)
        SmartColorizeStatic(quadratic_form, {"2": X_COLOR})
        
        # Find the coefficients in the general equation
        quad_form_a = quadratic_form[0][0]  # 'a' is typically first character
        quad_form_b = quadratic_form[0][4]  # 'b' is typically at position 4
        quad_form_c = quadratic_form[0][7]  # 'c' is typically at position 8
        
        # Create the quadratic formula
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(TEX_SCALE).to_corner(UR, buff=0.6)
        
        
        
        # Arrange the quadratic equation and formula
        quadratic_group = Group(
            quadratic_form,
            quadratic_formula
        )
        
        self.apply_smart_colorize(
            quadratic_group,
            {
                "b": B_COLOR,
                "c": C_COLOR,
                "x": X_COLOR,
                "a": A_COLOR,
            }
        )
        
        quadratic_form_bg = SurroundingRectangle(
            quadratic_form,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        quadratic_formula_bg = SurroundingRectangle(
            quadratic_formula,
            buff=0.2,
            fill_opacity=0.10,
            fill_color=EQUATION_BG_FILL,
            stroke_color=EQUATION_BG_STROKE,
            stroke_width=1,
            corner_radius=0.1
        )
        
        
        ###############################################################################
        # SOLVING THE EQUATION
        ###############################################################################
        
        
        q_equation = MathTex("1x^2 + 11x + 20 = 0 = 20").scale(TEX_SCALE).to_edge(UP, buff=0.6)
        SmartColorizeStatic(
            q_equation,
            {
                "x": X_COLOR,
                "2": X_COLOR,
            }
        )
        
        a_in_q_equation = self.find_element("1", q_equation, opacity=0)
        b_in_q_equation = self.find_element("11", q_equation, color=B_COLOR)
        
        # c_in_q_equation = self.find_element("20", q_equation, color=C_COLOR)
        
        twenty = self.find_elements("20", q_equation, color=C_COLOR)
        
        twenty_two = self.find_element("20", q_equation, nth=-1, color=RED)
        
        # Create coefficient labels
        a = MathTex("a = 1", color=A_COLOR).scale(TEX_SCALE)
        a_value = self.find_element("1", a)
        
        b = MathTex("b = 11", color=B_COLOR).scale(TEX_SCALE)
        b_value = self.find_element("11", b)
        
        c = MathTex("c = 20", color=C_COLOR).scale(TEX_SCALE)
        c_value = self.find_element("20", c)
        
        coefficients = Group(a, b, c).arrange(buff=1).next_to(q_equation, DOWN * 1.5)
        
        
  
        
        ###############################################################################
        # ANIMATIONS
        ###############################################################################
        
        
        
        
        
        
        self.play(
            FadeIn(
                quadratic_group,
                quadratic_form_bg,
                quadratic_formula_bg
            )
        )
        
        
        self.play(Write(q_equation))
        
        
        self.play(
            FadeIn(a[0][:2], b[0][:2], c[0][:2])
        )
        
        self.play(self.indicate(quad_form_a))
        
        self.play(FadeIn(a_value, target_position=a_in_q_equation), run_time=2)
        
        self.play(self.indicate(quad_form_b))
        
        self.play(FadeIn(b_value, target_position=b_in_q_equation), run_time=2)
        
        self.play(self.indicate(quad_form_c))
        
        self.play(FadeIn(c_value, target_position=twenty[0]), run_time=2)
        
        self.play(self.indicate(twenty))

        
        
        self.play(twenty.animate.set_color(BLUE))