from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class Proof2(Scene):
    def construct(self):
        self.diag()
    def diag(self):
        text_1 = Tex(
            r"Nhắc lại tính chất quan trọng của ma trận đường chéo:", tex_template=my_template, font_size=36
        )
        text_2 = Tex(
            r"$D = diag[x_1,x_2,\cdots,x_n]$", tex_template=my_template, font_size=36
        )
        tran_text_2 = Tex(
            r"$D = \begin{bmatrix}x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n\end{bmatrix}$", tex_template=my_template, font_size=36
        )
        tran_text_3_5 = Tex(
            r"$D^n = \underbrace{\begin{bmatrix}x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n\end{bmatrix} \cdot \begin{bmatrix}x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n\end{bmatrix}\cdots\begin{bmatrix}x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n\end{bmatrix}}_{n\text{ lần}}$",
            tex_template=my_template, font_size=36
        )

        tran_text_3 = Tex(
             r"$D^n = \begin{bmatrix}x_1^n & 0 & \cdots & 0 \\ 0 & x_2^n & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n^n\end{bmatrix}$", tex_template=my_template, font_size=36
        )
        tran_text_4 = Tex(
            r"$D^n = diag[x_1^n,x_2^n,\cdots,x_n^n]$", tex_template=my_template, font_size=36
        )
        tran_text_5 = Tex(
            r"$\displaystyle\sum_{i = 0}^{\infty}\frac{D^i t^i}{i!} = \sum_{i = 0}^{\infty} \frac{diag[x_1^i,x_2^i,\cdots,x_n^i]\cdot t^i}{i!}$", tex_template=my_template, font_size=36
        )
        tran_text_6 = Tex(
            r"$e^{Dt} = diag[e^{x_1t},e^{x_2t},\cdots,e^{x_nt}]$", tex_template=my_template, font_size=36
        )
        tran_text_7 = Tex(
            r"$e^{\Lambda t} = diag[e^{\lambda_1},e^{\lambda_2},\cdots,e^{\lambda_n}]$", tex_template=my_template, font_size=36
        )

        group = VGroup(text_1, text_2).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(group, run_time=6))
        self.wait(1)
        self.play(
            text_1.animate.shift(UP * 1.2),
            run_time=1
        )
        text_replace = Tex(
            r"Vì vậy mà ta có được",
            tex_template=my_template, font_size=36
        ).move_to(text_1.get_center())
        self.play(ReplacementTransform(text_2, tran_text_2))
        self.wait(3)
        self.play(ReplacementTransform(tran_text_2, tran_text_3_5))
        self.wait(3)
        self.play(ReplacementTransform(tran_text_3_5, tran_text_3))
        self.wait(3)
        self.play(ReplacementTransform(tran_text_3, tran_text_4))
        self.wait(3)
        self.play(ReplacementTransform(tran_text_4, tran_text_5))
        self.wait(3)
        self.play(ReplacementTransform(tran_text_5, tran_text_6))
        self.wait(3)
        self.play(ReplacementTransform(text_1, text_replace))
        self.play(ReplacementTransform(tran_text_6, tran_text_7))
        self.wait(3)
        self.play(FadeOut(group,tran_text_7, text_replace))