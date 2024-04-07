from manim import *

class MatchingEquationParts(Scene):
   
    def construct(self):

        eq1 = MathTex("E","=",r"E_{+}", "-","E_{-}")
        eq2 = MathTex("E","=",r"\frac{1}{4\pi\epsilon _{0} } ",r"\left ({ \frac{q}{r_{+}^{2}}} \right ) ", "-",r" \frac{1}{4\pi\epsilon _{0} }",r"\left ( {\frac{q}{r_{-}^{2}} }\right )")
        eq1[2].set_color(YELLOW)
        eq1[4].set_color(GREEN)

        eq2[3].set_color(YELLOW)
        eq2[6].set_color(GREEN)


        self.play(Write(eq1))
        # self.add(variables.arrange_in_grid(buff=1.0).shift(UP))
        self.wait(2.5)
        self.play(ReplacementTransform(eq1,eq2))
        self.wait(2.0)
        framebox1 = SurroundingRectangle(eq2[3], buff = .1)
        framebox2 = SurroundingRectangle(eq2[6], buff = .1,color=GREEN)
        r1=Tex("distance of point to +ve charge(+q)").shift(UP*2).set_color(YELLOW)
        r2=Tex("distance of point to -ve charge(-q)").shift(UP*2).set_color(GREEN)
        self.play(
            Create(framebox1),
            Write(r1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(framebox1,framebox2),
            ReplacementTransform(r1,r2),
        )
        self.wait(3)
        self.play(
        FadeOut(framebox2,run_time=2),
        FadeOut(r2,run_time=2)
        )
        



        # eq3 = TexMobject(r"E",r"=",r"{1 \\over 4\pi\epsilon _{0} }   \left   ({ {q \\over \left ( 1-{d \\over 2z} \right )^{2} }}\right )", r"-",r" {1 \\over 4\pi\epsilon _{0} }   \left   ( {{q \\over \left ( 1+{d \\over 2z} \right )^{2} }} \right )")

        eq3 = MathTex("E","=",r"{\frac{1}{4\pi\epsilon _{0} }}",r" \left ({ \frac{q}{\left ( z-\frac{d}{2} \right )^{2}} }\right ) ", "-",r" \frac{1}{4\pi\epsilon _{0} } ",r"\left ( {\frac{q}{\left ( z+\frac{d}{2} \right )^{2}} }\right )")
        # eq3 = MathTex("E","=",r"{\frac{1}{4\pi\epsilon _{0} }}",r" \left (\frac{",r"q",r"}{\left ( z-\frac{d}{2} \right )^{2}} \right ) ", "-",r" \frac{1}{4\pi\epsilon _{0} } ",r"\left ( {\frac{q}{\left ( z+\frac{d}{2} \right )^{2}} }\right )")

        eq3[3].set_color(YELLOW)
        eq3[6].set_color(GREEN)

        z=Tex("z = distance from midpoint of dipole to point", tex_to_color_map={"z":YELLOW}).shift(UP*2)
        d=Tex("d ","= distance between charges of dipole").shift(UP*2)
        #subsection of d in d
        d[0].set_color(YELLOW)

        self.play(TransformMatchingShapes(eq2, eq3),Write(z))
        self.play(FocusOn(z[0]))
        self.wait(2.0)
        self.play(ReplacementTransform(z,d))
        self.play(FocusOn(d[0]))
        self.wait(2.0)

        self.play(
        FadeOut(d,run_time=2)
        )

        self.play(ReplacementTransform(eq3[5],eq3[2]))
        self.wait(2.0)
        eq4 = MathTex(r"E" ,"=",r"{\frac{q}{4\pi\epsilon_{0}z^{2}}}",r"\left(\frac{1}{(1 - \frac{d}{2z})^{2}}", "-" ,r"\frac{1}{(1 + \frac{d}{2z})^{2}}\right)")

        eq4[3].set_color(YELLOW)
        eq4[5].set_color(GREEN)
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait(2.0)

        eq5=MathTex(r"E","=",r"\frac{q}{4\pi\epsilon_{0}z^{2}} ",r"\frac{\left ( 1+\frac{d}{2z} \right )^{2} - \left ( 1-\frac{d}{2z} \right )^{2} }{\left ( 1-\frac{d}{2z} \right )^{2}\left ( 1+\frac{d}{2z} \right )^{2}}")

        
        eq5[3].set_color(RED)
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait(2.0)

        eq6=MathTex(r"E","=",r"\frac{q}{4\pi\epsilon_{0}z^{2}} ",r"\frac{2d/z}{\left ( 1-\frac{d}{2z} \right )^{2}\left ( 1+\frac{d}{2z} \right )^{2}}")


       
        eq6[3].set_color(RED)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(2.0)

        eq7=MathTex(r"E",r"=",r"\frac{q}{4\pi\epsilon_{0}z^{2}}",r"\frac{2d/z}{(1-(\frac{d}{2z})^{2})^{2}}")
        eq7[3].set_color(RED)
        self.play(TransformMatchingShapes(eq6, eq7))
        self.wait(2.0)
        smol=MathTex("d/2z","<< ","1" ,r", 1 - d/2z \approx  1").shift(UP*2)
        self.play(Write(smol))
        self.wait(1.5)
        self.play(ShrinkToCenter(smol[0]),ScaleInPlace(smol[2],2))

        self.play(
        FadeOut(smol)
        )
        

        eq8=MathTex(r"E","=",r"\frac{1}{2\pi\epsilon_{0}}",r"\frac{qd}{z^{3}}")
        eq8[3].set_color(RED)
        self.play(TransformMatchingShapes(eq7, eq8))
        self.wait(2.0)


from manim import *

class PotentialDipole(Scene):
    def construct(self):
        # Title
        title = Text("Electric Dipole Potential", font_size=36, color=WHITE)
        self.add(title.to_edge(UP))

        eq1v0 = MathTex(
            r"V",r" =",r" -","{1 ","\\over "," 4\\pi\\epsilon_0}"," \\left( ","{q ","\\over"," r_1}"," - ","{q"," \\over ","r_2}"," \\right)"
        )

        eq1v0[7].set_color(PINK)
        eq1v0[9].set_color(RED)
        eq1v0[11].set_color(PINK)
        eq1v0[13].set_color(BLUE)

        t1=Text("Potential due to an electric dipole",font_size=24).shift(UP)

        eq2v0 = MathTex(r"r_1^2"," = r^2 + a^2 ",r"- 2ar\cos\theta")
        eq3v0 = MathTex(r"r_2^2"," = r^2 + a^2 ",r"+ 2ar\cos\theta").shift(DOWN)

        eq2v0[0].set_color(RED)
        eq3v0[0].set_color(BLUE)

        t2=Text("By geomentry we get",font_size=24).shift(UP)

        eq1v1 = MathTex(
            "V"," = ","-","{1"," \\over ","4\\pi\\epsilon_0}"," \\left("," {q"," \\over ","r^2 + a^2 - 2ar\\cos\\theta}"," - ","{q"," \\over ","r^2 + a^2 + 2ar\\cos\\theta}"," \\right)"
        )

        t3=Text("Substituting we get",font_size=24).shift(UP)

        eq1v1[9].set_color(RED)
        eq1v1[13].set_color(BLUE)
        eq1v1[7].set_color(PINK)
        eq1v1[11].set_color(PINK)

        eq1v2 = MathTex(
            "V"," = ","-","{q"," \\over 4\\pi\\epsilon_0}"," \\left("," {2a\\cos\\theta"," \\over ","r^2 + a^2\\cos^2\\theta}"," \\right)"
        )

        t4=Text("simplifying we get",font_size=24).shift(UP)
        
        eq1v2[3].set_color(PINK)
        eq1v2[6].set_color(PURPLE)
        eq1v2[8].set_color(PURPLE)

        t5 = Text("For points far away r >> a", font_size=24).shift(UP)

        t6=Text("further simplifying we get ",font_size=24).shift(UP)

        eq4v0= MathTex("V"," = ","{q"," \\over ","4\\pi\\epsilon_0}"," \\left( "," {2a\\cos\\theta"," \\over ","r^2}"," -"," {a^2\\cos^2\\theta"," \\over ","r^2}"," \\right)")
        eq4v0[2].set_color(PINK)
        eq4v0[6].set_color(PURPLE)
        eq4v0[8].set_color(PURPLE)
        eq4v0[10].set_color(PURPLE)
        eq4v0[12].set_color(PURPLE)

        eq5v0= MathTex("V"," = ","{p"," \\over ","4\\pi\\epsilon_0}"," \\left( "," {a\\cos\\theta"," \\over ","r^2}"," \\right)")
        eq5v0[2].set_color(PINK)
        eq5v0[6].set_color(PURPLE)
        eq5v0[8].set_color(PURPLE)

        eq5v2=MathTex("V"," = ","{p\\cos\\theta"," \\over ","r^2}"," - ","{a^2\\cos^2\\theta"," \\over ","r^3}")
        eq5v2[2].set_color(PINK)
        eq5v2[4].set_color(PINK)
        eq5v2[6].set_color(PINK)
        eq5v2[8].set_color(PINK)

        # Play animations with smooth transitions
        self.play(Write(t1),run_time=2)
        self.play(Write(eq1v0))
        self.wait(2)
        self.play(FadeOut(t1),ApplyMethod(eq1v0.shift, UP*2))
        self.wait(2)

        self.play(Write(t2),run_time=2)
        self.play(Write(eq2v0),Write(eq3v0))
        self.wait(2)

        self.play(FadeOut(t2),FadeOut(eq2v0),FadeOut(eq3v0),ApplyMethod(eq1v0.shift,DOWN*2),Write(t3))
        self.wait()
        self.play(TransformMatchingShapes(eq1v0,eq1v1),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t3,t4),TransformMatchingShapes(eq1v1,eq1v2),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t4,t5))
        self.wait(2)

        self.play(TransformMatchingShapes(eq1v2,eq4v0),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t5,t6))
        self.wait(2)

        self.play(TransformMatchingShapes(eq4v0,eq5v0),run_time=2)
        self.wait(2)

        self.play(TransformMatchingShapes(eq5v0,eq5v2),run_time=2)
        self.wait(2)





        


