"""Component for positioning arrows and lines and for creating expanded expressions."""

from manim import *

def get_normal(line_start_pt, line_end_pt, proportion=0.5, length=1, angle=90*DEGREES):
    l = Line(line_start_pt, line_end_pt)
    normal = l.copy().scale_to_fit_width(length).get_vector()
    
    vector = Vector(normal)
    vector.rotate(angle)
    vector.shift(l.point_from_proportion(proportion) - vector.get_start())
    return vector

def curved_arrow_to_angle(mob, angle_mob, angle=90*DEGREES, proportion=0.5, length=None, buff_from_mob=0.2, start_direction='bottom', **kwargs):
    line_start_pt = angle_mob.get_start()
    line_end_pt = angle_mob.get_end()
    
    if not length:
        length = np.linalg.norm(line_start_pt - line_end_pt) / 6
    
    # Handle direction input
    if isinstance(start_direction, str):
        direction_map = {
            'up': (mob.get_top, UP),
            'down': (mob.get_bottom, DOWN),
            'left': (mob.get_left, LEFT),
            'right': (mob.get_right, RIGHT),
            'bottom': (mob.get_bottom, DOWN),
            'top': (mob.get_top, UP)
        }
        get_point, direction = direction_map.get(start_direction.lower(), (mob.get_bottom, DOWN))
        start_point = get_point() + (buff_from_mob * direction)
    else:
        # If direction is a vector, use get_point_from_direction
        start_point = mob.get_center() + np.array(start_direction) + (buff_from_mob * np.array(start_direction))
        
    l = Line(line_start_pt, line_end_pt)
    normal = get_normal(line_start_pt, line_end_pt, proportion, length, angle)
    arrow = CurvedArrow(start_point, normal.get_end(), angle=angle, **kwargs)
    return arrow

def get_expanded_expression(expression, values, length=0.2):
    res = []
    for i in range(len(expression[0])):
        l = Arrow(expression[0][i].get_top(), expression[0][i].copy().shift(UP).get_center(), buff=0).scale_to_fit_width(length)
        if i != 1: 
            rotation_angle = PI/6 if i < 1 else -PI/6
            l.rotate(rotation_angle, about_point=l.get_start())
        
        # Color the text based on the value
        if values[i] == "Opp":
            val = Tex(values[i], color=GREEN)
        elif values[i] == "Adj":
            val = Tex(values[i], color=RED)
        else:
            val = Tex(values[i])
            
        val.scale(0.8).move_to(l.copy().scale(1.8).get_end())
        res.append(VGroup(l, val))
        
    return res
        
class RotatedCircumscribe(Circumscribe):
    def __init__(self, *args, angle: float = 0, **kwargs):
        super().__init__(*args, **kwargs) 
        frame = self.animations[0].mobject
        frame.rotate(angle, about_point=frame.get_center())
