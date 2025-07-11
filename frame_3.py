from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")
class EquationGroupDisplay(Scene):
    def construct(self):
        eq1 = MathTex("S_0", "=", r"\Pi", "-", r"\beta\underline{ S Z}", "-", r"\delta S")
        eq2 = MathTex("Z_0", "=", r"\beta\underline{ S Z}", "+", r"\zeta R", "-", r"\alpha\underline{ S Z}")
        eq3 = MathTex("R_0", "=", r"\delta S", "+", r"\alpha\underline{ S Z}", "-", r"\zeta R")
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        box = SurroundingRectangle(equations, color=WHITE, buff=0.4)
        eq1[0].set_color(YELLOW)
        eq2[0].set_color(YELLOW)
        eq3[0].set_color(YELLOW)
        text_1 = Tex(r"\text{Tại sao ta lại cần phải sử dụng đại số tuyến tính trong khi mô hình này là phi tuyến?}", tex_template=my_template).scale(0.7).next_to(box, UP, buff=0.2)

        self.play(Write(text_1))

        
        self.play(Create(box))
        self.play(Create(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1.copy(), eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2.copy(), eq3))
        self.wait(1)
