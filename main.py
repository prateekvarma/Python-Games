from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which colored turtle do you think is going to win? Enter a "
                                                          "color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-80 + (index * 30))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"Your turtle colored {user_bet} won!")
            else:
                print(f"Sorry, your turtle colored {user_bet} lost")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()