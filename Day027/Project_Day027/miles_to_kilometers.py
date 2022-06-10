from tkinter import *
FONT = ('Arial', 14)
# Window Setup
window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# GUI Labels
mile = Label(text='Miles', font=FONT)
mile.grid(column=3, row=1)
is_equal_to = Label(text='is equal to', font=FONT)
is_equal_to.grid(column=1, row=2)
km = Label(text='Km', font=FONT)
km.grid(column=3, row=2)
result = Label(text=0, font=FONT)
result.grid(column=2, row=2)


# Function to calculate
def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.60934, 2)
    result.config(text=kilometers)
    print(miles)


# Input
miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)

# Button
calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=2, row=3)


window.mainloop()