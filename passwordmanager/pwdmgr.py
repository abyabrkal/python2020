from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)




canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="passwordmanager/logo.png")
canvas.create_image(150, 150, image=lock_img)
canvas.config()
canvas.grid(column=1, row=1)




window.mainloop()