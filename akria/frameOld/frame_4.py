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
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            x_length=14,
            y_length=10,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_opacity": 2,
                "stroke_width": 1
            }
        )
        plane_after = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            x_length=14,
            y_length=10,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.7,
                "stroke_width": 1
            }
        )


        self.add(plane,plane_after)

        # Điểm khảo sát
        point = Dot(plane.c2p(1, 1), color=RED)
        label = MathTex("(1,1)").next_to(point, UP+RIGHT, buff=0.1).scale(0.6)
        self.add(point, label)

        new_point = Dot(plane.c2p(1.841470985, 1.693147181), color=RED)
        new_label = MathTex("(1.84,1.69)").next_to(point, UP+RIGHT, buff=0.1).scale(0.6)
        



        # Biến đổi phi tuyến
        def nonlinear_transform(p):
            x, y = p[:2]
            return np.array([
                x + math.sin(y),
                y + math.log(abs(x) + 1),
                0
            ])

        # Tạo bản sao plane & point
        plane_target = plane.copy()
        point_target = point.copy()
        label_target = label.copy()

        # Áp dụng biến đổi cho plane
        plane_target.apply_function(nonlinear_transform)
        # Áp dụng biến đổi cho point
        point_target.move_to(nonlinear_transform(plane.p2c(point.get_center())))
        label_target.next_to(point_target, UP+RIGHT, buff=0.1)

        # Text chú thích
        # text = Tex(
        #     r"\text{Biến đổi phi tuyến: } T(x,y) = (x+\sin(y), y+\sin(x))",
        #     tex_template=my_template
        # ).to_edge(UP).scale(0.7)
        
        text_1 = MathTex(r"\text{Biến đổi phi tuyến:} T(x,y) = \begin{bmatrix}x+\sin(y) \\ y+\ln(|x|+1) \end{bmatrix}", tex_template=my_template, color = YELLOW).move_to(UP*3.2)
        # box = SurroundingRectangle(text_1, color=WHITE, buff=0.4, BackgroundColoredVMobjectDisplayer=BLACK)
        self.play(Create(text_1))

        # banner = Rectangle(
        #     width=14,
        #     height=1.5,
        #     fill_color=BLACK,
        #     fill_opacity=1,
        #     stroke_opacity=0
        # ).to_edge(UP*0.000000005)


        # self.wait(1)
        # self.add(banner, text_1)
        # self.wait(2)


        # Animate biến đổi
        self.wait(1)

        self.play(
            Transform(plane, plane_target),
            Transform(point, point_target),
            Transform(label, label_target),
            run_time=3
        )
        self.play(
            FadeOut(point, label),
            Create(new_point),
            Create(new_label),
            run_time=0.2
            
        )
        self.wait(2)    
