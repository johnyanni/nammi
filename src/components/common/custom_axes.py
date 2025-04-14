from manim import *

class CustomAxes(Axes):
    def __init__(self, tip_color=WHITE, **kwargs):
        if "x_range" in kwargs:
            x_min, x_max, x_step = kwargs["x_range"]
            kwargs["x_range"] = [x_min - x_step, x_max + x_step, x_step]
            
            # Setup x_axis_config to exclude extreme values
            if "x_axis_config" not in kwargs:
                kwargs["x_axis_config"] = {}
            
            if "numbers_to_exclude" not in kwargs["x_axis_config"]:
                kwargs["x_axis_config"]["numbers_to_exclude"] = []
            elif not isinstance(kwargs["x_axis_config"]["numbers_to_exclude"], list):
                kwargs["x_axis_config"]["numbers_to_exclude"] = [kwargs["x_axis_config"]["numbers_to_exclude"]]
                
            # Add the extreme values to exclude list for x-axis
            kwargs["x_axis_config"]["numbers_to_exclude"].extend([x_min - x_step, x_max + x_step])
        
        if "y_range" in kwargs:
            y_min, y_max, y_step = kwargs["y_range"]
            kwargs["y_range"] = [y_min - y_step, y_max + y_step, y_step]
            
            # Setup y_axis_config to exclude extreme values
            if "y_axis_config" not in kwargs:
                kwargs["y_axis_config"] = {}
            
            if "numbers_to_exclude" not in kwargs["y_axis_config"]:
                kwargs["y_axis_config"]["numbers_to_exclude"] = []
            elif not isinstance(kwargs["y_axis_config"]["numbers_to_exclude"], list):
                kwargs["y_axis_config"]["numbers_to_exclude"] = [kwargs["y_axis_config"]["numbers_to_exclude"]]
                
            # Add the extreme values to exclude list for y-axis
            kwargs["y_axis_config"]["numbers_to_exclude"].extend([y_min - y_step, y_max + y_step])
        
        kwargs["tips"] = False
            
        super().__init__(**kwargs)

        axis_config = getattr(self, "axis_config", {})
        tip_width =  axis_config.get("tip_width", 0.2)
        tip_length = axis_config.get("tip_length", 0.2)
        
        self.positive_x_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_length, 
            start_angle=0,
            color=tip_color
        ).next_to(self.x_axis.get_end(), direction=RIGHT, buff=0)
        
        self.negative_x_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_length,
            color=tip_color
        ).next_to(self.x_axis.get_start(), direction=LEFT, buff=0)
        
        self.positive_y_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_length, 
            start_angle=PI/2,
            color=tip_color
        ).next_to(self.y_axis.get_end(), direction=UP, buff=0)
        
        self.negative_y_arrow = ArrowTriangleTip(
            fill_opacity=1, 
            width=tip_width, 
            length=tip_length, 
            start_angle=-PI/2,
            color=tip_color
        ).next_to(self.y_axis.get_start(), direction=DOWN, buff=0)

        self.add(self.positive_x_arrow, self.negative_x_arrow, self.positive_y_arrow, self.negative_y_arrow)
