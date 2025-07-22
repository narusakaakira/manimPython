from manim import *

# Tạo template hỗ trợ tiếng Việt
my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class Frame5(Scene):
    def construct(self):
        self.Frame1()
        self.wait(1)
        self.Frame2()
        self.wait(1)
        self.Frame3()

    def Frame1(self):
        text1 = Tex(
            r"Trong khoảng thời gian ngắn ($\Pi = \delta = 0$), "
            r"ta có được hai điểm cân bằng",
            font_size=36,
            tex_template=my_template
        ).move_to(ORIGIN + UP)

        eq = MathTex(
            r"(\overline{S}, \overline{I}, \overline{Z}, \overline{R}, \overline{Q})= "
            r"(\overline{S}, 0, 0, 0, 0), (0, 0, \overline{Z}, \overline{R}, \overline{Q})",
            font_size=36,
            tex_template=my_template
        ).next_to(text1, DOWN, buff=0.8)

        self.play(Write(text1))
        self.play(Write(eq))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(eq))

    def Frame2(self):
        # Vector u
        u_def = MathTex(
            r"u = \begin{bmatrix} I \\ Z \\ Q \end{bmatrix}",
            font_size=36,
            tex_template=my_template
        ).move_to(ORIGIN)

        # Hệ phương trình
        system = MathTex(
            r"\dot{u} = Ju",
            font_size=36,
            tex_template=my_template
        ).move_to(ORIGIN)

        # Jacobian
        jacobian = MathTex(
            r"J = \begin{bmatrix} "
            r"-(\rho+\kappa) & \beta S & 0 \\ "
            r"\rho & -\alpha S - \sigma & 0 \\ "
            r"\kappa & \sigma & -\gamma "
            r"\end{bmatrix}",
            font_size=36,
            tex_template=my_template
        ).move_to(ORIGIN)
        # Jacobian definition (as in the image)
        jacobian_def = MathTex(
            r"J = \left. \frac{\delta (\text{độ thay đổi của hệ tại } i)}{\delta x_j} \right|_x"
            r"= \left. \frac{\delta (\text{độ tăng của hệ tại } i)}{\delta x_j} \right|_x"
            r"- \left. \frac{\delta (\text{độ giảm của hệ tại } i)}{\delta x_j} \right|_x",
            font_size=28,
            tex_template=my_template
        ).move_to(ORIGIN)
        next = MathTex(
            r"J = F - V"
        ).move_to(ORIGIN)
        # Animation sequence
        self.play(Write(u_def))
        self.wait(3)

        self.play(ReplacementTransform(u_def, system))
        self.wait(3)

        self.play(ReplacementTransform(system, jacobian))
        self.wait(3)
        self.play(ReplacementTransform(jacobian, jacobian_def))
        self.wait(5)
        self.play(ReplacementTransform(jacobian_def, next))
        self.wait(5)
        self.play(FadeOut(next))
    def Frame3(self):
        text_1 = Tex(
            r"$F$ mô tả sự bổ sung các ca nhiễm mới vào hệ, tức là ca nhiễm từ ngoài đi vào hệ $(I, Z, Q)$",
            font_size=36,
            tex_template=my_template
        )
        text_2 = Tex(
            r" $(-V)$ mô tả sự thay đổi trạng thái của các đối tượng $(I, Z, Q)$, do đó $V$ sẽ là hàm mô tả sự giảm cục bộ của hệ.",
            font_size=36,
            tex_template=my_template
        )
        group = VGroup(text_1, text_2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(ORIGIN)
        self.play(Write(group),run_time = 10)
        self.wait(3)
        self.play(FadeOut(group))