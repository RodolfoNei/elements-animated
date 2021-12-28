from manim import *
config.background_color = WHITE

# Elements components definitions

class SampleII(Scene):
    def construct(self):
        self.play(Write(Text('Prop. II Test').set_color(BLACK)))
        self.wait(3)