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


        
    




