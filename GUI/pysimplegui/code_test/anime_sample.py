# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_OpenCV.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from PIL import Image
import cv2 as cv
import io

"""
OpenCVを使用してファイルを開いて再生するデモプログラム
主な目的は、次のことを示すことです。
1.OpenCVを使用してビデオファイルから一度にフレームを取得する方法
2.PySimpleGUIウィンドウに画像を表示する方法
さらにスライダーを使用してビデオのフレーム位置を変更できます。
"""

# メイン関数
def main():

    # ポップアップでファイル名を取得する
    filename = sg.popup_get_file('　再生する動画ファイルを指定してください　')

    #　取得したファイルがNoneなら、終了
    if filename is None:
        return

    #　選択された動画ファイルの読み込み
    vidFile = cv.VideoCapture(filename)

    #　動画ファイルのプロパティを取得（総フレーム数、FPS）
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.theme('Black')

    # ウィンドウレイアウトを定義（1行目：テキスト、2行目：動画、3行目：スライダー、4行目：ボタン）
    layout = [[sg.Text(' 動画再生中　 ', size=(15, 1), font='Helvetica 20')],
                  [sg.Image(filename='', key='-image-')],
                  [sg.Slider(range=(0, num_frames),size=(60, 10), orientation='h', key='-slider-')],
                  [sg.Button('Exit', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14')]]

    # ウィンドウを作成
    window = sg.Window('　動画ファイルを再生するアプリ　', layout, no_titlebar=False, location=(0, 0))

    image_elem = window['-image-']
    slider_elem = window['-slider-']

    cur_frame = 0
    #　ビデオファイルが開かれている間は、ループ
    while vidFile.isOpened():

        # イベントを取得
        event, values = window.read(timeout=0)

        # 「Exit」ボタン押下時の処理
        if event in ('Exit', None):
            break

        #　ビデオファイルからの読み込み
        ret, frame = vidFile.read()

        #　データが不足している場合は、ループを停止させます。
        if not ret:  # if out of data stop looping
            break

        #　スライダーを手動で動かした場合は、指定したフレームにジャンプします
        if int(values['-slider-']) != cur_frame-1:
            cur_frame = int(values['-slider-'])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)

        #　スライダー表示を更新
        slider_elem.update(cur_frame)
        cur_frame += 1

        #　カメラ映像を圧縮して、画像表示画面'-image-'を更新する
        imgbytes = cv.imencode('.png', frame)[1].tobytes()
        image_elem.update(data=imgbytes)

#メイン関数をCALL
main()