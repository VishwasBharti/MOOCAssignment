from manimlib.imports import *
class Scene1(GraphScene, Scene):
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
		dsp_intro = TextMobject("What is DSP?")
		asp = TextMobject("ASP(Analog Signal Processing):")
		asp.set_color(ORANGE)
		dsp_intro.set_color(YELLOW)
		dsp_intro.move_to(ORIGIN)
		image1 = ImageMobject("Scene1.png")
		image1.to_edge(DOWN)
		radio = ImageMobject("radio.png")
		radio.move_to(LEFT)
		tv = ImageMobject("tv.png")
		tv.next_to(radio, RIGHT)
		asp.move_to(5*LEFT)
		self.add_sound("background_music.mp3", gain = -2)
		self.add_sound("Scene1_p1.wav", gain = 10) 
		self.wait(1)
		self.play(ShowCreation(dsp_intro))
		self.wait(19)
		self.play(dsp_intro.shift, 3*UP, FadeIn(tv), FadeIn(radio), FadeIn(asp.scale(0.4)))
		self.wait(32)
		self.clear()
		self.play(FadeIn(image1.scale(1.8)))
		self.wait()
		self.add_sound("Scene1_p2.wav", gain = 10)
		axis1 = Axes(
		    x_min = -10,
		    x_max = 11,
		    y_min = -1,
		    y_max = 1,
		    x_axis_label = "$n$",
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-10,11)),
		    y_labelled_nums = [-1,1],
		    center_point = 2*UP,
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
		    })
		xlabels_axis1 = axis1.get_x_axis().get_number_mobjects(*list(range(-10,11)))
		ylabels_axis1 = axis1.get_y_axis().get_number_mobjects(*[-1,1])

		discrete_input_signal_x_val = np.array(range(-10,11))
		analog_input_signal_y_val = axis1.get_graph(lambda x: (np.sinc(x)+np.sin(x)+(np.cos(x))**2)/2, x_min = -10, x_max = 10)
		analog_input_signal_y_val.set_color(DARK_BLUE)
		discrete_input_signal_y_val = [(np.sinc(x)+np.sin(x)+(np.cos(x))**2)/2 for x in range(-10,11)]

		analog_output_signal_y_val = axis1.get_graph(lambda x: (np.sinc(x)+np.cos(x)+(np.sin(x))**2)/2)
		analog_output_signal_y_val.set_color(MAROON_B)
		discrete_output_signal_y_val = [(np.sinc(x)+np.cos(x)+(np.sin(x))**2)/2 for x in range(-10,11)]
		self.play(ShowCreation(axis1), ShowCreation(xlabels_axis1), ShowCreation(ylabels_axis1))
		self.play(ShowCreation(analog_input_signal_y_val))
		self.wait()
		dots_input, lines_input = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = BLUE)
		dots_input_group = VGroup(*dots_input)
		lines_input_group = VGroup(*lines_input)
		self.wait()
		self.play(ShowCreation(dots_input_group), ShowCreation(lines_input_group), run_time = 8)
		self.wait(2)
		self.remove(analog_input_signal_y_val)
		dots_output, lines_output = self.get_discrete(discrete_input_signal_x_val, discrete_output_signal_y_val, myaxes = axis1, mycolor = PINK)
		lines_output_group = VGroup(*lines_output)
		dots_output_group = VGroup(*dots_output)
		self.remove(lines_input_group)
		self.play(ReplacementTransform(dots_input_group, dots_output_group), run_time = 5)
		self.play(ShowCreation(lines_output_group))
		self.wait(24)
		self.play(ShowCreation(analog_output_signal_y_val), run_time = 6)
		self.wait(2)
		self.remove(lines_output_group, dots_output_group)
		self.wait(10)

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