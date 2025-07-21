from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class equilibriumPoint(Scene):
   def construct(self):
          

        SysEquation = MathTex(
            r"0 &= -\beta S Z \\",
            r"0 &= \beta S Z+ \zeta R - \alpha S Z \\",
            r"0 &= \delta S + \alpha S Z - \zeta R.",
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)


        Intro = Tex(r"Trở lại với mô hình, xét tại điểm cân bằng ta sẽ có hệ phương trình như sau",
            tex_template=my_template,
            font_size=30

        ).next_to(SysEquation, UP)


     
        Description = Tex(r"Giải hệ này, ta sẽ được các giá trị tức thời của $S$, $Z$, $R$ tại điểm cân bằng là:", 
            tex_template=my_template,
            font_size=36
        ).move_to(ORIGIN)

        Result = MathTex(r"(\overline{S}, \overline{Z}, \overline{R}) \in \{(\overline{S} ,0,0),(0,\overline{Z} ,0)\}", 
            tex_template=my_template,
            font_size=36
        ).next_to(Description, DOWN)



        
        self.play(Write(Intro))
        self.wait(1)
        self.play(Write(SysEquation))
        self.play(
            FadeOut(Intro),
            FadeOut(SysEquation)
        )
        self.wait()
        self.play(
            FadeIn(Description),
            run_time=2
        )
        self.wait(1)
        self.play(Write(Result))
        self.wait()

