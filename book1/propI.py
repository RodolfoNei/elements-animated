# import sys
from manim import *
config.background_color = WHITE

class ProblemI(Scene):
    def construct(self):
        title = Text('PROP. I - PROBLEM', color=BLACK)
        text = Text('On a given finite right line (AB) to construct an equilateral triangle.', color=BLACK, slant=ITALIC).scale(0.55)
        VGroup(title, text).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(Write(text))

        self.wait(3)

class SolI(Scene):
    def construct(self):
        lineAB = Line(color=BLACK)

        pointA = lineAB.get_start()
        pointA_text = Text('A', size=0.75, color=BLACK).next_to(pointA, LEFT)

        pointB = lineAB.get_end()
        pointB_text = Text('B', size=0.75, color=BLACK).next_to(pointB, RIGHT)

        circleBCD = Circle(radius=lineAB.width, color=BLACK).move_arc_center_to(pointA)
        pointD_text = Text('D', size=0.75, color=BLACK).next_to(circleBCD, LEFT)
        circleACE = Circle(radius=lineAB.width, color=BLACK).move_arc_center_to(pointB)
        pointE_text = Text('E', size=0.75, color=BLACK).next_to(circleACE, RIGHT)
        lineCA = Line(pointA, circleBCD.point_at_angle(60*DEGREES), color=BLACK)
        lineCB = Line(pointB, circleACE.point_at_angle(120*DEGREES), color=BLACK)

        pointC = lineCA.get_end()
        pointC_text = Text('C', size=0.75, color=BLACK).next_to(pointC, UP)

        self.wait(1)

        self.play(Write(pointA_text), Write(pointB_text))
        self.play(Create(lineAB))

        self.wait(1)

        self.play(Create(circleBCD))
        self.play(Write(pointC_text))
        self.play(Write(pointD_text))

        self.wait(1)

        self.play(Create(circleACE))
        self.play(Write(pointE_text))

        self.wait(1)

        self.play(Create(lineCA))

        self.wait(1)

        self.play(Create(lineCB))

        self.wait(1)