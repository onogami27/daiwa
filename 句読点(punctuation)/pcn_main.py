import PySimpleGUI as sg
from transformers import pipeline
import os

#GUIテーマの設定
sg.theme("Black")

#オプション設定
sg.set_options(
    use_ttk_buttons=True,
    dpi_awareness=True
)

#ページカウント初期化
page_count = 0

#レイアウト
lay_1 = [
    [sg.Frame("処理ファイル読み込み",layout=[
        [sg.InputText(key = "file_in",size=(20,1)),sg.FileBrowse("選択")],
        [sg.Button("読み込み処理",key = "file_read")],
    ])]
]

lay_2 = [
    [sg.Frame("ファイル内容出力",layout =[
        [sg.Multiline(key="file_out",size=(50,10))],
        [sg.Text("文字数："),sg.InputText(key="let",size=(10,1)),sg.Button("前へ",key="back"),sg.Button("次へ",key="next"),
         sg.Text("count"),sg.InputText(default_text=page_count,size=(3,1),key="page_count",enable_events=True)],
    ])]
]
    
lay_3 = [
    [sg.Frame("処理後結果出力",layout=[
        [sg.Multiline(key="result_out",size=(50,10))],
        
    ])]
]
    





layout = [[sg.Column(lay_1,vertical_alignment="t"),sg.Column(lay_2)],lay_3]

#ウィンドウの設定
window = sg.Window("句読点処理",layout = layout)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    #読み込み処理ボタンを押した時の処理
    if event == "file_read":
        if value["file_in"] == "":
            sg.popup("ファイルを選択して下さい")
            continue
        else:
            try:
                file_data = open(r"{}".format(value["file_in"]),encoding="utf_8")
                data = file_data.read()
                print(data[0:100])
                window["file_out"].update(data)
                window["let"].update(len(data))
                file_data.close()
            except:
                pass
            
    #前へボタンを押した時の処理
    if event == "back":
        if page_count == 0:
            pass
        else:
            page_count -= 1
            
            try:
                
                window["file_out"].update(data[0:100])
                window["page_count"].update(page_count)
            except:
                
                pass
    #次へボタンを押した時の処理
    if event == "next":
        
        page_count +=1
        
        try:
            
            window["file_out"].update(data[101:200])
            window["page_count"].update(page_count)
        except:
            pass
    