from turtle import *

#we want to make a house

#step one draw a square:

width(7)

speed(4)

color("green")

begin_fill()

forward(200)

left(90)


forward (200)

left(90)

forward(200)

left(90)


forward (200)

left(90)

end_fill()

#end of square 

#step two draw a door:


begin_fill()

forward(70)

color("yellow")

left(90)

forward(120)   #height of the door.

right(90)

forward(60)

right(90)

forward(120)

end_fill()

penup()

goto(200,200)

pendown()

#end of door


#step three drawing a roof:


color("red")

begin_fill()

right(150)

forward(200)

left(120)

forward(200)

end_fill()

#end of roof


#step four making window1 :


penup()

goto(200,200)

color("brown")

begin_fill()

pendown()

left(90)

penup()

goto(170,170)

pendown()


right(30)

pendown()

right(30)

right(60)

right(10)

right(5)

right(5)

right(10)

forward(40)

left(90)

forward(40)

left(90)

forward(40)

left(90)

forward(40)

end_fill()


#step five making window2:

penup()

goto(10,10)

pendown()

penup()

goto(50,50)

color("brown")

begin_fill()

forward(119)

pendown()

left(90)

forward(40)

left(90)

forward(40)

left(90)

forward(40)

left(90)

forward(40)

end_fill()

#end of making/drawing a house.




exitonclick()



