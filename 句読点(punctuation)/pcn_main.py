import PySimpleGUI as sg
from transformers import pipeline
import os

#モデルの読み込み
nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char")


#GUIテーマの設定
sg.theme("Black")

#オプション設定
sg.set_options(
    use_ttk_buttons=True,
    dpi_awareness=True,
    
    
)

#ユーザーセッティング
Setings = sg.UserSettings(filename="setings_file",path=os.path.split(__file__)[0])
Setings.load()


#ページカウント初期化
page_count = 0

#レイアウト
lay_1 = [
    [sg.Frame("処理ファイル読み込み",layout=[
        [sg.InputText(key = "file_in",size=(20,1)),sg.FileBrowse("選択")],
        [sg.Button("読み込み処理",key = "file_read")],

    ])],
    [sg.Frame("処理開始",visible=False,key="frame_start",pad=(30,50),element_justification="center",layout=[
         [sg.Button("開始",key="START",font=("meiryo",30))],
     ])]
]

lay_2 = [
    [sg.Frame("ファイル内容出力",layout =[
        [sg.Text("",key="page_value"),sg.InputText(key="now_count",size=(5,1),background_color="#696969"),sg.Text("※500文字以下にして下さい",text_color="red",key="warning",visible=False)],
        [sg.Multiline(key="file_out",size=(50,10))],
        [sg.Text("文字総数："),sg.InputText(key="let",size=(10,1)),sg.Button(image_source="back.png",key="back",mouseover_colors="white",button_color="black"),sg.Button(image_source="next.png",key="next",mouseover_colors="white",button_color="black"),
         sg.Text("ページNo."),sg.InputText(default_text=page_count,size=(3,1),key="page_count",enable_events=True)],
    ]),],
    
]
    
lay_3 = [
    [sg.Frame("処理後結果出力",layout=[
        [sg.Multiline(key="result_out",size=(50,10))],
        
    ])]
]

lay_4 = [
    [sg.Text("スコア許容度"),sg.InputText(default_text="0.7",key="threshold",size=(4,1))],
    [sg.Text("0～0.99までの数値を記入\n数値が上がるにつれ句読点挿入の\n判定が厳しくなります",text_color="#00ff00")],
    [sg.Button("agv",key="agv")],
]
    


layout = [[sg.Column(lay_1,vertical_alignment="t"),sg.Column(lay_2)],[sg.Column(lay_3),sg.Column(lay_4)]]

#ウィンドウの設定
window = sg.Window("句読点処理",layout = layout)



#句読点メイン処理関数
def main(value,threshold):
    def insert_char_to_sentence(i, char, sentence): # sentenceのi文字目にcharを挿入する
        l = list(sentence)
        l.insert(i, char)
        text = "".join(l)
        return text

    original_sentence = f"{value}" # 省略
    thresh = threshold # このスコア以上の場合、句読点を挿入する
    i = 0
    punctuations = ["、", "。", "?"]
    chars_after_mask = 100
    corrected_sentence = original_sentence
    while i < len(corrected_sentence):
        i += 1
        if corrected_sentence[i-1] in punctuations: continue # 句読点が連続してくることはない
        masked_text = insert_char_to_sentence(i, nlp.tokenizer.mask_token, corrected_sentence)
        
        pre_context, post_context = masked_text.split("。")[-1].split(nlp.tokenizer.mask_token)
        res = nlp(f"{pre_context}{nlp.tokenizer.mask_token}{post_context[:chars_after_mask]}")[0] # scoreが一番高い文
        if res["token_str"] not in punctuations: continue
        if res["score"] < thresh: continue

        punctuation = res["token_str"] if res["token_str"] != "?" else "。" # 今回は"？"は"。"として扱う
        corrected_sentence = insert_char_to_sentence(i, punctuation, corrected_sentence)
    
    return corrected_sentence





