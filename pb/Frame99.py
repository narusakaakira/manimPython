from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class SZRE99(Scene):    
    def construct(self):
        self.show_population_limit()
        self.show_stability_reasoning()
    def show_population_limit(self):
            eq_initial = MathTex(r"S' + Z' + R' = \Pi", font_size=48).move_to(ORIGIN)
            eq_limit = MathTex(
                r"\lim_{t \to +\infty} S + Z + R = +\infty",
                tex_template=my_template, color=YELLOW, font_size=42
            ).move_to(ORIGIN)

            self.play(Write(eq_initial))
            self.wait(1)
            self.play(Transform(eq_initial, eq_limit))
            self.wait(2)
            self.play(FadeOut(eq_initial))

    def show_stability_reasoning(self):
        lines = [
            r"\text{Nếu như} \lim_{t \to +\infty}S(t) = +\infty",
            r"\text{thì từ } S' \text{ có }\displaystyle\lim_{t \to +\infty}(- \beta S Z - \delta S) = -\infty",
            r"S(t) \text{ sẽ giảm về rất nhỏ, vô lý}",
            r"\text{Do đó chỉ có thể } Z \text{ hoặc } R \text{ tiến ra vô cùng}",
            r"\text{Vì vậy } S \text{ sẽ phải giảm dần về } 0"
        ]
        line_mobjects = [MathTex(l, tex_template=my_template, font_size=36) for l in lines]
        vgroup = VGroup(*line_mobjects).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        for line in vgroup:
            self.play(Write(line))
            self.wait(0.5)

        self.wait(2)