#サイトURL : https://www.teru2teru.com/python/pysimplegui/screen_transition/

import PySimpleGUI as sg
import random as rand
import pyttsx3

# ウィンドウのテーマ
sg.theme('python')

def make_main():
    # ------------ メインウィンドウ作成 ------------
    main_layout = [ [sg.Text('ユニークな新単語を生成するアプリケーション', size=(50,3))], 
                    [sg.Text('メニューを選択してください', size=(50, 2))], 
                    [sg.Button('sub1', size=(20, 2), key='-sub1-')],
                    [sg.Button('sub2', size=(20, 2), key='-sub2-')],
                    [sg.Button('sub3', size=(20, 2), key='-sub3-')],
                    [sg.Button('sub4', size=(20, 2), key='-sub4-')],
                    [sg.Button('sub5', size=(20, 2), key='-sub5-')],
                    [sg.Button('アプリケーションを終了する', size=(30, 2), key='-exit-')]
    ]
    return sg.Window("main_layout", main_layout, finalize=True)

def make_sub1():
    # ------------ サブ１ウィンドウ作成 ------------
    sub1_layout = [  [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するよ！！')],     # テキスト設置
                [sg.Multiline('文字を入力してください', size=(80, 20), key='sentence')], # 文章入力欄を設置
                [sg.Button('新単語生成', key='-generate-')], 
                [sg.Button('新単語を読み上げる', key='-speak-')],
                [sg.Output(size=(60, 8))], 
                [sg.Text('言語設定')],
                [sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Button('メニュー選択画面に戻る', size=(60, 1), key='-back-')],
    ]    
    return sg.Window("sub1_layout", sub1_layout, finalize=True)


def make_sub2():
    # ------------ サブ２ウィンドウ作成 ------------
    sub2_layout = [  [sg.Text('ひらがなでランダムに文字を生成するよ！！')],     
                [sg.Button('メニュー選択画面に戻る', size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub2_layout', sub2_layout, finalize=True)


def make_sub3():
    # ------------ サブ３ウィンドウ作成 ------------
    sub3_layout = [  [sg.Text('カタカナでランダムに文字を生成するよ！！')],     
                [sg.Button('メニュー選択画面に戻る', size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub3_layout', sub3_layout, finalize=True)


def make_sub4():
    # ------------ サブ４ウィンドウ作成 ------------
    sub5_layout = [  [sg.Text('ローマ字でランダムに文字を生成するよ！！')],     
                [sg.Button('メニュー選択画面に戻る', size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub5_layout', sub5_layout, finalize=True)


def make_sub5():
    # ------------ サブ５ウィンドウ作成 ------------
    sub4_layout = [  [sg.Text('ひらがなで名前をランダムに生成するよ！！')],
                [sg.Text('実は機械学習を使ってるんだよね！！')],  
                [sg.Button('メニュー選択画面に戻る', size=(60, 1), key='-back-')],
    ]    
    return sg.Window('sub4_layout', sub4_layout, finalize=True)


# 最初に表示するウィンドウを指定する。
window = make_main()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # sub1ボタンが押された場合
    elif event == "-sub1-":
        # メインウィンドウを閉じて、サブ１ウィンドウを作成して表示する
        window.close()
        window = make_sub1()
        
        
#--------サブ１のウィンドウについての設定--------    
    if event == '-generate-':
        c = list (values['sentence'])
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
    if event == '-speak-':
        engine = pyttsx3.init()
        engine.say(cc) 
        engine.runAndWait()
            
    # window右上のx印を押して閉じたとき
    if event == sg.WIN_CLOSED: 
        break
        
        
        
    #sub2ボタンが押された場合
    elif event == '-sub2-':
        # メインウィンドウを閉じて、サブ２ウィンドウを作成して表示する
        window.close()
        window = make_sub2()


    #sub3ボタンが押された場合
    elif event == '-sub3-':
        # メインウィンドウを閉じて、サブ３ウィンドウを作成して表示する
        window.close()
        window = make_sub3()


    #sub4ボタンが押された場合
    elif event == '-sub4-':
        # メインウィンドウを閉じて、サブ４ウィンドウを作成して表示する
        window.close()
        window = make_sub4()
        
        
    #sub5ボタンが押された場合
    elif event == '-sub5-':
        # メインウィンドウを閉じて、サブ５ウィンドウを作成して表示する
        window.close()
        window = make_sub5()



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