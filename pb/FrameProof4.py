from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class Proof4(Scene):
    def construct(self):
        self.eq()
    def eq(self):
        font_size = 34

        # System of equations
        eqs = VGroup(
            MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S", font_size=font_size),
            MathTex("I'", "=", r"\beta S Z", "-", r"\rho I", "-", r"\delta I", "-", r"\kappa I", font_size=font_size),
            MathTex("Z'", "=", r"\rho I", "+", r"\zeta R", "-", r"\alpha S Z", "-", r"\sigma Z", font_size=font_size),
            MathTex("R'", "=", r"\delta S", "+", r"\delta I", "+", r"\alpha S Z", "-", r"\zeta R", "+", r"\gamma Q", font_size=font_size),
            MathTex("Q", "=", r"\kappa I", "+", r"\sigma Z", "-", r"\gamma Q", font_size=font_size)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)

        self.play(Write(eqs))
        self.wait(1)

        # Create flowchart boxes
        box_w, box_h = 1.8, 1.5
        S_box = Rectangle(width=box_w, height=box_h).shift(LEFT*6)
        I_box = Rectangle(width=box_w, height=box_h).shift(LEFT*3)
        Z_box = Rectangle(width=box_w, height=box_h).shift(ORIGIN)
        R_box = Rectangle(width=box_w, height=box_h).shift(RIGHT*3)
        Q_box = Rectangle(width=box_w, height=box_h).shift(DOWN*2.5)
            
        S_lbl = Text("S", font_size=font_size).move_to(S_box)
        I_lbl = Text("I", font_size=font_size).move_to(I_box)
        Z_lbl = Text("Z", font_size=font_size).move_to(Z_box)
        R_lbl = Text("R", font_size=font_size).move_to(R_box)
        Q_lbl = Text("Q", font_size=font_size).move_to(Q_box)

        boxes = VGroup(
            S_box, S_lbl,
            I_box, I_lbl,
            Z_box, Z_lbl,
            R_box, R_lbl,
            Q_box, Q_lbl
        )

        # Arrows and labels
        inflow = Arrow(S_box.get_left() + LEFT*1.5, S_box.get_left(), buff=0, stroke_width=2)
        inflow_lbl = MathTex(r"\Pi").next_to(inflow, UP)

        s_to_i = Arrow(S_box.get_right(), I_box.get_left(), buff=0, stroke_width=2)
        s_to_i_lbl = MathTex(r"\beta S Z").next_to(s_to_i, UP)

        i_to_z = Arrow(I_box.get_right(), Z_box.get_left(), buff=0, stroke_width=2)
        i_to_z_lbl = MathTex(r"\rho I").next_to(i_to_z, UP)

        z_to_r_upper = Arrow(Z_box.get_right() + UP*0.2, R_box.get_left() + UP*0.2, buff=0, stroke_width=2)
        z_to_r_upper_lbl = MathTex(r"\alpha S Z").next_to(z_to_r_upper, UP)

        r_to_z_lower = Arrow(R_box.get_left() + DOWN*0.2, Z_box.get_right() + DOWN*0.2, buff=0, stroke_width=2)
        r_to_z_lower_lbl = MathTex(r"\zeta R").next_to(r_to_z_lower, DOWN)

        s_to_r_above = VGroup(
            Line(S_box.get_top(), S_box.get_top() + UP*1.2, stroke_width=2),
            Line(S_box.get_top() + UP*1.2, R_box.get_top() + UP*1.2, stroke_width=2),
            Arrow(R_box.get_top() + UP*1.5, R_box.get_top() + DOWN*0.3, stroke_width=2)
        )
        s_to_r_above_lbl = MathTex(r"\delta S").move_to(S_box.get_top() + R_box.get_top() + UP*0.8 + RIGHT*1.2).shift(UP*0.3)

        i_to_r_below = VGroup(
            Line(I_box.get_top(), I_box.get_top() + UP*0.5, stroke_width=2),
            Line(I_box.get_top() + UP*0.5, R_box.get_top() + UP*0.5 + LEFT*0.3, stroke_width=2),
            Arrow(R_box.get_top() + UP*0.78 + LEFT*0.3, R_box.get_top() + DOWN*0.2 +LEFT*0.3, stroke_width=2)
        )
        i_to_r_below_lbl = MathTex(r"\delta I").move_to(I_box.get_top() + R_box.get_top() + UP*0.8)

        # New arrows to Q
        i_to_q = Arrow(I_box.get_bottom(), Q_box.get_left() + UP*0.1, buff=0, stroke_width=2)
        i_to_q_lbl = MathTex(r"\kappa I").next_to(i_to_q, LEFT)

        z_to_q = Arrow(Z_box.get_bottom(), Q_box.get_top(), buff=0, stroke_width=2)
        z_to_q_lbl = MathTex(r"\sigma Z").next_to(z_to_q, RIGHT)

        q_to_r = Arrow(Q_box.get_right(), R_box.get_bottom(), buff=0, stroke_width=2)
        q_to_r_lbl = MathTex(r"\gamma Q").next_to(q_to_r, DOWN)

        flowchart = VGroup(
            boxes,
            inflow, inflow_lbl,
            s_to_i, s_to_i_lbl,
            i_to_z, i_to_z_lbl,
            z_to_r_upper, z_to_r_upper_lbl,
            r_to_z_lower, r_to_z_lower_lbl,
            s_to_r_above, s_to_r_above_lbl,
            i_to_r_below, i_to_r_below_lbl,
            i_to_q, i_to_q_lbl,
            z_to_q, z_to_q_lbl,
            q_to_r, q_to_r_lbl
        )

        flowchart.move_to(eqs)

        # Animation
        self.play(ReplacementTransform(eqs, flowchart))
        self.wait(2)

        # Shrink and move down
        self.play(
            flowchart.animate.scale(0.6).to_edge(DOWN*1.1),
            run_time=1.5
        )
        self.wait(0.5)
        eqs1 = VGroup(
            MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S", font_size=font_size),
            MathTex("I'", "=", r"\beta S Z", "-", r"\rho I", "-", r"\delta I", "-", r"\kappa I", font_size=font_size),
            MathTex("Z'", "=", r"\rho I", "+", r"\zeta R", "-", r"\alpha S Z", "-", r"\sigma Z", font_size=font_size),
            MathTex("R'", "=", r"\delta S", "+", r"\delta I", "+", r"\alpha S Z", "-", r"\zeta R", "+", r"\gamma Q", font_size=font_size),
            MathTex("Q", "=", r"\kappa I", "+", r"\sigma Z", "-", r"\gamma Q", font_size=font_size)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN + UP*2).scale(0.9)
        # Show equations above
        self.play(FadeIn(eqs1, shift=UP*2))
        self.wait(2)