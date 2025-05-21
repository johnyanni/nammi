from math import sin, cos, tan, asin, acos, atan, degrees
from utils import *

angle_prec = 6

def generate_sin_variants(opp, hyp, unknown, original_angle, angle_rad, angle_symbol=r"\theta", unit=None, prec=2):
    sin_angle = round(sin(angle_rad), angle_prec)
    unit_exp = fr"\ \text{{{unit}}}" if unit else ''
    if unknown == "opp":
        middle_val = round(hyp * sin(angle_rad), angle_prec)
        final_val = round(middle_val, prec)
        return [
            fr"\sin({angle_symbol}) = \frac{{\text{{opp}}}}{{\text{{hyp}}}}",
            # fr"\sin({original_angle}) = \frac{{{adj}}}{{{hyp}}}",
            fr"{hyp} \times \sin({original_angle}) = \frac{{{opp}}}{{{hyp}}} \times {hyp}",
            fr"{opp} = {hyp} \times \sin({original_angle})",
            dms_steps("sin", original_angle),
            fr"{opp} = {hyp} \times {sin_angle}",
            fr"{opp} = {middle_val}",
            fr"{opp} = {final_val} {unit_exp}"
        ]
    middle_val = round(opp / sin(angle_rad), angle_prec)
    final_val = round(middle_val, prec)
    return [
        fr"\sin({angle_symbol}) = \frac{{\text{{opp}}}}{{\text{{hyp}}}}",
        fr"\sin({original_angle}) = \frac{{{opp}}}{{{hyp}}}",
        fr"{hyp} = \frac{{{opp}}}{{\sin({original_angle})}}",
        dms_steps("sin", original_angle),
        fr"{hyp} = \frac{{{opp}}}{{{sin_angle}}}",
        fr"{hyp} = {middle_val}",
        fr"{hyp} = {final_val} {unit_exp}"
    ]

        
def generate_cos_variants(adj, hyp, unknown, original_angle, angle_rad, angle_symbol=r"\theta", unit=None, prec=2):
    cos_angle = round(cos(angle_rad), angle_prec)
    unit_exp = fr"\ \text{{{unit}}}" if unit else ''
    if unknown == "adj":
        middle_val = round(hyp * cos(angle_rad), angle_prec)
        final_val = round(middle_val, prec)
        return [
            fr"\cos({angle_symbol}) = \frac{{\text{{adj}}}}{{\text{{hyp}}}}",
            # fr"\cos({original_angle}) = \frac{{{adj}}}{{{hyp}}}",
            fr"{hyp} \times \cos({original_angle}) = \frac{{{adj}}}{{{hyp}}} \times {hyp}",
            fr"{adj} = {hyp} \times \cos({original_angle})",
            dms_steps("cos", original_angle),
            fr"{adj} = {hyp} \times {cos_angle}",
            fr"{adj} = {middle_val}",
            fr"{adj} = {final_val} {unit_exp}"
        ]

    middle_val = round(adj / cos(angle_rad), angle_prec)
    final_val = round(middle_val, prec)
    return [
        fr"\cos({angle_symbol}) = \frac{{\text{{adj}}}}{{\text{{hyp}}}}",
        fr"\cos({original_angle}) = \frac{{{adj}}}{{{hyp}}}",
        fr"{hyp} = \frac{{{adj}}}{{\cos({original_angle})}}",
        dms_steps("cos", original_angle),
        fr"{hyp} = \frac{{{adj}}}{{{cos_angle}}}",
        fr"{hyp} = {middle_val}",
        fr"{hyp} = {final_val} {unit_exp}"
    ]

