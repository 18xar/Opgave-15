from tkinter import *

# theLabel = Label(root,text="Første vindue")
#theLabel.pack()

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Button 1", fg="red")
button1.pack(side=LEFT)


root.mainloop()

