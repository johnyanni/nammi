from manim import *
from math import radians
from trig_variants import *
from triangle_config import *
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

        self._steps = self._get_solution_steps()
        self._triangle = self._build()
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

        if self.h:
            B = 4 * RIGHT
            C = 5 * UP
        else:
            B = 5 * RIGHT
            C = 4 * UP
        
        
        full_triangle = VGroup()
        self.components = {}

        # Configuration dictionaries
        rotation_config = ROTATION_CONFIG
        angle_config = ANGLE_CONFIG
        side_names_config = SIDE_NAMES_CONFIG
        side_edge_config = SIDE_EDGE_CONFIG

        # Create triangle
        triangle = self._create_triangle(A, B, C, rotation_config)
        full_triangle.add(triangle)

        # Get rotated vertices
        A, B, C = triangle.get_vertices()
        D = self.get_foot_of_perpendicular(A, B, C) if self.h else None
        
        # Add altitude if needed
        if self.h:
            altitude, h_label = self._create_altitude(A, D, side_edge_config)
            full_triangle.add(altitude, h_label)
            
        # Create right angle indicator
        right_angle = self._create_right_angle(A, B, C, D)
        full_triangle.add(right_angle)

        # Add side labels
        self._add_side_labels(full_triangle, A, B, C, side_names_config, side_edge_config)            

        # Add angle labels
        self._add_angle_labels(full_triangle, A, B, C, angle_config)

        # Set colors
        self._apply_colors()

        # Store unknown info
        self._store_unknown_info(side_names_config)

        # Store triangle info
        self.components["triangle"] = triangle if not self.h else VGroup(triangle, altitude)
        self.components["right_angle"] = right_angle
        
        # Center the triangle
        full_triangle.move_to(ORIGIN)    
        
        return full_triangle


    def _create_triangle(self, A, B, C, rotation_config):
        triangle = Polygon(A, B, C, color=self.color).set_z_index(2)
        rotation = rotation_config.get(self.right_angle_position, 0)

        if self.h:
            rotation = -Angle.from_three_points(A, B, C).get_value() + PI

        return triangle.rotate(rotation)

    def _create_right_angle(self, A, B, C, D):
        if self.h:
            right_angle = Angle.from_three_points(B, D, A, elbow=True, radius=0.3)
        else:
            right_angle = Angle.from_three_points(B, A, C, elbow=True, radius=0.3)
            
        return right_angle

    def _create_altitude(self, A, D, edge_config):
        altitude = Line(A, D)
        
        label_position = get_normal(A, D, length=self.label_shift)
        value_label = MathTex(self.h).scale(self.label_scale)
        name_label = Tex("opp").scale(self.label_scale)

        label_group = VGroup(name_label, value_label).arrange(DOWN)
        label_group.move_to(label_position.get_end())
        label_group.set_color(self.color_map["opp"])

        # Store components
        self.components[f"label_h"] = value_label
        self.components[f"label_h_name"] = name_label    
    
        return altitude, label_group

    def _add_side_labels(self, container, A, B, C, side_names_config, side_edge_config):
        vertices = {"a": (A, C), "b": (B, A), "c": (C, B)}
        known_angle = "alpha" if self.alpha else "beta"

        for side, value in [("a", self.a), ("b", self.b), ("c", self.c)]:
            if not value: continue

            v1, v2 = vertices[side]
            label_group = self._create_side_label(
                v1, v2, value, side, known_angle, side_names_config, side_edge_config
            )
            container.add(label_group)

    def _create_side_label(self, v1, v2, value, side, known_angle, side_names_config, side_edge_config):
        label_position = get_normal(v1, v2, length=self.label_shift)
        angle = self._calculate_rotation_angle(v1, v2)

        # Adjust for specific side
        if side == "c":
            angle = self._adjust_hypotenuse_angle(angle)
            # label_position = get_normal(v1, v2, length=self.label_shift + 0.5)
            
        # Create value label
        value_label = MathTex(value).scale(self.label_scale)
    
        # Create name label
        side_name = side_names_config[known_angle][side] if not self.h else "hyp"

        if self.h and self.unknown != side:
            name_label = None
        else:
            name_label = Tex(side_name).scale(self.label_scale)
    
        # Group and position
        label_group = VGroup()
        if name_label: label_group.add(name_label)
        label_group.add(value_label)
        label_group.arrange(DOWN).rotate(angle)
        label_group.set_color(self.color_map[side_name])
    
        edge_alignment = side_edge_config[self.right_angle_position].get(side, ORIGIN)
        label_group.move_to(label_position.get_end())#, aligned_edge=edge_alignment)
        
        # Store components
        self.components[f"label_{side}"] = value_label
        self.components[f"label_{side}_name"] = name_label
    
        return label_group

    def _calculate_rotation_angle(self, p1, p2):
        angle = Line(p1, p2).get_angle()
        if abs(round(angle, 3)) in [round(x, 3) for x in [PI / 2, PI]]:
            return 0
        return angle

    def _adjust_hypotenuse_angle(self, angle):
        if self.right_angle_position in ["top_right", "top_left"]:
            return PI + angle
        return angle

    def _add_angle_labels(self, container, A, B, C, angle_config):
        if self.alpha:
            angle_group = self._create_angle_label(
                C, B, A, self.alpha, "alpha", angle_config, self.indicate_alpha_with_arrow
            )
            container.add(angle_group)

        if self.beta:
            angle_group = self._create_angle_label(
                A, C, B, self.beta, "beta", angle_config, self.indicate_beta_with_arrow
            )
            container.add(angle_group)

    def _create_angle_label(self, p1, p2, p3, value, angle_name, angle_config, use_arrow):
        angle_obj = Angle.from_three_points(p1, p2, p3, radius=self.angle_radius)
        label = MathTex(rf"{value}").scale(self.label_scale)

        if not use_arrow:
            position = get_normal(angle_obj.get_end(), angle_obj.get_start(), length=self.angle_shift)
            label.move_to(position.get_end())
            group = VGroup(angle_obj, label)
        else:
            config = angle_config[self.right_angle_position][angle_name]
            position = get_normal(
                angle_obj.get_end(), angle_obj.get_start(),
                proportion=0.6, length=1.2, angle=config["angle"]
            )
            label.move_to(position.get_end())

            arrow = curved_arrow_to_angle(
                label, angle_obj,
                start_direction=config["arrow_start"],
                radius=config["arrow_radius"]
            ).set_z_index(3)

            group = VGroup(angle_obj, label, arrow)

        # Store components
        self.components[f"label_{angle_name}"] = label
        if hasattr(self, 'alpha') and angle_name == "alpha" and self.alpha:
            self.components["alpha_value"] = group
        elif hasattr(self, 'beta') and angle_name == "beta" and self.beta:
            self.components["beta_value"] = group

        return group

    def _apply_colors(self):
        for angle_name in ["alpha", "beta"]:
            label_key = f"label_{angle_name}"
            if label_key in self.components:
                self.components[label_key].set_color(self.color_map["angle"])
    
    def _store_unknown_info(self, side_names_config):
        known_angle = "alpha" if self.alpha else "beta"
    
        if self.unknown not in ["alpha", "beta"]:
            side_name = "hyp" if self.h else side_names_config[known_angle][self.unknown]
            self.components["unknown_color"] = self.color_map.get(side_name)
        else:
            self.components["unknown_color"] = self.color_map.get("angle")
    
        self.components["unknown_label"] = self.components.get(f"label_{self.unknown}")
                
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
                ("h", "beta"): lambda: generate_sin_variants(h_val, self.a, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("b", "alpha"): lambda: generate_tan_variants(self.a, b_val, "opp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("c", "alpha"): lambda: generate_sin_variants(self.a, c_val, "opp", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
                ("b", "beta"): lambda: generate_tan_variants(self.a, b_val, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
                ("c", "beta"): lambda: generate_cos_variants(self.a, c_val, "adj", self.beta, beta_val, unit=unit, prec=self.solution_prec),
            },
            "b": {
                ("h", "alpha"): lambda: generate_sin_variants(h_val, self.b, "adj", self.alpha, alpha_val, unit=unit, prec=self.solution_prec),
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
    
