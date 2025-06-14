from manim import *

class Rule1ConstantDerivative(Scene):
    def construct(self):
        rule = MathTex(
            r"\text{If } f(x) = b, \text{ then } f'(x) = 0 \text{ where } b \text{ is a constant.}"
        )
        rule.to_edge(UP)
        self.play(Write(rule))
        self.wait(2)
        self.play(FadeOut(rule))

        
        fx_example = MathTex(r"f(x) = 7")
        self.play(Write(fx_example))
        self.wait(1)
        self.play(FadeOut(fx_example))

        
        example = MathTex(r"\frac{d}{dx}(7) = 0")
        self.play(Write(example))
        self.wait(1)

        const = example.get_part_by_tex("7")
        result = example.get_part_by_tex("0")

        framebox1 = SurroundingRectangle(const, buff=0.1, color=BLUE)
        framebox2 = SurroundingRectangle(result, buff=0.1, color=GREEN)

        self.play(Create(framebox1))
        self.wait(1)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(2)


class Rule2PowerRule(Scene):
    def construct(self):
   
        title = Text("Power Rule of Derivatives", font_size=48)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

      
        formula = MathTex(r"\frac{d}{dx}(x^n) = nx^{n-1}")
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))

        
        example_caption = Text("Example", font_size=42)
        example_caption.to_edge(UP)
        self.play(Transform(title, example_caption))
        self.wait(1)

      
        example = MathTex(r"f(x) = x^3")
        example.move_to(ORIGIN)
        self.play(Write(example))
        self.wait(1)
        self.play(FadeOut(example))

       
        deriv = MathTex(r"\frac{d}{dx}(x^3) = 3x^{2}")
        deriv.move_to(ORIGIN)
        self.play(Write(deriv))
        self.wait(1)

        
        final = MathTex(r"f'(x) = 3x^{2}").set_color(YELLOW)
        final.move_to(ORIGIN)
        self.play(Transform(deriv, final))
        self.wait(2)


from manim import *

class Rule3SumRule(Scene):
    def construct(self):

        title = Text("Sum Rule of Derivatives", font_size=48)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        rule = MathTex("\\frac{d}{dx}[f(x) + g(x)] =", "f'(x)", "+", "g'(x)")
        rule.move_to(ORIGIN)
        self.play(Write(rule))
        rl1 = Underline(rule[1], color=GREEN)
        rl2 = Underline(rule[3], color=GREEN)
        self.play(Create(rl1))
        self.wait(2)
        self.play(ReplacementTransform(rl1, rl2))
        self.play(FadeOut(rule), FadeOut(rl2))

        example_title = Text("Example", font_size=42)
        example_title.to_edge(UP)
        self.play(Transform(title, example_title))
        self.wait(1)

        fx = MathTex("f(x) =", "x^2", "+", "3x")
        fx.move_to(ORIGIN)
        self.play(Write(fx))
        self.wait(2)
        self.play(FadeOut(fx))

        step = MathTex(
            "\\frac{d}{dx}(x^2 + 3x) =", "\\frac{d}{dx}(x^2)", "+", "\\frac{d}{dx}(3x)"
        )
        step.move_to(ORIGIN)
        self.play(Write(step))
        self.wait(3)

        framebox1 = SurroundingRectangle(step[1], buff=0.1)
        framebox2 = SurroundingRectangle(step[3], buff=0.1)

        self.play(Create(framebox1))
        self.wait(1)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(2)
        self.play(FadeOut(step), FadeOut(framebox2))

        final = MathTex(r"f'(x) = 2x + 3").set_color(YELLOW)
        final.move_to(ORIGIN)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))

        axes = Axes(
            x_range=[-4, 4], y_range=[-5, 25],
            x_length=8, y_length=5,
            axis_config={"color": GREY}
        )

        graph_fx = axes.plot(lambda x: x**2 + 3*x, color=BLUE)
        graph_fpx = axes.plot(lambda x: 2*x + 3, color=ORANGE)

        label_fx = axes.get_graph_label(graph_fx, label="x^2 + 3x", direction=UR)
        label_fpx = axes.get_graph_label(graph_fpx, label="2x + 3", direction=DL)

        self.play(Create(axes), Create(graph_fx), Create(graph_fpx))
        self.play(FadeIn(label_fx), FadeIn(label_fpx))
        self.wait(2)

        x_val = 1
        point = axes.c2p(x_val, x_val**2 + 3*x_val)  # f(1) = 1 + 3 = 4
        slope = 2*x_val + 3  # f'(1) = 2(1) + 3 = 5
        dx = 1
        dy = slope * dx

        tangent_line = Line(
            point - np.array([dx, dy, 0]),
            point + np.array([dx, dy, 0]),
            color=YELLOW
        )
        dot = Dot(point, color=YELLOW)

        self.play(FadeIn(dot), Create(tangent_line))
        self.wait(3)


