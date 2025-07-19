from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class SZRExplanation(Scene):
    def construct(self):
        self.show_system()
        self.show_pi_note()
        self.show_beta_sz_explanation()
        self.show_delta_s_explanation()
        self.show_population_limit()
        self.show_stability_reasoning()

    def show_system(self):
        eq_S = MathTex(r"S' = \Pi - \beta S Z - \delta S", tex_template=my_template, font_size=40)
        eq_Z = MathTex(r"Z' = \beta S Z + \zeta R - \alpha S Z", tex_template=my_template, font_size=40)
        eq_R = MathTex(r"R' = \delta S + \alpha S Z - \zeta R", tex_template=my_template, font_size=40)

        system = VGroup(eq_S, eq_Z, eq_R).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(system))
        self.wait(1)

        self.play(FadeOut(eq_Z), FadeOut(eq_R))
        # ✅ dịch S' cao hơn
        self.play(eq_S.animate.move_to(UP * 3))
        self.wait(1)

    def show_pi_note(self):
        pi_note = Tex(
            r"$\Pi$: tốc độ sinh đẻ tự nhiên của con người",
            tex_template=my_template, font_size=38
        ).move_to(ORIGIN)
        self.play(Write(pi_note))
        self.wait(2)
        self.play(FadeOut(pi_note))

    def show_beta_sz_explanation(self):
        steps = [
            r"\text{Tổng số dân: } N",
            r"\text{Mỗi Zombie lây } \beta N \text{ người}",
            r"\text{Có } Z \text{ Zombie: } \beta N Z \text{ người}",
            r"\text{Xác suất chọn người khỏe mạnh: } P(S) = \frac{S}{N}",
            r"\text{Tốc độ lây nhiễm: } (\beta N Z) \cdot P(S) = \beta S Z"
        ]
        step_mobjects = [MathTex(s, tex_template=my_template, font_size=36) for s in steps]
        vgroup = VGroup(*step_mobjects).arrange(DOWN*1.5, buff=0.4).move_to(ORIGIN)

        for step in vgroup:
            self.play(Write(step))
            self.wait(1)
        self.play(FadeOut(vgroup))

    def show_delta_s_explanation(self):
        steps = [
            r"\text{Bị chết do các nguyên nhân khác ngoài Zombie}",
            r"\text{Tỉ lệ tử vong của người khỏe mạnh là } \delta",
            r"\text{Tốc độ tử vong tự nhiên của dân số: } \delta S"
        ]
        step_mobjects = [MathTex(s, tex_template=my_template, font_size=36) for s in steps]
        vgroup = VGroup(*step_mobjects).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for step in vgroup:
            self.play(Write(step))
            self.wait(1)

        self.wait(1)
        self.play(FadeOut(vgroup))


