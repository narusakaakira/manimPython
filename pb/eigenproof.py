from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class EigenvalueProof(Scene):
    def construct(self):
        font_size = 34

        step1 = Tex(
            r"Vậy còn nếu $\lambda = \beta \overline{Z}$ thì sao? "
            r"Ta sẽ chứng minh rằng đây không phải là giá trị riêng của hệ. "
            r"Xét phương trình giá trị riêng: \\[10pt]"
            r"$(J-\lambda I)v=0$ với $\lambda=\beta\overline{Z}$. Khi đó:",
            tex_template=my_template,
            font_size=font_size
        )

        step2 = MathTex(
            r"J-\lambda I = "
            r"\begin{bmatrix} "
            r"0 & 0 & -\beta S+c & 0 \\ "
            r"\beta Z & -\rho-\beta Z & \beta S & 0 \\ "
            r"-\alpha Z & \rho & -\alpha S-c-\beta Z & \zeta \\ "
            r"\alpha Z & 0 & \alpha S & -\zeta-\beta Z "
            r"\end{bmatrix}",
            tex_template=my_template,
            font_size=font_size
        )

        step3 = Tex(
            r"Gọi $v=\begin{bmatrix}v_1\\v_2\\v_3\\v_4\end{bmatrix}$, ta có hệ:",
            tex_template=my_template,
            font_size=font_size
        )

        step4 = MathTex(
            r"(J-\lambda I)v = "
            r"\begin{bmatrix} "
            r"(-\beta S+c)v_3 \\ "
            r"\beta Zv_1+(-\rho-\beta Z)v_2+\beta Sv_3 \\ "
            r"-\alpha Zv_1+\rho v_2+(-\alpha S-c-\beta Z)v_3+\zeta v_4 \\ "
            r"\alpha Zv_1+\alpha Sv_3+(-\zeta-\beta Z)v_4 "
            r"\end{bmatrix} = "
            r"\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}",
            tex_template=my_template,
            font_size=font_size
        )

        step5 = Tex(
            r"Từ phương trình hàng thứ nhất: $(-\beta S+c)v_3=0$ "
            r"Giả sử $c\neq\beta S$, ta có $v_3=0$. \\"
            r"Khi đó phương trình hàng 2 và 4 cho ta:",
            tex_template=my_template,
            font_size=font_size
        )

        step6 = MathTex(
            r"v_2 = \frac{\beta Z}{\rho+\beta Z}v_1, \quad "
            r"v_4 = \frac{\alpha Z}{\zeta+\beta Z}v_1",
            tex_template=my_template,
            font_size=font_size
        )

        step7 = Tex(
            r"Thay vào hàng 3 ta được:",
            tex_template=my_template,
            font_size=font_size
        )

        step8 = MathTex(
            r"v_1 \cdot \bigg( -\alpha Z+\frac{\alpha Z\zeta}{\zeta+\beta Z}+\rho\cdot\frac{\beta Z}{\rho+\beta Z} \bigg)=0",
            tex_template=my_template,
            font_size=font_size
        )

        step9 = Tex(
            r"Với các tham số dương, hệ số khác 0, nên $v_1=0$. \\"
            r"Từ đó $v_2=v_3=v_4=0$. \\"
            r"Vậy $\lambda=\beta\overline{Z}$ không phải là giá trị riêng của $J$.",
            tex_template=my_template,
            font_size=font_size
        )

        steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9]

        steps[0].move_to(ORIGIN)

        # Hiển thị từng bước
        self.play(Write(steps[0]), run_time=5)
        self.wait(1)

        for i in range(1, len(steps)):
            steps[i].move_to(ORIGIN)
            self.play(ReplacementTransform(steps[i-1], steps[i]))
            self.wait(5 )

        self.wait(2)
