import colorgram,random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
t = Turtle()
t.shape("classic")
t.color("green", 'blue')
t.speed("fastest")


color_list = colorgram.extract("hirst.jpeg", 2 ** 32)
color_palette = []
for i in range(len(color_list)):
    rgb = color_list[i]
    color = rgb.rgb
    color1 = (color[0], color[1], color[2])
    color_palette.append(color1)
color_palette = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163), (3, 111, 115), (87, 51, 49), (62, 59, 77), (35, 37, 36)]

t.penup()
t.setheading(310)
t.fd(450)
t.setheading(0)
t.pendown()

for j in range(10):
    t.penup()
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.fd(500)
    t.setheading(0)
    t.pendown()
    for i in range(10):
        t.pencolor(random.choice(color_palette))
        t.dot(20)
        t.penup()
        t.fd(50)





screen.exitonclick()





