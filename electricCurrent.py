from manim import *

class ColoredCircuit(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        c = MathTex(
            r"""\draw (0,0) to[isource, l=$I_0$, v=$V_0$] (0,3);""", 
            r"""\draw (0,3) to[short, -*] (2,3);""",
            r"""\draw (2,3) to[R=$R_1$, i>_=$I_1$] (2,0);""",
            r"""\draw (2,3) -- (4,3);""", 
            r"\draw (4,3) to[R=$R_2$, i>_=$I_2$] (4,0);",
            r"\draw (4,0) to[short, -*] (2,0)--(0,0);"
            , stroke_width=4
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=template
            
            )
        # for cir, clr in zip(c[0,4],[RED, GREEN, BLUE, YELLOW]):
        #     cir.set_color(clr)
        c.set_color_by_tex_to_color_map({"I_0":RED, "R_1":YELLOW, "R_2":BLUE})

        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=3)
        self.play(ApplyWave(c[0]))
        self.play(Indicate(c[2], color=TEAL), run_time=2) 
        self.play(Circumscribe(c[4], fade_out=True, color=BLUE))
        self.wait(2)


class KirchhoffsCurrentLaw(Scene):
    def construct(self):
        # Adding circuitikz package to the preamble
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        circuit_tex = [
            r"""\draw (0,0) to[isource, l=$I_0$, v=$V_0$, color=red] (0,3);""",
            r"""\draw (0,3) to[short, -*] (2,3);""",
            r"""\draw (2,3) to[R=$R_1$, color=yellow] (2,0);""",
            r"""\draw (2,3) -- (4,3);""",
            r"\draw (4,3) to[R=$R_2$, color=blue] (4,0);",
            r"\draw (4,0) to[short, -*] (2,0)--(0,0);"
        ]

        circuit = MathTex(*circuit_tex,
            stroke_width=3,
            fill_opacity=0,
            stroke_opacity=1,
            tex_environment="circuitikz",
            tex_template=template
        )

        circuit.set_color_by_tex_to_color_map({"I_0":RED, "R_1":YELLOW, "R_2":BLUE, "I_1":YELLOW, "I_2":BLUE})


        # Add labels for the currents and voltages
        current_label = MathTex(r"I_0 \rightarrow", color=RED).next_to(circuit[1], UP)
        current_label1 = MathTex(r"I_1 \downarrow", color=YELLOW).next_to(circuit[2], RIGHT)
        current_label2 = MathTex(r"I_2 \downarrow", color=BLUE).next_to(circuit[4], RIGHT)
        current_label3= MathTex(r"\leftarrow I_1 + I_2", color=YELLOW).next_to(circuit[5], DOWN)
        current_label4= MathTex(r"\leftarrow I_0", color=RED).next_to(circuit[5], DOWN)

        current_labels = VGroup(current_label1, current_label2)

        junction_text = Text("At any junction, the sum of currents entering equals the sum of currents leaving.", font_size=24).shift(UP*3.5)
        kvl_equation = MathTex(r"I_0 = I_1 + I_2", font_size=32).shift(UP*3.5)

        self.play(Write(circuit, shift=UP, target_position=ORIGIN), run_time=3)
        self.wait(1)
        self.play(Write(junction_text),run_time=2)
        self.wait(1)
        self.play(Indicate(circuit[0]), run_time=2) 
        self.wait(1)
        self.play(Write(current_label))
        self.wait(1)
        self.play(ReplacementTransform(junction_text,kvl_equation,run_time=2))
        self.wait(1)
        self.play(Indicate(circuit[2]),Indicate(circuit[4]), run_time=2) 
        self.wait(1)
        self.play(ReplacementTransform(current_label,current_labels,run_time=2))
        self.wait(2)
        self.play(ReplacementTransform(current_labels,current_label3,run_time=2))
        self.wait(2)
        self.play(ReplacementTransform(current_label3,current_label4,run_time=2))
        self.wait(2)
        self.play(Indicate(circuit[0]), run_time=2) 
        self.wait(1)
        self.play(FadeOut(kvl_equation),FadeOut(current_label4))
        


class KirchhoffsVoltageLaw(Scene):
    def construct(self):
         
        # Adding circuitikz package to the preamble

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        circuit_tex = [
            r"""\draw (0,0) to[V, v=$V_s$, color=red] (0,3);""",
            r"""\draw (0,3) to[R=$R_1$, color=yellow] (3,3);""",
            r"""\draw (3,3) to[R=$R_2$, color=blue] (3,0);""",
            r"\draw (3,0) -- (0,0);"
        ]

        circuit = MathTex(*circuit_tex,
            stroke_width=3,
            fill_opacity=0,
            stroke_opacity=1,
            tex_environment="circuitikz",
            tex_template=template
        )

        circuit.set_color_by_tex_to_color_map({"V_s":RED, "R_1":YELLOW, "R_2":BLUE})

        # Add labels for the currents and voltages
        voltage_label1 = MathTex(r"\overset{V_{R1} }{\leftrightarrow } ", color=YELLOW).next_to(circuit[1], DOWN)
        voltage_label2 = MathTex(r"\overset{V_{R2} }{\updownarrow }", color=BLUE).next_to(circuit[2], RIGHT)

        voltage_labels = VGroup(voltage_label1, voltage_label2)

        kvl_text = Text("sum of potential changes around any closed loop involving resistors and cells is 0", font_size=24).shift(UP*3.5)
        kvl_equation = MathTex(r"V_s"," = ",r"V_1 ","+",r" V_2", font_size=42).shift(UP*3.5)
        kvl_equation[0].set_color(RED) 
        kvl_equation[2].set_color(YELLOW) 
        kvl_equation[4].set_color(BLUE) 

        kvl_group1 = VGroup( kvl_equation[1],  kvl_equation[2])
        kvl_group2 = VGroup( kvl_equation[3],  kvl_equation[4])
        kvl_equation2 = MathTex(r"V_s"," ="," I \cdot R_1 ","+"," I \cdot R_2", font_size=42).shift(UP*3.5)
        kvl_equation2.set_color_by_tex("V_s", RED)
        kvl_equation2.set_color_by_tex("R_1", YELLOW)
        kvl_equation2.set_color_by_tex("R_2", BLUE)

        current_label1 = MathTex(r"I \uparrow").next_to(circuit[0], LEFT) 
        current_label2 = MathTex(r"I \rightarrow").next_to(circuit[1], UP)
        current_label3 = MathTex(r"I \downarrow").next_to(circuit[2], LEFT)
        current_label4 = MathTex(r"\leftarrow I").next_to(circuit[3], DOWN)



        self.play(Write(circuit, shift=UP, target_position=ORIGIN), run_time=3)
        self.wait(1)
        self.play(Write(kvl_text),run_time=2)
        self.wait(1)
        self.play(Write(voltage_label1),Write(voltage_label2))
        self.wait(2)
        self.play(FadeOut(kvl_text,run_time=2))
        self.wait(2)
        self.play(Indicate(circuit[0]),Write(kvl_equation[0]), run_time=2)
        self.wait(1)
        self.play(Indicate(circuit[1]),Write(kvl_group1), run_time=2)
        self.wait(1)
        self.play(Indicate(circuit[2]),Write(kvl_group2), run_time=2)
        self.wait(1)
        self.play(Write(current_label1),run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(current_label1,current_label2),run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(current_label2,current_label3),run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(current_label3,current_label4),run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(kvl_equation,kvl_equation2,run_time=2))
        self.wait(2)

        self.play(FadeOut(kvl_equation2),FadeOut(current_label4))
        self.wait(2)
        

