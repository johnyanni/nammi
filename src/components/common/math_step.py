
from manim import *




class MathStep:
    """A robust class for creating mathematical steps with annotations."""
    
    def __init__(self, scene, number=None):
        """Initialize a math step."""
        self.scene = scene
        self.number = number
        self.title = None
        self.expressions = []
        self.pending_annotations = []  # Store annotation info for later creation
        self.annotation_placeholders = []  # Placeholders to reserve space
        self.annotations = {}  # Will store created annotations by expression index
        self.group = None
    
    def add_title(self, title_text, color="#DBDBDB", scale=0.55):
        """Add a title to the step."""
        if self.number is not None:
            title_text = f"Step {self.number}: {title_text}"
            
        self.title = Tex(title_text, color=color).scale(scale)
        return self
    
    def add_expression(self, expression):
        """Add an expression to the step."""
        self.expressions.append(expression)
        return expression  # Return for chained operations like finding elements
    
    def register_annotation(self, term_added, left_term, right_term, color=None, h_spacing=0):
        """Register an annotation and create a placeholder to reserve space."""
        if not self.expressions:
            raise ValueError("Add an expression before registering annotations")
        
        # Store the annotation details for later creation
        expr_idx = len(self.expressions) - 1
        self.pending_annotations.append({
            'term': term_added,
            'left': left_term,
            'right': right_term,
            'color': color,
            'h_spacing': h_spacing,
            'expr_idx': expr_idx  # Associate with the last added expression
        })
        
        # Create an invisible placeholder to reserve space
        # This is a crucial step to ensure space is allocated during layout
        FOOTNOTE_SCALE = 0.5
        placeholder = VGroup(
            # Create two invisible placeholders with same size as annotations
            *[MathTex(rf"{term_added}").scale(FOOTNOTE_SCALE).set_opacity(0) for _ in range(2)]
        )
        
        # Rough positioning - will be refined after layout
        placeholder[0].next_to(left_term, DOWN)
        placeholder[1].next_to(right_term, DOWN)
        
        # Align bottoms of placeholders
        if placeholder[0].get_y() < placeholder[1].get_y():
            placeholder[1].align_to(placeholder[0], DOWN)
        else:
            placeholder[0].align_to(placeholder[1], DOWN)
        
        self.annotation_placeholders.append((placeholder, expr_idx))
        
        return self
    
    def build(self, buff=0.2, aligned_edge=LEFT):
        """Build the step group with space reserved for annotations."""
        elements = []
        
        # Add title if it exists
        if self.title:
            elements.append(self.title)
        
        # Add expressions with their placeholders
        for i, expr in enumerate(self.expressions):
            elements.append(expr)
            
            # Add placeholders after the expression they belong to
            for placeholder, expr_idx in self.annotation_placeholders:
                if expr_idx == i:
                    elements.append(placeholder)
        
        # Create and arrange the group
        self.group = VGroup(*elements).arrange(DOWN, buff=buff, aligned_edge=aligned_edge)
        return self.group
    
    def create_annotations(self):
        """Create the actual annotations based on placeholder positions."""
        FOOTNOTE_SCALE = 0.5
        created = {}
        
        # Create annotations based on pending information
        for anno_info in self.pending_annotations:
            # Get information
            expr_idx = anno_info['expr_idx']
            left_term = anno_info['left']
            right_term = anno_info['right']
            term = anno_info['term']
            color = anno_info['color']
            h_spacing = anno_info['h_spacing']
            
            # Create annotation terms
            terms = VGroup(*[MathTex(rf"{term}").scale(FOOTNOTE_SCALE) for _ in range(2)])
            
            if color:
                terms.set_color(color)
            
            # Find the corresponding placeholder
            placeholder = None
            for ph, ph_idx in self.annotation_placeholders:
                if ph_idx == expr_idx:
                    placeholder = ph
                    break
            
            if placeholder:
                # Position based on placeholder positions (which are correctly arranged)
                terms[0].move_to(placeholder[0])
                terms[1].move_to(placeholder[1])
                
                # Apply horizontal spacing if needed
                terms[0].shift(LEFT * h_spacing)
                terms[1].shift(RIGHT * h_spacing)
                
                # Store by expression index
                if expr_idx not in created:
                    created[expr_idx] = []
                created[expr_idx].append(terms)
        
        self.annotations = created  # Store for later reference
        return created
    
    def get_expression(self, index=0):
        """Get an expression by index."""
        if index >= len(self.expressions):
            raise IndexError(f"Expression index {index} out of range (0-{len(self.expressions)-1})")
        
        return self.expressions[index]
    
    def get_annotation(self, expr_index=0, anno_index=0):
        """Get a specific annotation by indices."""
        if expr_index not in self.annotations:
            raise KeyError(f"No annotations for expression index {expr_index}")
        
        if anno_index >= len(self.annotations[expr_index]):
            raise IndexError(f"Annotation index {anno_index} out of range for expression {expr_index}")
        
        return self.annotations[expr_index][anno_index]
    
