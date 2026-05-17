from manim import *
import numpy as np

class Force(Scene):
    def construct(self):
        # Background grid
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1]).fade(0.8)
        self.add(plane)

        
        s1 = Tex(r"Total momentum conserved:", font_size=26).move_to([-4.2, 2.5, 0])
        s2 = MathTex(r"\vec{p}_1 + \vec{p}_2 = \text{constant}", font_size=30).move_to([-4.2, 1.8, 0])
        
        s3 = Tex(r"Change in total is zero:", font_size=26).move_to([-4.2, 0.8, 0])
        s4 = MathTex(r"\Delta\vec{p}_1 + \Delta\vec{p}_2 = 0", font_size=30).move_to([-4.2, 0.1, 0])
        
        s5 = Tex(r"Momentums are opposite:", font_size=26).move_to([-4.2, -0.9, 0])
        s6 = MathTex(r"\Delta\vec{p}_1 = -\Delta\vec{p}_2", font_size=30).move_to([-4.2, -1.6, 0])

        
        
        c = Circle(radius=0.4, color=BLUE, fill_opacity=0.5).move_to([1.5, 0, 0])
        r = Circle(radius=0.4, color=RED, fill_opacity=0.5).move_to([3.5, 0, 0])
        self.add(c, r)

       
        p1_arrow = Arrow([1.5, 0.5, 0], [3.5, 0.5, 0], color=BLUE, buff=0)
        p1_label = MathTex(r"\vec{p}_1", font_size=30, color=BLUE).next_to(p1_arrow, UP)

        
        p2_arrow = Arrow([3.5, -0.5, 0], [4.0, -0.5, 0], color=RED, buff=0)
        p2_label = MathTex(r"\vec{p}_2 = 0", font_size=30, color=RED).next_to(p2_arrow, DOWN)

        

        
        self.play(Create(p1_arrow), Write(p1_label), Create(p2_arrow), Write(p2_label), run_time=1.5)
        self.wait(2.5)

        
        p1_arrow_new = Arrow([1.5, 0.5, 0], [2.2, 0.5, 0], color=BLUE, buff=0)
        p2_arrow_new = Arrow([3.5, -0.5, 0], [5.5, -0.5, 0], color=RED, buff=0)
        p2_label_new = MathTex(r"\vec{p}_2", font_size=30, color=RED).next_to(p2_arrow_new, DOWN)

        self.play(
            c.animate.move_to([2.8, 0, 0]),
            r.animate.move_to([4.8, 0, 0]),
            Transform(p1_arrow, p1_arrow_new),
            Transform(p2_arrow, p2_arrow_new),
            Transform(p2_label, p2_label_new),
            run_time=3
        )
        self.wait(0.5)

        
        self.play(Write(s1), Write(s2), run_time=1.9)
        self.play(Write(s3), Write(s4), run_time=1.9)
        self.play(Write(s5), Write(s6), run_time=1.9)
        self.wait(15)

       
        self.play(
            FadeOut(c), FadeOut(r),
            FadeOut(p1_arrow), FadeOut(p1_label),
            FadeOut(p2_arrow), FadeOut(p2_label),
            FadeOut(s1), FadeOut(s2), FadeOut(s3), 
            FadeOut(s4), FadeOut(s5), FadeOut(s6),
            run_time=1.5
        )
        self.wait(1.5)

        
        step_1 = MathTex(r"\Delta\vec{p}_1 = -\Delta\vec{p}_2", font_size=36).move_to([0, 2, 0])
        
       
        step_2_txt = Tex(r"Divide by the impact time ($\Delta t$):", font_size=30).move_to([0, 0.8, 0])
        step_2_math = MathTex(r"\frac{\Delta\vec{p}_1}{\Delta t} = -\frac{\Delta\vec{p}_2}{\Delta t}", font_size=40).move_to([0, -0.2, 0])
        
        step_3_txt = Tex(r"Apply Newton's 2nd Law ($\vec{F} = \frac{\Delta\vec{p}}{\Delta t}$):", font_size=30).move_to([0, -1.4, 0])
        step_3_math = MathTex(r"\therefore \vec{F}_1 = -\vec{F}_2", font_size=44, color=YELLOW).move_to([0, -2.6, 0])

       
        self.play(Write(step_1), run_time=1.5)
        self.wait(21)
        
        self.play(Write(step_2_txt), run_time=1.5)
        self.play(Write(step_2_math), run_time=1.5)
        self.wait(2)
        
        self.play(Write(step_3_txt), run_time=1.5)
        self.play(Write(step_3_math), run_time=1.5)
        self.wait(2)
        
        box = SurroundingRectangle(step_3_math, color=YELLOW, buff=0.3)
        self.play(Create(box), run_time=1.5)
        self.wait(40)