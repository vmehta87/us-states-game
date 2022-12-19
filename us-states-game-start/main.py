import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

count = 0
confirmed_answers = []
game_on = True
while game_on:
    answer_state = screen.textinput(title='Guess the State', prompt='Whats another state name?').title()

    data = pandas.read_csv('50_states.csv')
    state_list = data.state.to_list()
    if answer_state in state_list and answer_state not in confirmed_answers:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        count += 1
        confirmed_answers.append(answer_state)
        t2 = turtle.Turtle()
        t2.hideturtle()
        t2.penup()
        t2.goto(250, 250)
        t2.clear()
        t2.write(f'{count}/50')
# row = data[data.state == answer_state]
# turtle.write(data.state)


screen.mainloop()