import turtle as t
from turtle import Screen
import random
tim = t.Turtle()

color = ["red", "green", "blue", "yellow",
         "orange", "purple", "pink", "grey", "black",  "brown", "violet", "cyan", "magenta", "indigo"]


def draw(num_sides, end):
    while num_sides < end:
        num_sides += 1

        for _ in range(num_sides):
            angle = 360/num_sides
            tim.forward(70)
            tim.right(angle)

        tim.color(color[random.randint(0, 13)])


draw(1, 18)
tim.hideturtle()

screen = Screen()

screen.mainloop()
