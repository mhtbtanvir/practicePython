# import turtle


# def draw_attractive_design3():
#     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#     pen = turtle.Turtle()
#     pen.speed(90000000000)
#     turtle.bgcolor("black")
#     pen.pensize(4)

#     for index in range(5):
#         pen.color(colors[index % 6])

#         for i in range(35):

#             pen.forward(100)
#             pen.left(59)
#             pen.forward(50)
#             pen.left(91)
#             pen.forward(50)
#             pen.left(59)
#             pen.forward(100)
#             pen.right(121)

#     pen.hideturtle()


# draw_attractive_design3()

# turtle.done()
import prettytable
from prettytable import PrettyTable
table = PrettyTable()  # constructor of the class/blueprint
table.add_column("name", ["Alice", "Bob", "Charlie"])
table.add_column("age", [24, 30, 22])
table.add_column("city", ["New York", "Los Angeles", "Chicago"])
table.align = "l"  # left align the text in the tab le
table.valign = "b"
table.title = "User Information"  # set the title of the table
print(table)
