from lib import graphics as gr
window = gr.GraphWin("TY_Picture", 500, 350)
print('Задание 1')#------------------------------------------------Exercise 1
"""Code not optimized"""
TY_Field1 = gr.Rectangle(gr.Point(0,350), gr.Point(500,200))
TY_Field1.draw(window)
TY_Field1.setFill('Green')

TY_Flower1 = gr.Circle(gr.Point(80,300),15)
TY_Flower1.setFill('Red')
TY_Flower1.draw(window)

TY_Flower2 = gr.Circle(gr.Point(160,280),15)
TY_Flower2.setFill('Red')
TY_Flower2.draw(window)

TY_Flower3 = gr.Circle(gr.Point(240,320),15)
TY_Flower3.setFill('Red')
TY_Flower3.draw(window)

TY_Flower3 = gr.Circle(gr.Point(210,240),15)
TY_Flower3.setFill('Red')
TY_Flower3.draw(window)

TY_House_Roof = gr.Circle(gr.Point(350,150),50)
TY_House_Roof.setFill('Brown')
TY_House_Roof.draw(window)

TY_House_Wall = gr.Rectangle(gr.Point(300,300), gr.Point(400,150))
TY_House_Wall.setFill('Gray')
TY_House_Wall.draw(window)

TY_House_Step = gr.Rectangle(gr.Point(320,300),gr.Point(380,280))
TY_House_Step.setFill('Black')
TY_House_Step.draw(window)

TY_House_Door = gr.Rectangle(gr.Point(330,280),gr.Point(370,220))
TY_House_Door.setFill('Orange')
TY_House_Door.draw(window)

TY_House_Tube = gr.Rectangle(gr.Point(370,130),gr.Point(390,90))
TY_House_Tube.setFill('Black')
TY_House_Tube.draw(window)

TY_Tree_Wood = gr.Rectangle(gr.Point(50,220),gr.Point(80,170))
TY_Tree_Wood.setFill('Brown')
TY_Tree_Wood.draw(window)

TY_Tree_Leafs = gr.Circle(gr.Point(65,145),50)
TY_Tree_Leafs.setFill('Green')
TY_Tree_Leafs.draw(window)

TY_Tree_Apple1 = gr.Circle(gr.Point(80,155),10)
TY_Tree_Apple1.setFill('Yellow')
TY_Tree_Apple1.draw(window)

TY_Tree_Apple2 = gr.Circle(gr.Point(60,115),10)
TY_Tree_Apple2.setFill('Yellow')
TY_Tree_Apple2.draw(window)

TY_Tree_Apple3 = gr.Circle(gr.Point(90,125),10)
TY_Tree_Apple3.setFill('Yellow')
TY_Tree_Apple3.draw(window)

TY_Cloud_1 = gr.Circle(gr.Point(150,20),15)
TY_Cloud_1.setFill('Blue')
TY_Cloud_1.draw(window)

TY_Cloud_2 = gr.Circle(gr.Point(170,20),15)
TY_Cloud_2.setFill('Blue')
TY_Cloud_2.draw(window)

TY_Cloud_3 = gr.Circle(gr.Point(135,35),15)
TY_Cloud_3.setFill('Blue')
TY_Cloud_3.draw(window)

TY_Cloud_4 = gr.Circle(gr.Point(155,35),15)
TY_Cloud_4.setFill('Blue')
TY_Cloud_4.draw(window)

TY_Cloud_5 = gr.Circle(gr.Point(180,35),15)
TY_Cloud_5.setFill('Blue')
TY_Cloud_5.draw(window)

TY_Sun_Circle = gr.Circle(gr.Point(500,0),50)
TY_Sun_Circle.setFill('Yellow')
TY_Sun_Circle.draw(window)

TY_Sun_Ray1 = gr.Line(gr.Point(500,0),gr.Point(420,120))
TY_Sun_Ray1.setFill('Yellow')
TY_Sun_Ray1.draw(window)

TY_Sun_Ray2 = gr.Line(gr.Point(500,0),gr.Point(350,90))
TY_Sun_Ray2.setFill('Yellow')
TY_Sun_Ray2.draw(window)

