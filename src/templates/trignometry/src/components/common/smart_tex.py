"""Smart TeX utilities for Manim animations."""

from manim import *
from typing import Dict, List, Union, Optional, Tuple

def search_shape_in_text(text: VMobject, shape: VMobject, index=0, threshold=100000):
    r"""Receives two VMobjects resulting from rendering text (either by Tex, Text
    or MathTex) and looks for occurrences of the second in the first, but comparing
    the shapes and not the text itself.
    
    In essence, it goes through all the elements of text[index] grouped according to the
    number of elements of shape[0], and for each group it calculates a hash of
    both shapes and compares them.
    
    It returns a list with all the indices of text[index] where it was found. Each
    element of that list is a slice because the text may span more than one
    element of text[0].
    
    The parameter threshold influences the result. With its default value of None
    the matching of shapes can produce some false positives (but this is how manim's
    TransformMatchingShapes works too). You can give it very large values (above 100000)
    to reduce the chance of false positives, at the cost of a little longer run time.
    
    Example (changing the color of all x's):
       gx = MathTex(r'''
            g(x) = \begin{cases} 
            x(2-x) &(|x-1| \leq 1) \\
            0 &(|x-1| > 1)
            \end{cases}''')
        self.add(gx)
        self.wait()
        self.play(*[
            Transform(gx[0][group], MathTex("a").move_to(gx[0][group]), path_arc=-PI)
            for group in search_shape_in_text(gx, MathTex("x"))
        ])
        self.wait()
    """

    # Define the font template
    template = TexTemplate()
    template.add_to_preamble(
        r"""
        \usepackage[T1]{fontenc}
        \usepackage{txfonts}
        """
    )

    if hasattr(text, "tex_string") and not isinstance(text, Tex):
        text_copy = MathTex(text.tex_string, tex_template=template)
    elif hasattr(text, "tex_strings"):
        text_copy = Tex(*text.tex_strings, tex_template=template)
    else:
        text_copy = text

    if hasattr(shape, "tex_string") and not isinstance(shape, Tex):
        shape_copy = MathTex(shape.tex_string, tex_template=template)
    elif hasattr(shape, "tex_strings"):
        shape_copy = Tex(*shape.tex_strings, tex_template=template)
    else:
        shape_copy = shape

    # Perform the shape search
    results = _do_shape_search(text_copy, shape_copy, index, threshold)

    return results


def _do_shape_search(text: VMobject, shape: VMobject, index=0, threshold=100000):
    """Internal function that does the actual shape searching"""

    def get_mobject_key(mobject: Mobject) -> int:
        mobject.save_state().center().scale_to_fit_height(1)
        r = np.array2string(
            mobject.points,
            precision=2,
            separator=" ",
            suppress_small=True,
            threshold=threshold,
        )
        r = r.replace("-0. ", " 0. ")
        mobject.restore()
        return hash(r)

    results = []
    l = len(shape.submobjects[0])
    shape_aux = VMobject()
    shape_aux.points = np.concatenate([p.points for p in shape.submobjects[0]])
    for i in range(len(text.submobjects[index]) - l + 1):
        subtext = VMobject()
        subtext.points = np.concatenate(
            [p.points for p in text.submobjects[index][i : i + l]]
        )
        if get_mobject_key(subtext) == get_mobject_key(shape_aux):
            results.append(slice(i, i + l))
    return results


def search_shapes_in_text(text: VMobject, shapes: list[VMobject], index=0):
    r"""Like the previous one, but receives a list of possible sub-texts to search for.
    Example (replaces all x's, both normal and small ones,
    which have a different shape):
        gx = MathTex(r'''
            \sum_{x=0}^\infty \frac{1}{x!} = e^x
            ''').scale(3)
        self.add(gx)
        self.wait()
        self.play(*[
            gx[0][group].animate.set_color(YELLOW)
            for group in search_shapes_in_text(gx, [MathTex("x"), MathTex("^x")])
        ])
        self.wait()
    """
    results = []
    for shape in shapes:
        results += search_shape_in_text(text, shape, index)
    return results


def group_shapes_in_text(text: VMobject, shapes: VMobject | list[VMobject], index=0):
    r"""
    This functions receives a text in which it has to search a given shape (or list of shapes)
    It returns a VGroup with the shapes found in the text
    It is a usability improvement with respect to search_shape_in_text, because it directly returns
    a group of VMobjects instead of index slices. It also accepts a list or a single shape.
    Example of use (replaces all x's, both normal and small ones,
    which have a different shape):
        gx = MathTex(r'''
            \sum_{x=0}^\infty \frac{1}{x!} = e^x
            ''').scale(3)
        self.add(gx)
        self.wait()
        results = group_shapes_in_text(gx, [MathTex("x"), MathTex("^x")])
        self.play(results.animate.set_color(YELLOW))
        self.wait()
    """
    if isinstance(shapes, VMobject):
        shapes = [shapes]
    results = search_shapes_in_text(text, shapes, index)
    if not results:
        # print(
        #     f"No results found for {''.join(shapes[0].tex_string.split(' ')[1:])[:-1]}"
        # )
        return VGroup(MathTex(""))

    return VGroup(*[text[index][s] for s in results])


