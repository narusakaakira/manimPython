from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class EquationGroupDisplay(Scene):
    def construct(self):
        intro_1 = MathTex(r"\text{Xét hệ $f: \mathbb{R}^n \to \mathbb{R}^m$ khả vi tại điểm $x^*$,}",tex_template=my_template, color = YELLOW).scale(0.7).move_to(UP)
        
        intro_2 = MathTex(r"\text{ khi đó tồn tại ánh xạ tuyến tính $L: \mathbb{R}^n \to \mathbb{R}^m$ sao cho}",tex_template=my_template, color = YELLOW).scale(0.7).next_to(intro_1, DOWN)
        self.play(Write(intro_1))
        self.play(Write(intro_2))


        # Cả nhóm dịch chuyển lên trên
        group = VGroup(intro_1, intro_2)
        self.play(group.animate.shift(1.3 * UP))


        limit_tex = MathTex(r"\lim_{h \to 0} \frac{|| f(x^* + h) - f(x^*) - L(h)||}{||h||} = 0. ").scale(0.7)
        function_1 = MathTex(r"f(x) = f(x^*) + J_f(x^*) (x - x^*) + r(x), \text{ với } \lim_{x \to x^*} \frac{||r(x)||}{||x - x^*||} = 0", tex_template=my_template).scale(0.7)
        function_2 = MathTex(r"f(x) \approx  f(x^*) + J_f(x^*) (x - x^*)").scale(0.7)

        intro_3 = MathTex(r"\text{Đặt hàm dao động $u = x - x_0$, ta được $\dot{u} = \dot{x}$ và từ (1) ta được }",tex_template=my_template, color = YELLOW).move_to(UP*1.5).scale(0.7)

        text_1 = MathTex(r"f(x) \approx J_f(x_0) (x - x_0)", tex_template=my_template).scale(0.7).move_to(UP*0.5)
        text_2 = MathTex(r"\dot{u} = J_f(x_0)u", tex_template=my_template).scale(0.7).move_to(UP*0.5)


        self.play(Create(limit_tex), run_time = 2)
        self.play(
            FadeOut(limit_tex),
            run_time=1
        )
        self.play(
            FadeOut(intro_1, intro_2),
            run_time=1,
        )
        self.play(Create(function_1),run_time=1)
        self.play(
            FadeOut(function_1),
            run_time=1,
        )
        self.play(Create(function_2),run_time=1)
        self.play(
            FadeOut(function_2),
            run_time=1,
        )

        self.play(Write(intro_3))
        self.play(Write(text_1))
        self.play(
            FadeOut(text_1),
            run_time=1,
        )

        self.play(Write(text_2))
        self.wait()




