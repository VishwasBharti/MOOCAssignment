from manimlib.imports import *
import numpy as np
import itertools as it

from manimlib.animation.creation import Write, DrawBorderThenFill, ShowCreation
from manimlib.animation.transform import Transform
from manimlib.animation.update import UpdateFromAlphaFunc
from manimlib.constants import *
from manimlib.mobject.functions import ParametricFunction
from manimlib.mobject.geometry import Line
from manimlib.mobject.geometry import Rectangle
from manimlib.mobject.geometry import RegularPolygon
from manimlib.mobject.number_line import NumberLine
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.mobject.svg.tex_mobject import TextMobject
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VectorizedPoint
from manimlib.scene.scene import Scene
from manimlib.utils.bezier import interpolate
from manimlib.utils.color import color_gradient
from manimlib.utils.color import invert_color
from manimlib.utils.space_ops import angle_of_vector

# TODO, this should probably reimplemented entirely, especially so as to
# better reuse code from mobject/coordinate_systems.
# Also, I really dislike how the configuration is set up, this
# is way too messy to work with.
def coord(x,y,z=0):
    return np.array([x,y,z])
def getX(mob):
    return mob.get_center()[0]
def getY(mob):
    return mob.get_center()[1]

class GraphScene(Scene):
    CONFIG = {
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
        "x_coords":np.array([-10,  -1, -1, 1, 1, 10]),
        "y_coords":np.array([0, 0, 1, 1, 0, 0]),
        "x_coords_triangle_part1":np.array([-10, -2]),
        "y_coords_triangle_part1":np.array([0, 0]),
        "x_coords_triangle_part2":np.array([-2, 0]),
        "y_coords_triangle_part2":np.array([0, 2]),
        "x_coords_triangle_part3":np.array([0, 2]),
        "y_coords_triangle_part3":np.array([2, 0]),
        "x_coords_triangle_part4":np.array([2, 10]),
        "y_coords_triangle_part4":np.array([0, 0]),
        "x_coords_rect2":np.array([-10, -10, -8, -8]),
        "y_coords_rect2":np.array([0, 1, 1, 0]),
        "x_coords_rect3":np.array([8, 8, 10, 10]),
        "y_coords_rect3":np.array([0, 1, 1, 0])                
    }

    def setup(self):
        self.default_graph_colors_cycle = it.cycle(self.default_graph_colors)
        self.left_T_label = VGroup()
        self.left_v_line = VGroup()
        self.right_T_label = VGroup()
        self.right_v_line = VGroup()
        x_num_range = float(self.x_max - self.x_min)
        self.space_unit_to_x = self.x_axis_width / x_num_range
        y_num_range = float(self.y_max - self.y_min)
        self.space_unit_to_y = self.y_axis_height / y_num_range        
        self.tuples = list(zip(self.x_coords*self.space_unit_to_x,self.y_coords*self.space_unit_to_y))
        self.tuples_triangle_part1 = list(zip(self.x_coords_triangle_part1*self.space_unit_to_x,self.y_coords_triangle_part1*self.space_unit_to_y))
        self.tuples_triangle_part2 = list(zip(self.x_coords_triangle_part2*self.space_unit_to_x,self.y_coords_triangle_part2*self.space_unit_to_y))
        self.tuples_triangle_part3 = list(zip(self.x_coords_triangle_part3*self.space_unit_to_x,self.y_coords_triangle_part3*self.space_unit_to_y))
        self.tuples_triangle_part4 = list(zip(self.x_coords_triangle_part4*self.space_unit_to_x,self.y_coords_triangle_part4*self.space_unit_to_y))
        self.tuples_rect2 = list(zip(self.x_coords_rect2*self.space_unit_to_x,self.y_coords_rect2*self.space_unit_to_y))
        self.tuples_rect3 = list(zip(self.x_coords_rect3*self.space_unit_to_x,self.y_coords_rect3*self.space_unit_to_y))    
    def setup_axes(self, animate=False):
        # TODO, once eoc is done, refactor this to be less redundant.
        x_num_range = float(self.x_max - self.x_min)
        self.space_unit_to_x = self.x_axis_width / x_num_range
        if self.x_labeled_nums is None:
            self.x_labeled_nums = []
        if self.x_leftmost_tick is None:
            self.x_leftmost_tick = self.x_min
        x_axis = NumberLine(
            x_min=self.x_min,
            x_max=self.x_max,
            unit_size=self.space_unit_to_x,
            tick_frequency=self.x_tick_frequency,
            leftmost_tick=self.x_leftmost_tick,
            numbers_with_elongated_ticks=self.x_labeled_nums,
            color=self.axes_color
        )
        x_axis.shift(self.graph_origin - x_axis.number_to_point(0))
        if len(self.x_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.x_labeled_nums = [x for x in self.x_labeled_nums if x != 0]
            x_axis.add_numbers(*self.x_labeled_nums)
        if self.x_axis_label:
            x_label = TextMobject(self.x_axis_label)
            x_label.next_to(
                x_axis.get_tick_marks(), UP + RIGHT,
                buff=SMALL_BUFF
            )
            x_label.shift_onto_screen()
            x_axis.add(x_label)
            self.x_axis_label_mob = x_label

        y_num_range = float(self.y_max - self.y_min)
        self.space_unit_to_y = self.y_axis_height / y_num_range

        if self.y_labeled_nums is None:
            self.y_labeled_nums = []
        if self.y_bottom_tick is None:
            self.y_bottom_tick = self.y_min
        y_axis = NumberLine(
            x_min=self.y_min,
            x_max=self.y_max,
            unit_size=self.space_unit_to_y,
            tick_frequency=self.y_tick_frequency,
            leftmost_tick=self.y_bottom_tick,
            numbers_with_elongated_ticks=self.y_labeled_nums,
            color=self.axes_color,
            line_to_number_vect=LEFT,
            label_direction=LEFT,
        )
        y_axis.shift(self.graph_origin - y_axis.number_to_point(0))
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))
        if len(self.y_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.y_labeled_nums = [y for y in self.y_labeled_nums if y != 0]
            y_axis.add_numbers(*self.y_labeled_nums)
        if self.y_axis_label:
            y_label = TextMobject(self.y_axis_label)
            y_label.next_to(
                y_axis.get_corner(UP + RIGHT), UP + RIGHT,
                buff=SMALL_BUFF
            )
            y_label.shift_onto_screen()
            y_axis.add(y_label)
            self.y_axis_label_mob = y_label

        if animate:
            self.play(Write(VGroup(x_axis, y_axis)))
        else:
            self.add(x_axis, y_axis)
        self.x_axis, self.y_axis = self.axes = VGroup(x_axis, y_axis)
        self.default_graph_colors = it.cycle(self.default_graph_colors)

    def coords_to_point(self, x, y):
        assert(hasattr(self, "x_axis") and hasattr(self, "y_axis"))
        result = self.x_axis.number_to_point(x)[0] * RIGHT
        result += self.y_axis.number_to_point(y)[1] * UP
        return result

    def point_to_coords(self, point):
        return (self.x_axis.point_to_number(point),
                self.y_axis.point_to_number(point))

    def get_graph(
        self, func,
        color=None,
        x_min=None,
        x_max=None,
        **kwargs
    ):
        if color is None:
            color = next(self.default_graph_colors_cycle)
        if x_min is None:
            x_min = self.x_min
        if x_max is None:
            x_max = self.x_max
        def parameterized_function(alpha):
            x = interpolate(x_min, x_max, alpha)
            y = func(x)
            if not np.isfinite(y):
                y = self.y_max
            return self.coords_to_point(x, y)

        graph = ParametricFunction(
            parameterized_function,
            color=color,
            **kwargs
        )
        graph.underlying_function = func
        return graph

    def input_to_graph_point(self, x, graph):
        return self.coords_to_point(x, graph.underlying_function(x))

    def angle_of_tangent(self, x, graph, dx=0.01):
        vect = self.input_to_graph_point(
            x + dx, graph) - self.input_to_graph_point(x, graph)
        return angle_of_vector(vect)

    def slope_of_tangent(self, *args, **kwargs):
        return np.tan(self.angle_of_tangent(*args, **kwargs))

    def get_derivative_graph(self, graph, dx=0.01, **kwargs):
        if "color" not in kwargs:
            kwargs["color"] = self.default_derivative_color

        def deriv(x):
            return self.slope_of_tangent(x, graph, dx) / self.space_unit_to_y
        return self.get_graph(deriv, **kwargs)

    def get_graph_label(
        self,
        graph,
        label="f(x)",
        x_val=None,
        direction=RIGHT,
        buff=MED_SMALL_BUFF,
        color=None,
    ):
        label = TexMobject(label)
        color = color or graph.get_color()
        label.set_color(color)
        if x_val is None:
            # Search from right to left
            for x in np.linspace(self.x_max, self.x_min, 100):
                point = self.input_to_graph_point(x, graph)
                if point[1] < FRAME_Y_RADIUS:
                    break
            x_val = x
        label.next_to(
            self.input_to_graph_point(x_val, graph),
            direction,
            buff=buff
        )
        label.shift_onto_screen()
        return label

    def show_area(self,graph):
        dx = 0.005
        rects = self.get_riemann_rectangles(
                    graph,
                    x_min = -1,
                    x_max = 1,
                    dx = dx,
                    stroke_width = dx,
                )
        foreground_mobjects = [self.axes]

        self.play(
            DrawBorderThenFill(
                rects,
                run_time = 2,
                rate_func = smooth,
                lag_ratio = 0.5,
            )
        )
        self.wait()

    def get_riemann_rectangles(
        self,
        graph,
        x_min=None,
        x_max=None,
        dx=0.1,
        input_sample_type="left",
        stroke_width=1,
        stroke_color=BLACK,
        fill_opacity=1,
        start_color=None,
        end_color=None,
        show_signed_area=True,
        width_scale_factor=1.001
    ):
        x_min = x_min if x_min is not None else self.x_min
        x_max = x_max if x_max is not None else self.x_max
        if start_color is None:
            start_color = self.default_riemann_start_color
        if end_color is None:
            end_color = self.default_riemann_end_color
        rectangles = VGroup()
        x_range = np.arange(x_min, x_max, dx)
        colors = color_gradient([start_color, end_color], len(x_range))
        for x, color in zip(x_range, colors):
            if input_sample_type == "left":
                sample_input = x
            elif input_sample_type == "right":
                sample_input = x + dx
            elif input_sample_type == "center":
                sample_input = x + 0.5 * dx
            else:
                raise Exception("Invalid input sample type")
            graph_point = self.input_to_graph_point(sample_input, graph)
            points = VGroup(*list(map(VectorizedPoint, [
                self.coords_to_point(x, 0),
                self.coords_to_point(x + width_scale_factor * dx, 0),
                graph_point
            ])))

            rect = Rectangle()
            rect.replace(points, stretch=True)
            if graph_point[1] < self.graph_origin[1] and show_signed_area:
                fill_color = invert_color(color)
            else:
                fill_color = color
            rect.set_fill(fill_color, opacity=fill_opacity)
            rect.set_stroke(stroke_color, width=stroke_width)
            rectangles.add(rect)
        return rectangles

    def get_riemann_rectangles_list(
        self,
        graph,
        n_iterations,
        max_dx=0.5,
        power_base=2,
        stroke_width=1,
        **kwargs
    ):
        return [
            self.get_riemann_rectangles(
                graph=graph,
                dx=float(max_dx) / (power_base**n),
                stroke_width=float(stroke_width) / (power_base**n),
                **kwargs
            )
            for n in range(n_iterations)
        ]

    def get_area(self, graph, t_min, t_max):
        numerator = max(t_max - t_min, 0.0001)
        dx = float(numerator) / self.num_rects
        return self.get_riemann_rectangles(
            graph,
            x_min=t_min,
            x_max=t_max,
            dx=dx,
            stroke_width=0,
        ).set_fill(opacity=self.area_opacity)

    def transform_between_riemann_rects(self, curr_rects, new_rects, **kwargs):
        transform_kwargs = {
            "run_time": 2,
            "lag_ratio": 0.5
        }
        added_anims = kwargs.get("added_anims", [])
        transform_kwargs.update(kwargs)
        curr_rects.align_submobjects(new_rects)
        x_coords = set()  # Keep track of new repetitions
        for rect in curr_rects:
            x = rect.get_center()[0]
            if x in x_coords:
                rect.set_fill(opacity=0)
            else:
                x_coords.add(x)
        self.play(
            Transform(curr_rects, new_rects, **transform_kwargs),
            *added_anims
        )

    def get_vertical_line_to_graph(
        self,
        x, graph,
        line_class=Line,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(x, 0),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_vertical_lines_to_graph(
        self, graph,
        x_min=None,
        x_max=None,
        num_lines=20,
        **kwargs
    ):
        x_min = x_min or self.x_min
        x_max = x_max or self.x_max
        return VGroup(*[
            self.get_vertical_line_to_graph(x, graph, **kwargs)
            for x in np.linspace(x_min, x_max, num_lines)
        ])

    def get_secant_slope_group(
        self,
        x, graph,
        dx=None,
        dx_line_color=None,
        df_line_color=None,
        dx_label=None,
        df_label=None,
        include_secant_line=True,
        secant_line_color=None,
        secant_line_length=10,
    ):
        """
        Resulting group is of the form VGroup(
            dx_line,
            df_line,
            dx_label, (if applicable)
            df_label, (if applicable)
            secant_line, (if applicable)
        )
        with attributes of those names.
        """
        kwargs = locals()
        kwargs.pop("self")
        group = VGroup()
        group.kwargs = kwargs

        dx = dx or float(self.x_max - self.x_min) / 10
        dx_line_color = dx_line_color or self.default_input_color
        df_line_color = df_line_color or graph.get_color()

        p1 = self.input_to_graph_point(x, graph)
        p2 = self.input_to_graph_point(x + dx, graph)
        interim_point = p2[0] * RIGHT + p1[1] * UP

        group.dx_line = Line(
            p1, interim_point,
            color=dx_line_color
        )
        group.df_line = Line(
            interim_point, p2,
            color=df_line_color
        )
        group.add(group.dx_line, group.df_line)

        labels = VGroup()
        if dx_label is not None:
            group.dx_label = TexMobject(dx_label)
            labels.add(group.dx_label)
            group.add(group.dx_label)
        if df_label is not None:
            group.df_label = TexMobject(df_label)
            labels.add(group.df_label)
            group.add(group.df_label)

        if len(labels) > 0:
            max_width = 0.8 * group.dx_line.get_width()
            max_height = 0.8 * group.df_line.get_height()
            if labels.get_width() > max_width:
                labels.set_width(max_width)
            if labels.get_height() > max_height:
                labels.set_height(max_height)

        if dx_label is not None:
            group.dx_label.next_to(
                group.dx_line,
                np.sign(dx) * DOWN,
                buff=group.dx_label.get_height() / 2
            )
            group.dx_label.set_color(group.dx_line.get_color())

        if df_label is not None:
            group.df_label.next_to(
                group.df_line,
                np.sign(dx) * RIGHT,
                buff=group.df_label.get_height() / 2
            )
            group.df_label.set_color(group.df_line.get_color())

        if include_secant_line:
            secant_line_color = secant_line_color or self.default_derivative_color
            group.secant_line = Line(p1, p2, color=secant_line_color)
            group.secant_line.scale_in_place(
                secant_line_length / group.secant_line.get_length()
            )
            group.add(group.secant_line)

        return group

    def add_T_label(self, x_val, side=RIGHT, label=None, color=WHITE, animated=False, **kwargs):
        triangle = RegularPolygon(n=3, start_angle=np.pi / 2)
        triangle.set_height(MED_SMALL_BUFF)
        triangle.move_to(self.coords_to_point(x_val, 0), UP)
        triangle.set_fill(color, 1)
        triangle.set_stroke(width=0)
        if label is None:
            T_label = TexMobject(self.variable_point_label, fill_color=color)
        else:
            T_label = TexMobject(label, fill_color=color)

        T_label.next_to(triangle, DOWN)
        v_line = self.get_vertical_line_to_graph(
            x_val, self.v_graph,
            color=YELLOW
        )

        if animated:
            self.play(
                DrawBorderThenFill(triangle),
                ShowCreation(v_line),
                Write(T_label, run_time=1),
                **kwargs
            )

        if np.all(side == LEFT):
            self.left_T_label_group = VGroup(T_label, triangle)
            self.left_v_line = v_line
            self.add(self.left_T_label_group, self.left_v_line)
        elif np.all(side == RIGHT):
            self.right_T_label_group = VGroup(T_label, triangle)
            self.right_v_line = v_line
            self.add(self.right_T_label_group, self.right_v_line)

    def get_animation_integral_bounds_change(
        self,
        graph,
        new_t_min,
        new_t_max,
        fade_close_to_origin=True,
        run_time=1.0
    ):
        curr_t_min = self.x_axis.point_to_number(self.area.get_left())
        curr_t_max = self.x_axis.point_to_number(self.area.get_right())
        if new_t_min is None:
            new_t_min = curr_t_min
        if new_t_max is None:
            new_t_max = curr_t_max

        group = VGroup(self.area)
        group.add(self.left_v_line)
        group.add(self.left_T_label_group)
        group.add(self.right_v_line)
        group.add(self.right_T_label_group)

        def update_group(group, alpha):
            area, left_v_line, left_T_label, right_v_line, right_T_label = group
            t_min = interpolate(curr_t_min, new_t_min, alpha)
            t_max = interpolate(curr_t_max, new_t_max, alpha)
            new_area = self.get_area(graph, t_min, t_max)

            new_left_v_line = self.get_vertical_line_to_graph(
                t_min, graph
            )
            new_left_v_line.set_color(left_v_line.get_color())
            left_T_label.move_to(new_left_v_line.get_bottom(), UP)

            new_right_v_line = self.get_vertical_line_to_graph(
                t_max, graph
            )
            new_right_v_line.set_color(right_v_line.get_color())
            right_T_label.move_to(new_right_v_line.get_bottom(), UP)

            # Fade close to 0
            if fade_close_to_origin:
                if len(left_T_label) > 0:
                    left_T_label[0].set_fill(opacity=min(1, np.abs(t_min)))
                if len(right_T_label) > 0:
                    right_T_label[0].set_fill(opacity=min(1, np.abs(t_max)))

            Transform(area, new_area).update(1)
            Transform(left_v_line, new_left_v_line).update(1)
            Transform(right_v_line, new_right_v_line).update(1)
            return group

        return UpdateFromAlphaFunc(group, update_group, run_time=run_time)

    def animate_secant_slope_group_change(
        self, secant_slope_group,
        target_dx=None,
        target_x=None,
        run_time=3,
        added_anims=None,
        **anim_kwargs
    ):
        if target_dx is None and target_x is None:
            raise Exception(
                "At least one of target_x and target_dx must not be None")
        if added_anims is None:
            added_anims = []

        start_dx = secant_slope_group.kwargs["dx"]
        start_x = secant_slope_group.kwargs["x"]
        if target_dx is None:
            target_dx = start_dx
        if target_x is None:
            target_x = start_x

        def update_func(group, alpha):
            dx = interpolate(start_dx, target_dx, alpha)
            x = interpolate(start_x, target_x, alpha)
            kwargs = dict(secant_slope_group.kwargs)
            kwargs["dx"] = dx
            kwargs["x"] = x
            new_group = self.get_secant_slope_group(**kwargs)
            group.become(new_group)
            return group

        self.play(
            UpdateFromAlphaFunc(
                secant_slope_group, update_func,
                run_time=run_time,
                **anim_kwargs
            ),
            *added_anims
        )
        secant_slope_group.kwargs["x"] = target_x
        secant_slope_group.kwargs["dx"] = target_dx
"""
    def setup(self):
        #self.screen_grid = NumberPlane()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords*self.space_unit_to_x,self.y_coords*self.space_unit_to_y))

        #dots,labels,numbers = self.get_all_mobs()
        #self.add(dots,labels)

    def get_dots(self,coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_dot_labels(self,dots,direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})",height=0.3)\
                      .next_to(dot,direction,buff=SMALL_BUFF) 
                      # This is called Multi-line statement, learn how to use it here:
                      # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
            ])
        return labels

    def get_dot_numbers(self,dots):
        numbers = VGroup(*[
            TextMobject(f"{n}",height=0.2).next_to(dot,DOWN,buff=SMALL_BUFF)
            for n,dot in zip(range(1,len(dots)+1),dots)
            ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots,labels,numbers
"""        
"""
class PathAsCorners(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.play(ShowCreation(path),run_time = 5)        
"""
class MOOC(GraphScene):
    CONFIG = {
        "y_max" : 4,
        "y_min" : 0,
        "x_max" : 11,
        "x_min" : -11,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,4,1),
        "x_labeled_nums": range(-10,11,1),
        "x_label_decimal":0,
        "graph_origin": 0 * DOWN + 0 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": "n",
        "x_axis_width":10
    }

    def construct(self):
        #text1 = TextMobject("DTFT of 2 Convolved Discrete Time Signals").scale(1.3)
        #text1.set_color(YELLOW)
        #self.play(Write(text1),run_time = 3)
        #self.wait(3)
        #self.play(FadeOut(text1)) 
        # text2 = TextMobject("What is Convolution?")
        # text2.to_edge(UP)
        # text2.set_color(RED)
        # self.play(Write(text2),run_time = 2)
        # self.wait(3)
        # text3 = TextMobject("{Convolution is a mathematical operation on two signals.Since we are dealing with Discrete Signals, the Convolution of both signals is also discrete. It can be obtained by using following formulae,}").scale(0.8)
        # text3.next_to(text2,DOWN,buff=1)
        # text3.set_color(BLUE)
        # self.play(Write(text3),run_time = 2)
        # self.wait(3)
        # text4 = TexMobject("(f*g)[n] = \sum_{m=-\infty}^{\infty}{f[n-m]g[m]}")
        # text4.set_color(BLUE)
        # self.play(Write(text4),run_time = 2)
        # self.wait(3)       

        self.setup_axes(animate=True) #animate=True to add animation
        #x = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        #y = np.heaviside(x,0.5)
        #graph1 = self.get_graph(y, color = GREEN, x_min = -1, x_max = 1)
        #graph1 = self.get_graph(lambda x : 0, color = RED,x_max = 0)
        #graph2 = Line(DOWN,UP)
        #graph3 = self.get_graph(lambda x : 1, color = RED,x_min = 0)
        #self.play(ShowCreation(graph),run_time = 2)
        #self.play(ShowCreation(graph2),run_time = 2)
        #self.wait()
        rect_func = VMobject()
        rect_func.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        VGroup(rect_func).set_color(RED)
        #self.play(ShowCreation(rect_func),run_time = 2)
        path1 = self.get_graph(lambda x: np.heaviside(x+1,1)-np.heaviside(x-2,1),x_min = -10,x_max = 10)
        path2 = self.get_graph(lambda x: np.piecewise(x,[x<-2,x==-2,(x>-2)&(x<0),x==0,(x>0)&(x<2),x==2,x>2],[0,0,x+2,2,-x+2,0,0]),x_min = -10,x_max = 10)
        FT_rect_function = self.get_graph(lambda x: 2*np.sinc(2*x),color = WHITE,x_min = -10,x_max = 10)
        #self.play(ShowCreation(FT),run_time = 2)
        Discrete_rect_func = self.get_vertical_lines_to_graph(path1,color = RED,x_min = -10,x_max = 10,num_lines = 21)
        Discrete_triangle_func = self.get_vertical_lines_to_graph(path2,color = YELLOW,x_min = -10,x_max = 10,num_lines = 21)
        triangle_part1 = VMobject()
        triangle_part1.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_triangle_part1]])
        VGroup(triangle_part1).set_color(YELLOW)     
        triangle_part2 = VMobject()
        triangle_part2.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_triangle_part2]])
        VGroup(triangle_part2).set_color(YELLOW)
        triangle_part3 = VMobject()
        triangle_part3.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_triangle_part3]])
        VGroup(triangle_part3).set_color(YELLOW)
        triangle_part4 = VMobject()
        triangle_part4.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_triangle_part4]])
        VGroup(triangle_part4).set_color(YELLOW)   
        rect_func2 = VMobject()
        rect_func2.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_rect2]])
        rect_func3 = VMobject()
        rect_func3.set_points_as_corners([*[coord(x,y) for x,y in self.tuples_rect3]])        
        VGroup(rect_func2).set_color(RED)
        VGroup(rect_func3).set_color(RED)
        #self.play(ShowCreation(Discrete_rect_func),ShowCreation(path2),run_time = 10)
        #self.add(rect_func)
        dx = 0.005
        rect1 = self.get_riemann_rectangles(
                    path2,
                    x_min = -1,
                    x_max = 1,
                    dx = dx,
                    stroke_width = dx,
                )
        #self.play(ShowCreation(rect_func))
        #self.play(ShowCreation(rect_func2))
        #point1 = (7*self.space_unit_to_x)*RIGHT
        #self.play(rect_func2.shift,point1,ShowCreation(triangle_part1),run_time = 2)
        #self.wait(1)
        point2 = (2*self.space_unit_to_x)*RIGHT
        self.play(rect_func2.shift,point2,ShowCreation(triangle_part2),ShowCreation(rect1),run_time = 5)
        self.wait(1)
        point3 = (2*self.space_unit_to_x)*RIGHT
        self.play(rect_func2.shift,point3,ShowCreation(triangle_part3),Uncreate(rect1),run_time = 5)
        self.wait(1)
        #point4 = (7*self.space_unit_to_x)*RIGHT
        #self.play(rect_func2.shift,point4,ShowCreation(triangle_part4),run_time = 2)
        #self.show_area(path1)
        #self.play(ShowCreation(rect_func2))
        #Move(rect_func2,point, run_time = 3)
        #self.play(ShowCreation(rect_func3))
        
        # self.play(Transform(VGroup(rect_func2),VGroup(rect_func3)),ShowCreation(triangle_function),ShowCreation(rects),run_time = 10)
        #self.play(ShowCreation(triangle_function),run_time = 5)
