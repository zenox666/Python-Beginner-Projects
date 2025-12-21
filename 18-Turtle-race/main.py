from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput("Make a bet","Who's gonna win the race? Enter a color:")

colors = ["red","orange","yellow","green","blue","purple"]
y_pos = -100
turtles = []
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_pos)
    y_pos += 40
    turtles.append(new_turtle)

if bet:
    is_race_on = True

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.speed("fastest")
finish_line.goto(210, 200)
finish_line.left(360)
finish_line.pendown()
finish_line.goto(210, -200)
finish_line_coord = 190

display_winner = Turtle()
display_winner.hideturtle()
display_winner.penup()
display_winner.speed("fastest")

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > finish_line_coord:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == bet:
                display_winner.write(arg=f"You've have Won!, The {winner} turtle is the winner!", align="center")
            else:
                display_winner.write(arg=f"You've have Lost!, The {winner} turtle is the winner!",align="center")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()
