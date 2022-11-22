import PySimpleGUI as sg
import cv2

from video_reader import VideoReader
#from serial_sender import SerialSender
#from .serial_sender import SerialSender
kei=25
kei_s=0
sg.theme("Default")

sg.set_options(dpi_awareness=True,use_ttk_buttons=True)

lay_mes = [
    [sg.Frame("",layout=[
        [sg.Multiline(size=(80,5),key="In")],
        #[sg.Output(size=(80,5),key="In")],
        [sg.Text("ボタンの値"),sg.InputText(key="in_push",size=(10,1))],
        [sg.Text("スライダー(横)"),sg.InputText(key="in_beside",size=(10,1))],
        [sg.Text("スライダー(縦)"),sg.InputText(key="in_vertical",size=(10,1))],
    ])]

]

lay_Button = [
    [sg.Button("",image_filename="b_png\y1.png",key="1",image_subsample=2,pad=(5,0)),sg.Button("",image_filename="b_png\y2.png",key="2",image_subsample=2,pad=(0,0)),sg.Button("",image_filename="b_png\y3.png",key="3",image_subsample=2,pad=(5,0))],
    [sg.Button("",image_filename="b_png\y4.png",key="4",image_subsample=2,pad=(5,2)),sg.Button("",image_filename="b_png\y5.png",key="5",image_subsample=2,pad=(0,2)),sg.Button("",image_filename="b_png\y6.png",key="6",image_subsample=2,pad=(5,2))],
    [sg.Button("",image_filename="b_png\y7.png",key="7",image_subsample=2,pad=(5,0)),sg.Button("",image_filename="b_png\y8.png",key="8",image_subsample=2,pad=(0,0)),sg.Button("",image_filename="b_png\y9.png",key="9",image_subsample=2,pad=(3,0))],
    [sg.Slider(range=(-50,50),default_value=0.0,orientation="h",enable_events=True,pad=((5,0),(0,20)),size=(30,20),key="beside")]

]

lay_cap = [
    [sg.Frame("",layout=[
        [sg.Image("",key="cap",)],
    ],size=(400,400),element_justification="center",vertical_alignment="c",)]

]

#layout = [[lay_mes],[sg.Frame("",layout=[[sg.Column(lay_Button,vertical_alignment="c"),sg.Slider(range=(1,10),enable_events=True,pad=((0,20),(0,0)),size=(13,20))]])],sg.Column(lay_cap,vertical_alignment="c")],
layout = [[lay_mes],[sg.Column(lay_Button,vertical_alignment="c"),sg.Slider(range=(0,100),default_value=25.0,enable_events=True,pad=((0,20),(0,0)),size=(13,20),key="vertical"),sg.Column(lay_cap,vertical_alignment="c")]]


window = sg.Window("application",layout)

Video = VideoReader(0)



#Cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#フレームレート，解像度を設定
#Cap.set(cv2.CAP_PROP_FPS, 60)
#Cap.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
#Cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while True:
    event,value = window.read(timeout=0)

    if event == None:
        break


    markers,frame = Video.execute()
    #Serial_data = Video.execute()[0]

    #ボタンを押した時の処理
    if event == "1":
        #window["in_push"].update("1")
        l_pw=int(500+kei*4.99)
        r_pw=500
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "2":
        #window["in_push"].update("2")
        l_pw=int(500+kei*4.99)
        r_pw=int(500+kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "3":
        #window["in_push"].update("3")
        l_pw=500
        r_pw=int(500+kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "4":
        #window["in_push"].update("4")
        l_pw=int(500+kei*4.99)
        r_pw=int(500-kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
       # SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "5":
        #window["in_push"].update("5")
        l_pw=500
        r_pw=500
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "6":
        #window["in_push"].update("6")
        l_pw=int(500-kei*4.99)
        r_pw=int(500+kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)
    if event == "7":
        #window["in_push"].update("7")
        l_pw=int(500-kei*4.99)
        r_pw=500
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "8":
        window["in_push"].update("8")
        l_pw=int(500-kei*4.99)
        r_pw=int(500-kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)

    if event == "9":
        window["in_push"].update("9")
        l_pw=500
        r_pw=int(500-kei*4.99)
        back_data=str(l_pw)+"/"+str(r_pw)
        #SerialSender.send(back_data)
        window["in_push"].update(back_data)
        window["In"].update(back_data)


    if event == "vertical":
        kei=int(value['vertical'])

    if event == "beside":
        kei_s=int(value['beside'])
        window["In"].update(kei_s)
    '''
    if VideoReader._read_mark_id_points(out_data)!="":
        window["In"].update(markers)
    '''

    window["in_beside"].update(int(value['beside']))
    window["in_vertical"].update(int(value['vertical']))

    #window["In"].update(Serial_data)

    #imageに動画をUP
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window["cap"].update(imgbytes)

    #ラベルエリアに表示
    window["In"].update(markers)
