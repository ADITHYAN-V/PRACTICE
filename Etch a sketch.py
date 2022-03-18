from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.setheading(90)
t.speed("fastest")

def move_fd():
    t.fd(20)
def move_back():
    t.bk(20)
def move_left():
    t.left(90)
    t.fd(20)
    t.right(90)
def move_right():
    t.right(90)
    t.fd(20)
    t.left(90)
def rotateleft():
    t.left(20)
def rotateright():
    t.right(20)
screen.listen()
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=move_fd, key="w")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=rotateright, key="l")
screen.onkey(fun=rotateleft, key="j")
screen.exitonclick()

