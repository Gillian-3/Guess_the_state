import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
# THIS CODE IS USED FOR TAKING COORDINATES OF EACH STATES
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")
states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="whats another state name").title()
    if answer_state=="Exit":
        result_list=[item for item in states if item not in guessed_states]
        result_dict={
            "Missed States":result_list
        }
        df=pd.DataFrame(result_dict)
        df.to_csv("missed_states.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state = data[data.state == answer_state]
        t.goto(int(current_state.x),int(current_state.y))
        t.write(answer_state)


screen.exitonclick()