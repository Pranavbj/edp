from manim import *

class FormulaAnimation(Scene):
    def construct(self):
        # Define the formula
        formula = MathTex(
            "W(s) = \\int \\vec{f}(s) \\cdot d \\cdot (\\vec{s})"
        )

        # Add the formula to the scene
        self.play(Write(formula))

        # Add animation (e.g., scaling)
        self.wait(1)  # Wait for 1 second
        self.play(formula.animate.scale(1.5))
        self.wait(1)

        # You can add more animations as needed

        # Remove the formula
        self.play(FadeOut(formula))
        self.wait(1)

