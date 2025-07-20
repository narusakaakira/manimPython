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

        # self.add(plane)

        # Biến đổi phi tuyến
        def nonlinear_transform(p):
            x, y = p[:2]
            return np.array([
                x + math.sin(y),
                y + math.log(abs(x) + 1),
                0
            ])

        plane_target = plane.copy()
        plane_target.apply_function(nonlinear_transform)
        # self.play(
        #     Transform(plane, plane_target),
        #     run_time=3
        # )

        
        # origin_transformed = nonlinear_transform(np.array([0, 0, 0]))
        # new_point = Dot(origin_transformed, color=RED)

    

        self.add(plane_target)


        # self.add(plane_target)
        # self.add(new_point)


