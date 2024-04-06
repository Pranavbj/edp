from manim import *

class BrownianMotion(Scene):
    def construct(self):
        text1 = Text(".", color=BLUE).shift(UP * 2 + RIGHT * 1)
        text2 = Text(".", color=BLUE).shift(UP * 1 + RIGHT * -2)
        text3 = Text(".", color=BLUE).shift(UP * 3 + RIGHT * 3)
        text4 = Text(".", color=BLUE).shift(DOWN * 1 + RIGHT * -1)
        text5 = Text(".", color=BLUE).shift(DOWN * 2 + RIGHT * 3)
        text6 = Text(".", color=BLUE).shift(UP * 3 + RIGHT * -3)
        text7 = Text(".", color=BLUE).shift(DOWN * 3 + RIGHT * 1)
        text8 = Text(".", color=BLUE).shift(UP * 1 + RIGHT * 0)
        text9 = Text(".", color=BLUE).shift(DOWN * 2 + RIGHT * -2)
        text10 = Text(".", color=BLUE).shift(UP * 1 + RIGHT * 2)

        arrows_texts = [
            (Arrow(text1.get_center(), text2.get_center(), color=WHITE), text1, text2),
            (Arrow(text2.get_center(), text3.get_center(), color=WHITE), text2, text3),
            (Arrow(text3.get_center(), text4.get_center(), color=WHITE), text3, text4),
            (Arrow(text4.get_center(), text5.get_center(), color=WHITE), text4, text5),
            (Arrow(text5.get_center(), text6.get_center(), color=WHITE), text5, text6),
            (Arrow(text6.get_center(), text7.get_center(), color=WHITE), text6, text7),
            (Arrow(text7.get_center(), text8.get_center(), color=WHITE), text7, text8),
            (Arrow(text8.get_center(), text9.get_center(), color=WHITE), text8, text9),
            (Arrow(text9.get_center(), text10.get_center(), color=WHITE), text9, text10)
        ]

        for arrow, text1, text2 in arrows_texts:
            self.play(Create(arrow), Write(text1), Write(text2))
            self.wait(1)

        for arrow, text1, text2 in arrows_texts:
            self.remove(arrow, text1, text2)
