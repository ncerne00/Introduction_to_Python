import turtle

turtle.setup(600, 600)
turtle.title("My First Turtle Drawing")

turtle.forward(200)
turtle.right(90)
turtle.forward(90)

turtle.right(45)
turtle.pensize(4)
turtle.pencolor("red")
turtle.forward(200)

turtle.setheading(90) #point the turtle at 90 degrees
turtle.pencolor("green")
turtle.forward(400)

turtle.setheading(200)
turtle.pencolor("cyan")
turtle.forward(200)

turtle.setheading(-45)
turtle.pencolor("mediumaquamarine")
turtle.forward(200)

turtle.penup()
turtle.goto(-200, 300)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.goto(-200, -200)
turtle.setheading(45)
turtle.pencolor("blue")
turtle.pendown()
turtle.dot()
turtle.forward(100)
turtle.dot()

turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.circle(70, extent=180) # extent is a keyword argument, what extent of the circle do you wanna draw? 

turtle.penup()
turtle.goto(200, 100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()


turtle.done()
