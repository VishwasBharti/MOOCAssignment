from manimlib.imports import *

class MOOC(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : 0,
        "x_max" : 11,
        "x_min" : -11,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,2,1),
        "x_labeled_nums": range(-10,11,1),
        "x_label_decimal":0,
        "graph_origin": 0 * DOWN + 0 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": "n",
        "x_axis_width":10
    }

    def construct(self):
        text1 = TextMobject("DTFT of 2 Convolved Discrete Time Signals").scale(1.3)
        text1.set_color(YELLOW)
        self.play(Write(text1),run_time = 3)
        self.wait(3)
        self.remove(text1) 
        text2 = TextMobject("What is Convolution?")
        text2.to_edge(UP)
        text2.set_color(RED)
        self.play(Write(text2),run_time = 2)
        self.wait(3)
        text3 = TextMobject("{Convolution is a mathematical operation on two signals.Since we are dealing with Discrete Signals, the Convolution of both signals is also discrete. It can be obtained by using following formulae,}").scale(0.8)
        text3.next_to(text2,DOWN,buff=1)
        text3.set_color(BLUE)
        self.play(Write(text3),run_time = 2)
        self.wait(3)
        text4 = TexMobject("(f*g)[n] = \sum_{m=-\infty}^{\infty}{f[n-m]g[m]}")
        text4.set_color(BLUE)
        self.play(Write(text4),run_time = 2)
        self.wait(3)       

        #self.setup_axes(animate=True) #animate=True to add animation
        #graph = self.get_graph(lambda x : x**2, color = GREEN, x_min = -10, x_max = 10)
        #self.play(ShowCreation(graph),run_time = 2)
        #self.wait()