def generate_tan_variants(opp, adj, unknown, original_angle, angle_rad, angle_symbol=r"\theta", unit=None, prec=2):
    tan_angle = round(tan(angle_rad), angle_prec)
    unit_exp = fr"\ \text{{{unit}}}" if unit else ''
    if unknown == "opp":
        middle_val = round(adj * tan(angle_rad), angle_prec)
        final_val = round(middle_val, prec)
        return [
            fr"\tan({angle_symbol}) = \frac{{\text{{adj}}}}{{\text{{opp}}}}",
            # fr"\tan({original_angle}) = \frac{{{opp}}}{{{adj}}}",
            fr"{adj} \times \tan({original_angle}) = \frac{{{opp}}}{{{adj}}} \times {adj}",
            fr"{opp} = {adj} \times \tan({original_angle})",
            dms_steps("tan", original_angle),
            fr"{opp} = {adj} \times {tan_angle}",
            fr"{opp} = {middle_val}",
            fr"{opp} = {final_val} {unit_exp}"
        ]

    middle_val = round(opp / tan(angle_rad), angle_prec)
    final_val = round(middle_val, prec)
    return [
        fr"\tan({angle_symbol}) = \frac{{\text{{adj}}}}{{\text{{opp}}}}",
        fr"\tan({original_angle}) = \frac{{{adj}}}{{{opp}}}",
        fr"{opp} = \frac{{{adj}}}{{\tan({original_angle})}}",
        dms_steps("tan", original_angle),
        fr"{opp} = \frac{{{adj}}}{{{tan_angle}}}",
        fr"{opp} = {middle_val}",
        fr"{opp} = {final_val} {unit_exp}"
    ]


def generate_asin_variants(opp, hyp, angle_symbol=r"\theta", prec=2):
    opp_over_hyp = round(opp / hyp, angle_prec)
    asin_val = round(degrees(asin(opp_over_hyp)), angle_prec)
    dms_val = decimal_to_dms(asin_val)
    final_val = decimal_to_dms(asin_val, round_to=prec)
    return [
        fr"\sin({angle_symbol}) = \frac{{\text{{opp}}}}{{\text{{hyp}}}}",
        fr"\sin({angle_symbol}) = \frac{{{opp}}}{{{hyp}}}",
        # fr"\sin({angle_symbol}) = {opp_over_hyp}",
        # fr"{angle_symbol} = \sin^{{-1}}\left({opp_over_hyp}\right)",
        fr"{angle_symbol} = \sin^{{-1}}\left( \frac{{{opp}}}{{{hyp}}} \right)",
        inverse_trig_steps("sin", rf"{opp} \div {hyp}"),
        fr"{angle_symbol} = {asin_val}^\circ \quad \framebox[1cm]{{\strut DMS}}",
        fr"{angle_symbol} = {dms_val}",
        fr"{angle_symbol} = {final_val}",
    ]

def generate_acos_variants(adj, hyp, angle_symbol=r"\theta", prec=2):
    adj_over_hyp = round(adj / hyp, angle_prec)
    acos_val = round(degrees(acos(adj_over_hyp)), angle_prec)
    dms_val = decimal_to_dms(acos_val)
    final_val = decimal_to_dms(acos_val, round_to=prec)
    return [
        fr"\cos({angle_symbol}) = \frac{{\text{{adj}}}}{{\text{{hyp}}}}",
        fr"\cos({angle_symbol}) = \frac{{{adj}}}{{{hyp}}}",
        # fr"\cos({angle_symbol}) = {adj_over_hyp}",
        # fr"{angle_symbol} = \cos^{{-1}}\left({adj_over_hyp}\right)",
        fr"{angle_symbol} = \cos^{{-1}}\left( \frac{{{adj}}}{{{hyp}}} \right)",
        inverse_trig_steps("cos", rf"{adj} \div {hyp}"),
        fr"{angle_symbol} = {acos_val}^\circ \quad \framebox[1cm]{{\strut DMS}}",
        fr"{angle_symbol} = {dms_val}",
        fr"{angle_symbol} = {final_val}",
    ]

def generate_atan_variants(opp, adj, angle_symbol=r"\theta", prec=2):
    opp_over_adj = round(opp / adj, angle_prec)
    atan_val = round(degrees(atan(opp_over_adj)), angle_prec)
    dms_val = decimal_to_dms(atan_val)
    final_val = decimal_to_dms(atan_val, round_to=prec)
    return [
        fr"\tan({angle_symbol}) = \frac{{\text{{opp}}}}{{\text{{adj}}}}",
        fr"\tan({angle_symbol}) = \frac{{{opp}}}{{{adj}}}",
        # fr"\tan({angle_symbol}) = {opp_over_adj}",
        # fr"{angle_symbol} = \tan^{{-1}}\left({opp_over_adj}\right)",
        fr"{angle_symbol} = \tan^{{-1}}\left( \frac{{{opp}}}{{{adj}}} \right)",
        inverse_trig_steps("tan", rf"{opp} \div {adj}"),
        fr"{angle_symbol} = {atan_val}^\circ \quad \framebox[1cm]{{\strut DMS}}",
        fr"{angle_symbol} = {dms_val}",
        fr"{angle_symbol} = {final_val}",
    ]

