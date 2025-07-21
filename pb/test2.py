from manim import *
import numpy as np
# from manim import config

# config["quality"] = "low_quality"
# config["frame_rate"] = 15 
# Parameters
Pi = 0.01
delta = 0.0001
beta = 0.02
zeta = 0.05
alpha = 0.01
rho = 0.05

T = 100
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

x =[0, T, 5]
y =[0, 600, 50]

S0, Z0, R0, I0 = 500, 0, 1, 0


def param_tex(val, symbol):
    return MathTex(rf"{symbol} = {val:.4f}").scale(0.4)


class ZombieModelWithInfected(Scene):
    def compute_euler(self, alpha_val, beta_val, zeta_val, rho_val):
        S = np.zeros(N + 1)
        Z = np.zeros(N + 1)
        R = np.zeros(N + 1)
        I = np.zeros(N + 1)
        S[0], Z[0], R[0], I[0] = S0, Z0, R0, I0

        def derivatives(S, I, Z, R):
            dS = Pi - beta_val * S * Z - delta * S
            dI = beta_val * S * Z - rho_val * I - delta * I
            dZ = rho_val * I + zeta_val * R - alpha_val * S * Z
            dR = delta * S + delta * I + alpha_val * S * Z - zeta_val * R
            return dS, dI, dZ, dR

        for n in range(N):
            dS, dI, dZ, dR = derivatives(S[n], I[n], Z[n], R[n])
            S[n + 1] = S[n] + h * dS
            I[n + 1] = I[n] + h * dI
            Z[n + 1] = Z[n] + h * dZ
            R[n + 1] = R[n] + h * dR
        return S, I, Z, R
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

        title = Text("Euler Method: S-I-Z-R model", font_size=24).to_edge(UP)

        legend_items = VGroup(
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=BLUE), Text("Susceptibles", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=ORANGE), Text("Infected", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=GREEN), Text("Zombies", font_size=18)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.2, RIGHT * 0.2, color=RED), Text("Removed", font_size=18)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, aligned_edge=UP, buff=0.5)

        legend_items.scale(0.7)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items).next_to(title, DOWN)

        init_values = VGroup(
            MathTex(rf"S0 = {S0}", font_size=16),
            MathTex(rf"R0 = {R0}", font_size=16),
            MathTex(rf"Z0 = {Z0}", font_size=16)
        ).arrange(RIGHT, buff=0.3)

        init_box = SurroundingRectangle(init_values, color=WHITE, buff=0.1)
        init_group = VGroup(init_box, init_values).next_to(legend, DOWN, buff=0.1)
        alpha_tracker = ValueTracker(alpha)
        beta_tracker = ValueTracker(beta)
        zeta_tracker = ValueTracker(zeta)
        rho_tracker = ValueTracker(rho)

        param_items_static = VGroup(
            param_tex(alpha, r"\alpha"),
            param_tex(beta, r"\beta"),
            param_tex(beta / alpha, r"r_0"),
            param_tex(zeta, r"\zeta"),
            param_tex(rho, r"\rho"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        param_box = SurroundingRectangle(param_items_static, color=WHITE, buff=0.2)
        param_group = VGroup(param_box, param_items_static).move_to(axes.c2p(7, 400))

        dynamic_labels = [
            always_redraw(lambda:
                param_tex(alpha_tracker.get_value(), r"\alpha").move_to(param_items_static[0])
            ),
            always_redraw(lambda:
                param_tex(beta_tracker.get_value(), r"\beta").move_to(param_items_static[1])
            ),
            always_redraw(lambda:
                param_tex(beta_tracker.get_value() / alpha_tracker.get_value(), r"r_0").move_to(param_items_static[2])
            ),
            always_redraw(lambda:
                param_tex(zeta_tracker.get_value(), r"\zeta").move_to(param_items_static[3])
            ),
            always_redraw(lambda:
                param_tex(rho_tracker.get_value(), r"\rho").move_to(param_items_static[4])
            )
        ]

        for i in range(4):
            param_items_static[i] = dynamic_labels[i]

        def make_graph(color, idx):
            return always_redraw(lambda: axes.plot_line_graph(
                x_values=t,
                y_values=self.compute_euler(
                    alpha_tracker.get_value(),
                    beta_tracker.get_value(),
                    zeta_tracker.get_value(),
                    rho_tracker.get_value()
                )[idx],
                line_color=color,
                stroke_width=3,
                add_vertex_dots=False
            ))

        graph_S = make_graph(BLUE, 0)
        graph_I = make_graph(ORANGE, 1)
        graph_Z = make_graph(RED, 2)
        graph_R = make_graph(GREEN, 3)

        self.play(Write(title))
        self.play(Create(plane))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(legend), Create(param_group), Create(init_group))
        self.wait(0.5)

        self.play(Create(graph_S), Create(graph_I), Create(graph_Z), Create(graph_R),run_time=2)
        self.wait(1)
        
        self.animate_tracker(alpha_tracker, alpha, 0.003)
        self.animate_tracker(beta_tracker, beta, 0.01)
        self.animate_tracker(zeta_tracker, zeta, 0.03)
        self.animate_tracker(rho_tracker, rho, 0.03)
        self.wait(1)
        