while True:
    event,value = window.read(timeout=0)
    
    if event == None:
        
        Setings.delete_file() #ユーザーセッティングファイルを消去
        break

    #入力文字数のカウント
    text_count = len(value["file_out"])
    if text_count > 500:#入力した文字が500を超えた時の処理
        
        window["now_count"].update(value = text_count,background_color="red",)
        window["warning"].update(visible=True)
        pass
    else:
        window["now_count"].update(text_count,background_color="#696969")
        window["warning"].update(visible=False)
    
    
    #読み込み処理ボタンを押した時の処理
    if event == "file_read":
        page_count = 0 #ページカウントリセット　誤動作防止の為
        
        if value["file_in"] == "":
            sg.popup("ファイルを選択して下さい")
            continue
        else:
            try:
                
                #処理開始ボタンを非表示にする
                window["frame_start"].update(visible=False)
                
                file_data = open(r"{}".format(value["file_in"]),encoding="utf_8")
                data = file_data.read()
                
                global data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,\
                    data_11,data_12,data_13,data_14,data_15,data_16,data_17,data_18,data_19,data_20
                
                Setings["data_0"] = data[0:500]
                Setings["data_1"] = data[500:1000]
                Setings["data_2"] = data[1000:1500]
                Setings["data_3"] = data[1500:2000]
                Setings["data_4"] = data[2000:2500]
                Setings["data_5"] = data[2500:3000]
                Setings["data_6"] = data[3000:3500]
                Setings["data_7"] = data[3500:4000]
                Setings["data_8"] = data[4000:4500]
                Setings["data_9"] = data[4500:5000]
                Setings["data_10"] = data[5000:5500]
                Setings["data_11"] = data[5500:6000]
                Setings["data_12"] = data[6000:6500]
                Setings["data_13"] = data[6500:7000]
                Setings["data_14"] = data[7000:7500]
                Setings["data_15"] = data[7500:8000]
                Setings["data_16"] = data[8000:8500]
                Setings["data_17"] = data[8500:9000]
                Setings["data_18"] = data[9000:9500]
                Setings["data_19"] = data[9500:10000]
                Setings["data_20"] = data[10000:10500]
                
                window["file_out"].update(Setings["data_0"])
                window["page_count"].update(page_count)
                window["page_value"].update("0～500文字を表示")
                window["let"].update(len(data))
                file_data.close()
                
                #処理開始ボタンを表示する
                window["frame_start"].update(visible=True)
                
                
            except:
                pass
    
    def judgment():
        if page_count == 0: 
            window["file_out"].update(Setings["data_0"])
            window["page_count"].update(page_count)
            window["page_value"].update("0～500文字を表示")
        elif page_count == 1:  
            window["file_out"].update(Setings["data_1"])
            window["page_count"].update(page_count)
            window["page_value"].update("500～1000文字を表示")
        elif page_count == 2:
            window["file_out"].update(Setings["data_2"])
            window["page_count"].update(page_count)
            window["page_value"].update("1000～1500文字を表示")
        elif page_count == 3:
            window["file_out"].update(Setings["data_3"])
            window["page_count"].update(page_count)
            window["page_value"].update("1500～2000文字を表示")
        elif page_count == 4:
            window["file_out"].update(Setings["data_4"])
            window["page_count"].update(page_count)
            window["page_value"].update("2000～2500文字を表示")
        elif page_count == 5:
            window["file_out"].update(Setings["data_5"])
            window["page_count"].update(page_count)
            window["page_value"].update("2500～3000文字を表示")
        elif page_count == 6:
            window["file_out"].update(Setings["data_6"])
            window["page_count"].update(page_count)
            window["page_value"].update("3000～3500文字を表示")
        elif page_count == 7:
            window["file_out"].update(Setings["data_7"])
            window["page_count"].update(page_count)
            window["page_value"].update("3500～4000文字を表示")
        elif page_count == 8:
            window["file_out"].update(Setings["data_8"])
            window["page_count"].update(page_count)
            window["page_value"].update("4000～4500文字を表示")
        elif page_count == 9:
            window["file_out"].update(Setings["data_9"])
            window["page_count"].update(page_count)
            window["page_value"].update("4500～5000文字を表示")
        elif page_count == 10:
            window["file_out"].update(Setings["data_10"])
            window["page_count"].update(page_count)
            window["page_value"].update("5000～5500文字を表示")
        elif page_count == 11:
            window["file_out"].update(Setings["data_11"])
            window["page_count"].update(page_count)
            window["page_value"].update("5500～6000文字を表示")
        elif page_count == 12:
            window["file_out"].update(Setings["data_12"])
            window["page_count"].update(page_count)
            window["page_value"].update("6000～6500文字を表示")
        elif page_count == 13:
            window["file_out"].update(Setings["data_13"])
            window["page_count"].update(page_count)
            window["page_value"].update("6500～7000文字を表示")
        elif page_count == 14:
            window["file_out"].update(Setings["data_14"])
            window["page_count"].update(page_count)
            window["page_value"].update("7000～7500文字を表示")
        elif page_count == 15:
            window["file_out"].update(Setings["data_15"])
            window["page_count"].update(page_count)
            window["page_value"].update("7500～8000文字を表示")
        elif page_count == 16:
            window["file_out"].update(Setings["data_16"])
            window["page_count"].update(page_count)
            window["page_value"].update("8000～8500文字を表示")
        elif page_count == 17:
            window["file_out"].update(Setings["data_17"])
            window["page_count"].update(page_count)
            window["page_value"].update("8500～9000文字を表示")
        elif page_count == 18:
            window["file_out"].update(Setings["data_18"])
            window["page_count"].update(page_count)
            window["page_value"].update("9000～9500文字を表示")
        elif page_count == 19:
            window["file_out"].update(Setings["data_19"])
            window["page_count"].update(page_count)
            window["page_value"].update("9500～10000文字を表示")
        elif page_count == 20:
            window["file_out"].update(Setings["data_20"])
            window["page_count"].update(page_count)
            window["page_value"].update("10000～10500文字を表示")
    
    #ユーザーセッティングへテキスト内容を保存する        
    def save_text():
        if page_count == 0:
            Setings["data_0"] = value["file_out"]
        if page_count == 1:
            Setings["data_1"] = value["file_out"] 
        if page_count == 2:
            Setings["data_2"] = value["file_out"]    
        if page_count == 3:
            Setings["data_3"] = value["file_out"]  
        if page_count == 4:
            Setings["data_4"] = value["file_out"]
        if page_count == 5:
            Setings["data_5"] = value["file_out"]
        if page_count == 6:
            Setings["data_6"] = value["file_out"]
        if page_count == 7:
            Setings["data_7"] = value["file_out"]
        if page_count == 8:
            Setings["data_8"] = value["file_out"]
        if page_count == 9:
            Setings["data_9"] = value["file_out"]
        if page_count == 10:
            Setings["data_10"] = value["file_out"]
        if page_count == 11:
            Setings["data_11"] = value["file_out"]
        if page_count == 12:
            Setings["data_12"] = value["file_out"]
        if page_count == 13:
            Setings["data_13"] = value["file_out"]
        if page_count == 14:
            Setings["data_14"] = value["file_out"]
        if page_count == 15:
            Setings["data_15"] = value["file_out"]
        if page_count == 16:
            Setings["data_16"] = value["file_out"]
        if page_count == 17:
            Setings["data_17"] = value["file_out"]
        if page_count == 18:
            Setings["data_18"] = value["file_out"]
        if page_count == 19:
            Setings["data_19"] = value["file_out"]
        if page_count == 20:
            Setings["data_20"] = value["file_out"]
            
            
    
            
    #前へボタンを押した時の処理
    if event == "back":
        
        save_text()
        
        if page_count == 0:
            pass
        else:
            page_count -= 1
            window["now_count"].update(page_count)
            
            try:
                
                judgment()
                
        
            except:
                sg.popup("ファイルを読み込んで下さい")
                pass
            
    #次へボタンを押した時の処理
    if event == "next":
        
        save_text()
        
        if page_count == 20:
            pass
        else:
            page_count +=1
            window["now_count"].update(page_count)
        
        try:
            
            judgment()
            
            
        except:
            sg.popup("ファイルを読み込んで下さい")
            pass
    
    #句得点処理
    if event == "START":
        
        save_text()
        
        if value["threshold"] == "":
            sg.popup("スコア許容度を入力して下さい")
            continue
        else:
            #句読点処理
            OUT_TEXT = main(value=Setings["data_0"],threshold=float(value["threshold"]))
            window["result_out"].update(OUT_TEXT)
        
        
        
        
    #TEST
    if event == "agv":
        
        save_text()
        
        S = Setings.get_dict()
        out_values = ""
        for i in S.values():
            out_values += i + "\n"
            
        window["result_out"].update(out_values)
        
    





Setings.delete_file() #ユーザーセッティングファイルを消去