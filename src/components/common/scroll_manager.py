"""Scroll manager for handling scrolling animations in tutorials."""

from manim import *

class ScrollManager(VGroup):
    def __init__(self, equations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equations = equations
        self.start_position=self.equations[0].copy()
        self.current_position = 0
        self.last_in_view = 0
    
    def prepare_next(self, scene=None, animation_type=Write, steps=1, run_time=None, animation_kwargs=None):
        """Writes the next equation(s) without scrolling.
        
        Args:
            scene: The manim scene to animate on (optional)
            steps: Number of equations to write (default: 1)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for the animation (optional)
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs

        if scene is not None:    
            animations = [
                animation_type(self.equations[self.current_position + i], **animation_kwargs)
                for i in range(steps)
            ]
            
            scene.play(*animations, **run_time)
        
        self.current_position += steps
        
    
    def scroll_down(self, scene, steps=1, run_time=None):
        """Scrolls equations up and reveals new equations"""
        run_time = {} if run_time is None else {"run_time": run_time}
        hidden_equations = self.equations[self.last_in_view:self.last_in_view+steps]
        viewed_equations = self.equations[self.last_in_view+steps:self.current_position]
        
        VGroup(viewed_equations.copy(), self.equations[self.current_position:]).align_to(self.start_position, UP)
        scene.play(viewed_equations.animate.align_to(self.start_position, UP), FadeOut(hidden_equations, shift=UP*2), **run_time)
        self.remove(hidden_equations)
        self.last_in_view += steps
