from manim import *

# đổi tỉ lệ 4:3
config.pixel_height = 1080
config.pixel_width = 1440

class LinearTranform(Scene):
    def construct(self):
        #tạo lưới đồ thị
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-5 ,5, 1],
            x_length=14,
            y_length=10,
            tips=True,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )

        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")
        x_label.shift(LEFT*0.2)

        y_label.shift(UP)

        arrow_x = Arrow(
            start=plane.c2p(-7, 0),
            end=plane.c2p(7.2, 0),
            buff=0,
            color=WHITE,
            stroke_width=1
        )

        arrow_y = Arrow(
            start=plane.c2p(0, -5.5),
            end=plane.c2p(0, 5.4),
            buff=0,
            color=WHITE,
            stroke_width=1
        )

        #tạo i^

        arrow_i =  Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(1, 0), 
            color = YELLOW,
            stroke_width=1.5
        ).add_tip(tip_length=0.2, tip_width=0.2)

        #tạo j^

        arrow_j =  Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(0, 1),
            color = RED,
            stroke_width=1.5
        ).add_tip(tip_length=0.2, tip_width=0.2)

        arrow_v =  Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(4, 2),
            color = BLUE,
            stroke_width=1.5
        ).add_tip(tip_length=0.2, tip_width=0.2)


    
        # label for arrow_i
        label_i = MathTex(r"\vec{i}", color=YELLOW).scale(0.7)
        label_i.next_to(arrow_i.get_end(), RIGHT + UP, buff=0.1)

        # label for arrow_j
        label_j = MathTex(r"\vec{j}", color=RED).scale(0.7)
        label_j.next_to(arrow_j.get_end(), UP+ RIGHT, buff=0.1)

        vector_i_tex = MathTex(r"\scriptsize\vec{i} = \begin{bmatrix}1 \\ 0\end{bmatrix},", color=YELLOW).to_corner(UR).shift(LEFT*2)

        arrow_v =  Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(2, 2),
            color = BLUE,
            stroke_width=1.5
        ).add_tip(tip_length=0.2, tip_width=0.2)

        label_v = MathTex(r"\vec{v}", color=BLUE).scale(0.7)
        label_v.next_to(arrow_v.get_end(), UP+ RIGHT, buff=0.1)

        matrix_tex = MathTex(r"\scriptsize I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}",color = YELLOW).move_to(vector_i_tex.get_center() + RIGHT * 0.7 + DOWN*1.25)

        vector_v_ex = MathTex(r"\scriptsize\vec{v} = \begin{bmatrix}2 \\ 2\end{bmatrix}", color = BLUE).next_to(arrow_v, UP*0.7 , buff=0.1)
        

        

        origin_label = MathTex("O").scale(0.7).next_to(plane.c2p(0, 0), DOWN+LEFT, buff=0.1)

        

        
        # 1
        self.add(plane, arrow_i, arrow_j, origin_label, x_label, y_label, arrow_x, arrow_y, label_i, label_j, matrix_tex,vector_v_ex, arrow_v)
        self.wait(3)
        self.play(
            FadeOut(matrix_tex),
            run_time=1
        )
        #2
        exam_tex = MathTex(r"\scriptsize I = \begin{bmatrix}2 & 1 \\ 0 & 2\end{bmatrix}", color = YELLOW).move_to(vector_i_tex.get_center() + RIGHT * 0.7 + DOWN*1.25)
        self.play(Create(exam_tex), run_time=1)

        #3

        T = [[2, 1], [0, 2]]

        self.wait(1)
        self.play(FadeOut(vector_v_ex))
        self.play(
            plane.animate.apply_matrix(T),
            arrow_i.animate.apply_matrix(T),
            arrow_j.animate.apply_matrix(T),
            arrow_v.animate.apply_matrix(T),
            run_time=3
        )
        self.wait(1)
        