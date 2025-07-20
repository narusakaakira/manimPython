from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class latentInfection(Scene):
    def construct(self):
        # Jacobian tổng quát
        jacobian_general = MathTex(
            r"J=",
            r"\begin{bmatrix}"
            r"-\beta Z & 0 & -\beta S & 0\\"
            r"\beta Z & \rho & \beta S & 0\\"
            r"-\alpha Z & \rho & -\alpha S & \zeta \\"
            r"\alpha Z & 0 & \alpha S & -\zeta"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)
        # Biến đổi jacobian
        jacobian_Sbar_1 = MathTex(
            r"\det(J(\overline{S},0,0,0) - \lambda I) &=",
            r"\det \begin{bmatrix}"
            r"\lambda & 0 & \beta \overline{S} & 0\\"
            r"0 & -\rho - \lambda & \beta \overline{S} & 0\\"
            r"0 & \rho & -\alpha\overline{S} - \lambda & \zeta\\"
            r"0 & 0 & \alpha \overline{S} & -\zeta - \lambda"
            r"\end{bmatrix}\\",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        jacobian_Sbar_2 = MathTex(
            r"\det(J(\overline{S},0,0,0) - \lambda I) &=",
            r"-\lambda \det\begin{bmatrix}"
            r"-\rho - \lambda & \beta\overline{S} & 0\\"
            r"\rho & -\alpha\overline{S} - \lambda & \zeta\\"
            r"0 & \alpha\overline{S} & -\zeta - \lambda"
            r"\end{bmatrix}\\",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        jacobian_Sbar_3 = MathTex(
            r"\det(J(\overline{S},0,0,0) - \lambda I) &=",
            r"\det \begin{bmatrix}"
            r"\lambda & 0 & \beta \overline{S} & 0\\"
            r"0 & -\rho - \lambda & \beta \overline{S} & 0\\"
            r"0 & \rho & -\alpha\overline{S} - \lambda & \zeta\\"
            r"0 & 0 & \alpha \overline{S} & -\zeta - \lambda"
            r"\end{bmatrix}\\",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)
        # Kết quả biến đổi jacobian
        jacobian_Zbar = MathTex(
            r"\det(J(\overline{S},0,0,0) - \lambda I) &=",
            r" \lambda[-\lambda^3 - (\rho + \zeta + \alpha\overline{S})\lambda^2 - (\rho\alpha\overline{S} + \rho\zeta - \rho\beta\overline{S})\lambda + \rho\zeta\beta\overline{S}]",
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
        self.play(Write(jacobian_general))
        self.wait(2)

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
            ReplacementTransform(jacobian_Sbar_2, jacobian_Sbar_3),
            run_time=2
        )
        self.wait(1)
        self.play(
            FadeOut(jacobian_Sbar_2),
            ReplacementTransform(jacobian_Sbar_3, jacobian_Zbar),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(jacobian_Sbar_3,jacobian_Zbar))
        self.play(
            Write(conclusion_Sbar),
            run_time=2
        )
        self.wait(1)
        self.play(
            ReplacementTransform(conclusion_Sbar, jacobian_result),
            run_time=2
        )
        self.wait(1)


   


