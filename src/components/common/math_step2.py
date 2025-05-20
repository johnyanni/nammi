from manim import *
from typing import Union, Sequence, Optional

TEX_SCALE = 0.8
TEXT_SCALE = 0.6

class MathStep(VGroup):
    def __init__(self,
                 expressions: Union[str, MathTex, Sequence[Union[str, MathTex]]],
                 label: Optional[str] = None,
                 annotation: Optional[str] = None):
        super().__init__()

        # Convert input to MathTex list
        if isinstance(expressions, (str, MathTex)):
            expressions = [expressions]
        self.expressions = [MathTex(e).scale(TEX_SCALE) if isinstance(e, str) else e.scale(TEX_SCALE) for e in expressions]
        self.expr_group = VGroup(*self.expressions).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.add(self.expr_group)

        # Add label if provided
        if label:
            self.label = Text(label).scale(TEXT_SCALE)
            self.label.next_to(self.expr_group, LEFT, buff=0.4)
            self.add(self.label)

        # Add annotation if provided
        if annotation:
            self.annotation = Text(annotation).scale(TEXT_SCALE)
            self.annotation.next_to(self.expr_group, RIGHT, buff=0.4)
            self.add(self.annotation)

    def reveal(self):
        anims = []
        if hasattr(self, 'label'):
            anims.append(FadeIn(self.label))
        anims += [Write(expr) for expr in self.expressions]
        if hasattr(self, 'annotation'):
            anims.append(FadeIn(self.annotation))
        return anims


class MathStepGroup(VGroup):
    def __init__(self, vertical_spacing: float = 0.6):
        super().__init__()
        self.vertical_spacing = vertical_spacing

    def add_step(self, step: MathStep):
        if len(self.submobjects) == 0:
            step.to_edge(UP, buff=0.6)
        else:
            last_step = self[-1]
            step.next_to(last_step, DOWN, buff=self.vertical_spacing)
        self.add(step)
        return step

    def reveal_next_step(self, scene: Scene, step: MathStep):
        self.add_step(step)
        if len(self.submobjects) == 1:
            scene.play(*step.reveal())
        else:
            old_steps = VGroup(*self[:-1])
            shift_amount = step.height + self.vertical_spacing
            scene.play(
                old_steps.animate.shift(UP * shift_amount),
                FadeIn(step, shift=DOWN)
            )
            scene.play(*step.reveal())

# Helper function to create a labeled math step (label above, expression(s) below), with optional annotations
def create_step(
    label: str,
    expressions: Optional[Union[str, MathTex, Sequence[Union[str, MathTex]]]] = None,
    annotations: Optional[Sequence[Sequence[Mobject]]] = None
) -> VGroup:
    """
    Create a labeled math step with one or more expressions stacked below the label.
    Optionally include annotations (a list of lists), where each inner list contains
    Mobjects to place beneath the corresponding expression.
    """
    label_text = Text(label).scale(TEXT_SCALE)
    # Handle default for backward compatibility
    if expressions is None:
        expr_group = VGroup()
    else:
        if isinstance(expressions, (str, MathTex)):
            exprs = [expressions]
        else:
            exprs = list(expressions)
        exprs = [
            MathTex(expr).scale(TEX_SCALE) if isinstance(expr, str) else expr.scale(TEX_SCALE)
            for expr in exprs
        ]
        # Build group interleaving expressions with optional annotations
        rows = []
        for i, expr in enumerate(exprs):
            rows.append(expr)
            if annotations and i < len(annotations) and annotations[i]:
                # Arrange annotation objects in a row, place below expr
                annot_row = VGroup(*annotations[i]).arrange(RIGHT, buff=0.4)
                annot_row.next_to(expr, DOWN, buff=0.2)
                rows.append(annot_row)
        expr_group = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    # Arrange label above internal expressions with a small spacing
    return VGroup(label_text, expr_group).arrange(DOWN, aligned_edge=LEFT, buff=0.1)


# Helper function to create a labeled math step with expressions and targeted annotations
def create_annotated_step(
    label: str,
    expressions: Sequence[MathTex],
    annotation_map: Optional[Sequence[Tuple[Mobject, Mobject]]] = None,
    annotation_buff: float = 0.2
) -> VGroup:
    """
    Create a labeled math step with expressions and precise annotations.

    Parameters:
    - label: str label shown above the expressions
    - expressions: list of MathTex expressions
    - annotation_map: list of (annotation_mobject, target_mobject) tuples
    - annotation_buff: vertical spacing between expression and its annotations

    Returns:
    - VGroup with label and vertically arranged expression blocks (each expression + its annotations)
    """
    label_text = Text(label).scale(TEXT_SCALE)
    expr_blocks = []

    for expr in expressions:
        expr.scale(TEX_SCALE)
        annotations_for_expr = []
        if annotation_map:
            for annotation, target in annotation_map:
                # Check if the target is a submobject of expr (or is expr itself)
                if target in expr.submobjects or target is expr:
                    annotation.next_to(target, DOWN, buff=annotation_buff)
                    annotations_for_expr.append(annotation)
        if annotations_for_expr:
            expr_block = VGroup(expr, *annotations_for_expr).arrange(DOWN, buff=annotation_buff, aligned_edge=LEFT)
        else:
            expr_block = expr
        expr_blocks.append(expr_block)

    expr_group = VGroup(*expr_blocks).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    return VGroup(label_text, expr_group).arrange(DOWN, buff=0.2, aligned_edge=LEFT)