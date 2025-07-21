from manim import *
from manim.utils.tex_templates import TexTemplate
import numpy as np

# LaTeX template hỗ trợ tiếng Việt
my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{amsmath}
\usepackage{vntex}
""")

# Parameters
Pi = 0.01
delta = 0.0001
beta = 0.008
zeta = 0.05
alpha = 0.01

T = 100
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

x = [0, T, 5]
y = [0, 600, 50]

S0, Z0, R0 = 500, 0, 1


def param_tex(val, symbol):
    return MathTex(rf"{symbol} = {val:.4f}", tex_template=my_template).scale(0.5)


class ZombieModel(Scene):
    def compute_euler(self, alpha_val, beta_val, zeta_val):
        S = np.zeros(N + 1)
        Z = np.zeros(N + 1)
        R = np.zeros(N + 1)
        S[0], Z[0], R[0] = S0, Z0, R0

        def derivatives(S, Z, R):
            dS = Pi - beta_val * S * Z - delta * S
            dZ = beta_val * S * Z + zeta_val * R - alpha_val * S * Z
            dR = delta * S + alpha_val * S * Z - zeta_val * R
            return dS, dZ, dR

        for n in range(N):
            dS, dZ, dR = derivatives(S[n], Z[n], R[n])
            S[n + 1] = S[n] + h * dS
            Z[n + 1] = Z[n] + h * dZ
            R[n + 1] = R[n] + h * dR
        return S, Z, R

    def animate_tracker(self, tracker, base_value, delta, run_time=2):
        """
        Animate a tracker: increase by delta → decrease by delta → return to base_value.
        """
        self.play(tracker.animate.set_value(base_value + delta), run_time=run_time, rate_func=smooth)
        self.wait(0.2)
        self.play(tracker.animate.set_value(base_value - delta), run_time=run_time, rate_func=smooth)
        self.wait(0.2)
        self.play(tracker.animate.set_value(base_value), run_time=run_time, rate_func=smooth)
        self.wait(0.5)

    def construct(self):
        # Grid
        plane = NumberPlane(
            x_range=x,
            y_range=y,
            x_length=10,
            y_length=6,
            background_line_style={
                "stroke_color": GREY,
                "stroke_opacity": 0.3,
                "stroke_width": 1,
            }
        ).to_edge(DOWN)
        plane.axes.set_opacity(0)

        # Axes
        axes = Axes(
            x_range=x,
            y_range=y,
            x_length=10,
            y_length=6,
            axis_config={"color": GREY, "include_ticks": True, "include_numbers": True, "font_size": 20},
        ).to_edge(DOWN)

        # Labels
        x_label = Tex(r"\text{Thời gian}", tex_template=my_template).scale(0.5)
        x_label.next_to(axes.x_axis, DOWN)

        y_label = Tex(r"\text{Dân số}", tex_template=my_template).rotate(PI / 2).scale(0.5)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)
        y_label.align_to(axes.y_axis, UP + DOWN)

        # Title
        title = Tex(r"\text{Mô hình Zombie tấn công}", tex_template=my_template, font_size=24).to_edge(UP)

        # Legend
        legend_items = VGroup(
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=BLUE),
                   Tex(r"\text{Người khỏe mạnh}", font_size=18, tex_template=my_template)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=GREEN),
                   Tex(r"\text{Zombies}", font_size=18, tex_template=my_template)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=RED),
                   Tex(r"\text{Đã mất}", font_size=18, tex_template=my_template)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, aligned_edge=UP, buff=0.5)

        legend_items.scale(0.7)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items).next_to(title, DOWN)

        init_values = VGroup(
            MathTex(rf"S_0 = {S0}", font_size=16, tex_template=my_template),
            MathTex(rf"R_0 = {R0}", font_size=16, tex_template=my_template),
            MathTex(rf"Z_0 = {Z0}", font_size=16, tex_template=my_template)
        ).arrange(RIGHT, buff=0.3)

        init_box = SurroundingRectangle(init_values, color=WHITE, buff=0.1)
        init_group = VGroup(init_box, init_values).next_to(legend, DOWN, buff=0.1)

        # Trackers
        alpha_tracker = ValueTracker(alpha)
        beta_tracker = ValueTracker(beta)
        zeta_tracker = ValueTracker(zeta)

        # Static placeholders
        alpha_item_static = param_tex(alpha, r"\alpha")
        beta_item_static = param_tex(beta, r"\beta")
        zeta_item_static = param_tex(zeta, r"\zeta")
        r0_item_static = param_tex(beta / alpha, r"r_0")

        param_items = VGroup(
            alpha_item_static,
            beta_item_static,
            zeta_item_static,
            r0_item_static
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        param_box = SurroundingRectangle(param_items, color=WHITE, buff=0.2)
        param_group = VGroup(param_box, param_items).move_to(axes.c2p(8, 350))

        # Dynamic labels
        alpha_label = always_redraw(lambda:
            param_tex(alpha_tracker.get_value(), r"\alpha").move_to(alpha_item_static)
        )
        beta_label = always_redraw(lambda:
            param_tex(beta_tracker.get_value(), r"\beta").move_to(beta_item_static)
        )
        zeta_label = always_redraw(lambda:
            param_tex(zeta_tracker.get_value(), r"\zeta").move_to(zeta_item_static)
        )
        r0_label = always_redraw(lambda:
            param_tex(beta_tracker.get_value() / alpha_tracker.get_value(), r"r_0").move_to(r0_item_static)
        )

        param_items[0] = alpha_label
        param_items[1] = beta_label
        param_items[2] = zeta_label
        param_items[3] = r0_label

        def make_graph(color, idx):
            return always_redraw(lambda: axes.plot_line_graph(
                x_values=t,
                y_values=self.compute_euler(
                    alpha_tracker.get_value(),
                    beta_tracker.get_value(),
                    zeta_tracker.get_value()
                )[idx],
                line_color=color,
                stroke_width=3,
                add_vertex_dots=False
            ))

        graph_S = make_graph(BLUE, 0)
        graph_Z = make_graph(RED, 1)
        graph_R = make_graph(GREEN, 2)

        self.play(Write(title))
        self.play(Create(plane))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(legend), Create(param_group), Create(init_group))
        self.wait(0.25)

        self.play(Create(graph_S), Create(graph_Z), Create(graph_R), run_time=2)
        self.wait(1)

        self.animate_tracker(alpha_tracker, alpha, 0.003)
        self.animate_tracker(beta_tracker, beta, 0.001)
        self.animate_tracker(zeta_tracker, zeta, 0.03)

        self.wait(1)
