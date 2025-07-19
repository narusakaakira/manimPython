from manim import *
my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
""")
class SZRLabels(Scene):
    def construct(self):
        # Tiêu đề
        title = Text("Các trạng thái trong mô hình SZR", font_size=30).to_edge(UP)
        self.play(Write(title))

        # Các item
        items = VGroup(
            Tex(r" Người khỏe mạnh, Susceptible $(S)$", tex_template=my_template, color = YELLOW),
            Tex(r" Người nhiễm bệnh, Zombie $(Z)$",tex_template=my_template, color = YELLOW),
            Tex(r" Người đã chết, Removed $(R)$", tex_template=my_template, color = YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        items2 = VGroup(
            Tex(r"$\delta$: tỉ lệ tử vong của người khỏe mạnh qua những nguyên nhân non-zombie", tex_template=my_template, color=YELLOW,font_size=38),
            Tex(r"$\zeta$: tỉ lệ người đã chết trở thành Zombie", tex_template=my_template, color=YELLOW,font_size=38),
            Tex(r"$\beta$: tỉ lệ người khỏe mạnh trở thành Zombie", tex_template=my_template, color=YELLOW,font_size=38),
            Tex(r"$\alpha$: tỉ lệ Zombie bị tiêu diệt", tex_template=my_template, color=YELLOW,font_size=38),
            Tex(r"$\Pi$: tỉ lệ sinh tự nhiên của con người", tex_template=my_template, color=YELLOW,font_size=38)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        # Hiển thị từng item
        note = Tex(
            r"``Tỉ lệ'' ta sẽ quy ước là ``tỉ lệ thay đổi trên mỗi đơn vị thời gian, tức là $1t$'', hay là ``tốc độ''",
            tex_template=my_template,
            font_size=38
        ).move_to(ORIGIN)


        for item in items:
            self.play(FadeIn(item, shift=RIGHT))
            self.wait(2)
        self.wait(5)
        for item in items:
            self.play(FadeOut(item))
        self.play(FadeOut(title))
        self.wait(2)
    
        for item in items2:
            self.play(FadeIn(item, shift=RIGHT))
            self.wait(2)
        
        self.wait(5)
        for item in items2:
            self.play(FadeOut(item))
        self.play(FadeIn(note, shift=RIGHT))
        self.wait(4)
        self.play(FadeOut(note))
        