"""Tutorial on triangle properties and classifications."""

from manim import *
from src.components.common.base_scene import MathTutorialScene
from src.components.common.smart_tex import *
from src.components.styles.constants import *

class TriangleClassification(MathTutorialScene):
    def construct(self):
        # This is just a sample to demonstrate branching
        title = Tex("Types of Triangles").scale(TEXT_SCALE)
        self.add(title) 