from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers 
  random.shuffle(password_list)

  password = ''.join(password_list)

  pyperclip.copy(password)
  pass_input.delete(0, END)
  pass_input.insert(0, password)


# ---------------------------- WEBSITE SEARCH ------------------------------- #
def find_password():
  search = web_input.get()
  try:
    with open("./passwordmanager/data.json", "r") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="⚠️ Oops", message=f"File not found!!!")
  else:
    if search in data.keys():
      website = data[search]["email"]
      password = data[search]["password"]
      messagebox.showinfo(title=f"{search}", message=f"Email: {website}\nPassword: {password}")
    else:
      messagebox.showinfo(title="⚠️ Oops", message=f"No details for the {search} exists!!!")
  finally:
    web_input.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = web_input.get()
  email = user_input.get()
  password = pass_input.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="⚠️ Oops", message=f"Please make sure data is not left emtpy!!!")
  else:
    try:
      with open("./passwordmanager/data.json", "r") as fpass:
        # read old data if file present
        data = json.load(fpass)
    except FileNotFoundError:
      with open("./passwordmanager/data.json", "w") as fpass:
        # create file and write first data
        json.dump(new_data, fpass, indent=4)
    else:
      # if try was successful, read is successful
      # So, update old data with new data
      data.update(new_data)

      with open("./passwordmanager/data.json", "w") as fpass:
        # save updated data
        json.dump(data, fpass, indent=4)
    finally:
      # whatever be case, clear the form data
      web_input.delete(0, END)
      pass_input.delete(0, END)
  


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# *************** ROW0  **************

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./passwordmanager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# *************** ROW1  **************
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

web_button = Button(text="Search", width=13, command=find_password)
web_button.grid(column=2, row=1, columnspan=1)

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

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

# *************** ROW4  **************
add_button = Button(text="Add Entry", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()