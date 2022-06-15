from tkinter import *

window=Tk()

def convert():
    kg_val = float(kg_value.get())
    grams_text = kg_val * 1000
    pounds_text = kg_val * 2.20462
    ounces_text = kg_val * 35.274

    grams.insert(END,grams_text)
    pounds.insert(END, pounds_text)
    ounces.insert(END, ounces_text)

kg=Label(window,text="kg")
kg.grid(row=0,column=0)

kg_value = StringVar()
e1 = Entry(window, textvariable=kg_value)
e1.grid(row=0,column=1)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0,column=2)

grams=Text(window,height=1,width=20)
grams.grid(row=1,column=0)

pounds=Text(window, height=1,width=20)
pounds.grid(row=1,column=1)

ounces=Text(window, height=1,width=20)
ounces.grid(row=1, column=2)






window.mainloop()