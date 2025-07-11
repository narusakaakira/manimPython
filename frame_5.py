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


        # self.add(plane,plane_after)
        self.add(plane_after)

        # Điểm khảo sát
        point = Dot(plane.c2p(1, 1), color=RED)
        label = MathTex("(1,1)").next_to(point, UP+RIGHT, buff=0.1).scale(0.6)

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

        self.wait(1)

        self.play(
            Transform(plane, plane_target),
            run_time=3
        )
        # self.play(
        #     FadeOut(point, label),
        #     Create(new_point),
        #     Create(new_label),
        #     run_time=0.2
            
        # )
        # self.wait(2)    
