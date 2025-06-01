from manim import *
import re

def get_normal(line_start_pt, line_end_pt, proportion=0.5, length=1.0, angle=90*DEGREES):
    l = Line(line_start_pt, line_end_pt)

    line_vector = l.get_unit_vector()
    normal_vector = np.array([-line_vector[1], line_vector[0], 0])
    normal_vector = normal_vector * length
    
    vector = Vector(normal_vector)
    vector.rotate(-90*DEGREES)
    vector.rotate(angle)
        
    vector.shift(l.point_from_proportion(proportion) - vector.get_start())

    return vector

def curved_arrow_to_angle(mob, angle_mob, angle=90*DEGREES, proportion=0.5, length=None, buff=0.1, start_direction='bottom', **kwargs):
    line_start_pt = angle_mob.get_start()
    line_end_pt = angle_mob.get_end()
    
    if not length:
        length = np.linalg.norm(line_start_pt - line_end_pt) / 6
        
    # Handle direction input
    if isinstance(start_direction, str):
        direction_map = {
            'up': mob.get_top,
            'down': mob.get_bottom,
            'left': mob.get_left,
            'right': mob.get_right,
            'bottom': mob.get_bottom,
            'top': mob.get_top
        }
        start_point = direction_map.get(start_direction.lower(), mob.get_bottom)()
    else:
        # If direction is a vector, use get_point_from_direction
        start_point = mob.get_center() + np.array(start_direction)


    direction_vector = start_point - mob.get_center()
    if np.linalg.norm(direction_vector) > 0:
        direction_unit = direction_vector / np.linalg.norm(direction_vector)
        start_point = start_point + buff * direction_unit
        
    normal = get_normal(line_start_pt, line_end_pt, proportion, length, angle)
    arrow = CurvedArrow(start_point, normal.get_end(), angle=angle, tip_length=0.20, **kwargs)
    return arrow

def get_expanded_expression(expression, values, length=0.2, hyp_color=GREEN, adj_color=RED, opp_color=ORANGE):
    res = []
    for i in range(len(expression[0])):
        l = Arrow(expression[0][i].get_top(), expression[0][i].copy().shift(UP).get_center(), buff=0).scale_to_fit_width(length)
        if i != 1: 
            rotation_angle = PI/6 if i < 1 else -PI/6
            l.rotate(rotation_angle, about_point=l.get_start())
            
        # Color the text based on the value
        if values[i] == "Hyp":
            val = Tex(values[i], color=hyp_color)
        elif values[i] == "Adj":
            val = Tex(values[i], color=adj_color)
        elif values[i] == "Opp":
            val = Tex(values[i], color=opp_color)
        else:
            val = Tex(values[i])
            
        val.scale(0.7).move_to(l.copy().scale(1.5).get_end())
        res.append(VGroup(l, val))
        
    return res


def dms_terms(angle):
    degree_idx = angle.find("\\circ")
    minute_idx = angle.find("'")
    
    degrees = angle[:degree_idx - 1]

    if minute_idx != -1:
        minutes = angle[degree_idx + 6:minute_idx]
    else:
        minutes = None
    return degrees, minutes, None

def dms_steps(func, angle):
    degrees, minutes, seconds = dms_terms(angle)
    if degrees and not (minutes or seconds):
        return rf"\framebox[1cm]{{\strut {func}}} \quad {degrees} \quad \framebox[1cm]{{\strut =}}"
    
    if not seconds:
        return rf"\framebox[1cm]{{\strut {func}}} \quad {degrees} \quad \framebox[1cm]{{\strut DMS}} \quad {minutes} \quad \framebox[1cm]{{\strut DMS}} \quad \framebox[1cm]{{\strut =}}"
    
    return rf"\framebox[1cm]{{\strut {func}}} \quad {degrees} \quad \framebox[1cm]{{\strut DMS}} \quad {minutes} \quad \framebox[1cm]{{\strut DMS}} \quad {seconds} \quad \framebox[1cm]{{\strut DMS}} \quad  \framebox[1cm]{{\strut =}}"

def decimal_to_dms(decimal_degrees, round_to=3):
    degrees = int(decimal_degrees)
    remainder = abs(decimal_degrees - degrees) * 60
    minutes = int(remainder)
    seconds = int(round((remainder - minutes) * 60, 0))
    
    # Handle floating point rounding errors
    if seconds >= 60:
        seconds -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        degrees += 1

    if round_to == 2: 
        minutes += seconds > 30
        return fr"{degrees}^\circ\ {minutes}'"
    elif round_to == 1:
        minutes += seconds > 30
        degrees += minutes > 30
        return fr"{degrees}^\circ"
    return fr"{degrees}^\circ\ {minutes}'\ {seconds}''"


def inverse_trig_steps(func, ratio):
    return rf"\framebox[1cm]{{\strut Shift}} \quad \framebox[1cm]{{\strut {func}}} \quad {ratio} \quad \framebox[1cm]{{\strut =}}"

def color_indices(obj, idx_list, color="#00BFFF"):
    for i in idx_list:
        obj[0][i].set_color(color)
        obj[0][i].set_stroke_width(3)

def add_underline(
        mobject,
        color=RED, line_width=2,
        line_spacing=0.05, buff=0.1,
        comment=None, comment_scale=0.70,
        comment_color=RED, comment_right_buff=1,
        comment_down_buff=0
):
    width = mobject.width
    
    underline1 = Line(
        start=np.array([-width/2, 0, 0]),
        end=np.array([width/2, 0, 0]),
        stroke_width=line_width,
        color=color,
    )
    underline2 = underline1.copy()
    
    underlines = VGroup(underline1, underline2).arrange(DOWN, buff=line_spacing)
    underlines.next_to(mobject, DOWN, buff=buff)

    if comment:
        comment = MathTex(f"{comment}").scale(comment_scale).set_color(comment_color).next_to(underlines, RIGHT * comment_right_buff + DOWN * comment_down_buff)
    return VGroup(underlines, comment) if comment else underlines

    
def extract_number(s, convert_angle=True):
    if not s:
        return None
    # Match degrees like 11^\circ 12'
    angle_match = re.match(
        r"(\\?(\d+))\^\\?circ"
        r"(?:\s*(\d+)[']?)?"
        r"(?:\s*(\d+)[\"″]?)?", 
        s
    )
    if angle_match:
        degrees_part = int(angle_match.group(2))
        minutes_part = int(angle_match.group(3) or 0)
        seconds_part = int(angle_match.group(4) or 0)
        if convert_angle:
            return degrees_part + minutes_part / 60 + seconds_part / 3600
        return degrees_part, minutes_part, seconds_part

    # General number extractor 
    num_match = re.search(r"[-+]?[0-9]*\.?[0-9]+", s)
    if num_match:
        num = float(num_match.group())
        if int(num) == num:
            return int(num)
        return num
    
    return None

