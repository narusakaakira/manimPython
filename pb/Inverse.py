from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class VInv_FVInv_R0(Scene):
    def construct(self):
        # Step 1: V^{-1}
        V_inv = MathTex(
            r"V^{-1} ="
            r"\begin{bmatrix}"
            r"\displaystyle \frac{1}{\rho+\kappa} & 0 & 0 \\[12pt]"
            r"\displaystyle \frac{\rho}{(\rho+\kappa)(\alpha N+\sigma)} & \displaystyle \frac{1}{\alpha N+\sigma} & 0 \\[12pt]"
            r"\displaystyle \frac{\rho\sigma+\kappa(\alpha N+\sigma)}{\gamma(\rho+\kappa)(\alpha N+\sigma)} &"
            r"\displaystyle \frac{\sigma}{\gamma(\alpha N+\sigma)} &"
            r"\displaystyle \frac{1}{\gamma}"
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)


        # Step 2: FV^{-1}
        FV_inv = MathTex(
            r"FV^{-1} = \begin{bmatrix} "
            r"\frac{\beta S \rho}{(\rho+\kappa)(\alpha S+\sigma)} & \frac{\beta S}{\alpha S+\sigma} & 0 \\ "
            r"0 & 0 & 0 \\ "
            r"0 & 0 & 0 "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        # Step 3: R_0
        R_0 = MathTex(
            r"R_0 = \frac{\beta S \rho}{(\rho+\kappa)(\alpha S+\sigma)}",
            tex_template=my_template,
            font_size=40
        ).move_to(ORIGIN)
        R_02 = MathTex(
            r"R_0 \approx \lim_{S \to +\infty} \frac{\beta S \rho}{(\rho+\kappa)(\alpha S+\sigma)}",
            tex_template=my_template,
            font_size=40
        )
        R_03 = MathTex(
            r"R_0 \approx \frac{\beta\rho}{(\rho + \kappa)\alpha}",
            tex_template=my_template,
            font_size=40
        )
        # Show V^{-1}
        self.play(Write(V_inv))
        self.wait(2)

        # Transform to FV^{-1}
        self.play(ReplacementTransform(V_inv, FV_inv))
        self.wait(2)

        # Transform to R_0
        self.play(ReplacementTransform(FV_inv, R_0))
        self.wait(2)
        
        self.play(ReplacementTransform(R_0, R_02))
        self.wait(2)
        self.play(ReplacementTransform(R_02, R_03))
        self.wait(2)
        
