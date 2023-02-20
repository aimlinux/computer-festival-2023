
import PySimpleGUI as sg
import random as rand

def gui():
    
    # ウィンドウのテーマ
    sg.theme('BrightColors')
    
    # ウィンドウの内容を1列ずつ定義
    layout = [  [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するアプリケーション')],     # テキスト設置
                [sg.Multiline('文字を入力してください', size=(80, 20), key='sentence')], # 文章入力欄を設置
                [sg.Button('新単語生成', key='-generate-')], 
                [sg.Output(size=(60, 8))], 
                [sg.Text('変換言語設定')],
                [sg.Spin(['ひらがなのみ', 'ひらがな・カタカナ'], size=(30,1), initial_value='ひらがな・カタカナ', key='-language-')], 
                [sg.Button('アプリケーションを終了する', key='-ok-')],
    ]
    
    
#----これ以降は必要に応じて書き換える必要あり----
    window = sg.Window('Text Conversion Application', layout)      # ウィンドウ定義

    while True:
        # ウィンドウを表示
        event, values = window.read()
        
        if event == '-generate-':
            c = list (values['sentence'])
            a = rand.randint(0,len(c))
            while True:
                ca = rand.randint(12353,12527)
                if 12438 > ca or ca > 12449:
                    break; 
            cc = c[:a]
            cc.append(chr(ca))
            i = a
            for i in range(len(c)-a):
                cc.append(c[i+a])
            cc = ''.join(cc)
            print(cc)

        if event == '-ok-':
            break
        
        # window右上の×印を押して閉じたとき
        if event == sg.WIN_CLOSED: 
            break

    # 画面から削除して終了
    window.close()  # ウィンドウを閉じる


if __name__ == '__main__':
    gui()