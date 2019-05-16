import PySimpleGUI as sg
import server
import client

def SetupWindow():
    layout = [
        [sg.InputText("Skriv dit navn her.")],
        [sg.Text("Hvis du tilslutter en chat-gruppe skal du skrive IP'en.")],
        [sg.InputText("Skriv ip'en her! Lad være tom, hvis du tilslutter.")],
        [sg.Text("Vil du hoste eller tilslutte?")],
        [sg.RButton("Host"), sg.RButton("Tilslut")]        
    ]

    window = sg.Window("Chat-opsætning").Layout(layout)

    button, values = window.Read()

    name = str(values[0])
    print("Dit navn/id er: " + name)
    
    returnList = [button]
    returnList.append(name)
    if button == "Tilslut":
        ip = str(values[1])
        returnList.append(ip)
        print("Den målrettede ip er: " + ip)
        window.Close()
    if button == "Host":
        server.startServer(name) 
        
    return returnList


def ChatWindow():
    layout = [
        [sg.Text("Chat:")],
        [sg.Text("Velkommen til chatrummet!")],
        [sg.Multiline("", size=(30, 5), key="__CHAT__")],
        [sg.Input(), sg.RButton("Send")]
    ]

    window = sg.Window("Chatvindue").Layout(layout)

    return window


def sendMessage(event, input, window, name, button):
    if event == "Send":
        message = "{}: {} \n".format(name, input[0])
        chatList.append(message)
        if button == "Tilslut":
            client.sendMessage(message)
        elif button == "Host":
            server.sendMessage(message)
        
        window.FindElement("__CHAT__").Update("".join(chatList))


server = server.Server()

returnList = SetupWindow()
chatWindow = ChatWindow()

chatList = []
while True:
    event, values = chatWindow.Read()
    server.loopServer()
    if event is None or event == "Exit":
        break
    if event == "Chat":
        sendMessage(event, values, chatWindow, returnList[1], returnList[0])
    if event == "Refresh":
        if returnList[0] == "Tilslut":
            # Refresh (få beskeder fra server og put dem ind i chatlist og opdater ui)
            chatList.append(client.receiveMessage())
        elif returnList[0] == "Host":
            chatList.append(server.receiveMessage)
        
        # Opdater UI
        chatWindow.FindElement("__CHAT__").Update("".join(chatList))
