"""Math step layout system for creating structured mathematical solutions in Manim."""

from typing import List, Optional, Dict, Any
from manim import *


TEX_SCALE = 0.7
FOOTNOTE_SCALE = 0.55

class MathContentBlock:
    """A flexible content block for math tutorials that handles expressions, annotations, and layout."""
    
    def __init__(
        self,
        title=None,
        title_color=GREY,
        title_scale=0.6,
        alignment=LEFT,
        title_buff=0.2,
        expression_buff=0.2,
        annotation_buff=0.15,
        step_buff=0.5
    ):
        self.title = title
        self.title_color = title_color
        self.title_scale = title_scale
        self.alignment = alignment
        self.title_buff = title_buff
        self.expression_buff = expression_buff
        self.annotation_buff = annotation_buff
        self.step_buff = step_buff
        
        self.content_items = []
        self.rendered_group = None
    
    def add_expression(self, expression_tex, scale=TEX_SCALE, color=WHITE):
        """Add a math expression to the content block."""
        if isinstance(expression_tex, str):
            expression = MathTex(expression_tex).scale(scale)
            if color != WHITE:
                expression.set_color(color)
        else:
            expression = expression_tex  # Allow passing in a pre-built mobject
            
        self.content_items.append({
            "type": "expression",
            "content": expression,
            "annotations": []
        })
        return expression
    
    def add_annotation(self, 
                      annotation_text, 
                      left_element, 
                      right_element=None,
                      color=BLUE, 
                      h_spacing=0):
        """Add an annotation between elements of the last expression."""
        if not self.content_items or self.content_items[-1]["type"] != "expression":
            raise ValueError("Can only add annotations to expressions")
            
        # Create annotation
        annotation = MathTex(annotation_text).scale(FOOTNOTE_SCALE)
        if color != WHITE:
            annotation.set_color(color)
            
        # Store annotation with its references
        self.content_items[-1]["annotations"].append({
            "text": annotation,
            "left_ref": left_element,
            "right_ref": right_element,
            "color": color,
            "h_spacing": h_spacing
        })
        return annotation
    
    def render(self, scene=None):
        """Render the content block to a VGroup."""
        if not self.content_items:
            return VGroup()
            
        result = VGroup()
        
        # Add title if provided
        if self.title:
            title = Tex(self.title, color=self.title_color).scale(self.title_scale)
            result.add(title)
        
        # Process content items
        content_group = VGroup()
        
        for item in self.content_items:
            if item["type"] == "expression":
                expression = item["content"]
                
                # Create a group for this expression and its annotations
                expr_group = VGroup(expression)
                
                # Process annotations for this expression
                if item["annotations"]:
                    # Create and position annotations
                    for anno in item["annotations"]:
                        left_ref = anno["left_ref"]
                        right_ref = anno["right_ref"]
                        
                        if isinstance(left_ref, (tuple, list)):
                            left_ref = expression[0][left_ref[0]:left_ref[1]]
                        
                        if isinstance(right_ref, (tuple, list)):
                            right_ref = expression[0][right_ref[0]:right_ref[1]]
                            
                        if right_ref is None:
                            # Single reference annotation
                            anno_text = anno["text"]
                            anno_text.next_to(left_ref, DOWN, buff=self.annotation_buff)
                            if anno["h_spacing"] != 0:
                                anno_text.shift(RIGHT * anno["h_spacing"])
                        else:
                            # Two reference annotation
                            anno_texts = VGroup(
                                anno["text"].copy(),
                                anno["text"].copy()
                            )
                            anno_texts[0].next_to(left_ref, DOWN, buff=self.annotation_buff)
                            anno_texts[1].next_to(right_ref, DOWN, buff=self.annotation_buff)
                            
                            if anno["h_spacing"] != 0:
                                anno_texts[0].shift(LEFT * anno["h_spacing"])
                                anno_texts[1].shift(RIGHT * anno["h_spacing"])
                            
                            # Align vertically if needed
                            if anno_texts[0].get_y() < anno_texts[1].get_y():
                                anno_texts[1].align_to(anno_texts[0], DOWN)
                            else:
                                anno_texts[0].align_to(anno_texts[1], DOWN)
                                
                            expr_group.add(anno_texts)
                
                content_group.add(expr_group)
        
        # Arrange everything
        content_group.arrange(DOWN, aligned_edge=self.alignment, buff=self.expression_buff)
        
        if self.title:
            result.arrange(DOWN, aligned_edge=self.alignment, buff=self.title_buff)
        else:
            result = content_group
            
        self.rendered_group = result
        
        # If scene is provided, add to scene
        if scene:
            scene.add(result)
            
        return result
    
    def get_mobject(self):
        """Get the rendered mobject, rendering if necessary."""
        if self.rendered_group is None:
            self.render()
        return self.rendered_group


