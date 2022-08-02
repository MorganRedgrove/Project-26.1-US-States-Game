import turtle
import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")
image = ("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

name_pen = Turtle()
name_pen.hideturtle()
name_pen.penup()

state_count = 0

states_guessed = []
states_missed = []

while len(states_guessed) <50:
     answer_state = screen.textinput(title=f"Guess the State {state_count}/50", prompt="What's another state's name?").title()
     data = pandas.read_csv("50_states.csv")
     for state in data["state"]:
          if answer_state == state:
               state_count += 1
               x = float(data.x[data.state == state])
               #print(x)
               y = float(data.y[data.state == state])
               #print(y)
               name_pen.goto(x,y)
               name_pen.write(state)
               states_guessed.append(state)
               print(states_guessed)
          elif answer_state == "Exit":
               for state in data["state"]:
                    if state not in states_guessed:
                         states_missed.append(state)
               states_missed_df = pandas.DataFrame(states_missed)
               states_missed_df.to_csv("missed_states.csv")
               break



