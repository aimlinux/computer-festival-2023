
import PySimpleGUI as sg 

def gui():
    #テーマ設定
    sg.theme('DarkAmber')
    
    layout = [
        [sg.text('創造性あふれる新たな文字を作成するアプリです.')], 
        [sg.Multiline('文字を入力して下さい. ', size=(30, 10), key='sentence')]
    ]
    
    window = sg.Window('Text Application', layout)
    
    while True:
        
        event, values = window.read()
        
        if event == 'bt': 
            
            sg.Popup(title='新単語結果！！')
            
        elif event == sg.WIN_CLOSED:
            break
    
    

    
if __name__ == '__main__':
    gui()