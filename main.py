from tkinter import *


def button_clicked():
	new_text = float(input.get()) * 1.60934
	answer.config(text=new_text)


window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)

#Label
miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

isequal = Label(text="is equal to", font=("Arial", 12))
isequal.grid(column=0, row=1)

answer = Label(text="0", font=("Arial", 12))
answer.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()

