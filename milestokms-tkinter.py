from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=300)


def button_clicked():
    miles = input.get()
    if miles.isnumeric():
      kms = int(miles) * 1.60934
    else:
      kms = 0
      input.config(text="0")
    my_label4.config(text=kms)


# ******* ROW 0 ****************

# Label - Heading
my_label1 = Label(text="Miles to Kms Convertor")
my_label1.config(font=("Arial", 24, "bold"))
my_label1.grid(column=1, row=0)
my_label1.config(padx=10, pady=10)

# ******* ROW 1 ****************

# Entry - Miles entry
input = Entry(width=10)
input.grid(column=1, row=1)

# Label - text
my_label2 = Label(text="miles")
my_label2.grid(column=2, row=1)


# ******* ROW 2 ****************


# Label - text
my_label3 = Label(text="is equal to")
my_label3.grid(column=0, row=2)

# Label - Converted kms value
my_label4 = Label(text="")
my_label4.config(font=("Arial", 18, "bold"))
my_label4.grid(column=1, row=2)

# Label - text
my_label5 = Label(text="kms")
my_label5.grid(column=2, row=2)

# ******* ROW 3 ****************

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)



window.mainloop()