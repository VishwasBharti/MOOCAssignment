from manimlib.imports import *
class Scene2(GraphScene, Scene):
	CONFIG = {
        "y_max" : 3,
        "y_min" : -1,
        "x_max" : 11,
        "x_min" : -11,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 

        "y_labeled_nums": list(range(0,5)),
        "x_labeled_nums": list(range(-10,11)),
        "x_label_decimal":0,
        "graph_origin": -3 * DOWN + 0 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": "n",
        "x_axis_width":10
    }
	def construct(self):
		heading = TextMobject("\\textsc{LSI(Linear Shift-Invariant) System}")
		heading.to_edge(UP)
		heading.set_color(GOLD_A)
		linearity_text = TextMobject("Linearity")
		linearity_text.next_to(heading, DOWN+LEFT)
		linearity_text.set_color(GOLD_B)
		x1_eq = TexMobject(r"{ x }_{ 1 }[n]\xrightarrow {  } { y }_{ 1 }[n]")
		x1_eq.next_to(heading, DOWN)
		x1_eq.set_color(BLUE)
		x2_eq = TexMobject(r"{ x }_{ 2 }[n]\xrightarrow {  } { y }_{ 2 }[n]")
		x2_eq.next_to(x1_eq, DOWN)
		x2_eq.set_color(BLUE)
		linearity_eq = TexMobject(r"\alpha { x }_{ 1 }[n]+\beta { x }_{ 2 }[n]\xrightarrow {  } { \alpha y }_{ 1 }[n]+{ \beta y }_{ 2 }[n]")
		linearity_eq.next_to(x2_eq, DOWN)
		linearity_eq.set_color(TEAL_A)
		linearity_eq_2 = TexMobject(r"2 { x }_{ 1 }[n]- { x }_{ 2 }[n]\xrightarrow {  } { 2 y }_{ 1 }[n]-{  y }_{ 2 }[n]")
		linearity_eq_2.next_to(x2_eq, DOWN)
		linearity_eq_2.set_color(TEAL_A)
		axis1 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$x_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*RIGHT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis1 = axis1.scale(0.5)
		axis1.move_to(3*LEFT)
		xlabels_axis1 = axis1.get_x_axis().get_number_mobjects(*list(range(-4,5)))
		ylabels_axis1 = axis1.get_y_axis().get_number_mobjects(*[-1,1])

		discrete_input_signal_x_val = np.array(range(-4,5))
		discrete_input_signal_y_val = [(np.sinc(x)+np.sin(x)+(np.cos(x))**2)/2 for x in range(-4,5)]
		discrete_input_signal_y_val_s = [(np.sinc(x)+np.sin(x)+(np.cos(x))**2) for x in range(-4,5)]
		dots_input, lines_input = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = BLUE)
		dots_input_group = VGroup(*dots_input)
		lines_input_group = VGroup(*lines_input)
		dots_input_s, lines_input_s = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val_s, myaxes = axis1, mycolor = BLUE)
		dots_input_group_s = VGroup(*dots_input_s)
		lines_input_group_s = VGroup(*lines_input_s)
		axis2 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$y_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*LEFT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis3 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$y_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*LEFT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis4 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$y_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*LEFT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis5 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$y_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*LEFT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis6 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
		    y_axis_label = "$y_1[n]$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-5,5)),
		    y_labelled_nums = [-1,1],
		    center_point = DOWN+3*LEFT,
		    x_axis_config={
		        "unit_size": 1,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 1.2,
		            "tick_frequency": 1,
		            "include_tip": False,
		            "label_direction": UP
		    })
		axis2 = axis2.scale(0.5)
		axis3 = axis3.scale(0.5)
		axis4 = axis4.scale(0.5)
		axis5 = axis5.scale(0.5)
		axis6 = axis6.scale(0.5)
		axis2.move_to(3*RIGHT)
		axis3.move_to(3*LEFT+1.5*DOWN)
		axis4.move_to(3*RIGHT+1.5*DOWN)
		axis5.move_to(3*LEFT+3*DOWN)
		axis6.move_to(3*RIGHT+3*DOWN)
		xlabels_axis2 = axis2.get_x_axis().get_number_mobjects(*list(range(-4,5)))
		ylabels_axis2 = axis2.get_y_axis().get_number_mobjects(*[-1,1])

		discrete_input_signal_x_val_2 = np.array(range(-4,5))
		discrete_input_signal_y_val_2 = [(np.sinc(x)+np.sin(x))/2 for x in range(-4,5)]
		discrete_input_signal_y_val_2_s = [(np.sinc(x)+np.sin(x)) for x in range(-4,5)]
		dots_input_2, lines_input_2 = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_2, myaxes = axis2, mycolor = WHITE)
		dots_input_2_s, lines_input_2_s = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_2_s, myaxes = axis2, mycolor = WHITE)
		discrete_input_signal_y_val_3 = [(np.sinc(x)+np.sin(x)+np.cos(x))/2 for x in range(-4,5)]
		dots_input_3, lines_input_3 = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_3, myaxes = axis3, mycolor = PINK)
		discrete_input_signal_y_val_3_s = [-(np.sinc(x)+np.sin(x)+np.cos(x))/2 for x in range(-4,5)]
		dots_input_3_s, lines_input_3_s = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_3_s, myaxes = axis3, mycolor = PINK)
		discrete_input_signal_y_val_4 = [(np.sinc(x)+np.sin(x)+np.tan(x))/2 for x in range(-4,5)]
		dots_input_4, lines_input_4 = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_4, myaxes = axis4, mycolor = RED_A)
		discrete_input_signal_y_val_4_s = [-(np.sinc(x)+np.sin(x)+np.tan(x))/2 for x in range(-4,5)]
		dots_input_4_s, lines_input_4_s = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_4_s, myaxes = axis4, mycolor = RED_A)
		discrete_input_signal_y_val_5_s = [(np.sinc(x)+np.sin(x)+(np.cos(x))**2)-(np.sinc(x)+np.sin(x)+np.cos(x))/2 for x in range(-4,5)]
		dots_input_5_s, lines_input_5_s = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_5_s, myaxes = axis5, mycolor = PURPLE_A)
		discrete_input_signal_y_val_6_s = [(np.sinc(x)+np.sin(x))-(np.sinc(x)+np.sin(x)+np.tan(x))/2 for x in range(-4,5)]
		dots_input_6_s, lines_input_6_s = self.get_discrete(discrete_input_signal_x_val_2, discrete_input_signal_y_val_6_s, myaxes = axis6, mycolor = PINK)
		dots_input_group_2 = VGroup(*dots_input_2)
		lines_input_group_2 = VGroup(*lines_input_2)
		dots_input_group_2_s = VGroup(*dots_input_2_s)
		lines_input_group_2_s = VGroup(*lines_input_2_s)
		dots_input_group_3 = VGroup(*dots_input_3)
		lines_input_group_3 = VGroup(*lines_input_3)
		dots_input_group_3_s = VGroup(*dots_input_3_s)
		lines_input_group_3_s = VGroup(*lines_input_3_s)
		dots_input_group_4 = VGroup(*dots_input_4)
		lines_input_group_4 = VGroup(*lines_input_4)
		dots_input_group_4_s = VGroup(*dots_input_4_s)
		lines_input_group_4_s = VGroup(*lines_input_4_s)
		dots_input_group_5_s = VGroup(*dots_input_5_s)
		lines_input_group_5_s = VGroup(*lines_input_5_s)
		dots_input_group_6_s = VGroup(*dots_input_6_s)
		lines_input_group_6_s = VGroup(*lines_input_6_s)
		shift_invariance_text = TextMobject("Shift-Invariance or Time-Invariance")
		shift_invariance_text.next_to(heading, DOWN)
		shift_invariance_text.set_color(GOLD_B)
		x_eq = TexMobject(r"{ x }[n]\xrightarrow {  } { y }[n]")
		x_eq.next_to(shift_invariance_text, DOWN)
		x_eq.set_color(BLUE)
		shift_invariance_eq = TexMobject(r"{ x }[n-D]\xrightarrow {  } { y }[n-D]")
		shift_invariance_eq.next_to(x_eq, DOWN)
		shift_invariance_eq.set_color(TEAL_A)
		shift_invariance_eq_text = TextMobject("where D is an integer")
		shift_invariance_eq_text.next_to(shift_invariance_eq, DOWN)
		shift_invariance_eq_text.set_color(TEAL_A)
		self.add_sound("Scene2.wav", gain = 10)
		self.play(ShowCreation(heading))
		self.wait(2)
		self.play(ShowCreation(linearity_text))
		self.wait(5)
		self.play(ShowCreation(x1_eq),ShowCreation(axis1), ShowCreation(axis2),ShowCreation(dots_input_group), ShowCreation(lines_input_group), ShowCreation(dots_input_group_2), ShowCreation(lines_input_group_2))
		self.wait(8)
		self.play(ShowCreation(x2_eq),ShowCreation(axis3), ShowCreation(axis4),ShowCreation(dots_input_group_3), ShowCreation(lines_input_group_3),ShowCreation(dots_input_group_4), ShowCreation(lines_input_group_4))
		self.wait(7)
		self.play(ShowCreation(linearity_eq))
		self.wait(9)
		self.play(ShowCreation(axis5), ShowCreation(axis6))
		self.remove(x1_eq,x2_eq,linearity_eq)
		self.play(FadeIn(linearity_eq_2))
		self.play(linearity_eq_2.shift,UP)
		self.wait(5)
		self.play(ReplacementTransform(dots_input_group,dots_input_group_s),ReplacementTransform(lines_input_group,lines_input_group_s))
		self.wait(3)
		self.play(ReplacementTransform(dots_input_group_2,dots_input_group_2_s),ReplacementTransform(lines_input_group_2,lines_input_group_2_s))
		self.wait(7)
		self.play(ReplacementTransform(dots_input_group_3,dots_input_group_3_s),ReplacementTransform(lines_input_group_3,lines_input_group_3_s))
		self.wait(3)
		self.play(ReplacementTransform(dots_input_group_4,dots_input_group_4_s),ReplacementTransform(lines_input_group_4,lines_input_group_4_s))
		self.wait(6)
		self.play(ReplacementTransform(dots_input_group_s,dots_input_group_5_s),ReplacementTransform(lines_input_group_s,lines_input_group_5_s), ReplacementTransform(dots_input_group_3_s,dots_input_group_5_s),ReplacementTransform(lines_input_group_3_s,lines_input_group_5_s))
		self.wait(5)
		self.play(ReplacementTransform(dots_input_group_2_s,dots_input_group_6_s),ReplacementTransform(lines_input_group_2_s,lines_input_group_6_s), ReplacementTransform(dots_input_group_4_s,dots_input_group_6_s),ReplacementTransform(lines_input_group_4_s,lines_input_group_6_s))
		self.wait(5)
		self.clear()
		#self.add_sound("Scene2_prop2.wav", gain = 10)
		self.play(ShowCreation(shift_invariance_text))
		self.wait(2)
		self.play(ShowCreation(x_eq))
		self.wait(6)
		self.play(ShowCreation(shift_invariance_eq))
		self.wait(2)
		self.play(ShowCreation(shift_invariance_eq_text))
		self.wait(2)
		self.play(ShowCreation(axis3), ShowCreation(axis4))
		self.wait(2)
		self.play(ShowCreation(dots_input_group_3), ShowCreation(lines_input_group_3), ShowCreation(dots_input_group_4), ShowCreation(lines_input_group_4))
		self.wait(3)
		self.play(dots_input_group_3.shift,0.5*RIGHT,lines_input_group_3.shift,0.5*RIGHT)
		self.wait(2)
		self.play(dots_input_group_4.shift,0.5*RIGHT,lines_input_group_4.shift,0.5*RIGHT)
		self.wait(2)
		##############################################################################################################################################################
	def to_dots(self, x_points, y_points, myaxes, mycolor=YELLOW):
	    '''
	    Converts point coordinates to Dots objects
	    '''
	    return [Dot(myaxes.coords_to_point(x_points[i], y_points[i]), color=mycolor) for i in range(len(x_points))]

	def to_lines(self, x_points, y_points, myaxes, mycolor=YELLOW):
	    '''
	    Converts point coordinates to Lines objects
	    '''
	    return [Line(myaxes.coords_to_point(x_points[i], 0), myaxes.coords_to_point(x_points[i], y_points[i]), color=mycolor, fill_opacity=0.5)\
	     for i in range(len(x_points))]

	def plot_discrete(self, x_points, y_points, myaxes, mycolor=YELLOW):
	    '''
	    Plots a discrete function with points (x_points, y_points) on myaxes.
	    '''

	    dots = self.to_dots(x_points, y_points, myaxes, mycolor)
	    lines = self.to_lines(x_points, y_points, myaxes, mycolor)
	    self.play(

	        *[AnimationGroup(
	            Animation(Mobject(), run_time=0.1*i),
	            ShowCreation(lines[i], run_time=0.5), lag_ratio=1) for i in range(len(lines))
	            ],
	        *[AnimationGroup(
	            Animation(Mobject(), run_time=0.1*i+0.5),
	            GrowFromCenter(dots[i], run_time=0.3), lag_ratio=1) for i in range(len(dots))
	            ]
	        )
	    # self.play(*[GrowFromCenter(dot) for dot in dots], run_time=0.5)
	    # self.wait(0.1)
	    return dots, lines

	def get_discrete(self, x_points, y_points, myaxes, mycolor = YELLOW):
	    '''
	    Gives dots and lines to plot
	    '''
	    dots = self.to_dots(x_points, y_points, myaxes, mycolor)
	    lines = self.to_lines(x_points, y_points, myaxes, mycolor)
	    return dots, lines