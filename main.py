import turtle as t
import random

don = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    colour = (r, b, g)
    return colour


don.speed('fastest')

def draw_gap(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        don.color(random_colour())
        don.circle(100)
        don.setheading(don.heading() + size_of_gap)

draw_gap(3)

screen = t.Screen()
screen.exitonclick()