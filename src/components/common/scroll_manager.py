"""Scroll manager for handling scrolling animations in tutorials."""

from manim import *

class ScrollManager(VGroup):
    def __init__(self, equations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equations = equations
        self.start_position = self.equations[0].copy()
        self.current_position = 0
        self.last_in_view = 0
        self.last_steps = 0
        # Store callouts with their target scroll index
        self.callouts_by_scroll_index = (
            {}
        )  # Key: scroll index, Value: list of callout managers
        self.scroll_count = 0  # Track number of scrolls

    def prepare_next(
        self,
        scene=None,
        target_slice=slice(None),
        same_item=False,
        animation_type=Write,
        steps=1,
        run_time=None,
        animation_kwargs=None,
    ):
        """Writes the next equation(s) without scrolling.

        Args:
            scene: The manim scene to animate on (optional)
            steps: Number of equations to write (default: 1)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for the animation (optional)
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if same_item:
            self.current_position -= self.last_steps
            
        if scene is not None:
            animations = [
                animation_type(
                    self.equations[self.current_position + i][0][target_slice], **animation_kwargs
                )
                for i in range(steps)
            ]

            scene.play(*animations, **run_time)

        self.last_steps = steps
        self.current_position += steps

    def attach_callout_at_scroll(self, scroll_index, callout_manager):
        """Attach a callout manager to fade out at a specific scroll index."""
        if scroll_index not in self.callouts_by_scroll_index:
            self.callouts_by_scroll_index[scroll_index] = []
        self.callouts_by_scroll_index[scroll_index].append(callout_manager)
        return self

    def scroll_down(self, scene, steps=1, run_time=None):
        """Scrolls equations up and reveals new equations"""
        run_time = {} if run_time is None else {"run_time": run_time}
        hidden_equations = self.equations[self.last_in_view : self.last_in_view + steps]
        viewed_equations = self.equations[
            self.last_in_view + steps : self.current_position
        ]

        callout_animations = []

        # Increment scroll count
        previous_scroll_count = self.scroll_count
        self.scroll_count += steps

        # Directly hide callouts associated with scroll_index + 1
        for scroll_index, managers in self.callouts_by_scroll_index.items():
            if (
                scroll_index < self.scroll_count
                and scroll_index >= previous_scroll_count
            ):
                for callout_manager in managers:
                    if callout_manager.is_visible:
                        callout_animations.append(
                            FadeOut(callout_manager.get_callout(), shift=UP * 2)
                        )
                        callout_manager.is_visible = False
                        print(
                            f"Reached scroll index {self.scroll_count}, fading out callout."
                        )

        VGroup(
            viewed_equations.copy(), self.equations[self.current_position :]
        ).align_to(self.start_position, UP)

        scene.play(
            viewed_equations.animate.align_to(self.start_position, UP),
            FadeOut(hidden_equations, shift=UP * 2),
            *callout_animations,
            **run_time,
        )
        self.remove(hidden_equations)
        self.last_in_view += steps

    def _is_target_in_container(self, target, container):
        """Recursively check if target is inside a container"""
        if target == container:
            return True

        if hasattr(container, "submobjects") and container.submobjects:
            for submob in container.submobjects:
                if self._is_target_in_container(target, submob):
                    return True

        return False

    def _is_container_parent_of(self, potential_parent, child):
        """Check if potential_parent is a parent/ancestor of child"""
        # Get the parent of the child
        if hasattr(child, "parent_mobject") and child.parent_mobject is not None:
            parent = child.parent_mobject

            # Check if this parent is our target
            if parent == potential_parent:
                return True

            # If not, check the parent's parent recursively
            return self._is_container_parent_of(potential_parent, parent)

        return False

    def get_top_level_parent(self, target):
        """Find the top-level parent equation (direct child of self.equations) containing the target."""
        for equation in self.equations:
            if self._is_target_in_container(target, equation):
                return equation
        return None  # If not found
