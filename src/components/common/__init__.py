"""Common components for math tutorials.

Note: smart_tex and constants are designed to be used with wildcard imports:
from src.components.common.smart_tex import *
from src.components.styles.constants import *

For other components, use explicit imports.
"""

# Import everything we want to expose
from .base_scene import MathTutorialScene
from .smart_tex import *  # Import all smart_tex utilities
from .scroll_manager import ScrollManager
from .quick_tip import QuickTip
from .annotation import Annotation

# Define what gets exported with 'from src.components.common import *'
__all__ = [
    'MathTutorialScene',
    'SmartColorize',
    'SmartColorizeStatic', 
    'search_shape_in_text',
    'search_shapes_in_text',  # Add other smart_tex utilities
    'group_shapes_in_text',
    'all_sizes_symbol',
    'ScrollManager',
    'QuickTip',
    'Annotation'
]
