from turtle import Turtle, Screen
pen = Turtle()


def dotted_line():
    for _ in range(4):

        for _ in range(10):
            pen.forward(10)
            pen.penup()
            pen.forward(10)
            pen.pendown()

        pen.left(90)
    pen.left(45)

    for _ in range(14):

        pen.penup()

        pen.forward(10)
        pen.pendown()
        pen.forward(10)
    pen.left(135)
    pen.penup()
    pen.forward(200)
    pen.pendown()
    pen.left(135)
    for _ in range(14):

        pen.penup()

        pen.forward(10)
        pen.pendown()
        pen.forward(10)


for _ in range(4):
    dotted_line()
    pen.right(45)
pen.left(45)
pen.right(90)

for _ in range(4):
    dotted_line()
    pen.right(45)


screen = Screen()
screen.exitonclick()
