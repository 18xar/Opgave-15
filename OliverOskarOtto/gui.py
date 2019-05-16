import PySimpleGUI as sg

layout = [[sg.Text("Point A:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Text("Point B:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Text("Point C:")],
    [sg.Text("x = "), sg.InputText(0), sg.Text("y = "), sg.InputText(0)],
    [sg.Submit()]
]

done = sg.Window("Beregn punkter").Layout(layout)
button, values = done.Read()

