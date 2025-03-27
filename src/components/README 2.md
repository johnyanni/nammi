# NAMMI Components

This directory contains the core components used across all NAMMI (New Age Math Made Interactive) tutorials. The components are organized into two main categories: common components and styling components.

## Common Components (`common/`)

### Base Scene (`base_scene.py`)
The foundation for all tutorial scenes. Provides common functionality for:
- Voiceover management
- Scene transitions
- Common animation patterns
- Base scene setup and configuration

### Scroll Manager (`scroll_manager.py`)
Manages text scrolling and visibility in tutorial scenes:
- Handles text positioning and scrolling
- Manages text visibility and timing
- Provides smooth scrolling animations
- Controls text layout and organization

### Quick Tip (`quick_tip.py`)
Creates and manages tooltips for additional information:
- Displays helpful tips during tutorials
- Manages tip positioning and timing
- Provides customizable tip styles
- Handles tip animations and transitions

### Slope Overlay (`slope_overlay.py`)
Specialized component for slope visualization:
- Creates visual representations of slope
- Shows slope direction and magnitude
- Provides interactive slope demonstrations
- Manages slope-related animations

### Full Screen Overlay (`full_screen_overlay.py`)
Handles full-screen transitions and overlays:
- Creates smooth scene transitions
- Manages full-screen content display
- Provides overlay animations
- Controls overlay timing and effects

### Smart Tex (`smart_tex.py`)
Enhanced mathematical text rendering:
- Handles complex mathematical expressions
- Provides consistent text styling
- Manages mathematical symbols
- Supports custom text formatting

## Styling Components (`styles/`)

### Constants (`constants.py`)
Central location for all shared constants:
- Animation timing constants
- Text scaling factors
- Font sizes
- Common color definitions
- Other shared values

### Theme (`theme.py`)
Manages visual theming and styling:
- Defines color schemes
- Controls visual consistency
- Manages style inheritance
- Provides theme customization

## Usage Examples

### Creating a New Tutorial Scene
```python
from src.components.common.base_scene import MathTutorialScene
from src.components.common.scroll_manager import ScrollManager
from src.components.common.quick_tip import QuickTip

class MyTutorial(MathTutorialScene):
    def construct(self):
        # Create scroll manager for text
        scroll_mgr = ScrollManager(solution_steps)
        
        # Add a quick tip
        tip = QuickTip("This is a helpful tip!")
        
        # Use common styling
        text = MathTex(r"y = mx + b").scale(MATH_SCALE)
```

### Using Slope Visualization
```python
from src.components.common.slope_overlay import SlopeOverlay

# Create slope overlay
slope_screen = SlopeOverlay()

# Show slope visualization
self.play(FadeIn(slope_screen))
```

### Applying Common Styling
```python
from src.components.styles.constants import *

# Use common constants
text = MathTex(r"y = mx + b").scale(MATH_SCALE)
title = Tex("Title").scale(TEXT_SCALE)
```

## Best Practices

1. **Component Usage**
   - Always use the provided components instead of creating custom implementations
   - Follow the established patterns for component integration
   - Use the appropriate styling constants

2. **Text Management**
   - Use ScrollManager for all text-based content
   - Follow the established text scaling conventions
   - Use SmartTex for mathematical expressions

3. **Visual Elements**
   - Use QuickTip for additional information
   - Implement SlopeOverlay for slope demonstrations
   - Use FullScreenOverlay for transitions

4. **Styling**
   - Use constants from the styles directory
   - Follow the established theme system
   - Maintain consistent visual appearance

## Contributing

When adding new components:
1. Place them in the appropriate directory
2. Update this README with new component information
3. Add proper documentation and type hints
4. Include usage examples
5. Follow the established coding standards

## Dependencies

- Manim
- Python 3.8+
- Azure Text-to-Speech (for voiceovers) 