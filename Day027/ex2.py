from tkinter import *

window = Tk()
window.title('Second exercise',)
window.minsize(width=500, height=300)

label = Label(text='That is a label!', font=('Courier', 24))
label.grid(column=0, row=0)

button = Button(text='Click me!')
button.grid(column=1, row=2)

button2 = Button(text='No! Click ME!')
button2.grid(column=3, row=1)

my_input = Entry(width=10)
my_input.grid(column=4, row=3)


window.mainloop()