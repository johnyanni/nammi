"""Tutorial on classifying triangles by their sides and angles."""

from manim import *
from src.components.common.base_scene import *
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip
from src.components.styles.constants import *

class TrianglesClassification(MathTutorialScene):
    """A tutorial that teaches how to classify triangles based on their sides and angles."""
    def construct(self):
        # This is just a sample to demonstrate branching
        title = Tex("Types of Triangles").scale(TEXT_SCALE)
        self.add(title) 