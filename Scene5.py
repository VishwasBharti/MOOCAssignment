from manimlib.imports import *
def coord(x,y,z=0):
	return np.array([x,y,z])
class Scene5(GraphScene, Scene, CoordinateSystem):
	def construct(self):
		intro_text = TextMobject("We can observe that there is duality between multiplication and convolution in time domain and frequency domain.")
		intro_text.set_color(BLUE)
		intro_text.to_edge(UP)
		self.add_sound("background_music.mp3", gain = -2)
		self.add_sound("Scene5_p1.wav", gain = 10)
		self.wait(2)
		self.play(ShowCreation(intro_text.scale(0.6)))
		self.wait(10)
		convolution = TexMobject(r"\frac{ 1 }{ 2\pi } \int_{-\pi}^{\pi} X_{ 1 }(\nu) X_{ 2 }(\omega - \nu) d\nu ")
		convolution.move_to(ORIGIN)
		convolution.set_color(GREEN)
		self.play(ShowCreation(convolution))
		self.wait(7)
		PI = 3
		axis1 = Axes(
			x_min = -3*PI,
			x_max = 3*PI,
			y_min = -1,
			y_max = 2,
			x_axis_label = "$\\omega$",
			axes_color = GREY_BROWN,
			x_labelled_nums = ["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "$0$", "$\\pi$", "$2\\pi$", "$3\\pi$"],
			y_labelled_nums = [-1,2],
			center_point = ORIGIN,
			x_axis_config={
				"unit_size": 1,
				"tick_frequency": PI,
				"include_tip": False,
				"label_direction": DOWN+0.5*LEFT
			},
			y_axis_config={
					"unit_size": 1,
					"tick_frequency": 1,
					"include_tip": False,
			})
		ylabels_axis1 = axis1.get_y_axis().get_number_mobjects(*[-1,2])
		xlabels_axis1 = ["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "$0$", "$\\pi$", "$2\\pi$", "$3\\pi$"]
		coords_axis1 = [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0]]
		xlabels_axis1_group = VGroup(*[TextMobject(f"{round(x)}$\\pi$", font = "Times", stroke_width = 0, color = GREEN).next_to([x*PI,y*PI,0], DOWN) for x,y in coords_axis1])

		axis2 = Axes(
			x_min = -3*PI,
			x_max = 3*PI,
			y_min = -1,
			y_max = 2,
			x_axis_label = "$\\omega$",
			axes_color = GREY_BROWN,
			x_labelled_nums = ["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "$0$", "$\\pi$", "$2\\pi$", "$3\\pi$"],
			y_labelled_nums = [-1,2],
			center_point = ORIGIN,
			x_axis_config={
				"unit_size": 1,
				"tick_frequency": PI,
				"include_tip": False,
				"label_direction": DOWN+0.5*LEFT
			},
			y_axis_config={
					"unit_size": 1,
					"tick_frequency": 1,
					"include_tip": False,
			})
		ylabels_axis2 = axis2.get_y_axis().get_number_mobjects(*[-1,2])
		xlabels_axis2 = ["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "$0$", "$\\pi$", "$2\\pi$", "$3\\pi$"]
		coords_axis2 = [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0]]
		xlabels_axis2_group = VGroup(*[TextMobject(f"{round(x)}$\\pi$", font = "Times", stroke_width = 0, color = GREEN).next_to([x*PI,y*PI,0], DOWN) for x,y in coords_axis2])

		#self.play(ShowCreation(axis1.scale(0.6)), ShowCreation(xlabels_axis1_group.scale(0.6)))
		#self.wait()
		sf = 0.6 #scaling factor
		x_coords = np.array([-3*PI, -9*PI/4, -9*PI/4, -7*PI/4, -7*PI/4, -PI/4, -PI/4, PI/4, PI/4, 7*PI/4, 7*PI/4, 9*PI/4, 9*PI/4, 3*PI])
		y_coords = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0])
		tuples = list(zip(x_coords, y_coords))
		X_w = VMobject()
		X_w.set_points_as_corners([*[coord(x,y) for x,y in tuples]])
		VGroup(X_w).set_color(RED)
		x_coords_part = np.array([-3*PI, -9*PI/4, -9*PI/4, -7*PI/4, -7*PI/4, -PI/4, -PI/4, PI/4, PI/4, 7*PI/4, 7*PI/4, 9*PI/4, 9*PI/4, 3*PI])
		y_coords_part = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0])
		tuples_part = list(zip(x_coords_part, y_coords_part))
		X_w_2 = VMobject()
		X_w_2.set_points_as_corners([*[coord(x,y) for x,y in tuples_part]])
		X_w_2.set_color(BLUE)
		Dots_array = [[-PI, 0, 0], [-PI/4, 0, 0], [0, 0, 0], [PI/4, 0, 0], [PI, 0, 0]]
		w_minuspi = TextMobject("$\\omega - \\pi$", color = YELLOW).next_to([-PI, 0, 0], UP)
		w_minuspi.scale(sf)
		w_minuspiby4 = TextMobject("$\\omega - \\pi/4$", color = YELLOW).next_to([-PI/4, 0, 0], UP)
		w_minuspiby4.scale(sf)
		#w_minuspiby4.rotate(np.pi/2, about_point = [-PI/4, 0, 0])
		w = TextMobject("$\\omega$", color = YELLOW).next_to([0, 0, 0], UP)
		w.scale(sf)
		#w.rotate(np.pi/2, about_point = [0, 0, 0])
		w_pluspiby4 = TextMobject("$\\omega + \\pi/4$", color = YELLOW).next_to([PI/4, 0, 0], UP)
		w_pluspiby4.scale(sf)
		#w_pluspiby4.rotate(np.pi/2, about_point = [PI/4, 0, 0])
		w_pluspi = TextMobject("$\\omega + \\pi$", color = YELLOW).next_to([PI, 0, 0], UP)
		w_pluspi.scale(sf)

		w_plus2pi = TextMobject("$\\omega + 2\\pi$", color = YELLOW).next_to([2*PI, 0, 0], UP)
		w_plus2pi.scale(sf)

		w_plus3pi = TextMobject("$\\omega + 3\\pi$", color = YELLOW).next_to([3*PI, 0, 0], UP)
		w_plus3pi.scale(sf)
		
		w_minus2pi = TextMobject("$\\omega - 2\\pi$", color = YELLOW).next_to([-2*PI, 0, 0], UP)
		w_minus2pi.scale(sf)
		
		w_minus3pi = TextMobject("$\\omega - 3\\pi$", color = YELLOW).next_to([-3*PI, 0, 0], UP)
		w_minus3pi.scale(sf)

		#Dots_label = VGroup(w_minuspi, w_minuspiby4, w, w_pluspiby4, w_pluspi)
		#Dots_label.set_color(YELLOW)
		#Dots_label.move_to(2*DOWN)	`1`
		Dots = VGroup(*[Dot(v) for v in Dots_array])
		X_w_part = VGroup(X_w_2, Dots,w_minus3pi,w_minus2pi, w_minuspi, w_minuspiby4, w, w_pluspiby4, w_pluspi, w_plus2pi, w_plus3pi)
		X_w_part.move_to(2*DOWN)
				

		##triangle part
		tri_part1 = VMobject()
		tri_part2 = VMobject()
		tri_part3 = VMobject()
		tri_part4 = VMobject()
		tri_part1_x = np.array([-PI,-PI/2])
		tri_part1_y = np.array([0,0])
		tri_part1_tuples = list(zip(tri_part1_x, tri_part1_y))
		tri_part1.set_points_as_corners([*[coord(x,y) for x,y in tri_part1_tuples]])
		tri_part1.set_color(YELLOW)
		#tri_part1.shift(2*UP)

		tri_part2_x = np.array([-PI/2,0])
		tri_part2_y = np.array([0,PI/2])
		tri_part2_tuples = list(zip(tri_part2_x, tri_part2_y))
		tri_part2.set_points_as_corners([*[coord(x,y) for x,y in tri_part2_tuples]])
		tri_part2.set_color(YELLOW)
		#tri_part2.shift(2*UP)

		tri_part3_x = np.array([0,PI/2])
		tri_part3_y = np.array([PI/2,0])
		tri_part3_tuples = list(zip(tri_part3_x, tri_part3_y))
		tri_part3.set_points_as_corners([*[coord(x,y) for x,y in tri_part3_tuples]])
		tri_part3.set_color(YELLOW)
		#tri_part3.shift(2*UP)

		tri_part4_x = np.array([PI/2,PI])
		tri_part4_y = np.array([0,0])
		tri_part4_tuples = list(zip(tri_part4_x, tri_part4_y))
		tri_part4.set_points_as_corners([*[coord(x,y) for x,y in tri_part4_tuples]])
		tri_part4.set_color(YELLOW)
		#tri_part4.shift(2*UP)
		tri_all = VGroup(tri_part1, tri_part2, tri_part3, tri_part4)

		group_1 = VGroup(axis1, xlabels_axis1_group, X_w, tri_all)
		X_w_2 = X_w.copy()
		group_2 = VGroup(axis2, xlabels_axis2_group, X_w_2)

		##convolution text 
		part1 = TexMobject(r"for \omega \in [-\pi, -\pi/2], \quad \frac { 1 }{ 2\pi  } \int _{ -\pi  }^{ -\pi/2  }{ X(\nu ) } { X(\omega - \nu) }d\nu = 0")
		part1.move_to(2*UP)
		part2 = TexMobject(r"for \omega \in [-\pi/2, 0], \quad \frac { 1 }{ 2\pi  } \int _{ -\pi/4  }^{ \omega+\pi/4  }{ 1 }\times { 1 }d\nu = \frac{ 1 }{ 2\pi }(\omega + \pi/2)").next_to(part1, DOWN)
		part3 = TexMobject(r"for \omega \in [0, \pi/2], \quad \frac { 1 }{ 2\pi  } \int _{ \omega-\pi/4  }^{ \pi/4  }{ 1 }\times { 1 }d\nu = \frac{ 1 }{ 2\pi }(\pi/2 - \omega)").next_to(part2, DOWN)
		part4 = TexMobject(r"for \omega \in [\pi/2, \pi], \quad \frac { 1 }{ 2\pi  } \int _{ \pi/2  }^{ +\pi  }{ X(\nu ) }\times { X(\omega - \nu) }d\nu = 0").next_to(part3, DOWN)

		part_all = VGroup(part1, part2, part3, part4)
		part_all.set_color(BLUE)
		part_all.scale(sf)
		part_all.shift(DOWN)
		self.remove(intro_text)
		group_1.move_to(2*UP)
		group_1.scale(sf)
		group_2.move_to(2*DOWN)
		X1 = TexMobject(r"X_{ 1 }(\omega)")
		X1_nu = TexMobject(r"X_{ 1 }(\nu)")
		X1_nu.set_color(GREEN)
		X_w.set_color(GREEN)
		X2 = TexMobject(r"X_{ 2 }(\omega)")
		X2_nu = TexMobject(r"X_{ 2 }(\nu)")
		X2_nu.set_color(BLUE)
		X2_minus_nu = TexMobject(r"X_{ 2 }(-\nu)")
		X2_minus_nu.set_color(BLUE)
		X2_minus_nu.move_to(ORIGIN)
		X2_nu_omega = TexMobject(r"X_{ 2 }(\omega - \nu)")
		X2_nu_omega.set_color(BLUE)
		X2_nu_omega.move_to(ORIGIN)
		X_w_2.set_color(BLUE)
		X1.to_edge(UP)
		X1_nu.to_edge(UP)
		X1.set_color(RED)
		X2.move_to(ORIGIN)
		X2_nu.move_to(ORIGIN)
		X2.set_color(RED)
		self.remove(convolution)
		self.play(ShowCreation(axis1), ShowCreation(xlabels_axis1_group), ShowCreation(X_w), ShowCreation(group_2.scale(sf)), ShowCreation(X1), ShowCreation(X2))
		self.wait(7)
		self.add_sound("Scene5_p2.wav", gain =10)
		self.wait(22)
		self.play(ReplacementTransform(X1, X1_nu), FadeIn(X_w))
		self.wait(8)
		self.play(ReplacementTransform(X2, X2_nu), FadeIn(X_w_2))
		self.wait(2)
		self.play(ReplacementTransform(X2_nu, X2_minus_nu))
		origin_dot = Dot([0,-2.5,0], radius = 0.01)
		X_w_3 = X_w_2.copy()
		self.play(ReplacementTransform(X_w_2, origin_dot))
		self.play(ReplacementTransform(origin_dot, X_w_3))
		self.wait(10)
		self.remove(xlabels_axis2_group)
		self.play(ShowCreation(X_w_part.scale(sf)), ReplacementTransform(X2_minus_nu, X2_nu_omega))
		self.wait(15)
		self.play(X_w_part.shift, 4*UP+PI*sf*LEFT)
		#path1 = axis1.get_graph(lambda x: np.piecewise(x,[x<-PI/4,(x>=-PI/4)&(x<=PI/4),x>PI/4],[0,1,0]),x_min = -PI,x_max = PI)
		self.remove(group_2, origin_dot, axis2, X2_nu_omega, X1_nu, X_w_3)

		rect_num = 50
		rect_width = float(PI/(2*rect_num))
		rect_color = BLUE
		rect_opacity = 1
		x_temp = range(0,int(rect_num/2))
		x_coord_right = [rect_width/2+i*rect_width for i in x_temp]
		x_coord_left = [-(rect_width/2+(int(rect_num/2)-1-i)*rect_width) for i in x_temp]
		x_coord = x_coord_left + x_coord_right
		rectangles = VGroup(*[Rectangle(width = rect_width, height = 1, fill_color = rect_color, fill_opacity = rect_opacity).move_to([x,0.5,0]) for x in x_coord])
		rectangles.move_to(2*UP)
		self.wait(8)
		self.play(X_w_part.shift, (sf*PI/2)*RIGHT, ShowCreation(tri_part1), ShowCreation(part1), run_time = 3)
		self.play(X_w_part.shift, (sf*PI/2)*RIGHT, ShowCreation(rectangles.scale(sf)), ShowCreation(tri_part2), ShowCreation(part2), run_time = 2)
		rectangles2 = rectangles.copy()
		rectangles2.set_fill(BLACK)
		rectangles2.set_stroke(BLACK)
		self.play(X_w_part.shift, (sf*PI/2)*RIGHT, ShowCreation(rectangles2.scale(0.9)), ShowCreation(tri_part3), ShowCreation(part3), run_time = 2)
		self.play(X_w_part.shift, (sf*PI/2)*RIGHT, ShowCreation(tri_part4), ShowCreation(part4), run_time = 3)
		self.remove(rectangles, rectangles2)
		self.wait(2)
		self.add_sound("Scene5_p3.wav", gain = 10)
		self.wait(60)
