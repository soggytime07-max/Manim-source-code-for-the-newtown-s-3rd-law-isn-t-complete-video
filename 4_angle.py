from manim import *
import numpy as np

class Rotation(Scene):

    def s(self, x, y):
        return np.array([x * (7/8), y * (4/8), 0])

    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], y_range=[-8, 8, 1]).fade(0.8)
        self.add(plane)

        
        ball = Circle(radius=0.4, color=BLUE, fill_opacity=0.5)
        ball.move_to(self.s(0, -4))
        self.add(ball)

        arrow1 = Arrow(self.s(0, -4), self.s(0, 4), color=YELLOW, buff=0)
        p1 = MathTex("p_1", font_size=36, color=YELLOW)
        p1.move_to(self.s(1.5, 0))
        self.wait(5)
        self.play(
            ball.animate.move_to(self.s(0, 4)),
            Create(arrow1), Write(p1),
            run_time=3
        )
        self.wait(5)

        # Fade ball and arrow, keep plane for rotation
        self.play(FadeOut(ball), FadeOut(arrow1),FadeOut(p1))
        self.wait(3)

        # 1st rotation
        angle_label1 = MathTex(
            r"90°\ \text{rotation}",
            font_size=32, color=GREEN
        ).move_to(self.s(0, 6))

        self.play(Write(angle_label1), run_time=0.8)
        self.play(
            Rotate(plane, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.play(FadeOut(angle_label1))
        self.wait(0.5)
       
        
        
        ball2 = Circle(radius=0.4, color=BLUE, fill_opacity=0.5)
        ball2.move_to(self.s(2.5, 0))
        self.add(ball2)

        arrow2 = Arrow(self.s(2.5, 0), self.s(-2.5, 0), color=YELLOW, buff=0)
        p2 = MathTex("p_2", font_size=36, color=YELLOW)
        p2.move_to(self.s(0, 1.5))

        self.play(
            ball2.animate.move_to(self.s(-2.5, 0)),
            Create(arrow2), Write(p2),
            run_time=3
        )
        self.wait(5)

        self.play(FadeOut(ball2), FadeOut(arrow2),FadeOut(p2))
        self.wait(0.3)

        # 2nd rotation
        angle_label2 = MathTex(
            r"90°\ \text{rotation}",
            font_size=32, color=GREEN
        ).move_to(self.s(0, 6))

        self.play(Write(angle_label2), run_time=0.8)
        self.play(
            Rotate(plane, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.play(FadeOut(angle_label2))
        self.wait(0.3)

        # --- Experiment 3 --- same experiment again
        ball3 = Circle(radius=0.4, color=BLUE, fill_opacity=0.5)
        ball3.move_to(self.s(0, -4))
        self.add(ball3)

        arrow3 = Arrow(self.s(0, -4), self.s(0, 4), color=YELLOW, buff=0)
        p3 = MathTex("p_3", font_size=36, color=YELLOW)
        p3.move_to(self.s(1.5, 0))

        self.play(
            ball3.animate.move_to(self.s(0, 4)),
            Create(arrow3), Write(p3),
            run_time=3
        )
        self.wait(5)

        # --- Payoff at top ---
        self.play(
            FadeOut(ball3), FadeOut(arrow3),
            FadeOut(plane), FadeOut(p1), FadeOut(p2), FadeOut(p3)
        )

        eq = MathTex(
            r"p_1 = p_2 = p_3",
            font_size=44, color=YELLOW
        ).move_to(self.s(0, 5))

        sub = Tex(
            r"Same physics at every orientation",
            font_size=30
        ).move_to(self.s(0, 3))

        box = SurroundingRectangle(eq, color=YELLOW, buff=0.3)

        self.play(Write(eq), run_time=1.5)
        self.play(Create(box), run_time=1)
        self.play(Write(sub), run_time=1.5)
        self.wait(19)