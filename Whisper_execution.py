
import whisper
import PySimpleGUI as sg
import subprocess
import os
import six
import torch
import requests
import json


#話者分離機能OFF　API処理
def main_act(API_key,audio_file,noise,language):
    headers = {
    'accept': 'application/json',
    #APIキー
    'x-gladia-key': f'{API_key}',
}

    files = {
        #読み込みファイル
        'audio': (f"{audio_file}", open(f'{audio_file}', 'rb'), 'audio/mpeg'),
        #翻訳言語
        'language': (None, f'{language}'),
        #翻訳言語
        'target_translation_language': (None, f'{language}'),
        #言語行動 [manual, automatic single language, automatic multiple languages]
        'language_behaviour': (None, 'manual'),
        #ノイズ減少機能
        'toggle_noise_reduction': (None, f'{noise}'),
        #出力フォーマット [json, srt, txt, plain]
        'output_format': (None, 'plain'),
        #話者分離機能
        'toggle_diarization': (None, 'false'),


    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)

    
    outv = response.text
    out_V = outv.replace('"','')
    return out_V

#話者分離機能ON　API処理
def diarization_main_act(API_key,audio_file,speakers,noise,language):
    headers = {
    'accept': 'application/json',
    #APIキー
    'x-gladia-key': f'{API_key}',
}

    files = {
        #読み込みファイル
        'audio': (f"{audio_file}", open(f'{audio_file}', 'rb'), 'audio/mpeg'),
        #翻訳言語
        'language': (None, f'{language}'),
        #翻訳言語
        'target_translation_language': (None, f'{language}'),
        #言語行動 [manual, automatic single language, automatic multiple languages]
        'language_behaviour': (None, 'manual'),
        #ノイズ減少機能
        'toggle_noise_reduction': (None, f'{noise}'),
        #出力フォーマット [json, srt, txt, plain]
        'output_format': (None, 'plain'),
        #話者分離機能
        'toggle_diarization': (None, 'true'),
        #最大スピーカー数
        'diarization_max_speakers': (None, f'{speakers}'),
        

    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)

    #out = json.loads(response.text)
    #out_str = ""
    
    
    #for i in out["prediction"]:
    #    out_str += f"{i['speaker']}:{i['transcription']}\n"
    
    
    outv = response.text
    out_V = outv.replace('"','')
    
    return out_V

#CUDA認識
cuda = str(torch.cuda.is_available())

#def resource_path(relative):
#  if hasattr(sys, "_MEIPASS"):
#      return os.path.join(sys._MEIPASS, relative)
#  return os.path.join(relative)

sg.theme("Black")

def Whisper_start(model,file_name,language_name,output_dir):
    Model = whisper.load_model(model)
    result = Model.transcribe(file_name,verbose=True,language="{}".format(language_name))
    file_first_name = os.path.split(file_name)[1]
    File_First_Name = os.path.splitext(file_first_name)[0]
 
    Name_File = "{}.txt".format(File_First_Name)
    HH = os.path.join(output_dir,Name_File)
    print(HH)
    with open(HH,"w") as f:
        f.write(result["text"])
        f.close()
        
    


sg.set_options(dpi_awareness=True,use_ttk_buttons=True,font=("デジタル",10))

Model_list = ["tiny.en","tiny","base.en","base","small.en","small","medium.en","medium","large-v1","large-v2","large"]

Language_list =["af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu","fa",
                "fi","fo","fr","gl","gu","ha","haw","hi","hr","ht","hu","hy","id","is","it","iw","ja","jw","ka","kk","km","kn","ko",
                "la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc","pa","pl","ps","pt",
                "ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th","tk","tl","tr","tt","uk","ur",
                "uz","vi","yi","yo","zh","Afrikaans","Albanian","Amharic","Arabic","Armenian","Assamese","Azerbaijani","Bashkir","Basque",
                "Belarusian","Bengali","Bosnian","Breton","Bulgarian","Burmese","Castilian","Catalan","Chinese","Croatian","Czech","Danish",
                "Dutch","English","Estonian","Faroese","Finnish","Flemish","French","Galician","Georgian","German","Greek","Gujarati",
                "Haitian","Haitian Creole","Hausa","Hawaiian","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Italian","Japanese",
                "Javanese","Kannada","Kazakh","Khmer","Korean","Lao","Latin","Latvian","Letzeburgesch","Lingala","Lithuanian","Luxembourgish",
                "Macedonian","Malagasy","Malay","Malayalam","Maltese","Maori","Marathi","Moldavian","Moldovan","Mongolian","Myanmar",
                "Nepali","Norwegian","Nynorsk","Occitan","Panjabi","Pashto","Persian","Polish","Portuguese","Punjabi","Pushto","Romanian",
                "Russian","Sanskrit","Serbian","Shona","Sindhi","Sinhala","Sinhalese","Slovak","Slovenian","Somali","Spanish","Sundanese",
                "Swahili","Swedish","Tagalog","Tajik","Tamil","Tatar","Telugu","Thai","Tibetan","Turkish","Turkmen","Ukrainian","Urdu",
                "Uzbek","Valencian","Vietnamese","Welsh","Yiddish","Yoruba"]

