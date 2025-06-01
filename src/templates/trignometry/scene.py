# %%
from manim import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.base_scene import *
from src.components.common.quick_tip import *
from src.components.common.smart_tex import *
from triangle import Triangle
from utils import color_indices, add_underline, dms_terms, extract_number, get_expanded_expression

config.media_width = "80%"

# %%
def get_side_name(side, angle):
    if side == "c" or h is not None:
        return "hyp"
    
    if angle == "alpha":
        return "adj" if side == "b" else "opp"
    return "adj" if side == "a" else "opp"

def get_side_color(side, angle):
    side_name = get_side_name(side, angle)
    if side_name == "adj": return ADJ_COLOR
    if side_name == "opp": return OPP_COLOR
    if side_name == "hyp": return HYP_COLOR

def get_trig_eqn(s):
    if s.tex_string[1] == "c":
        return "cos"
    elif s.tex_string[1] == "s":
        return "sin"
    elif s.tex_string[1] == "t":
        return "tan"

    return None
    
def get_known_angle(alpha, beta):
    return alpha if alpha else beta

# %%
# Colors
TRIANGLE_COLOR = WHITE
ANGLE_COLOR = BLUE
HYP_COLOR = GREEN
OPP_COLOR = RED
ADJ_COLOR = TEAL
COMMENTS_COLOR = YELLOW
SUBTITLE_COLOR = GREY

TOP_EDGE_BUFF = 1.4
STEPS_BUFF = 0.45

# %%
# Triangle with h
a = "a"
b = "19"
c = None
h = "17.6"
alpha = r"68^\circ"
beta = r"13^\circ"
unknown = "a"
right_angle_position = "perpendicular_foot"
solution_prec = 2 
indicate_alpha_with_arrow = True  
indicate_beta_with_arrow = False  



# Triangle 
"""
a = None
b = r"37.8 \text{ cm}"
c = "h"
h = None 
alpha = None
beta = r"47^\circ 12'"
unknown = "c"
right_angle_position = "top_left" # bottom_right, bottom_left, top_right, top_left
solution_prec = 2                 # In case of angle, 2 = nearest minute
indicate_alpha_with_arrow = True  # Has no effect when unknown is "alpha" or "beta"
indicate_beta_with_arrow = True  # Has no effect when unknown is "alpha" or "beta"
"""

angle_shift = 0.6
label_shift = 0.70
label_scale = 0.70
triangle_scale = 0.70
triangle_edge_buff = 1.5

