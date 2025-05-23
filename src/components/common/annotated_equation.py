from manim import *

class AnnotatedEquation(VGroup):
    """A specialized VGroup for equations with annotations.
    
    This class handles the proper animation sequencing of equations
    and their annotations, whether used with ScrollManager or manually.
    """
    
    def __init__(self, equation, annotations, **kwargs):
        super().__init__(**kwargs)
        self.equation = equation
        self.annotations = VGroup(*annotations) if annotations else VGroup()
        self.add(equation)
        if len(self.annotations) > 0:
            self.add(self.annotations)
    
    def animate_in(self, scene, equation_anim=Write, annotation_anim=FadeIn, 
                   equation_runtime=None, annotation_runtime=None):
        """Animate this equation with its annotations.
        
        Args:
            scene: The Manim scene to animate in
            equation_anim: Animation type for the equation (default: Write)
            annotation_anim: Animation type for annotations (default: FadeIn)
            equation_runtime: Runtime for equation animation
            annotation_runtime: Runtime for annotation animation
        """
        # Animate equation
        eq_kwargs = {"run_time": equation_runtime} if equation_runtime else {}
        scene.play(equation_anim(self.equation, **eq_kwargs))
        
        # Animate annotations if they exist
        if len(self.annotations) > 0:
            ann_kwargs = {"run_time": annotation_runtime} if annotation_runtime else {}
            scene.play(annotation_anim(self.annotations, **ann_kwargs))
    
    def get_equation_only(self):
        """Get just the equation without annotations."""
        return self.equation
    
    def get_annotations_only(self):
        """Get just the annotations without the equation."""
        return self.annotations