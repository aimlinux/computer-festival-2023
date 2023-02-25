#サイトURL : https://www.teru2teru.com/python/pysimplegui/screen_transition/

import PySimpleGUI as sg

def make_main():
    # ------------ メインウィンドウ作成 ------------
    main_layout = [[sg.Text("メインウィンドウ")],
            [sg.Button("Open")],
            [sg.Button("Exit")]]
    return sg.Window("メインウィンドウ", main_layout, finalize=True)

def make_sub():
    # ------------ サブウィンドウ作成 ------------
    sub_layout = [[sg.Text("サブウィンドウ")],
            [sg.Button("Close")],
            [sg.Button("Exit")]]
    return sg.Window("サブウィンドウ", sub_layout, finalize=True)

# 最初に表示するウィンドウを指定する。
window = make_main()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # Openボタンが押された場合
    elif event == "Open":
        # メインウィンドウを閉じて、サブウィンドウを作成して表示する
        window.close()
        window = make_sub()

    # Closeボタンが押された場合
    elif event == "Close":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make_main()

# ウィンドウを終了する
window.close()