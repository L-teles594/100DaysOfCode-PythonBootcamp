from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label
my_tkinter = Label(text='I am a label', font=('Courier', 24, 'bold'))
my_tkinter.pack(side='top')


def click_button():
    string = my_input.get()
    my_tkinter.config(text=string)


# Button
my_button = Button(text='Click Me', command=click_button)
my_button.pack()

# Input
my_input = Entry(width=17)
my_input.insert(END, string='Type something here')
my_input.pack()

# Text
text = Text(width=30, height=5)
text.focus()
text.insert(END, 'Type some Text here...')
print(text.get('1.0', END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(width=5, from_=0, to=10, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check button
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkedbutton = Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used)
checkedbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radio1.pack()
radio2.pack()


# Listbox
def listbox_used():
    print()

listbox = Listbox(height=4)
fruits = ['Banana', 'Apple', 'Pear', 'Orange']

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


window.mainloop()