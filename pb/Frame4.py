from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class ShowTheoremAndDefinitions(Scene):
    def construct(self):
        theorem1 = Tex(
            r"Khi đại dịch Zombie xảy ra, nếu không có biện pháp can thiệp, thì nhân loại sẽ diệt vong.",
            tex_template=my_template,
            font_size=32
        ).move_to(ORIGIN)

        def1 = Tex(
            r"\textbf{Định nghĩa 1.} Một điểm cân bằng của hệ phương trình vi phân là một điểm $(S_0, Z_0, R_0)$ sao cho $S' = 0, Z' = 0, R' = 0$ tại điểm đó.",
            tex_template=my_template,
            font_size=30
        ).move_to(ORIGIN)

        def2 = Tex(
            r"\textbf{Định nghĩa 2.} Một điểm cân bằng là ổn định nếu mọi điểm gần nó đều tiến về nó khi $t \to +\infty$.",
            tex_template=my_template,
            font_size=30
        ).move_to(ORIGIN)

        def3 = Tex(
            r"\textbf{Định nghĩa 3.} Một điểm cân bằng là không ổn định nếu có ít nhất một điểm gần nó mà không tiến về nó khi $t \to +\infty$.",
            tex_template=my_template,
            font_size=30
        ).move_to(ORIGIN)

        # Hiện lần lượt, chậm hơn
        for mobj in [theorem1, def1, def2, def3]:
            self.play(Write(mobj, run_time=3))  # Viết ra chậm hơn
            self.wait(10)                        # Dừng lâu hơn
            self.play(FadeOut(mobj, run_time=2))  # Biến mất cũng chậm hơn
