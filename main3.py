from turtle import Turtle, Screen
import random

screen = Screen()

# def forward():
#     timmy.forward(10)
# def backward():
#     timmy.backward(10)
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
# def right():
#     timmy.right(10)
# def left():
#     timmy.left(10)

# screen.listen()
# screen.onkey(forward, "w")
# screen.onkey(backward, "x")
# screen.onkey(clear, "c")
# screen.onkey(right, "d")
# screen.onkey(left, "a")

race_on = False
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make a Bet", prompt  = "which turtle would win the race? Enter a colour: ")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
nicks = ["tilk", "meow", "hind","look", "cute", "verb", "head"]
# timmy = Turtle(shape= 'turtle')
# timmy.penup()
# timmy.goto(x= -240, y=80)
x = -240
y = -180
list = []
for i in range(7):
    no = i-1
    name = nicks[no]
    colour = color[no]
    y += 50
    name = Turtle(shape= 'turtle')
    name.penup()
    name.goto(x,y)
    name.color(colour)
    list.append(name)

if user_bet:
    race_on = True
while race_on:
    
    for t in list:
        if t.xcor()> 230:
            race_on = False
            winner = t.pencolor()
            winner = winner.title()
            if t.pencolor() == user_bet:
                print(f"You guessed right. {winner} turtle got to the finish line first")
            else:
                print(f"You guessed wrong. {winner} turtle got to the finish line first")
        distance = random.randint(0,15)
        t.forward(distance)
       
        










screen.exitonclick()