TY_Sun_Ray3 = gr.Line(gr.Point(500,0),gr.Point(280,50))
TY_Sun_Ray3.setFill('Yellow')
TY_Sun_Ray3.draw(window)

TY_Sun_Ray4 = gr.Line(gr.Point(500,0),gr.Point(200,20))
TY_Sun_Ray4.setFill('Yellow')
TY_Sun_Ray4.draw(window)

window.getMouse()
window.close()

print('Задание 2')#------------------------------------------------Exercise 2
"""Functions added"""
window = gr.GraphWin("TY_Picture", 500, 350)
TY_Field1 = gr.Rectangle(gr.Point(0,350), gr.Point(500,200))
TY_Field1.draw(window)
TY_Field1.setFill('Green')

def TY_Flowers():
    TY_Flower1 = gr.Circle(gr.Point(80,300),15)
    TY_Flower1.setFill('Red')
    TY_Flower1.draw(window)

    TY_Flower2 = gr.Circle(gr.Point(160,280),15)
    TY_Flower2.setFill('Red')
    TY_Flower2.draw(window)

    TY_Flower3 = gr.Circle(gr.Point(240,320),15)
    TY_Flower3.setFill('Red')
    TY_Flower3.draw(window)

    TY_Flower3 = gr.Circle(gr.Point(210,240),15)
    TY_Flower3.setFill('Red')
    TY_Flower3.draw(window)

def TY_House():
    TY_House_Roof = gr.Circle(gr.Point(350,150),50)
    TY_House_Roof.setFill('Brown')
    TY_House_Roof.draw(window)

    TY_House_Wall = gr.Rectangle(gr.Point(300,300), gr.Point(400,150))
    TY_House_Wall.setFill('Gray')
    TY_House_Wall.draw(window)

    TY_House_Step = gr.Rectangle(gr.Point(320,300),gr.Point(380,280))
    TY_House_Step.setFill('Black')
    TY_House_Step.draw(window)

    TY_House_Door = gr.Rectangle(gr.Point(330,280),gr.Point(370,220))
    TY_House_Door.setFill('Orange')
    TY_House_Door.draw(window)

    TY_House_Tube = gr.Rectangle(gr.Point(370,130),gr.Point(390,90))
    TY_House_Tube.setFill('Black')
    TY_House_Tube.draw(window)

def TY_Tree():
    TY_Tree_Wood = gr.Rectangle(gr.Point(50,220),gr.Point(80,170))
    TY_Tree_Wood.setFill('Brown')
    TY_Tree_Wood.draw(window)

    TY_Tree_Leafs = gr.Circle(gr.Point(65,145),50)
    TY_Tree_Leafs.setFill('Green')
    TY_Tree_Leafs.draw(window)

    TY_Tree_Apple1 = gr.Circle(gr.Point(80,155),10)
    TY_Tree_Apple1.setFill('Yellow')
    TY_Tree_Apple1.draw(window)

    TY_Tree_Apple2 = gr.Circle(gr.Point(60,115),10)
    TY_Tree_Apple2.setFill('Yellow')
    TY_Tree_Apple2.draw(window)

    TY_Tree_Apple3 = gr.Circle(gr.Point(90,125),10)
    TY_Tree_Apple3.setFill('Yellow')
    TY_Tree_Apple3.draw(window)

def TY_Cloud1():
    TY_Cloud_1 = gr.Circle(gr.Point(100,20),15)
    TY_Cloud_1.setFill('Blue')
    TY_Cloud_1.draw(window)

    TY_Cloud_2 = gr.Circle(gr.Point(120,20),15)
    TY_Cloud_2.setFill('Blue')
    TY_Cloud_2.draw(window)

    TY_Cloud_3 = gr.Circle(gr.Point(140,20),15)
    TY_Cloud_3.setFill('Blue')
    TY_Cloud_3.draw(window)

    TY_Cloud_4 = gr.Circle(gr.Point(110,35),15)
    TY_Cloud_4.setFill('Blue')
    TY_Cloud_4.draw(window)

    TY_Cloud_5 = gr.Circle(gr.Point(130,35),15)
    TY_Cloud_5.setFill('Blue')
    TY_Cloud_5.draw(window)

