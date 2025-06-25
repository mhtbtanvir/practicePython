import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
map = "blank_states_img.gif"
screen.addshape(map)
turtle.shape(map)


# def get_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"you guesses {len(guessed_states)}/50 states So far!",
        prompt="Got another Name?").title()
    missing_states = [
        state for state in all_states if state not in guessed_states]
    # if answer_state == "Exit":
    #     # missing state names
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)

    missed_state_data = pandas.DataFrame(missing_states)
    missed_state_data.to_csv("missed_states.csv")
    break

    # # to get the missing states with the co ordinates
    # missed_state = data[~data.state.isin(guessed_states)]
    # missed_state.to_csv("missed_state.csv")
    # break

    # missing_states.to_csv("missing ststes.csv")

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        match = data[data.state == answer_state]
        x = int(match.x)
        y = int(match.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(f"{answer_state}")


screen.exitonclick()
