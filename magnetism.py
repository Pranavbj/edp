from manim import *

class MagneticFieldCircularloop(Scene):
    def construct(self):

        title = Text(r"Magnetic field on the axis of a circular current loop").scale(0.8).to_edge(UP)

        # Step 1: Display STEP 1 equation and explanation
        t1v0 = MathTex(r"Consider \; a \; conducting \; element \;",r" d\ell \;",r" of \; the \; loop").scale(0.8).shift(UP*2)
        t1v0.set_color_by_tex("d\ell", RED)
        t1v1 = MathTex(r"magnitude \; "," dB \;",r" of \; the \; magnetic \; field \; due \; to \;"," d\ell ",r"\; is \; given \; by ").next_to(t1v0, DOWN).scale(0.8)
        t1v2= MathTex(r"the \; Biot-Savart \; law").next_to(t1v1, DOWN).scale(0.8)
        t1v1.set_color_by_tex("dB", BLUE)
        t1v1.set_color_by_tex("d\ell", RED)

        # Step 2: Display STEP 1 equation and explanation
        step1_eq = MathTex(
            "dB ","= ","{\\mu_0 I \\, d\\ell","\\over"," 4\\pi ","r^3","}"," \\times r"
        )
        step1_eq.set_color_by_tex("dB", BLUE)
        step1_eq.set_color_by_tex("r^3", GREEN)


        t2v0 = MathTex( r"r^2 ","= x^2 + R^2", r" \; and \; ", r"|d\ell \times r| = r \, d\ell").scale(0.8).shift(UP*2)
        t2v0.set_color_by_tex("r^2", GREEN)
        t2v0.set_color_by_tex("d\ell", RED)

        # Step 3: Display STEP 2 equation and explanation
        step2_eq = MathTex(
            "dB ","="," {\\mu_0 I \\, d\\ell ","\\over"," 4\\pi}","{1 ","\\over"," (x^2 + R^2)^{3/2}}"
        )
        step2_eq.set_color_by_tex("(x^2 + R^2)^{3/2}", GREEN)
        step2_eq.set_color_by_tex("dB", BLUE)


        t3v0 = MathTex(r" components \;in \; y-axis \; cancels\; out,\; only \;the  \;","x-component"," \;survives").scale(0.8).shift(UP*2)
        t3v1 = MathTex(r"net\;contribution\;along\;the \;x-direction \; ","=",r"\;  dB_x",r" =",r" dB ",r"\cos \theta").next_to(t2v0, DOWN).scale(0.8)
        t3v0.set_color_by_tex("x-component", GREEN)
        t3v1.set_color_by_tex("dB_x", RED)
        t3v1.set_color_by_tex("dB", BLUE)
        t3v1.set_color_by_tex("\cos \theta", PINK)

        # Step 4: Display STEP 3 equation and explanation
        step3_eq = MathTex(
            "\\cos \\theta ","= +"," {R ","\\over","(x^2 + R^2)^{1/2}}"
        ).next_to(step2_eq, DOWN)

        step3_eq.set_color_by_tex("(x^2 + R^2)^{1/2}", GREEN)
        step3_eq.set_color_by_tex("\\cos \\theta ", PINK)


        # Step 5: Display STEP 4 equation and explanation
        step4_eq = MathTex(
            "dB_{x}"," = ","{ \\mu_0 I \\, d\\ell ","\\over"," 4\\pi }","{R ","\\over"," (x^2 + R^2)^{3/2}}"
        )
        step4_eq.set_color_by_tex("(x^2 + R^2)^{3/2}}", GREEN)
        step4_eq.set_color_by_tex("R ", RED)
        step4_eq.set_color_by_tex("dB_{x}", BLUE)

        # Step 6: Display LAST STEP equation and explanation
        last_step_eq = MathTex(
            " B \hat{\mathbf{i}} ","="," {{\mu_0 I","R^2","}","\over"," {2 {(x^2 + R^2)^{3/2}}}}","\hat{\mathbf{i}}"
        )
        
        last_step_eq.set_color_by_tex("R^2", RED)
        last_step_eq.set_color_by_tex("(x^2 + R^2)^{3/2}}", GREEN)
        last_step_eq.set_color_by_tex("B \hat{\mathbf{i}}", BLUE)

        self.play(Write(title))

        self.play(Write(t1v0),run_time=2)
        self.wait(1)
        self.play(Write(t1v1),run_time=2)
        self.wait(1)
        self.play(Write(t1v2),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t1v2,step1_eq),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t1v1,t2v0),FadeOut(t1v0),run_time=2)
        self.wait(2)

        self.play(TransformMatchingShapes(step1_eq,step2_eq),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(t2v0,t3v0),run_time=2)
        self.wait(2)
        self.play(Write(t3v1),run_time=2)
        self.wait(2)

        self.play(Write(step3_eq),run_time=2)
        self.wait(2)

        self.play(TransformMatchingShapes(step2_eq,step4_eq),run_time=2)
        self.wait(2)

        self.play(TransformMatchingShapes(step4_eq,last_step_eq),run_time=2)
        self.wait(2)