def TY_Cloud2():
    TY_Cloud_1 = gr.Circle(gr.Point(250,60),15)
    TY_Cloud_1.setFill('Blue')
    TY_Cloud_1.draw(window)

    TY_Cloud_2 = gr.Circle(gr.Point(270,60),15)
    TY_Cloud_2.setFill('Blue')
    TY_Cloud_2.draw(window)

    TY_Cloud_3 = gr.Circle(gr.Point(290,60),15)
    TY_Cloud_3.setFill('Blue')
    TY_Cloud_3.draw(window)

    TY_Cloud_4 = gr.Circle(gr.Point(260,75),15)
    TY_Cloud_4.setFill('Blue')
    TY_Cloud_4.draw(window)

    TY_Cloud_5 = gr.Circle(gr.Point(280,75),15)
    TY_Cloud_5.setFill('Blue')
    TY_Cloud_5.draw(window)

def TY_Cloud3():
    TY_Cloud_1 = gr.Circle(gr.Point(400,100),15)
    TY_Cloud_1.setFill('Blue')
    TY_Cloud_1.draw(window)

    TY_Cloud_2 = gr.Circle(gr.Point(420,100),15)
    TY_Cloud_2.setFill('Blue')
    TY_Cloud_2.draw(window)

    TY_Cloud_3 = gr.Circle(gr.Point(440,100),15)
    TY_Cloud_3.setFill('Blue')
    TY_Cloud_3.draw(window)

    TY_Cloud_4 = gr.Circle(gr.Point(410,115),15)
    TY_Cloud_4.setFill('Blue')
    TY_Cloud_4.draw(window)

    TY_Cloud_5 = gr.Circle(gr.Point(430,115),15)
    TY_Cloud_5.setFill('Blue')
    TY_Cloud_5.draw(window)

def TY_Sun():
    TY_Sun_Circle = gr.Circle(gr.Point(500,0),50)
    TY_Sun_Circle.setFill('Yellow')
    TY_Sun_Circle.draw(window)

    TY_Sun_Ray1 = gr.Line(gr.Point(500,0),gr.Point(420,120))
    TY_Sun_Ray1.setFill('Yellow')
    TY_Sun_Ray1.draw(window)

    TY_Sun_Ray2 = gr.Line(gr.Point(500,0),gr.Point(350,90))
    TY_Sun_Ray2.setFill('Yellow')
    TY_Sun_Ray2.draw(window)

    TY_Sun_Ray3 = gr.Line(gr.Point(500,0),gr.Point(280,50))
    TY_Sun_Ray3.setFill('Yellow')
    TY_Sun_Ray3.draw(window)

    TY_Sun_Ray4 = gr.Line(gr.Point(500,0),gr.Point(200,20))
    TY_Sun_Ray4.setFill('Yellow')
    TY_Sun_Ray4.draw(window)

def TY_picture():
    TY_Cloud1()
    TY_Cloud2()
    TY_Cloud3()
    TY_Flowers()
    TY_Sun()
    TY_Tree()
    TY_House()

TY_picture()

window.getMouse()
window.close()

print('Задание 3')#------------------------------------------------Exercise 3
"""Parameters added """
window = gr.GraphWin("TY_Picture", 500, 350)
TY_Field1 = gr.Rectangle(gr.Point(0,350), gr.Point(500,200))
TY_Field1.draw(window)
TY_Field1.setFill('Green')

def TY_Flowers1(position):
    TY_Flower1 = gr.Circle(gr.Point(80+position,300),15)
    TY_Flower1.setFill('Red')
    TY_Flower1.draw(window)

    TY_Flower2 = gr.Circle(gr.Point(160+position,280),15)
    TY_Flower2.setFill('Red')
    TY_Flower2.draw(window)

    TY_Flower3 = gr.Circle(gr.Point(240+position,320),15)
    TY_Flower3.setFill('Red')
    TY_Flower3.draw(window)

    TY_Flower3 = gr.Circle(gr.Point(210+position,240),15)
    TY_Flower3.setFill('Red')
    TY_Flower3.draw(window)

