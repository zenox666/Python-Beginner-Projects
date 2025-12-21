import turtle as t
import colorgram
import random

colors = colorgram.extract('image.jpg', 30)
rgb_codes = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_codes.append(new_color)

t.colormode(255)

bob = t.Turtle()
screen = t.Screen()
bob.speed('fastest')


bob.setheading(225)
bob.hideturtle()
bob.penup()
bob.forward(300)
bob.setheading(0)

dots = 100
for i in range(1,dots+1):
    bob.dot(18,random.choice(rgb_codes))
    bob.penup()
    bob.forward(50)
    if i % 10==0:
        bob.penup()
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)


screen.exitonclick()
