from manim import *

class DriftVelocity(Scene):
    def construct(self):
        # Matching colors for specific equation parts
        col0 = RED
        col1 = ORANGE
        col2 = PURPLE
        col3 = BLUE
        col4=  GREEN
        col5= YELLOW
        col6= PINK
        
        # \[ a = - \frac{E e}{m} \]  
        
        eq1=MathTex(r"a","=", "-" ,r"\frac{E e}{m}")
        
        for i in [0,3]:  
            eq1[i].set_color(col0)        
        
        
        
        # \[ V_i = v_i + \frac{eE}{m} t_i \]
        eq2=MathTex(r"V_i", "=", r"v_i", "-", r"\frac{eE}{m} t_i")
        text1=Text("V_i: velocity at time t").scale(0.5)
        text2=Text("v_i: velocity immediately after last collision").scale(0.5)
        text3=Text("t_i: time elapsed after last collision").scale(0.5)
        for i in [0,2,4 ]:  
            eq2[i].set_color(col1)

        
        eq3=MathTex(r"v", "=", r"u", "+", r"a",r"t")
        eq3a=MathTex(r"v", "=", r"u", "-",r"\frac{eE}{m} t")
        
        for i in [0,2,4,5]:  
            eq3[i].set_color(col2)
            
        for i in [0,2,4]:  
            eq3a[i].set_color(col2)    
        
        # \[ v_d = \frac{eE \tau}{m} \]
        eq4=MathTex(r"v_d", "=","-", r"\frac{eE \tau}{m}")
        
        for i in [0,3]:  
            eq4[i].set_color(col3)
        
        text4=Text("On using:").scale(0.5).shift(UP*1.5)
        
        self.play(Write(text4),FadeIn(eq3))
        self.wait(2)
        self.play(FadeOut(text4),eq3.animate.move_to(UP*2),FadeIn(eq1))
        
        framebox1 = SurroundingRectangle(eq1, buff=0.1)
        framebox2 = SurroundingRectangle(eq3[4], buff=0.1)
                  
        self.play(
            Create(framebox1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait(2)
        self.play(
        FadeOut(framebox2,run_time=2)
        )
        
        # transform eq3[4] to eq1
        
        self.play(FadeOut(eq1),ReplacementTransform(eq3,eq3a))
        self.wait(2)
        
        self.play(eq3a.animate.move_to(UP*2))
        
        self.play(FadeIn(eq2))
        self.wait(2)
        
        self.play(FadeOut(eq3a),eq2.animate.move_to(UP*2))
        text1.shift(DOWN*1)
        text2.shift(DOWN*2)
        text3.shift(DOWN*3)
        
        self.play(FadeIn(text1),FadeIn(text2),FadeIn(text3))
        self.wait(2)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))
        
        text5=Text("Average initial velocity is 0").scale(0.5)
        eq5=MathTex(r"V_{avg}", "=", r"0", "-", r"\frac{eE}{m} t_{avg}")
        for i in [0,2,4]:  
            eq5[i].set_color(col4)
        
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5),FadeIn(eq5))
        self.wait(2)
        self.play(FadeOut(eq2),eq5.animate.move_to(UP*2))
        
        eq6=MathTex(r"V_{avg}", "=","-", r"\frac{eE}{m} t_{avg}")
        for i in [0,3]:  
            eq6[i].set_color(col5)
        
        self.play(FadeIn(eq6))
        self.wait(2)
        self.play(FadeOut(eq5),eq6.animate.move_to(UP*2))
        
        eq7=MathTex(r"V_{avg}", "=","-", r"\frac{eE}{m} \tau")
        for i in [0,3]:  
            eq7[i].set_color(col6)
        text6=Text("where τ is the average time between collisions").scale(0.5).shift(DOWN*1.5)
        
        self.play(FadeIn(eq7),Write(text6))
        self.wait(2)
        self.play(FadeOut(text6),FadeOut(eq6),FadeOut(eq7))
        
        text7=Text("Drift velocity v_d:").scale(0.5).shift(UP*2)
        self.play(FadeIn(eq4),FadeIn(text7))

        

        
       

        
        
