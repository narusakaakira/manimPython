from manim import *

class FUV(Scene):
    def construct(self):
        # Trục toạ độ
        axes = Axes(
            x_range=[0, 4],
            y_range=[0, 4],
            x_length=5,
            y_length=5,
            axis_config={"include_tip": True}
        ).shift(LEFT*2)

        labels = axes.get_axis_labels("I", "Z")

        # Véc-tơ ban đầu
        vec_init = Arrow(axes.c2p(0, 0), axes.c2p(1, 1), color=WHITE, buff=0)
        label_init = MathTex(r"\vec{u}_0", font_size=30).next_to(vec_init.get_end(), UL)

        self.play(Create(axes), Write(labels))
        self.play(GrowArrow(vec_init), FadeIn(label_init))
        self.wait(1)

        # Véc-tơ F - V
        vec_F_minus_V = Arrow(axes.c2p(0, 0), axes.c2p(2, 1.5), color=BLUE, buff=0)
        label_F_minus_V = MathTex(r"(F - V) \vec{u}_0", font_size=28, color=BLUE).next_to(vec_F_minus_V.get_end(), UR)

        # Véc-tơ F V^{-1}
        vec_FVinv = Arrow(axes.c2p(0, 0), axes.c2p(3, 2.5), color=RED, buff=0)
        label_FVinv = MathTex(r"F V^{-1} \vec{u}_0", font_size=28, color=RED).next_to(vec_FVinv.get_end(), UR)

        # Hiện chú giải
        legend = VGroup(
            Dot(color=BLUE).next_to(axes, RIGHT, buff=1),
            Text("Tốc độ tức thời (F - V)", font_size=24, color=BLUE).next_to(axes, RIGHT, buff=1).shift(DOWN*0.2 + RIGHT*0.4),
            Dot(color=RED).next_to(axes, RIGHT, buff=1).shift(DOWN*0.5),
            Text("Số ca mới (F V^{-1})", font_size=24, color=RED).next_to(axes, RIGHT, buff=1).shift(DOWN*0.7 + RIGHT*0.4),
        )

        self.play(GrowArrow(vec_F_minus_V), FadeIn(label_F_minus_V))
        self.wait(1)

        self.play(GrowArrow(vec_FVinv), FadeIn(label_FVinv))
        self.wait(1)

        self.play(FadeIn(legend))
        self.wait(2)
