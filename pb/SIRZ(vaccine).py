from manim import *

class SIZREquationsToFlowchartFull(Scene):
    def construct(self):
        font_size = 36

        # System of equations
        eq1 = MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S + cZ", font_size=font_size)
        eq2 = MathTex("I'", "=", r"\beta S Z", "-", r"\rho I", "-", r"\delta I", font_size=font_size)
        eq3 = MathTex("Z'", "=", r"\rho I", "+", r"\zeta R", "-", r"\alpha S Z - cZ", font_size=font_size)
        eq4 = MathTex("R'", "=", r"\delta S", "+", r"\delta I", "+", r"\alpha S Z", "-", r"\zeta R", font_size=font_size)

        equations = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)
        self.play(Write(equations))
        self.wait(1)

        # Create flowchart boxes
        box_width, box_height = 1.8, 1.3
        S_box = Rectangle(width=box_width, height=box_height).shift(LEFT*4.5)
        I_box = Rectangle(width=box_width, height=box_height).shift(LEFT*1.5)
        Z_box = Rectangle(width=box_width, height=box_height).shift(RIGHT*1.5)
        R_box = Rectangle(width=box_width, height=box_height).shift(RIGHT*4.5)

        S_label = Text("S", font_size=font_size).move_to(S_box)
        I_label = Text("I", font_size=font_size).move_to(I_box)
        Z_label = Text("Z", font_size=font_size).move_to(Z_box)
        R_label = Text("R", font_size=font_size).move_to(R_box)

        boxes = VGroup(S_box, S_label, I_box, I_label, Z_box, Z_label, R_box, R_label)

        # Arrows + labels
        inflow = Arrow(S_box.get_left() + LEFT*1.5, S_box.get_left(), buff=0, stroke_width=2)
        inflow_label = MathTex(r"\Pi").next_to(inflow, UP)

        s_to_i = Arrow(S_box.get_right(), I_box.get_left(), buff=0, stroke_width=2)
        s_to_i_label = MathTex(r"\beta S Z").next_to(s_to_i, UP)

        i_to_z = Arrow(I_box.get_right(), Z_box.get_left(), buff=0, stroke_width=2)
        i_to_z_label = MathTex(r"\rho I").next_to(i_to_z, UP)

        z_to_r_upper = Arrow(Z_box.get_right() + UP*0.3, R_box.get_left() + UP*0.3, buff=0, stroke_width=2)
        z_to_r_upper_label = MathTex(r"\alpha S Z").next_to(z_to_r_upper, UP)

        r_to_z_lower = Arrow(R_box.get_left() + DOWN*0.3, Z_box.get_right() + DOWN*0.3, buff=0, stroke_width=2)
        r_to_z_lower_label = MathTex(r"\zeta R").next_to(r_to_z_lower, DOWN)

        s_to_r_above = VGroup(
            Line(S_box.get_top(), S_box.get_top() + UP*1.15, stroke_width=2),
            Line(S_box.get_top() + UP*1.15, R_box.get_top() + UP*1.15, stroke_width=2),
            Arrow(R_box.get_top() + UP*1.35, R_box.get_top() + DOWN*0.2, stroke_width=2)
        )
        s_to_r_above_label = MathTex(r"\delta S").move_to(S_box.get_top() + R_box.get_top() + UP*0.9)

        i_to_r_below = VGroup(
            Line(I_box.get_bottom(), I_box.get_bottom() + DOWN*1.2, stroke_width=2),
            Line(I_box.get_bottom() + DOWN*1.2, R_box.get_bottom() + DOWN*1.2, stroke_width=2),
            Arrow(R_box.get_bottom() + DOWN*1.4, R_box.get_bottom() + UP*0.2, stroke_width=2)
        )
        z_to_s_below = VGroup(
            Line(Z_box.get_top(), Z_box.get_top() + UP*0.8, stroke_width=2),
            Line(Z_box.get_top() + UP*0.8, S_box.get_top() + UP*0.8 + RIGHT*0.5, stroke_width=2),
            Arrow(S_box.get_top() + UP*1.1 + RIGHT*0.5, S_box.get_top() + DOWN*0.2 + RIGHT*0.5, stroke_width=2)
        )
        z_to_s_below_label = MathTex(r"c Z").move_to(Z_box.get_bottom() + S_box.get_bottom()+ UP*2.5 + RIGHT*0.5)
        i_to_r_below_label = MathTex(r"\delta I").move_to(I_box.get_bottom() + R_box.get_bottom() + DOWN*1.2).shift(DOWN*0.3)

        # Group all flowchart elements
        flowchart = VGroup(
            boxes,
            inflow, inflow_label,
            s_to_i, s_to_i_label,
            i_to_z, i_to_z_label,
            z_to_r_upper, z_to_r_upper_label,
            r_to_z_lower, r_to_z_lower_label,
            s_to_r_above, s_to_r_above_label,
            i_to_r_below, i_to_r_below_label,
            z_to_s_below, z_to_s_below_label
        )

        # Place flowchart at the same position as equations
        flowchart.move_to(equations)

        # Transform equations → flowchart
        self.play(ReplacementTransform(equations, flowchart))
        self.wait(2)
                # Thu nhỏ flowchart và di chuyển xuống
        self.play(
            flowchart.animate.scale(0.7).to_edge(DOWN*1.1),
            run_time=1.5
        )
        self.wait(0.5)
        # System of equations
        # Tạo lại hệ phương trình ở vị trí trên
        
        # System of equations
        eq_1 = MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S + cZ", font_size=font_size)
        eq_2 = MathTex("I'", "=", r"\beta S Z", "-", r"\rho I", "-", r"\delta I", font_size=font_size)
        eq_3 = MathTex("Z'", "=", r"\rho I", "+", r"\zeta R", "-", r"\alpha S Z - cZ", font_size=font_size)
        eq_4 = MathTex("R'", "=", r"\delta S", "+", r"\delta I", "+", r"\alpha S Z", "-", r"\zeta R", font_size=font_size)
        self.play(FadeIn(VGroup(eq_1, eq_2, eq_3, eq_4).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2.3)))
        self.wait(2)
