"""Scroll manager for handling scrolling animations in tutorials."""

from manim import *
from src.components.common.base_scene import LABEL_SCALE, MATH_SCALE, ANNOTATION_SCALE
from src.components.common.base_scene import MathTutorialScene

class ScrollManager(VGroup):
    def __init__(self, equations=None, scene=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equations = equations if equations else VGroup()
        self.scene = scene  # Store scene reference
        self.start_position = self.equations[0].copy() if equations else None
        self.current_position = 0
        self.last_in_view = 0
        self.last_steps = 0
        self.replacements = {}
        # Store callouts with their target scroll index
        self.callouts_by_scroll_index = {}  # Key: scroll index, Value: list of callout managers
        self.scroll_count = 0  # Track number of scrolls

        # Step management
        self.steps = {} # Dictionary mapping labels to step indices
        self.arranged_equations = VGroup() # VGroup to arrange equations
        
        # Initialize math scene
        self.math_scene = MathTutorialScene()  

    # Helper methods for common operations
    def _get_scene(self, scene=None):
        """Get scene, using provided scene or stored scene."""
        scene = scene or self.scene
        if scene is None:
            raise ValueError("No scene available. Either pass scene to constructor, use set_scene(), or provide scene parameter.")
        return scene

    def _get_animation_params(self, run_time=None, animation_kwargs=None):
        """Get standardized animation parameters."""
        return (
            {} if run_time is None else {"run_time": run_time},
            {} if animation_kwargs is None else animation_kwargs
        )

    def _validate_position(self, steps=1, error_msg=None):
        """Validate and adjust current position and steps.
        Returns adjusted steps count."""
        if self.current_position >= len(self.equations):
            if error_msg:
                print(error_msg)
            return 0
            
        if self.current_position + steps > len(self.equations):
            steps = len(self.equations) - self.current_position
            if steps <= 0:
                print("No more equations to display.")
                return 0
        return steps

    def _validate_index(self, index, context=""):
        """Validate if an index is within visible range."""
        if index < self.last_in_view or index >= self.current_position:
            raise IndexError(f"{context}: Index {index} is out of the currently visible range ({self.last_in_view}-{self.current_position-1})")
        if self.equations[index] is None:
            raise ValueError(f"{context}: No equation exists at index {index} (it may have been part of a group replacement)")
        return True

    def set_scene(self, scene):
        """Set the scene reference if not provided during initialization."""
        self.scene = scene
        return self

    def update_start_position(self):
        if not self.start_position:
            self.start_position = self.equations[0].copy()

    def create_tex(self, text, label=None, scale=LABEL_SCALE, **kwargs):
        """Create a Tex object with the given text and scale.
        
        Example usage:
            create_tex("Hello", color=RED, font_size=48)
            create_tex("World", tex_template=my_template)
        """
        text = Tex(text, **kwargs).scale(scale)

        return text, label

    def create_math_tex(self, tex, label=None, scale=MATH_SCALE, **kwargs):
        """Create a MathTex object
        
        Example usage:
            create_math_tex("x^2 + y^2", color=BLUE)
            create_math_tex("\\frac{a}{b}", tex_to_color_map={"a": RED, "b": GREEN})
        """
        expression = MathTex(tex, **kwargs).scale(scale)

        return expression, label

    
    def create_annotated_equation(self, equation_text, annotation_text, from_term, to_term,
                                  color=RED, scale=MATH_SCALE, annotation_scale=ANNOTATION_SCALE, 
                                  nth_from=0, nth_to=0, h_spacing=0, label=None):
        """Create an equation with annotations as a single VGroup."""
        equation = MathTex(equation_text).scale(scale)
        
        from_element = self.math_scene.find_element(from_term, equation, nth=nth_from)
        to_element = self.math_scene.find_element(to_term, equation, nth=nth_to)

        if from_element is None or to_element is None:
            print(f"[WARN] Couldn't find: from='{from_term}' or to='{to_term}'")
            return equation

        # Use the existing add_annotations with scale parameter
        annotations = self.math_scene.add_annotations(
            annotation_text, from_element, to_element, 
            color=color, h_spacing=h_spacing, scale=annotation_scale
        )

        result = VGroup(equation, *annotations)
        result._has_annotation = True
        
        return result, label
    
    def set_position_target(self, target, direction=DOWN, buff=0.4, align_edge=LEFT):
        """Set the target for automatic positioning."""
        self.position_target = target
        self.position_config = {
            'direction': direction,
            'buff': buff,
            'align_edge': align_edge
        }
    
    def arrange_equations(self):
        self.arranged_equations.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
    
        # Only reposition to target if we haven't scrolled
        if self.position_target and self.scroll_count == 0:
            self.arranged_equations.next_to(
                self.position_target, 
                self.position_config.get('direction', DOWN),
                buff=self.position_config.get('buff', 0.4)
            )
            if 'align_edge' in self.position_config:
                self.arranged_equations.align_to(
                    self.position_target,
                    self.position_config['align_edge']
                )

    def add_to_arragement(self, group):
        self.arranged_equations.add(group)
        self.arrange_equations()
        
    def get_arranged_equations(self):
        return self.arranged_equations

        
    def create_step(self, step, label=None, arrange=True):
        # Check if the label already exists
        if label and label in self.steps:
            raise ValueError(f"Step label '{label}' already exists.")

        # Current step index
        step_index = len(self.equations)

        # Use index as default label if none provided
        label = step_index if not label else label

        self.steps[label] = step_index

        # Add the step to equations
        self.equations.add(step)

        # Add the equation to the arrangement if required
        if arrange:
            self.arranged_equations.add(step)
            self.arrange_equations()
        
        return step

    def create_steps(self, steps, labels=None, arrange=True):
        """Create multiple steps with optional labels."""
        if labels is None:
            labels = [None] * len(steps)

        steps_group = VGroup()
        for step, label in zip(steps, labels):
            steps_group.add(self.create_step(step, label, arrange=False))
            
        if arrange:
            self.arranged_equations.add(steps_group)
            self.arrange_equations()
            
        return steps_group

    def construct_step(self, *args, arrange_dir=DOWN, aligned_edge=LEFT, buff=0.2, add_to_scroll=True, arrange=True):
        """
        Accepts any number of two-value tuples as arguments - (step, label)
        """
        steps = VGroup()
        for step, label in args:
            if add_to_scroll:
                steps.add(self.create_step(step, label, arrange=False))
            else:
                steps.add(step)

        steps.arrange(arrange_dir, aligned_edge=aligned_edge, buff=buff)

        # If the steps are not a part of the flow yet, but they a part of the arrangement
        if arrange:
            self.arranged_equations.add(steps)
            self.arrange_equations()
            
        return steps
    
    def get_by_label(self, label):
        """Get an element by its label."""
        if label not in self.steps:
            raise KeyError(f"No element with label '{label}' found")
        
        index = self.steps[label]
        return self.equations[index]
            
    def _resolve_target(self, target):
        if target in self.steps:
            return self.steps[target]
        elif isinstance(target, int):
            return target
        else:
            raise ValueError(f"Target '{target}' is not a valid step label or index")
        
    def prepare_next(self, target=None, scene=None, target_slice=slice(None), same_item=False, 
                     animation_type=Write, steps=1, run_time=None, lag_ratio=1, animation_kwargs=None):
        """Prepare next elements with optional scene override."""

        # Update start_position after arranging the steps
        self.update_start_position()
        
        # Debug flag - set to True to enable debug output
        DEBUG = False
        
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
        if same_item:
            self.current_position -= self.last_steps

        # Handle target-based preperation
        if target:
            target_index = self._resolve_target(target)
            
            if target_index >= self.current_position:
                steps = target_index - self.current_position + 1
            else:
                raise ValueError(f"Target index {target_index} is behind current position {self.current_position}")

            
        steps = self._validate_position(steps, "No more equations to display.")
        if steps == 0:
            return self
        
        animations = []
        
        for i in range(steps):
            if self.current_position + i >= len(self.equations):
                break
            
            item = self.equations[self.current_position + i]

            # Handle annotated equations
            if isinstance(item, VGroup) and hasattr(item, '_has_annotation'):
                if DEBUG:
                    print(f"\n[DEBUG] Item {self.current_position}: ANNOTATED EQUATION")
                    print(f"  Type: {type(item).__name__}")
                    print(f"  Has annotation: {hasattr(item, '_has_annotation')}")
                
                animations.append(animation_type(item[0], **animation_kwargs))
                if len(item) > 1:
                    animations.append(FadeIn(VGroup(*item[1:])))
                continue
                    
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

            elif isinstance(item, VGroup) and len(item) > 0 and isinstance(item[0], (MathTex, Tex, Text)):
                to_animate = item
                method = "VGROUP (text/math)"
                details = "Animating entire VGroup of text/math elements"
                
            else:
                to_animate = item[0][target_slice]
                method = "MATHTEX/TEX/OTHER"
                details = f"Using item[0][{target_slice}]"
                
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
            if run_time:
                scene.play(AnimationGroup(*animations, lag_ratio=lag_ratio), **run_time)
            else:
                scene.play(AnimationGroup(*animations, lag_ratio=lag_ratio))

        self.last_steps = steps
        self.current_position += steps
        return self

    def scroll_down(self, target=None, scene=None, steps=1, run_time=None):
        """Scrolls equations up and reveals new equations"""
        scene = self._get_scene(scene)
        run_time, _ = self._get_animation_params(run_time)

        # Handle target-based scrolling
        if target:
            target_index = self._resolve_target(target)
            steps = target_index - self.last_in_view
            
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
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
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
        self.fade_out_in_view(
            steps=self.current_position - self.last_in_view,
            scene=scene,
            animation_type=animation_type,
            run_time=run_time,
            animation_kwargs=animation_kwargs,
        )
        
    def attach_callout_at_scroll(self, scroll_index, callout_manager):
        """
        Attach a callout manager to fade out at a specific scroll index.
        No scene parameter needed as this just stores data.
        """
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
        """
        Replaces an equation at its current position
        
        Args:
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Animation to use for replacement (default: ReplacementTransform)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)Add commentMore actions
            move_new_content: Whether to move the new content to the position of the old one (optional)
        """
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
        self._validate_index(index, "replace_in_place")
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
        """
        Highlights an equation before replacing it
        
        Args:
            index: Index of the equation to replace
            new_content: New equation/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            highlight_color: Color to use for highlighting (default: YELLOW)
            highlight_time: Duration of highlight animation in seconds (default: 0.5)Add commentMore actions
            replace_time: Duration of replacement animation in seconds (default: 1)
            final_color: Final color of the new content (default: WHITE)
        """
        scene = self._get_scene(scene)
        self._validate_index(index, "highlight_and_replace")
            
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
        """
        Restores an equation to its original state before replacement
        
        Args:
            index: Index of the equation to restore
            scene: The manim scene to animate on (if None, uses stored scene)
            animation_type: Animation to use for restoration (default: Transform)Add commentMore actions
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
        """
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
        if index not in self.replacements:
            raise KeyError(f"No original equation stored for index {index}")
        
        self._validate_index(index, "restore_original")
        current = self.equations[index]
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
        """
        Updates multiple equations in a cascading sequence
        
        Args:
            start_index: Index of the first equation to replace
            new_contents: List of new equations/content to replace with
            scene: The manim scene to animate on (if None, uses stored scene)
            cascade_delay: Delay between successive animations in seconds (default: 0.2)
            run_time: Duration of each replacement animation in seconds (default: 1)
            animation_type: Animation to use for replacement (default: ReplacementTransform)
        """
        scene = self._get_scene(scene)
        
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
        """
        Fades in from a source position.
        
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
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
        # Check if we're using the old single-argument style
        if target is None and hasattr(source, 'get_center'):
            # Old style: source is position, target is next in queue
            source_position = source.get_center()
            steps = self._validate_position(1, "No more equations to display.")
            if steps == 0:
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
        """
        Transform a copy of source to a target element.
        
        Args:
            source: Source mobject to copy and transform from
            target: Target mobject to transform to (if None, uses next element in queue)
            scene: The manim scene to animate on (if None, uses stored scene)
            run_time: Animation duration in seconds (optional)
            animation_kwargs: Additional keyword arguments for animation (optional)
            
        Returns:
            self: For method chaining
        """
        scene = self._get_scene(scene)
        run_time, animation_kwargs = self._get_animation_params(run_time, animation_kwargs)
        
        # If no target specified, use the next element in queue
        if target is None:
            steps = self._validate_position(1, "No more equations to display.")
            if steps == 0:
                return self
            target = self.equations[self.current_position]
            self.current_position += 1
        else:
            # If target is specified, check if it's in our equations
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