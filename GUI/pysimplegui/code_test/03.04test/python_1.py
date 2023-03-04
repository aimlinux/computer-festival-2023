import time
import PySimpleGUI as sg

#ウィンドウ作成
layout = [[sg.InputText("",size=(35,1),key="tx1",text_color="#0000ff",background_color="#ffff00")],
        [sg.Button("文",key="bt1")],
        [sg.Button("clear",key="bt2"),sg.Button("Quit",key="bt3")]]
window = sg.Window("sleep",layout)

#イベントループ
step = 0
while True:
    event, values = window.read(timeout=10)
    if event in (None,"bt3"):
        break
    elif event == "bt1":
        step += 1
        if step == 1:
            window["tx1"].update("ようこそ")
            ts = time.time()
        else:
            if time.time() - ts >= 3:
                window["tx1"].update("プログラムを起動します")
    elif event == "bt2":
        window["tx1"].update("")
        step = 0

#終了処理
window.close()