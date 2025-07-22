from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class FVTransform(Scene):
    def construct(self):
        # Tóm tắt chi tiết
        summary = Tex(
            r"Khi xét thay đổi nhỏ của $I, Z, Q$, ta thấy $\beta S Z$ "
            r"hầu như chỉ thay đổi theo $Z$, do đó chỉ xuất hiện ở hàng 1 cột 2 của $F$. "
            r"Ma trận $V$ biểu diễn các hệ số giảm theo từng biến.",
            tex_template=my_template,
            font_size=34
        ).move_to(ORIGIN + UP*1)

        detail = Tex(
            r"Hàng 1: $I$ giảm bởi $(\rho+\kappa)I$, $Z$ tăng bởi $\rho I$, $Q$ tăng bởi $\kappa I$. \\"
            r"Hàng 2: $Z$ giảm bởi $\rho I$ và $(\alpha S+\sigma)Z$, $Q$ tăng bởi $\sigma Z$. \\"
            r"Hàng 3: $Q$ giảm bởi $\kappa I$, $\sigma Z$ và $\gamma Q$.",
            tex_template=my_template,
            font_size=32
        ).next_to(summary, DOWN, buff=0.6)

        self.play(Write(summary),run_time = 5)
        self.wait(1)
        self.play(Write(detail), run_time = 5)
        self.wait(2)

        # Gom nhóm summary + detail
        text_group = VGroup(summary, detail)

        # Ma trận F và V
        matrices = MathTex(
            r"F = \begin{bmatrix} "
            r"0 & \beta S & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0"
            r"\end{bmatrix} , \quad "
            r"V = \begin{bmatrix} "
            r"\rho+\kappa & 0 & 0 \\ "
            r"-\rho & \alpha S + \sigma & 0 \\ "
            r"-\kappa & -\sigma & \gamma"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=34
        ).move_to(text_group.get_center())

        # Transform
        self.play(FadeOut(text_group))
        self.wait(2)
        self.play(FadeIn(matrices))
        self.wait(2)
