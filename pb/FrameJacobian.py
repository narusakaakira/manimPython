from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class JacobianEigenvalues(Scene):
    def construct(self):
        # Jacobian tổng quát
        jacobian_general = MathTex(
            r"J=",
            r"\begin{bmatrix}"
            r"-\beta Z & -\beta S & 0 \\"
            r"\beta Z-\alpha Z & \beta S-\alpha S & \zeta \\"
            r"\alpha Z & \alpha S & -\zeta"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        jacobian_Sbar = MathTex(
            r"J(\bar{S},0,0)=",
            r"\begin{bmatrix}"
            r"0 & -\beta\bar{S} & 0 \\"
            r"0 & \beta\bar{S}-\alpha\bar{S} & \zeta \\"
            r"0 & \alpha\bar{S} & -\zeta"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        jacobian_Zbar = MathTex(
            r"J(0,\bar{Z},0)=",
            r"\begin{bmatrix}"
            r"-\beta\bar{Z} & 0 & 0 \\"
            r"\beta\bar{Z}-\alpha\bar{Z} & 0 & \zeta \\"
            r"\alpha\bar{Z} & 0 & -\zeta"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        # Hiện tổng quát
        self.play(Write(jacobian_general))
        self.wait(2)

        # Biến thành tại (S̄,0,0)
        self.play(Transform(jacobian_general, jacobian_Sbar))
        self.wait(2)

        # Eigenvalues tại (S̄,0,0)
        eigen_Sbar = MathTex(
            r"\det(J-\lambda I) = \lambda \bigg[ -\lambda^2 + ((\beta-\alpha)\bar{S}-\zeta)\lambda + \zeta\beta\bar{S} \bigg]",
            tex_template=my_template,
            font_size=32
        ).next_to(jacobian_general, DOWN, buff=0.8)

        conclusion_Sbar = Tex(
            r"Điểm $(\bar{S},0,0)$ không ổn định do tồn tại nghiệm dương.",
            tex_template=my_template,
            font_size=30
        ).next_to(eigen_Sbar, DOWN)

        self.play(Write(eigen_Sbar))
        self.wait(2)
        self.play(Write(conclusion_Sbar))
        self.wait(2)

        # Xóa eigen & kết luận
        self.play(FadeOut(eigen_Sbar), FadeOut(conclusion_Sbar))

        # Biến thành tại (0,Z̄,0)
        self.play(Transform(jacobian_general, jacobian_Zbar))
        self.wait(2)

        # Eigenvalues tại (0,Z̄,0)
        eigen_Zbar = MathTex(
            r"\det(J-\lambda I) = -\lambda (\lambda+\beta\bar{Z})(\lambda+\zeta)",
            tex_template=my_template,
            font_size=32
        ).next_to(jacobian_general, DOWN, buff=0.8)

        conclusion_Zbar = Tex(
            r"Điểm $(0,\bar{Z},0)$ ổn định do mọi nghiệm đều âm.",
            tex_template=my_template,
            font_size=30
        ).next_to(eigen_Zbar, DOWN)

        self.play(Write(eigen_Zbar))
        self.wait(2)
        self.play(Write(conclusion_Zbar))
        self.wait(2)

        # Kết thúc
        self.play(FadeOut(jacobian_general), FadeOut(eigen_Zbar), FadeOut(conclusion_Zbar))
