from manim import *

class MotionalEMF(Scene):
    def construct(self):

        title = Text(r"Motional Electromotive force").scale(0.8).to_edge(UP)
        self.play(Write(title))

        t1v0 = MathTex(r"the \,magnetic \, flux \,",r"\Phi_B", r"\text{ enclosed by the loop }", r"PQRS").scale(0.8).shift(UP*1.5)
        t1v0.set_color_by_tex("\Phi_B", BLUE)
        self.play(Write(t1v0))
        self.wait(2)

        eq1v0 = MathTex(r"\Phi_B ",r"= ",r"B ",r"\cdot ",r"l",r"x").scale(0.8).next_to(t1v0, DOWN)
        eq1v0[0].set_color( BLUE)
        eq1v0[2].set_color(ORANGE)
        eq1v0.set_color_by_tex("l", GREEN)
        eq1v0.set_color_by_tex("x", PINK)

        self.play(Write(eq1v0),run_time=2)
        self.wait(1)

        t1v1 = MathTex(r"\text{Since \( x \) is changing with time...}").scale(0.8).next_to(eq1v0, DOWN)
        self.play(Write(t1v1))
        self.wait(2)

        eq2v0=MathTex(r" -",r"{d",r"\Phi_B",r"\over",r"d",r"t}",r" =",r"-",r"B",r"l",r"{d(","x",") ",r"\over",r"dt}").next_to(t1v1, DOWN)
        eq2v0[2].set_color( BLUE)
        eq2v0[8].set_color(ORANGE)
        eq2v0.set_color_by_tex("l", GREEN)
        eq2v0.set_color_by_tex("x", PINK)

        self.play(Write(eq2v0),run_time=2)
        self.wait(1)

        eq2v1=MathTex(r" -",r"{d",r"\Phi_B",r"\over",r"d",r"t}",r" =",r"-",r"B",r"l",r"{d(","vt",") ",r"\over",r"dt}").next_to(t1v1, DOWN)
        eq2v1[2].set_color( BLUE)
        eq2v1[8].set_color(ORANGE)
        eq2v1.set_color_by_tex("l", GREEN)
        eq2v1.set_color_by_tex("vt", PINK)

        self.play(TransformMatchingTex(eq2v0,eq2v1),run_time=2)
        self.wait(1)

        eq2v2=MathTex(r"{d",r"\Phi_B",r"\over",r"d",r"t}",r" =",r"B",r"l",r"v").next_to(t1v1, DOWN)
        eq2v2[1].set_color( BLUE)
        eq2v2[6].set_color(ORANGE)
        eq2v2.set_color_by_tex("l", GREEN)
        eq2v2[8].set_color(PINK)

        self.play(TransformMatchingTex(eq2v1,eq2v2),run_time=2)
        self.wait(1)

        eq2v3=MathTex(r"\varepsilon",r" =",r"B",r"l",r"v").next_to(t1v1, DOWN)
        eq2v3.set_color_by_tex("l", GREEN)
        eq2v3[0].set_color( BLUE)
        eq2v3[2].set_color(ORANGE)
        eq2v3[4].set_color(PINK)

        self.play(TransformMatchingTex(eq2v2,eq2v3),run_time=2)
        self.wait(1)

        v1=VGroup(t1v0,eq1v0,t1v1)

        self.play(FadeOut(v1),ApplyMethod(eq2v3.shift, 2*UP),run_time=2)
        self.wait(1)

        t2v0 = MathTex(r"\text{The work done in moving the charge from } P \text{ to } Q \text{ is,}").next_to(eq2v3, DOWN)
        self.play(Write(t2v0))
        self.wait(1)

        eq3v0 = MathTex(r"W"," ="," q","B","l","v").next_to(t2v0, DOWN)
        eq3v0[0].set_color( BLUE)
        eq3v0[3].set_color(ORANGE)
        eq3v0.set_color_by_tex("l", GREEN)
        eq3v0.set_color_by_tex("v", PINK)

        self.play(Write(eq3v0),run_time=2)
        self.wait(1)




        
