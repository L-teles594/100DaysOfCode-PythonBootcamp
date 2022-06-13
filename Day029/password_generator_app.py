from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    from random import choice
    from pyperclip import copy

    password_entry.delete(0, END)

    with open('ansi_table.txt') as file:
        ansi_list = file.read().split('\n')

    new_password = ''
    while len(new_password) < 30:
        new_password += choice(ansi_list)
    copy(new_password)
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    my_email = email_username_entry.get()
    my_website = website_entry.get()
    my_password = password_entry.get()
    if len(my_website) == 0 or len(my_password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty")
    else:
        message = f'These are the details entered:\nEmail: {my_email}\nPassword: {my_password}\n Is it ok to save?'
        is_ok = messagebox.askokcancel(title=f'{my_website}', message=message)
        if is_ok:
            with open('my_list.txt', 'a') as file:
                file.write(f'{my_website} | {my_email} | {my_password}\n')

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
screen = Tk()
screen.title('Password Manager')
screen.config(pady=20, padx=20)

# Image Canvas
lock_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels Setup
website = Label(text='Website:')
website.grid(column=0, row=1)
email_username = Label(text='Email/Username:')
email_username.grid(column=0, row=2)
password = Label(text='Password:')
password.grid(column=0, row=3)

# Entries Setup
website_entry = Entry(width=42)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry = Entry(width=42)
email_username_entry.insert(END, 'lucas@ficticius.com')
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

# Buttons Setup
generate_password = Button(text='Generate', command=generator)
generate_password.grid(column=2, row=3)
add_button = Button(text='Add', width=39, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()