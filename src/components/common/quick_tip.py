"""Quick tip component for displaying helpful hints in tutorials."""

from manim import *
from ..styles.theme import *

class QuickTip(VGroup):
    def __init__(
            self,
            body_text,
            header_text="QUICKTIP",
            box_width=4,
            header_color=WHITE,
            header_bg_color=BLUE,
            body_color=WHITE,
            fill_color=BLUE_E,
            fill_opacity=0.7,
            font_size=28,
            line_spacing=0.1,
            **kwargs
    ):
        super().__init__(**kwargs)
        
        header = Text(header_text, color=header_color, weight=BOLD).scale(0.4)          
        header_background = Rectangle(
            width=box_width, height=0.5, color=header_bg_color, fill_opacity=1, stroke_width=0
        )
        header_group = VGroup(header_background, header)
        header.align_to(header_background, LEFT).shift(RIGHT * 0.2)
        
        body_lines = self.wrap_tex(body_text, box_width - 0.25, font_size)
        body = VGroup(*[Tex(line, color=body_color, font_size=font_size) 
                      for line in body_lines])
        body.arrange(DOWN, buff=line_spacing)

        # Calculate dimensions
        total_height = header.height + body.height + line_spacing * 4
        box = Rectangle(
            width=box_width,
            height=total_height,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=fill_color,
            stroke_width=0,
        )

        VGroup(header_group, VGroup(body, box)).arrange(DOWN, buff=-0.05)
        self.add(box, body, header_group)

    def wrap_tex(self, text, max_width, font_size):
        words = []
        current_word = []
        in_command = False
        
        for char in text:
            if char == "\\":
                in_command = True
                current_word.append(char)
            elif char == " " and not in_command:
                words.append("".join(current_word))
                current_word = []
            elif char in ["{", "}"]:
                current_word.append(char)
                in_command = False
            else:
                current_word.append(char)
                if in_command and char.isalpha():
                    in_command = False

        if current_word:
            words.append("".join(current_word))

        # Build lines
        lines = []
        current_line = []
        current_width = 0
        
        for word in words:
            test_tex = Tex(" ".join(current_line + [word]), font_size=font_size)
            if test_tex.width > max_width:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                current_line.append(word)
                
        lines.append(" ".join(current_line))
        return lines