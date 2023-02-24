import PySimpleGUI as sg
import random as rand
import pyttsx3

def make_main():
    #----メインウィンドウの作成----
    # ウィンドウのテーマ
    sg.theme('BrightColors')
    # ウィンドウの内容を1列ずつ定義
    main_layout = [ [sg.Text('入力された文字から創造性のあふれるユニークな単語を生成するアプリケーション')], 
                    [sg.Text('モードを選択してください')], 
                    [sg.Button('sub1', key='-sub1-')]
                    #[sg.Button('sub2')]
    ]
    return sg.Window("メインウィンドウ", main_layout, finalize=True)

    
def make_sub1():
    #----サブウィンドウ1の作成----
    sub1_layout = [  [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するアプリケーション')],     # テキスト設置
                [sg.Multiline('文字を入力してください', size=(80, 20), key='sentence')], # 文章入力欄を設置
                [sg.Button('新単語生成', key='-generate-')], 
                [sg.Button('新単語を読み上げる', key='-speak-')],
                [sg.Output(size=(60, 8))], 
                [sg.Text('言語設定')],
                [sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Button('アプリケーションを終了する', key='-ok-')],
    ]    
    
    while True:
        # ウィンドウを表示
        event, values = window.read()

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
            
        if event == '-ok-':
            break
        
        # window右上のx印を押して閉じたとき
        if event == sg.WIN_CLOSED: 
            break

    # 画面から削除して終了
    window.close() 
    
    return sg.window('サブウィンドウ1', sub1_layout, finalize=True)
    
    
    
    
    
#最初に表示するウィンドウを指定する
window = make_main()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == '-sub1-':
        window.close()
        window = make_sub1()

    
window.close()


