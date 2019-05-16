#import arcade
from tkinter import *
from NinaMohammadNichi import drawPrimitives as dp

# theLabel = Label(root,text="Første vindue")
#theLabel.pack()

height = 100.0
length = 100.0
width = 100.0
def plzWork ():
    print("Plz?")
root = Tk()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(root, text="Button 1", command=lambda: dp.drawBox(height, length, width))
button1.pack()

root.mainloop()