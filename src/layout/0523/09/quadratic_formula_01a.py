from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.smart_tex import SmartColorizeStatic

config.verbosity = "ERROR"

MATH_SCALE = 1.20

class QuadraticFormula01(MathTutorialScene): 
    def construct(self):

        A_COLOR = "#47e66c"
        B_COLOR = "#ff79c6"
        C_COLOR = "#00bfff"
        
        
        
        
        
        
        # ============================================
        # SECTION 1: QUESTION
        # ============================================
        
        question_text = MathTex(r"\text{Solve using the quadratic formula:} \; 4(x+5)^2 = 48").scale(LABEL_SCALE).set_color(LIGHT_GRAY).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.4)

        self.play(
            Write(question_text, run_time=3),  
        )
        
        self.wait(1)    
    
    
    
    
    
        # ============================================
        # SECTION 2: FORMULAS
        # ============================================
        
        quadratic_form = self.create_labeled_formula(
            "Standard Form",
            r"ax^2 + bx + c = 0"
        )
        
        quadratic_formula = self.create_labeled_formula(
            "Quadratic Formula",
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        )
        
        quadratic_group = VGroup(
            quadratic_form.group,
            quadratic_formula.group
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.2).to_corner(DR, buff=0.3).set_color(LIGHT_GRAY)
        
        # DEV MODE        
        quadratic_form_coefficients = self.parse_elements(quadratic_form.formula,
            ('a', 'a', 0, A_COLOR),
            ('b', 'b', 0, B_COLOR),
            ('c', 'c', 0, C_COLOR)
        )
        
        self.apply_smart_colorize(
            [quadratic_formula.formula],
            {
                "a": A_COLOR,
                "b": B_COLOR,
                "c": C_COLOR
            }
        )
        
        
        self.play(
            self.FadeInThenWrite(
                [quadratic_form.background],
                [quadratic_form.label, quadratic_form.formula],
            )
        )
        
        self.wait(1)
        
        self.play(
            self.FadeInThenWrite(
                [quadratic_formula.background], 
                [quadratic_formula.label, quadratic_formula.formula],
            )
        )
        
        self.wait(1)
                           
                   
                   

        
        
        scroll = ScrollManager(scene=self)
        
        
        
        # ============================================
        # SECTION 3: SOLUTION
        # ============================================
        
        
        
        # ======== Step 1: Convert to standard form (divide by 4) ========
      
        s1_divide_step = scroll.construct_step(
            scroll.create_tex(r"First, get the equation in \textbf{standard form}:", label="l_convert_to_standard_form"),
            scroll.create_tex(r"Divide both sides by 4", label="l_divide_both_sides_by_4"),
            scroll.create_annotated_equation(
                r"4(x+5)^2 = 48",
                r"\div 4",
                "4",
                "48",
                label="ae_divide_both_sides_by_4"
            ),
            scroll.create_math_tex(r"(x+5)^2 = 12", label="m_divide_by_4_result")
        )
        
        
        
        
        # ======== Step 2: Expand the squared term (FOIL) ========
        
        s2_expand_step = scroll.construct_step(
            scroll.create_tex("Expand the squared term:", label="l_expand_squared_term"),
            scroll.create_math_tex(r"(x+5)^2 = (x+5)(x+5)", label="m_expand_squared_term", color=LIGHT_GRAY, scale=M_MATH_SCALE),
            scroll.create_math_tex("x^2 + 10x + 25 = 12", label="m_expand_squared_term_result")
        )
        
        
        
            
        # ======== Step 3: Get in standard form (subtract 12) ========

        s3_subtract_step = scroll.construct_step(
            scroll.create_tex("Subtract 12 from both sides:", label="l_subtract_12_from_both_sides"),
            scroll.create_annotated_equation(
                r"x^2 + 10x + 25 = 12",
                "-12",
                "25",
                "12",
                label="ae_subtract_12_from_both_sides"
            ),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0", label="m_subtract_12_from_both_sides_result")
        )
            
            
            
        
        # ======== Step 4: Standard form: Identify coefficients ========
        
        s4_identify_coefficients_step = scroll.construct_step(
            scroll.create_tex("Now, identify the coefficients:"),
            scroll.create_math_tex(r"x^2 + 10x + 13 = 0"),
            scroll.create_math_tex(r"a = 1 \quad b = 10 \quad c = 13", scale=1.0),
            add_to_scroll=False,
            buff=0.3
        )
        
        coefficient_values_in_equation = self.parse_elements(
            s4_identify_coefficients_step[1],
            ('a_value', 'x', 0, A_COLOR),  
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )
        
        coefficient_labels = self.parse_elements(
            s4_identify_coefficients_step[2],
            ('a_label', 'a =', 0, A_COLOR),
            ('b_label', 'b =', 0, B_COLOR),
            ('c_label', 'c =', 0, C_COLOR)
        )
                
        coefficient_values = self.parse_elements(
            s4_identify_coefficients_step[2],
            ('a_value', '1', 0, A_COLOR),
            ('b_value', '10', 0, B_COLOR),
            ('c_value', '13', 0, C_COLOR)
        )
        
        scroll.create_steps(s4_identify_coefficients_step[:-1], ["l_identify_coefficients", "m_standard_form_equation"], arrange=False)
        scroll.create_steps(coefficient_labels.values(), ["coefficient_a_label", "coefficient_b_label", "coefficient_c_label"], arrange=False)
        scroll.create_steps(coefficient_values.values(), ["coefficient_a_value", "coefficient_b_value", "coefficient_c_value"], arrange=False)
        
        
        
        # ======== Step 5: Use the quadratic formula ========
        
        s5_quadratic_formula_step = scroll.construct_step(
            scroll.create_tex(r"Use the \textbf{quadratic formula} to solve for $x$:", label="l_quadratic_formula"),
            scroll.create_math_tex(r"x \quad = \quad \frac{-b \pm \sqrt{b^2 \ - \ 4ac}}{2a}", label="m_quadratic_formula")
        )
        
        coefficient_values_in_formula = self.parse_elements(
            s5_quadratic_formula_step[1],
            ('b', 'b', B_COLOR),
            ('a1', 'a', 0, A_COLOR),
            ('c', 'c', C_COLOR),
            ('a2', 'a', 1, A_COLOR)
        )
        
        
        
        # ======== Step 6: Substitute values ========
        
        s6_substitute_values_step = scroll.construct_step(
            scroll.create_tex(r"Substitute the coefficients into the formula:"),
            scroll.create_math_tex(r"x = \frac{-(10) \pm \sqrt{(10)^2 - 4(1)(13)}}{2(1)}"),
            add_to_scroll=False
        )
        
        substituted_values = self.parse_elements(
            s6_substitute_values_step[1],
            ('b_in_frac', '10', 0, B_COLOR, 0),
            ('b_in_sqrt', '10', 1, B_COLOR, 0),
            ('a_in_4ac', '1', 2, A_COLOR, 0),
            ('c_in_4ac', '13', 0, C_COLOR, 0),
            ('a_in_denom', '1', -1, A_COLOR, 0)
        )
        
        visible_copies = VGroup()

        for name, element in substituted_values.items():
            visible_copy = element.copy().set_opacity(1)
            setattr(visible_copies, name, visible_copy)
            visible_copies.add(visible_copy)
        
        s6_substitute_values_step[1].add(visible_copies)
        
        scroll.create_steps(s6_substitute_values_step, ["l_substitute_values", "m_empty_formula"], arrange=False)
        scroll.create_steps(visible_copies, arrange=False)
        
        
        
        
       
        
        
        
        
        
        
        # ===============================================================
        # SCROLL ARRANGEMENT
        # ===============================================================
        
        sol_steps = scroll.get_arranged_equations()
        sol_steps.next_to(question_text, DOWN, buff=0.4).align_to(question_text, LEFT)
        
        
        
        
        
        
        
        
        # ===============================================================
        # ===============================================================
        # ANIMATIONS
        # ===============================================================
        # ===============================================================
        
        
        
        # ===============================================================
        # Animation: Step 1: Convert to standard form (divide by 4) 
        # ===============================================================
        
        scroll.prepare_next("l_convert_to_standard_form")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        scroll.prepare_next("l_divide_both_sides_by_4")
        scroll.prepare_next("ae_divide_both_sides_by_4")
        scroll.prepare_next("m_divide_by_4_result")
        
        self.wait(1)
        
        
        
        
        
        
        
        # ===============================================================
        # Animation: Step 2: Expand the squared term (FOIL) 
        # ===============================================================

        scroll.prepare_next("l_expand_squared_term")
        scroll.prepare_next("m_expand_squared_term")
        scroll.prepare_next("m_expand_squared_term_result")
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("ae_divide_both_sides_by_4")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        
        # ===============================================================
        # Animation: Step 3: Get in standard form (subtract 12) 
        # ===============================================================
        
        scroll.prepare_next("l_subtract_12_from_both_sides")
        scroll.prepare_next("ae_subtract_12_from_both_sides")
        scroll.prepare_next("m_subtract_12_from_both_sides_result")
        self.play(self.indicate(quadratic_form.group, scale_factor=1.2))
        
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        total_in_view = scroll.current_position - scroll.last_in_view
        scroll.scroll_down(steps=total_in_view - 1, run_time=2)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        # ===============================================================
        # Animation: Step 4: Standard form: Identify coefficients 
        # ===============================================================
        
        scroll.prepare_next("l_identify_coefficients")
        scroll.prepare_next("m_standard_form_equation")
        
        scroll.prepare_next("coefficient_a_label")
        scroll.prepare_next("coefficient_b_label")
        scroll.prepare_next("coefficient_c_label")
        
        self.play(self.indicate(quadratic_form_coefficients['a']))
        scroll.fade_in_from_target(coefficient_values_in_equation['a_value'], coefficient_values['a_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['b']))
        scroll.fade_in_from_target(coefficient_values_in_equation['b_value'], coefficient_values['b_value'])
        
        self.play(self.indicate(quadratic_form_coefficients['c']))
        scroll.fade_in_from_target(coefficient_values_in_equation['c_value'], coefficient_values['c_value'])
        
        self.wait(1)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        scroll.scroll_down("m_standard_form_equation")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        
        
        
        
        
        
        
        # ===============================================================
        # Animation: Step 5: The quadratic formula 
        # ===============================================================
        
        scroll.prepare_next("l_quadratic_formula")
        self.play(self.indicate(quadratic_formula.group, scale_factor=1.2))
        scroll.prepare_next("m_quadratic_formula")
        
        self.wait(1)
        
        
        
        
        
        # ===============================================================
        # Animation: Step 6: Substitute values 
        # ===============================================================
       
        scroll.prepare_next("l_substitute_values")
        scroll.prepare_next("m_empty_formula")
        
        self.play(
            self.indicate(coefficient_values['b_value'], color=None),
            self.indicate(coefficient_values_in_formula['b'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_frac)
        scroll.fade_in_from_target(coefficient_values['b_value'], visible_copies.b_in_sqrt)
        
        
        self.play(
            self.indicate(coefficient_values['a_value'], color=None),
            self.indicate(coefficient_values_in_formula['a1'], color=None),
        )
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_4ac)
    
            
        self.play(
            self.indicate(coefficient_values['c_value'], color=None),
            self.indicate(coefficient_values_in_formula['c'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['c_value'], visible_copies.c_in_4ac)
        
        
        self.play(
            self.indicate(coefficient_values['a_value'], color=None),
            self.indicate(coefficient_values_in_formula['a2'], color=None)
        )
        scroll.fade_in_from_target(coefficient_values['a_value'], visible_copies.a_in_denom)
       
        self.wait(1)
        
        
        
        
        
        
        
        


        

        
        

        
        
        
        
        
        