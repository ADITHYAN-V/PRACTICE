from turtle import Turtle, Screen

t = Turtle()
t.shape("classic")
t.color("green", 'blue')
n = int(input("Enter the amount of sides up-to you want to draw: "))
x = int(input("Enter the length of the side :"))
for i in range(n):
    sides = i + 1
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    if sides >= 3:
        ext_angle = 360 / sides
        for j in range(sides):
            t.fd(x)
            t.left(ext_angle)
            if t.pos() == (0.00, 0.00):
                break

screen = Screen()
screen.exitonclick()
