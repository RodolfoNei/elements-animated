# import sys
from manim import *
config.background_color = WHITE

solText1 = Text('With A as centre, and AB as radius,\ndescribe the circle BCD')
solText2 = Text('With B as centre, and BA as radius,\ndescribe the circle ACE,\ncutting the former circle in C.')
solText3 = Text('Join CA, CB')
solText4 = Text('Then ABC is the equilateral triangle required.')
text_group = VGroup(solText1, solText2, solText3, solText4).arrange(direction=DOWN, aligned_edge=LEFT, buff=1).shift(3*LEFT).scale(0.5).set_color(BLACK)

lineAB = Line()

pointA = lineAB.get_start()
pointA_text = Text('A', size=0.75).next_to(pointA, LEFT)

pointB = lineAB.get_end()
pointB_text = Text('B', size=0.75).next_to(pointB, RIGHT)

circleBCD = Circle(radius=lineAB.width).move_arc_center_to(pointA)
pointD_text = Text('D', size=0.75).next_to(circleBCD, LEFT)
circleACE = Circle(radius=lineAB.width).move_arc_center_to(pointB)
pointE_text = Text('E', size=0.75).next_to(circleACE, RIGHT)
lineCA = Line(circleBCD.point_at_angle(60*DEGREES), pointA)
lineCB = Line(circleACE.point_at_angle(120*DEGREES), pointB)

pointC = lineCA.get_start()
pointC_text = Text('C', size=0.75).next_to(pointC, UP)

triangleGroup = VGroup(lineCA, lineAB, lineCB)
fullElemGroup = VGroup(pointA_text, pointB_text, circleBCD, pointD_text, circleACE, pointE_text, pointC_text, triangleGroup).shift(3.5*RIGHT).scale(0.85).set_color(BLACK)

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
        self.wait(1)
        
        self.play(Write(pointA_text), Write(pointB_text))
        self.play(Create(lineAB))

        self.play(Write(solText1))
        self.wait(1)
        self.play(Create(circleBCD))
        self.play(Write(pointC_text))
        self.play(Write(pointD_text))

        self.wait(1)

        self.play(Write(solText2))
        self.wait(2)
        self.play(Create(circleACE))
        self.play(Write(pointE_text))

        self.wait(1)

        self.play(Write(solText3))
        self.wait(1)
        self.play(Create(lineCA))
        self.play(Create(lineCB))

        self.play(Write(solText4), triangleGroup.animate.set_color('#800080'))
        self.wait(1)

class DemI(Scene):
    def construct(self):
        self.add(fullElemGroup)
        self.wait(3)