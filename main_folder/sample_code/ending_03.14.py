# https://github.com/PySimpleGUI/PySimpleGUI
# https://github.com/aimlinux/computer-festival-2023/blob/main/GUI/pysimplegui/main_3/main_3.py

# -*- coding: utf-8 -*-

#----[pip install pysimplegui]----
#----[pip install pyttsx3]----
#----[pip install pyautogui]----
#----[pip install screeninfo]----
#----[pip install pillow]----
#----[pip install pandas]----
#----[pip install pickle]----
#----[pip install scikit-learn]----


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
from PIL import ImageGrab, Image, ImageTk
import win32gui


#--------機械学習で使用--------
import pandas as pd
import pickle
import warnings
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import KFold
from sklearn import svm

warnings.simplefilter('ignore')
#ファイル読み込み
df = pd.read_csv('namelist.csv',sep=",")#Githubとメイン環境はPathは共通



#--------モニターの解像度を取得--------
from screeninfo import get_monitors as gm
monitor = gm()[0]
window_size = (monitor.width, monitor.height)
#print(window_size)



#--------ウィンドウのテーマ--------
sg.theme('Material4')
#sg.theme('LightBlue3')
#ランダムにテーマを変える : sg.theme('SystemDefault8')
#メインテーマ候補 : [LightGreen2, DarkTeal5, LightBlue3]

#--------タイトルバーのアイコンの画像指定（use_custom_titlebar=Trueが指定されている場合のみ有効）--------
#icon_image = 'main_folder/img/icon_img.ico'


#time.sleep(0.1)
sg.popup_ok('アプリケーションを起動します。', font=('Arial', 12), text_color='#ff1493')
#pg.confirm('本当に起動しますか？')
time.sleep(0.2)


# --------起動時アニメーション（本物）--------

#voc = pd.read_csv("voc.csv")#メイン環境
voc = pd.read_csv("main_folder/voc.csv")#Github環境
#tex = pd.read_csv("test1.csv")#メイン環境
tex = pd.read_csv("main_folder/test1.csv")#Github環境

voc = voc.sample(frac=1, ignore_index=True)


canvas = sg.Canvas(size=(1300,920),pad=((0,0),(0,0)))

def ending_1(canvas):
    ending_1 = [
        [canvas]
                ]
    return sg.Window("アプリ君・甲", ending_1,size=(1300,920),relative_location=(0, -75),
                    border_depth=2, resizable=False, finalize=True, 
                    right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False, keep_on_top=True)
    
    
window = ending_1(canvas)

def kou():
    j=0
    
    for i in range(185):
        
        jimaku(voc,tex,i)
        j += 1
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()
        
    for j in range(185):
        j = j + 185
        jimaku(voc,tex,j)
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()

    for i in range(35):
        canvas.tk_canvas.delete("text","k")
        canvas.tk_canvas.create_text(280+i*7,400,fill="red",text="終わり...",font=("Arial",24+i),tag="text")
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update() 

#  ↑ 5.768s
def jimaku(voc,tex,i):
        canvas.tk_canvas.delete("text")
        if i < 186:
            canvas.tk_canvas.create_text(3240-i*16,400,fill="red",text="終わり...",font=("Arial",24),tag="text")
        else:
            canvas.tk_canvas.create_text(280,400,fill="red",text="終わり...",font=("Arial",24),tag="text")
        for j in range(len(tex)):
            x = tex["x"][j]-i*tex["speed"][j]
            if x > -100 :
                canvas.tk_canvas.create_text(x,int(tex["y"][j]),text=voc["voc"][j%352],fill="white",font=("Arial",12+int(tex["size"][j])*4),tag="text")

kou()

time.sleep(2)

window.close()


def ending_2(canvas):
    ending_2 = [
        [canvas]
                ]
    return sg.Window("アプリ君・甲", ending_2,size=(1300,920),relative_location=(0, -75),
                    border_depth=2, resizable=False, finalize=True, 
                    right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False, keep_on_top=True)



window = ending_2(canvas)

def kou():
    j=0
    
    for i in range(185):
        
        jimaku(voc,tex,i)
        j += 1
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()
        
    for j in range(185):
        j = j + 185
        jimaku(voc,tex,j)
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update()

    for i in range(35):
        canvas.tk_canvas.delete("text","k")
        canvas.tk_canvas.create_text(280+i*7,400,fill="red", text="パーフェクト", font=("Arial",24+i), tag="text")
        canvas.tk_canvas.after(22)
        canvas.tk_canvas.update() 

#  ↑ 5.768s
def jimaku(voc,tex,i):
        canvas.tk_canvas.delete("text")
        if i < 186:
            canvas.tk_canvas.create_text(3240-i*16,400,fill="red",text="パーフェクト",font=("Arial",24),tag="text")
        else:
            canvas.tk_canvas.create_text(280,400,fill="red",text="パーフェクト",font=("Arial",24),tag="text")
        for j in range(len(tex)):
            x = tex["x"][j]-i*tex["speed"][j]
            if x > -100 :
                canvas.tk_canvas.create_text(x,int(tex["y"][j]),text=voc["voc"][j%352],fill="white",font=("Arial",12+int(tex["size"][j])*4),tag="text")

kou()

time.sleep(2)

window.close()