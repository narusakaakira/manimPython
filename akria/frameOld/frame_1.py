from manim import *

# đổi tỉ lệ 4:3
config.pixel_height = 1080
config.pixel_width = 1440

class GridWithManualArrows(Scene):
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



        vector_i_tex = MathTex(r"\scriptsize\vec{i} = \begin{bmatrix}1 \\ 0\end{bmatrix},", color=YELLOW).to_corner(UR).shift(LEFT*2)
        vector_j_tex = MathTex(r"\scriptsize\vec{j} = \begin{bmatrix}0 \\ 1\end{bmatrix}", color=RED).next_to(vector_i_tex, RIGHT*2)

    
        # label for arrow_i
        label_i = MathTex(r"\vec{i}", color=YELLOW).scale(0.7)
        label_i.next_to(arrow_i.get_end(), RIGHT + UP, buff=0.1)

        # label for arrow_j
        label_j = MathTex(r"\vec{j}", color=RED).scale(0.7)
        label_j.next_to(arrow_j.get_end(), UP+ RIGHT, buff=0.1)

        vector_v_ex = MathTex(r"\scriptsize\vec{v} = \begin{bmatrix}4 \\ 2\end{bmatrix}", color=BLUE).to_corner(UR).shift(LEFT*2, DOWN*0.5)

        label_v = MathTex(r"\vec{v}", color=BLUE).scale(0.7)
        label_v.next_to(arrow_v.get_end(), UP+ RIGHT, buff=0.1)
        

        

        origin_label = MathTex("O").scale(0.7).next_to(plane.c2p(0, 0), DOWN+LEFT, buff=0.1)
        


        self.play(Create(plane), run_time=1)
        self.play(Create(arrow_x), run_time=1)
        self.play(Create(arrow_y), run_time=1)
        self.play(Create(origin_label),run_time=1)
        self.play(Create(x_label), run_time=1)
        self.play(Create(y_label), run_time=1)
        self.play(Create(arrow_i), run_time=1)
        self.play(Write(label_i), run_time=0.5)
        self.wait()
        self.play(Create(arrow_j), run_time=1)
        self.play(Write(label_j), run_time=0.5)
        self.wait(1)
        self.play(Create(VGroup(vector_i_tex, vector_j_tex)), run_time=3)


        matrix_tex = MathTex(r"\scriptsize I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}").move_to(vector_i_tex.get_center() + RIGHT * 0.5)
        self.play(
            ReplacementTransform(
                VGroup(vector_i_tex, vector_j_tex),
                matrix_tex
            )
        )
        self.wait(1)
        vector_v= MathTex(r"\scriptsize\overrightarrow{v} = \begin{bmatrix}x\\y\end{bmatrix}").next_to(matrix_tex,DOWN*2)
        self.play(Create(vector_v), runtime=1)
        self.wait(2)
        self.play(
            FadeOut(vector_v),
            FadeOut(matrix_tex),
            run_time=1
        )
                # Bước 1: Hiển thị tích ma trận: Iv
        dot_product_tex = MathTex(
            r"\scriptsize I \cdot \overrightarrow{v} = ",
        ).next_to(matrix_tex, DOWN*0.25 + LEFT*1, buff=0.8)

        self.play(Write(dot_product_tex), run_time=1)

        # Bước 2: Hiển thị biểu thức đầy đủ
        multiplication_tex = MathTex(
            r"\scriptsize\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix} \cdot \begin{bmatrix}x\\y\end{bmatrix}",
        ).next_to(dot_product_tex, RIGHT, buff=0.3)

        self.play(Write(multiplication_tex), run_time=2)

        #Bước 3: Biến đổi
        result_tex = MathTex(r"\scriptsize = \begin{bmatrix}1 \\ 0 \end{bmatrix} \cdot x + \begin{bmatrix}0 \\ 1 \end{bmatrix} \cdot y = \begin{bmatrix}x\\y\end{bmatrix}  ",).next_to(multiplication_tex, DOWN, buff=0.3)

        self.play(Write(result_tex), run_time=1.5)
        self.wait(3)

        self.play(
            FadeOut(dot_product_tex, multiplication_tex, result_tex),
            run_time=1
        )
        self.play(Create(arrow_v), run_time=1)
        self.play(Write(vector_v_ex), run_time=1)
        self.wait()




