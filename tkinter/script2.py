from tkinter import *

window = Tk()


def convertKG():
  grams = float(kg.get())*1000
  pounds = float(kg.get())*2.20462
  ounces = float(kg.get())*35.274

  t_grams.insert(END, grams)
  t_pounds.insert(END, pounds)
  t_ounces.insert(END, ounces)


l = Label(window, text="Kg")
l.grid(row=0, column=0)

kg = StringVar()
e1 = Entry(window, textvariable=kg)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convertKG)
b1.grid(row=0, column=2)


t_grams = Text(window, height=1, width=20)
t_grams.grid(row=1, column=0)

t_pounds = Text(window, height=1, width=20)
t_pounds.grid(row=1, column=1)

t_ounces = Text(window, height=1, width=20)
t_ounces.grid(row=1, column=2)


window.mainloop()