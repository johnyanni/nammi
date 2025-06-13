from manim import *

class CustomAxes(Axes):
    def __init__(self, tip_width=0.2, tip_height=0.2, tip_color=WHITE, **kwargs):
        if "tips" not in kwargs:
            kwargs["tips"] = False
            
        super().__init__(**kwargs)

        self.positive_x_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_height, 
            start_angle=0,
            color=tip_color
        ).next_to(self.x_axis.get_end(), direction=RIGHT, buff=0)
        
        self.negative_x_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_height,
            color=tip_color
        ).next_to(self.x_axis.get_start(), direction=LEFT, buff=0)
        
        self.positive_y_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_height, 
            start_angle=PI/2,
            color=tip_color
        ).next_to(self.y_axis.get_end(), direction=UP, buff=0)
        
        self.negative_y_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_height, 
            start_angle=-PI/2,
            color=tip_color
        ).next_to(self.y_axis.get_start(), direction=DOWN, buff=0)

        self.add(self.positive_x_arrow, self.negative_x_arrow, self.positive_y_arrow, self.negative_y_arrow)