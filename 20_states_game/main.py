import turtle
import pandas

# set up turtle
screen = turtle.Screen()
screen.title('United States Game')
turtle.shape("square")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# create a new turtle to write text
turtle_write = turtle.Turtle()
turtle_write.penup()
turtle_write.hideturtle()


# set up data
df = pandas.read_csv('50_states.csv')
all_states = df.state.tolist()
correct_answers = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State ({len(correct_answers)}/50)", prompt="Guess state's name!").title()

    if answer_state is not None:
        if answer_state in all_states:
            answer_df = df[df.state == answer_state]
            turtle_write.goto(answer_df.x.values[0], answer_df.y.values[0])
            turtle_write.write(answer_state, move=False, align='center', font=('Arial', 6, 'normal'))
            correct_answers.append(answer_state)
            all_states.remove(answer_state)

    if len(correct_answers) >= 50:
        game_is_on = False

turtle.mainloop()
