from manim import *
import numpy as np

class Space(Scene): 

    def s(self, x, y):
        return np.array([x * (7/8), y * (4/8), 0])

    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], y_range=[-8, 8, 1]).fade(0.8)
        self.add(plane)

        c = Circle(radius=0.48, color=BLUE, fill_opacity=0.5)
        c.move_to(self.s(-4, 0))
        r = Circle(radius=0.48, color=RED, fill_opacity=0.5)
        r.move_to(self.s(4, 0))
        self.add(c, r)

        a = Arrow(self.s(-4, 0), self.s(-4, 7), color=YELLOW, buff=0)
        b = Arrow(self.s( 4, 0), self.s( 4, 7), color=YELLOW, buff=0)
        
        ta = Tex("10AM")
        tb = Tex("10PM")
        
        ta.move_to(self.s(-4, -2)) 
        tb.move_to(self.s(4, -2))

        t  = MathTex("p_1", font_size=36).move_to(self.s(-3, 6))
        t1 = MathTex("p_2", font_size=36).move_to(self.s( 5, 6))
        
        self.wait(7)
        self.play(
            c.animate.move_to(self.s(-4, 7)),
            Create(a), Write(t),
            Write(ta),
            run_time=6
        )
        self.wait(7)
        self.play(
            Create(b), Write(t1),
            r.animate.move_to(self.s(4, 7)),
            Write(tb),
            run_time=4
        )
        self.wait(27)