from manim import *
import numpy as np

class Rule3DifferenceRule(Scene):
    def construct(self):
       
        title = Text("Difference Rule of Derivatives", font_size=48)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        
        rule = MathTex(r"\frac{d}{dx}[f(x) - g(x)] =", "f'(x)", "-", "g'(x)")
        rule.move_to(ORIGIN)
        self.play(Write(rule))
        rl1 = Underline(rule[1], color=GREEN)
        rl2 = Underline(rule[3], color=RED)
        self.play(Create(rl1))
        self.wait(1)
        self.play(ReplacementTransform(rl1, rl2))
        self.wait(1)
        self.play(FadeOut(rule), FadeOut(rl2))

        
        example_title = Text("Example", font_size=42)
        example_title.to_edge(UP)
        self.play(Transform(title, example_title))
        self.wait(1)

       
        fx = MathTex(r"f(x) = x^3 - \ln(x)")
        fx.move_to(ORIGIN)
        self.play(Write(fx))
        self.wait(2)
        self.play(FadeOut(fx))

        
        step = MathTex(
            "\\frac{d}{dx}(x^3 - \ln(x)) =", "\\frac{d}{dx}(x^3)", "-", "\\frac{d}{dx}(\ln(x))"
        )
        step.move_to(ORIGIN)
        self.play(Write(step))
        self.wait(2)

        framebox1 = SurroundingRectangle(step[1], buff=0.1)
        framebox2 = SurroundingRectangle(step[3], buff=0.1)

        self.play(Create(framebox1))
        self.wait(1)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(1)
        self.play(FadeOut(step), FadeOut(framebox2))

        
        final = MathTex(r"f'(x) = 3x^2 - \frac{1}{x}").set_color(YELLOW)
        final.move_to(ORIGIN)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))

        
        axes = Axes(
            x_range=[0.1, 3], y_range=[-1, 30],
            x_length=8, y_length=5,
            axis_config={"color": GREY}
        )

        graph_fx = axes.plot(lambda x: x**3 - np.log(x), color=PURPLE_B)
        graph_fpx = axes.plot(lambda x: 3*x**2 - 1/x, color=TEAL)

        label_fx = axes.get_graph_label(graph_fx, label="x^3 - ln(x)", direction=UR)
        label_fpx = axes.get_graph_label(graph_fpx, label="3x^2 - 1/x", direction=DL)

        self.play(Create(axes), Create(graph_fx), Create(graph_fpx))
        self.play(FadeIn(label_fx), FadeIn(label_fpx))
        self.wait(2)

        
        x_val = 1
        f_val = x_val**3 - np.log(x_val)
        slope = 3*x_val**2 - 1/x_val  # f'(1) = 3 - 1 = 2
        point = axes.c2p(x_val, f_val)

        dx = 1
        dy = slope * dx

        tangent_line = Line(
            point - np.array([dx, dy, 0]),
            point + np.array([dx, dy, 0]),
            color=ORANGE
        )
        dot = Dot(point, color=ORANGE)

        self.play(FadeIn(dot), Create(tangent_line))
        self.wait(3)


class ConstantMultipleRule(Scene):
    def construct(self):
        title = Text("Constant Multiple Rule", font_size=48)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        rule = MathTex(r"\frac{d}{dx}[k \cdot f(x)]", "=", r"k \cdot f'(x)")
        rule.move_to(ORIGIN)
        self.play(Write(rule))
        self.wait(2)
        self.play(FadeOut(rule))

        example_caption = Text("Example", font_size=42)
        example_caption.to_edge(UP)
        self.play(Transform(title, example_caption))
        self.wait(1)

        func = MathTex(r"f(x)=5x^3")
        func.move_to(ORIGIN)
        self.play(Write(func))
        self.wait(1)
        self.play(FadeOut(func))

        step = MathTex(r"\frac{d}{dx}(5x^3) = 5 \cdot \frac{d}{dx}(x^3)")
        step.move_to(ORIGIN)
        self.play(Write(step))
        self.wait(1)
        self.play(FadeOut(step))

        final = MathTex(r"f'(x)=15x^2")
        final.set_color_by_tex("15x^2", YELLOW)
        final.move_to(ORIGIN)
        self.play(Write(final))
        self.wait(2)