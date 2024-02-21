import turtle
import pandas


data = pandas.read_csv('50_states.csv')


###SCREEN STUFF###
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(730,496)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#print(data)

state_dict = data["state"].to_dict()
state_list = data["state"].to_list()
xylist = list(zip(data.x, data.y))
#print(coords)


#print(state_dict)

def place_state(state_name, xpos, ypos):
    pass

answer_state = screen.textinput(title="Guess the State", prompt="Name a State!").title()
#
if answer_state in state_dict.values():
    for state in state_list:
        if state == answer_state:
            xy_index = state_list.index(state)
            print(xy_index)
            x = xylist[xy_index][0]
            y = xylist[xy_index][1]






# if answer_state in state_dict.values():



###Works - but probably won't use###
#row_index = data.index.get_loc(data[data["state"] == answer_state].index[0])






#screen.exitonclick()