import colorgram
from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
timmy = Turtle()
# colours = colorgram.extract('download.jpg',30)
# colour_group = []
# # print(colours)
# for j in colours:
#     r = j.rgb.r 
#     g = j.rgb.g
#     b = j.rgb.b
#     new_colour = (r, g, b)
#     colour_group.append(new_colour)

# print(colour_group)

colour_list = [(244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238)]
timmy.speed(3)
timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
def move():
    for i in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.forward(50)
    reset()

def reset():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
for i in range(10):
    move()

screen = Screen()
screen.exitonclick()