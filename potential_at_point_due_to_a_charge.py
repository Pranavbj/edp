from manim import *

class ElectricPotential(Scene):
    def construct(self):
        # Matching colors for specific equation parts
        col0 = RED
        col1 = ORANGE
        col2 = PURPLE
        col3 = BLUE
        
        # Equation 1
        eq1 = MathTex(r"U", "=","-", r"\int_{\infty}^{r}", r"\frac{Q}{4\pi \epsilon_0 r'^2}", r"dr'")
        for i in [0, 3,4,5]:  
            eq1[i].set_color(col0)
        
        self.play(Write(eq1))
        self.wait(2.5)
        
        # framebox1 = SurroundingRectangle(eq1[3], buff=0.1)
        # self.play(Create(framebox1))
        # self.wait(2)
        # self.play(FadeOut(framebox1, run_time=2))
        
        # Equation 2
        eq2 = MathTex(r"V(r)", "=","-", r"\int_{\infty}^{r}", r"\frac{Q}{4\pi \epsilon_0 r'^2}", r"dr'")
        for i in [0,3,4,5]: 
            eq2[i].set_color(col1)  
        
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2.5)
        
        # Equation 3
        eq3 = MathTex(r"V(r)", "=", r"-\left[-\frac{Q}{4\pi \epsilon_0 r'}\right]_{\infty}^{r}")
        for i in [0, 2]:  
            eq3[i].set_color(col2)
        
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2.5)
        
        # Equation 4
        eq4 = MathTex(r"V(r)", "=", r"\left(\frac{Q}{4\pi \epsilon_0 r}\right)", "-", r"\left(\frac{Q}{4\pi \epsilon_0 \infty}\right)")
        for i in [0, 2, 4]: 
            eq4[i].set_color(col3)
        
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(2.5)
        
        # Equation 5
        eq5 = MathTex(r"V(r)", "=", r"\frac{Q}{4\pi \epsilon_0 r}")
        eq5[2].set_color(col1)  
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(2.5)

