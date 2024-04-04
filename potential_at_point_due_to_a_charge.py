from manim import *

class ElectricPotential(Scene):
    def construct(self):
        # Matching colors for specific equation parts
        col0 = RED
        col1 = ORANGE
        col2 = PURPLE
        col3 = BLUE
        
        # Equation 1
        eq1 = MathTex(r"W", "=","-", r"\int_{\infty}^{r}", r"\frac{Q}{4\pi \epsilon_0 r'^2}", r"dr'")
        for i in [0, 3,4,5]:  
            eq1[i].set_color(col0)
        
        text0 = Text("WORK DONE FORMULA:").scale(0.5)
        text0.shift(UP * 2)
        self.play(Write(eq1), Write(text0))
        self.wait(2.5)
        self.play(FadeOut(text0),eq1.animate.move_to(UP * 2))
        
        
        # framebox1 = SurroundingRectangle(eq1[3], buff=0.1)
        # self.play(Create(framebox1))
        # self.wait(2)
        # self.play(FadeOut(framebox1, run_time=2))
        
        eq0= MathTex(r"V(r)", "=", r"W")
        text1 = Text("V(r) is the potential at a point r due to a charge Q").scale(0.5) 
        
        for i in [0, 2]:  
            eq0[i].set_color(col1)
            
        self.play(Write(eq0))
        text1.shift(DOWN * 2)
        self.play(Write(text1))
        self.wait(2)
        
        self.play(FadeOut(text1),FadeOut(eq0))
        
        # Equation 2
        eq2 = MathTex(r"V(r)", "=","-", r"\int_{\infty}^{r}", r"\frac{Q}{4\pi \epsilon_0 r'^2}", r"dr'")
        for i in [0,3,4,5]: 
            eq2[i].set_color(col1) 
            
        eq2a = MathTex(r"V(r)","=", "-",r"\left( \frac{Q}{4\pi \epsilon_0}", r"\right) \int_{\infty}^{r}" r"\frac{1}{r'^2}", "\,dr'")
        for i in [0, 3, 4, 5]:  
            eq2a[i].set_color(col1)
        
        eq2b = MathTex(r"\int \frac{1}{r^n}" ,"\ dr", "=" ,r"\frac{-1}{(n-1)r^{n-1}}")

        
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2.5)
        # self.play(ReplacementTransform(eq2[3:], eq2a[3:]))   
        self.play(eq2.animate.shift(UP*3),Write(eq2a))     
        self.wait(2.5)
        
        self.play(FadeOut(eq2))
        self.play(eq2a.animate.move_to(UP*2))
        
        text2= Text("The integral is solved using the formula").scale(0.5)
        text2.shift(DOWN * 2)
        self.play(Write(text2))
        self.play(eq2b.animate.shift(DOWN*1))
        self.wait(2.5)
        
        self.play(FadeOut(text2),FadeOut(eq2b))
        
        # Equation 3
        eq3 = MathTex(r"V(r)", "=", r"-\left[-\frac{Q}{4\pi \epsilon_0 r'}\right]_{\infty}^{r}")
        for i in [0, 2]:  
            eq3[i].set_color(col2)
        
        self.play(ReplacementTransform(eq2a, eq3))
        self.wait(2.5)
        
        # Equation 4
        eq4 = MathTex(r"V(r)", "=", r"\left(\frac{Q}{4\pi \epsilon_0 r}\right)", "-", r"\left(\frac{Q}{4\pi \epsilon_0 \infty}\right)")
        for i in [0, 2, 4]: 
            eq4[i].set_color(col3)
        
        self.play(eq3.animate.shift(UP*2),Write(eq4))
        self.wait(2.5)
        
        self.play(FadeOut(eq3))
        
        # Equation 5
        eq5 = MathTex(r"V(r)", "=", r"\frac{Q}{4\pi \epsilon_0 r}")
        eq5[2].set_color(col1)  
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(2.5)

