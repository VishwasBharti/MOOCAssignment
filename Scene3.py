from manimlib.imports import *
class Scene3(GraphScene, Scene):
	def construct(self):
		impulse_func = TexMobject(r"\delta[n]\quad =\quad \begin{cases} 1\quad ,\quad n=0 \\ 0\quad ,\quad otherwise \end{cases}")
		impulse_func.set_color(MAROON_A)
		impulse_func.to_edge(UP)
		general_impulse_func = TexMobject(r"\delta[n-n_{o}]\quad =\quad \begin{cases} 1\quad ,\quad n=n_{o} \\ 0\quad ,\quad otherwise \end{cases}")
		general_impulse_func.set_color(MAROON_A)
		general_impulse_func.to_edge(UP)
		axis1 = Axes(
			x_min = -10,
			x_max = 11,
			y_min = 0,
			y_max = 1,
			x_axis_label = "$n$",
		axes_color = GREY_BROWN,
			x_labelled_nums = list(range(-10,11)),
			y_labelled_nums = [-1,1],
			center_point = 2*DOWN,
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
		ylabels_axis1 = axis1.get_y_axis().get_number_mobjects(*[0,1])

		impulse_eq = TexMobject(r"{ \delta }[n]\xrightarrow {  } { h }[n]")
		impulse_eq.move_to(UP)
		impulse_eq.set_color(BLUE)
		general_impulse_eq = TexMobject(r"{ \delta }[n-k]\xrightarrow {  } { h }[n-k]")
		general_impulse_eq.next_to(impulse_eq, DOWN)
		general_impulse_eq.set_color(BLUE)		
		discrete_input_signal_x_val = np.array(range(-10,11))
		discrete_input_signal_y_val = [(np.sinc(x)) for x in range(-10,11)]
		discrete_output_signal_x_val = np.array(range(-10,11))
		discrete_output_signal_y_val = [(((0.9)**x)*np.heaviside(x, 1)) for x in range(-10,11)]
		impulse = TextMobject("$\\delta$[n]")
		impulse.set_color(YELLOW)
		impulse.move_to(1*LEFT)
		impulse_dots, impulse_lines = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = YELLOW)
		impulse_dots_lines_group = VGroup(*impulse_dots, *impulse_lines, impulse)
		impulse_dots_copy, impulse_lines_copy = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = YELLOW)
		impulse_response_dots, impulse_response_lines = self.get_discrete(discrete_output_signal_x_val, discrete_output_signal_y_val, myaxes = axis1, mycolor = TEAL_A)
		impulse_response = TextMobject("h[n]")
		impulse_response.set_color(TEAL)
		impulse_response.move_to(1*LEFT)
		impulse_response_dots_lines_group = VGroup(*impulse_response_dots, *impulse_response_lines, impulse_response)
		impulse_decomposition_text = TextMobject("Any general discrete signal can be decomposed into a linear combination of shifted impulses. In better words, any discrete signal is equal to its convolution with the impulse function.")
		impulse_decomposition_text.set_color(BLUE)
		impulse_decomposition_text.next_to(impulse_func, DOWN)
		
		discrete_input_signal_x_val = np.array(range(-10,11))
		discrete_input_signal_y_val = [(np.sinc(x)+np.sin(x)+(np.cos(x))**2)/2 for x in range(-10,11)]
		dots_input, lines_input = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = BLUE)
		dots_input_group = VGroup(*dots_input)
		lines_input_group = VGroup(*lines_input)
		dots_input2, lines_input2 = self.get_discrete(discrete_input_signal_x_val, discrete_input_signal_y_val, myaxes = axis1, mycolor = YELLOW)
		dots_input_group2 = VGroup(*dots_input2)
		lines_input_group2 = VGroup(*lines_input2)
		impulse_decomposition = TexMobject(r"x[n]\quad =\quad \sum _{ k=-\infty  }^{ \infty  }{ x[k]\delta [n-k] } = x*\delta[n]")
		impulse_decomposition.set_color(MAROON_A)
		impulse_decomposition.next_to(impulse_func, DOWN)
		impulse_eq.next_to(impulse_decomposition, DOWN)
		general_impulse_eq.next_to(impulse_eq, DOWN)
		#10_p2
		x_k_delta_n_k = TexMobject(r"{ x[k]\delta }[n-k]\xrightarrow {  } x[k]{ h }[n-k]")
		x_k_delta_n_k.set_color(TEAL_A)
		x_k_delta_n_k.next_to(general_impulse_eq, DOWN)
		final_expression = TexMobject(r"\sum _{ k=-\infty  }^{ \infty  }{ x[k]\delta [n-k] }\xrightarrow {  }\sum _{ k=-\infty  }^{ \infty  }{ x[k]h[n-k] }")
		final_expression.set_color(TEAL_A)
		final_expression.next_to(x_k_delta_n_k, DOWN)

		text1 = TextMobject("Usually this infinite sum converges. We can find out the output signal y[n] for any input signal x[n] if we know the impulse response h[n] which characterises the LSI System.")
		text1.set_color(BLUE)
		text1.to_edge(UP)
		output_expression = TexMobject(r"y[n] = \sum _{ k=-\infty  }^{ \infty  }{ x[k]h[n-k] } = x*h[n]")
		output_expression.set_color(MAROON_A)
		output_expression.next_to(text1, DOWN)

		text2 = TextMobject(" note that convolution is an operation between two sequences and not two numbers.")
		text2.set_color(BLUE)
		text2.next_to(output_expression, DOWN)

		#animation start
		self.add_sound("Scene3_p1.wav", gain = 10)
		self.add(axis1, xlabels_axis1, ylabels_axis1)
		self.wait(2)
		self.play(ReplacementTransform(impulse_dots_lines_group, impulse_response_dots_lines_group), run_time = 4)
		self.wait(8)
		#14
		self.remove(impulse_response_dots_lines_group)
		self.play(ShowCreation(impulse_func), ShowCreation(VGroup(*impulse_lines_copy)), ShowCreation(VGroup(*impulse_dots_copy)))
		self.wait()
		self.remove(impulse_eq)
		#self.play(ShowCreation(impulse_decomposition_text.scale(0.8)))
		self.remove(*impulse_dots_copy, *impulse_lines_copy)
		self.play(ShowCreation(lines_input_group), ShowCreation(dots_input_group), lag_ratio = 2, run_time = 2)
		self.play(ShowCreation(lines_input_group2), ShowCreation(dots_input_group2), lag_ratio = 2, run_time = 13)
		self.play(FadeIn(impulse_decomposition.scale(0.8)))
		self.wait(20)
		#53
		self.add_sound("Scene3_p2.wav", gain = 10)
		self.play(ReplacementTransform(impulse_func, general_impulse_func))
		self.remove(axis1, xlabels_axis1, ylabels_axis1, dots_input_group, dots_input_group2, lines_input_group, lines_input_group2)
		self.wait(2)
		self.play(ShowCreation(impulse_eq))
		self.wait(4)
		self.play(ShowCreation(general_impulse_eq))
		self.wait(7)
		self.play(ShowCreation(x_k_delta_n_k))
		self.wait(12)
		#22
		self.play(ShowCreation(final_expression))
		self.wait(20)
		self.clear()
		self.add_sound("Scene3_p3.wav", gain = 10)
		#self.play(ShowCreation(text1.scale(0.8)))
		self.play(ShowCreation(output_expression))
		#self.play(ShowCreation(text2.scale(0.8)))
		self.wait(10)
#########################################################################################################################################################
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