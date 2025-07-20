from manim import *
import numpy as np

# Parameters
Pi = 0.01
delta = 0.0001
beta = 0.0095
zeta = 0.1
alpha = 0.0005

T = 20
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

S0, Z0, R0 = 5, 0, 1


def param_tex(val, symbol):
    return MathTex(rf"{symbol} = {val:.4f}").scale(0.5)


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

    def construct(self):
        # Grid
        plane = NumberPlane(
            x_range=[0, T, 2.5],
            y_range=[0, 200, 25],
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
            x_range=[0, 20, 2.5],
            y_range=[0, 200, 25],
            x_length=10,
            y_length=6,
            axis_config={"color": GREY, "include_ticks": True, "include_numbers": True, "font_size": 20},
        ).to_edge(DOWN)

        # Labels
        x_label = axes.get_x_axis_label("Time", direction=DOWN).scale(0.5)
        y_label = Text("Population", font_size=20).rotate(PI / 2)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)
        y_label.align_to(axes.y_axis, UP + DOWN)

        # Title
        title = Text("When Zombies Attack!", font_size=24).to_edge(UP)

        # Legend
        legend_items = VGroup(
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=BLUE), Text("Susceptibles", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=GREEN), Text("Zombies", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=RED), Text("Removed", font_size=18)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, aligned_edge=UP, buff=0.5)

        legend_items.scale(0.7)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items).next_to(title, DOWN)

        # Trackers
        alpha_tracker = ValueTracker(alpha)
        beta_tracker = ValueTracker(beta)
        zeta_tracker = ValueTracker(zeta)

        # Static placeholders
        alpha_item_static = param_tex(alpha, r"\alpha")
        beta_item_static = param_tex(beta, r"\beta")
        zeta_item_static = param_tex(zeta, r"\zeta")

        param_items = VGroup(
            alpha_item_static,
            beta_item_static,
            zeta_item_static,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        param_box = SurroundingRectangle(param_items, color=WHITE, buff=0.2)
        param_group = VGroup(param_box, param_items).move_to(axes.c2p(2, 150))

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

        param_items[0] = alpha_label
        param_items[1] = beta_label
        param_items[2] = zeta_label

        # Graphs
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

        # Animation sequence
        self.play(Write(title))
        self.play(Create(plane))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(legend), Create(param_group))
        self.wait(0.5)

        self.play(Create(graph_S), Create(graph_Z), Create(graph_R))
        self.wait(1)

        # Animate alpha over 5s
        self.play(
            alpha_tracker.animate.set_value(alpha * 20),
            run_time=5,
            rate_func=smooth
        )
        self.wait(0.5)

        # Animate beta over 5s
        self.play(
            beta_tracker.animate.set_value(beta * 20),
            run_time=5,
            rate_func=smooth
        )
        self.wait(0.5)

        # Animate zeta over 5s
        self.play(
            zeta_tracker.animate.set_value(zeta * 20),
            run_time=5,
            rate_func=smooth
        )
        self.wait(1)
