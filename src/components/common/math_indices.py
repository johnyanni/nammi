"""Component for displaying indices of MathTex objects."""

from manim import *

class MathIndices:
    """A utility class for displaying indices of MathTex objects."""
    
    @staticmethod
    def display_indices(scene, mathtex_obj, label_text="", display_duration=5):
        """
        Displays the indices of characters in a MathTex object by overlaying index labels.
        
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
        
        # Create group for index labels
        index_labels_group = VGroup()
        
        # Handle different structures of MathTex
        if len(mathtex_obj.submobjects) > 0:
            # Extract the first submobject (typical for MathTex)
            submob = mathtex_obj[0]
            
            # Add index labels for each part
            for i in range(len(submob)):
                # Get character
                char = submob[i]
                
                # Create index label
                index_label = Text(str(i), font_size=14, color=RED)
                
                # Position label above the character
                index_label.move_to(char.get_center() + UP * 0.3)
                
                # Add a small background for better visibility
                bg = SurroundingRectangle(
                    index_label, 
                    color=BLUE, 
                    stroke_width=1, 
                    fill_color=BLACK,
                    fill_opacity=0.7,
                    buff=0.05
                )
                
                # Group label with its background
                label_group = VGroup(bg, index_label)
                index_labels_group.add(label_group)
        
        # Make sure the original MathTex is visible (add it if it's not already in the scene)
        if mathtex_obj not in scene.mobjects:
            scene.add(mathtex_obj)
            
        # Add the index labels on top
        scene.add(index_labels_group)
        
        # Print the structure information to the console for reference
        print(f"Structure of {label_text}:")
        print(f"Total submobjects: {len(mathtex_obj.submobjects)}")
        for i, submob in enumerate(mathtex_obj.submobjects):
            if hasattr(submob, "submobjects"):
                print(f"  Submobject {i} has {len(submob.submobjects)} parts")
        
        # Wait for the specified duration
        scene.wait(display_duration)
        
        # Clean up just the index labels, leaving the original MathTex
        scene.remove(index_labels_group)
        if header:
            scene.remove(header)
        
        # Note: We don't remove the original mathtex_obj since we're assuming
        # it's part of the scene and should remain visible