class MathTutorialLayout:
    """Manages the layout of multiple MathContentBlocks with consistent spacing."""
    
    def __init__(
        self,
        title=None,
        title_scale=0.7,
        title_color=WHITE,
        step_buff=0.5,
        left_edge=1.0,
        top_edge=0.5,
        alignment=LEFT
    ):
        self.title = title
        self.title_scale = title_scale
        self.title_color = title_color
        self.step_buff = step_buff
        self.left_edge = left_edge
        self.top_edge = top_edge
        self.alignment = alignment
        
        self.steps = []
        self.rendered_group = None
        
    def add_step(self, content_block):
        """Add a MathContentBlock as a step."""
        self.steps.append(content_block)
        return content_block
        
    def create_step(self, title=None, **kwargs):
        """Create and add a new step."""
        step = MathContentBlock(title=title, **kwargs)
        self.steps.append(step)
        return step
        
    def render(self, scene=None):
        """Render all steps to a VGroup."""
        result = VGroup()
        
        # Add title if provided
        if self.title:
            title = Tex(self.title, color=self.title_color).scale(self.title_scale)
            result.add(title)
        
        # Render each step
        step_groups = VGroup()
        for step in self.steps:
            step_groups.add(step.render())
        
        # Arrange steps
        step_groups.arrange(DOWN, aligned_edge=self.alignment, buff=self.step_buff)
        
        if self.title:
            result.arrange(DOWN, aligned_edge=self.alignment, buff=self.step_buff)
        else:
            result = step_groups
            
        # Position the result
        result.to_edge(UP, buff=self.top_edge).to_edge(LEFT, buff=self.left_edge)
        
        self.rendered_group = result
        
        # If scene is provided, add to scene
        if scene:
            scene.add(result)
            
        return result
    
    def get_mobject(self):
        """Get the rendered mobject, rendering if necessary."""
        if self.rendered_group is None:
            self.render()
        return self.rendered_group
    
