from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")
MOVE_DISTANCE = 5
TURN_ANGLE = 5
DELAY = 30

tim.forward_move = False
tim.backward_move = False
tim.turn_left_move = False
tim.turn_right_move = False


def start_forward():
    tim.forward_move = True
def stop_forward():
    tim.forward_move = False
def start_backward():
    tim.backward_move = True
def stop_backward():
    tim.backward_move = False
def start_left():
    tim.turn_left_move = True
def stop_left():
    tim.turn_left_move = False
def start_right():
    tim.turn_right_move = True
def stop_right():
    tim.turn_right_move = False
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def update():
    if tim.forward_move:
        tim.forward(MOVE_DISTANCE)
    if tim.backward_move:
        tim.backward(MOVE_DISTANCE)
    if tim.turn_left_move:
        tim.left(TURN_ANGLE)
    if tim.turn_right_move:
        tim.right(TURN_ANGLE)
    screen.ontimer(update, DELAY)


screen.listen()
screen.onkeypress(start_forward, "w")
screen.onkeyrelease(stop_forward, "w")
screen.onkeypress(start_backward, "s")
screen.onkeyrelease(stop_backward, "s")
screen.onkeypress(start_left, "a")
screen.onkeyrelease(stop_left, "a")
screen.onkeypress(start_right, "d")
screen.onkeyrelease(stop_right, "d")
screen.onkey(clear, "c")

update()
screen.exitonclick()
