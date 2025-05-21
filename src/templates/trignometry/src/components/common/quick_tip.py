"""Quick tip component for displaying helpful hints in tutorials."""

from manim import *
from .smart_tex import SmartColorizeStatic

class QuickTip(VGroup):

    def __init__(
            self,
            body_text,
            header_text="QUICKTIP",
            box_width=5,
            header_color=WHITE,
            header_bg_color="#9A48D0",
            body_color=WHITE,
            fill_color="#3B1C62",
            fill_opacity=1,
            font_size=28,
            line_spacing=0.1,
            color_map=None,
            **kwargs
    ):
        super().__init__(**kwargs)
        
        header = Text(header_text, color=header_color, weight=BOLD).scale(0.4)          
        header_background = RoundedRectangle(
            corner_radius=0.1, width=box_width, height=0.5, color=header_bg_color, fill_opacity=1, stroke_width=0
        )
        header_group = VGroup(header_background, header)
        header.align_to(header_background, LEFT).shift(RIGHT * 0.2)

        body_lines = self.wrap_tex(body_text, box_width - 0.25, font_size)
        body = VGroup(*[Tex(line, color=body_color, font_size=font_size) 
                      for line in body_lines])
        body.arrange(DOWN, buff=line_spacing)

        if color_map:
            for part in body:
                SmartColorizeStatic(part, color_map=color_map)
         
        # Calculate dimensions
        total_height = header.height + body.height + line_spacing * 4
        box = RoundedRectangle(
            corner_radius=0.1,
            width=box_width,
            height=total_height,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=fill_color,
            stroke_width=0,
        )

        VGroup(header_group, VGroup(body, box)).arrange(DOWN, buff=-0.15)
        self.add(box, body, header_group)
          
    def wrap_tex(self, text, max_width, font_size):        
        import re
        
        # Split by math blocks to preserve them
        math_pattern = r'(\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{.*?\}.*?\\end\{.*?\})'
        parts = re.split(math_pattern, text, flags=re.DOTALL)
        
        lines = []
        current_line = []
                
        for part in parts:
            if re.match(math_pattern, part):
                # This is a math block, keep it intact
                if current_line:
                    test_width = Tex(" ".join(current_line) + " " + part, font_size=font_size).width
                    if test_width > max_width and len(current_line) > 0:
                        lines.append(" ".join(current_line))
                        current_line = [part]
                    else:
                        current_line.append(part)
                else:
                    current_line.append(part)
            else:
                # Regular text, split into words
                words = part.split()
                for word in words:
                    test_line = current_line + [word]
                    test_tex = Tex(" ".join(test_line), font_size=font_size)
                    
                    if test_tex.width > max_width and len(current_line) > 0:
                        lines.append(" ".join(current_line))
                        current_line = [word]
                    else:
                        current_line.append(word)
        
        # Add the last line if there's anything left
        if current_line:
            lines.append(" ".join(current_line))
            
        return lines
