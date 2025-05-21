"""Component for displaying indices of MathTex objects."""

from manim import *

class MathIndices:
    """A utility class for displaying indices of MathTex objects."""
    
    @staticmethod
    def display_indices(scene, mathtex_obj, label_text="", display_duration=5):
        """
        Displays the indices of characters in a MathTex object.
        
        Args:
            scene: The Manim scene to add/remove objects to/from
            mathtex_obj: The MathTex object to visualize
            label_text: Optional text to display above the expression
            display_duration: How long to display the visualization (seconds)
            
        Example Usage:
            self.display_indices(step2_info, "step2_info")
        """
        # Add a header with the label text
        header = None
        if label_text:
            header = Text(label_text, font_size=36)
            header.to_edge(UP)
            scene.add(header)
        
        # Add the original expression
        original = mathtex_obj.copy()
        original.move_to(ORIGIN + UP)
        scene.add(original)
        
        # Create visualization group
        viz_group = VGroup()
        
        # Handle different structures of MathTex
        if len(mathtex_obj.submobjects) > 0:
            # Extract the first submobject (typical for MathTex)
            submob = mathtex_obj[0]
            
            # Add index labels for each part
            for i in range(len(submob)):
                # Get character
                char = submob[i].copy()
                
                # Create index label
                index_label = Text(str(i), font_size=18, color=RED)
                index_label.next_to(char, DOWN, buff=0.1)
                
                # Create background for visibility
                bg = SurroundingRectangle(
                    char, 
                    color=BLUE, 
                    stroke_width=1, 
                    fill_opacity=0.1,
                    buff=0.05
                )
                
                # Group character with its index
                char_group = VGroup(char, bg, index_label)
                viz_group.add(char_group)
            
            # Arrange the visualization
            viz_group.arrange(RIGHT, buff=0.3)
            viz_group.move_to(ORIGIN + DOWN)
            
            # Add the visualization
            scene.add(viz_group)
        
        # Print the structure information to the console for reference
        print(f"Structure of {label_text}:")
        print(f"Total submobjects: {len(mathtex_obj.submobjects)}")
        for i, submob in enumerate(mathtex_obj.submobjects):
            if hasattr(submob, "submobjects"):
                print(f"  Submobject {i} has {len(submob.submobjects)} parts")
        
        # Wait for the specified duration
        scene.wait(display_duration)
        
        # Clean up
        scene.remove(viz_group)
        if header:
            scene.remove(header)
        scene.remove(original) 