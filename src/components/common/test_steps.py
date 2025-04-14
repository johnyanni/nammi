from manim import *
from .smart_tex import *

class TestSteps(VMobject):
    def __init__(
            self,
            step_1,
            step_2,
            slope,
            y_intercept,
            title = None,
            title_color=WHITE,
            title_scale=0.70,
            step_1_label="Step 1: Plug in the values of x and y",
            step_2_label="Step 2: Simplify the right side",
            label_color=GRAY,
            label_scale=0.60,
            buff=0.3,
            title_buff=0.3,
            **kwargs):
        super().__init__(**kwargs)
    
        # Store the values
        self._step_1 = step_1
        self._step_2 = step_2
        self._slope = slope
        self._y_intercept = y_intercept
        
        # Create labels
        self.step_1_label = Tex(step_1_label, color=label_color).scale(label_scale)
        self.step_2_label = Tex(step_2_label, color=label_color).scale(label_scale)
        
        # Arrange steps with labels
        step_1_labeled = VGroup(self.step_1_label, step_1).arrange(DOWN, aligned_edge=LEFT)
        step_2_labeled = VGroup(self.step_2_label, step_2).arrange(DOWN, aligned_edge=LEFT)
        
        # Group the steps
        steps_group = VGroup(step_1_labeled, step_2_labeled).arrange(DOWN, aligned_edge=LEFT, buff=buff)

        # Add title if specific
        if title:
            self._title = Tex(title, color=title_color).scale(title_scale)
            group = VGroup(self._title, steps_group).arrange(DOWN, aligned_edge=LEFT, buff=title_buff)
            steps_group.shift(RIGHT/3)
        else:
            group = steps_group
            self._title = None
        
        self.add(group)
        
        self._initialize_components()
    
    def _initialize_components(self):
        """Extract and store all components during initialization for easier access later."""
        # Find the indices of key components
        equal_index = search_shape_in_text(self._step_1, MathTex("="))[0]
        slope_index = search_shape_in_text(self._step_1, MathTex(fr"{self._slope}"))[0]
        y_intercept_index = search_shape_in_text(self._step_1, MathTex(fr"{self._y_intercept}"))[-1]
        times_index = search_shape_in_text(self._step_1, MathTex(r"\times"))
        not_equal_index = search_shape_in_text(self._step_2, MathTex(r"\ne"))
        
        self._components = {
            "step_1_y": self._step_1[0][:equal_index.start],
            "step_1_equal_sign": self._step_1[0][equal_index],
            "slope": self._step_1[0][slope_index],
            "y_intercept": self._step_1[0][y_intercept_index],
            "y_intercept_sign": self._step_1[0][y_intercept_index.start - 1],
            "step_1_right_side": self._step_1[0][equal_index.stop:],
            "step_2_y": self._step_2[0][:equal_index.start],
        }
        
        # Handle the x component based on whether there's a times symbol
        if times_index:
            times_index = times_index[0]
            self._components["times"] = self._step_1[0][times_index]
            self._components["x"] = self._step_1[0][times_index.stop:y_intercept_index.start - 1]
        else:
            self._components["x"] = self._step_1[0][slope_index.stop:y_intercept_index.start - 1]

        if not_equal_index:
            not_equal_index = not_equal_index[0]
            self._components["step_2_equal_sign"] = self._step_2[0][not_equal_index.start:not_equal_index.stop+1]
            self._components["step_2_right_side"] = self._step_2[0][not_equal_index.stop+1:]
        else: 
            self._components["step_2_equal_sign"] = self._step_2[0][equal_index]
            self._components["step_2_right_side"] = self._step_2[0][equal_index.stop:]
            
    
    def get_component(self, name):
        return self._components.get(name)

    @property
    def step_1(self):
        return self._step_1

    @property
    def step_2(self):
        return self._step_2

    @property
    def title(self):
        return self._title