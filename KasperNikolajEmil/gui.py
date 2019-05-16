from behindthescenes import *


def choice():
    layout = [
        [sg.Text("Vælg om du vil se hvilke opgaver du mangler, eller om du vil se hvem der skal i skrivefængsel")],
        [sg.RButton("Egne"), sg.RButton("Alle")]
        ]
    
    window = sg.Window("Valg").Layout(layout)

    button, values = window.Read()

    return button


def prisonGUI(prisoners):
    layout = [
        [sg.Text("Personer der skal i skrivefængsel")],
        [sg.Multiline("", key="personer")],
        [sg.Exit()]
    ]

    window1 = sg.Window("Folk der skal i skrivefængsel").Layout(layout)
    
    tt = ""

    

    for x in range(len(prisoners)):
        tt = "{}{}\n".format(tt, prisoners[x])
    
    print(tt)
    window1.FindElement("personer").Update("{}".format(tt))
    button, values = window1.Read()


def createPopUp(manglende, tf):
    if tf == True:
        sg.Popup("Du har lavet alle dine opgaver og skal ikke i skrivefængsel")
    else:
        tt = ""
        layout = [
            [sg.Text("Du skal i skrivefængsel")],
            [sg.Text("Opgaver du mangler")],
            [sg.Multiline("", key="gg")],
            [sg.Exit()]
        ]
        window2 = sg.Window("Opgaver du mangler").Layout(layout)
        for x in manglende.items():
            kap = x[0]
            opgaver = x[1]
            # print(opgaver)
            if len(opgaver) <= 0:
                continue
            else:
                for o in range(len(opgaver)):
                    print(opgaver[o])
                    tt = "{}{}: {}\n".format(tt, kap, opgaver[o])
        # print("tt:", tt)
        window2.FindElement("gg").Update("{}".format(tt))    
        window2.Read()


choice = choice()
path = findPath()
if choice == "Egne":
    opgaveFiles = ReturnDict(path[0])
    kap = list(opgaveFiles.keys())
    listWithPeopleInPrison = PeopleInPrison(path[1] + "/Mirsad Kadribasic - ZZMatInfoMappe/Oversigt18RPLUS.xlsx")
    ownFiles = getOwnFiles(path[1], kap)
    manglende, x, m = compare(opgaveFiles, ownFiles)
    createPopUp(manglende, x)
elif choice == "Alle":
    listtemp = PeopleInPrison(path[1] + "/Mirsad Kadribasic - ZZMatInfoMappe/Oversigt18RPLUS.xlsx")
    # print(listtemp)
    prisonGUI(listtemp)