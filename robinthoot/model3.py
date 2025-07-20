from manim import *
import numpy as np

# Parameters
Pi = 0.01
delta = 0.0001
beta = 0.0095
zeta = 0.1
alpha = 0.0005
rho = 0.2
kappa = 0.05
sigma = 0.04
gamma = 0.02

T = 20
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

x = [0, T, 2.5]
y = [0, 600, 50]

S0, Z0, R0, I0, Q0 = 500, 0, 1, 0, 0


def param_tex(val, symbol):
    return MathTex(rf"{symbol} = {val:.4f}").scale(0.5)


class ZombieModelWithQuarantine(Scene):
    def compute_euler(self, alpha_val, beta_val, zeta_val, rho_val, kappa_val, sigma_val, gamma_val):
        S = np.zeros(N + 1)
        I = np.zeros(N + 1)
        Z = np.zeros(N + 1)
        R = np.zeros(N + 1)
        Q = np.zeros(N + 1)
        S[0], I[0], Z[0], R[0], Q[0] = S0, I0, Z0, R0, Q0

        def derivatives(S, I, Z, R, Q):
            dS = Pi - beta_val * S * Z - delta * S
            dI = beta_val * S * Z - rho_val * I - delta * I - kappa_val * I
            dZ = rho_val * I + zeta_val * R - alpha_val * S * Z - sigma_val * Z
            dR = delta * S + delta * I + alpha_val * S * Z - zeta_val * R + gamma_val * Q
            dQ = kappa_val * I + sigma_val * Z - gamma_val * Q
            return dS, dI, dZ, dR, dQ

        for n in range(N):
            dS, dI, dZ, dR, dQ = derivatives(S[n], I[n], Z[n], R[n], Q[n])
            S[n + 1] = S[n] + h * dS
            I[n + 1] = I[n] + h * dI
            Z[n + 1] = Z[n] + h * dZ
            R[n + 1] = R[n] + h * dR
            Q[n + 1] = Q[n] + h * dQ
        return S, I, Z, R, Q

    def construct(self):
        plane = NumberPlane(
            x_range=x,
            y_range=y,
            y_length=6,
            background_line_style={
                "stroke_color": GREY,
                "stroke_opacity": 0.3,
                "stroke_width": 1,
            }
        ).to_edge(DOWN)
        plane.axes.set_opacity(0)

        axes = Axes(
            x_range=x,
            y_range=y,
            x_length=10,
            y_length=6,
            axis_config={"color": GREY, "include_ticks": True, "include_numbers": True, "font_size": 20},
        ).to_edge(DOWN)

        x_label = axes.get_x_axis_label("Time", direction=DOWN).scale(0.5)
        y_label = Text("Population", font_size=20).rotate(PI / 2)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)
        y_label.align_to(axes.y_axis, UP + DOWN)

        title = Text("Euler Method: S-I-Z-R-Q dynamics", font_size=24).to_edge(UP)

        legend_items = VGroup(
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=BLUE), Text("Susceptibles", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=ORANGE), Text("Infected", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=GREEN), Text("Zombies", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=RED), Text("Removed", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=PURPLE), Text("Quarantined", font_size=18)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, aligned_edge=UP, buff=0.5)

        legend_items.scale(0.7)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items).next_to(title, DOWN)

        trackers = [
            ValueTracker(alpha),
            ValueTracker(beta),
            ValueTracker(zeta),
            ValueTracker(rho),
            ValueTracker(kappa),
            ValueTracker(sigma),
            ValueTracker(gamma),
        ]
        symbols = [r"\alpha", r"\beta", r"\zeta", r"\rho", r"\kappa", r"\sigma", r"\gamma"]

        param_items_static = VGroup(
            *[param_tex(val, sym) for val, sym in zip(
                [alpha, beta, zeta, rho, kappa, sigma, gamma], symbols
            )]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        param_box = SurroundingRectangle(param_items_static, color=WHITE, buff=0.2)
        param_group = VGroup(param_box, param_items_static).move_to(axes.c2p(2, 300))

        for i, tracker in enumerate(trackers):
            param_items_static[i] = always_redraw(lambda i=i:
                param_tex(trackers[i].get_value(), symbols[i]).move_to(param_items_static[i])
            )

        def make_graph(color, idx):
            return always_redraw(lambda: axes.plot_line_graph(
                x_values=t,
                y_values=self.compute_euler(*[tr.get_value() for tr in trackers])[idx],
                line_color=color,
                stroke_width=3,
                add_vertex_dots=False
            ))

        graph_S = make_graph(BLUE, 0)
        graph_I = make_graph(ORANGE, 1)
        graph_Z = make_graph(GREEN, 2)
        graph_R = make_graph(RED, 3)
        graph_Q = make_graph(PURPLE, 4)

        self.play(Write(title))
        self.play(Create(plane))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(legend), Create(param_group))
        self.wait(0.5)

        self.play(Create(graph_S), Create(graph_I), Create(graph_Z), Create(graph_R), Create(graph_Q),run_time=2)
        self.wait(1)
