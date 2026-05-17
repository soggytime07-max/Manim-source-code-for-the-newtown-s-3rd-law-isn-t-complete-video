from manim import *

class Noether(Scene):

    def construct(self):


        title = Tex(
            r"So what connects all of this?",
            font_size=42, color=YELLOW
        ).move_to([0, 3.2, 0])

        self.play(Write(title), run_time=1.5)
        self.wait(0.5)

        
        n1 = Tex(
            r"Noether's Theorem:",
            font_size=38, color=GREEN
        ).move_to([0, 2.0, 0])

        n2 = Tex(
            r"Every continuous symmetry of a system",
            font_size=32
        ).move_to([0, 1.2, 0])

        n3 = Tex(
            r"corresponds to exactly one conserved quantity.",
            font_size=32
        ).move_to([0, 0.5, 0])

        box_noether = SurroundingRectangle(
            VGroup(n1, n2, n3),
            color=GREEN, buff=0.3
        )

        self.play(Write(n1), run_time=1.2)
        self.play(Write(n2), Write(n3), run_time=2)
        self.play(Create(box_noether), run_time=1)
        self.wait(2)

        row1 = Tex(
            r"Translational symmetry $\longrightarrow$ Momentum conservation $\longrightarrow$ Newton's 3rd",
            font_size=26, color=WHITE
        ).move_to([0, -0.5, 0])

        row2 = Tex(
            r"Rotational symmetry $\longrightarrow$ Angular momentum conservation",
            font_size=26, color=WHITE
        ).move_to([0, -1.1, 0])

        row3 = Tex(
            r"Time translation symmetry $\longrightarrow$ Energy conservation",
            font_size=26, color=WHITE
        ).move_to([0, -1.7, 0])

        self.play(Write(row1), run_time=1.5)
        self.play(Write(row2), run_time=1.5)
        self.play(Write(row3), run_time=1.5)
        self.wait(8)

       
        self.play(
            FadeOut(title), FadeOut(n1), FadeOut(n2), FadeOut(n3),
            FadeOut(box_noether), FadeOut(row1), FadeOut(row2), FadeOut(row3),
            run_time=1.5
        )
        self.wait(1)

        a1 = Tex(
            r"Newton's 1st Law:",
            font_size=38, color=BLUE
        ).move_to([0, 2.8, 0])

        a2 = Tex(
            r"Valid within a perfect inertial frame.",
            font_size=30
        ).move_to([0, 2.0, 0])

        a3 = Tex(
            r"The universe doesn't always provide one.",
            font_size=30, color=RED
        ).move_to([0, 1.3, 0])

        divider = Tex(
            r"$\updownarrow$ \ Same structure",
            font_size=32, color=YELLOW
        ).move_to([0, 0.5, 0])

        b1 = Tex(
            r"Noether's Theorem:",
            font_size=38, color=GREEN
        ).move_to([0, -0.3, 0])

        b2 = Tex(
            r"Valid when the universe satisfies the symmetry.",
            font_size=30
        ).move_to([0, -1.0, 0])

        b3 = Tex(
            r"The universe doesn't always do that either.",
            font_size=30, color=RED
        ).move_to([0, -1.7, 0])

        self.play(Write(a1), run_time=1)
        self.play(Write(a2), Write(a3), run_time=2)
        self.play(Write(divider), run_time=1)
        self.play(Write(b1), run_time=1)
        self.play(Write(b2), Write(b3), run_time=2)
        self.wait(5)

        self.play(
            FadeOut(a1), FadeOut(a2), FadeOut(a3),
            FadeOut(divider), FadeOut(b1), FadeOut(b2), FadeOut(b3),
            run_time=2.5
        )
        self.wait(0.3)

        
        c1 = Tex(
            r"These laws are \textbf{local}, not global.",
            font_size=40, color=YELLOW
        ).move_to([0, 2.5, 0])

        c2 = Tex(
            r"In your lab, translational symmetry holds.",
            font_size=30
        ).move_to([0, 1.5, 0])

        c3 = Tex(
            r"Momentum is conserved. Newton's 3rd works.",
            font_size=30
        ).move_to([0, 0.8, 0])

        c4 = Tex(
            r"But the universe is expanding.",
            font_size=32, color=RED
        ).move_to([0, -0.2, 0])

        c5 = Tex(
            r"Space is not static. Time breaks the symmetry.",
            font_size=30, color=RED
        ).move_to([0, -0.9, 0])

        c6 = Tex(
            r"Time translation symmetry fails globally.",
            font_size=30, color=RED
        ).move_to([0, -1.6, 0])

        c7 = Tex(
            r"Energy is not conserved across the universe.",
            font_size=30, color=RED
        ).move_to([0, -2.3, 0])

        self.play(Write(c1), run_time=1.2)
        self.play(Write(c2), Write(c3), run_time=2)
        self.wait(2.5)
        self.play(Write(c4), run_time=1)
        self.play(Write(c5), Write(c6), run_time=2)
        self.play(Write(c7), run_time=1.5)
        self.wait(15)

        self.play(
            FadeOut(c1), FadeOut(c2), FadeOut(c3),
            FadeOut(c4), FadeOut(c5), FadeOut(c6), FadeOut(c7),
            run_time=1.5
        )
        self.wait(0.3)


        end1 = Tex(
            r"Newton's 3rd is not fundamental.",
            font_size=36
        ).move_to([0, 1.5, 0])

        end2 = Tex(
            r"Momentum conservation is.",
            font_size=36
        ).move_to([0, 0.7, 0])

        end3 = Tex(
            r"Symmetry is.",
            font_size=44, color=YELLOW
        ).move_to([0, -0.3, 0])

        end4 = Tex(
            r"locally.",
            font_size=36, color=RED
        ).move_to([0, -1.3, 0])

        box_end = SurroundingRectangle(end3, color=YELLOW, buff=0.3)

        self.play(Write(end1), run_time=1.2)
        self.play(Write(end2), run_time=1.2)
        self.play(Write(end3), run_time=1.2)
        self.play(Create(box_end), run_time=1)
        self.play(Write(end4), run_time=1.5)
        self.wait(3)