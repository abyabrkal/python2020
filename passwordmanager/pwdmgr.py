from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# *************** ROW0  **************

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="passwordmanager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# *************** ROW1  **************
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

# *************** ROW2  **************
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "superman@krypton.com")

# *************** ROW3  **************
pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

pass_button = Button(text="Generate Password")
pass_button.grid(column=2, row=3)

# *************** ROW4  **************
add_button = Button(text="Add Entry", width=36)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()