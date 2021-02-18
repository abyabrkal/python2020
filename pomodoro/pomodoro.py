from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# *************** ROW0  **************
#title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
#title_label.config(padx=50)
title_label.grid(column=1, row=0)


# *************** ROW1  **************
#timer label
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# *************** ROW2  **************
#start button
start_button = Button(text="Start")
start_button.config(padx=10, pady=5)
start_button.grid(column=0, row=2)

#reset button
reset_button = Button(text="Reset")
reset_button.config(padx=10, pady=5)
reset_button.grid(column=2, row=2)


# *************** ROW3  **************
#4Tick label
tick_label = Label(text="✔", fg=GREEN, bg=YELLOW)
tick_label.config(font=(FONT_NAME, 28))
tick_label.config(padx=50)
tick_label.grid(column=1, row=3)





window.mainloop()