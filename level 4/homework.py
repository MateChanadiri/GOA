from turtle import *

#drawing the rectangle

width(5)
color("gray")
begin_fill()

penup()
goto(100,100)
pendown()
right(180)
forward(200)
left(90)
forward(400)
left(90)
forward(200)
left(90)
forward(400)
left(40)
end_fill()
#drawing the triangle
color("black")
begin_fill()
forward(170)
left(105)
forward(160)
end_fill()
#drawing the second triangle a window where the king will be standing
penup()
goto(-5,170)
color("gray")
begin_fill()
pendown()
left(80)
forward(50)
right(135)
forward(60)
right(130)
forward(45)
end_fill()
#drawing the king
penup()
goto(10,140)
color("yellow")
begin_fill()
pendown()
circle(10)
end_fill()
#drawing the GOA logo first the letter  G
penup()
goto(10,80)
pendown()
color("black")
left(180)
forward(90)
left(130)
forward(90)
left(90)
forward(30)
left(90)
forward(60)
#drawing the GOA logo second the letter O
penup()
goto(0,0)
begin_fill()
pendown()
circle(50)
end_fill()
#drawing the GOA logo third letter      A
penup()
goto(-40, -210)
pendown()
left(250)
forward(90)
left(360)
left(230)
forward(90)
penup()
goto(-30,-150)
pendown()
left(40)
forward(50)
exitonclick





