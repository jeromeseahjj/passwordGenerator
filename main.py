# ---------------------------- IMPORT ------------------------------- #
from tkinter import *
from tkinter import messagebox
from password import generate
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=data[website], 
                                message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) # Read the old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4) # Write everything to JSON
        else:
            data.update(new_data) # Update the existing dictionary

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) # Write everything to JSON
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

def generate_password():
    password = generate()
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website")
label_website.grid(row=1, column=0)
label_email = Label(text="Eamil/Username")
label_email.grid(row=2, column=0)
label_password = Label(text="password")
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=35)
entry_website.grid(row=1,column=1)
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2,column=1, columnspan=2)
entry_email.insert(0, 'email@gmail.com')
entry_password = Entry(width=21)
entry_password.grid(row=3,column=1)

# Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()