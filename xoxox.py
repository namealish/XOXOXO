from tkinter import *
import random, time

root = Tk()
label = Label(width=20, text="xoxoxo", font=('Arial', 20, 'bold'))

buttons = [Button(width=5, height=2, font=('Arial', 20, 'bold'), bg="green") for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
buttons[0].grid(row=1, column=0)
buttons[1].grid(row=1, column=1)
buttons[1].grid(row=1, column=2)

root.mainloop()

