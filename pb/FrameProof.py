from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class Proof(Scene):
    def construct(self):
        exp_new = Tex(
            r"Đặt $J = J_f(x_0)$ và đặt $e^{Jt} = \displaystyle\sum_{i=0}^{\infty} \frac{J^i t^i}{i!}$",tex_template=my_template
        ).move_to(ORIGIN)
        
        self.play(Write(exp_new))
        self.wait(2)
        self.play(FadeOut(exp_new))
        self.theorem2()
        self.themrem2_proof()
        self.theorem3()
    def theorem2(self):
        theorem2 = Tex(
            r"\textbf{Nhận xét:} Trong trường hợp này, $J$ sẽ là ma trận khả chéo, tức là tồn tại $P^{-1}$ sao cho $J = P\Lambda P^{-1}$, trong đó $P=[v_1, v_2, \ldots, v_n]$ là ma trận gồm các eigenvector của $J$ và $\Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$ là ma trận đường chéo gồm các eigenvalue tương ứng.",tex_template=my_template, font_size=36
        ).move_to(ORIGIN)
        self.play(Write(theorem2, run_time=8))
        self.wait(5)
        self.play(FadeOut(theorem2))

    def themrem2_proof(self):
        text_1 = Tex(
            r"\textbf{Chứng minh:} Chúng ta chỉ cần chứng minh chiều thuận. Với mọi $i$, với tính chất của các eigenvalue và eigenvector thì ta có ",tex_template=my_template, font_size=36
        ).move_to(ORIGIN)
        text_2 = Tex(
            r"$Jv_i = \lambda_i v_i \Rightarrow JP = \Lambda P \Leftrightarrow J = P\Lambda P^{-1}$",tex_template=my_template, font_size=36
        )
        text_3 = Tex(
            r"Như thế là hoàn tất chứng minh",tex_template=my_template, font_size=36
        )
        group = VGroup(text_1, text_2, text_3).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(group, run_time=6))
        self.wait(5)
        self.play(FadeOut(group))
    def theorem3(self):
        text_1 = Tex(
            r"\textbf{Nhận xét:} Nếu như $J$ có đầy đủ $n$ eigenvector độc lập tuyến tính thì sẽ có $e^{Jt} = P e^{\Lambda t}P^{-1}$",tex_template=my_template, font_size=36
        )
        text_2 = Tex(
            r"\textit{Chứng minh:} Ta có $J^2 = (P\Lambda P^{-1})(P\Lambda P^{-1}) = P\Lambda^2 P^{-1}$. Từ đây sử dụng quy nạp lên tổng quát thì ta có được:",tex_template=my_template, font_size=36
        )
        text_3 = Tex(
            r"$J^i = P\Lambda^i P^{-1}$, với mọi $i$ nguyên dương",tex_template=my_template, font_size=36
        )
        text_4 = Tex(
            r"Và từ khai triển của hàm mũ đã gọi ra thì được ta được",tex_template=my_template, font_size=36
        )
        exp_5 = Tex(
            r"$e^{Jt} = \displaystyle \sum_{i = 0}^{\infty} \frac{J^it^i}{i!}$",tex_template=my_template, font_size=36,color=YELLOW
        )
        group = VGroup(text_1, text_2, text_3, text_4, exp_5).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        exp_6 = Tex(
            r"$e^{Jt} = \displaystyle \sum_{i = 0}^{\infty} \frac{P\Lambda^iP^{-1}t^i}{i!}$",tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())
        exp_7= Tex(
            r"$e^{Jt} = \displaystyle P\left(\sum_{i = 0}^{\infty} \frac{\Lambda^it^i}{i!}\right)P^{-1}$",tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())
        exp_8= Tex(
            r"$e^{Jt} = Pe^{\Lambda t}P^{-1}$",tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())
        self.play(Write(group, run_time=12))
        self.wait(1)
        next_tex = Tex(
            r"$e^{Jt} = \displaystyle \sum_{i = 0}^{\infty} \frac{P\Lambda^iP^{-1}t^i}{i!}$",
            tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())

        self.play(ReplacementTransform(exp_5, next_tex))
        self.wait(1)

        next_tex2 = Tex(
            r"$e^{Jt} = \displaystyle P\left(\sum_{i = 0}^{\infty} \frac{\Lambda^it^i}{i!}\right)P^{-1}$",
            tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())

        self.play(ReplacementTransform(next_tex, next_tex2))
        self.wait(1)

        next_tex3 = Tex(
            r"$e^{Jt} = Pe^{\Lambda t}P^{-1}$",
            tex_template=my_template, font_size=36, color=YELLOW
        ).move_to(exp_5.get_center())

        self.play(ReplacementTransform(next_tex2, next_tex3))
        self.wait(2)
        self.play(FadeOut(group))

    def diag(self):
        text_1 = Tex(
            r"Nhắc lại tính chất quan trọng của ma trận đường chéo:", tex_template=my_template, font_size=36
        )
        text_2 = Tex(
            r"$D = diag[x_1,x_2,\cdots,x_n]", tex_template=my_template, font_size=36
        )
        tran_text_2 = Tex(
            r"$D = \begin{matrix}x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n\end{matrix}$", tex_template=my_template, font_size=36
        )