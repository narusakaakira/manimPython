from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class jacoblast(Scene):
    def construct(self):
        # Công thức 1
        eq1 = MathTex(
            r"(\overline{S},\overline{I},\overline{Z},\overline{R}) = \left( \frac{c}{\beta'}, \frac{c}{\rho}\overline{Z}, \overline{Z}, \frac{\alpha c}{\zeta\beta}\overline{Z} \right)",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        # Công thức 2
        eq2 = MathTex(
            r"J = \begin{bmatrix} "
            r"\beta Z & 0 & -\beta S + c & 0 \\ "
            r"\beta Z & -\rho & \beta S & 0 \\ "
            r"-\alpha Z & \rho & -\alpha S - c & \zeta \\ "
            r"\alpha Z & 0 & \alpha S & -\zeta "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        # Công thức 3
        eq3 = MathTex(
            r"\det(J(\overline{S},\overline{I},\overline{Z},\overline{R}) - \lambda I) = \det"
            r"\begin{bmatrix} "
            r"\beta\overline{Z} - \lambda & 0 & 0 & 0 \\ "
            r"\beta\overline{Z} & -\rho-\lambda & c & 0 \\ "
            r"-\alpha\overline{Z} & \rho & -\frac{\alpha c}{\beta}-c-\lambda & \zeta \\ "
            r"\alpha\overline{Z} & 0 & \frac{\alpha c}{\beta} & -\zeta-\lambda "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=34
        ).move_to(ORIGIN)

        # Công thức 4
        eq4 = MathTex(
            r"= -(\beta\overline{Z}-\lambda) \det"
            r"\begin{bmatrix} "
            r"-\rho-\lambda & c & 0 \\ "
            r"\rho & -\frac{\alpha c}{\beta}-c-\lambda & \zeta \\ "
            r"0 & \frac{\alpha c}{\beta} & -\zeta-\lambda "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=34
        ).move_to(ORIGIN)

        # Công thức 5
        eq5 = MathTex(
            r"= -(\beta\overline{Z}-\lambda) \Bigg\{ -\lambda \bigg[ \lambda^2 + "
            r"\left( \rho + \frac{\alpha c}{\beta} + c + \zeta \right)\lambda + "
            r"\frac{\zeta\alpha c}{\beta} + \frac{\rho\alpha c}{\beta} + \rho\zeta + c\zeta "
            r"\bigg] \Bigg\}",
            tex_template=my_template,
            font_size=32
        ).move_to(ORIGIN)

        # Vị trí căn giữa

        # Hiện công thức 1
        self.play(Write(eq1))
        self.wait(1)

        # Transform 1 → 2
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(1)

        # Transform 2 → 3
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(1)

        # Transform 3 → 4
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(1)

        # Transform 4 → 5
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(1)

        # Highlight phương trình bậc 2 trong ngoặc
        quadratic = eq5.get_part_by_tex(
            r"\lambda^2 + \left( \rho + \frac{\alpha c}{\beta} + c + \zeta \right)\lambda"
        )
        self.play(quadratic.animate.set_color(YELLOW))
        self.wait(2)