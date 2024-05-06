from manim import *

class CapacitorEnergy(Scene):
    def construct(self):
        title = Text("Energy stored in capacitor")
        self.add(title.to_edge(UP))


        eq1v0 = MathTex(r"dW", r"=", r"V",  r"dq")
        eq1v1 = MathTex(r"dW", r"=", r"\frac{q}{C}",r"dq")

        frameEq1a = SurroundingRectangle(eq1v0[2], buff = .05)
        frameEq1b = SurroundingRectangle(eq1v1[2], buff = .05)

        eq1v0[2].set_color(RED)
        eq1v0[3].set_color(PINK)

        eq1v1[2].set_color(RED)
        eq1v1[3].set_color(PINK)

        self.play(Write(eq1v0))
        self.wait(2) 

        t1 = MathTex(r"\text{we know that }", r"V = \frac{q}{C}", tex_to_color_map={r"V = \frac{q}{C}": RED}).shift(UP*1)
        

        self.play(
        Create(frameEq1a),
        Write(t1)
        )
        self.wait(2) 

        self.play(
            ReplacementTransform(eq1v0, eq1v1),
            ReplacementTransform(frameEq1a, frameEq1b)
            )
        self.wait(2) 
        self.play(FadeOut(t1), FadeOut(frameEq1b))
        self.wait(1) 

        #moveq1 up
        self.play(ApplyMethod(eq1v1.shift, UP*1.8))
        self.wait(1)

        #integrate both sides
        t2 = MathTex(r"\text{Total work done to charge a capacitor to a charge }", r"( q_0 )", tex_to_color_map={r"( q_0 )": RED}).shift(UP*1)
        eq2v0 = MathTex(r" W",r" =",r"\int_{0}^{q_0}",r"dW")
        eq2v1 = MathTex(r" W",r" =",r"\int_{0}^{q_0}",r"\frac{q}{C}",r"dq")
        eq2v2= MathTex(r" W",r" =",r"\frac{1}{C}",r" \int_{0}^{q_0}",r"q",r"dq")
        eq2v3= MathTex(r" W",r" =",r"\frac{1}{C}",r" \left[ \frac{q^2}{2} \right]_{0}^{q_0}")
        eq2v4= MathTex(r" W",r" =",r"\frac{1}{2C}",r"q_0^2")

        eq2v0[3].set_color(RED)
        eq2v1[3].set_color(RED)
        eq2v1[4].set_color(PINK)
        eq2v2[2].set_color(RED)
        eq2v2[4].set_color(RED)
        eq2v2[5].set_color(PINK)
        eq2v3[2].set_color(RED)
        eq2v3[3].set_color(YELLOW)
        eq2v4[2].set_color(YELLOW)
        eq2v4[3].set_color(YELLOW)

        self.play(Write(t2, run_time=2))
        self.wait()
        self.play(ApplyWave(t2))

        self.play(Write(eq2v0))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait()
        
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(eq1v1, buff = .05)))
        self.play(Indicate(eq2v0[3]))
        self.wait()

        self.play(TransformMatchingTex(eq2v0,eq2v1),run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(eq2v1, eq2v2))
        self.wait()

        self.play(Uncreate(VGroup(eq2v2[3], eq2v2[4], eq2v2[5])))
        self.wait()

        self.play(TransformMatchingTex(eq2v2, eq2v3))
        self.wait(2)

        self.play(TransformMatchingShapes(eq2v3, eq2v4),run_time=2)
        self.wait()

        self.play(FadeOut(eq1v1))
        self.play(ApplyMethod(eq2v4.shift, UP*2))

        t3 = Text("so total energy stored in capacitor").shift(UP*1.2)
        self.play(Write(t3))
        self.wait()

        eq3v0 = MathTex(r"U =",r" \frac{1}{2} CV^2")
        eq3v1 = MathTex(r"U =",r"\frac{1}{2} \frac{q_0^2}{C}")
        eq3v2 = MathTex(r"U =",r"\frac{1}{2} q_0 V")

        eq3v0[1].set_color(YELLOW)
        eq3v1[1].set_color(YELLOW)
        eq3v2[1].set_color(YELLOW)

        self.play(Write(eq3v0))
        self.wait(1)

        eq3v1.next_to(eq3v0, DOWN)
        self.play(TransformMatchingTex(eq3v0.copy(), eq3v1))
        self.wait(1)

        eq3v2.next_to(eq3v1, DOWN)
        self.play(TransformMatchingTex(eq3v1.copy(), eq3v2))
        self.wait(1)

        self.play(ShowCreationThenFadeOut(SurroundingRectangle(eq3v0[1], buff = .05)),ShowCreationThenFadeOut(SurroundingRectangle(eq3v1[1], buff = .05)),ShowCreationThenFadeOut(SurroundingRectangle(eq3v2[1], buff = .05)))
        self.wait(1)



class ACVoltageCapacitor(Scene):
    def construct(self):

        equation_1 = MathTex(r"v","=",r" {q ","\over"," C}")
        equation_2 = MathTex(r"V_m \sin(\omega t) ","=","{q ","\over"," C}")
        equation_3 = MathTex(r"i",r" = {d \over dt} \left( V_m C \sin(\omega t) \right)"," =",r" \omega C V_m \cos(\omega t)")
        equation_4 = MathTex(r"i = i_m \sin(\omega t + { \pi \over 2})")
        equation_5 = MathTex(r"i_m = {V_m \over {1 \over \omega C}}")
        equation_6 = MathTex(r"X_C = {1 \over \omega C}")
        equation_7 = MathTex(r"i_m = {V_m \over X_C}")

        equations = [equation_1, equation_2, equation_3, equation_4, equation_5, equation_6, equation_7]

        texts = [
            MathTex(r"\text{From Kirchhoff’s loop rule, the voltage across the source and the capacitor are equal.}"),
            MathTex(r"\text{To find the current, we use the relation:}"),
            MathTex(r"\text{Using the relation:}"),
            MathTex(r"\text{where the amplitude of the oscillating current is } i_m = \omega C V_m."),
            MathTex(r"\text{Comparing it to } i_m = ",r"\frac{V_m}{R}",r" \text{ for a purely resistive circuit,}"),
            MathTex(r"\text{we find that } ",r"\frac{1}{\omega C} ",r"\text{ plays the role of resistance.}"),
            MathTex(r"\text{It is called capacitive reactance and is denoted by } ",r"X_C:"),
            MathTex(r"\text{So that the amplitude of the current is:}"),
        ]

        title = Text(r"AC Voltage in a Capacitor").scale(0.8).to_edge(UP)
        self.play(Write(title))

        texts[0].shift(UP*1.5).scale(0.6)
        self.play(Write(texts[0]))
        self.wait(2)

        equation_1[2].set_color("BLUE")
        equation_1[4].set_color("PINK")
        self.play(Write(equation_1))
        self.wait(2)

        texts[1].shift(UP*1.5).scale(0.8)

        equation_2[0].set_color("RED")
        equation_2[2].set_color("BLUE")
        equation_2[4].set_color("PINK")

        self.play(TransformMatchingShapes(texts[0],texts[1]),run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(equation_1,equation_2),run_time=2)
        self.wait(2)

        texts[2].shift(UP*1.5).scale(0.8)

        equation_3[0].set_color("RED")
        equation_3[1].set_color("BLUE")
        equation_3[3].set_color("PINK")

        self.play(TransformMatchingShapes(texts[1],texts[2]),run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(equation_2,equation_3),run_time=2)
        self.wait(2)



        




