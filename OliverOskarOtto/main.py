import PySimpleGUI as sg

layout = [[sg.Text("Point A:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Text("Point B:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Text("Point C:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Submit()]
]

done = sg.Window("Put in coordinates").Layout(layout)
button, values = done.Read()

Ax = float(values[0])
Ay = float(values[1])
Bx = float(values[2])
By = float(values[3])
Cx = float(values[4])
Cy = float(values[5])