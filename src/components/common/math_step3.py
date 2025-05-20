"""Math step layout system for creating structured mathematical solutions in Manim."""

from typing import List, Optional, Dict, Any
from manim import *

# Assume FOOTNOTE_SCALE is defined elsewhere - we'll include it as a default
FOOTNOTE_SCALE = 0.55  # Default value

class MathStepGroup:
    """A group of related mathematical steps with a label and expressions."""
    
    def __init__(
        self, 
        label_text: str = "", 
        label_color: str = "#DBDBDB",
        label_scale: float = 0.6,
        element_buff: float = 0.2,
        find_element_func = None
    ):
        """Initialize a math step group."""
        self.label_text = label_text
        self.label_color = label_color
        self.label_scale = label_scale
        self.element_buff = element_buff
        self.find_element_func = find_element_func
        
        self.label = None
        self.expressions = []  # List of expressions
        self.annotations = []  # List of (expr_index, annotation_info) tuples
        self.built_group = None
        
        # Create label if provided
        if label_text:
            self.label = Tex(label_text, color=label_color).scale(label_scale)
    
    def add_expression(self, expression):
        """Add an expression to this step group."""
        self.expressions.append(expression)
        self.built_group = None  # Mark for rebuild
        return len(self.expressions) - 1
    
    def add_annotation(
        self, 
        text,  # The text of the annotation
        left_target,  # Target element in left
        right_target,  # Target element in right
        to_expr_index=-1,  # Expression to add annotation to
        color=WHITE,
        scale=FOOTNOTE_SCALE,
        h_spacing=0
    ):
        """Add annotation to a specific expression."""
        if not self.expressions:
            raise ValueError("Cannot add annotation without expressions")
            
        # Normalize negative indices
        if to_expr_index < 0:
            to_expr_index = len(self.expressions) + to_expr_index
            
        if to_expr_index < 0 or to_expr_index >= len(self.expressions):
            raise ValueError(f"Expression index {to_expr_index} out of range")
        
        # Store annotation information for later creation
        self.annotations.append((
            to_expr_index,
            {
                'text': text,
                'left_target': left_target,
                'right_target': right_target,
                'color': color,
                'scale': scale,
                'h_spacing': h_spacing
            }
        ))
        
        self.built_group = None  # Mark for rebuild
        
    def add_annotations(self, term_added, left_term, right_term, color=None, h_spacing=0):
        """Direct implementation of your original add_annotations method.
        
        This is included for compatibility with any code that expects this method,
        but it should generally be used through add_annotation instead.
        """
        terms = VGroup(*[MathTex(rf"{term_added}").scale(FOOTNOTE_SCALE) for _ in range(2)])
        if color:
            terms.set_color(color)
            
        terms[0].next_to(left_term, DOWN)
        terms[1].next_to(right_term, DOWN)
        
        # Apply horizontal spacing adjustment
        terms[0].shift(LEFT * h_spacing)  # Move left annotation further left
        terms[1].shift(RIGHT * h_spacing)  # Move right annotation further right
        
        if terms[0].get_y() < terms[1].get_y():
            terms[1].align_to(terms[0], DOWN)
        else:
            terms[0].align_to(terms[1], DOWN)

        return terms
    
    def get_group(self):
        """Get the arranged group for this step."""
        if self.built_group is not None:
            return self.built_group
            
        if not self.find_element_func:
            raise ValueError("Must set find_element_func before getting the group")
            
        elements = []
        if self.label:
            elements.append(self.label)
            
        # Add all expressions
        for expr in self.expressions:
            elements.append(expr)
        
        # Create all annotations
        for expr_idx, annotation_info in self.annotations:
            if expr_idx < 0 or expr_idx >= len(self.expressions):
                continue  # Skip invalid indices
                
            expr = self.expressions[expr_idx]
            
            # Find the target elements
            left_element = self.find_element_func(
                annotation_info['left_target'], 
                expr[0]  # Access the actual MathTex object
            )
            right_element = self.find_element_func(
                annotation_info['right_target'], 
                expr[0]  # Access the actual MathTex object
            )
            
            if left_element and right_element:
                # Create annotation using your original method
                annotation = self.add_annotations(
                    annotation_info['text'],
                    left_element,
                    right_element,
                    color=annotation_info['color'],
                    h_spacing=annotation_info['h_spacing']
                )
                
                # Add annotation after its corresponding expression
                insert_idx = elements.index(expr) + 1
                elements.insert(insert_idx, annotation)
        
        # Create the group with proper arrangement
        self.built_group = VGroup(*elements).arrange(
            DOWN, 
            aligned_edge=LEFT, 
            buff=self.element_buff
        )
        
        return self.built_group


class MathSolution:
    """A complete mathematical solution with multiple step groups."""
    
    def __init__(
        self, 
        step_groups=None,
        group_buff=0.5,
        find_element_func=None
    ):
        """Initialize a math solution."""
        self.step_groups = step_groups or []
        self.group_buff = group_buff
        self.find_element_func = find_element_func
        self.group = None
        
        # Set functions for all steps
        if self.find_element_func and self.step_groups:
            for step in self.step_groups:
                step.find_element_func = self.find_element_func
    
    def add_step_group(self, step_group):
        """Add a step group to the solution."""
        if self.find_element_func:
            step_group.find_element_func = self.find_element_func
            
        self.step_groups.append(step_group)
        self.group = None  # Mark for rebuild
        return step_group
    
    def create_step_group(self, label_text="", **kwargs):
        """Create and add a new step group."""
        step_group = MathStepGroup(label_text, **kwargs)
        if self.find_element_func:
            step_group.find_element_func = self.find_element_func
        return self.add_step_group(step_group)
    
    def set_find_element_func(self, func):
        """Set the function used to find elements in expressions."""
        self.find_element_func = func
        for step in self.step_groups:
            step.find_element_func = func
        self.group = None  # Mark for rebuild
    
    def get_group(self):
        """Get the complete arranged solution."""
        if self.group is not None:
            return self.group
            
        if not self.find_element_func:
            raise ValueError("Must set find_element_func before getting the group")
            
        # Get the arranged group for each step
        step_groups = [sg.get_group() for sg in self.step_groups]
        
        # Arrange all step groups vertically
        self.group = VGroup(*step_groups).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=self.group_buff
        )
        
        return self.group