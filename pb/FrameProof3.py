from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class Proof3(Scene):
    def construct(self):
        self.algr()
        self.eigen()
        self.theorem()
    def algr(self):
        text_1 = Tex( r"Công thức nghiệm của $u$ là", tex_template=my_template).shift(UP * 1.2)
        text_2 = Tex(
            r"$u(t) = e^{Jt}u(0)$", 
            tex_template=my_template, font_size=36
        ).next_to(text_1, DOWN, buff=0.5)
        tran1 = Tex(
            r"$u(t) = Pe^{\Lambda t}P^{-1}u(0)$", 
            tex_template=my_template, font_size=36
        ).next_to(text_1, DOWN*2, buff=0.5)
        tran2 = Tex(
            r"$u(t) = Pe^{\Lambda t}[P^{-1}u(0)]$ ", 
            tex_template=my_template, font_size=36
        ).next_to(text_1, DOWN*2, buff=0.5)
        group = VGroup(text_1, text_2).move_to(ORIGIN)
        self.play(Write(group, run_time=5))
        self.wait(1)
        self.play(ReplacementTransform(text_2, tran1))
        self.wait(1)
        self.play(ReplacementTransform(tran1, tran2))
        self.wait(3)
        self.play(FadeOut(group), FadeOut(tran2))
    def eigen(self):
        text_1 = Tex(
            r"Tồn tại bộ số $(c_1,c_2,\cdots,c_n) \in \mathbb{R}^n$ sao cho", 
            tex_template=my_template, font_size=36
        )
        text_2 = Tex(
            r"$u(0) = c_1v_1 + c_2v_2 + \cdots + c_nv_n$", 
            tex_template=my_template, font_size=36
        )
        text_3 = Tex(
            r"$P^{-1} u(0) = \begin{bmatrix}c_1 \\ c_2 \\ \vdots \\ c_n\end{bmatrix}$", 
            tex_template=my_template, font_size=36
        )
        text_4 = Tex(
            r"$e^{\Lambda t} [P^{-1} u(0)] = \begin{bmatrix}c_1 \\ c_2 \\ \vdots \\ c_n\end{bmatrix}\cdot\begin{bmatrix}e^{\lambda_1 t} & 0 & \cdots & 0 \\0 & e^{\lambda_2 t} & \cdots & 0 \\\vdots & \vdots & \ddots & \vdots \\0 & 0 & \cdots & e^{\lambda_n t}\end{bmatrix}$", 
            tex_template=my_template, font_size=36
        )
        text_5 = Tex(
            r"$e^{\Lambda t} [P^{-1} u(0)] = \begin{bmatrix}c_1 e^{\lambda_1 t} \\ c_2 e^{\lambda_2 t} \\ \vdots \\ c_n e^{\lambda_n t}\end{bmatrix}$", 
            tex_template=my_template, font_size=36
        )
        text_6 = Tex(
            r"$u(t) = [v_1,v_2,\ldots,v_n]\cdot \begin{bmatrix}c_1 e^{\lambda_1 t} \\ c_2 e^{\lambda_2 t} \\ \vdots \\ c_n e^{\lambda_n t} \end{bmatrix}$", 
            tex_template=my_template, font_size=36
        )
        text_7 = Tex(
            r"$u(t) = \displaystyle\sum_{i=1}^{n} c_i e^{\lambda_i t} v_i$", 
            tex_template=my_template, font_size=36
        )
        text_8 = Tex(
            r"Với các $\lambda_i$ là các eigenvalue của $J$, tức là nghiệm của phương trình", 
            tex_template=my_template, font_size=36
        ).next_to(text_7, DOWN, buff=0.5)
        text_9 = Tex(
            r"$\det(J - \lambda I) = 0$", 
            tex_template=my_template, font_size=36
        ).next_to(text_8, DOWN, buff=0.5)
        self.play(Write(text_1, run_time=5))
        self.wait(1)
        self.play(ReplacementTransform(text_1, text_2))
        self.wait(4)
        self.play(ReplacementTransform(text_2, text_3))
        self.wait(3)
        self.play(ReplacementTransform(text_3, text_4))
        self.wait(3)
        self.play(ReplacementTransform(text_4, text_5))
        self.wait(3)
        self.play(ReplacementTransform(text_5, text_6))
        self.wait(3)
        self.play(ReplacementTransform(text_6, text_7))
        self.wait(3)
        self.play(Write(text_8), run_time=3)
        self.play(Write(text_9), run_time=3)
        self.play(FadeOut(text_7, text_8, text_9))
    def theorem(self):
        text_1 = Tex(
            r"\textbf{Định lý Hartman-Grobman:} Gần một điểm cân bằng (tức là tất cả các eigenvalue của ma trận Jacobian tại điểm đó đều có phần thực khác 0) hệ phương trình phi tuyến", tex_template=my_template, font_size=36
        ).shift(UP * 2.7)
        text_2 = Tex(
            r"$\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$", tex_template=my_template, font_size=36
        ).next_to(text_1, DOWN, buff=0.5)
        text_3 = Tex(
            r"có quỹ đạo gần điểm cân bằng giống về hình dạng với quỹ đạo của hệ tuyến tính hóa", tex_template=my_template, font_size=36
        ).next_to(text_2, DOWN, buff=0.5)
        text_4 = Tex(
            r"$\dot{\mathbf{x}} = J\mathbf{x}$", tex_template=my_template, font_size=36
        ).next_to(text_3, DOWN, buff=0.5)
        text_5 = Tex(
            r"Cụ thể, nếu các eigenvalue đều có phần thực la âm, thì hệ ổn định gần điểm cân bằng. Nếu có một eigenvalue có phần thực dương, thì hệ không ổn định gần điểm cân bằng đó. Nếu phần thực lớn nhất của các eigenvalue bằng 0 thì không thể đánh giá độ ổn định", tex_template=my_template, font_size=36
        ).next_to(text_4, DOWN, buff=0.5)
        self.play(Write(text_1, run_time=5))
        self.play(Write(text_2, run_time=5))
        self.play(Write(text_3, run_time=5))
        self.play(Write(text_4, run_time=5))
        self.play(Write(text_5, run_time=5))



