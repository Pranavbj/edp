from manim import *

class ElectrostaticPotential(Scene):
    def construct(self):
        # Matching colors for specific equation parts
        col1 = ORANGE
        col2 = PURPLE
        col3 = BLUE
        col4 = GREEN
        
        # Equation 1
        eq1 = MathTex(r"W_{a \rightarrow b}", "=", r"\int_{a}^{b}", r"\mathbf{F} \cdot d\mathbf{r}", "=", r"\int_{a}^{b}", r"\frac{1}{4 \pi \epsilon_0 r^2}", r"q q_0", r"dr")
        for i in [0, 2, 3, 5, 6, 7, 8]:  # Set color to the terms in equation 1
            eq1[i].set_color(col1)
        
        self.play(Write(eq1))
        self.wait(2.5)
        
        # Equation 2
        eq2 = MathTex(r"U", "=", "U_b", "-", "U_a", "=", "-", "W_{a \rightarrow b}", "=", r"\frac{q q_0}{4 \pi \epsilon_0}", r"\left( \frac{1}{r_a} - \frac{1}{r_b} \right)")
        for i in [0, 2, 4, 6, 8, 9]:  # Set color to the terms in equation 2
            eq2[i].set_color(col2)
        
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2.5)
        
        # Equation 3
        eq3 = MathTex(r"U", "=", "U_b", "-", "U_a", "=", "-", "W_{a \rightarrow b}", "=", r"\frac{q q_0}{4 \pi \epsilon_0}", r"\left( \frac{1}{r_b} - \frac{1}{r_a} \right)")
        for i in [0, 2, 4, 6, 8, 9]:  # Set color to the terms in equation 3
            eq3[i].set_color(col3)
        
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2.5)
        
        # Equation 4
        eq4 = MathTex(r"U_r", "=", "U", "-", "U_{\infty}", "=", r"\frac{q q_0}{4 \pi \epsilon_0 r}")
        eq4[3].set_color(col4)  # Set color to the term in equation 4
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(2.5)