# %%
%%manim -v ERROR --disable_caching -qh Trig
class Trig(MathTutorialScene):
    def solve_for_angle(self, steps):
        steps[-3][0][-7:].scale(MATH_SCALE).shift(LEFT * 0.2)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=STEPS_BUFF).to_edge(LEFT).shift(RIGHT * 1.5)
        steps.to_edge(UP, buff=TOP_EDGE_BUFF)
        
        # Color steps
        a_val = extract_number(a)
        b_val = extract_number(b)
        c_val = extract_number(c)
        self.apply_smart_colorize(
            steps,
            {
                "\theta": ANGLE_COLOR,
                f"{alpha}": ANGLE_COLOR,
                f"{beta}": ANGLE_COLOR,
                "hyp": HYP_COLOR,
                "opp": OPP_COLOR,
                "adj": ADJ_COLOR,
                f"{a_val}": get_side_color("a", unknown),
                f"{b_val}": get_side_color("b", unknown),
                f"{c_val}": get_side_color("c", unknown),
            }
        )

        # Make sure other steps are white
        steps[-3][0][2:].set_color(WHITE)
        steps[-2][0][2:].set_color(WHITE)
        steps[-1][0][2:].set_color(WHITE)

        # Color calclator comments
        color_indices(steps[-3], [-1, -2, -6, -7])
        color_indices(steps[-4], [0, 1, 7, 8, 9, 10, 14, 15, -1, -2, -4, -5])

        # Add annotation for the seconds
        angle_str = steps[-2].tex_string
        seconds_val = angle_str[angle_str.find("'") + 2:]
        seconds = steps[-2][0][search_shape_in_text(steps[-2], MathTex(f"{seconds_val}"))[0]]
        if int(seconds_val[:-2]) >= 30:
            seconds_underline = add_underline(seconds, comment=r"\ge 30''", color=COMMENTS_COLOR, comment_color=COMMENTS_COLOR)
        else:
            seconds_underline = add_underline(seconds, comment="< 30''", color=COMMENTS_COLOR, comment_color=COMMENTS_COLOR)

        # Data for animations
        step_1_eql_idx = search_shape_in_text(steps[0], MathTex("="))[0]
        step_1_eql = steps[0][0][step_1_eql_idx]
        step_1_trig = steps[0][0][:step_1_eql_idx.start]

        step_2_eql = steps[1][0][step_1_eql_idx]
        step_2_trig = steps[1][0][:step_1_eql_idx.start]
        step_2_left_parent = steps[1][0][3]
        step_2_right_parent = steps[1][0][step_1_eql_idx.start - 1]
        step_2_trig_wo_parent = steps[1][0][:3]
        step_2_angle = steps[1][0][4]
        step_2_right_side = steps[1][0][step_1_eql_idx.stop:]

        step_3_angle = steps[2][0][0]
        step_3_eql = steps[2][0][1]
        step_3_angle_w_eql = steps[2][0][:2]
        step_3_trig = steps[2][0][2:5]
        step_3_inverse = steps[2][0][5:7]
        step_3_left_parent = steps[2][0][7]
        step_3_right_parent = steps[2][0][-1]
        step_3_ratio = steps[2][0][8:-1]


        step_5_degree_symbol_idx = search_shape_in_text(steps[4], MathTex(r"\circ"))[-1]
        step_5_angle_w_eql = steps[4][0][:2]
        step_5_right_side = steps[4][0][2:step_5_degree_symbol_idx.stop]
        step_5_wo_dms = steps[4][0][:step_5_degree_symbol_idx.stop]
        step_5_dms = steps[4][0][step_5_degree_symbol_idx.stop:]        

        step_6_degree_symbol_idx = search_shape_in_text(steps[5], MathTex(r"\circ"))[-1]
        step_6_angle_w_eql = steps[5][0][:2]
        step_6_right_side = steps[5][0][2:]
        step_6_angle_degree = steps[5][0][2:step_6_degree_symbol_idx.stop]

        step_7_degree_symbol_idx = search_shape_in_text(steps[6], MathTex(r"\circ"))[-1]
        step_7_angle_w_eql = steps[6][0][:2]
        step_7_angle_degree = steps[6][0][2:step_7_degree_symbol_idx.stop]
        step_7_angle_remain = steps[6][0][step_7_degree_symbol_idx.stop:]

        # Animations
        scroll_steps = VGroup(
            *steps[:4],
            VGroup(step_5_wo_dms),
            VGroup(step_5_dms),
            steps[5],
            VGroup(seconds_underline),
            steps[-1]
        )
        
        scroll = ScrollManager(scroll_steps)

        # Ratio used
        scroll.prepare_next(self)
        self.wait()
        
        # Plugging in the values
        self.play(
            ReplacementTransform(step_1_trig.copy(), step_2_trig),
            ReplacementTransform(step_1_eql.copy(), step_2_eql),
        )
        self.play(Write(step_2_right_side))
        scroll.prepare_next()
        self.wait()

        # Separate the angle
        self.play(
            ReplacementTransform(step_2_angle.copy(), step_3_angle),
            ReplacementTransform(step_2_eql.copy(), step_3_eql),
            ReplacementTransform(step_2_trig_wo_parent.copy(), step_3_trig),
            ReplacementTransform(step_2_left_parent.copy(), step_3_left_parent),
            ReplacementTransform(step_2_right_parent.copy(), step_3_right_parent),
            ReplacementTransform(step_2_right_side.copy(), step_3_ratio),
        )
        self.play(Write(step_3_inverse))
        scroll.prepare_next()
        self.wait()

        # Calculate the trig value
        scroll.prepare_next(self, animation_type=FadeIn)
        self.wait()
        
        # Plugging in the trig value
        scroll.scroll_down(self, steps=2)

        self.play(
            ReplacementTransform(step_3_angle_w_eql.copy(), step_5_angle_w_eql),
        )
        self.play(Write(step_5_right_side))
        scroll.prepare_next()
        self.wait()

        # Convert to dms
        scroll.prepare_next(self, animation_type=FadeIn)
        self.wait()

        # Converted angle
        self.play(
            ReplacementTransform(step_5_angle_w_eql.copy(), step_6_angle_w_eql),
        )
        self.play(Write(step_6_right_side))
        self.wait()
        
        self.play(
            ReplacementTransform(step_6_angle_w_eql.copy(), step_7_angle_w_eql)
        )
        self.wait()
        scroll.prepare_next()

        # Comment
        scroll.prepare_next(self, animation_type=FadeIn)
        self.wait()
        
        # Round
        self.play(
            ReplacementTransform(step_6_angle_degree.copy(), step_7_angle_degree),
            Write(step_7_angle_remain)
        )
        scroll.prepare_next()
        
        self.play(Create(self.create_surrounding_rectangle(steps[-1], buff=0.15)))
        
    def solve_for_side(self, triangle_obj, steps):
        unknown_label = triangle_obj.components["unknown_label"]
        unknown_label_str= unknown_label.tex_string
        unknown_color = triangle_obj.components["unknown_color"]
                                
        # Arrange steps
        steps.arrange(DOWN, aligned_edge=LEFT, buff=STEPS_BUFF).to_edge(LEFT, buff=1.5)
        steps.to_edge(UP, buff=TOP_EDGE_BUFF)
        
        # Color calclator comments
        if h:
            degrees, minutes, seconds = dms_terms(beta)
        else:
            degrees, minutes, seconds = dms_terms(alpha if alpha else beta)
        if degrees and minutes:
            color_indices(steps[-4], [0, 1, 5, 6])
            color_indices(steps[-4], [7 + len(degrees), 8 + len(degrees), 12 + len(degrees), 13 + len(degrees)])
            dm_offset = len(degrees) + len(minutes)
            color_indices(steps[-4], [14 + dm_offset, 15 + dm_offset, 19 + dm_offset, 20 + dm_offset])
        
            if seconds:
                dms_offset = dm_offset + len(seconds)
                color_indices(steps[-4], [20 + dms_offset, 21 + dms_offset, 25 + dms_offset, 26 + dms_offset])
            color_indices(steps[-4], [-5, -4, -2, -1])
        elif degrees:
            color_indices(steps[-4], [0, 1, 5, 6, -1, -2, -4, -5])
            
        # Add annotation for rounding
        mid_sol_str = steps[-2].tex_string.replace(" ", "")
        decimal_point_idx = mid_sol_str.find(".")

        if decimal_point_idx:
            num_to_check_idx = decimal_point_idx + solution_prec + 1
            comment = r"\ge 5" if int(mid_sol_str[num_to_check_idx]) >= 5 else "< 5"
            underlines = add_underline(
                steps[-2][0][num_to_check_idx],
                comment=comment,
                comment_right_buff=3,
                color=COMMENTS_COLOR,
                comment_color=COMMENTS_COLOR
            )
        else: underlines = None
        
        # Color steps
        if h:
            known_side = extract_number(h)
            known_side_color = OPP_COLOR
        elif known_side := extract_number(a):
            known_side_color = OPP_COLOR if alpha else ADJ_COLOR
        elif known_side := extract_number(b):
            known_side_color = ADJ_COLOR if alpha else OPP_COLOR
        elif known_side := extract_number(c):
            known_side_color = HYP_COLOR

        self.apply_smart_colorize(
            steps[:4],
            {
                f"{unknown_label_str}": unknown_color,
                f"{known_side}": known_side_color,
                f"{degrees}": ANGLE_COLOR,
                f"{minutes}": ANGLE_COLOR,
                r"\circ": ANGLE_COLOR,
                "'": ANGLE_COLOR,
                r"\theta": ANGLE_COLOR,
                f"{alpha}": ANGLE_COLOR,
                f"{beta}": ANGLE_COLOR,
                "hyp": HYP_COLOR,
                "opp": OPP_COLOR,
                "adj": ADJ_COLOR,
            }
        )
        self.apply_smart_colorize(
            steps[4:],
            {
                f"{unknown_label_str}": unknown_color,
                f"{known_side}": known_side_color,
            }
        )

        steps[-2][0][2:].set_color(WHITE)
        
        # Data for animations
        trig_eqn = get_trig_eqn(steps[0])
        known_angle = "beta" if beta else "alpha"
        unknown_side_name = get_side_name(unknown, known_angle)

        if trig_eqn in ["sin", "cos"] and unknown_side_name == "adj" or \
           trig_eqn in ["tan", "sin"] and unknown_side_name == "opp":
            self.find_numerator_steps(triangle_obj, steps, underlines)
        else:
            self.find_denominator_steps(triangle_obj, steps, underlines)
            
        self.play(Create(self.create_surrounding_rectangle(steps[-1], buff=0.15)))
        return

    def find_denominator_steps(self, triangle_obj, steps, comment=None):
        unknown_label = triangle_obj.components["unknown_label"]
        unknown_label_str= unknown_label.tex_string
        
        step_2_eql_idx = search_shape_in_text(steps[1], MathTex("="))[0]
        step_2_den_idx = search_shape_in_text(steps[1], MathTex(f"{unknown_label_str}"))[0]

        step_2_trig_term = steps[1][0][:step_2_eql_idx.start]
        step_2_eql = steps[1][0][step_2_eql_idx]
        step_2_unkown = steps[1][0][step_2_den_idx]
        step_2_num = steps[1][0][step_2_eql_idx.stop:step_2_den_idx.start-1]
        step_2_fraction = steps[1][0][step_2_den_idx.start - 1]
        
        trig_eqn = get_trig_eqn(steps[0])
        step_3_trig_idx = search_shape_in_text(steps[2], MathTex(rf"{{\{trig_eqn}}}"))[0]
        numerator_idx = slice(2, step_3_trig_idx.start - 1)
        
        step_3_unknown = steps[2][0][0]
        step_3_unknown_w_eql = steps[2][0][:2]
        step_3_eql = steps[2][0][1]
        step_3_trig_term = steps[2][0][step_3_trig_idx.start:]
        step_3_fraction = steps[2][0][step_3_trig_idx.start - 1]
        step_3_num = steps[2][0][numerator_idx]

        
        step_5_unknown_w_eql = steps[4][0][:2]
        step_5_num = steps[4][0][numerator_idx]
        step_5_fraction = steps[4][0][numerator_idx.stop]
        step_5_trig_evaluation = steps[4][0][numerator_idx.stop + 1:]
    
        step_6_unknown_w_eql = steps[5][0][:2]
        step_6_right_term = steps[5][0][2:]
        
        step_7_unknown_w_eql = steps[6][0][:2]
        step_7_right_term = steps[6][0][2:]

        scroll_steps = VGroup(
            *steps[:-1],
        )
        if comment:
            scroll_steps.add(VGroup(comment))
        scroll_steps.add(steps[-1])
        
        scroll = ScrollManager(scroll_steps)

        # Ratio used
        scroll.prepare_next(self)
        self.wait()
        
        # Plugging in the values
        scroll.prepare_next(self)
        self.wait()

        # Separate the unknown
        self.play(
            ReplacementTransform(step_2_unkown.copy(), step_3_unknown),
            ReplacementTransform(step_2_eql.copy(), step_3_eql),
            ReplacementTransform(step_2_num.copy(), step_3_num),
            ReplacementTransform(step_2_fraction.copy(), step_3_fraction),
            ReplacementTransform(step_2_trig_term.copy(), step_3_trig_term),
            run_time=2
        )
        scroll.prepare_next()
        self.wait()

        # Calculate the trig value
        self.play(Succession(
            *[
                FadeIn(obj) for obj in steps[3][:]
            ]
        ))
        scroll.prepare_next()
        self.wait()
        
        # Plugging in the trig value
        scroll.scroll_down(self, steps=2)

        self.play(
            ReplacementTransform(step_3_unknown_w_eql.copy(), step_5_unknown_w_eql),
            ReplacementTransform(step_3_num.copy(), step_5_num),
            ReplacementTransform(step_3_fraction.copy(), step_5_fraction),
            run_time=1
        )
        self.play(Write(step_5_trig_evaluation))
        scroll.prepare_next()
        self.wait()

        # Multiply
        self.play(
            ReplacementTransform(step_5_unknown_w_eql.copy(), step_6_unknown_w_eql),
        )
        self.play(Write(step_6_right_term))
        scroll.prepare_next()
        self.wait()

        # Comment
        if comment:
            scroll.prepare_next(self)
            self.wait()
        
        # Round
        self.play(
            ReplacementTransform(step_6_unknown_w_eql.copy(), step_7_unknown_w_eql),
        )
        self.play(Write(step_7_right_term))
        scroll.prepare_next()        

        
    def find_numerator_steps(self, triangle_obj, steps, comment=None):
        unknown_label = triangle_obj.components["unknown_label"]
        unknown_label_str= unknown_label.tex_string
        
        step_2_times_idx = search_shape_in_text(steps[1], MathTex(r"\times"))
        step_2_eql_idx = search_shape_in_text(steps[1], MathTex("="))[0]
        
        step_2_wo_times = steps[1][0][step_2_times_idx[0].stop:step_2_times_idx[-1].start]
        step_2_left_multiply = VGroup(steps[1][0][:step_2_times_idx[0].stop])
        step_2_right_multiply = VGroup(steps[1][0][step_2_times_idx[-1].start:])
        step_2_unkown = steps[1][0][search_shape_in_text(steps[1], MathTex(f"{unknown_label_str}"))[0]]
        step_2_trig_term = steps[1][0][step_2_times_idx[0].stop:step_2_eql_idx.start]
        step_2_eql = steps[1][0][step_2_eql_idx]
        step_2_left_term = steps[1][0][:step_2_eql_idx.start]
        step_2_wo_multiply = VGroup(steps[1][0][step_2_times_idx[0].stop:step_2_times_idx[-1].start])
        
        step_3_times_idx = search_shape_in_text(steps[2], MathTex(r"\times"))[0]
        step_3_unknown = steps[2][0][0]
        step_3_eql = steps[2][0][1]
        step_3_right_term = steps[2][0][2:] # After the =
        step_3_multiply_factor = steps[2][0][2:step_3_times_idx.stop]

        step_5_times_idx = search_shape_in_text(steps[4], MathTex(r"\times"))[0]
        step_5_unknown_w_eql = steps[4][0][:2]
        step_5_multiply_factor = steps[4][0][2:step_5_times_idx.stop]
        step_5_trig_evaluation = steps[4][0][step_5_times_idx.stop:]
    
        step_6_unknown_w_eql = steps[5][0][:2]
        step_6_right_term = steps[5][0][2:]
        
        step_7_unknown_w_eql = steps[6][0][:2]
        step_7_right_term = steps[6][0][2:]

        scroll_steps = VGroup(
            steps[0],
            step_2_wo_multiply,
            step_2_right_multiply,
            step_2_left_multiply,
            *steps[2:-1],
        )
        if comment:
            scroll_steps.add(VGroup(comment))
        scroll_steps.add(steps[-1])
        
        scroll = ScrollManager(scroll_steps)

        # Ratio used
        scroll.prepare_next(self)
        self.wait()
        
        # Plugging in the values
        self.play(Write(step_2_wo_times))
        scroll.prepare_next()
        self.wait()

        # Multiply by the denominator
        self.play(Succession(
            FadeIn(step_2_right_multiply),
            FadeIn(step_2_left_multiply),
        ))
        scroll.prepare_next(steps=2)
        self.wait()

        # Simplify
        self.play(
            ReplacementTransform(step_2_unkown.copy(), step_3_unknown),
            ReplacementTransform(step_2_eql.copy(), step_3_eql),
            ReplacementTransform(step_2_left_term.copy(), step_3_right_term),
            run_time=2
        )
        scroll.prepare_next()
        self.wait()

        # Calculate the trig value
        self.play(Succession(
            *[
                FadeIn(obj) for obj in steps[3][:]
            ]
        ))
        scroll.prepare_next()
        self.wait()
        
        # Plugging in the trig value
        scroll.scroll_down(self, steps=4)

        self.play(
            ReplacementTransform(step_3_unknown.copy(), step_5_unknown_w_eql[0]),
            ReplacementTransform(step_3_eql.copy(), step_5_unknown_w_eql[1]),
            ReplacementTransform(step_3_multiply_factor.copy(), step_5_multiply_factor),
        )
        self.play(Write(step_5_trig_evaluation))
        scroll.prepare_next()
        self.wait()

        # Multiply
        self.play(
            ReplacementTransform(step_5_unknown_w_eql.copy(), step_6_unknown_w_eql),
        )
        self.play(Write(step_6_right_term))
        self.wait()
        scroll.prepare_next()
        self.wait()

        # Comment
        if comment:
            scroll.prepare_next(self, animation_type=FadeIn, run_time=1)
            self.wait()
        
        # Round
        self.play(
            ReplacementTransform(step_6_unknown_w_eql.copy(), step_7_unknown_w_eql),
        )
        self.play(Write(step_7_right_term))
        scroll.prepare_next()        
        
    def construct(self):        
        # Create the triangle
        triangle_obj = Triangle(
            a=a,
            b=b,
            c=c,
            h=h,
            alpha=alpha,
            beta=beta,
            unknown=unknown,
            indicate_alpha_with_arrow=indicate_alpha_with_arrow,
            indicate_beta_with_arrow=indicate_beta_with_arrow,
            right_angle_position=right_angle_position,
            solution_prec=solution_prec,
            label_scale=label_scale,
            label_shift=label_shift,
            angle_shift=angle_shift,
            color=TRIANGLE_COLOR,
            color_map = {
                "hyp": HYP_COLOR,
                "opp": OPP_COLOR,
                "adj": ADJ_COLOR,
                "angle": ANGLE_COLOR,
            }
        )
        unknown_label = triangle_obj.components["unknown_label"]
        unknown_color = triangle_obj.components["unknown_color"]
        unknown_label_str= unknown_label.tex_string
        
        triangle = triangle_obj.triangle().scale(triangle_scale).to_edge(UP, buff=TOP_EDGE_BUFF)
        steps_str = triangle_obj.get_steps()

        # Title
        prec_map = {
            1: "degree",
            2: "minute",
            3: "second",
        }
        title = Tex(f"Find ${unknown_label_str}$").scale(TITLE_SCALE).to_corner(UL)
        title[0][-1].set_color(unknown_color)

        
        
        if unknown in ["beta", "alpha"]:
            subtitle_text = f"nearest {prec_map[solution_prec]}"
        else:
            subtitle_text = f"{solution_prec} dec. places"
        subtitle = Tex(f"({subtitle_text})").scale(MATH_SCALE_SMALL)
        subtitle.set_color(SUBTITLE_COLOR)
        subtitle.next_to(title, RIGHT, buff=0.2)

        # Steps
        steps = VGroup(
            *[
                MathTex(fr"{expr}").scale(MATH_SCALE) for expr in steps_str
            ]
        )
        steps[-4].scale(0.8)

        # Animations
        for component in [
                "triangle", "right_angle", "alpha_value", "beta_value",
                "label_a", "label_b", "label_c", "label_h",
        ]:
            if component in triangle_obj.components:
                self.play(Write(triangle_obj.components[component]), run_time=1.2)
        self.wait()
        
        self.play(FadeIn(title, subtitle))
        self.wait()

        # Add ratios
        if unknown not in ["alpha", "beta"]:
            trig_func = get_trig_eqn(steps[0])
            # Add ratios
            soh = Tex(r"SOH", color=BLUE)
            cah = Tex(r"CAH", color=BLUE)
            toa = Tex(r"TOA", color=BLUE)
            
            sct = VGroup(soh, cah, toa).scale(MATH_SCALE).arrange(RIGHT, aligned_edge=LEFT, buff=1.5).to_edge(DOWN)
            
            ratio = (soh, ["Sin", "Opp", "Hyp"])
            if trig_func == "cos":
                ratio = (cah, ["Cos", "Adj", "Hyp"])
            elif trig_func == "tan":
                ratio = (toa, ["Tan", "Opp", "Adj"])
            expanded_lst = get_expanded_expression(*ratio, hyp_color=HYP_COLOR, adj_color=ADJ_COLOR, opp_color=OPP_COLOR)
            sohcahtoa_all = VGroup(soh, cah, toa, *expanded_lst)
                
            self.play(Write(sct))
            self.wait()

        for component in ["label_a_name","label_b_name", "label_c_name", "label_h_name"]:
            if component in triangle_obj.components and triangle_obj.components[component] is not None:
                self.play(Write(triangle_obj.components[component]), run_time=1)
        self.wait()

        if unknown not in ["alpha", "beta"]:
            self.play(
                *[
                    Write(element)
                    for group in expanded_lst
                    for element in group
                ]
            )
            self.wait()
        
        self.play(triangle.animate.to_edge(RIGHT, buff=triangle_edge_buff))
        self.wait()

        if unknown in ["alpha", "beta"]:
            self.solve_for_angle(steps)           
        else:
            self.solve_for_side(triangle_obj, steps)

        self.wait(4)

# %%



