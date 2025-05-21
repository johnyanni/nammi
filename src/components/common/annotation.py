from manim import Mobject, ManimColor
import functools


class Annotation:
    """
    A class to lazily hold the annotation data for later use and flexiblty

    Examples:
    ```
        exp = MathTex("x^2 + 10x + 25 = 12"),
        a1 = Annotation(
               "-12",
                # it will not be evaluated until we call `a`
                # lazy evaluation is usefual if we are creating steps
                # and we cannot get a hold of the exp to be annotated yet
                self.find_element_lazy("25"),
                self.find_element_lazy("12"),
                color=RED,
            )
        annotation = a1(self, exp) # evaluate annotation

        a2 = Annotation(
                added_term = "-12",
                # you could pass the str patterns directly if you don't need the
                # flexiblty of `find_element` function
                left_term = "25",
                right_term = "12",
            )

        a3 = Annotation(
                added_term = "-12",
                # or you even could mix between lazy evaluation and str
                left_term = self.find_element_lazy("25"),
                right_term = "12",
                color=RED,
            )
    ```
    """

    def __init__(
        self,
        added_term: str,
        left_term: str | functools.partial | Mobject,
        right_term: str | functools.partial | Mobject,
        color: ManimColor | str | None = None,
        h_spacing: float = 0,
    ):
        self.added_term = added_term
        self.left_term = left_term
        self.right_term = right_term
        self.color = color
        self.h_spacing = h_spacing

    def __call__(self, scene, exp=None):
        left_term = self.left_term
        # if it is find_element_lazy, evaluate it first
        if type(self.left_term) is functools.partial:
            assert exp is not None
            left_term = self.left_term(exp=exp)
        elif type(self.left_term) is str:
            assert exp is not None
            left_term = scene.find_element(pattern=self.left_term, exp=exp)

        right_term = self.right_term
        # if it is find_element_lazy, evaluate it first
        if type(self.right_term) is functools.partial:
            assert exp is not None
            right_term = self.right_term(exp=exp)
        elif type(self.right_term) is str:
            assert exp is not None
            right_term = scene.find_element(pattern=self.right_term, exp=exp)

        if left_term is None:
            print("Cannot find left term target")
            return None

        if right_term is None:
            print("Cannot find right term target")
            return None

        return scene.add_annotations(
            term_added=self.added_term,
            left_term=left_term,
            right_term=right_term,
            color=self.color,
            h_spacing=self.h_spacing,
        )
