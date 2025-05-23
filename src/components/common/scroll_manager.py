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
        self.replacements = {}  # Add this line
        # Store callouts with their target scroll index
        self.callouts_by_scroll_index = (
            {}
        )  # Key: scroll index, Value: list of callout managers
        self.scroll_count = 0  # Track number of scrolls

    def prepare_next(self, scene=None, target_slice=slice(None), same_item=False, 
                    animation_type=Write, steps=1, run_time=None, animation_kwargs=None):
        """Enhanced prepare_next with automatic annotation detection."""
        
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if same_item:
            self.current_position -= self.last_steps
                
        if self.current_position >= len(self.equations):
            print("No more equations to display.")
            return self
        
        # DEBUG: Add this line
        print(f"prepare_next called for position {self.current_position}")
        
        # NEW: Auto-detect annotated equations
        current_item = self.equations[self.current_position]
        print(f"Current item type: {type(current_item)}")
        if (isinstance(current_item, VGroup) and 
            hasattr(current_item, '_is_annotated_equation') and 
            current_item._is_annotated_equation):
            
            print(f"Auto-detected annotated equation at position {self.current_position}")
            
            if scene is not None:
                # Show equation first, then annotations
                equation = current_item.equation
                if run_time is not None:
                    scene.play(animation_type(equation[target_slice], **animation_kwargs), run_time=run_time)
                else:
                    scene.play(animation_type(equation[target_slice], **animation_kwargs))
                
                # Then show annotations
                if hasattr(current_item, 'annotations') and len(current_item.annotations) > 0:
                    print(f"Showing {len(current_item.annotations)} annotations")
                    if run_time is not None:
                        scene.play(FadeIn(current_item.annotations), run_time=run_time)
                    else:
                        scene.play(FadeIn(current_item.annotations))
            
            self.last_steps = steps
            self.current_position += steps
            return self
        
        # EXISTING: Regular handling for non-annotated elements
        if scene is not None:
            animations = [
                animation_type(
                    self.equations[self.current_position + i][0][target_slice], **animation_kwargs
                )
                for i in range(steps)
            ]

            if run_time is not None:
                scene.play(*animations, run_time=run_time)
            else:
                scene.play(*animations)

        self.last_steps = steps
        self.current_position += steps
        return self

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

        
    def replace_in_place(self, scene, index, new_content, animation_type=ReplacementTransform, run_time=None, animation_kwargs=None, move_new_content=True):
        """Replaces an equation at its current position
        
        Args:
            scene: The manim scene to animate on
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            animation_type: Animation to use for replacement (default: Transform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            move_new_content: Whether to move the new content the position of the old one (optional)
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range ({self.last_in_view}-{self.current_position-1})")
        
        if self.equations[index] is None:
            raise ValueError(f"No equation exists at index {index} (it may have been part of a group replacement)")
            
        original = self.equations[index]
        self.replacements[index] = original
        
        # Position the new content where the original is
        if move_new_content:
            new_content.move_to(original.get_center())
        
        # Perform the replacement animation
        scene.play(animation_type(original, new_content, **animation_kwargs), **run_time)
        
        # Update the equations list
        self.equations[index] = new_content
        self.remove(original)
        #self.add(new_content)
    
    def highlight_and_replace(self, scene, index, new_content, highlight_color=YELLOW, 
                              highlight_time=0.5, replace_time=1, final_color=WHITE):
        """Highlights an equation before replacing it
        
        Args:
            scene: The manim scene to animate on
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            highlight_color: Color to use for highlighting (default: YELLOW)
            highlight_time: Duration of highlight animation in seconds (default: 0.5)
            replace_time: Duration of replacement animation in seconds (default: 1)
            final_color: Final color of the new content (default: WHITE)
        """
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range ({self.last_in_view}-{self.current_position-1})")
        
        if self.equations[index] is None:
            raise ValueError(f"No equation exists at index {index} (it may have been part of a group replacement)")
            
        original = self.equations[index]
        self.replacements[index] = original
        
        # Highlight the original equation
        scene.play(original.animate.set_color(highlight_color), run_time=highlight_time)
        
        # Position the new content
        new_content.move_to(original.get_center())
        new_content.set_color(highlight_color)
        
        # Replace with the new content
        scene.play(ReplacementTransform(original, new_content), run_time=replace_time)
        
        # Fade to final color
        scene.play(new_content.animate.set_color(final_color), run_time=highlight_time)
        
        # Update the equations list
        self.equations[index] = new_content
        self.remove(original)
        # self.add(new_content)
    
    def restore_original(self, scene, index, animation_type=Transform, run_time=None, animation_kwargs=None):
        """Restores an equation to its original state before replacement
        
        Args:
            scene: The manim scene to animate on
            index: Index of the equation to restore
            animation_type: Animation to use for restoration (default: Transform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if index not in self.replacements:
            raise KeyError(f"No original equation stored for index {index}")
        
        current = self.equations[index]
        
        if current is None:
            raise ValueError(f"No equation exists at index {index} (it may have been part of a group replacement)")
            
        original = self.replacements[index].copy()
        
        # Position the original where the current one is
        original.move_to(current.get_center())
        
        # Perform the restoration animation
        scene.play(animation_type(current, original, **animation_kwargs), **run_time)
        
        # Update the equations list
        self.equations[index] = original
        self.remove(current)
        self.add(original)
        
        # Remove from replacements dictionary
        del self.replacements[index]
    
    def cascade_update(self, scene, start_index, new_contents, cascade_delay=0.2, run_time=1, animation_type=ReplacementTransform):
        """Updates multiple equations in a cascading sequence
        
        Args:
            scene: The manim scene to animate on
            start_index: Index of the first equation to replace
            new_contents: List of new equations/content to replace with
            cascade_delay: Delay between successive animations in seconds (default: 0.2)
            run_time: Duration of each replacement animation in seconds (default: 1)
            animation_type: Animation to use for replacement (default: Transform)
        """
        if start_index < self.last_in_view or start_index + len(new_contents) > self.current_position:
            raise IndexError(f"Replacement range {start_index}-{start_index + len(new_contents) - 1} is outside visible range")
        
        for i, new_content in enumerate(new_contents):
            index = start_index + i
            
            if self.equations[index] is None:
                continue  
                
            original = self.equations[index]
            self.replacements[index] = original
            
            # Position the new content
            new_content.move_to(original.get_center())
            
            # Perform the replacement animation with delay
            scene.play(animation_type(original, new_content), run_time=run_time)
            
            # Update the equations list
            self.equations[index] = new_content
            self.remove(original)
            
            # Add delay between animations if not the last one
            if i < len(new_contents) - 1:
                scene.wait(cascade_delay)
                
                
    def fade_in_from_target(self, scene, target, steps=1, run_time=None, animation_kwargs=None):
        """Fades in the next equation(s) from a target position
        
        Args:
            scene: The manim scene to animate on
            target: Target position or mobject to fade from
            steps: Number of equations to fade in (default: 1)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            
        Returns:
            self: For method chaining
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Make sure we have enough equations left
        if self.current_position + steps > len(self.equations):
            steps = len(self.equations) - self.current_position
            if steps <= 0:
                print("No more equations to display.")
                return self
        
        # Get the equations to fade in
        equations_to_fade = [self.equations[self.current_position + i] for i in range(steps)]
        
        # Get target position
        target_position = target.get_center() 
        
        # Fade in each equation from the target position
        animations = [
            FadeIn(eq, target_position=target_position, **animation_kwargs)
            for eq in equations_to_fade
        ]
        
        scene.play(*animations, **run_time)
        
        # Update position counter
        self.current_position += steps
        
        return self
    

    