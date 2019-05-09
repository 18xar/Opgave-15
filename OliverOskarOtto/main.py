import PySimpleGUI as sg
import PointsToDistance

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

ax = float(values[0])
ay = float(values[1])
bx = float(values[2])
by = float(values[3])
cx = float(values[4])
cy = float(values[5])

PointsToDistance.PointsToDistance(ax, ay, bx, by, cx, cy)