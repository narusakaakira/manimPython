from manim import *

class SRZEquationsToFlowchart(Scene):
    def construct(self):
        font_size = 36

        # Hệ phương trình ban đầu
        eq1 = MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S", font_size=font_size)
        eq2 = MathTex("Z'", "=", r"\beta S Z", "+", r"\zeta R", "-", r"\alpha S Z", font_size=font_size)
        eq3 = MathTex("R'", "=", r"\delta S", "+", r"\alpha S Z", "-", r"\zeta R", font_size=font_size)

        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(ORIGIN)
        self.play(Write(equations))
        self.wait(1)

        # Tạo flowchart SRZ
        box_w, box_h = 1.8, 1.3
        S_box = Rectangle(width=box_w, height=box_h).shift(LEFT*3)
        Z_box = Rectangle(width=box_w, height=box_h)
        R_box = Rectangle(width=box_w, height=box_h).shift(RIGHT*3)

        S_label = Text("S", font_size=font_size).move_to(S_box)
        Z_label = Text("Z", font_size=font_size).move_to(Z_box)
        R_label = Text("R", font_size=font_size).move_to(R_box)

        boxes = VGroup(S_box, S_label, Z_box, Z_label, R_box, R_label)

        inflow = Arrow(S_box.get_left() + LEFT*1.5, S_box.get_left(), buff=0, stroke_width=2)
        inflow_label = MathTex(r"\Pi").next_to(inflow, UP)

        s_to_z = Arrow(S_box.get_right(), Z_box.get_left(), buff=0, stroke_width=2)
        s_to_z_label = MathTex(r"\beta S Z").next_to(s_to_z, UP)

        z_to_r = Arrow(Z_box.get_right(), R_box.get_left(), buff=0, stroke_width=2)
        z_to_r_label = MathTex(r"\alpha S Z").next_to(z_to_r, UP)

        r_to_z = Arrow(R_box.get_left(), Z_box.get_right(), buff=0, stroke_width=2).shift(DOWN*0.3)
        r_to_z_label = MathTex(r"\zeta R").next_to(r_to_z, DOWN)

        s_to_r_v = VGroup(
            Line(S_box.get_top(), S_box.get_top() + UP*1, stroke_width=2),
            Line(S_box.get_top() + UP*1, R_box.get_top() + UP*1, stroke_width=2),
            Arrow(R_box.get_top() + UP*1 , R_box.get_top(), stroke_width=2)
        )
        s_to_r_label = MathTex(r"\delta S").move_to(S_box.get_top() + R_box.get_top() + UP*1.2).shift(UP*0.3)

        flowchart = VGroup(
            boxes,
            inflow, inflow_label,
            s_to_z, s_to_z_label,
            z_to_r, z_to_r_label,
            r_to_z, r_to_z_label,
            s_to_r_v, s_to_r_label
        )
        flowchart.move_to(equations)

        # Chuyển đổi hệ phương trình → flowchart
        self.play(ReplacementTransform(equations, flowchart))
        self.wait(1)
        eq_1 = MathTex("S'", "=", r"\Pi", "-", r"\beta S Z", "-", r"\delta S", font_size=font_size)
        eq_2 = MathTex("Z'", "=", r"\beta S Z", "+", r"\zeta R", "-", r"\alpha S Z", font_size=font_size)
        eq_3 = MathTex("R'", "=", r"\delta S", "+", r"\alpha S Z", "-", r"\zeta R", font_size=font_size)
        # Thu nhỏ flowchart và hiển thị lại hệ phương trình
        equations_new = VGroup(
            eq_1, eq_2.copy(), eq_3.copy()
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(UP)

        self.play(
            flowchart.animate.scale(0.8).shift(DOWN * 0.5),
            Write(equations_new),
            run_time=2
        )
        self.wait(2)