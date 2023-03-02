import PySimpleGUI as sg
from transformers import pipeline
import os
import torch

#cuDNNライブラリが最適なアルゴリズムを自動的に選択
torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True


#モデル実行時の警告を消す
from transformers import logging
logging.set_verbosity_warning()
logging.set_verbosity_error()
#警告文を消す
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

#テキストを読み込む前に次へor前へボタンを押した時にエラーを出す為の信号
flug = False

#cudaの認識確認
#cudaの認識確認

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")
  
  
  


nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char-whole-word-masking",device=device,)

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
         sg.Text("ページNo."),sg.InputText(default_text=page_count,size=(5,1),key="page_count",enable_events=True)],
    ]),],
    
]
    
lay_3 = [
    [sg.Frame("処理後結果出力",layout=[
        [sg.Multiline(key="result_out",size=(50,10))],
        
    ])]
]

lay_4 = [
    [sg.Text("batch_size"),sg.InputText(default_text="1",key="batch_size",size=(6,1))],
    [sg.Text("スコア許容度"),sg.InputText(default_text="0.5",key="threshold",size=(4,1))],
    [sg.Text("0～0.99までの数値を記入\n数値が上がるにつれ句読点挿入の\n判定が厳しくなります",text_color="#00ff00")],
    [sg.Frame("結果をテキストファイルに保存",key="OUT",visible=False,layout=[
        [sg.Text("出力ファイル名"),sg.InputText(default_text="result",key="out_file_name",size=(20,1)),sg.Text(".txt")],
        [sg.Button("保存する",key="save",button_color=("white","#0000ff"))]
    ])],
    
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
    
    
    #総文字数カウント
    TT = Setings.get_dict()
    TT_count = 0
    for i in TT.values():
        col = len(i)
        TT_count += col
    window["let"].update(TT_count)
    
    #読み込み処理ボタンを押した時の処理
    if event == "file_read":
        page_count = 0 #ページカウントリセット　誤動作防止の為
        
        if value["file_in"] == "":
            sg.popup("ファイルを選択して下さい")
            continue
        else:
            try:
                
                
                #出力結果保存を非表示にする
                window["OUT"].update(visible=False)
                
                file_data = open(r"{}".format(value["file_in"]),encoding="utf_8")
                data = file_data.read()
                
                #読み込んだファイルの内容をユーザーセッティングに保存する(500文字刻み)
                for d_count in range(2001):
                    L = d_count * 500
                    R = L + 500
                    Setings[f"data_{d_count}"] = data[L:R]
                
              
                window["file_out"].update(Setings["data_0"])
                window["page_count"].update(page_count)
                window["page_value"].update("0～500文字を表示")
                window["let"].update(len(data))
                file_data.close()
                
                #処理開始ボタンを表示する
                window["frame_start"].update(visible=True)
                
                #次へor前へボタンを押せるようにする
                flug = True
                
                
            except:
                pass
    
    #page_countに応じて画面を更新する
    def judgment(page_count):
        
        LL = page_count * 500
        RR = LL + 500
        
        window["file_out"].update(Setings[f"data_{page_count}"])
        window["page_count"].update(page_count)
        window["page_value"].update(f"{LL}～{RR}文字を表示")
        
     
    
    #ユーザーセッティングへテキスト内容を保存する        
    def save_text(page_count):
        Setings[f"data_{page_count}"] = value["file_out"]
       
    
    #前へボタンを押した時の処理
    if event == "back":
        if flug == False:
            sg.popup("ファイルを読み込んでください")
            pass
        else:
            save_text(page_count)
            
            if page_count == 0:
                pass
            else:
                page_count -= 1
                window["now_count"].update(page_count)
                
                try:
                    
                    judgment(page_count)
                    
            
                except:
                    sg.popup("ファイルを読み込んで下さい")
                    pass
            
    #次へボタンを押した時の処理
    if event == "next":
        
        if flug == False:
            sg.popup("ファイルを読み込んでください")
            pass
        else:
        
            save_text(page_count)
            
            if page_count == 2000:
                pass
            else:
                page_count +=1
                window["now_count"].update(page_count)
            
            try:
                
                judgment(page_count)
                
                
            except:
                sg.popup("ファイルを読み込んで下さい")
                pass
    
    #句得点処理
    if event == "START":
        
        save_text(page_count)
        
        if value["threshold"] == "":
            sg.popup("スコア許容度を入力して下さい")
            continue
        else:
            #句読点処理
            save_text(page_count)
            
            
            S = Setings.get_dict()
            out_values = ""
            for tes in S.values():
                OUT_TEXT = main(value=tes ,threshold=float(value["threshold"]))
                out_values += OUT_TEXT + "\n"
                
            window["result_out"].update(out_values)
            window["OUT"].update(visible=True)
        
        
        
        
    #出力結果を保存する
    if event == "save":
        if value["result_out"] == "":
            sg.popup("出力結果がありません")
            continue
        else:
            
            file = open(f"{value['out_file_name']}.txt","w",encoding="UTF-8")
            file.write(value["result_out"])
            file.close()
            sg.popup("ファイルの保存が完了しました")
        
        
        
        
    





Setings.delete_file() #ユーザーセッティングファイルを消去