# https://github.com/PySimpleGUI/PySimpleGUI
# https://github.com/aimlinux/computer-festival-2023/blob/main/GUI/pysimplegui/main_3/main_3.py

# -*- coding: utf-8 -*-

#----[pip install pysimplegui]----
#----[pip install pyttsx3]----
#----[pip install pyautogui]----
#----[pip install screeninfo]----

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


#--------モニターの解像度を取得--------
from screeninfo import get_monitors as gm
monitor = gm()[0]
window_size = (monitor.width, monitor.height)
#print(window_size)



#--------ウィンドウのテーマ--------
sg.theme('python')
sg.theme('LightBlue3')
#ランダムにテーマを変える : sg.theme('SystemDefault8')
#メインテーマ候補 : [LightGreen2, DarkTeal5, LightBlue3]

#--------タイトルバーのアイコンの画像指定（use_custom_titlebar=Trueが指定されている場合のみ有効）--------
#icon_image = 'main_folder/img/icon_img.ico'


time.sleep(0.2)
sg.popup_ok('アプリケーションを起動します。', font=('Arial', 12), text_color='#ff1493')
#pg.confirm('本当に起動しますか？')
time.sleep(0.2)





#--------各ウィンドウのオブジェクト定義--------
def make_main():
    top_col = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_main-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ メインウィンドウ作成 ------------
    main_layout = [ 
                [sg.Column(top_col)], 
                #[sg.Text('', size=(70, 1))], 
                [sg.Text('ユニークな新単語を生成するアプリケーション', font=('Arial', 25),
                text_color='#ff1493', size=(45,2))], 
                [sg.Text('・モードを選択してください', font=('Noto Serif CJK JP', 20),
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
    return sg.Window("main_layout", main_layout, finalize=True, size=(1300, 920), relative_location=(0, -80), border_depth=2,
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)


def make_sub1():
    top_col_sub1 = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_sub1-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ サブ１ウィンドウ作成 ------------
    sub1_layout = [ 
                [sg.Column(top_col_sub1)], 
                #[sg.Text('', size=(80, 1))],  
                [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するよ！！', text_color='#191970', font=('Arial', 18))],
                [sg.Text('', size=(80, 1))],
                # 文章入力欄を設置
                [sg.Multiline('文字を入力してください', font=('Arial', 13), text_color='#191970', size=(60, 6), key='-sentence_1-')],
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_1-')], 
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_1-')],
                [sg.Output(size=(70, 10), font=('Arial', 13))], 
                #[sg.Text('言語設定', font=('Arial', 13), text_color='#191970')],
                #[sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], font=('Arial', 13), 
                #size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Text('', size=(80, 1))],
                [sg.Button('モード選択画面に戻る',  font=('Arial', 13), size=(60, 1), key='-back-')],
    ]    
    return sg.Window("sub1_layout", sub1_layout, finalize=True, size=(1300, 920), relative_location=(0, -80), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)



def make_sub2():
    top_col_sub2 = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_sub2-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ サブ２ウィンドウ作成 ------------
    col2 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970')],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_2-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_2-')], 
    ]
    sub2_layout = [ 
                [sg.Column(top_col_sub2)], 
                #[sg.Text('', size=(80, 1))],  
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
    return sg.Window('sub2_layout', sub2_layout, finalize=True, size=(1300,920), relative_location=(0, -80), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)


def make_sub3():
    top_col_sub3 = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_sub3-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ サブ３ウィンドウ作成 ------------
    col3 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_3-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_3-')], 
    ]
    sub3_layout = [ 
                [sg.Column(top_col_sub3)], 
                #[sg.Text('', size=(80, 1))],  
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
    return sg.Window('sub3_layout', sub3_layout, finalize=True, size=(1300, 920), relative_location=(0, -80), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)


def make_sub4():
    top_col_sub4 = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_sub4-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ サブ４ウィンドウ作成 ------------
    col4 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_4-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_4-')], 
    ]
    sub4_layout = [ 
                [sg.Column(top_col_sub4)],
                #[sg.Text('', size=(80, 1))],  
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
    return sg.Window('sub4_layout', sub4_layout, finalize=True, size=(1300, 920), relative_location=(0, -80), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)     


def make_sub5():
    top_col_sub5 = [
                [sg.Button('〓Menu', key='-TopMenu-'), 
                sg.Button('〓preservation', key='-TopPreservation_sub5-'), 
                sg.Button('〓Voice', key='-TopVoice-')], 
    ]
    # ------------ サブ５ウィンドウ作成 ------------
    col5 = [    [sg.Text('文字数の上限と下限を入力してね', font=('Arial, 10'), text_color='#191970'), 
                sg.Text('(デフォルトの値は上限が5、下限が2だよ)', font=('Arial, 10'), text_color='#191970', )],
                [sg.Text('※何も値が入っていない時や、ありえないような値が入っているとアプリが落ちる事があるよ！！', font=('Arial', 10), text_color='#191970')],
                [sg.Multiline('5', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-jog_5-'), 
                sg.Multiline('2', font=('Arial', 9), text_color='#191970', size=(12, 2), key='-kag_5-')], 
    ]  
    sub5_layout = [ 
                [sg.Column(top_col_sub5)],
                #[sg.Text('', size=(80, 1))],  
                [sg.Text('ひらがなで名前をランダムに生成するよ！！', font=('Arial', 18), text_color='#191970')],
                [sg.Text('', size=(80, 1))],                
                [sg.Column(col5)], 
                [sg.Button('新単語生成', font=('Arial', 13), key='-generate_5-')],
                [sg.Button('新単語を読み上げる', font=('Arial', 13), key='-speak_5-')],
                [sg.Output(size=(70, 12), font=('Arial', 13))],
                #[sg.Text('', size=(80, 1))],
                #[sg.Text('実は機械学習を使ってるんだよね！！', font=('Arial', 16), text_color='#191970')],  
                [sg.Text('', size=(80, 1))],
                [sg.Button('モード選択画面に戻る', font=('Arial', 13), size=(60, 1), key='-back-')],
                [sg.Text('', size=(80, 1))],
    ]    
    return sg.Window('sub5_layout', sub5_layout, finalize=True, size=(1300, 920), relative_location=(0, -80), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)




#--------画像表示の定義--------
def img_1():
    img_1_layout = [
        [sg.Image(filename='main_folder/img/img_1.png')]
    ]
    return sg.Window('img_1', img_1_layout, size=(640, 320), relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)

def img_2():
    img_2_layout = [
        [sg.Image(filename='main_folder/img/img_2.png')]
    ]
    return sg.Window('img_2', img_2_layout, size=(640, 320), relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)

def img_3():
    img_3_layout = [
    [sg.Image(filename='main_folder/img/img_3.png')]
    ]
    return sg.Window('img_3', img_3_layout, size=(640, 320), relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
    
def img_4():
    img_4_layout = [
        [sg.Image(filename='main_folder/img/img_4.png')]
    ]
    return sg.Window('img_4', img_4_layout, size=(640, 320), relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
    
def img_5():
    img_5_layout = [
        [sg.Image(filename='main_folder/img/img_5.png')]
    ]
    return sg.Window('img_5', img_5_layout, size=(640, 320), relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)


#--------起動時アニメーション--------
window = img_1()
step = 0
while True:
    event, values = window.read(500)
    break
window.close()

window = img_2()
step = 1
while True:
    event, values = window.read(300)
    break
window.close()

window = img_3()
step = 2
while True:
    event, values = window.read(300)
    break
window.close()

window = img_4()
step = 3
while True:
    event, values = window.read(300)
    break
window.close()

window = img_5()
step = 4
while True:
    event, values = window.read(1000)
    break
window.close()


time.sleep(0.1)
# それぞれの解の初期化
cc_sub1 = 'NULL'
cc_sub2 = 'NULL'
cc_sub3 = 'NULL'
cc_sub4 = 'NULL'
cc_sub5 = 'NULL'


# --------最初に表示するウィンドウを指定する--------
window = make_main()

#--------ウィンドウを繰り返し表示する--------
while True:
    event, values = window.read()
            


# --------右クリックオプション（Exitを除く）--------
    if event == 'Click':
        pg.click(button='left')
        
    if event == 'Menu':
        window.close()
        window = make_main()
        
    if event == 'Restart':
        sg.popup_ok_cancel('アプリケーションを再起動します。', font=('Arial', 12), text_color='#ff1493')
        #pg.confirm('本当に再起動します？')
        window.close()
        time.sleep(0.2)
        window = make_main()
        continue
    
    if event == 'Force Quit':
        window.close()
        pg.confirm('アプリケーションを強制終了します。')
        break
    
    
#--------Topオプション--------
    if event == '-TopMenu-':
        pg.click(button='right')


    if event == '-TopPreservation_main-':
        sg.popup_ok('ここではファイルを書き込みできないよ...',
                'モードを選択してね！！', text_color='#191970')
        
        
#--------txtファイルへのテキストの保存--------

#--------サブ1ウィンドウ--------
    if event == '-TopPreservation_sub1-':
        Origin_window_sub1 = window
        TxtFile_sub1 = 0
        open_file_sub1 = [
            [sg.FileBrowse('.txtファイル'),
            sg.InputText(key='-InputTxt_sub1-')], 
            [sg.Button('ファイルに最新の出力されたテキストを書き込みます', key='-WriteTxt_sub1-')], 
            [sg.Text('※必ず戻るボタンを押して戻ってね。', text_color='#191970')],
            [sg.Text('    ここでは右上の×ボタンは押さないでね。', text_color='#191970')],
            [sg.Button('戻る', key='-FileExit_sub1-')]
        ]   
        window = sg.Window('open_file_sub1', open_file_sub1, relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)

    if event == '-WriteTxt_sub1-':
        TxtFile_sub1 = values['-InputTxt_sub1-']
        f_txt = open(TxtFile_sub1, 'a', encoding='UTF-8')
        f_txt.write(cc_sub1)
        f_txt.write('\n')
        f_txt.close()
        
    if event == '-FileExit_sub1-':
        window.close()
        window = Origin_window_sub1
    

#--------サブ2ウィンドウ--------
    if event == '-TopPreservation_sub2-':
        Origin_window_sub2 = window
        TxtFile_sub2 = 0
        open_file_sub2 = [
            [sg.FileBrowse('.txtファイル'),
            sg.InputText(key='-InputTxt_sub2-')], 
            [sg.Button('ファイルに最新の出力されたテキストを書き込みます', key='-WriteTxt_sub2-')], 
            [sg.Text('※必ず戻るボタンを押して戻ってね。', text_color='#191970')],
            [sg.Text('    ここでは右上の×ボタンは押さないでね。', text_color='#191970')],
            [sg.Button('戻る', key='-FileExit_sub2-')]
        ]   
        window = sg.Window('open_file_sub2', open_file_sub2, relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
        
    if event == '-WriteTxt_sub2-':
        TxtFile_sub2 = values['-InputTxt_sub2-']
        f_txt = open(TxtFile_sub2, 'a', encoding='UTF-8')
        f_txt.write(cc_sub2)
        f_txt.write('\n')
        f_txt.close()
    
    if event == '-FileExit_sub2-':
        window.close()
        window = Origin_window_sub2
        
        
#--------サブ3ウィンドウ--------
    if event == '-TopPreservation_sub3-':
        Origin_window_sub3 = window
        TxtFile_sub3 = 0
        open_file_sub3 = [
            [sg.FileBrowse('.txtファイル'),
            sg.InputText(key='-InputTxt_sub3-')], 
            [sg.Button('ファイルに最新の出力されたテキストを書き込みます', key='-WriteTxt_sub3-')], 
            [sg.Text('※必ず戻るボタンを押して戻ってね。', text_color='#191970')],
            [sg.Text('    ここでは右上の×ボタンは押さないでね。', text_color='#191970')],
            [sg.Button('戻る', key='-FileExit_sub3-')]
        ]   
        window = sg.Window('open_file_sub3', open_file_sub3, relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
        
    if event == '-WriteTxt_sub3-':
        TxtFile_sub3 = values['-InputTxt_sub3-']
        f_txt = open(TxtFile_sub3, 'a', encoding='UTF-8')
        f_txt.write(cc_sub3)
        f_txt.write('\n')
        f_txt.close()
    
    if event == '-FileExit_sub3-':
        window.close()
        window = Origin_window_sub3


#--------サブ4ウィンドウ--------
    if event == '-TopPreservation_sub4-':
        Origin_window_sub4 = window
        TxtFile_sub4 = 0
        open_file_sub4 = [
            [sg.FileBrowse('.txtファイル'),
            sg.InputText(key='-InputTxt_sub4-')], 
            [sg.Button('ファイルに最新の出力されたテキストを書き込みます', key='-WriteTxt_sub4-')], 
            [sg.Text('※必ず戻るボタンを押して戻ってね。', text_color='#191970')],
            [sg.Text('    ここでは右上の×ボタンは押さないでね。', text_color='#191970')],
            [sg.Button('戻る', key='-FileExit_sub4-')]
        ]   
        window = sg.Window('open_file_sub4', open_file_sub4, relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
        
    if event == '-WriteTxt_sub4-':
        TxtFile_sub4 = values['-InputTxt_sub4-']
        f_txt = open(TxtFile_sub4, 'a', encoding='UTF-8')
        f_txt.write(cc_sub4)
        f_txt.write('\n')
        f_txt.close()
    
    if event == '-FileExit_sub4-':
        window.close()
        window = Origin_window_sub4


#--------サブ5ウィンドウ--------
    if event == '-TopPreservation_sub5-':
        Origin_window_sub5 = window
        TxtFile_sub5 = 0
        open_file_sub5 = [
            [sg.FileBrowse('.txtファイル'),
            sg.InputText(key='-InputTxt_sub5-')], 
            [sg.Button('ファイルに最新の出力されたテキストを書き込みます', key='-WriteTxt_sub5-')], 
            [sg.Text('※必ず戻るボタンを押して戻ってね。', text_color='#191970')],
            [sg.Text('    ここでは右上の×ボタンは押さないでね。', text_color='#191970')],
            [sg.Button('戻る', key='-FileExit_sub5-')]
        ]   
        window = sg.Window('open_file_sub5', open_file_sub5, relative_location=(0,0), border_depth=2, 
                    use_default_focus=True, resizable=True, right_click_menu=['Unused', ['Click', 'Menu', 'Restart', 'Properties', 'Force Quit', 'Exit']], 
                    right_click_menu_font='Helvetica', right_click_menu_text_color='#000000', right_click_menu_selected_colors='#da70d6',
                    right_click_menu_tearoff=False)
        
    if event == '-WriteTxt_sub5-':
        TxtFile_sub5 = values['-InputTxt_sub5-']
        f_txt = open(TxtFile_sub5, 'a', encoding='UTF-8')
        f_txt.write(cc_sub5)
        f_txt.write('\n')
        f_txt.close()
    
    if event == '-FileExit_sub5-':
        window.close()
        window = Origin_window_sub5

        
        

#-------音声読み上げ機能の変更---------
    #if event == values['-volume-']:
        #スピーチのレートを変更
        #rate = engine.getProperty('rate')
        #engine.setProperty('rate', rate-100)
        #スピーチのボリュームを変更
        #volume = engine.getProperty('volume')
        #engine.setProperty('volume', volume-1.00)
        #スピーチの声を変える(0が男性, 1が女性の声)
        #voices = engine.getProperty('voices')
        #engine.setProperty('voice', voices[0].id)



#-------ウィンドウが閉じたとき or Exit（右クリックオプション）が押されたとき--------
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        pg.confirm('本当に終了するの...?')
        
        #--------終了時のアニメーション--------
        window = img_5()
        step = 9
        while True:
            event, values = window.read(600)
            break
        window.close()

        window = img_4()
        step = 8
        while True:
            event, values = window.read(300)
            break
        window.close()

        window = img_3()
        step = 7
        while True:
            event, values = window.read(300)
            break
        window.close()

        window = img_2()
        step = 6
        while True:
            event, values = window.read(300)
            break
        window.close()

        window = img_1()
        step = 5
        while True:
            event, values = window.read(600)
            break
        window.close()

        sg.popup_ok('アプリケーションを終了しました。', font=('Arial', 12), text_color='#ff1493')
        window.close()
        break



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
        window.close()



# ウィンドウを終了する
window.close()

if __name__ == 'main':
    exit()