device_list=["cpu", "cuda", "ipu", "xpu", "mkldnn", "opengl", "opencl", "ideep", "hip", "ve", "ort", "mps", "xla", "lazy", "vulkan", "meta", "hpu"]

output_format_list = ["txt","vtt","srt","tsv","json","all"]


API_Language_list = ["afrikaans","albanian","amharic","arabic","armenian","assamese","azerbaijani",
                     "bashkir","basque","belarusian","bengali","bosnian","breton","bulgarian","catalan",
                     "chinese","croatian","czech","danish","dutch","english","estonian","faroese",
                     "finnish","french","galician","georgian","german","greek","gujarati","haitian creole",
                     "hausa","hawaiian","hebrew","hindi","hungarian","icelandic","indonesian","italian",
                     "japanese","javanese","kannada","kazakh","khmer","korean","lao","latin","latvian",
                     "lingala","lithuanian","luxembourgish","macedonian","malagasy","malay","malayalam",
                     "maltese","maori","marathi","mongolian","myanmar","nepali","norwegian","nynorsk",
                     "occitan","pashto","persian","polish","portuguese","punjabi","romanian","russian",
                     "sanskrit","serbian","shona","sindhi","sinhala","slovak","slovenian","somali",
                     "spanish","sundanese","swahili","swedish","tagalog","tajik","tamil","tatar",
                     "telugu","thai","tibetan","turkish","turkmen","ukrainian","urdu","uzbek",
                     "vietnamese","welsh","wolof","yiddish","yoruba"]

lay_1 = sg.Tab("通常Whisper",[
    [sg.Text("CUDA認識"),sg.InputText(default_text= cuda , size=(6,1),)],
    [sg.Frame("",[
    [sg.Text("task選択"),sg.Combo(values=["transcribe","translate"],default_value="transcribe",key="task",readonly=True)],
    [sg.Text("翻訳するファイルを選択"),sg.InputText(key="in_file",size=(20,1)),sg.FileBrowse("ファイル選択")],
    [sg.Text("学習モデルを選択"),sg.Combo(values=Model_list,auto_size_text=True,key="model",readonly=True,default_value="base")],
    [sg.Text("モデル保存場所を選択"),sg.InputText(default_text=f"{os.path.dirname(__file__)}",key="model_dir",size=(20,1)),sg.FolderBrowse("フォルダ選択")],
    [sg.Text("翻訳言語を選択"),sg.Combo(values=Language_list,size=(15,1),key="language",readonly=True,default_value="Japanese")],
    [sg.Text("デバイスを選択 --device"),sg.Combo(values=device_list,size=(15,1),key="device",readonly=True,default_value="cpu")],
    [sg.Text("出力形式を選択"),sg.Combo(values=output_format_list,auto_size_text=True,readonly=True,default_value="all",key="output_format")],
    [sg.Text("保存先のフォルダを選択"),sg.InputText(key="output_dir",size=(20,1)),sg.FolderBrowse("フォルダ選択")],]),],
    [sg.Frame("",[
    [sg.Multiline(size=(52,10),key="out")],
    [sg.Button("保存先のフォルダを開く",key="open_dir",visible=False,button_color=("white","blue")),],
    ])],
    [sg.Button("START",key="START")],
])


