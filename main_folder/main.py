# https://github.com/PySimpleGUI/PySimpleGUI
# https://github.com/aimlinux/computer-festival-2023/blob/main/GUI/pysimplegui/main_3/main_3.py

# -*- coding: utf-8 -*-

#----[pip install pysimplegui]----
#----[pip install pyttsx3]----
#----[pip install pyautogui]----
#----[pip install screeninfo]----
#----[pip install opencv-python]----
#----[pip install opencv-contrib-python]----

import os
import PySimpleGUI as sg
import random as rand
import pyttsx3
import numpy as np
from msilib.schema import Upgrade
from re import U
from turtle import update
import pyautogui as pg
import time

#--------アニメーション関係--------
#from PIL import Image
#import cv2 as cv
#import io

#--------モニターの解像度を取得--------
from screeninfo import get_monitors as gm
monitor = gm()[0]
window_size = (monitor.width, monitor.height)


#--------ウィンドウのテーマ--------
sg.theme('python')
sg.theme('LightBlue3')
#ランダムにテーマを変える : sg.theme('SystemDefault8')
#メインテーマ候補 : [LightGreen2, DarkTeal5, LightBlue3]



sg.popup_ok('アプリケーションを起動します。', font=('Arial', 12), text_color='#ff1493')
#pg.confirm('本当に起動しますか？')



#--------各ウィンドウのオブジェクト定義--------
def make_main():
    # ------------ メインウィンドウ作成 ------------
    main_layout = [ [sg.Text('', size=(70, 1))], 
                [sg.Text('ユニークな新単語を生成するアプリケーション', font=('Arial', 25),
                text_color='#ff1493', size=(45,2))], 
                [sg.Text('モードを選択してください', font=('Noto Serif CJK JP', 20),
                text_color='#191970', size=(45, 2))], 
                [sg.Button('入力された文字からユニークな新単語を生成するモード', font=('Arial', 11), size=(50, 2), key='-sub1-')],
                [sg.Button('ひらがなでランダムに文字を生成するモード', font=('Arial', 11), size=(50, 2), key='-sub2-')],
                [sg.Button('カタカナでランダムに文字を生成するモード', font=('Arial', 11), size=(50, 2), key='-sub3-')],
                [sg.Button('ローマ字でランダムに文字を生成するモード', font=('Arial', 11), size=(50, 2), key='-sub4-')],
                [sg.Button('ひらがなで名前をランダムに生成するモード', font=('Arial', 11), size=(50, 2), key='-sub5-')],
                [sg.Text('', size=(70, 1))],
                [sg.Checkbox('音声OFF', default=None, font=('Arial', 16), key='-volume-')],
                [sg.Text('', size=(70, 1))],
                [sg.Button('アプリケーションを終了する', font=('Arial, 13'), size=(40, 2), key='-exit-')]
    ]
    return sg.Window("main_layout", main_layout, finalize=True, size=(1300, 820))


