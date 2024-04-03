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




