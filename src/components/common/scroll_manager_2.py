"""Enhanced scroll manager for handling scrolling animations in tutorials.

This improved version of ScrollManager includes additional features:
- Better step group management with batch preparation
- Enhanced replacement options
- Superior cascade animations
- More flexible animation timing control
- Proper handling of callouts and scroll events
- Smart animation speed adjustment based on content
"""

from manim import *

class ScrollManager:
    def __init__(self, elements, *args, **kwargs):
        """Initialize the ScrollManager with elements to manage.
        
        Args:
            elements: A VGroup of elements that need to be managed
            *args: Additional positional arguments
            **kwargs: Additional keyword arguments
        """
        # Core state tracking
        self.elements = elements
        self.start_position = self.elements[0].get_center() if len(elements) > 0 else ORIGIN
        self.current_position = 0
        self.last_in_view = 0
        self.last_steps = 0
        self.replacements = {}
        self.scroll_count = 0
        
        # Advanced tracking for smart scrolling and animations
        self.default_run_time = 1.0
        self.callouts_by_scroll_index = {}
        self.animations_in_progress = False
        self.highlighted_elements = set()
        self.auto_adjust_timing = kwargs.get('auto_adjust_timing', True)
        self.custom_animation_speeds = {}
        
        # Initialize with animations turned off
        self.animations_enabled = True
        
        # Configure additional options
        self.smooth_scroll = kwargs.get('smooth_scroll', True)
        self.scroll_direction = kwargs.get('scroll_direction', UP)
        self.visible_elements = []
    
    def disable_animations(self):
        """Temporarily disable animations for batch operations."""
        self.animations_enabled = False
        return self
    
    def enable_animations(self):
        """Re-enable animations after batch operations."""
        self.animations_enabled = True
        return self
    
    def prepare_next(
        self,
        scene=None,
        target_slice=slice(None),
        same_item=False,
        animation_type=Write,
        steps=1,
        run_time=None,
        animation_kwargs=None,
        fade_strategy="one_by_one", # "one_by_one", "together", "staggered"
        stagger_ratio=0.3
    ):
        """Writes the next element(s) without scrolling.

        Args:
            scene: The manim scene to animate on (optional)
            target_slice: Optional slice to target specific parts of the element
            same_item: Whether to keep working with the same item (don't increment)
            animation_type: The type of animation to use (default: Write)
            steps: Number of elements to write (default: 1)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for the animation
            fade_strategy: Strategy for fading in multiple elements: 
                          "one_by_one", "together", or "staggered"
            stagger_ratio: Ratio of stagger between elements (0-1) for "staggered" strategy
        
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            self.current_position += steps
            return self
        
        # Handle run_time intelligently
        if run_time is None:
            if self.auto_adjust_timing:
                run_time = self._get_adaptive_run_time(steps)
            else:
                run_time = self.default_run_time
                
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if same_item:
            self.current_position -= self.last_steps
            
        if scene is not None:
            animations = []
            
            # Different strategies for handling multiple elements
            if fade_strategy == "one_by_one":
                # Animate one element at a time
                for i in range(steps):
                    if self.current_position + i < len(self.elements):
                        animations.append(
                            animation_type(
                                self.elements[self.current_position + i][0][target_slice], 
                                **animation_kwargs
                            )
                        )
                
                if animations:
                    scene.play(*animations, **run_time_dict)
                    self.visible_elements.extend([self.elements[self.current_position + i] for i in range(steps) 
                                              if self.current_position + i < len(self.elements)])
            
            elif fade_strategy == "together":
                # Animate all elements together
                elements_to_animate = VGroup(*[
                    self.elements[self.current_position + i][0][target_slice]
                    for i in range(steps)
                    if self.current_position + i < len(self.elements)
                ])
                
                if len(elements_to_animate) > 0:
                    scene.play(animation_type(elements_to_animate, **animation_kwargs), **run_time_dict)
                    self.visible_elements.extend([self.elements[self.current_position + i] for i in range(steps) 
                                               if self.current_position + i < len(self.elements)])
            
            elif fade_strategy == "staggered":
                # Staggered animation with lag ratio
                elements_to_animate = [
                    self.elements[self.current_position + i][0][target_slice]
                    for i in range(steps)
                    if self.current_position + i < len(self.elements)
                ]
                
                if elements_to_animate:
                    scene.play(
                        AnimationGroup(
                            *[animation_type(elem, **animation_kwargs) for elem in elements_to_animate],
                            lag_ratio=stagger_ratio
                        ), 
                        **run_time_dict
                    )
                    self.visible_elements.extend([self.elements[self.current_position + i] for i in range(steps) 
                                               if self.current_position + i < len(self.elements)])

        self.last_steps = steps
        self.current_position += steps
        return self

    def _get_adaptive_run_time(self, steps):
        """Calculate an appropriate runtime based on content size and complexity."""
        base_time = self.default_run_time
        
        # For multiple elements, add more time
        if steps > 1:
            base_time *= min(1.5, 1 + (steps * 0.1))
            
        # Check if any elements have custom speeds
        for i in range(steps):
            idx = self.current_position + i
            if idx in self.custom_animation_speeds and idx < len(self.elements):
                return self.custom_animation_speeds[idx]
                
        return base_time

    def set_animation_speed(self, element_index, run_time):
        """Set a custom animation speed for a specific element.
        
        Args:
            element_index: Index of the element to customize
            run_time: The animation duration to use
            
        Returns:
            self: For method chaining
        """
        self.custom_animation_speeds[element_index] = run_time
        return self

    def scroll_down(self, scene, steps=1, run_time=None, scroll_animation=None):
        """Scrolls elements up and reveals new elements.
        
        Args:
            scene: The manim scene to animate on
            steps: Number of steps to scroll (default: 1)
            run_time: Animation duration in seconds (optional)
            scroll_animation: Custom scroll animation type (optional)
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            self.last_in_view += steps
            self.scroll_count += steps
            return self
        
        # Handle run_time intelligently
        if run_time is None:
            if self.auto_adjust_timing:
                # Scrolling large content takes longer
                run_time = 0.5 + (min(steps, 5) * 0.2)
            else:
                run_time = 1.0
                
        run_time_dict = {"run_time": run_time}
        
        # Get elements that will be hidden and those that remain visible
        if self.last_in_view < len(self.elements):
            hidden_elements = self.elements[self.last_in_view : self.last_in_view + steps]
        else:
            hidden_elements = VGroup()
            
        if self.last_in_view + steps < len(self.elements) and self.current_position > self.last_in_view + steps:
            viewed_elements = self.elements[
                self.last_in_view + steps : self.current_position
            ]
        else:
            viewed_elements = VGroup()

        # Prepare callout animations for elements going out of view
        callout_animations = []
        previous_scroll_count = self.scroll_count
        self.scroll_count += steps

        # Handle any callouts associated with this scroll index
        for scroll_index, managers in self.callouts_by_scroll_index.items():
            if scroll_index < self.scroll_count and scroll_index >= previous_scroll_count:
                for callout_manager in managers:
                    if callout_manager.is_visible:
                        callout_animations.append(
                            FadeOut(callout_manager.get_callout(), shift=self.scroll_direction * 2)
                        )
                        callout_manager.is_visible = False

        # Create the main scroll animation
        if len(viewed_elements) > 0:
            # Copy to maintain positions
            elements_copy = VGroup(
                viewed_elements.copy(), 
                self.elements[self.current_position:].copy() if self.current_position < len(self.elements) else VGroup()
            )
            elements_copy.align_to(self.start_position, -self.scroll_direction)

            # Main scroll animation
            main_animations = [
                viewed_elements.animate.align_to(self.start_position, -self.scroll_direction),
                FadeOut(hidden_elements, shift=self.scroll_direction * 2),
                *callout_animations
            ]

            # Use custom scroll animation if provided
            if scroll_animation:
                scene.play(scroll_animation(*main_animations), **run_time_dict)
            else:
                scene.play(*main_animations, **run_time_dict)

            # Update tracking and remove hidden elements
            self.remove_from_visible(hidden_elements)
        else:
            # If no visible elements to scroll, just fade out the hidden ones
            if len(hidden_elements) > 0:
                scene.play(
                    FadeOut(hidden_elements, shift=self.scroll_direction * 2),
                    *callout_animations,
                    **run_time_dict
                )
                self.remove_from_visible(hidden_elements)

        self.last_in_view += steps
        return self
    
    def remove_from_visible(self, elements):
        """Remove elements from the visible elements list.
        
        Args:
            elements: Elements to remove from the visible list
        """
        elements_set = set(elements)
        self.visible_elements = [e for e in self.visible_elements if e not in elements_set]

    def _is_target_in_container(self, target, container):
        """Recursively check if target is inside a container.
        
        Args:
            target: Target element to find
            container: Container to search within
            
        Returns:
            bool: True if target is inside container, False otherwise
        """
        if target == container:
            return True

        if hasattr(container, "submobjects") and container.submobjects:
            for submob in container.submobjects:
                if self._is_target_in_container(target, submob):
                    return True

        return False

    def get_top_level_parent(self, target):
        """Find the top-level parent element containing the target.
        
        Args:
            target: Target element to find parent for
            
        Returns:
            Mobject: The parent element or None if not found
        """
        for element in self.elements:
            if self._is_target_in_container(target, element):
                return element
        return None

    def replace_in_place(self, scene, index, new_content, animation_type=ReplacementTransform, 
                         run_time=None, animation_kwargs=None, maintain_position=True,
                         maintain_z_index=True):
        """Replaces an element at its current position.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to replace
            new_content: New element/content to replace with
            animation_type: Animation to use for replacement (default: ReplacementTransform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation
            maintain_position: Whether to maintain the exact position of the original
            maintain_z_index: Whether to maintain the z-index of the original
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            self.replacements[index] = self.elements[index]
            self.elements[index] = new_content
            return self
            
        # Validate index
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range ({self.last_in_view}-{self.current_position-1})")
        
        if self.elements[index] is None:
            raise ValueError(f"No element exists at index {index} (it may have been removed)")
        
        # Set animation parameters
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        original = self.elements[index]
        self.replacements[index] = original
        
        # Position the new content exactly where the original is
        if maintain_position:
            new_content.move_to(original.get_center())
            if hasattr(original, "get_alignment") and hasattr(new_content, "align_to"):
                try:
                    alignment = original.get_alignment()
                    new_content.align_to(original, alignment)
                except:
                    pass
                
        # Copy z-index if requested
        if maintain_z_index and hasattr(original, "z_index") and hasattr(new_content, "set_z_index"):
            new_content.set_z_index(original.z_index)
        
        # Perform the replacement animation
        scene.play(animation_type(original, new_content, **animation_kwargs), **run_time_dict)
        
        # Update the elements list
        self.elements[index] = new_content
        self.update_visible_element(index, original, new_content)
        
        return self
    
    def update_visible_element(self, index, old_element, new_element):
        """Update an element in the visible elements list.
        
        Args:
            index: Index of the element to update
            old_element: Original element to replace
            new_element: New element to use as replacement
        """
        for i, elem in enumerate(self.visible_elements):
            if elem == old_element:
                self.visible_elements[i] = new_element
                break

    def highlight_and_replace(self, scene, index, new_content, 
                              highlight_color=YELLOW, highlight_time=0.5, 
                              replace_time=1, final_color=WHITE,
                              animation_kwargs=None):
        """Highlights an element before replacing it.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to replace
            new_content: New element/content to replace with
            highlight_color: Color to use for highlighting
            highlight_time: Duration of highlight animation
            replace_time: Duration of replacement animation
            final_color: Final color of the new content
            animation_kwargs: Additional keyword arguments for animation
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            self.replacements[index] = self.elements[index]
            self.elements[index] = new_content
            return self
            
        # Validate index
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range ({self.last_in_view}-{self.current_position-1})")
        
        if self.elements[index] is None:
            raise ValueError(f"No element exists at index {index}")
            
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        original = self.elements[index]
        self.replacements[index] = original
        
        # Highlight the original element
        scene.play(original.animate.set_color(highlight_color), run_time=highlight_time)
        
        # Position the new content and highlight it
        new_content.move_to(original.get_center())
        new_content.set_color(highlight_color)
        
        # Replace with the new content
        scene.play(ReplacementTransform(original, new_content, **animation_kwargs), run_time=replace_time)
        
        # Fade to final color
        scene.play(new_content.animate.set_color(final_color), run_time=highlight_time)
        
        # Update the elements list
        self.elements[index] = new_content
        self.update_visible_element(index, original, new_content)
        
        # Track this as a highlighted element
        self.highlighted_elements.add(index)
        
        return self

    def restore_original(self, scene, index, animation_type=Transform, 
                         run_time=None, animation_kwargs=None):
        """Restores an element to its original state before replacement.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to restore
            animation_type: Animation to use for restoration
            run_time: Animation duration in seconds
            animation_kwargs: Additional keyword arguments for animation
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            if index in self.replacements:
                self.elements[index] = self.replacements[index]
                del self.replacements[index]
            return self
            
        # Validate replacements
        if index not in self.replacements:
            raise KeyError(f"No original element stored for index {index}")
        
        current = self.elements[index]
        if current is None:
            raise ValueError(f"No element exists at index {index}")
            
        # Set animation parameters
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Get a copy of the original
        original = self.replacements[index].copy()
        
        # Position the original where the current one is
        original.move_to(current.get_center())
        
        # Perform the restoration animation
        scene.play(animation_type(current, original, **animation_kwargs), **run_time_dict)
        
        # Update the elements list
        self.elements[index] = original
        self.update_visible_element(index, current, original)
        
        # Remove from highlighted elements if it was highlighted
        if index in self.highlighted_elements:
            self.highlighted_elements.remove(index)
        
        # Remove from replacements dictionary
        del self.replacements[index]
        
        return self

    def cascade_update(self, scene, start_index, new_contents, cascade_delay=0.2, 
                       run_time=1, animation_type=ReplacementTransform,
                       cascade_direction="down", animation_kwargs=None):
        """Updates multiple elements in a cascading sequence.
        
        Args:
            scene: The manim scene to animate on
            start_index: Index of the first element to replace
            new_contents: List of new elements/content to replace with
            cascade_delay: Delay between successive animations
            run_time: Duration of each replacement animation
            animation_type: Animation to use for replacement
            cascade_direction: Direction of cascade ("down", "up", "left", "right")
            animation_kwargs: Additional keyword arguments for animation
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            for i, new_content in enumerate(new_contents):
                index = start_index + i
                if index < len(self.elements) and self.elements[index] is not None:
                    self.replacements[index] = self.elements[index]
                    self.elements[index] = new_content
            return self
                
        # Validate range
        end_index = start_index + len(new_contents) - 1
        if start_index < self.last_in_view or end_index >= self.current_position:
            raise IndexError(f"Replacement range {start_index}-{end_index} is outside visible range")
            
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Get direction vector
        direction_vectors = {
            "down": DOWN,
            "up": UP,
            "left": LEFT,
            "right": RIGHT
        }
        direction = direction_vectors.get(cascade_direction.lower(), DOWN)
        
        # Animate the replacements in sequence
        for i, new_content in enumerate(new_contents):
            index = start_index + i
            
            if self.elements[index] is None:
                continue
                
            original = self.elements[index]
            self.replacements[index] = original
            
            # Position the new content
            new_content.move_to(original.get_center())
            
            # Add a slight shift in the cascade direction for visual effect
            shift_amount = direction * (0.1 * i)
            new_content.shift(shift_amount)
            
            # Perform the replacement animation
            scene.play(
                animation_type(original, new_content, **animation_kwargs),
                run_time=run_time
            )
            
            # Animate the slight bounce back
            scene.play(
                new_content.animate.shift(-shift_amount),
                run_time=min(0.2, run_time/3)
            )
            
            # Update the elements list
            self.elements[index] = new_content
            self.update_visible_element(index, original, new_content)
            
            # Add delay between animations if not the last one
            if i < len(new_contents) - 1:
                scene.wait(cascade_delay)
                
        return self

    def fade_in_from_target(self, scene, target, steps=1, run_time=None, 
                           animation_kwargs=None, scale_factor=1.0,
                           fade_direction=None):
        """Fades in the next element(s) from a target position with enhanced effects.
        
        Args:
            scene: The manim scene to animate on
            target: Target position or mobject to fade from
            steps: Number of elements to fade in
            run_time: Animation duration in seconds
            animation_kwargs: Additional keyword arguments for animation
            scale_factor: Scale factor for the fade animation (1.0 = normal size)
            fade_direction: Optional direction for the fade animation
            
        Returns:
            self: For method chaining
        """
        if not self.animations_enabled:
            self.current_position += min(steps, len(self.elements) - self.current_position)
            return self
            
        # Set animation parameters
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Make sure we have enough elements left
        if self.current_position + steps > len(self.elements):
            steps = len(self.elements) - self.current_position
            if steps <= 0:
                print("No more elements to display.")
                return self
        
        # Get the elements to fade in
        elements_to_fade = [self.elements[self.current_position + i] for i in range(steps)]
        
        # Get target position or center of target mobject
        if isinstance(target, (int, float)) or len(target) == 3:  # If target is a position
            target_position = target
        else:  # If target is a mobject
            target_position = target.get_center()
            
        # Prepare animations with enhanced effects
        animations = []
        for element in elements_to_fade:
            # Start slightly scaled if scale_factor != 1.0
            if scale_factor != 1.0:
                element.scale(1/scale_factor)
                
            # Apply fade animation with direction if specified
            if fade_direction is not None:
                animations.append(
                    FadeIn(element, target_position=target_position, shift=fade_direction, 
                          scale=scale_factor, **animation_kwargs)
                )
            else:
                animations.append(
                    FadeIn(element, target_position=target_position, 
                          scale=scale_factor, **animation_kwargs)
                )
            
            # Add to visible elements
            self.visible_elements.append(element)
        
        # Play the animations
        if animations:
            scene.play(*animations, **run_time_dict)
            
            # If we scaled, we need to restore the original scale
            if scale_factor != 1.0:
                restore_animations = [elem.animate.scale(scale_factor) for elem in elements_to_fade]
                scene.play(*restore_animations, run_time=min(0.3, run_time or 0.5))
        
        # Update position counter
        self.current_position += steps
        
        return self
        
    def replace_with_callout(self, scene, index, new_content, callout_text, 
                            callout_position=UP, callout_color=YELLOW, 
                            run_time=1, animation_type=ReplacementTransform):
        """Replaces an element and adds a callout pointing to it.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to replace
            new_content: New element/content to replace with
            callout_text: Text to display in the callout
            callout_position: Direction of the callout relative to the element
            callout_color: Color of the callout
            run_time: Animation duration in seconds
            animation_type: Animation to use for replacement
            
        Returns:
            CalloutManager: Manager for the created callout
        """
        # First replace the element
        self.replace_in_place(scene, index, new_content, 
                             animation_type=animation_type, run_time=run_time)
        
        # Create the callout text
        callout_tex = Tex(callout_text, color=callout_color).scale(0.8)
        
        # Create background for better visibility
        background = SurroundingRectangle(
            callout_tex,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_width=0,
            buff=0.2
        )
        
        # Group text and background
        callout_group = VGroup(background, callout_tex)
        
        # Position next to the element
        callout_group.next_to(new_content, callout_position, buff=0.2)
        
        # Create arrow pointing from callout to element
        arrow = Arrow(
            callout_group.get_edge_center(-callout_position),
            new_content.get_edge_center(callout_position),
            buff=0.1,
            color=callout_color
        )
        
        # Group everything together
        full_callout = VGroup(callout_group, arrow)
        
        # Animate the callout appearance
        scene.play(FadeIn(full_callout))
        
        # Create a callout manager for easy reference
        class CalloutManager:
            def __init__(self, scene, callout, element, scroll_index):
                self.scene = scene
                self.callout = callout
                self.element = element
                self.is_visible = True
                self.scroll_index = scroll_index
                
            def hide(self, run_time=0.5):
                if self.is_visible:
                    self.scene.play(FadeOut(self.callout), run_time=run_time)
                    self.is_visible = False
                return self
                
            def show(self, run_time=0.5):
                if not self.is_visible:
                    self.scene.play(FadeIn(self.callout), run_time=run_time)
                    self.is_visible = True
                return self
                
            def get_callout(self):
                return self.callout
        
        # Create the manager
        manager = CalloutManager(scene, full_callout, new_content, self.scroll_count)
        
        # Register this callout to disappear at the next scroll
        self.attach_callout_at_scroll(self.scroll_count + 1, manager)
        
        return manager
    
    def attach_callout_at_scroll(self, scroll_index, callout_manager):
        """Attach a callout manager to fade out at a specific scroll index.
        
        Args:
            scroll_index: Scroll index at which to fade out the callout
            callout_manager: CalloutManager object to manage
            
        Returns:
            self: For method chaining
        """
        if scroll_index not in self.callouts_by_scroll_index:
            self.callouts_by_scroll_index[scroll_index] = []
        self.callouts_by_scroll_index[scroll_index].append(callout_manager)
        return self
    
    def batch_operations(self, scene, operations):
        """Perform multiple operations in a batch without intermediate animations.
        
        Args:
            scene: The manim scene to animate on
            operations: List of (method_name, args, kwargs) tuples to execute
            
        Returns:
            self: For method chaining
        """
        # Disable animations temporarily
        self.disable_animations()
        
        # Execute all operations
        for method_name, args, kwargs in operations:
            method = getattr(self, method_name)
            method(scene, *args, **kwargs)
            
        # Re-enable animations
        self.enable_animations()
        
        return self
    
    def highlight_element(self, scene, index, color=YELLOW, scale_factor=1.2, 
                         run_time=1, restore=True, restore_time=None):
        """Highlights an element with color change and optional scaling.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to highlight
            color: Color to use for highlighting
            scale_factor: Scale factor for the highlight animation
            run_time: Animation duration in seconds
            restore: Whether to restore the element after highlighting
            restore_time: Duration of restoration animation (defaults to run_time/2)
            
        Returns:
            self: For method chaining
        """
        # Validate index
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range")
        
        if self.elements[index] is None:
            raise ValueError(f"No element exists at index {index}")
            
        element = self.elements[index]
        
        # Store original properties
        original_color = element.get_color()
        original_scale = element.get_scale()
        
        # Highlight animation
        if scale_factor != 1.0:
            scene.play(
                element.animate.set_color(color).scale(scale_factor),
                run_time=run_time
            )
        else:
            scene.play(
                element.animate.set_color(color),
                run_time=run_time
            )
        
        # Only restore if requested
        if restore:
            restore_time = restore_time or (run_time / 2)
            if scale_factor != 1.0:
                scene.play(
                    element.animate.set_color(original_color).scale(1/scale_factor),
                    run_time=restore_time
                )
            else:
                scene.play(
                    element.animate.set_color(original_color),
                    run_time=restore_time
                )
                
        # Track as highlighted if not restored
        if not restore:
            self.highlighted_elements.add(index)
            
        return self
    
    def scroll_to(self, scene, index, run_time=None):
        """Scrolls to make a specific element visible at the top of the view.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to scroll to
            run_time: Animation duration in seconds
            
        Returns:
            self: For method chaining
        """
        # Validate index
        if index < 0 or index >= len(self.elements):
            raise IndexError(f"Index {index} is out of range")
            
        # If element is already visible, do nothing
        if index >= self.last_in_view and index < self.current_position:
            return self
            
        # Calculate how many steps to scroll
        if index < self.last_in_view:
            # Need to scroll up (not currently supported)
            raise NotImplementedError("Scrolling up is not currently supported")
        else:
            # Need to scroll down
            steps_to_scroll = index - self.last_in_view + 1
            self.scroll_down(scene, steps=steps_to_scroll, run_time=run_time)
            
        return self
    
    def fadeout_all(self, scene, run_time=1):
        """Fades out all currently visible elements.
        
        Args:
            scene: The manim scene to animate on
            run_time: Animation duration in seconds
            
        Returns:
            self: For method chaining
        """
        # Get all visible elements
        visible_elements = self.elements[self.last_in_view:self.current_position]
        
        # Fade them out
        if len(visible_elements) > 0:
            scene.play(FadeOut(visible_elements), run_time=run_time)
            
        # Update tracking
        self.last_in_view = self.current_position
        self.visible_elements = []
            
        return self
    
    def flash_element(self, scene, index, color=YELLOW, num_flashes=1, 
                     time_per_flash=0.25, restore=True):
        """Creates a flashing effect around an element.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to flash
            color: Color to use for flashing
            num_flashes: Number of flash iterations
            time_per_flash: Duration of each flash
            restore: Whether to restore the original color after flashing
            
        Returns:
            self: For method chaining
        """
        # Validate index
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range")
        
        if self.elements[index] is None:
            raise ValueError(f"No element exists at index {index}")
            
        element = self.elements[index]
        original_color = element.get_color()
        
        # Create flash animation
        for _ in range(num_flashes):
            scene.play(
                element.animate.set_color(color),
                run_time=time_per_flash/2
            )
            scene.play(
                element.animate.set_color(BLACK),
                run_time=time_per_flash/2
            )
            
        # Restore original color if requested
        if restore:
            scene.play(
                element.animate.set_color(original_color),
                run_time=time_per_flash
            )
        else:
            # Set to highlight color
            scene.play(
                element.animate.set_color(color),
                run_time=time_per_flash
            )
            # Track as highlighted
            self.highlighted_elements.add(index)
            
        return self
    
    def append_elements(self, new_elements):
        """Appends new elements to the managed elements list.
        
        Args:
            new_elements: New elements to append
            
        Returns:
            self: For method chaining
        """
        # Convert to VGroup if not already
        if not isinstance(new_elements, VGroup):
            new_elements = VGroup(*new_elements)
            
        # Add to elements list
        self.elements.add(*new_elements)
        
        return self
    
    def group_replace_in_place(self, scene, indices, new_contents, 
                              animation_type=ReplacementTransform, 
                              run_time=None):
        """Replaces multiple elements together in a single animation.
        
        Args:
            scene: The manim scene to animate on
            indices: List of indices of elements to replace
            new_contents: List of new elements/content to replace with
            animation_type: Animation to use for replacement
            run_time: Animation duration in seconds
            
        Returns:
            self: For method chaining
        """
        if len(indices) != len(new_contents):
            raise ValueError("Number of indices must match number of new contents")
            
        # Validate indices
        for index in indices:
            if index < self.last_in_view or index >= self.current_position:
                raise IndexError(f"Index {index} is out of the currently visible range")
            
            if self.elements[index] is None:
                raise ValueError(f"No element exists at index {index}")
                
        # Set animation parameters
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        
        # Prepare originals and new contents
        originals = []
        for index in indices:
            original = self.elements[index]
            self.replacements[index] = original
            originals.append(original)
            
        # Position new contents
        for i, index in enumerate(indices):
            new_contents[i].move_to(self.elements[index].get_center())
            
        # Perform the group replacement animation
        scene.play(
            *[animation_type(original, new_content) 
              for original, new_content in zip(originals, new_contents)],
            **run_time_dict
        )
        
        # Update the elements list
        for i, index in enumerate(indices):
            self.elements[index] = new_contents[i]
            self.update_visible_element(index, originals[i], new_contents[i])
            
        return self
    
    def get_visible_range(self):
        """Gets the currently visible range of indices.
        
        Returns:
            tuple: (first_visible_index, last_visible_index)
        """
        return (self.last_in_view, self.current_position - 1)
    
    def is_visible(self, index):
        """Checks if an element is currently visible.
        
        Args:
            index: Index of the element to check
            
        Returns:
            bool: True if the element is visible, False otherwise
        """
        return index >= self.last_in_view and index < self.current_position
        
    def reset_view(self, scene, fade_out=True, run_time=1):
        """Resets the view to the beginning.
        
        Args:
            scene: The manim scene to animate on
            fade_out: Whether to fade out elements before resetting
            run_time: Animation duration for fade out
            
        Returns:
            self: For method chaining
        """
        # Fade out visible elements if requested
        if fade_out:
            visible_elements = self.elements[self.last_in_view:self.current_position]
            if len(visible_elements) > 0:
                scene.play(FadeOut(visible_elements), run_time=run_time)
                
        # Reset tracking
        self.last_in_view = 0
        self.current_position = 0
        self.visible_elements = []
        
        # Clear any temporary state
        self.highlighted_elements = set()
        
        return self

    def get_element(self, index):
        """Gets the element at the specified index.
        
        Args:
            index: Index of the element to get
            
        Returns:
            Mobject: The element at the index, or None if not found
        """
        if 0 <= index < len(self.elements):
            return self.elements[index]
        return None
    
    def apply_to_element(self, scene, index, animation, run_time=None):
        """Applies a custom animation to an element.
        
        Args:
            scene: The manim scene to animate on
            index: Index of the element to animate
            animation: Animation function that takes an element and returns an Animation
            run_time: Animation duration in seconds
            
        Returns:
            self: For method chaining
        """
        # Validate index
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"Index {index} is out of the currently visible range")
        
        if self.elements[index] is None:
            raise ValueError(f"No element exists at index {index}")
            
        # Create and play the animation
        element = self.elements[index]
        animation_obj = animation(element)
        
        run_time_dict = {} if run_time is None else {"run_time": run_time}
        scene.play(animation_obj, **run_time_dict)
        
        return self