def colorize_similar_tex(eq, config, index=0):
    # Small adition (inspired by VirusMinus8 discord user
    """
    This function receives a Tex or MathTex object and a dictionary. The dictionary keys
    are strings and the values are colors. The strings are rendered through MathTex
    and the resulting shape is searched in eq. All occurences are changed to the given
    color. If an index is provided, the search happens only inside `eq[index]`, for the
    case it has several submobject. index=0 searchs all the submobjects.
    """
    for key, color in config.items():
        group_shapes_in_text(eq, MathTex(key)).set_color(color)
    return eq


def all_sizes_symbol(txt: str, template=None):
    """Builds a list of Tex objects with the same symbol in different sizes and templates.
    Includes both default LaTeX and custom template versions.

    Args:
        txt: The symbol or expression to render
        template: Optional TeX template to use (if None, only uses default)
    """
    sizes = [r"\displaystyle", r"\textstyle", r"\scriptstyle", r"\scriptscriptstyle"]
    results = []

    # Create math mode versions with default LaTeX
    results.append(MathTex(f"{txt}"))

    # If template provided, add template versions
    if template:
        results.extend(
            [MathTex(f"{size} {txt}", tex_template=template) for size in sizes]
        )

    # Only add text versions for simple text (not math expressions)
    if all(c.isalnum() for c in txt):  # Check if txt is alphanumeric
        # Add default text versions
        results.extend([MathTex(f"{size} \\text{{{txt}}}") for size in sizes])
        # Add template text versions if template provided
        if template:
            results.extend(
                [
                    MathTex(f"{size} \\text{{{txt}}}", tex_template=template)
                    for size in sizes
                ]
            )

    return results


def set_color_by_shape_map(text: VMobject, color_map: dict):
    r"""Colors elements in text based on their shape, similar to set_color_by_tex_to_color_map
    but works by matching shapes instead of tex strings.

    Args:
        text: VMobject (usually from Tex or MathTex)
        color_map: Dictionary mapping tex strings to colors

    Example:
        set_color_by_shape_map(equation, {
            "x": RED,
            "y": BLUE,
            r"\circ": YELLOW
        })
    """
    for tex, color in color_map.items():
        group_shapes_in_text(text, all_sizes_symbol(tex)).set_color(color)
    return text


def SmartColorizeStatic(text: VMobject, color_map: dict, template=None):
    """Creates a list of FadeToColor animations for elements in text based on their shape.
    Checks both default LaTeX style and custom template style for better matching.

    Args:
        text: VMobject (usually from Tex or MathTex)
        color_map: Dictionary mapping tex strings to either a color or a tuple of (color, indices)
        template: Optional TeX template to use for matching
    """
    if template is None and hasattr(text, "tex_template"):
        template = text.tex_template

    for tex, value in color_map.items():
        # Determine color and indices
        if isinstance(value, tuple):
            color, indices = value
        else:
            color, indices = value, None

        # Try with both default and custom template
        default_shapes = all_sizes_symbol(tex)  # Default LaTeX style
        template_shapes = (
            all_sizes_symbol(tex, template) if template else []
        )  # Custom template style

        # Combine results from both shape sets
        groups = group_shapes_in_text(text, default_shapes + template_shapes)

        # Apply color only to specified indices, or all if indices is None
        if indices is not None:
            # Handle slice objects
            if isinstance(indices, slice):
                groups = groups[indices]
            else:
                groups = [groups[i] for i in indices]

        for group in groups:
            group.set_color(color)

    return text


def SmartColorize(text: VMobject, color_map: dict, template=None):
    """Creates a list of FadeToColor animations for elements in text based on their shape.
    Checks both default LaTeX style and custom template style for better matching.

    Args:
        text: VMobject (usually from Tex or MathTex)
        color_map: Dictionary mapping tex strings to either a color or a tuple of (color, indices)
        template: Optional TeX template to use for matching
    """
    if template is None and hasattr(text, "tex_template"):
        template = text.tex_template

    animations = []
    for tex, value in color_map.items():
        # Determine color and indices
        if isinstance(value, tuple):
            color, indices = value
        else:
            color, indices = value, None

        # Try with both default and custom template
        default_shapes = all_sizes_symbol(tex)  # Default LaTeX style
        template_shapes = (
            all_sizes_symbol(tex, template) if template else []
        )  # Custom template style

        # Combine results from both shape sets
        groups = group_shapes_in_text(text, default_shapes + template_shapes)

        # Apply color only to specified indices, or all if indices is None
        if indices is not None:
            # Handle slice objects
            if isinstance(indices, slice):
                groups = groups[indices]
            else:
                groups = [groups[i] for i in indices]
        # If indices is None, color all groups
        animations.extend([FadeToColor(group, color) for group in groups])

    return AnimationGroup(*animations)
