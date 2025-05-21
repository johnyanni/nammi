from manim import *
from math import radians
from trig_variants import *
from utils import *

class Triangle:
    def __init__(
            self,
            a=None,
            b=None,
            c=None,
            h=None,
            alpha=None,
            beta=None,
            unknown=None,
            indicate_alpha_with_arrow=True,
            indicate_beta_with_arrow=True,
            label_shift=0.3,
            label_scale=0.65,
            angle_shift=0.4,
            angle_radius=0.8,
            right_angle_position="bottom_left",
            solution_prec=2,
            color=WHITE,
            color_map=None 
    ):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.alpha = alpha
        self.beta = beta
        self.unknown = unknown
        self.indicate_alpha_with_arrow = False if unknown in ["alpha", "beta"] else indicate_alpha_with_arrow
        self.indicate_beta_with_arrow = False if unknown in ["alpha", "beta"] else  indicate_beta_with_arrow
        self.label_shift = label_shift
        self.label_scale = label_scale
        self.angle_shift = angle_shift
        self.angle_radius = angle_radius
        self.right_angle_position = "perpendicular_foot" if h else right_angle_position
        self.solution_prec = solution_prec
        self.color = color
        if color_map:
            self.color_map = color_map
        else:
            self.color_map = {
                "hyp": GREEN,
                "opp": RED,
                "adj": YELLOW,
                "angle": BLUE,
            }
        
        self._triangle = self._build()
        self._steps = self._get_solution_steps()
    def get_foot_of_perpendicular(self, A, B, C):
        BC = C - B
        t = np.dot(A - B, BC) / np.dot(BC, BC)
        D = B + t * BC
        return D
    
    def triangle(self):
        return self._triangle 

    def get_steps(self):
        return self._steps
    
    def get_final_solution(self):
        solution = self._steps[-1]
        return solution
    
    def extract_unit(self, s):
        if not s:
            return None
        
        units = ["km", "mm", "cm", "m"]
        unit_match = next((u for u in units if u in s), None)
        return unit_match

    def _build(self):
        A = ORIGIN
        B = 4 * RIGHT
        C = 3 * UP
        # B = 3 * RIGHT
        # C = 4 * UP
        
        full_triangle = VGroup()
        self.components = {}
        labels_map = {}
        label_positions_map = {}
        label_angles_map = {}
        label_aligned_edge_map = {}
        
        rotation_map = {
            "top_right": PI,
            "top_left": -PI / 2,
            "bottom_right": PI / 2,
            "bottom_left": 0,
            "perpendicular_foot": PI - Line(C, B).get_angle(),
        }

        angle_config = {
            "top_right": {
                "alpha": {"angle": 235 * DEGREES, "arrow_start": "right", "arrow_radius": -PI / 3},
                "beta": {"angle": -155 * DEGREES, "arrow_start": "right", "arrow_radius": PI / 3},
            },
            "top_left": {
                "alpha": {"angle": 5 * DEGREES, "arrow_start": "left", "arrow_radius": -PI / 3},
                "beta": {"angle": -85 * DEGREES, "arrow_start": "left", "arrow_radius": PI / 3},
            },
            "bottom_right": {
                "alpha": {"angle": -25 * DEGREES, "arrow_start": "right", "arrow_radius": -PI / 3},
                "beta": {"angle": -155 * DEGREES, "arrow_start": "down", "arrow_radius": PI / 3},
            },
            "bottom_left": {
                "alpha": {"angle": 200 * DEGREES, "arrow_start": "up", "arrow_radius": PI / 3},
                "beta": {"angle": -155 * DEGREES, "arrow_start": "left", "arrow_radius": PI / 3},
            },
            "perpendicular_foot": {
                "alpha": {"angle": -65 * DEGREES, "arrow_start": "right", "arrow_radius": PI / 3},
                "beta": {"angle": -45 * DEGREES, "arrow_start": "down", "arrow_radius": -PI / 3},
            }
        }

        side_names_map = {
            "alpha": {"a": "opp", "b": "adj", "c": "hyp"},
            "beta":  {"a": "adj", "b": "opp", "c": "hyp"},
        }

        side_edge_map = {
            "top_right": {"a": LEFT, "b": DOWN},
            "top_left": {"a": DOWN, "b": RIGHT},
            "bottom_right": {"a": UP, "b": LEFT},
            "bottom_left": {"a": RIGHT, "b": UP},
            "perpendicular_foot": {"a": ORIGIN, "b": ORIGIN, "h": RIGHT},
        }

        triangle = Polygon(A, B, C, color=self.color).set_z_index(2).rotate(rotation_map[self.right_angle_position])
        full_triangle.add(triangle)

        A, B, C = triangle.get_vertices()
        D = self.get_foot_of_perpendicular(A, B, C)

        if not self.h:
            right_angle = Angle.from_three_points(B, A, C, elbow=True, radius=0.3)
        else:
            altitude = Line(A, D)
            right_angle = Angle.from_three_points(B, D, A, elbow=True, radius=0.3)

            label_h_position = get_normal(D, A, length=self.label_shift)
            label_h = MathTex(self.h).scale(self.label_scale).move_to(
                label_h_position.get_end(),
                aligned_edge=side_edge_map[self.right_angle_position]["h"]
            )
            label_h_position.set_opacity(0)
            full_triangle.add(altitude, label_h, label_h_position)
            self.components["label_h"] = label_h
            label_positions_map["h"] = label_h_position
            label_angles_map["h"] = 0
            label_aligned_edge_map["h"] = side_edge_map[self.right_angle_position]["h"]

        full_triangle.add(right_angle)

        def rotation_angle(p1, p2):
            angle = Line(p1, p2).get_angle()
            if abs(round(angle, 3)) in [round(x, 3) for x in [PI / 2, PI]]:
                return 0
            return angle

        known_angle = "alpha" if self.alpha else "beta"
        if self.a:
            label_a_position = get_normal(A, C, length=self.label_shift)
            label_a_angle = rotation_angle(A, C)
            label_a = MathTex(self.a).scale(self.label_scale).rotate(label_a_angle)
            labels_map["a"] = label_a
            label_positions_map["a"] = label_a_position
            label_angles_map["a"] = label_a_angle
            label_aligned_edge_map["a"] = side_edge_map[self.right_angle_position]["a"]

            # a -> opp of alpha, a -> adj of beta
            side_name = side_names_map[known_angle]["a"]
            label_a_name = Tex(side_name).scale(self.label_scale).rotate(label_a_angle)

            label_a_group = VGroup(label_a_name, label_a).arrange(DOWN)
            label_a_group.set_color(self.color_map[side_name])
            label_a_group.move_to(
                label_a_position.get_end(),
                aligned_edge=side_edge_map[self.right_angle_position]["a"]
            )
            label_a_position.set_opacity(0)
            full_triangle.add(label_a, label_a_position)
            full_triangle.add(label_a_name)
            self.components["label_a"] = label_a
            self.components["label_a_name"] = label_a_name
                
                
                
        if self.b:
            label_b_position = get_normal(B, A, length=self.label_shift)
            label_b_angle = rotation_angle(B, A)
            label_b = MathTex(self.b).scale(self.label_scale).rotate(label_b_angle)
            labels_map["b"] = label_b
            label_positions_map["b"] = label_b_position
            label_angles_map["b"] = label_b_angle
            label_aligned_edge_map["b"] = side_edge_map[self.right_angle_position]["b"]

            # b -> adj of alpha, b -> opp of beta
            side_name = side_names_map[known_angle]["b"]
            label_b_name = Tex(side_name).scale(self.label_scale).rotate(label_b_angle)
            
            label_b_group = VGroup(label_b_name, label_b).arrange(DOWN)
            label_b_group.set_color(self.color_map[side_name])
            label_b_group.move_to(
                label_b_position.get_end(),
                aligned_edge=side_edge_map[self.right_angle_position]["b"]
            )
            label_b_position.set_opacity(0)
            full_triangle.add(label_b, label_b_position)
            full_triangle.add(label_b_name)
            self.components["label_b"] = label_b
            self.components["label_b_name"] = label_b_name
            

        if self.c:
            # if self.right_angle_position in ["top_right", "top_left"]:
            #     label_c_angle = 0
            #     label_shift_offset = 0.2
            # else:
            #     label_c_angle = rotation_angle(C, B)
            #     label_shift_offset = 0
            label_c_angle = rotation_angle(C, B)
            label_shift_offset = 0.5
            if self.right_angle_position in ["top_right", "top_left"]:
                label_c_angle = PI + label_c_angle
            
            label_c_position = get_normal(C, B, length=self.label_shift + label_shift_offset)
            label_c = MathTex(self.c).scale(self.label_scale).rotate(label_c_angle).move_to(label_c_position.get_end())
            labels_map["c"] = label_c
            label_positions_map["c"] = label_c_position
            label_angles_map["c"] = label_c_angle
            
            side_name = side_names_map[known_angle]["c"]
            label_c_name_position = get_normal(C, B, length=self.label_shift + label_shift_offset - 0.5)
            label_c_name = Tex(side_name).scale(self.label_scale).rotate(label_c_angle).move_to(label_c_name_position.get_end())

            VGroup(label_c, label_c_name).set_color(self.color_map[side_name])
            label_c_position.set_opacity(0)
            full_triangle.add(label_c, label_c_position)
            full_triangle.add(label_c_name)
            self.components["label_c"] = label_c
            self.components["label_c_name"] = label_c_name
            
            
        # Angles
        if self.alpha:
            alpha_obj = Angle.from_three_points(C, B, A, radius=self.angle_radius)
            alpha_label = MathTex(rf"{self.alpha}").scale(self.label_scale)
            if not self.indicate_alpha_with_arrow:
                alpha_position = get_normal(alpha_obj.get_end(), alpha_obj.get_start(), length=self.angle_shift)
                alpha_label.move_to(alpha_position.get_end())
                alpha_position.set_opacity(0)
                full_triangle.add(alpha_obj, alpha_label, alpha_position)
                labels_map["alpha"] = alpha_label
                self.components["label_alpha"] = alpha_label
            else:
                alpha_position = get_normal(
                    alpha_obj.get_end(), alpha_obj.get_start(),
                    proportion=0.6, length=1.2,
                    angle=angle_config[self.right_angle_position]["alpha"]["angle"]
                )
                alpha_label.move_to(alpha_position.get_end())
                alpha_arrow = curved_arrow_to_angle(
                    alpha_label, alpha_obj,
                    start_direction=angle_config[self.right_angle_position]["alpha"]["arrow_start"],
                    radius=angle_config[self.right_angle_position]["alpha"]["arrow_radius"]
                ).set_z_index(3)
                full_triangle.add(alpha_obj, alpha_label, alpha_arrow)
                labels_map["alpha"] = alpha_label
                self.components["label_alpha"] = alpha_label

        if self.beta:
            beta_obj = Angle.from_three_points(A, C, B, radius=self.angle_radius)
            beta_label = MathTex(rf"{self.beta}").scale(self.label_scale)
            if not self.indicate_beta_with_arrow:
                beta_position = get_normal(beta_obj.get_end(), beta_obj.get_start(), length=self.angle_shift)
                beta_label.move_to(beta_position.get_end())
                beta_position.set_opacity(0)
                full_triangle.add(beta_obj, beta_label, beta_position)
                labels_map["beta"] = beta_label
                self.components["label_beta"] = beta_label
            else:
                beta_position = get_normal(
                    beta_obj.get_end(), beta_obj.get_start(),
                    proportion=0.6, length=1.2,
                    angle=angle_config[self.right_angle_position]["beta"]["angle"]
                )
                beta_label.move_to(beta_position.get_end())
                beta_arrow = curved_arrow_to_angle(
                    beta_label, beta_obj,
                    start_direction=angle_config[self.right_angle_position]["beta"]["arrow_start"],
                    radius=angle_config[self.right_angle_position]["beta"]["arrow_radius"]
                ).set_z_index(3)
                full_triangle.add(beta_obj, beta_label, beta_arrow)
                labels_map["beta"] = beta_label
                self.components["label_beta"] = beta_label

        if self.h: self.components["triangle_w_h"] = VGroup(triangle, altitude)
        
        full_triangle.move_to(ORIGIN)
        
        if self.unknown not in ["alpha", "beta"]:
            side_name = side_names_map[known_angle][self.unknown]
            self.components["unknown_color"] = self.color_map.get(side_name)
        else:
            self.components["unknown_color"] = self.color_map.get("angle")
        self.components["unknown_label"] = labels_map.get(self.unknown, None)
        self.components["unknown_label_position"] = label_positions_map.get(self.unknown, None)
        self.components["unknown_label_angle"] = label_angles_map.get(self.unknown, None)
        self.components["unknown_label_edge"] = label_aligned_edge_map.get(self.unknown, ORIGIN)

        self.components["triangle"] = triangle
        self.components["right_angle"] = right_angle
        
        if self.alpha:
            self.components["angle_value"] = VGroup(alpha_obj, alpha_label)
            if self.indicate_alpha_with_arrow: self.components["angle_value"].add(alpha_arrow)
        elif self.beta:
            self.components["angle_value"] = VGroup(beta_obj, beta_label)
            if self.indicate_beta_with_arrow: self.components["angle_value"].add(beta_arrow)
            
        # Colors
        try:
            alpha_label.set_color(self.color_map["angle"])
        except:
            pass

        try:
            beta_label.set_color(self.color_map["angle"])
        except:
            pass
    
        
        return full_triangle
    
    def _get_solution_steps(self):
        if self.unknown not in {"a", "b", "c", "h", "alpha", "beta"}:
            return []

        def get_val(v):
            return extract_number(v) if isinstance(v, str) else v

        a_val = get_val(self.a)
        b_val = get_val(self.b)
        c_val = get_val(self.c)
        h_val = get_val(self.h)

        # Extract unit
        for m in [self.a, self.b, self.c, self.h]:
            unit = self.extract_unit(m)
            if unit:
                break
        
        try:
            alpha_val = round(radians(get_val(self.alpha)), 5) if self.alpha else None
        except:
            alpha_val = None
        try:
            beta_val = round(radians(get_val(self.beta)), 5) if self.beta else None
        except:
            beta_val = None

        known_vals = {
            "a": a_val,
            "b": b_val,
            "c": c_val,
            "h": h_val,
            "alpha": alpha_val,
            "beta": beta_val,
        }
        
        trig_expressions = {
            "a": {
                ("h", "beta"): lambda: generate_cos_variants(self.a, h_val, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("b", "alpha"): lambda: generate_tan_variants(self.a, b_val, "opp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("c", "alpha"): lambda: generate_sin_variants(self.a, c_val, "opp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("b", "beta"): lambda: generate_tan_variants(self.a, b_val, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("c", "beta"): lambda: generate_cos_variants(self.a, c_val, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
            },
            "b": {
                ("h", "alpha"): lambda: generate_sin_variants(self.b, h_val, "adj", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("a", "alpha"): lambda: generate_tan_variants(self.b, a_val, "adj", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("c", "alpha"): lambda: generate_cos_variants(self.b, c_val, "adj", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("a", "beta"): lambda: generate_tan_variants(self.b, a_val, "opp", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("c", "beta"): lambda: generate_sin_variants(self.b, c_val, "opp", self.beta, beta_val, unit=unit, prec=self.solution_prec),
            },
            "c": {
                ("a", "alpha"): lambda: generate_sin_variants(a_val, self.c, "hyp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("b", "alpha"): lambda: generate_cos_variants(b_val, self.c, "hyp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("b", "beta"): lambda: generate_sin_variants(b_val, self.c, "hyp", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("a", "beta"): lambda: generate_cos_variants(a_val, self.c, "hyp", self.beta, beta_val, unit=unit, prec=self.solution_prec),
            },
            "alpha": {
                ("b", "h"): lambda: generate_asin_variants(h_val, b_val, self.alpha, prec=self.solution_prec),
                ("a", "c"): lambda: generate_asin_variants(a_val, c_val, self.alpha, prec=self.solution_prec),
                ("a", "b"): lambda: generate_atan_variants(a_val, b_val, self.alpha, prec=self.solution_prec),
                ("b", "c"): lambda: generate_acos_variants(b_val, c_val, self.alpha, prec=self.solution_prec),
            },
            "beta": {
                ("b", "h"): lambda: generate_asin_variants(h_val, a_val, self.beta, prec=self.solution_prec),
                ("a", "c"): lambda: generate_acos_variants(a_val, c_val, self.beta, prec=self.solution_prec),
                ("a", "b"): lambda: generate_atan_variants(b_val, a_val, self.beta, prec=self.solution_prec),
                ("b", "c"): lambda: generate_asin_variants(b_val, c_val, self.beta, prec=self.solution_prec),
            }
        }

        for param_set, generator in trig_expressions.get(self.unknown, {}).items():
            if all(known_vals[p] is not None for p in param_set):
                return generator()
            
        return []
    
