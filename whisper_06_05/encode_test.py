import PySimpleGUI as sg



lay = [
    [sg.Multiline(key="out",size=(52,10))],
    [sg.Button("start",key="start")],
    ]

window = sg.Window("",layout=lay)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event =="start":
        hh = open("KMSI.txt","r",encoding="utf-8")
        window["out"].update(hh.read())
        