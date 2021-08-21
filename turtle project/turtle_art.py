'''
Project 1 - Turtle Art - Spring 2020
Author: <Nicholas Richard Cerne, ncerne00, 9061-81543>

This program uses turtle graphics to generate a drawing of our solar system.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Nick Cerne
'''


import turtle
import random
#main stuff
wn = turtle.Screen()
wn.bgcolor("#6c32ab")
turtle.speed(0)
turtle.setup(600, 600)
turtle.title("Project 1 - Turtle Art")


#random stars
s = 0
t = 50
turtle.pencolor("white")
while s < t:
    s += 1
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
    


# sun
turtle.penup()
turtle.goto(0,0)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#mercury
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(0, -35)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#venus
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(75)
turtle.penup()
turtle.goto(35, -50)
turtle.fillcolor("#c46200")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Earth
turtle.penup()
turtle.goto(0, -75)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(95, 0)
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Mars
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(125)
turtle.penup()
turtle.goto(-125, 0)
turtle.fillcolor("tan")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Jupiter
turtle.penup()
turtle.goto(0, -125)
turtle.pendown()
turtle.circle(150)
turtle.penup()
turtle.goto(0, 165)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Saturn
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(175)
turtle.penup()
turtle.goto(-50, 180)
turtle.fillcolor("beige")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Uranus
turtle.penup()
turtle.goto(0, -175)
turtle.pendown()
turtle.circle(200)
turtle.penup()
turtle.goto(200, 0)
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Neptune
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(225)
turtle.penup()
turtle.goto(223, 50)
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Pluto
turtle.penup()
turtle.goto(0, -225)
turtle.pendown()
turtle.circle(250)
turtle.penup()
turtle.goto(-248, 0)
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#drawn star shape
turtle.penup()
turtle.goto(-300, -205)
turtle.pencolor("yellow")
turtle.pendown()
for i in range(5): #angles of which star are drawn
    turtle.forward(150)
    turtle.right(144)

#drawn star shape
turtle.penup()
turtle.goto(145, -205)
turtle.pencolor("yellow")
turtle.pendown()
for i in range(5):
    turtle.forward(150)
    turtle.right(144)

# border frame
turtle.pencolor("Black")
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
for i in range(5):
    turtle.forward(595)
    turtle.pensize(20)
    turtle.right(90)


