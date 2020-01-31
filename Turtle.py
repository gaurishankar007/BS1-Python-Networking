import turtle
A = turtle.Turtle()
A.pencolor("blue")  # Coloring the lines with color
A.forward(200)
A.left(90)
A.forward(200)
A.left(90)
A.forward(200)
A.left(90)
A.forward(200)
# Using loop
B = turtle.Turtle()
for i in range(2):
    B.forward(100)
    B.left(90)
    B.forward(100)
    B.left(90)
# Drawing circle from the same starting point
B.begin_fill()
B.shape('triangle')  # This replaces the arrow with the triangle and also with arrow, circle etc.
B.circle(40)
B.fillcolor("yellow")
B.end_fill()

B.penup()  # This stops from being written in the picture from the starting point
B.goto(100, 300)
B.pendown()
B.begin_fill()
B.shape("arrow")
B.circle(50)
B.fillcolor("red")
B.end_fill()

C = turtle.Turtle()
for j in range(10):
    C.circle(10*j)
    C.up()  # Same as penup()
    C.sety((10*j)*(-1))
    C.down()  # Same as pendown()

D = turtle.Turtle()
D.penup()
D.goto(125, -175)
D.down()
for k in range(5):
    D.circle(10*k)

E = turtle.Turtle()
E.up()
E.setx(-300)
E.down()
for i in range(1, 10):
    E.circle(10*i)
    E.up()
    E.sety((10*i)*-1)
    E.down()

# This makes the picture not to stop from being shown up at the screen and also stops the turtle codes from being run written below it.
turtle.done()