class MathContentBlock:
    """A flexible content block for math tutorials that handles expressions, annotations, and layout."""
    
    def __init__(
        self,
        title=None,
        title_color=GREY,
        title_scale=0.6,
        alignment=LEFT,
        title_buff=0.2,
        expression_buff=0.2,
        annotation_buff=0.15,
        step_buff=0.5
    ):
        self.title = title
        self.title_color = title_color
        self.title_scale = title_scale
        self.alignment = alignment
        self.title_buff = title_buff
        self.expression_buff = expression_buff
        self.annotation_buff = annotation_buff
        self.step_buff = step_buff
        
        self.content_items = []
        self.rendered_group = None
    
    def add_expression(self, expression_tex, scale=TEX_SCALE, color=WHITE):
        """Add a math expression to the content block."""
        if isinstance(expression_tex, str):
            expression = MathTex(expression_tex).scale(scale)
            if color != WHITE:
                expression.set_color(color)
        else:
            expression = expression_tex  # Allow passing in a pre-built mobject
            
        self.content_items.append({
            "type": "expression",
            "content": expression,
            "annotations": []
        })
        return expression
    
    def add_annotation(self, 
                      annotation_text, 
                      left_element, 
                      right_element=None,
                      color=BLUE, 
                      h_spacing=0):
        """Add an annotation between elements of the last expression."""
        if not self.content_items or self.content_items[-1]["type"] != "expression":
            raise ValueError("Can only add annotations to expressions")
            
        # Create annotation
        annotation = MathTex(annotation_text).scale(FOOTNOTE_SCALE)
        if color != WHITE:
            annotation.set_color(color)
            
        # Store annotation with its references
        self.content_items[-1]["annotations"].append({
            "text": annotation,
            "left_ref": left_element,
            "right_ref": right_element,
            "color": color,
            "h_spacing": h_spacing
        })
        return annotation
    
    def render(self, scene=None):
        """Render the content block to a VGroup."""
        if not self.content_items:
            return VGroup()
            
        result = VGroup()
        
        # Add title if provided
        if self.title:
            title = Tex(self.title, color=self.title_color).scale(self.title_scale)
            result.add(title)
        
        # Process content items
        content_group = VGroup()
        
        for item in self.content_items:
            if item["type"] == "expression":
                expression = item["content"]
                
                # Create a group for this expression and its annotations
                expr_group = VGroup(expression)
                
                # Process annotations for this expression
                if item["annotations"]:
                    # Create and position annotations
                    for anno in item["annotations"]:
                        left_ref = anno["left_ref"]
                        right_ref = anno["right_ref"]
                        
                        if isinstance(left_ref, (tuple, list)):
                            left_ref = expression[0][left_ref[0]:left_ref[1]]
                        
                        if isinstance(right_ref, (tuple, list)):
                            right_ref = expression[0][right_ref[0]:right_ref[1]]
                            
                        if right_ref is None:
                            # Single reference annotation
                            anno_text = anno["text"]
                            anno_text.next_to(left_ref, DOWN, buff=self.annotation_buff)
                            if anno["h_spacing"] != 0:
                                anno_text.shift(RIGHT * anno["h_spacing"])
                        else:
                            # Two reference annotation
                            anno_texts = VGroup(
                                anno["text"].copy(),
                                anno["text"].copy()
                            )
                            anno_texts[0].next_to(left_ref, DOWN, buff=self.annotation_buff)
                            anno_texts[1].next_to(right_ref, DOWN, buff=self.annotation_buff)
                            
                            if anno["h_spacing"] != 0:
                                anno_texts[0].shift(LEFT * anno["h_spacing"])
                                anno_texts[1].shift(RIGHT * anno["h_spacing"])
                            
                            # Align vertically if needed
                            if anno_texts[0].get_y() < anno_texts[1].get_y():
                                anno_texts[1].align_to(anno_texts[0], DOWN)
                            else:
                                anno_texts[0].align_to(anno_texts[1], DOWN)
                                
                            expr_group.add(anno_texts)
                
                content_group.add(expr_group)
        
        # Arrange everything
        content_group.arrange(DOWN, aligned_edge=self.alignment, buff=self.expression_buff)
        
        if self.title:
            result.arrange(DOWN, aligned_edge=self.alignment, buff=self.title_buff)
        else:
            result = content_group
            
        self.rendered_group = result
        
        # If scene is provided, add to scene
        if scene:
            scene.add(result)
            
        return result
    
    def get_mobject(self):
        """Get the rendered mobject, rendering if necessary."""
        if self.rendered_group is None:
            self.render()
        return self.rendered_group


class MathTutorialLayout:
    """Manages the layout of multiple MathContentBlocks with consistent spacing."""
    
    def __init__(
        self,
        title=None,
        title_scale=0.7,
        title_color=WHITE,
        step_buff=0.5,
        left_edge=1.0,
        top_edge=0.5,
        alignment=LEFT
    ):
        self.title = title
        self.title_scale = title_scale
        self.title_color = title_color
        self.step_buff = step_buff
        self.left_edge = left_edge
        self.top_edge = top_edge
        self.alignment = alignment
        
        self.steps = []
        self.rendered_group = None
        
    def add_step(self, content_block):
        """Add a MathContentBlock as a step."""
        self.steps.append(content_block)
        return content_block
        
    def create_step(self, title=None, **kwargs):
        """Create and add a new step."""
        step = MathContentBlock(title=title, **kwargs)
        self.steps.append(step)
        return step
        
    def render(self, scene=None):
        """Render all steps to a VGroup."""
        result = VGroup()
        
        # Add title if provided
        if self.title:
            title = Tex(self.title, color=self.title_color).scale(self.title_scale)
            result.add(title)
        
        # Render each step
        step_groups = VGroup()
        for step in self.steps:
            step_groups.add(step.render())
        
        # Arrange steps
        step_groups.arrange(DOWN, aligned_edge=self.alignment, buff=self.step_buff)
        
        if self.title:
            result.arrange(DOWN, aligned_edge=self.alignment, buff=self.step_buff)
        else:
            result = step_groups
            
        # Position the result
        result.to_edge(UP, buff=self.top_edge).to_edge(LEFT, buff=self.left_edge)
        
        self.rendered_group = result
        
        # If scene is provided, add to scene
        if scene:
            scene.add(result)
            
        return result
    
    def get_mobject(self):
        """Get the rendered mobject, rendering if necessary."""
        if self.rendered_group is None:
            self.render()
        return self.rendered_group