# import sys
from manim import *
config.background_color = WHITE

solText1 = MarkupText('With <i>A</i> as centre, and <i>AB</i> as radius,\ndescribe the circle <i>BCD</i>')
solText2 = MarkupText('With <i>B</i> as centre, and <i>BA</i> as radius,\ndescribe the circle <i>ACE</i>,\ncutting the former circle in <i>C</i>')
solText3 = MarkupText('Join <i>CA</i>, <i>CB</i>')
solText4 = MarkupText('Then <i>ABC is the equilateral triangle required</i>')
VGroup(solText1, solText2, solText3, solText4).arrange(direction=DOWN, aligned_edge=LEFT, buff=1).shift(3*LEFT).scale(0.5).set_color(BLACK)

demText1 = MarkupText('Because <i>A</i> is the centre of the circle <i>BCD</i>,\n<i>AC</i> is equal to <i>AB</i>')
demText2 = MarkupText('Again, because <i>B</i> is the centre of the circle <i>ACE</i>,\n<i>BC</i> is equal to <i>BA</i>')
demText3 = MarkupText('Hence we have proved <i>AC</i> = <i>AB</i>, and <i>BC</i> = <i>AB</i>')
demText4 = MarkupText('But things which are equal to the same are\nequal to one another; therefore <i>AC</i> is equal\nto <i>BC</i>')
demText5 = MarkupText('Therefore the three lines <i>AB</i>, <i>BC</i>, <i>CA</i>\nare equal to one another')
demText6 = MarkupText('Hence the triangle <i>ABC</i> is equilateral;\nand it is described on the given line <i>AB</i>,\n<i>which was required to be done</i>')
VGroup(demText1, demText2, demText3, demText4, demText5, demText6).arrange(direction=DOWN, aligned_edge=LEFT, buff=1).shift(3.5*LEFT).scale(0.4).set_color(BLACK)

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
        text = Text('On a given finite right line (AB) to construct an equilateral triangle', color=BLACK, slant=ITALIC).scale(0.55)
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

        self.play(Write(solText4))
        self.wait(1)

class DemI(Scene):
    def construct(self):
        self.add(fullElemGroup)

        self.play(Write(demText1), VGroup(lineAB, lineCA).animate.set_color(RED))
        self.wait(2)
        self.play(VGroup(lineAB, lineCA).animate.set_color(BLACK))

        self.play(Write(demText2), VGroup(lineAB, lineCB).animate.set_color(RED))
        self.wait(2)
        self.play(VGroup(lineAB, lineCB).animate.set_color(BLACK))

        self.play(Write(demText3))
        self.wait(1)
        self.play(Write(demText4), VGroup(lineCA, lineCB).animate.set_color(RED))
        self.wait(4)
        self.play(VGroup(lineCA, lineCB).animate.set_color(BLACK))


        self.play(Write(demText5), triangleGroup.animate.set_color(RED))
        self.wait(1)
        self.play(Write(demText6))
        self.wait(3)