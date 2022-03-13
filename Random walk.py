from turtle import Turtle, Screen
import random
t = Turtle()
t.shape("classic")
t.color("green", 'blue')
t.pensize(10)
t.speed("fastest")
c = ["red","blue","cyan","green","black","grey","purple","violet","pink","turquoise","magenta","orange","darkblue",
     "aqua","maroon","white","lightgreen","lightblue","brown","darkgreen","lime","gold","silver","tomato",
     "chocolate","plum","indigo","lavender","crimson","rosybrown","bisque","salmon","greenyellow","palegreen",
     "firebrick","olive"]
#def rand_colour():
#    r = random.randint(0,255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    return (r,g,b)

while True:
    t.pencolor(random.choice(c))
    t.right(random.randint(0, 365))
    t.fd(random.randint(20,100))
    #m = random.randint(1,100000) #Can be used to relay the pen bck to origin randomly.
    #if m%12 == 0:
    #    t.home()




screen = Screen()
screen.exitonclick()
