from manim import *
import numpy as np
import math

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")

class NonlinearTransform(Scene):
    def construct(self):
        # Lưới tọa độ ban đầu
        plane = NumberPlane(
            x_range=[-7, 7, 0.25],
            y_range=[-5, 5, 0.25],
            x_length=14,
            y_length=10,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_opacity": 2,
                "stroke_width": 1
            }
        )
        
        # Biến đổi phi tuyến
        def nonlinear_transform(p):
            x, y = p[:2]
            return np.array([
                x + math.sin(y),
                y + math.log(abs(x) + 1),
                0
            ])
        
        image = ImageMobject("./assets/frame_5_1.png")
        image.scale(0.7)
        image.to_corner(UR)
        
        target_point = np.array([-2.75, 2.5, 0])  # (x=3, y=1)
        rect = Rectangle(
            width=2,        # chiều rộng
            height=1.5,       # chiều cao
            color=YELLOW,     # màu viền
            fill_color=BLUE_E, 
            fill_opacity=0
        ).move_to(target_point)

        

        rect_after = Rectangle(
            width=image.width,        # chiều rộng
            height=image.height,          # chiều cao
            color=YELLOW,     # màu viền
            fill_color=BLUE_E, 
            fill_opacity=0

        ).move_to(image.get_center())

        rect_down = Rectangle(
            width=10,        # chiều rộng
            height=1.4,          # chiều cao
            color=BLACK,     # màu viền
            fill_opacity=1

        ).to_corner(DOWN).shift(DOWN*0.5)

        midpoint = rect_after.get_left()
        arrow = Arrow(
            start=plane.c2p(-1.75, 2.5),
            end=midpoint,
            buff=0,
            color=YELLOW,
            stroke_width=3
        )

        text_1 = MathTex(r"\text{Biến đổi phi tuyến:} T\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}x+\sin(y) \\ y+\ln(|x|+1) \end{bmatrix}", tex_template=my_template, color = YELLOW).to_corner(DOWN).shift(DOWN*0.5)



        plane_target = plane.copy()
        plane_target.apply_function(nonlinear_transform)

        self.add(plane)
        self.add(rect_down)
        self.play(Create(text_1))

        self.play(
            Create(rect),
        )
        
        self.play(
            Transform(plane, plane_target),
            run_time=3
        )
        self.play(
                        Create(arrow),
            FadeIn(image),
            Create(rect_after),
            runtime=2
        )
        # self.play(
        #     FadeOut(plane_after),
        #     run_time=3
        # )

        
        self.wait(2)    
