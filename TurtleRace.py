from turtle import Turtle, Screen
import random

t1, t2, t3, t4, t5, t6 = [Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"),
                          Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle")]
screen = Screen()
screen.setup(width=500, height=400)
colour_palette = ['indigo', 'blue', 'green', 'yellow', 'orange', 'red']
x1, x2, x3, x4, x5, x6, = colour_palette
t1.shape("arrow")
t1.penup()
t1.goto(x=-230, y=-100)
t1.pendown()
t1.goto(x=-230, y=150)
t1.penup()
t1.goto(x=229, y=-100)
t1.pendown()
t1.goto(x=229, y=150)
t1.shape("turtle")
t1.penup()

t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()
t6.penup()

t1.color(x1)
t2.color(x2)
t3.color(x3)
t4.color(x4)
t5.color(x5)
t6.color(x6)

x = True
while x:
    t1.goto(x=-230, y=50)
    t2.goto(x=-230, y=100)
    t3.goto(x=-230, y=150)
    t4.goto(x=-230, y=0)
    t5.goto(x=-230, y=-50)
    t6.goto(x=-230, y=-100)

    turtle_list = [t1, t2, t3, t4, t5, t6]

    is_race_on = False

    user_bet = screen.textinput(title="Make your prediction",
                                prompt="Which turtle would win the race?\nEnter a colour :")

    if user_bet:
        is_race_on = True

    while is_race_on:
        for i in turtle_list:
            rand_distance = random.randint(0, 10)
            i.forward(rand_distance)
            if i.xcor() > 229:
                if i.pencolor() == user_bet:
                    x = screen.textinput(title="YOU WIN!", prompt="Wanna play again?(y/n)")
                    print("USER WINS")
                else:
                    x = screen.textinput(title="YOU LOST!", prompt=f"{i.pencolor().capitalize()} coloured turtle won\n"
                                                                    "Wanna play again(y/n)")
                    print("USER LOST")

                is_race_on = False
                break
    if x.lower() == "y":
        x = True
    else:
        x = False
