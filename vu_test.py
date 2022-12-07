

import PySimpleGUI as sg

# ボタンが押されたときに表示する画像のファイルパス
img_file1 = "C:\ ar-marker-main\ ar-marker-main\ src\ AprilTag\ AprilTag000.png"

# ボタンが押されていないときに表示する画像のファイルパス
img_file2 = "C:\ ar-marker-main\ ar-marker-main\src\AprilTag\AprilTag600.png"

# Imageウィジェットを作成
img = sg.Image(filename=img_file1,key="IMG")

# GUIのレイアウト
layout = [
    [img],
    [sg.Button('Press Me',key='Press Me',button_type=9)]
]

# GUIのウィンドウを作成
window = sg.Window('Image Viewer', layout)

# GUIのイベントループ
while True:
    event, values = window.read(timeout=0)
    if event in (None, 'Cancel'):
        break
    if event == 'Press Me':
        # ボタンが押されたときに、画像を差し替える
        window["IMG"].update(filename=img_file2)
    if event != 'Press Me':
        # ボタンが押されていないときに、画像を差し替える
        window["IMG"].update(filename=img_file1)

# GUIのウィンドウを閉じる
window.close()