def make_sub1():
    # ------------ サブ１ウィンドウ作成 ------------
    sub1_layout = [ #[sg.Text('', size=(80, 1))],  
                [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するよ！！', text_color='#191970', font=('Arial', 18))],
                [sg.Text('', size=(80, 1))],
                # 文章入力欄を設置
                [sg.Multiline('文字を入力してください', font=('Arial', 13), text_color='#191970', size=(60, 6), key='-sentence_1-')],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_1-')], 
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_1-')],
                [sg.Output(size=(70, 10), font=('Arial', 13))], 
                [sg.Text('言語設定', font=('Arial', 13), text_color='#191970')],
                [sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], font=('Arial', 13), 
                size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Text('', size=(80, 1))],
                [sg.Button('モード選択画面に戻る',  font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window("sub1_layout", sub1_layout, finalize=True, size=(1300, 960))


#--------Colum layout の定義--------
    
col2 = [
    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
    sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970')],
    [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
    [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_2-'), 
    sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_2-')], 
]

col3 = [
    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
    sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
    [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
    [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_3-'), 
    sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_3-')], 
]

col4 = [
    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
    sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
    [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
    [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_4-'), 
    sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_4-')], 
]

col5 = [
    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
    sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
    [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
    [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_5-'), 
    sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_5-')], 
]



def make_sub2():
    # ------------ サブ２ウィンドウ作成 ------------
    col2 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970')],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_2-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_2-')], 
    ]
    sub2_layout = [ #[sg.Text('', size=(80, 1))],  
                [sg.Text('ひらがなでランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 1))],
                [sg.Column(col2)], 
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_2-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_2-')],
                [sg.Output(size=(70, 12), font=('Arial', 13))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
                [sg.Text('', size=(80, 1))],
    ]    
    return sg.Window('sub2_layout', sub2_layout, finalize=True, size=(1300,960))


def make_sub3():
    # ------------ サブ３ウィンドウ作成 ------------
    col3 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_3-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_3-')], 
    ]
    sub3_layout = [ #[sg.Text('', size=(80, 1))],  
                [sg.Text('カタカナでランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 1))],
                [sg.Column(col3)], 
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_3-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_3-')],
                [sg.Output(size=(70, 12), font=('Arial', 13))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
                [sg.Text('', size=(80, 1))],
    ]    
    return sg.Window('sub3_layout', sub3_layout, finalize=True, size=(1300, 960))


def make_sub4():
    # ------------ サブ４ウィンドウ作成 ------------
    col4 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_4-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_4-')], 
    ]
    sub4_layout = [ #[sg.Text('', size=(80, 1))],  
                [sg.Text('ローマ字でランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 1))],
                [sg.Column(col4)], 
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_4-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_4-')],
                [sg.Output(size=(70, 12), font=('Arial', 13))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
                [sg.Text('', size=(80, 1))],
    ]    
    return sg.Window('sub4_layout', sub4_layout, finalize=True, size=(1300, 960))


def make_sub5():
    # ------------ サブ５ウィンドウ作成 ------------
    col5 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_5-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_5-')], 
    ]  
    sub5_layout = [ #[sg.Text('', size=(80, 1))],  
                [sg.Text('ひらがなで名前をランダムに生成するよ！！', font=('Arial', 18), text_color='#191970')],
                [sg.Text('', size=(80, 1))],                
                [sg.Column(col5)], 
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_5-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_5-')],
                [sg.Output(size=(70, 12), font=('Arial', 13))],
                [sg.Text('', size=(80, 1))],
                [sg.Text('実は機械学習を使ってるんだよね！！', font=('Arial', 16), text_color='#191970')],  
                [sg.Text('', size=(80, 1))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
                [sg.Text('', size=(80, 1))],
    ]    
    return sg.Window('sub5_layout', sub5_layout, finalize=True, size=(1300, 960))


#def end_window():
    # ---------エンドウィンドウ作成--------
    col_end = [        
        [sg.Button('終了', font=('Arial', 12), key='-TheEnd-'), 
        sg.Button('続ける', font=('Arial', 12), key='-continue-')], 
    ]
    end_layout = [
        [sg.Text('本当にアプリケーションを終了する？', font=('Arial', 10), text_color='#191970')],
        [sg.Column(col_end)]
    ]
    return sg.Window('end_layout', end_layout, finalize=True, size=(400, 100))



'''
#-------アニメーション定義---------
def animation():
    filename = sg.popup_get_file('')
    #取得したファイルがNoneなら終了
    if filename is None:
        return
    
    vidFile = cv.VideoCapture(filename) 
    
    #動画ファイルのプロパティを取得
    num_frame = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)
    
    #--------アニメーションウィンドウ作成---------
    animation_layout = [
        [sg.Image(filename='', key='-image-')],
    ]
    return sg.Window('animation_layout', animation_layout, finalize=True, size=(1300, 820))

start = time.time()

#----相対パスは各環境ごとに変更しよう----
cap = cv.VideoCapture(r'')
size = (1080, 720)
if (cap.isOpened()== False):  
    print("Error") 
    
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("main_layout", frame)
        if cv.waitKey(25) & 0xFF == ord('q'): 
            break    
    else:
        break
cap.release()

cv.destroyAllWindows()
'''


'''
def anime1_window():
    #-------起動アニメーション作成---------
    anime1_layout = [
        [sg.Image(source='main_folder/yuuyake.gif', key='-anime_1-')], 
    ]
    return sg.Window('anime1_layout', anime1_layout, finalize=True, size=(400, 100))
'''





# --------最初に表示するウィンドウを指定する--------
window = make_main()

#--------ウィンドウを繰り返し表示する--------
while True:
    event, values = window.read()
            
            

#-------ウィンドウが閉じたとき--------
    if event == sg.WIN_CLOSED:
        pg.confirm('本当に終了するの...？')
        sg.popup_ok_cancel('アプリケーションを終了します。', font=('Arial', 12), text_color='#ff1493')
        window.close()
        break



#-------音声読み上げ機能の変更---------
    #if event == values['-volume-']:
        #スピーチのレートを変更
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-100)
        #スピーチのボリュームを変更
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume-1.00)
        #スピーチの声を変える(0が男性, 1が女性の声)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)


#--------sub1ボタンが押された場合--------
    if event == "-sub1-":
        # メインウィンドウを閉じて、サブ１ウィンドウを作成して表示する
        window.close()
        window = make_sub1()
        
        
#--------サブ１のウィンドウについての設定--------    
    if event == '-generate_1-':
        c_sub1 = list (values['-sentence_1-'])
        a_sub1 = rand.randint(0,len(c_sub1))
        while True:
            ca_sub1 = rand.randint(12353,12540)
            if 12438 > ca_sub1 or ca_sub1 > 12449 or ca_sub1 == 12387 or ca_sub1 == 12540:
            #if ca_sub1 == 12387 or ca_sub1 == 12540:   ////----「ー」「っ」のみ表示----
                break; 
        cc_sub1 = c_sub1[:a_sub1]
        cc_sub1.append(chr(ca_sub1))
        i_sub1 = a_sub1
        for i_sub1 in range(len(c_sub1)-a_sub1):
            cc_sub1.append(c_sub1[i_sub1+a_sub1])
        cc_sub1 = ''.join(cc_sub1)
        print(cc_sub1)
        # --ランダムに生成--
        # print(rand.choice(cc_sub1, k=len(cc_sub1)))

        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc_sub1)
        engine.runAndWait()

    # --ボタンを押したら繰り返し再生--
    if event == '-speak_1-':
        engine = pyttsx3.init()
        engine.say(cc_sub1) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break
        
        
        
#--------sub2ボタンが押された場合--------
    elif event == '-sub2-':
        # メインウィンドウを閉じて、サブ２ウィンドウを作成して表示する
        window.close()
        window = make_sub2()
    
    
#--------サブ２のウィンドウについての設定--------    
    if event == '-generate_2-':
        #03.01修正箇所は最後にコメント
        kagen_sub2 = int(values['-kag_2-'])#
        jogen_sub2 = int(values['-jog_2-'])#
        #--------各環境で相対パスを変更しよう！！--------
        f_sub2=open("main_folder/hira.bin","rb")
        sum_sub2=[0]*85
        a_sub2=[]
        for i_sub2 in range(85):
            aa_sub2=[]
            for j_sub2 in range(85):
                b_sub2=f_sub2.read(2)
                aaa_sub2=b_sub2[0]*256+b_sub2[1]
                aa_sub2=aa_sub2+[aaa_sub2]
                sum_sub2[i_sub2]=sum_sub2[i_sub2]+aaa_sub2
            a_sub2=a_sub2+[aa_sub2]
        f_sub2.close
        
        #print(a)
        c_sub2=[]
        n_sub2 = 0#
        front_sub2=0
        while n_sub2 < jogen_sub2:#
            r_sub2=rand.randint(1+(n_sub2<kagen_sub2)*a_sub2[front_sub2][0],sum_sub2[front_sub2])#
            count_sub2=0
            i_sub2=-1
            while count_sub2<r_sub2:
                i_sub2=i_sub2+1
                count_sub2=count_sub2+a_sub2[front_sub2][i_sub2]
            #print(i_sub2)
            if i_sub2==0:
                break
            #c_sub2=c_sub2+[i_sub2+(227*256+130)*256+160+(i_sub2>32)*192]
            c_sub2=c_sub2+[227,129+(i_sub2>63),i_sub2+128-(i_sub2>63)*64]
            front_sub2=i_sub2
            n_sub2 = n_sub2 + 1#
        #print
        cc_sub2=bytes(c_sub2).decode("utf-8")
        print(cc_sub2)
        
        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc_sub2)
        engine.runAndWait()
        
    # --ボタンを押したら繰り返し再生--
    if event == '-speak_2-':
        engine = pyttsx3.init()
        engine.say(cc_sub2) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break



#--------sub3ボタンが押された場合--------
    elif event == '-sub3-':
        # メインウィンドウを閉じて、サブ３ウィンドウを作成して表示する
        window.close()
        window = make_sub3()


#--------サブ３のウィンドウについての設定--------    
    if event == '-generate_3-':
        kagen_sub3 = int(values['-kag_3-'])#
        jogen_sub3 = int(values['-jog_3-'])#
        #--------各環境で相対パスを変更しよう！！--------
        f_sub3=open("main_folder/kata.bin","rb")
        sum_sub3=[0]*93
        a_sub3=[]
        for i_sub3 in range(93):
            aa_sub3=[]
            for j_sub3 in range(93):
                b_sub3=f_sub3.read(2)
                aaa_sub3=b_sub3[0]*256+b_sub3[1]
                aa_sub3=aa_sub3+[aaa_sub3]
                sum_sub3[i_sub3]=sum_sub3[i_sub3]+aaa_sub3
            a_sub3=a_sub3+[aa_sub3]
        f_sub3.close
        #print(a_sub3)
        
        c_sub3=[]
        n_sub3 = 0
        front_sub3=0
        while n_sub3 < jogen_sub3:
            r_sub3=rand.randint(1+(n_sub3<kagen_sub3)*a_sub3[front_sub3][0],sum_sub3[front_sub3])#
            count_sub3=0
            i_sub3=-1
            while count_sub3<r_sub3:
                i_sub3=i_sub3+1
                count_sub3=count_sub3+a_sub3[front_sub3][i_sub3]
            #print(i_sub3)
            if i_sub3==0:
                break
            #c_sub3=c_sub3+[i_sub3+(227*256+130)*256+160+(i_sub3>32)*192]
            c_sub3=c_sub3+[227,130+(i_sub3>31),i_sub3+160-(i_sub3>31)*64]
            front_sub3=i_sub3
            n_sub3 = n_sub3 + 1#
        #print(c_sub3)
        cc_sub3=bytes(c_sub3).decode("utf-8")
        print(cc_sub3)
        
        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc_sub3)
        engine.runAndWait()
        
    # --ボタンを押したら繰り返し再生--
    if event == '-speak_3-':
        engine = pyttsx3.init()
        engine.say(cc_sub3) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break



#--------sub4ボタンが押された場合--------
    elif event == '-sub4-':
        # メインウィンドウを閉じて、サブ４ウィンドウを作成して表示する
        window.close()
        window = make_sub4()
        
        
#--------サブ４のウィンドウについての設定--------    
    if event == '-generate_4-':
        kagen_sub4 = int(values['-kag_4-'])#
        jogen_sub4 = int(values['-jog_4-'])#
        #--------各環境で相対パスを変更しよう！！--------
        f_sub4=open("main_folder/alp.bin","rb")
        sum_sub4=[0]*27
        a_sub4=[]
        for i_sub4 in range(27):
            aa_sub4=[]
            for j_sub4 in range(27):
                b_sub4=f_sub4.read(2)
                aaa_sub4=b_sub4[0]*256+b_sub4[1]
                aa_sub4=aa_sub4+[aaa_sub4]
                sum_sub4[i_sub4]=sum_sub4[i_sub4]+aaa_sub4
            a_sub4=a_sub4+[aa_sub4]
        f_sub4.close
        #print(a_sub4)
        
        c_sub4=[]
        n_sub4 = 0#
        front_sub4=0
        while n_sub4 < jogen_sub4:#
            r_sub4=rand.randint(1+(n_sub4<kagen_sub4)*a_sub4[front_sub4][0],sum_sub4[front_sub4])#
            count_sub4=0
            i_sub4=-1
            while count_sub4<r_sub4:
                i_sub4=i_sub4+1
                count_sub4=count_sub4+a_sub4[front_sub4][i_sub4]
            #print(i_sub4)
            if i_sub4==0:
                break
            #c_sub4=c_sub4+[i_sub4+(227*256+130)*256+160+(i_sub4>32)*192]
            c_sub4=c_sub4+[i_sub4+96]
            front_sub4=i_sub4
            n_sub4 = n_sub4 + 1#
        #print(c_sub4)
        cc_sub4=bytes(c_sub4).decode("utf-8")
        print(cc_sub4)
        
        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc_sub4)
        engine.runAndWait()
        
    # --ボタンを押したら繰り返し再生--
    if event == '-speak_4-':
        engine = pyttsx3.init()
        engine.say(cc_sub4) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break
        
        
        
#--------sub5ボタンが押された場合--------
    elif event == '-sub5-':
        # メインウィンドウを閉じて、サブ５ウィンドウを作成して表示する
        window.close()
        window = make_sub5()
        
        
#--------サブ5のウィンドウについての設定--------    
    if event == '-generate_5-':
        kagen_sub5 = int(values['-kag_5-'])#
        jogen_sub5 = int(values['-jog_5-'])#
        #--------各環境で相対パスを変更しよう！！--------
        f_sub5=open("main_folder/human.bin","rb")
        sum_sub5=[0]*85
        a_sub5=[]
        for i_sub5 in range(85):
            aa_sub5=[]
            for j_sub5 in range(85):
                b_sub5=f_sub5.read(2)
                aaa_sub5=b_sub5[0]*256+b_sub5[1]
                aa_sub5=aa_sub5+[aaa_sub5]
                sum_sub5[i_sub5]=sum_sub5[i_sub5]+aaa_sub5
            a_sub5=a_sub5+[aa_sub5]
        f_sub5.close
        #print(a_sub5)
        
        c_sub5=[]
        n_sub5 = 0#
        front_sub5=0
        while n_sub5 < jogen_sub5:
            r_sub5=rand.randint(1+(n_sub5<jogen_sub5)*a_sub5[front_sub5][0],sum_sub5[front_sub5])#
            count_sub5=0
            i_sub5=-1
            while count_sub5<r_sub5:
                i_sub5=i_sub5+1
                count_sub5=count_sub5+a_sub5[front_sub5][i_sub5]
            #print(i_sub5)
            if i_sub5==0:
                break
            #c_sub5=c_sub5+[i_sub5+(227*256+130)*256+160+(i_sub5>32)*192]
            c_sub5=c_sub5+[227,129+(i_sub5>63),i_sub5+128-(i_sub5>63)*64]
            front_sub5=i_sub5
            n_sub5 = n_sub5 + 1#
        #print(c_sub5)
        cc_sub5=bytes(c_sub5).decode("utf-8")
        print(cc_sub5)
        
        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc_sub5)
        engine.runAndWait()
        
    # --ボタンを押したら繰り返し再生--
    if event == '-speak_5-':
        engine = pyttsx3.init()
        engine.say(cc_sub5) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break



    # 「メニュー選択画面に戻る」ボタンが押された場合
    elif event == "-back-":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make_main()
    
    
    #「アプリケーションを終了する」ボタンが押された場合
    elif event == '-exit-':
        # メインウィンドウを閉じて、アプリケーションを終了する
        #pg.confirm("本当に終了しますか？")
        window.close()



# ウィンドウを終了する
window.close()

if __name__ == 'main':
    exit()