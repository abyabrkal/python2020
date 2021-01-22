import turtle

screen = turtle.Screen()
screen.title("Guess Game - US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess Game - US States", prompt="Enter the state's name?")

#def get_mouse_click_coords(x, y):
#  print(x, y)

## prints out the x, y coordinates of a mouse click
#turtle.onscreenclick(get_mouse_click_coords)
#turtle.mainloop()
## This gives the data to consle and waits at console.


screen.exitonclick()