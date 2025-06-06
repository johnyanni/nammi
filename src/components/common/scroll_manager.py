"""Scroll manager for handling scrolling animations in tutorials."""

from manim import *

class ScrollManager(VGroup):
    def __init__(self, equations, scene=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equations = equations
        self.scene = scene  # Store scene reference
        self.start_position = self.equations[0].copy()
        self.current_position = 0
        self.last_in_view = 0
        self.last_steps = 0
        self.replacements = {}
        # Store callouts with their target scroll index
        self.callouts_by_scroll_index = {}  # Key: scroll index, Value: list of callout managers
        self.scroll_count = 0  # Track number of scrolls

    def set_scene(self, scene):
        """Set the scene reference if not provided during initialization."""
        self.scene = scene
        return self

    
    def prepare_next(self, scene=None, target_slice=slice(None), same_item=False, 
                    animation_type=Write, steps=1, run_time=None, animation_kwargs=None):
        """Prepare next elements with optional scene override."""
        
        # Debug flag - set to True to enable debug output
        DEBUG = False
        
        # Use provided scene or stored scene
        if scene is None:
            scene = self.scene
            
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        if same_item:
            self.current_position -= self.last_steps
                
        if self.current_position >= len(self.equations):
            print("No more equations to display.")
            return self
        
        # Handle annotated equations
        current_item = self.equations[self.current_position]
        if isinstance(current_item, VGroup) and hasattr(current_item, '_has_annotation'):
            if DEBUG:
                print(f"\n[DEBUG] Item {self.current_position}: ANNOTATED EQUATION")
                print(f"  Type: {type(current_item).__name__}")
                print(f"  Has annotation: {hasattr(current_item, '_has_annotation')}")
                
            if scene is not None:
                scene.play(animation_type(current_item[0], **animation_kwargs))
                if len(current_item) > 1:
                    scene.play(FadeIn(VGroup(*current_item[1:])))
            self.last_steps = steps
            self.current_position += steps
            return self
        
        # Handle regular items
        if scene is not None:
            animations = []
            
            for i in range(steps):
                if self.current_position + i >= len(self.equations):
                    break
                    
                item = self.equations[self.current_position + i]
                
                if DEBUG:
                    print(f"\n[DEBUG] Item {self.current_position + i}:")
                    print(f"  Type: {type(item).__name__}")
                    if hasattr(item, 'tex_string'):
                        tex_str = item.tex_string[:50] + "..." if len(item.tex_string) > 50 else item.tex_string
                        print(f"  TeX: {tex_str}")
                    if isinstance(item, VGroup):
                        print(f"  VGroup length: {len(item)}")
                        if len(item) > 0:
                            print(f"  First element type: {type(item[0]).__name__}")
                
                # Determine which method is used
                if isinstance(item, (list, tuple)):
                    to_animate = VGroup(*item[target_slice])
                    method = "LIST/TUPLE"
                    details = f"Slicing list/tuple with {target_slice}"
                    
                elif isinstance(item, VGroup) and len(item) > 0 and not isinstance(item[0], (MathTex, Tex, Text)):
                    to_animate = item[target_slice]
                    method = "VGROUP (non-text)"
                    details = f"Slicing VGroup with {target_slice}"
                    
                else:
                    to_animate = item[0][target_slice]
                    method = "MATHTEX/TEX/OTHER"
                    details = f"Using item[0][{target_slice}]"
                    
                    # Additional debug for this case
                    if DEBUG:
                        print(f"  Submobjects: {len(item.submobjects) if hasattr(item, 'submobjects') else 'N/A'}")
                        if hasattr(item, 'submobjects') and len(item.submobjects) > 0:
                            print(f"  item[0] length: {len(item[0]) if hasattr(item[0], '__len__') else 'N/A'}")
                
                if DEBUG:
                    print(f"  METHOD: {method}")
                    print(f"  Details: {details}")
                    print(f"  Result type: {type(to_animate).__name__}")
                    if hasattr(to_animate, '__len__'):
                        print(f"  Result length: {len(to_animate)}")
                
                animations.append(animation_type(to_animate, **animation_kwargs))
            
            if animations:
                if run_time is not None:
                    scene.play(*animations, run_time=run_time)
                else:
                    scene.play(*animations)

        self.last_steps = steps
        self.current_position += steps
        return self

    
    def scroll_down(self, scene=None, steps=1, run_time=None):
        """Scrolls equations up and reveals new equations"""
        
        # Use provided scene or stored scene
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available.")
            
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
        
        
        
    def fade_out_in_view(
        self, steps=1, scene=None, animation_type=FadeOut, run_time=None, animation_kwargs=None
    ):
        """
        Fades out number of `steps` from the elements currently in view
        
        Args:
            steps: Number of elements to fade out (default: 1)
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Type of fade animation (default: FadeOut)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        steps = min(steps, self.current_position - self.last_in_view)
        animations = [
            animation_type(self.equations[self.last_in_view + i], **animation_kwargs)
            for i in range(steps)
        ]
        scene.play(*animations, **run_time)
        self.last_in_view += steps

    def fade_out_all_in_view(
        self, scene=None, animation_type=FadeOut, run_time=None, animation_kwargs=None
    ):
        """
        Fades out all elements currently in view
        
        Args:
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Type of fade animation (default: FadeOut)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
        """
        # Note: We pass scene through to fade_out_in_view, which will handle the stored scene logic
        self.fade_out_in_view(
            steps=self.current_position - self.last_in_view,
            scene=scene,
            animation_type=animation_type,
            run_time=run_time,
            animation_kwargs=animation_kwargs,
        )
        
    def attach_callout_at_scroll(self, scroll_index, callout_manager):
        """Attach a callout manager to fade out at a specific scroll index.
        No scene parameter needed as this just stores data."""
        if scroll_index not in self.callouts_by_scroll_index:
            self.callouts_by_scroll_index[scroll_index] = []
        self.callouts_by_scroll_index[scroll_index].append(callout_manager)
        return self
    
    

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

        
    def replace_in_place(self, index, new_content, scene=None, animation_type=ReplacementTransform, 
                        run_time=None, animation_kwargs=None, move_new_content=True):
        """Replaces an equation at its current position
        
        Args:
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Animation to use for replacement (default: ReplacementTransform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            move_new_content: Whether to move the new content to the position of the old one (optional)
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
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

    def highlight_and_replace(self, index, new_content, scene=None, highlight_color=YELLOW, 
                            highlight_time=0.5, replace_time=1, final_color=WHITE):
        """Highlights an equation before replacing it
        
        Args:
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            highlight_color: Color to use for highlighting (default: YELLOW)
            highlight_time: Duration of highlight animation in seconds (default: 0.5)
            replace_time: Duration of replacement animation in seconds (default: 1)
            final_color: Final color of the new content (default: WHITE)
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
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

    def restore_original(self, index, scene=None, animation_type=Transform, run_time=None, animation_kwargs=None):
        """Restores an equation to its original state before replacement
        
        Args:
            index: Index of the equation to restore
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Animation to use for restoration (default: Transform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
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

    def cascade_update(self, start_index, new_contents, scene=None, cascade_delay=0.2, run_time=1, animation_type=ReplacementTransform):
        """Updates multiple equations in a cascading sequence
        
        Args:
            start_index: Index of the first equation to replace
            new_contents: List of new equations/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            cascade_delay: Delay between successive animations in seconds (default: 0.2)
            run_time: Duration of each replacement animation in seconds (default: 1)
            animation_type: Animation to use for replacement (default: ReplacementTransform)
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
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

    def fade_in_from_target(self, source, target=None, scene=None, run_time=None, animation_kwargs=None):
        """Fades in from a source position.
        
        Can be called two ways:
        1. fade_in_from_target(source_position) - fades in next element from source
        2. fade_in_from_target(source_position, target_element) - fades in specific target from source
        
        Args:
            source: Source mobject to get the position from
            target: Target mobject to fade in (if None, uses next element in queue)
            scene: The manim scene to animate on (if None, uses stored scene)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            
        Returns:
            self: For method chaining
        """
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Check if we're using the old single-argument style
        if target is None and hasattr(source, 'get_center'):
            # Old style: source is position, target is next in queue
            source_position = source.get_center()
            if self.current_position >= len(self.equations):
                print("No more equations to display.")
                return self
            target = self.equations[self.current_position]
            self.current_position += 1
        else:
            # New style: source is position, target is specified
            source_position = source.get_center()
            if target is None:
                raise ValueError("Target must be specified when using new API style")
                
            # Update position tracking if target is in our equations list
            target_index = None
            for i, eq in enumerate(self.equations):
                if eq is target:  # Use 'is' for object identity
                    target_index = i
                    break
            
            # Only update position if target is ahead of current position
            if target_index is not None and target_index >= self.current_position:
                self.current_position = target_index + 1
        
        # Perform the animation
        scene.play(
            FadeIn(target, target_position=source_position, **animation_kwargs),
            **run_time
        )
        
        return self


    
    
    
    
    
    def transform_from_copy(self, source, target=None, scene=None, run_time=None, animation_kwargs=None):
        """Transform a copy of source to a target element.
        
        Args:
            source: Source mobject to copy and transform from
            target: Target mobject to transform to (if None, uses next element in queue)
            scene: The manim scene to animate on (if None, uses stored scene)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            
        Returns:
            self: For method chaining
        """
        run_time = {} if run_time is None else {"run_time": run_time}
        animation_kwargs = {} if animation_kwargs is None else animation_kwargs
        
        # Use stored scene if not provided
        if scene is None:
            scene = self.scene
            
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        
        # If no target specified, use the next element in queue
        if target is None:
            if self.current_position >= len(self.equations):
                print("No more equations to display.")
                return self
            target = self.equations[self.current_position]
            self.current_position += 1
        else:
            # If target is specified, check if it's in our equations
            # VGroup doesn't have index(), so we need to search manually
            target_index = None
            for i, eq in enumerate(self.equations):
                if eq is target:  # Use 'is' for object identity
                    target_index = i
                    break
            
            # Only update position if target is ahead of current position
            if target_index is not None and target_index >= self.current_position:
                self.current_position = target_index + 1
        
        # Perform TransformFromCopy
        scene.play(
            TransformFromCopy(source, target, **animation_kwargs),
            **run_time
        )
        
        return self