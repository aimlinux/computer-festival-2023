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
# import tkinter as tk

voc = pd.read_csv("./voc.csv")
tex = pd.read_csv("./test1.csv")


voc = voc.sample(frac=1, ignore_index=True)


# print(tex.head())

#--------モニターの解像度を取得--------
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

canvas = sg.Canvas(size=(1300,920),pad=((0,0),(0,0)))
canvas = sg.Canvas(size=(1300,920),pad=((0,0),(0,0)))

def openning(canvas):
    openning = [
        [canvas]
                ]

    return sg.Window("openning", openning,size=(1300,920),relative_location=(0, -75), border_depth=2,resizable=False,finalize=True)

# ----------------最初に表示するウィンドウを指定する----------------
window = openning(canvas)


# canvas.tk_canvas.create_line(450,211,450,527,fill="black",width=38,tag="k1")
# canvas.tk_canvas.create_line(450,230,850,230,fill="black",width=38,tag="k2")
# canvas.tk_canvas.create_line(850,211,850,527,fill="black",width=38,tag="k3")
# canvas.tk_canvas.create_line(450,360,850,360,fill="black",width=38,tag="k4")
# canvas.tk_canvas.create_line(450,500,850,500,fill="black",width=38,tag="k5")
# canvas.tk_canvas.create_line(650,230,650,700,fill="black",width=38,tag="k6")

