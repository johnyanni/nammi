from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager

config.verbosity = "ERROR"

# Define shared elements pattern
SHARED_ELEMENTS = [
    ('equals', '='),
    ('plus', '+', 0),  # First plus sign if it exists
]

class Pythagoras01b(MathTutorialScene):
    def construct(self):
        
        step1 = VGroup(
            Tex("Pythagoras' Theorem").scale(TEXT_SCALE),
            MathTex("c^2 = a^2 + b^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        step2 = VGroup(
            Tex("Substitute the values of a and b").scale(TEXT_SCALE),
            MathTex(r"c^2 = 5^2 + 10^2").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step3 = VGroup(
            Tex("Simplify").scale(TEXT_SCALE),
            MathTex(r"c^2 = 25 + 100").scale(MATH_SCALE),
            MathTex(r"c^2 = 125").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step4 = VGroup(
            Tex("Calculate the value of c").scale(TEXT_SCALE),
            MathTex(r"\sqrt{c^2} = \sqrt{125}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        step5 = VGroup(
            Tex("Round to 2 decimal places").scale(TEXT_SCALE),
            MathTex(r"c = 11.18 \ \text{cm}").scale(MATH_SCALE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Apply colors
        self.apply_smart_colorize(
            [step1[1], step2[1], step3[1], step3[2], step4[1], step5[1]],
            {
                "c": YELLOW,
                "a^2": GREEN,
                "b^2": RED,
                "c^2": YELLOW,
                "5^2": GREEN,
                "10^2": RED,
                "25": GREEN,
                "100": RED,
                "125": YELLOW,
                "11.18": YELLOW,
            }
        )
        
        # Position formulas
        main = VGroup(step1, step2, step3, step4, step5).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).to_edge(UP, buff=0.4).to_edge(LEFT, buff=1)
        
        # Parse each step with its unique elements + shared elements
        
        # Step 1: Original formula
        formula_parts = self.parse_elements(step1[1],
            ('c', 'c'),
            ('c_squared_exp', '^2', 0),
            ('a', 'a'),
            ('a_squared_exp', '^2', 1),
            ('b', 'b'),
            ('b_squared_exp', '^2', 2),
            *SHARED_ELEMENTS
        )
        
        # Step 2: Substituted values
        sub_parts = self.parse_elements(step2[1],
            ('c_squared', 'c^2'),
            ('five', '5'),
            ('five_squared', '^2', 1),
            ('ten', '10'),
            ('ten_squared', '^2', 2),
            *SHARED_ELEMENTS
        )
        
        # Step 3.1: First simplification
        calc1_parts = self.parse_elements(step3[1],
            ('c_squared', 'c^2'),
            ('twentyfive', '25'),
            ('hundred', '100'),
            *SHARED_ELEMENTS
        )
        
        # Step 3.2: Final result (no plus sign)
        calc2_parts = self.parse_elements(step3[2],
            ('c_squared', 'c^2'),
            ('result', '125'),
            ('equals', '=')
        )
        
        # Step 4: Square root - special handling
        calc3_sqrt = step4[1][0][0:2]
        calc3_c2 = step4[1][0][2:4].set_color(YELLOW)
        calc3_sqrt2 = step4[1][0][5:7]
        calc3_parts = self.parse_elements(step4[1],
            ('equals', '='),
            ('value', '125')
        )
        
        # Step 5: Final answer
        final_parts = self.parse_elements(step5[1],
            ('c', 'c'),
            ('equals', '='),
            ('value', '11.18'),
            ('unit', r'\text{cm}', 0, YELLOW)
        )
        
        # Create elements for ScrollManager
        elements = VGroup(
            step1[0],
            step1[1],
            
            step2[0],
            sub_parts['c_squared'],
            sub_parts['equals'],        # Added equals here
            sub_parts['five'],
            sub_parts['five_squared'],
            sub_parts['plus'],
            sub_parts['ten'],
            sub_parts['ten_squared'],
            
            step3[0],
            calc1_parts['c_squared'],
            calc1_parts['equals'],      # Added equals here
            calc1_parts['twentyfive'],
            calc1_parts['plus'],
            calc1_parts['hundred'],
            
            calc2_parts['c_squared'],
            calc2_parts['equals'],      # Added equals here
            calc2_parts['result'],
            
            step4[0],
            calc3_sqrt,
            calc3_c2,
            calc3_parts['equals'],
            calc3_sqrt2,
            calc3_parts['value'],
            
            step5[0],
            final_parts['c'],
            final_parts['equals'],      # Separated equals
            final_parts['value'],
            final_parts.get('unit', Text("")) # Separated unit
        )
        
        # Create scroll manager
        scroll_mgr = ScrollManager(elements, scene=self)
        
        # Step 1: Show Pythagoras' Theorem
        scroll_mgr.prepare_next()  # "Pythagoras' Theorem" label
        scroll_mgr.prepare_next()  # c² = a² + b² formula
        
        # Step 2: Substitute values
        scroll_mgr.prepare_next()  # "Substitute the values" label
        
        # Transform c² to substituted version
        scroll_mgr.transform_from_copy(
            VGroup(formula_parts['c'], formula_parts['c_squared_exp']), 
            sub_parts['c_squared']
        )
        
        # Transform = sign separately
        scroll_mgr.transform_from_copy(formula_parts['equals'], sub_parts['equals'])
        
        # Transform a to 5
        scroll_mgr.transform_from_copy(formula_parts['a'], sub_parts['five'])
        scroll_mgr.transform_from_copy(formula_parts['a_squared_exp'], sub_parts['five_squared'])
        
        # Transform + sign
        scroll_mgr.transform_from_copy(formula_parts['plus'], sub_parts['plus'])
        
        # Transform b to 10
        scroll_mgr.transform_from_copy(formula_parts['b'], sub_parts['ten'])
        scroll_mgr.transform_from_copy(formula_parts['b_squared_exp'], sub_parts['ten_squared'])
        
        # Step 3: Simplify
        scroll_mgr.prepare_next()  # "Simplify" label
        
        # Transform c² from substituted to simplified
        scroll_mgr.transform_from_copy(sub_parts['c_squared'], calc1_parts['c_squared'])
        
        # Transform = sign separately
        scroll_mgr.transform_from_copy(sub_parts['equals'], calc1_parts['equals'])
        
        # Transform 5² to 25
        scroll_mgr.transform_from_copy(
            VGroup(sub_parts['five'], sub_parts['five_squared']), 
            calc1_parts['twentyfive']
        )
        
        # Transform + sign
        scroll_mgr.transform_from_copy(sub_parts['plus'], calc1_parts['plus'])
        
        # Transform 10² to 100
        scroll_mgr.transform_from_copy(
            VGroup(sub_parts['ten'], sub_parts['ten_squared']), 
            calc1_parts['hundred']
        )
        
        # Step 3 continued: Simplify to c² = 125
        scroll_mgr.transform_from_copy(calc1_parts['c_squared'], calc2_parts['c_squared'])
        
        # Transform = sign separately
        scroll_mgr.transform_from_copy(calc1_parts['equals'], calc2_parts['equals'])
        
        # Transform 25 + 100 to 125
        scroll_mgr.transform_from_copy(
            VGroup(calc1_parts['twentyfive'], calc1_parts['plus'], calc1_parts['hundred']), 
            calc2_parts['result']
        )
        
        # Scroll to make room
        scroll_mgr.scroll_down(steps=2)
        
        # Step 4: Calculate c
        scroll_mgr.prepare_next()  # "Calculate the value of c" label
        scroll_mgr.prepare_next()  # Show √ symbol
        
        # Transform c² to √c²
        scroll_mgr.transform_from_copy(calc2_parts['c_squared'], calc3_c2)
        
        # Show equals sign
        scroll_mgr.prepare_next()  # Show =
        
        # Show second √ symbol
        scroll_mgr.prepare_next()  # Show √
        
        # Transform 125 to √125
        scroll_mgr.transform_from_copy(calc2_parts['result'], calc3_parts['value'])
        
        # Scroll to make room for final answer
        scroll_mgr.scroll_down(steps=8)
        
        # Step 5: Final result
        scroll_mgr.prepare_next()  # "Round to 2 decimal places" label
        
        # Transform √c² to c
        scroll_mgr.transform_from_copy(calc3_c2, final_parts['c'])
        
        # Transform equals sign from step 4
        scroll_mgr.transform_from_copy(calc3_parts['equals'], final_parts['equals'])
        
        # Transform √125 to 11.18 cm
        scroll_mgr.transform_from_copy(
            calc3_parts['value'], 
            VGroup(final_parts['value'], final_parts.get('unit', Text("")))
        )
        
        self.wait(2)