def TY_House1(place):
    TY_House_Roof = gr.Circle(gr.Point(350+place,150),50)
    TY_House_Roof.setFill('Brown')
    TY_House_Roof.draw(window)

    TY_House_Wall = gr.Rectangle(gr.Point(300+place,300), gr.Point(400+place,150))
    TY_House_Wall.setFill('Gray')
    TY_House_Wall.draw(window)

    TY_House_Step = gr.Rectangle(gr.Point(320+place,300),gr.Point(380+place,280))
    TY_House_Step.setFill('Black')
    TY_House_Step.draw(window)

    TY_House_Door = gr.Rectangle(gr.Point(330+place,280),gr.Point(370+place,220))
    TY_House_Door.setFill('Orange')
    TY_House_Door.draw(window)

    TY_House_Tube = gr.Rectangle(gr.Point(370+place,130),gr.Point(390+place,90))
    TY_House_Tube.setFill('Black')
    TY_House_Tube.draw(window)

def TY_Tree1(mesto):
    TY_Tree_Wood = gr.Rectangle(gr.Point(50+mesto,220),gr.Point(80+mesto,170))
    TY_Tree_Wood.setFill('Brown')
    TY_Tree_Wood.draw(window)

    TY_Tree_Leafs = gr.Circle(gr.Point(65+mesto,145),50)
    TY_Tree_Leafs.setFill('Green')
    TY_Tree_Leafs.draw(window)

    TY_Tree_Apple1 = gr.Circle(gr.Point(80+mesto,155),10)
    TY_Tree_Apple1.setFill('Yellow')
    TY_Tree_Apple1.draw(window)

    TY_Tree_Apple2 = gr.Circle(gr.Point(60+mesto,115),10)
    TY_Tree_Apple2.setFill('Yellow')
    TY_Tree_Apple2.draw(window)

    TY_Tree_Apple3 = gr.Circle(gr.Point(90+mesto,125),10)
    TY_Tree_Apple3.setFill('Yellow')
    TY_Tree_Apple3.draw(window)

def TY_Cloud(x,y):
    TY_Cloud_1 = gr.Circle(gr.Point(x,y),15)
    TY_Cloud_1.setFill('Blue')
    TY_Cloud_1.draw(window)

    TY_Cloud_2 = gr.Circle(gr.Point(x+20,y),15)
    TY_Cloud_2.setFill('Blue')
    TY_Cloud_2.draw(window)

    TY_Cloud_3 = gr.Circle(gr.Point(x+40,y),15)
    TY_Cloud_3.setFill('Blue')
    TY_Cloud_3.draw(window)

    TY_Cloud_4 = gr.Circle(gr.Point(x+10,y+15),15)
    TY_Cloud_4.setFill('Blue')
    TY_Cloud_4.draw(window)

    TY_Cloud_5 = gr.Circle(gr.Point(x+30,y+15),15)
    TY_Cloud_5.setFill('Blue')
    TY_Cloud_5.draw(window)

def TY_Sun1():
    TY_Sun_Circle = gr.Circle(gr.Point(500,0),50)
    TY_Sun_Circle.setFill('Yellow')
    TY_Sun_Circle.draw(window)

    TY_Sun_Ray1 = gr.Line(gr.Point(500,0),gr.Point(420,120))
    TY_Sun_Ray1.setFill('Yellow')
    TY_Sun_Ray1.draw(window)

    TY_Sun_Ray2 = gr.Line(gr.Point(500,0),gr.Point(350,90))
    TY_Sun_Ray2.setFill('Yellow')
    TY_Sun_Ray2.draw(window)

    TY_Sun_Ray3 = gr.Line(gr.Point(500,0),gr.Point(280,50))
    TY_Sun_Ray3.setFill('Yellow')
    TY_Sun_Ray3.draw(window)

    TY_Sun_Ray4 = gr.Line(gr.Point(500,0),gr.Point(200,20))
    TY_Sun_Ray4.setFill('Yellow')
    TY_Sun_Ray4.draw(window)

def TY_picture():
    TY_Cloud(20,20)
    TY_Cloud(160,70)
    TY_Cloud(300,40)
    TY_Flowers1(200)
    TY_Sun()
    TY_Tree1(250)
    TY_House1(-250)

TY_picture()

window.getMouse()
window.close()
