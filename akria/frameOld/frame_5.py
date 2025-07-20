from manim import *

class GridWithBox(Scene):
    def construct(self):
        # Tạo hệ trục với lưới
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=6,
            tips=False,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 24},
        ).add_coordinates()

        # Tạo lưới phụ (subgrid)
        sub_grid = NumberPlane(
            x_range=[-4, 4, 0.25],
            y_range=[-2, 4, 0.25],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_B,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5,
            },
        )

        # Lưới chính
        main_grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.5,
                "stroke_opacity": 1,
            },
        )

        # Hộp vuông nhỏ nổi bật tại (-2, 1)
        highlight_box = Square(side_length=0.5, color=YELLOW, stroke_width=2)
        highlight_box.move_to(axes.c2p(-2, 1))

        # Đưa các đối tượng lên màn hình
        self.add(sub_grid, main_grid, axes, highlight_box)