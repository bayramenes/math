from manim import *
import numpy as np




class WriteIntroTurkish(Scene):
    def construct(self):
        title = Text("Kalkülüs 101")
        self.play(Write(title))
        self.wait(1)

class WriteIntroArabic(Scene):
    def construct(self):
        
        title = Text('Calculus 101')

        self.play(Write(title))
        self.wait(1)

class derivativeShowcase(Scene):
    # a helper function to draw the line from the point to the x axis

    def draw_dashed_line_to_the_x_axis(self,ax,y_coordinate,color,x_coordinate):
        line= DashedLine(
            start=ax.c2p(x_coordinate,0),
            end=ax.c2p(x_coordinate,y_coordinate),
            color=color,

        )
        return line
    

    def construct(self):
        x_coordinate = ValueTracker(-2)
        axes=Axes(
            x_range=[-5,5,1],
            y_range=[-10,10,1],
            x_length=8,


        )
        fx= lambda x : x**3
        function = axes.plot(fx,color=RED)

        
        tangent =always_redraw(
            lambda : axes.get_secant_slope_group(
                graph=function,
                x=x_coordinate.get_value(),
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=4,
                
            )
        ) 
        line = always_redraw(
            lambda :self.draw_dashed_line_to_the_x_axis(
                ax = axes,
                x_coordinate=x_coordinate.get_value(),
                y_coordinate=fx(x_coordinate.get_value()),
                color=YELLOW,
            )
        )
        
        

        dot = always_redraw(
            lambda: Dot().move_to(
            axes.c2p(x_coordinate.get_value(),fx(x_coordinate.get_value()))
            )
        )
        functionText = MathTex(r"f(x)=x^3").next_to(axes,RIGHT)
        self.add(axes)
        self.play(Write(functionText),Create(function),run_time=2)
        self.wait(1.5)
        self.play(Create(dot),Create(tangent),FadeIn(line),run_time=1.5)
        self.play(x_coordinate.animate.set_value(2),run_time=4,rate_func=smooth)
        self.wait(1.5)
        self.play(x_coordinate.animate.set_value(0),run_time=2,rate_func=smooth)
        self.wait(1.5)
        self.play(x_coordinate.animate.set_value(1),run_time=1,rate_func=smooth)
        self.wait(1.5)
        self.play(x_coordinate.animate.set_value(-1),run_time=2,rate_func=smooth)

        
class AreaUnderCurve(Scene):
    def construct(self):
        x_coordinate = ValueTracker(0)
        delta_x=ValueTracker(1)
        axes=Axes(
            x_range=[0,10,1],
            y_range=[0,10,1],
            axis_config={"include_numbers":True},
        )
        fx= lambda x : np.sin(3/2*x) - x**2/20 +5
        function = axes.plot(fx,color=RED)
        areaUnderCurve = always_redraw(
            lambda : axes.get_area(
                graph = function,
                x_range=[0,x_coordinate.get_value()],
                opacity=1

            )
        )
        text = always_redraw(
            lambda : MathTex('\\int^{%s}_0 sin(\\frac{3x}{2}) - \\frac{x^2}{20} +5\\; \\mathrm{d}x' %(round(x_coordinate.get_value(),ndigits=1))).shift(UP*2 + 2*RIGHT)
        )

        # reimannSum = always_redraw(
        #     lambda : axes.get_riemann_rectangles(
        #             x_range=[0,x_coordinate.get_value()],
        #             graph=function,
        #             dx=delta_x.get_value(),
        #         )
        #     )
        
        self.play(Create(axes),run_time=1.5)
        self.play(Create(function),Create(text),run_time=1.5)
        self.add(areaUnderCurve)
        self.play(x_coordinate.animate.set_value(7),run_time=10,rate_func=double_smooth)



class ReimannShowCase(Scene):
    def construct(self):
        
        n=ValueTracker(1)
        axes=Axes(
            x_range=[0,10,1],
            y_range=[0,10,1],
            axis_config={"include_numbers":True},
        )
        fx= lambda x : np.sin(3/2*x) - x**2/20 +5
        function = axes.plot(fx,color=RED)
        reimannSum = always_redraw(
            lambda : axes.get_riemann_rectangles(
                    x_range=[0,8],
                    graph=function,
                    dx=1/n.get_value(),
                )
            )
        

        AreaUnderCurve=axes.get_area(
            graph = function,
            x_range=[0,8],
            opacity=1
        )
        text = always_redraw(
            lambda : MathTex(r'\lim_{n \rightarrow \infty} \sum^{n}_{i=1} \;(sin(\frac{3{x_i}}{2}) - \frac{{x_i}^2}{20} +5)\;(\Delta x)').shift(UP*2 + 2*RIGHT)
        )


        self.play(Create(axes),run_time=1.5)
        self.play(Create(function),Write(text),run_time=1.5)
        self.play(FadeIn(reimannSum),run_time=1)
        self.play(n.animate.set_value(15),run_time=7,rate_func=double_smooth)
        self.play(FadeTransform(reimannSum,AreaUnderCurve))
        
