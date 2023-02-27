#サイトURL : https://www.teru2teru.com/python/pysimplegui/screen_transition/
#----[pip install pysimplegui]----
#----[pip install pyttsx3]----
#----[pip install pyautogui]----

import PySimpleGUI as sg
import random as rand
import pyttsx3
import numpy as np
from msilib.schema import Upgrade
from re import U
from turtle import update
import pyautogui as pg

#pg.confirm("アプリケーションを起動しますか？")

#--------ウィンドウのテーマ--------
sg.theme('python')
sg.theme('LightBlue3')
#ランダムにテーマを変える
#sg.theme('SystemDefault8')
#メインテーマ候補
# [LightGreen2, DarkTeal5, LightBlue3]


#--------各ウィンドウのオブジェクト定義--------
def make_main():
    # ------------ メインウィンドウ作成 ------------
    main_layout = [ [sg.Text('', size=(70, 1))], 
                [sg.Text('ユニークな新単語を生成するアプリケーション', font=('Arial', 25),
                text_color='#ff1493', size=(45,2))], 
                [sg.Text('モードを選択してください', font=('Noto Serif CJK JP', 20),
                text_color='#191970', size=(45, 2))], 
                [sg.Button('入力された文字からユニークな新単語を生成するモード', font=('Arial'), size=(50, 2), key='-sub1-')],
                [sg.Button('ひらがなでランダムに文字を生成するモード', font=('Arial'), size=(50, 2), key='-sub2-')],
                [sg.Button('カタカナでランダムに文字を生成するモード', font=('Arial'), size=(50, 2), key='-sub3-')],
                [sg.Button('ローマ字でランダムに文字を生成するモード', font=('Arial'), size=(50, 2), key='-sub4-')],
                [sg.Button('ひらがなで名前をランダムに生成するモード', font=('Arial'), size=(50, 2), key='-sub5-')],
                [sg.Text('', size=(70, 1))],
                [sg.Checkbox('音声OFF', font=('Arial', 16))],
                [sg.Text('', size=(70, 1))],
                [sg.Button('アプリケーションを終了する', font=('Arial'), size=(30, 2), key='-exit-')]
    ]
    return sg.Window("main_layout", main_layout, finalize=True)

def make_sub1():
    # ------------ サブ１ウィンドウ作成 ------------
    sub1_layout = [ [sg.Text('', size=(80, 1))],  
                [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するよ！！', text_color='#191970', font=('Arial', 18))],
                [sg.Text('', size=(80, 1))],
                # 文章入力欄を設置
                [sg.Multiline('文字を入力してください', font=('Arial', 13), text_color='#191970', size=(60, 8), key='sentence_1')],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_1-')], 
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_1-')],
                [sg.Output(size=(70, 10), font=('Arial'))], 
                [sg.Text('言語設定', font=('Arial', 13), text_color='#191970')],
                [sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], font=('Arial', 13), 
                size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る',  font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window("sub1_layout", sub1_layout, finalize=True)


def make_sub2():
    # ------------ サブ２ウィンドウ作成 ------------
    sub2_layout = [ [sg.Text('', size=(80, 1))],  
                [sg.Text('ひらがなでランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 2))],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_2-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_2-')],
                [sg.Output(size=(70, 12), font=('Arial'))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],

    ]    
    return sg.Window('sub2_layout', sub2_layout, finalize=True)


def make_sub3():
    # ------------ サブ３ウィンドウ作成 ------------
    sub3_layout = [ [sg.Text('', size=(80, 1))],  
                [sg.Text('カタカナでランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 2))],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_3-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_3-')],
                [sg.Output(size=(70, 12), font=('Arial'))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub3_layout', sub3_layout, finalize=True)


def make_sub4():
    # ------------ サブ４ウィンドウ作成 ------------
    sub4_layout = [ [sg.Text('', size=(80, 1))],  
                [sg.Text('ローマ字でランダムに文字を生成するよ！！', font=('Arial', 18), text_color='#191970')],     
                [sg.Text('', size=(80, 2))],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_4-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_4-')],
                [sg.Output(size=(70, 12), font=('Arial'))],
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub4_layout', sub4_layout, finalize=True)


def make_sub5():
    # ------------ サブ５ウィンドウ作成 ------------
    sub5_layout = [ [sg.Text('', size=(80, 1))],  
                [sg.Text('ひらがなで名前をランダムに生成するよ！！', font=('Arial', 18), text_color='#191970')],
                [sg.Text('', size=(80, 2))],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_5-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_5-')],
                [sg.Output(size=(70, 12), font=('Arial'))],
                [sg.Text('', size=(80, 1))],
                [sg.Text('実は機械学習を使ってるんだよね！！', font=('Arial', 16), text_color='#191970')],  
                [sg.Text('', size=(80, 2))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub5_layout', sub5_layout, finalize=True)



# 最初に表示するウィンドウを指定する。
window = make_main()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break



#--------sub1ボタンが押された場合--------
    elif event == "-sub1-":
        # メインウィンドウを閉じて、サブ１ウィンドウを作成して表示する
        window.close()
        window = make_sub1()
        
        
#--------サブ１のウィンドウについての設定--------    
    if event == '-generate_1-':
        c = list (values['sentence_1'])
        a = rand.randint(0,len(c))
        while True:
            ca = rand.randint(12353,12540)
            if 12438 > ca or ca > 12449 or ca == 12387 or ca == 12540:
            #if ca == 12387 or ca == 12540:   ////----「ー」「っ」のみ表示----
                break; 
        cc = c[:a]
        cc.append(chr(ca))
        i = a
        for i in range(len(c)-a):
            cc.append(c[i+a])
        cc = ''.join(cc)
        print(cc)
        # --ランダムに生成--
        # print(rand.choice(cc, k=len(cc)))
        #----新単語を読み上げる----
        engine = pyttsx3.init()
        engine.say(cc)
        engine.runAndWait()
    
    # --ボタンを押したら繰り返し再生--
    if event == '-speak_1-':
        engine = pyttsx3.init()
        engine.say(cc) 
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
        #--------各環境で相対パスを変更しよう！！--------
        f_sub2=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/hiragana/hira.bin","rb")
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
        front_sub2=0
        while True:
            r_sub2=rand.randint(1,sum_sub2[front_sub2])
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
        #--------各環境で相対パスを変更しよう！！--------
        f_sub3=open("GUI\pysimplegui\main_3\sample_code\Data_Rand\katakana\kata.bin","rb")
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
        front_sub3=0
        while True:
            r_sub3=rand.randint(1,sum_sub3[front_sub3])
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
        #--------各環境で相対パスを変更しよう！！--------
        f_sub4=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/alpha/alp.bin","rb")
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
        front_sub4=0
        while True:
            r_sub4=rand.randint(1,sum_sub4[front_sub4])
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
        #--------各環境で相対パスを変更しよう！！--------
        f_sub5=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/human/human.bin","rb")
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
        front_sub5=0
        while True:
            r_sub5=rand.randint(1,sum_sub5[front_sub5])
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
        pg.confirm("本当に終了しますか？")
        window.close()


# ウィンドウを終了する
window.close()
