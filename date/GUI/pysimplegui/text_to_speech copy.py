
import PySimpleGUI as sg
from gtts import gTTS

def gui():
    # ウィンドウのテーマ
    sg.theme('DarkTeal1')
    
    # ウィンドウの内容を1列ずつ定義
    layout = [  [sg.Text('入力された文字から創造性のあふれるユニークな新単語を生成するアプリケーション')],     # テキスト設置
                [sg.Multiline('文字を入力してください', size=(80, 20), key='sentence')], # 文章入力欄を設置
                [sg.Button('新単語生成', key='bt')], 
                [sg.Text('ユニークな新単語が生成されました')], 
                [sg.InputText(default_text='speech_file', size=(80, 1), key='file_name')], # 出力ファイル名を入力する
                [sg.Text('変換言語設定')],
                [sg.Spin(['ひらがなのみ', 'ひらがな, カタカナ'], size=(30,1), initial_value='ひらがなのみ', key='language')], # jaが日本語、enが英語
    ]
    
    
#----これ以降は必要に応じて書き換える必要あり----
    window = sg.Window('Text Conversion Application', layout)      # ウィンドウ定義

    while True:
        # ウィンドウを表示
        event, values = window.read()

        if event == 'bt': # ボタンを押したとき
            message = text_to_speech(values['sentence'], values['file_name'], values['language']) # Text to Speechを実施
            sg.Popup(message, title='') # 処理結果をポップアップでお知らせ
        
        elif event == sg.WIN_CLOSED: # window右上の×印を押して閉じたとき
            break

    # 画面から削除して終了
    window.close()  # ウィンドウを閉じる


def text_to_speech(sentences, file_name, language):
    '''
    Text to Speechを実施する関数
    <入力>
        sentences:テキスト文章 (str)
        file_name:出力ファイル名 (str)
        language:日本語 or 英語 (str)
    <出力>
        message:処理結果 (str)
    '''
    try:
        # Text To Speech
        if language == '日本語':
            tts =gTTS(text=str(sentences), lang='ja')
            tts.save(str(file_name)+'.mp3')
        else:
            tts =gTTS(text=str(sentences), lang='en')
            tts.save(str(file_name)+'.mp3')
        message = '新単語が生成されます'
    except PermissionError:
        message = '入力された単語からは新単語を生成できません'
    return message
    

if __name__ == '__main__':
    gui()