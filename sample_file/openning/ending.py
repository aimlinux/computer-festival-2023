import os
import PySimpleGUI as sg
import random as rand
import pyttsx3
import numpy as np
from msilib.schema import Upgrade
from msilib.schema import Binary
from re import U
from turtle import update
import pyautogui as pg
import time
import threading
import pandas as pd
from PIL import Image, ImageTk

from screeninfo import get_monitors as gm
monitor = gm()[0]
window_size = (monitor.width, monitor.height)
# print(window_size)

#--------ウィンドウのテーマ--------
sg.theme('python')
sg.theme('LightBlue3')

time.sleep(0.2)
# sg.popup_ok('アプリケーションを起動します。', font=('Arial', 12), text_color='#ff1493')
# #pg.confirm('本当に起動しますか？')
# time.sleep(0.2)

#canvas = sg.Canvas()
canvas = sg.Canvas(size=(1300,9200),pad=((0,0),(0,0)))

def ending(canvas):
    openning = [
        [canvas]
                ]

    return sg.Window("openning", openning, size=(1300,920), relative_location=(0, -75), border_depth=2, resizable=False, finalize=True)

# ----------------最初に表示するウィンドウを指定する----------------
window = ending(canvas)

def end(canvas):
    read_image = Image.open('main_folder/img/img_5.png')
    im = ImageTk.PhotoImage(image=read_image)
    canvas.tk_canvas.create_image(650,460,image=im)
    canvas.tk_canvas.update()
    canvas.tk_canvas.after(500)
    read_image = Image.open('main_folder/img/img_4.png')
    im = ImageTk.PhotoImage(image=read_image)
    canvas.tk_canvas.create_image(650,460,image=im)
    canvas.tk_canvas.update()
    canvas.tk_canvas.after(500)
    read_image = Image.open('main_folder/img/img_3.png')
    im = ImageTk.PhotoImage(image=read_image)
    canvas.tk_canvas.create_image(650,460,image=im)
    canvas.tk_canvas.update()
    canvas.tk_canvas.after(500)
    read_image = Image.open('main_folder/img/img_2.png')
    im = ImageTk.PhotoImage(image=read_image)
    canvas.tk_canvas.create_image(650,460,image=im)
    canvas.tk_canvas.update()
    canvas.tk_canvas.after(500)
    read_image = Image.open('main_folder/img/img_1.png')
    im = ImageTk.PhotoImage(image=read_image)
    canvas.tk_canvas.create_image(650,460,image=im)
    canvas.tk_canvas.update()
    canvas.tk_canvas.after(500)


end(canvas)

window.close()
