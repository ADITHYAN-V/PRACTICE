from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("classic")
t.color("green", 'blue')
t.speed("fastest")
c = ["red", "blue", "cyan", "green", "black", "grey", "purple", "violet", "pink", "turquoise", "magenta", "orange",
     "darkblue",
     "aqua", "maroon", "white", "lightgreen", "lightblue", "brown", "darkgreen", "lime", "gold", "silver", "tomato",
     "chocolate", "plum", "indigo", "lavender", "crimson", "rosybrown", "bisque", "salmon", "greenyellow", "palegreen",
     "firebrick", "olive"]

radius = 100
increment = 5
angle = 0
while angle <= 360:
    t.pencolor(random.choice(c))
    t.circle(radius)
    t.seth(angle)
    angle += increment

screen = Screen()
screen.exitonclick()
