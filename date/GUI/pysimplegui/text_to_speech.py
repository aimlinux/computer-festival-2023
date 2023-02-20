
import PySimpleGUI as sg
from gtts import gTTS

def gui():
    # ウィンドウのテーマ
    sg.theme('DarkTeal1')
    
    # ウィンドウの内容を1列ずつ定義
    layout = [  [sg.Text('文章を音声に変換するアプリです')],     # テキスト設置
            [sg.Multiline('文章を入力してください', size=(80, 20), key='sentence')], # 文章入力欄を設置
                [sg.Text('出力ファイル名(.mp3)')],
                [sg.InputText(default_text='speech_file', size=(80, 1), key='file_name')], # 出力ファイル名を入力する
                [sg.Text('言語設定')],
                [sg.Spin(['日本語', '英語'], size=(10,1), initial_value='日本語', key='language')], # jaが日本語、enが英語
                [sg.Button('音声に変換する', key='bt')] ] # ボタンを設置
    # ウィンドウを作成する
    window = sg.Window('Text to Speech Application', layout)      # ウィンドウ定義

    while True:
        # ウィンドウを表示
        event, values = window.read()

        if event == 'bt': # ボタンを押したとき
            message = text_to_speech(values['sentence'], values['file_name'], values['language']) # Text to Speechを実施
            sg.Popup(message, title='音声変換結果') # 処理結果をポップアップでお知らせ
        
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
        message = '音声変換が終了しました'
    except PermissionError:
        message = 'ファイル出力が出来ませんでした。出力ファイル名を変更、もしくは音声の再生ウインドウが開いている場合は閉じてください。'
    return message
    

if __name__ == '__main__':
    gui()