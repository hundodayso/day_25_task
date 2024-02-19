import turtle


screen = turtle.Screen()
screen.title("US States Game")
screen.setup(730,496)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



answer_state = screen.textinput(title="Guess the State", prompt="Name a State!")



screen.exitonclick()