#import arcade
from tkinter import *
from NinaMohammadNichi import drawPrimitives as dp

root = Tk()

theLabel = Label(root,text="Første vindue")
theLabel.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
instruks = Text(root, height=2, width=2)
instruks.pack()
instruks.insert('5.0', 'Indtast')

hLabel = Label(root, text="Højde")
hLabel.pack()

height = Entry(root)
height.pack()

length = Entry(root)
length.pack()

width = Entry(root)
width.pack()

button1 = Button(root, text="Button 1", command=lambda: dp.drawBox(int(height), int(length), int(width)))
button1.pack()

mainloop()