lay_2 = sg.Tab("Gladia_API",[
    [sg.Frame("",[
    [sg.Text("APIキー"),sg.InputText(key="API_key",size=(25,1))],
    [sg.Text("オーディオファイル選択"),sg.InputText(key="API_in_file",size=(30,1)),sg.FileBrowse("選択")],
    [sg.Text("翻訳言語"),sg.Combo(values=API_Language_list,size=(15,1),key="target_translation_language",readonly=True,default_value="japanese")],
    [sg.Text("ノイズ減少機能"),sg.Checkbox("",key="toggle_noise_reduction",enable_events=True)],
    [sg.Frame("",layout=[
        
        [sg.Text("話者分離機能"),sg.Radio("OFF",group_id="A",default=True,key="toggle_diarization_off",enable_events=True),sg.Radio("ON",group_id="A",key="toggle_diarization_on",enable_events=True)],
        [sg.Text("最大スピーカー数",key="最大スピーカー数",visible=False),sg.InputText(key="diarization_max_speakers",size=(5,1),default_text="2",visible=False)],
        
    ])],
    
    
    
    
    ])],
    
    [sg.Frame("",[
        [sg.Multiline(size=(52,10),key="api_out")],
        
    ])],
    
    [sg.Button("START",key="api_start",enable_events=True)],
  
])


layout = [[sg.TabGroup([[lay_1,lay_2]])]]

window = sg.Window("Whisper",layout,)

while True:
    event, value = window.read()
    if event == None:
        break
    
    
    #翻訳処理関数
    def GO (file_path):
        
        out = subprocess.run("whisper  {0}  --language {1} --task {2} --model {3} --output_dir {4} --device {5} --model_dir {6} --output_format {7} ".format(file_path,value["language"],value["task"],value["model"],r"{}".format(value["output_dir"]),value["device"],
                                                                                                                                         value["model_dir"],value["output_format"]),shell=True,  stdout=subprocess.PIPE)#check=True
        out_put = str(out.stdout,"shift_jis")
        
        return out_put
    
    

   
    #翻訳処理実行
    if event == "START":
        
       
        
        if value["in_file"] == "":
            sg.popup("翻訳するファイルを選択して下さい")
            continue
        if value["output_dir"] == "":
            sg.popup("保存先のフォルダを選択して下さい")
            continue
        
        window["open_dir"].update(visible=False)
        window.refresh()
        go = GO(value["in_file"])
        window["out"].update(go)
        #Whisper_start(model=value["model"],file_name=value["in_file"],language_name=value["language"],output_dir=value["output_dir"])
        
        window["open_dir"].update(visible=True)
       
    #フォルダを開く    
    if event == "open_dir":
        if value["output_dir"] == "":
            sg.popup("保存先のフォルダを選択して下さい")
            continue
        os.chdir(value["output_dir"])
        subprocess.Popen(["explorer","."],shell=True)
        continue
    
    
#-+-+-+-+-+-+-+-+-+-+-+-Gladia_API実行処理-+-+-+-+-+-+-+-+-+-+-+-+-
    
    #ラジオボタン"話者分離機能"を切り替えた時の処理
    if value["toggle_diarization_on"] == True:
        window["最大スピーカー数"].update(visible=True)
        window["diarization_max_speakers"].update(visible=True)
    
    elif value["toggle_diarization_off"] == True:
        window["最大スピーカー数"].update(visible=False)
        window["diarization_max_speakers"].update(visible=False)

    #処理実行
    if event == "api_start":
        
        #(拡張子あり)ファイル名の取得
        file_name = os.path.split(value["API_in_file"])[1]
        #(拡張子無し)ファイル名の取得
        extension_file_name = os.path.splitext(file_name)[0]
        
        
        #ノイズ減少機能の有無を判定
        if value["toggle_noise_reduction"] == True:
           noise_value = "true"
           
        elif value["toggle_noise_reduction"] == False:
           noise_value = "false"
           
            
        #話者分離機能OFF　処理実行
        if value["toggle_diarization_off"] == True:
            get_api = main_act(API_key=f"{value['API_key']}", audio_file=value["API_in_file"],
                               noise=noise_value,language=value["target_translation_language"])
            window["api_out"].update(get_api)
            
            #テキスト出力
            f = open(f"{extension_file_name}.txt","w")
            f.write(get_api)
            f.close()
        #話者分離機能ON　処理実行
        elif value["toggle_diarization_on"] == True:
            get_api = diarization_main_act(API_key=f"{value['API_key']}", audio_file=value["API_in_file"], speakers=value["diarization_max_speakers"],
                                           noise=noise_value,language=value["target_translation_language"])
            window["api_out"].update(get_api)
            
            #テキスト出力
            f = open(f"{extension_file_name}.txt","w")
            f.write(get_api)
            f.close()
    
