from manim import *


class ElectrostaticPotential(Scene):
    def construct(self):
        # Matching colors for specific equation parts
        col0= RED
        col1 = ORANGE
        col2 = PURPLE
        col3 = BLUE
        col4 = GREEN
        
        #Equation 0
        
        eq0 = MathTex(r"U", "=", r"U_b", "-", r"U_a", "=", "-", r"W_{a \rightarrow b}")
        for i in [0, 2, 4, 7]:
            eq0[i].set_color(col1)

        
        text0 = Text("The potential energy of a point charge at a point in space").scale(0.5)
        text0.shift(UP * 2)
        self.play(Write(eq0), Write(text0))
        self.wait(2.5)
        self.play(FadeOut(text0))
             
        
        # Equation 1
        eq1 = MathTex(r"W_{a \rightarrow b}", "=", r"\int_{a}^{b}", r"\mathbf{F}", r"\cdot", r"d\mathbf{r}", "=", r"\int_{a}^{b}", r"\frac{1}{4 \pi \epsilon_0 r^2}", r"q q_0", r"dr")
        for i in [0, 2, 3,4, 5, 7, 8,9,10]:  # Set color to the terms in equation 1
            eq1[i].set_color(col1)
        
        
        
        text1 = Text("The work done on the particle to move it across the used path").scale(0.5)
        text1.shift(UP * 3)
        self.play(eq0.animate.move_to(UP * 2),FadeIn(eq1))
        self.wait(2)
        self.play(FadeOut(eq0))

        self.wait(1)
        self.play( Write(text1))
        self.wait(2)

        self.play(FadeOut(text1))
        self.wait(2)

        
        framebox1 = SurroundingRectangle(eq1[3], buff = .1)
        framebox2 = SurroundingRectangle(eq1[8:10], buff = .1,color=GREEN)
        
        self.play(
            Create(framebox1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait(3)
        self.play(
        FadeOut(framebox2,run_time=2),
        FadeOut(eq1,run_time=2)
        )
        
        
        
        # Equation 2
        eq2 = MathTex(r"W_{a \rightarrow b}", "=", r"\frac{q q_0}{4 \pi \epsilon_0}", r"\left( \frac{1}{r_a}", "-" ,r"\frac{1}{r_b} \right)")
        for i in [0, 2,3,5]:  # Set color to the terms in equation 2
            eq2[i].set_color(col2)  
            
        text3 = Text("on integrating...")
        eq_integration = MathTex(r"W_{a \rightarrow b}", "=",r"\int_{a}^{b} \frac{1}{4 \pi \epsilon_0 r^2} q q_0 \, dr")

        text3.shift(UP * 3)
        self.play( eq_integration.animate.move_to(UP * 2), Write(text3))
        self.wait(2)
        self.play(FadeOut(text3),FadeOut(eq_integration),Write(eq2))    
        
        self.wait(2.5)
        
        framebox3 = SurroundingRectangle(eq2[3], buff = .1,color=YELLOW)
        framebox4 = SurroundingRectangle(eq2[5], buff = .1,color=GREEN)
        
        self.play(
            Create(framebox3),
            Create(framebox4)
        )
        
        self.wait(2)
        self.play(
            FadeOut(framebox3,run_time=2),
            FadeOut(framebox4,run_time=2)
        )
        
        
        # Equation 3
        eq3 = MathTex( "-", r"W_{a \rightarrow b}", "=", r"\frac{q q_0}{4 \pi \epsilon_0}", r"\left( \frac{1}{r_b}", "-", r"\frac{1}{r_a} \right)")
        for i in [1,3,4,6]:  # Set color to the terms in equation 3
            eq3[i].set_color(col3)
            
       
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2.5)
        
        framebox5 = SurroundingRectangle(eq2[4], buff = .1,color=GREEN)
        framebox6 = SurroundingRectangle(eq2[6], buff = .1,color=YELLOW)
        
        self.play(
            Create(framebox5),
            Create(framebox6)
        )
        
        self.wait(2)
        self.play(
            FadeOut(framebox5,run_time=2),
            FadeOut(framebox6,run_time=2),
            FadeOut(eq3,run_time=2)
        )
        
        
        # Equation 4
        text4 = Text("potential energy of two charge system at infinite separation is 0").scale(0.5)
        e1=MathTex(r"U_{\infty}", "=", r"0")
        eq4 = MathTex(r"U_r", "=", r"U", "-", r"U_{\infty}", "=", r"\frac{q q_0}{4 \pi \epsilon_0 r}")
        eq4a=MathTex( r"U_r", "=", r"U", "-", r"U_{\infty}", "=", r"\frac{q q_0}{4 \pi \epsilon_0} ",r"\left( \frac{1}{r} - 0 \right)")
        eq4a.set_color(col4)  
        eq4[3].set_color(col4)  # Set color to the term in equation 4
        self.play( e1.animate.move_to(UP * 2), Write(text4))
        self.wait(2)
        self.play(FadeOut(text4),FadeIn(eq4a),)
        self.wait(2.5)
        self.play(FadeOut(e1))
        self.play(ReplacementTransform(eq4a, eq4))
