from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")


class vaccineFigure(Scene):
    def construct(self):
          # Jacobian tổng quát
        equation_SIZR = MathTex(
            r"S' &= \Pi - \beta S Z - \delta S + cZ \\",
            r"I' &= \beta S Z - \rho I - \delta I \\",
            r"Z' &= \rho I + \zeta R - \alpha S Z - cZ \\",
            r"R' &= \delta S + \delta I + \alpha S Z - \zeta R\\",
            tex_template=my_template,
            font_size=36

        )  
        jacobian_general = MathTex(
            r"J=",
            r"\begin{bmatrix}"
            r"\beta Z & 0 & -\beta S + c & 0 \\[6pt]"
            r"\beta Z & -\rho & \beta S & 0 \\[6pt]"
            r"-\alpha Z & \rho & -\alpha S - c & \zeta \\[6pt]"
            r"\alpha Z & 0 & \alpha S & -\zeta"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)
        # Biến đổi jacobian
        jacobian_Sbar_1 = MathTex(
            r"\det(J(\bar{S}, \bar{I}, \bar{Z}, \bar{R}) - \lambda I) =",
            r"\det \begin{bmatrix}"
            r"\beta \bar{Z} -\lambda & 0 & 0 & 0 \\[6pt]"
            r"\beta \bar{Z} & -\rho -\lambda & c & 0 \\[6pt]"
            r"-\alpha \bar{Z} & \rho & -\frac{\alpha c}{\beta} - c - \lambda & \zeta \\[6pt]"
            r"\alpha \bar{Z} & 0 & \frac{\alpha c}{\beta} & -\zeta - \lambda"
            r"\end{bmatrix}\\",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        jacobian_Sbar_2 = MathTex(
            r"\det(J(\bar{S}, \bar{I}, \bar{Z}, \bar{R}) - \lambda I) =",
            r"-(\beta \bar{Z} - \lambda) \det\begin{bmatrix}"
            r"-\rho - \lambda& c & 0 \\[6pt]"
            r"\rho & -\frac{\alpha c}{\beta} - c- \lambda & \zeta \\[6pt]"
            r"0 & \frac{\alpha c}{\beta} & -\zeta- \lambda"
            r"\end{bmatrix}\\",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)


        jacobian_Zbar = MathTex(
            r"\det(J(\bar{S}, \bar{I}, \bar{Z}, \bar{R}) - \lambda I) =",
            r"-(\beta \bar{Z} - \lambda)\bigg\{ -\lambda \bigg[\lambda^2 + \bigg( \rho + \frac{\alpha c}{\beta} + c + \zeta \bigg) \lambda+ \frac{\zeta \alpha c}{\beta} + \frac{\rho \alpha c}{\beta} + \rho \zeta + c \zeta\bigg]\bigg\}.",
            tex_template=my_template,
            font_size=28
        ).move_to(ORIGIN)
        # Giải thích điểm cân bằng
        conclusion_Sbar = Tex(
            r"Vì $\rho\zeta\beta\overline{S} > 0$ nên theo định lí Viette thì phương trình trên phải có 1 nghiệm dương, vì vậy điểm cân bằng này không ổn định. Tiếp theo, ta có ",
            tex_template=my_template,
            font_size=30
        ).move_to(ORIGIN)
        
        jacobian_result = MathTex(
            r"\det\big( J(0,0,\bar{Z},0) - \lambda I \big) = \det \begin{bmatrix}"
            r"-\beta \bar{Z} - \lambda & 0 & 0 & 0 \\"
            r"\beta \bar{Z} & -\rho - \lambda & 0 & 0 \\"
            r"-\alpha \bar{Z} & \rho & -\lambda & \zeta \\"
            r"\alpha \bar{Z} & 0 & 0 & -\zeta - \lambda"
            r"\end{bmatrix}.",
            tex_template=my_template,
            font_size=28
        )

        # Hiện tổng quát
        # self.play(Write(jacobian_general))
        # self.wait(2)
        self.play(Write(equation_SIZR))
        self.wait(2)
        self.play(
            ReplacementTransform(equation_SIZR, jacobian_general),
            run_time=1
        )
        self.wait(1)
        # Biến thành tại (S̄,0,0)
        self.play(
            ReplacementTransform(jacobian_general, jacobian_Sbar_1),
            run_time=1
        )
        self.wait(1)
        self.play(
            FadeOut(jacobian_general),
            ReplacementTransform(jacobian_Sbar_1, jacobian_Sbar_2),
            run_time=2
        )
        self.wait(1)
        self.play(
            FadeOut(jacobian_Sbar_1),
            ReplacementTransform(jacobian_Sbar_2, jacobian_Zbar),
            run_time=2
        )
        self.wait(1)
        # self.play(
        #     FadeOut(jacobian_Sbar_1),
        #     ReplacementTransform(jacobian_Sbar_2, jacobian_Sbar_3),
        #     run_time=2
        # )
        # self.wait(1)
        # self.play(
        #     FadeOut(jacobian_Sbar_2),
        #     ReplacementTransform(jacobian_Sbar_3, jacobian_Zbar),
        #     run_time=2
        # )
        # self.wait(1)
        # self.play(FadeOut(jacobian_Sbar_3,jacobian_Zbar))
        # self.play(
        #     Write(conclusion_Sbar),
        #     run_time=2
        # )
        # self.wait(1)
        # self.play(
        #     ReplacementTransform(conclusion_Sbar, jacobian_result),
        #     run_time=2
        # )
        # self.wait(1)

