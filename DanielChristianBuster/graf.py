import PySimpleGUI as sg

def graf():
    layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-105,-105), graph_top_right=(105,105), background_color='white', key='graph', tooltip='This is a cool graph!')]]

    window = sg.Window('Graph of Sine Function', grab_anywhere=True).Layout(layout).Finalize()

    graph = window.FindElement('graph')

    graph.DrawLine((-100,0), (100,0))
    graph.DrawLine((0,-100), (0,100))

    for x in range(-100, 101, 20):
        graph.DrawLine((x,-3), (x,3))
        if x != 0:
            graph.DrawText( x, (x,-10), color='green')

    for y in range(-100, 101, 20):
        graph.DrawLine((-3,y), (3,y))
        if y != 0:
            graph.DrawText( y, (-10,y), color='blue')

    event, values = window.Read()

    function = values[0]
    x = []
    for i in range(0,100):
        x.append()
    graph.DrawLine((-100,0), (100,0))