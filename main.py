import turtle
import pandas

correct_guesses = 0
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
###using Pandas to convert dataframe State column to a list
state_list = data["state"].to_list()
remaining_states = data["state"].to_list()
#creating a list of XY coordinates, at the same index level of the states.
xylist = list(zip(data.x, data.y))
#print(coords)
guessed_states = []


#Create list to hold all text positions of the states.
state_text_positions = []

#print(state_dict)

def place_state(state_name, xpos, ypos):
    show_text = turtle.Turtle()
    show_text.hideturtle()
    show_text.penup()
    show_text.setpos(text_x, text_y)
    show_text.write(f"{answer_state}", True, align="left", font=('Arial', 10, 'bold'))

    #state_text_positions.append()


while correct_guesses < 50:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="Name a State!").title()
    if answer_state == "Exit":
        state_df = pandas.DataFrame(data=remaining_states)
        state_df.to_csv('missed_states.csv')
        break
    if answer_state in state_dict.values():
        guessed_states.append(answer_state)
        for state in state_list:
            if state == answer_state:

                correct_guesses += 1
                xy_index = state_list.index(state)
                print(xy_index)
                text_x = xylist[xy_index][0]
                text_y = xylist[xy_index][1]
                place_state(answer_state, text_y, text_y)
                remaining_states.remove(answer_state)
                print(len(state_list))
                print(len(remaining_states))



# show_text = turtle.Turtle()
# show_text.hideturtle()
# show_text.penup()
# show_text.setpos(text_x, text_y)
# show_text.write(f"{answer_state}", True, align="left", font=('Courier', 10, 'bold'))
# if answer_state in state_dict.values():



###Works - but probably won't use###
#row_index = data.index.get_loc(data[data["state"] == answer_state].index[0])


