import turtle
import pandas
# import warnings
# warnings.filterwarnings(action="ignore", category=DeprecationWarning)

data = pandas.read_csv('50_states.csv')


###SCREEN STUFF###
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(730,496)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

print(data)

state_dict = data["state"].to_dict()





print(state_dict)

answer_state = screen.textinput(title="Guess the State", prompt="Name a State!").title()

if answer_state in state_dict.values():
    print("Progress")
    for

###Works###
#row_index = data.index.get_loc(data[data["state"] == answer_state].index[0])






#screen.exitonclick()