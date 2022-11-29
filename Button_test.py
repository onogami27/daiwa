import PySimpleGUI as sg
import datetime


sg.set_options(use_ttk_buttons=True)

sg.theme("SystemDefaultForReal")

layout = [
    [sg.Button("①PUSH",key="B_PUSH_1",button_type=9)],
    [sg.Button("②PUSH",key="B_PUSH_2",button_type=9)],
    [sg.InputText("",key="out",size=(6,1),readonly=True)],
]

window = sg.Window("",layout)

while True:
    event,value = window.read(timeout=0)
    
    if event == sg.WINDOW_CLOSED:
        break
    
    
        
    
    if event == "B_PUSH_1":
        window["out"].Update("True")
        
    elif event == "B_PUSH_2":
        window["out"].Update("True")
            
    else:
        window["out"].Update("False")
        
    if value["out"] == "True":
        print("GGG")
    
    