# def kou():
#     j = 0
#     for i in range(32):
#         canvas.tk_canvas.delete("k1")
#         canvas.tk_canvas.create_line(450,-316+i*17,450,0+i*17,fill="black",width=38,tag="k1")
#         jimaku(voc,tex,j)
#         canvas.tk_canvas.after(22)
#         canvas.tk_canvas.update()
#     #     j += 1
#     # for i in range(51):
#     #     canvas.tk_canvas.delete("k2")
#     #     canvas.tk_canvas.create_line(0+i*17,230,-400+i*17,230,fill="black",width=38,tag="k2")
#     #     jimaku(voc,tex,j)
#     #     canvas.tk_canvas.after(22)
#     #     canvas.tk_canvas.update()
#     #     j += 1
#     # for i in range(32):
#     #     canvas.tk_canvas.delete("k3")
#     #     canvas.tk_canvas.create_line(850,-316+i*17,850,0+i*17,fill="black",width=38,tag="k3")
#     #     jimaku(voc,tex,j)
#     #     canvas.tk_canvas.after(22)
#     #     canvas.tk_canvas.update()
#     #     j += 1
#     # for i in range(51):
#     #     canvas.tk_canvas.delete("k4")
#     #     canvas.tk_canvas.create_line(0+i*17,360,-400+i*17,360,fill="black",width=38,tag="k4")
#     #     jimaku(voc,tex,j)
#     #     canvas.tk_canvas.after(22)
#     #     canvas.tk_canvas.update()
#     #     j += 1
#     # for i in range(51):
#     #     canvas.tk_canvas.delete("k5")
#     #     canvas.tk_canvas.create_line(0+i*17,500,-400+i*17,500,fill="black",width=38,tag="k5")
#     #     jimaku(voc,tex,j)
#     #     canvas.tk_canvas.after(22)
#     #     canvas.tk_canvas.update()
#     #     j += 1
#     # for i in range(42):
#     #     canvas.tk_canvas.delete("k6")
#     #     canvas.tk_canvas.create_line(650,0+i*17,650,-470+i*17,fill="black",width=38,tag="k6") 
#     #     jimaku(voc,tex,j)
#     #     canvas.tk_canvas.after(22)
#     #     canvas.tk_canvas.update()
#     #     j += 1
def kou():
    j=0
    for i in range(185):
        canvas.tk_canvas.delete("k")
        canvas.tk_canvas.create_line(0+i*17,110,-400+i*17,110,fill="black",width=38,tag="k")
        if i < 57:canvas.tk_canvas.create_line(-102+i*17,230,-502+i*17,230,fill="black",width=38,tag="k")
        else:canvas.tk_canvas.create_line(450,230,850,230,fill="black",width=38,tag="k")
        if i < 63:canvas.tk_canvas.create_line(-204+i*17,360,-604+i*17,360,fill="black",width=38,tag="k")
        else:canvas.tk_canvas.create_line(450,360,850,360,fill="black",width=38,tag="k")
        if i < 69:canvas.tk_canvas.create_line(-306+i*17,500,-706+i*17,500,fill="black",width=38,tag="k")
        else:canvas.tk_canvas.create_line(450,500,850,500,fill="black",width=38,tag="k")
        canvas.tk_canvas.create_line(-408+i*17,650,-808+i*17,650,fill="black",width=38,tag="k")
        canvas.tk_canvas.create_line(-510+i*17,810,-910+i*17,810,fill="black",width=38,tag="k")

        canvas.tk_canvas.create_line(50,2201-i*17,50,2517-i*17,fill="black",width=38,tag="k")  
        canvas.tk_canvas.create_line(250,-1003+i*17,250,-1319+i*17,fill="black",width=38,tag="k")
        if i <  130:canvas.tk_canvas.create_line(450,2405-i*17,450,2721-i*17,fill="black",width=38,tag="k") 
        else:canvas.tk_canvas.create_line(450,211,450,527,fill="black",width=38,tag="k")
        if i < 114:canvas.tk_canvas.create_line(650,-1207+i*17,650,-1696+i*17,fill="black",width=38,tag="k") 
        else:canvas.tk_canvas.create_line(650,211,650,700,fill="black",width=38,tag="k")
        if i < 142:canvas.tk_canvas.create_line(850,2607-i*17,850,2923-i*17,fill="black",width=38,tag="k") 
        else:canvas.tk_canvas.create_line(850,211,850,527,fill="black",width=38,tag="k")
        canvas.tk_canvas.create_line(1050,-1411+i*17,1050,-1727+i*17,fill="black",width=38,tag="k") 
        canvas.tk_canvas.create_line(1250,2811-i*17,1250,3127-i*17,fill="black",width=38,tag="k") 

        jimaku(voc,tex,i)


        j += 1
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()
    for j in range(100):
        j = j + 185
        jimaku(voc,tex,j)
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()


    for i in range(35):
         canvas.tk_canvas.delete("text","k")
         canvas.tk_canvas.create_text(280+i*7,400,fill="red",text="アプリ君",font=("Arial",24+i),tag="text")
         canvas.tk_canvas.create_line(450+375/35*i,211+140/35*i,450+375/35*i,527-114/35*i,fill="black",width=38-0.8*i,tag="k")
         canvas.tk_canvas.create_line(450+375/35*i,230+126/35*i,850+51/35*i,230+126/35*i,fill="black",width=38-0.8*i,tag="k")
         canvas.tk_canvas.create_line(850+51/35*i,211+140/35*i,850+51/35*i,527-114/35*i,fill="black",width=38-0.8*i,tag="k")
         canvas.tk_canvas.create_line(450+375/35*i,360+21/35*i,850+51/35*i,360+21/35*i,fill="black",width=38-0.8*i,tag="k")
         canvas.tk_canvas.create_line(450+375/35*i,500-94/35*i,850+51/35*i,500-94/35*i,fill="black",width=38-0.8*i,tag="k")
         canvas.tk_canvas.create_line(650+212/35*i,211+145/35*i,650+212/35*i,700-256/35*i,fill="black",width=38-0.8*i,tag="k") 
         canvas.tk_canvas.after(22)
         canvas.tk_canvas.update() 




#  ↑ 5.768s
def jimaku(voc,tex,i):
        canvas.tk_canvas.delete("text")
        if i < 186:canvas.tk_canvas.create_text(3240-i*16,400,fill="red",text="アプリ君",font=("Arial",24),tag="text")
        else:canvas.tk_canvas.create_text(280,400,fill="red",text="アプリ君",font=("Arial",24),tag="text")
        for j in range(len(tex)):
            x = tex["x"][j]-i*tex["speed"][j]
            if x > -100 :
                canvas.tk_canvas.create_text(x,int(tex["y"][j]),text=voc["voc"][j%352],fill="white",font=("Arial",12+int(tex["size"][j])*4),tag="text")

    

# for i in range(100):
#     canvas.tk_canvas.delete("text")
#     for j in range(46):
#         canvas.tk_canvas.create_text(1300-i*15,5+j*23,text=j,fill="black",font=("Arial",20),tag="text")
#     canvas.tk_canvas.update()
#     canvas.tk_canvas.after(20)

kou()







#--------ウィンドウを繰り返し表示する--------
while True:
    event, values = window.read()


