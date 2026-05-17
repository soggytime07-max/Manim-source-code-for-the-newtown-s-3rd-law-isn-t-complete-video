from manim import *
import numpy as np
class force(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-6, 6, 1], y_range=[-6, 6, 1]).fade(0.8)
        c = Circle(radius = 1, color = BLUE, fill_opacity = 0.5)
        c.move_to([-4,0,0])
        r = Circle(radius = 1, color = RED, fill_opacity = 0.5)
        r.move_to([0,0,0])
        self.add(c,r)
        A = np.array([-3,2,0])
        A1 = np.array([0,2,0])
        a = Arrow(A,A1, color = YELLOW)
        B = np.array([-3,-2,0])
        B1 = np.array([0,-2,0])
        b = Arrow(B1,B, color = YELLOW)
        t = MathTex("F_1")
        t1 = MathTex("F_2")
        t.move_to([0,3,0])
        t1.move_to([0,-3,0])
        self.play(c.animate.move_to([-2.01,0,0]),Create(a),Write(t),run_time = 6)
        self.wait(1.5)
        self.play(Create(b), Write(t1),r.animate.move_to([+1.2,0,0]), run_time = 4)
        self.wait(9)