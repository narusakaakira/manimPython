from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class jacobianMatrix(Scene):
   def construct(self):
        jacobian = MathTex(
            r"J_{\mathbf{F}}(\mathbf{x}) = \begin{bmatrix}"
            r"\displaystyle \frac{\partial f_1}{\partial x_1} &"
            r"\displaystyle \frac{\partial f_1}{\partial x_2} &"
            r"\cdots &"
            r"\displaystyle \frac{\partial f_1}{\partial x_n} "
            r"\\[12pt]"
            r"\displaystyle \frac{\partial f_2}{\partial x_1} &"
            r"\displaystyle \frac{\partial f_2}{\partial x_2} &"
            r"\cdots &"
            r"\displaystyle \frac{\partial f_2}{\partial x_n} "
            r"\\[12pt]"
            r"\vdots & \vdots & \ddots & \vdots \\[6pt]"
            r"\displaystyle \frac{\partial f_m}{\partial x_1} &"
            r"\displaystyle \frac{\partial f_m}{\partial x_2} &"
            r"\cdots &"
            r"\displaystyle \frac{\partial f_m}{\partial x_n} "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        self.play(Write(jacobian),run_time=3)
        self.wait(2) 
          
