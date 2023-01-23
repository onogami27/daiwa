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
        [sg.Text("",key="page_value")],
        [sg.Multiline(key="file_out",size=(50,10))],
        [sg.Text("文字数："),sg.InputText(key="let",size=(10,1)),sg.Image(source="back.png",key="back",subsample=4,enable_events=True),sg.Image(source="next.png",key="next",subsample=4,enable_events=True),
         sg.Text("ページNo."),sg.InputText(default_text=page_count,size=(3,1),key="page_count",enable_events=True)],
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
                
                data_0 = data[0:500]
                data_1 = data[500:1000]
                data_2 = data[1000:1500]
                data_3 = data[1500:2000]
                data_4 = data[2000:2500]
                data_5 = data[2500:3000]
                data_6 = data[3000:3500]
                data_7 = data[3500:4000]
                data_8 = data[4000:4500]
                data_9 = data[4500:5000]
                data_10 = data[5000:5500]
                data_11 = data[5500:6000]
                data_12 = data[6000:6500]
                data_13 = data[6500:7000]
                data_14 = data[7000:7500]
                data_15 = data[7500:8000]
                data_16 = data[8000:8500]
                data_17 = data[8500:9000]
                data_18 = data[9000:9500]
                data_19 = data[9500:10000]
                data_20 = data[10000:10500]
                
                window["file_out"].update(data_0)
                window["page_count"].update(page_count)
                window["page_value"].update("0～500文字を表示")
                window["let"].update(len(data))
                file_data.close()
            except:
                pass
            
    def judgment():
        if page_count == 0:
            window["file_out"].update(data_0)
            window["page_count"].update(page_count)
            window["page_value"].update("0～500文字を表示")
        elif page_count == 1:
            window["file_out"].update(data_1)
            window["page_count"].update(page_count)
            window["page_value"].update("500～1000文字を表示")
        elif page_count == 2:
            window["file_out"].update(data_2)
            window["page_count"].update(page_count)
            window["page_value"].update("1000～1500文字を表示")
        elif page_count == 3:
            window["file_out"].update(data_3)
            window["page_count"].update(page_count)
            window["page_value"].update("1500～2000文字を表示")
        elif page_count == 4:
            window["file_out"].update(data_4)
            window["page_count"].update(page_count)
            window["page_value"].update("2000～2500文字を表示")
        elif page_count == 5:
            window["file_out"].update(data_5)
            window["page_count"].update(page_count)
            window["page_value"].update("2500～3000文字を表示")
        elif page_count == 6:
            window["file_out"].update(data_6)
            window["page_count"].update(page_count)
            window["page_value"].update("3000～3500文字を表示")
        elif page_count == 7:
            window["file_out"].update(data_7)
            window["page_count"].update(page_count)
            window["page_value"].update("3500～4000文字を表示")
        elif page_count == 8:
            window["file_out"].update(data_8)
            window["page_count"].update(page_count)
            window["page_value"].update("4000～4500文字を表示")
        elif page_count == 9:
            window["file_out"].update(data_9)
            window["page_count"].update(page_count)
            window["page_value"].update("4500～5000文字を表示")
        elif page_count == 10:
            window["file_out"].update(data_10)
            window["page_count"].update(page_count)
            window["page_value"].update("5000～5500文字を表示")
        elif page_count == 11:
            window["file_out"].update(data_11)
            window["page_count"].update(page_count)
            window["page_value"].update("5500～6000文字を表示")
        elif page_count == 12:
            window["file_out"].update(data_12)
            window["page_count"].update(page_count)
            window["page_value"].update("6000～6500文字を表示")
        elif page_count == 13:
            window["file_out"].update(data_13)
            window["page_count"].update(page_count)
            window["page_value"].update("6500～7000文字を表示")
        elif page_count == 14:
            window["file_out"].update(data_14)
            window["page_count"].update(page_count)
            window["page_value"].update("7000～7500文字を表示")
        elif page_count == 15:
            window["file_out"].update(data_15)
            window["page_count"].update(page_count)
            window["page_value"].update("7500～8000文字を表示")
        elif page_count == 16:
            window["file_out"].update(data_16)
            window["page_count"].update(page_count)
            window["page_value"].update("8000～8500文字を表示")
        elif page_count == 17:
            window["file_out"].update(data_17)
            window["page_count"].update(page_count)
            window["page_value"].update("8500～9000文字を表示")
        elif page_count == 18:
            window["file_out"].update(data_18)
            window["page_count"].update(page_count)
            window["page_value"].update("9000～9500文字を表示")
        elif page_count == 19:
            window["file_out"].update(data_19)
            window["page_count"].update(page_count)
            window["page_value"].update("9500～10000文字を表示")
        elif page_count == 20:
            window["file_out"].update(data_20)
            window["page_count"].update(page_count)
            window["page_value"].update("10000～10500文字を表示")
            
            
    #前へボタンを押した時の処理
    if event == "back":
        if page_count == 0:
            pass
        else:
            page_count -= 1
            
            try:
                exec("data_{0} = {1}".format(page_count,["{}".format(value['file_out'])]))
                judgment()
                
        
            except:
                sg.popup("ファイルを読み込んで下さい")
                pass
    #次へボタンを押した時の処理
    if event == "next":
        
        if page_count == 20:
            pass
        else:
            page_count +=1
        
        try:
            exec("data_{0} = {1}".format(page_count,["{}".format(value['file_out'])]))
            judgment()
            
            
            
        except:
            sg.popup("ファイルを読み込んで下さい")
            pass
    