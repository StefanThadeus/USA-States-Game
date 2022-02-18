import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A. States Game")

# fit window size to the map image
screen.setup(width=725, height=491)

# add image in the window
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# make turtle to write state names
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# import the Comma Separated Values data file using the pandas library
data = pandas.read_csv("50_states.csv")

answered_correctly = 0
guessed_list = []
while answered_correctly < 50:

    answer_state = screen.textinput(title=f"{answered_correctly}/50 States Correct",
                                    prompt="What's another state name?")

    answer_state = answer_state.strip()
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state not in guessed_list:
        for state in data.state:
            if answer_state == state:
                answered_correctly += 1
                state_row = data[data["state"] == state]
                state_x_coord = int(state_row.x)
                state_y_coord = int(state_row.y)

                writer.goto(state_x_coord, state_y_coord)
                writer.write(state, move=False, align="center", font=("Arial", 8, "normal"))
                guessed_list.append(state)

# save the un-guessed states in a csv file for the player to learn
not_guessed = []

for state in data.state:
    if state not in guessed_list:
        not_guessed.append(state)

learn_data_dict = {"State": not_guessed}

dataframe = pandas.DataFrame(learn_data_dict)
dataframe.to_csv("states_to_learn.csv")
