import colorgram
import turtle as t
import random
t.colormode(255)
rgb_codes = []
colors = colorgram.extract('OIP.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    my_color = (r, g, b)

    rgb_codes.append(my_color)

t.colormode(255)

hirst = t.Turtle()
hirst.speed("fastest")
hirst.penup()
hirst.setheading(225)
hirst.forward(400)
hirst.setheading(0)
hirst.setheading(180)
hirst.forward(80)
hirst.setheading(0)

total = 13*17
for dot in range(1, total+1):

    hirst.dot(20, random.choice(rgb_codes))
    hirst.penup()
    hirst.forward(50)
    hirst.pendown()
    if dot % 17 == 0:

        hirst.penup()
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(850)
        hirst.setheading(0)

hirst.hideturtle()
screen = t.Screen()
screen.exitonclick()
