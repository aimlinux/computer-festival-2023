# coding: utf-8
# *************************************************************************************
# * PysimpleGUI フォントの種類一覧
# *************************************************************************************
# *====================================================================================
# * インポートライブラリ
# *====================================================================================
# +-----------------------------------------------------------------------------------+
# + PySimpleGUI
# +-----------------------------------------------------------------------------------+
#(pip install pysimplegui)
import PySimpleGUI as sg

# +-----------------------------------------------------------------------------------+
# + クリップボード
# +-----------------------------------------------------------------------------------+
import pyperclip

# +-----------------------------------------------------------------------------------+
# + PyAutoGUI
# +-----------------------------------------------------------------------------------+
#(pip install pyautogui)
import pyautogui as pg

#-------------------------------------------------------------------------------------+
# スレッド処理
#-------------------------------------------------------------------------------------+
import threading

# *====================================================================================
# * GUI作成
# *====================================================================================
# +-----------------------------------------------------------------------------------+
# + スタイル設定
# +-----------------------------------------------------------------------------------+
sg.theme('Dark Blue 3')

# +-----------------------------------------------------------------------------------+
# + レイアウト設定
# +-----------------------------------------------------------------------------------+
tab1_layout = [
            [ sg.Submit(button_text='1フォント名：System 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('System',12),size=(400,1),key='button1')],
            [ sg.Submit(button_text='2フォント名：@System 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@System',12),size=(400,1),key='button2')],
            [ sg.Submit(button_text='3フォント名：Terminal 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Terminal',12),size=(400,1),key='button3')],
            [ sg.Submit(button_text='4フォント名：@Terminal 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Terminal',12),size=(400,1),key='button4')],
            [ sg.Submit(button_text='5フォント名：FixedSys 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('FixedSys',12),size=(400,1),key='button5')],
            [ sg.Submit(button_text='6フォント名：@FixedSys 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@FixedSys',12),size=(400,1),key='button6')],
            [ sg.Submit(button_text='7フォント名：Modern 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Modern',12),size=(400,1),key='button7')],
            [ sg.Submit(button_text='8フォント名：Roman 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Roman',12),size=(400,1),key='button8')],
            [ sg.Submit(button_text='9フォント名：Script 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Script',12),size=(400,1),key='button9')],
            [ sg.Submit(button_text='10フォント名：Courier 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier',12),size=(400,1),key='button10')],
            [ sg.Submit(button_text='11フォント名：MS Serif 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS Serif',12),size=(400,1),key='button11')],
            [ sg.Submit(button_text='12フォント名：MS Sans Serif 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS Sans Serif',12),size=(400,1),key='button12')],
            [ sg.Submit(button_text='13フォント名：Small Fonts 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Small Fonts',12),size=(400,1),key='button13')],
            [ sg.Submit(button_text='14フォント名：@Small Fonts 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Small Fonts',12),size=(400,1),key='button14')],
            [ sg.Submit(button_text='15フォント名：Marlett 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Marlett',12),size=(400,1),key='button15')],
            [ sg.Submit(button_text='16フォント名：Arial 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial',12),size=(400,1),key='button16')],
            [ sg.Submit(button_text='17フォント名：Arabic Transparent 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arabic Transparent',12),size=(400,1),key='button17')],
            [ sg.Submit(button_text='18フォント名：Arial Baltic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial Baltic',12),size=(400,1),key='button18')],
            [ sg.Submit(button_text='19フォント名：Arial CE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial CE',12),size=(400,1),key='button19')],
            [ sg.Submit(button_text='20フォント名：Arial CYR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial CYR',12),size=(400,1),key='button20')],
            [ sg.Submit(button_text='21フォント名：Arial Greek 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial Greek',12),size=(400,1),key='button21')],
            [ sg.Submit(button_text='22フォント名：Arial TUR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial TUR',12),size=(400,1),key='button22')],
            [ sg.Submit(button_text='23フォント名：Arial Black 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial Black',12),size=(400,1),key='button23')],
            [ sg.Submit(button_text='24フォント名：Bahnschrift Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift Light',12),size=(400,1),key='button24')],
            [ sg.Submit(button_text='25フォント名：Bahnschrift SemiLight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiLight',12),size=(400,1),key='button25')],
            [ sg.Submit(button_text='26フォント名：Bahnschrift 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift',12),size=(400,1),key='button26')],
            [ sg.Submit(button_text='27フォント名：Bahnschrift SemiBold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiBold',12),size=(400,1),key='button27')],
        ]

tab2_layout = [
            [ sg.Submit(button_text='28フォント名：Bahnschrift Light SemiCondensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift Light SemiCondensed',12),size=(400,1),key='button28')],
            [ sg.Submit(button_text='29フォント名：Bahnschrift SemiLight SemiConde 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiLight SemiConde',12),size=(400,1),key='button29')],
            [ sg.Submit(button_text='30フォント名：Bahnschrift SemiCondensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiCondensed',12),size=(400,1),key='button30')],
            [ sg.Submit(button_text='31フォント名：Bahnschrift SemiBold SemiConden 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiBold SemiConden',12),size=(400,1),key='button31')],
            [ sg.Submit(button_text='32フォント名：Bahnschrift Light Condensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift Light Condensed',12),size=(400,1),key='button32')],
            [ sg.Submit(button_text='33フォント名：Bahnschrift SemiLight Condensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiLight Condensed',12),size=(400,1),key='button33')],
            [ sg.Submit(button_text='34フォント名：Bahnschrift Condensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift Condensed',12),size=(400,1),key='button34')],
            [ sg.Submit(button_text='35フォント名：Bahnschrift SemiBold Condensed 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bahnschrift SemiBold Condensed',12),size=(400,1),key='button35')],
            [ sg.Submit(button_text='36フォント名：Calibri 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Calibri',12),size=(400,1),key='button36')],
            [ sg.Submit(button_text='37フォント名：Calibri Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Calibri Light',12),size=(400,1),key='button37')],
            [ sg.Submit(button_text='38フォント名：Cambria 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Cambria',12),size=(400,1),key='button38')],
            [ sg.Submit(button_text='39フォント名：Cambria Math 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Cambria Math',12),size=(400,1),key='button39')],
            [ sg.Submit(button_text='40フォント名：Candara 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Candara',12),size=(400,1),key='button40')],
            [ sg.Submit(button_text='41フォント名：Candara Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Candara Light',12),size=(400,1),key='button41')],
            [ sg.Submit(button_text='42フォント名：Comic Sans MS 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Comic Sans MS',12),size=(400,1),key='button42')],
            [ sg.Submit(button_text='43フォント名：Consolas 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Consolas',12),size=(400,1),key='button43')],
            [ sg.Submit(button_text='44フォント名：Constantia 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Constantia',12),size=(400,1),key='button44')],
            [ sg.Submit(button_text='45フォント名：Corbel 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Corbel',12),size=(400,1),key='button45')],
            [ sg.Submit(button_text='46フォント名：Corbel Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Corbel Light',12),size=(400,1),key='button46')],
            [ sg.Submit(button_text='47フォント名：Courier New 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New',12),size=(400,1),key='button47')],
            [ sg.Submit(button_text='48フォント名：Courier New Baltic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New Baltic',12),size=(400,1),key='button48')],
            [ sg.Submit(button_text='49フォント名：Courier New CE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New CE',12),size=(400,1),key='button49')],
            [ sg.Submit(button_text='50フォント名：Courier New CYR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New CYR',12),size=(400,1),key='button50')],
        ]

tab3_layout = [
            [ sg.Submit(button_text='51フォント名：Courier New Greek 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New Greek',12),size=(400,1),key='button51')],
            [ sg.Submit(button_text='52フォント名：Courier New TUR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Courier New TUR',12),size=(400,1),key='button52')],
            [ sg.Submit(button_text='53フォント名：Ebrima 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Ebrima',12),size=(400,1),key='button53')],
            [ sg.Submit(button_text='54フォント名：Franklin Gothic Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Franklin Gothic Medium',12),size=(400,1),key='button54')],
            [ sg.Submit(button_text='55フォント名：Gabriola 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Gabriola',12),size=(400,1),key='button55')],
            [ sg.Submit(button_text='56フォント名：Gadugi 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Gadugi',12),size=(400,1),key='button56')],
            [ sg.Submit(button_text='57フォント名：Georgia 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Georgia',12),size=(400,1),key='button57')],
            [ sg.Submit(button_text='58フォント名：Impact 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Impact',12),size=(400,1),key='button58')],
            [ sg.Submit(button_text='59フォント名：Ink Free 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Ink Free',12),size=(400,1),key='button59')],
            [ sg.Submit(button_text='60フォント名：Javanese Text 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Javanese Text',12),size=(400,1),key='button60')],
            [ sg.Submit(button_text='61フォント名：Leelawadee UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Leelawadee UI',12),size=(400,1),key='button61')],
            [ sg.Submit(button_text='62フォント名：Leelawadee UI Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Leelawadee UI Semilight',12),size=(400,1),key='button62')],
            [ sg.Submit(button_text='63フォント名：Lucida Console 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Lucida Console',12),size=(400,1),key='button63')],
            [ sg.Submit(button_text='64フォント名：Lucida Sans Unicode 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Lucida Sans Unicode',12),size=(400,1),key='button64')],
            [ sg.Submit(button_text='65フォント名：Malgun Gothic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Malgun Gothic',12),size=(400,1),key='button65')],
            [ sg.Submit(button_text='66フォント名：@Malgun Gothic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Malgun Gothic',12),size=(400,1),key='button66')],
            [ sg.Submit(button_text='67フォント名：Malgun Gothic Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Malgun Gothic Semilight',12),size=(400,1),key='button67')],
            [ sg.Submit(button_text='68フォント名：@Malgun Gothic Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Malgun Gothic Semilight',12),size=(400,1),key='button68')],
            [ sg.Submit(button_text='69フォント名：Microsoft Himalaya 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft Himalaya',12),size=(400,1),key='button69')],
            [ sg.Submit(button_text='70フォント名：Microsoft JhengHei 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft JhengHei',12),size=(400,1),key='button70')],
            [ sg.Submit(button_text='71フォント名：@Microsoft JhengHei 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft JhengHei',12),size=(400,1),key='button71')],
            [ sg.Submit(button_text='72フォント名：Microsoft JhengHei UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft JhengHei UI',12),size=(400,1),key='button72')],
            [ sg.Submit(button_text='73フォント名：@Microsoft JhengHei UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft JhengHei UI',12),size=(400,1),key='button73')],
            [ sg.Submit(button_text='74フォント名：Microsoft JhengHei Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft JhengHei Light',12),size=(400,1),key='button74')],
        ]

tab4_layout = [
            [ sg.Submit(button_text='75フォント名：@Microsoft JhengHei Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft JhengHei Light',12),size=(400,1),key='button75')],
            [ sg.Submit(button_text='76フォント名：Microsoft JhengHei UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft JhengHei UI Light',12),size=(400,1),key='button76')],
            [ sg.Submit(button_text='77フォント名：@Microsoft JhengHei UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft JhengHei UI Light',12),size=(400,1),key='button77')],
            [ sg.Submit(button_text='78フォント名：Microsoft New Tai Lue 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft New Tai Lue',12),size=(400,1),key='button78')],
            [ sg.Submit(button_text='79フォント名：Microsoft PhagsPa 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft PhagsPa',12),size=(400,1),key='button79')],
            [ sg.Submit(button_text='80フォント名：Microsoft Sans Serif 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft Sans Serif',12),size=(400,1),key='button80')],
            [ sg.Submit(button_text='81フォント名：Microsoft Tai Le 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft Tai Le',12),size=(400,1),key='button81')],
            [ sg.Submit(button_text='82フォント名：Microsoft YaHei 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft YaHei',12),size=(400,1),key='button82')],
            [ sg.Submit(button_text='83フォント名：@Microsoft YaHei 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft YaHei',12),size=(400,1),key='button83')],
            [ sg.Submit(button_text='84フォント名：Microsoft YaHei UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft YaHei UI',12),size=(400,1),key='button84')],
            [ sg.Submit(button_text='85フォント名：@Microsoft YaHei UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft YaHei UI',12),size=(400,1),key='button85')],
            [ sg.Submit(button_text='86フォント名：Microsoft YaHei Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft YaHei Light',12),size=(400,1),key='button86')],
            [ sg.Submit(button_text='87フォント名：@Microsoft YaHei Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft YaHei Light',12),size=(400,1),key='button87')],
            [ sg.Submit(button_text='88フォント名：Microsoft YaHei UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft YaHei UI Light',12),size=(400,1),key='button88')],
            [ sg.Submit(button_text='89フォント名：@Microsoft YaHei UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Microsoft YaHei UI Light',12),size=(400,1),key='button89')],
            [ sg.Submit(button_text='90フォント名：Microsoft Yi Baiti 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Microsoft Yi Baiti',12),size=(400,1),key='button90')],
            [ sg.Submit(button_text='91フォント名：MingLiU-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MingLiU-ExtB',12),size=(400,1),key='button91')],
            [ sg.Submit(button_text='92フォント名：@MingLiU-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@MingLiU-ExtB',12),size=(400,1),key='button92')],
            [ sg.Submit(button_text='93フォント名：PMingLiU-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('PMingLiU-ExtB',12),size=(400,1),key='button93')],
            [ sg.Submit(button_text='94フォント名：@PMingLiU-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@PMingLiU-ExtB',12),size=(400,1),key='button94')],
            [ sg.Submit(button_text='95フォント名：MingLiU_HKSCS-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MingLiU_HKSCS-ExtB',12),size=(400,1),key='button95')],
            [ sg.Submit(button_text='96フォント名：@MingLiU_HKSCS-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@MingLiU_HKSCS-ExtB',12),size=(400,1),key='button96')],
            [ sg.Submit(button_text='97フォント名：Mongolian Baiti 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Mongolian Baiti',12),size=(400,1),key='button97')],
            [ sg.Submit(button_text='98フォント名：ＭＳ ゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('ＭＳ ゴシック',12),size=(400,1),key='button98')],
            [ sg.Submit(button_text='99フォント名：@ＭＳ ゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@ＭＳ ゴシック',12),size=(400,1),key='button99')],
        ]

tab5_layout = [
            [ sg.Submit(button_text='100フォント名：MS UI Gothic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS UI Gothic',12),size=(400,1),key='button100')],
            [ sg.Submit(button_text='101フォント名：@MS UI Gothic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@MS UI Gothic',12),size=(400,1),key='button101')],
            [ sg.Submit(button_text='102フォント名：ＭＳ Ｐゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('ＭＳ Ｐゴシック',12),size=(400,1),key='button102')],
            [ sg.Submit(button_text='103フォント名：@ＭＳ Ｐゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@ＭＳ Ｐゴシック',12),size=(400,1),key='button103')],
            [ sg.Submit(button_text='104フォント名：MV Boli 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MV Boli',12),size=(400,1),key='button104')],
            [ sg.Submit(button_text='105フォント名：Myanmar Text 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Myanmar Text',12),size=(400,1),key='button105')],
            [ sg.Submit(button_text='106フォント名：Nirmala UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Nirmala UI',12),size=(400,1),key='button106')],
            [ sg.Submit(button_text='107フォント名：Nirmala UI Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Nirmala UI Semilight',12),size=(400,1),key='button107')],
            [ sg.Submit(button_text='108フォント名：Palatino Linotype 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Palatino Linotype',12),size=(400,1),key='button108')],
            [ sg.Submit(button_text='109フォント名：Segoe MDL2 Assets 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe MDL2 Assets',12),size=(400,1),key='button109')],
            [ sg.Submit(button_text='110フォント名：Segoe Print 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe Print',12),size=(400,1),key='button110')],
            [ sg.Submit(button_text='111フォント名：Segoe Script 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe Script',12),size=(400,1),key='button111')],
            [ sg.Submit(button_text='112フォント名：Segoe UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI',12),size=(400,1),key='button112')],
            [ sg.Submit(button_text='113フォント名：Segoe UI Black 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Black',12),size=(400,1),key='button113')],
            [ sg.Submit(button_text='114フォント名：Segoe UI Emoji 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Emoji',12),size=(400,1),key='button114')],
            [ sg.Submit(button_text='115フォント名：Segoe UI Historic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Historic',12),size=(400,1),key='button115')],
            [ sg.Submit(button_text='116フォント名：Segoe UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Light',12),size=(400,1),key='button116')],
            [ sg.Submit(button_text='117フォント名：Segoe UI Semibold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Semibold',12),size=(400,1),key='button117')],
            [ sg.Submit(button_text='118フォント名：Segoe UI Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Semilight',12),size=(400,1),key='button118')],
            [ sg.Submit(button_text='119フォント名：Segoe UI Symbol 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Segoe UI Symbol',12),size=(400,1),key='button119')],
            [ sg.Submit(button_text='120フォント名：SimSun 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('SimSun',12),size=(400,1),key='button120')],
            [ sg.Submit(button_text='121フォント名：@SimSun 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@SimSun',12),size=(400,1),key='button121')],
            [ sg.Submit(button_text='122フォント名：NSimSun 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('NSimSun',12),size=(400,1),key='button122')],
            [ sg.Submit(button_text='123フォント名：@NSimSun 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@NSimSun',12),size=(400,1),key='button123')],
        ]

tab6_layout = [
            [ sg.Submit(button_text='124フォント名：SimSun-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('SimSun-ExtB',12),size=(400,1),key='button124')],
            [ sg.Submit(button_text='125フォント名：@SimSun-ExtB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@SimSun-ExtB',12),size=(400,1),key='button125')],
            [ sg.Submit(button_text='126フォント名：Sitka Small 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Small',12),size=(400,1),key='button126')],
            [ sg.Submit(button_text='127フォント名：Sitka Text 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Text',12),size=(400,1),key='button127')],
            [ sg.Submit(button_text='128フォント名：Sitka Subheading 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Subheading',12),size=(400,1),key='button128')],
            [ sg.Submit(button_text='129フォント名：Sitka Heading 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Heading',12),size=(400,1),key='button129')],
            [ sg.Submit(button_text='130フォント名：Sitka Display 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Display',12),size=(400,1),key='button130')],
            [ sg.Submit(button_text='131フォント名：Sitka Banner 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sitka Banner',12),size=(400,1),key='button131')],
            [ sg.Submit(button_text='132フォント名：Sylfaen 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Sylfaen',12),size=(400,1),key='button132')],
            [ sg.Submit(button_text='133フォント名：Symbol 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Symbol',12),size=(400,1),key='button133')],
            [ sg.Submit(button_text='134フォント名：Tahoma 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Tahoma',12),size=(400,1),key='button134')],
            [ sg.Submit(button_text='135フォント名：Times New Roman 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman',12),size=(400,1),key='button135')],
            [ sg.Submit(button_text='136フォント名：Times New Roman Baltic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman Baltic',12),size=(400,1),key='button136')],
            [ sg.Submit(button_text='137フォント名：Times New Roman CE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman CE',12),size=(400,1),key='button137')],
            [ sg.Submit(button_text='138フォント名：Times New Roman CYR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman CYR',12),size=(400,1),key='button138')],
            [ sg.Submit(button_text='139フォント名：Times New Roman Greek 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman Greek',12),size=(400,1),key='button139')],
            [ sg.Submit(button_text='140フォント名：Times New Roman TUR 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Times New Roman TUR',12),size=(400,1),key='button140')],
            [ sg.Submit(button_text='141フォント名：Trebuchet MS 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Trebuchet MS',12),size=(400,1),key='button141')],
            [ sg.Submit(button_text='142フォント名：Verdana 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Verdana',12),size=(400,1),key='button142')],
            [ sg.Submit(button_text='143フォント名：Webdings 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Webdings',12),size=(400,1),key='button143')],
            [ sg.Submit(button_text='144フォント名：Wingdings 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Wingdings',12),size=(400,1),key='button144')],
            [ sg.Submit(button_text='145フォント名：游ゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游ゴシック',12),size=(400,1),key='button145')],
            [ sg.Submit(button_text='146フォント名：@游ゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游ゴシック',12),size=(400,1),key='button146')],
            [ sg.Submit(button_text='147フォント名：Yu Gothic UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Yu Gothic UI',12),size=(400,1),key='button147')],
            [ sg.Submit(button_text='148フォント名：@Yu Gothic UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Yu Gothic UI',12),size=(400,1),key='button148')],
        ]

tab7_layout = [
            [ sg.Submit(button_text='149フォント名：Yu Gothic UI Semibold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Yu Gothic UI Semibold',12),size=(400,1),key='button149')],
            [ sg.Submit(button_text='150フォント名：@Yu Gothic UI Semibold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Yu Gothic UI Semibold',12),size=(400,1),key='button150')],
            [ sg.Submit(button_text='151フォント名：游ゴシック Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游ゴシック Light',12),size=(400,1),key='button151')],
            [ sg.Submit(button_text='152フォント名：@游ゴシック Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游ゴシック Light',12),size=(400,1),key='button152')],
            [ sg.Submit(button_text='153フォント名：Yu Gothic UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Yu Gothic UI Light',12),size=(400,1),key='button153')],
            [ sg.Submit(button_text='154フォント名：@Yu Gothic UI Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Yu Gothic UI Light',12),size=(400,1),key='button154')],
            [ sg.Submit(button_text='155フォント名：游ゴシック Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游ゴシック Medium',12),size=(400,1),key='button155')],
            [ sg.Submit(button_text='156フォント名：@游ゴシック Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游ゴシック Medium',12),size=(400,1),key='button156')],
            [ sg.Submit(button_text='157フォント名：Yu Gothic UI Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Yu Gothic UI Semilight',12),size=(400,1),key='button157')],
            [ sg.Submit(button_text='158フォント名：@Yu Gothic UI Semilight 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Yu Gothic UI Semilight',12),size=(400,1),key='button158')],
            [ sg.Submit(button_text='159フォント名：BIZ UDゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('BIZ UDゴシック',12),size=(400,1),key='button159')],
            [ sg.Submit(button_text='160フォント名：@BIZ UDゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@BIZ UDゴシック',12),size=(400,1),key='button160')],
            [ sg.Submit(button_text='161フォント名：BIZ UDPゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('BIZ UDPゴシック',12),size=(400,1),key='button161')],
            [ sg.Submit(button_text='162フォント名：@BIZ UDPゴシック 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@BIZ UDPゴシック',12),size=(400,1),key='button162')],
            [ sg.Submit(button_text='163フォント名：BIZ UD明朝 Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('BIZ UD明朝 Medium',12),size=(400,1),key='button163')],
            [ sg.Submit(button_text='164フォント名：@BIZ UD明朝 Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@BIZ UD明朝 Medium',12),size=(400,1),key='button164')],
            [ sg.Submit(button_text='165フォント名：BIZ UDP明朝 Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('BIZ UDP明朝 Medium',12),size=(400,1),key='button165')],
            [ sg.Submit(button_text='166フォント名：@BIZ UDP明朝 Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@BIZ UDP明朝 Medium',12),size=(400,1),key='button166')],
            [ sg.Submit(button_text='167フォント名：メイリオ 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('メイリオ',12),size=(400,1),key='button167')],
            [ sg.Submit(button_text='168フォント名：@メイリオ 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@メイリオ',12),size=(400,1),key='button168')],
            [ sg.Submit(button_text='169フォント名：Meiryo UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Meiryo UI',12),size=(400,1),key='button169')],
            [ sg.Submit(button_text='170フォント名：@Meiryo UI 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Meiryo UI',12),size=(400,1),key='button170')],
            [ sg.Submit(button_text='171フォント名：ＭＳ 明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('ＭＳ 明朝',12),size=(400,1),key='button171')],
            [ sg.Submit(button_text='172フォント名：@ＭＳ 明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@ＭＳ 明朝',12),size=(400,1),key='button172')],
            [ sg.Submit(button_text='173フォント名：ＭＳ Ｐ明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('ＭＳ Ｐ明朝',12),size=(400,1),key='button173')],
            [ sg.Submit(button_text='174フォント名：@ＭＳ Ｐ明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@ＭＳ Ｐ明朝',12),size=(400,1),key='button174')],
        ]

tab8_layout = [
            [ sg.Submit(button_text='175フォント名：UD デジタル 教科書体 N-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 N-B',12),size=(400,1),key='button175')],
            [ sg.Submit(button_text='176フォント名：@UD デジタル 教科書体 N-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 N-B',12),size=(400,1),key='button176')],
            [ sg.Submit(button_text='177フォント名：UD デジタル 教科書体 NP-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 NP-B',12),size=(400,1),key='button177')],
            [ sg.Submit(button_text='178フォント名：@UD デジタル 教科書体 NP-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 NP-B',12),size=(400,1),key='button178')],
            [ sg.Submit(button_text='179フォント名：UD デジタル 教科書体 NK-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 NK-B',12),size=(400,1),key='button179')],
            [ sg.Submit(button_text='180フォント名：@UD デジタル 教科書体 NK-B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 NK-B',12),size=(400,1),key='button180')],
            [ sg.Submit(button_text='181フォント名：UD デジタル 教科書体 N-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 N-R',12),size=(400,1),key='button181')],
            [ sg.Submit(button_text='182フォント名：@UD デジタル 教科書体 N-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 N-R',12),size=(400,1),key='button182')],
            [ sg.Submit(button_text='183フォント名：UD デジタル 教科書体 NP-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 NP-R',12),size=(400,1),key='button183')],
            [ sg.Submit(button_text='184フォント名：@UD デジタル 教科書体 NP-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 NP-R',12),size=(400,1),key='button184')],
            [ sg.Submit(button_text='185フォント名：UD デジタル 教科書体 NK-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('UD デジタル 教科書体 NK-R',12),size=(400,1),key='button185')],
            [ sg.Submit(button_text='186フォント名：@UD デジタル 教科書体 NK-R 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@UD デジタル 教科書体 NK-R',12),size=(400,1),key='button186')],
            [ sg.Submit(button_text='187フォント名：游明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游明朝',12),size=(400,1),key='button187')],
            [ sg.Submit(button_text='188フォント名：@游明朝 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游明朝',12),size=(400,1),key='button188')],
            [ sg.Submit(button_text='189フォント名：游明朝 Demibold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游明朝 Demibold',12),size=(400,1),key='button189')],
            [ sg.Submit(button_text='190フォント名：@游明朝 Demibold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游明朝 Demibold',12),size=(400,1),key='button190')],
            [ sg.Submit(button_text='191フォント名：游明朝 Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('游明朝 Light',12),size=(400,1),key='button191')],
            [ sg.Submit(button_text='192フォント名：@游明朝 Light 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@游明朝 Light',12),size=(400,1),key='button192')],
            [ sg.Submit(button_text='193フォント名：HoloLens MDL2 Assets 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HoloLens MDL2 Assets',12),size=(400,1),key='button193')],
            [ sg.Submit(button_text='194フォント名：HGｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGｺﾞｼｯｸE',12),size=(400,1),key='button194')],
            [ sg.Submit(button_text='195フォント名：@HGｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGｺﾞｼｯｸE',12),size=(400,1),key='button195')],
            [ sg.Submit(button_text='196フォント名：HGPｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGPｺﾞｼｯｸE',12),size=(400,1),key='button196')],
            [ sg.Submit(button_text='197フォント名：@HGPｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGPｺﾞｼｯｸE',12),size=(400,1),key='button197')],
            [ sg.Submit(button_text='198フォント名：HGSｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGSｺﾞｼｯｸE',12),size=(400,1),key='button198')],
            [ sg.Submit(button_text='199フォント名：@HGSｺﾞｼｯｸE 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGSｺﾞｼｯｸE',12),size=(400,1),key='button199')],
            [ sg.Submit(button_text='200フォント名：HGｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGｺﾞｼｯｸM',12),size=(400,1),key='button200')],
            [ sg.Submit(button_text='201フォント名：@HGｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGｺﾞｼｯｸM',12),size=(400,1),key='button201')],
            [ sg.Submit(button_text='202フォント名：HGPｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGPｺﾞｼｯｸM',12),size=(400,1),key='button202')],
        ]

tab9_layout = [

            [ sg.Submit(button_text='203フォント名：@HGPｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGPｺﾞｼｯｸM',12),size=(400,1),key='button203')],
            [ sg.Submit(button_text='204フォント名：HGSｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGSｺﾞｼｯｸM',12),size=(400,1),key='button204')],
            [ sg.Submit(button_text='205フォント名：@HGSｺﾞｼｯｸM 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGSｺﾞｼｯｸM',12),size=(400,1),key='button205')],
            [ sg.Submit(button_text='206フォント名：HG行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG行書体',12),size=(400,1),key='button206')],
            [ sg.Submit(button_text='207フォント名：@HG行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG行書体',12),size=(400,1),key='button207')],
            [ sg.Submit(button_text='208フォント名：HGP行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP行書体',12),size=(400,1),key='button208')],
            [ sg.Submit(button_text='209フォント名：@HGP行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP行書体',12),size=(400,1),key='button209')],
            [ sg.Submit(button_text='210フォント名：HGS行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS行書体',12),size=(400,1),key='button210')],
            [ sg.Submit(button_text='211フォント名：@HGS行書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS行書体',12),size=(400,1),key='button211')],
            [ sg.Submit(button_text='212フォント名：HG教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG教科書体',12),size=(400,1),key='button212')],
            [ sg.Submit(button_text='213フォント名：@HG教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG教科書体',12),size=(400,1),key='button213')],
            [ sg.Submit(button_text='214フォント名：HGP教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP教科書体',12),size=(400,1),key='button214')],
            [ sg.Submit(button_text='215フォント名：@HGP教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP教科書体',12),size=(400,1),key='button215')],
            [ sg.Submit(button_text='216フォント名：HGS教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS教科書体',12),size=(400,1),key='button216')],
            [ sg.Submit(button_text='217フォント名：@HGS教科書体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS教科書体',12),size=(400,1),key='button217')],
            [ sg.Submit(button_text='218フォント名：HG明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG明朝B',12),size=(400,1),key='button218')],
            [ sg.Submit(button_text='219フォント名：@HG明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG明朝B',12),size=(400,1),key='button219')],
            [ sg.Submit(button_text='220フォント名：HGP明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP明朝B',12),size=(400,1),key='button220')],
            [ sg.Submit(button_text='221フォント名：@HGP明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP明朝B',12),size=(400,1),key='button221')],
            [ sg.Submit(button_text='222フォント名：HGS明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS明朝B',12),size=(400,1),key='button222')],
            [ sg.Submit(button_text='223フォント名：@HGS明朝B 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS明朝B',12),size=(400,1),key='button223')],
            [ sg.Submit(button_text='224フォント名：HG明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG明朝E',12),size=(400,1),key='button224')],
            [ sg.Submit(button_text='225フォント名：@HG明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG明朝E',12),size=(400,1),key='button225')],
            [ sg.Submit(button_text='226フォント名：HGP明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP明朝E',12),size=(400,1),key='button226')],
            [ sg.Submit(button_text='227フォント名：@HGP明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP明朝E',12),size=(400,1),key='button227')],
            [ sg.Submit(button_text='228フォント名：HGS明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS明朝E',12),size=(400,1),key='button228')],
            [ sg.Submit(button_text='229フォント名：@HGS明朝E 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS明朝E',12),size=(400,1),key='button229')],
            [ sg.Submit(button_text='230フォント名：HG創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button230')],
            [ sg.Submit(button_text='231フォント名：@HG創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button231')],
            [ sg.Submit(button_text='232フォント名：HGP創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button232')],
        ]

tab10_layout = [
                        [ sg.Submit(button_text='233フォント名：@HGP創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button233')],
            [ sg.Submit(button_text='234フォント名：HGS創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button234')],
            [ sg.Submit(button_text='235フォント名：@HGS創英角ﾎﾟｯﾌﾟ体 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS創英角ﾎﾟｯﾌﾟ体',12),size=(400,1),key='button235')],
            [ sg.Submit(button_text='236フォント名：HG創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button236')],
            [ sg.Submit(button_text='237フォント名：@HG創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button237')],
            [ sg.Submit(button_text='238フォント名：HGP創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button238')],
            [ sg.Submit(button_text='239フォント名：@HGP創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button239')],
            [ sg.Submit(button_text='240フォント名：HGS創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button240')],
            [ sg.Submit(button_text='241フォント名：@HGS創英ﾌﾟﾚｾﾞﾝｽEB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS創英ﾌﾟﾚｾﾞﾝｽEB',12),size=(400,1),key='button241')],
            [ sg.Submit(button_text='242フォント名：HG創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button242')],
            [ sg.Submit(button_text='243フォント名：@HG創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button243')],
            [ sg.Submit(button_text='244フォント名：HGP創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGP創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button244')],
            [ sg.Submit(button_text='245フォント名：@HGP創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGP創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button245')],
            [ sg.Submit(button_text='246フォント名：HGS創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HGS創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button246')],
            [ sg.Submit(button_text='247フォント名：@HGS創英角ｺﾞｼｯｸUB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HGS創英角ｺﾞｼｯｸUB',12),size=(400,1),key='button247')],
            [ sg.Submit(button_text='248フォント名：HG正楷書体-PRO 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG正楷書体-PRO',12),size=(400,1),key='button248')],
            [ sg.Submit(button_text='249フォント名：@HG正楷書体-PRO 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG正楷書体-PRO',12),size=(400,1),key='button249')],
            [ sg.Submit(button_text='250フォント名：HG丸ｺﾞｼｯｸM-PRO 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('HG丸ｺﾞｼｯｸM-PRO',12),size=(400,1),key='button250')],
            [ sg.Submit(button_text='251フォント名：@HG丸ｺﾞｼｯｸM-PRO 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@HG丸ｺﾞｼｯｸM-PRO',12),size=(400,1),key='button251')],
            [ sg.Submit(button_text='252フォント名：OCRB 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('OCRB',12),size=(400,1),key='button252')],
            [ sg.Submit(button_text='253フォント名：Book Antiqua 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Book Antiqua',12),size=(400,1),key='button253')],
            [ sg.Submit(button_text='254フォント名：Arial Narrow 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial Narrow',12),size=(400,1),key='button254')],
            [ sg.Submit(button_text='255フォント名：Arial Unicode MS 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Arial Unicode MS',12),size=(400,1),key='button255')],
            [ sg.Submit(button_text='256フォント名：@Arial Unicode MS 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Arial Unicode MS',12),size=(400,1),key='button256')],
            [ sg.Submit(button_text='257フォント名：Bookman Old Style 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bookman Old Style',12),size=(400,1),key='button257')],
            [ sg.Submit(button_text='258フォント名：Bradley Hand ITC 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bradley Hand ITC',12),size=(400,1),key='button258')],
            [ sg.Submit(button_text='259フォント名：Bookshelf Symbol 7 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Bookshelf Symbol 7',12),size=(400,1),key='button259')],
            [ sg.Submit(button_text='260フォント名：Century 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Century',12),size=(400,1),key='button260')],
        ]
tab11_layout = [
            [ sg.Submit(button_text='261フォント名：Freestyle Script 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Freestyle Script',12),size=(400,1),key='button261')],
            [ sg.Submit(button_text='262フォント名：French Script MT 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('French Script MT',12),size=(400,1),key='button262')],
            [ sg.Submit(button_text='263フォント名：Garamond 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Garamond',12),size=(400,1),key='button263')],
            [ sg.Submit(button_text='264フォント名：Century Gothic 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Century Gothic',12),size=(400,1),key='button264')],
            [ sg.Submit(button_text='265フォント名：Kristen ITC 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Kristen ITC',12),size=(400,1),key='button265')],
            [ sg.Submit(button_text='266フォント名：Juice ITC 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Juice ITC',12),size=(400,1),key='button266')],
            [ sg.Submit(button_text='267フォント名：Lucida Handwriting 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Lucida Handwriting',12),size=(400,1),key='button267')],
            [ sg.Submit(button_text='268フォント名：Mistral 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Mistral',12),size=(400,1),key='button268')],
            [ sg.Submit(button_text='269フォント名：Monotype Corsiva 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Monotype Corsiva',12),size=(400,1),key='button269')],
            [ sg.Submit(button_text='270フォント名：MT Extra 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MT Extra',12),size=(400,1),key='button270')],
            [ sg.Submit(button_text='271フォント名：MS Outlook 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS Outlook',12),size=(400,1),key='button271')],
            [ sg.Submit(button_text='272フォント名：Papyrus 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Papyrus',12),size=(400,1),key='button272')],
            [ sg.Submit(button_text='273フォント名：Pristina 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Pristina',12),size=(400,1),key='button273')],
            [ sg.Submit(button_text='274フォント名：MS Reference Sans Serif 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS Reference Sans Serif',12),size=(400,1),key='button274')],
            [ sg.Submit(button_text='275フォント名：MS Reference Specialty 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('MS Reference Specialty',12),size=(400,1),key='button275')],
            [ sg.Submit(button_text='276フォント名：Tempus Sans ITC 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Tempus Sans ITC',12),size=(400,1),key='button276')],
            [ sg.Submit(button_text='277フォント名：Wingdings 2 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Wingdings 2',12),size=(400,1),key='button277')],
            [ sg.Submit(button_text='278フォント名：Wingdings 3 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Wingdings 3',12),size=(400,1),key='button278')],
            [ sg.Submit(button_text='279フォント名：Rounded Mplus 1c Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Rounded Mplus 1c Medium',12),size=(400,1),key='button279')],
            [ sg.Submit(button_text='280フォント名：@Rounded Mplus 1c Medium 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Rounded Mplus 1c Medium',12),size=(400,1),key='button280')],
            [ sg.Submit(button_text='281フォント名：Rounded Mplus 1c Bold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('Rounded Mplus 1c Bold',12),size=(400,1),key='button281')],
            [ sg.Submit(button_text='282フォント名：@Rounded Mplus 1c Bold 01234 あいうえお アイウエオ ｱｲｳｴｵ ABCDEFG abcdefg',font=('@Rounded Mplus 1c Bold',12),size=(400,1),key='button282')],
        ]

layout = [
        [ sg.TabGroup([[sg.Tab('リスト01', tab1_layout),
                        sg.Tab('リスト02', tab2_layout),
                        sg.Tab('リスト03', tab3_layout),
                        sg.Tab('リスト04', tab4_layout),
                        sg.Tab('リスト05', tab5_layout),
                        sg.Tab('リスト06', tab6_layout),
                        sg.Tab('リスト07', tab7_layout),
                        sg.Tab('リスト08', tab8_layout),
                        sg.Tab('リスト09', tab9_layout),
                        sg.Tab('リスト10', tab10_layout),
                        sg.Tab('リスト11', tab11_layout),
                        ]]) ],
        ]

# +-----------------------------------------------------------------------------------+
# + ウィンドウ作成
# +-----------------------------------------------------------------------------------+
window = sg.Window('PysimpleGui & tkinter 使用可能 フォント一覧',layout,size=(1000,1000))

# *====================================================================================
# * プログラム開始
# *====================================================================================
# +-----------------------------------------------------------------------------------+
# + GUIループ
# +-----------------------------------------------------------------------------------+
while True:
    event, values = window.read()
        
    if event is None:
        break

    if event == "button1":
        print('System')
        pyperclip.copy('System')
    if event == "button2":
        print('@System')
        pyperclip.copy('@System')
    if event == "button3":
        print('Terminal')
        pyperclip.copy('Terminal')
    if event == "button4":
        print('@Terminal')
        pyperclip.copy('@Terminal')
    if event == "button5":
        print('FixedSys')
        pyperclip.copy('FixedSys')
    if event == "button6":
        print('@FixedSys')
        pyperclip.copy('@FixedSys')
    if event == "button7":
        print('Modern')
        pyperclip.copy('Modern')
    if event == "button8":
        print('Roman')
        pyperclip.copy('Roman')
    if event == "button9":
        print('Script')
        pyperclip.copy('Script')
    if event == "button10":
        print('Courier')
        pyperclip.copy('Courier')
    if event == "button11":
        print('MS Serif')
        pyperclip.copy('MS Serif')
    if event == "button12":
        print('MS Sans Serif')
        pyperclip.copy('MS Sans Serif')
    if event == "button13":
        print('Small Fonts')
        pyperclip.copy('Small Fonts')
    if event == "button14":
        print('@Small Fonts')
        pyperclip.copy('@Small Fonts')
    if event == "button15":
        print('Marlett')
        pyperclip.copy('Marlett')
    if event == "button16":
        print('Arial')
        pyperclip.copy('Arial')
    if event == "button17":
        print('Arabic Transparent')
        pyperclip.copy('Arabic Transparent')
    if event == "button18":
        print('Arial Baltic')
        pyperclip.copy('Arial Baltic')
    if event == "button19":
        print('Arial CE')
        pyperclip.copy('Arial CE')
    if event == "button20":
        print('Arial CYR')
        pyperclip.copy('Arial CYR')
    if event == "button21":
        print('Arial Greek')
        pyperclip.copy('Arial Greek')
    if event == "button22":
        print('Arial TUR')
        pyperclip.copy('Arial TUR')
    if event == "button23":
        print('Arial Black')
        pyperclip.copy('Arial Black')
    if event == "button24":
        print('Bahnschrift Light')
        pyperclip.copy('Bahnschrift Light')
    if event == "button25":
        print('Bahnschrift SemiLight')
        pyperclip.copy('Bahnschrift SemiLight')
    if event == "button26":
        print('Bahnschrift')
        pyperclip.copy('Bahnschrift')
    if event == "button27":
        print('Bahnschrift SemiBold')
        pyperclip.copy('Bahnschrift SemiBold')
    if event == "button28":
        print('Bahnschrift Light SemiCondensed')
        pyperclip.copy('Bahnschrift Light SemiCondensed')
    if event == "button29":
        print('Bahnschrift SemiLight SemiConde')
        pyperclip.copy('Bahnschrift SemiLight SemiConde')
    if event == "button30":
        print('Bahnschrift SemiCondensed')
        pyperclip.copy('Bahnschrift SemiCondensed')
    if event == "button31":
        print('Bahnschrift SemiBold SemiConden')
        pyperclip.copy('Bahnschrift SemiBold SemiConden')
    if event == "button32":
        print('Bahnschrift Light Condensed')
        pyperclip.copy('Bahnschrift Light Condensed')
    if event == "button33":
        print('Bahnschrift SemiLight Condensed')
        pyperclip.copy('Bahnschrift SemiLight Condensed')
    if event == "button34":
        print('Bahnschrift Condensed')
        pyperclip.copy('Bahnschrift Condensed')
    if event == "button35":
        print('Bahnschrift SemiBold Condensed')
        pyperclip.copy('Bahnschrift SemiBold Condensed')
    if event == "button36":
        print('Calibri')
        pyperclip.copy('Calibri')
    if event == "button37":
        print('Calibri Light')
        pyperclip.copy('Calibri Light')
    if event == "button38":
        print('Cambria')
        pyperclip.copy('Cambria')
    if event == "button39":
        print('Cambria Math')
        pyperclip.copy('Cambria Math')
    if event == "button40":
        print('Candara')
        pyperclip.copy('Candara')
    if event == "button41":
        print('Candara Light')
        pyperclip.copy('Candara Light')
    if event == "button42":
        print('Comic Sans MS')
        pyperclip.copy('Comic Sans MS')
    if event == "button43":
        print('Consolas')
        pyperclip.copy('Consolas')
    if event == "button44":
        print('Constantia')
        pyperclip.copy('Constantia')
    if event == "button45":
        print('Corbel')
        pyperclip.copy('Corbel')
    if event == "button46":
        print('Corbel Light')
        pyperclip.copy('Corbel Light')
    if event == "button47":
        print('Courier New')
        pyperclip.copy('Courier New')
    if event == "button48":
        print('Courier New Baltic')
        pyperclip.copy('Courier New Baltic')
    if event == "button49":
        print('Courier New CE')
        pyperclip.copy('Courier New CE')
    if event == "button50":
        print('Courier New CYR')
        pyperclip.copy('Courier New CYR')
    if event == "button51":
        print('Courier New Greek')
        pyperclip.copy('Courier New Greek')
    if event == "button52":
        print('Courier New TUR')
        pyperclip.copy('Courier New TUR')
    if event == "button53":
        print('Ebrima')
        pyperclip.copy('Ebrima')
    if event == "button54":
        print('Franklin Gothic Medium')
        pyperclip.copy('Franklin Gothic Medium')
    if event == "button55":
        print('Gabriola')
        pyperclip.copy('Gabriola')
    if event == "button56":
        print('Gadugi')
        pyperclip.copy('Gadugi')
    if event == "button57":
        print('Georgia')
        pyperclip.copy('Georgia')
    if event == "button58":
        print('Impact')
        pyperclip.copy('Impact')
    if event == "button59":
        print('Ink Free')
        pyperclip.copy('Ink Free')
    if event == "button60":
        print('Javanese Text')
        pyperclip.copy('Javanese Text')
    if event == "button61":
        print('Leelawadee UI')
        pyperclip.copy('Leelawadee UI')
    if event == "button62":
        print('Leelawadee UI Semilight')
        pyperclip.copy('Leelawadee UI Semilight')
    if event == "button63":
        print('Lucida Console')
        pyperclip.copy('Lucida Console')
    if event == "button64":
        print('Lucida Sans Unicode')
        pyperclip.copy('Lucida Sans Unicode')
    if event == "button65":
        print('Malgun Gothic')
        pyperclip.copy('Malgun Gothic')
    if event == "button66":
        print('@Malgun Gothic')
        pyperclip.copy('@Malgun Gothic')
    if event == "button67":
        print('Malgun Gothic Semilight')
        pyperclip.copy('Malgun Gothic Semilight')
    if event == "button68":
        print('@Malgun Gothic Semilight')
        pyperclip.copy('@Malgun Gothic Semilight')
    if event == "button69":
        print('Microsoft Himalaya')
        pyperclip.copy('Microsoft Himalaya')
    if event == "button70":
        print('Microsoft JhengHei')
        pyperclip.copy('Microsoft JhengHei')
    if event == "button71":
        print('@Microsoft JhengHei')
        pyperclip.copy('@Microsoft JhengHei')
    if event == "button72":
        print('Microsoft JhengHei UI')
        pyperclip.copy('Microsoft JhengHei UI')
    if event == "button73":
        print('@Microsoft JhengHei UI')
        pyperclip.copy('@Microsoft JhengHei UI')
    if event == "button74":
        print('Microsoft JhengHei Light')
        pyperclip.copy('Microsoft JhengHei Light')
    if event == "button75":
        print('@Microsoft JhengHei Light')
        pyperclip.copy('@Microsoft JhengHei Light')
    if event == "button76":
        print('Microsoft JhengHei UI Light')
        pyperclip.copy('Microsoft JhengHei UI Light')
    if event == "button77":
        print('@Microsoft JhengHei UI Light')
        pyperclip.copy('@Microsoft JhengHei UI Light')
    if event == "button78":
        print('Microsoft New Tai Lue')
        pyperclip.copy('Microsoft New Tai Lue')
    if event == "button79":
        print('Microsoft PhagsPa')
        pyperclip.copy('Microsoft PhagsPa')
    if event == "button80":
        print('Microsoft Sans Serif')
        pyperclip.copy('Microsoft Sans Serif')
    if event == "button81":
        print('Microsoft Tai Le')
        pyperclip.copy('Microsoft Tai Le')
    if event == "button82":
        print('Microsoft YaHei')
        pyperclip.copy('Microsoft YaHei')
    if event == "button83":
        print('@Microsoft YaHei')
        pyperclip.copy('@Microsoft YaHei')
    if event == "button84":
        print('Microsoft YaHei UI')
        pyperclip.copy('Microsoft YaHei UI')
    if event == "button85":
        print('@Microsoft YaHei UI')
        pyperclip.copy('@Microsoft YaHei UI')
    if event == "button86":
        print('Microsoft YaHei Light')
        pyperclip.copy('Microsoft YaHei Light')
    if event == "button87":
        print('@Microsoft YaHei Light')
        pyperclip.copy('@Microsoft YaHei Light')
    if event == "button88":
        print('Microsoft YaHei UI Light')
        pyperclip.copy('Microsoft YaHei UI Light')
    if event == "button89":
        print('@Microsoft YaHei UI Light')
        pyperclip.copy('@Microsoft YaHei UI Light')
    if event == "button90":
        print('Microsoft Yi Baiti')
        pyperclip.copy('Microsoft Yi Baiti')
    if event == "button91":
        print('MingLiU-ExtB')
        pyperclip.copy('MingLiU-ExtB')
    if event == "button92":
        print('@MingLiU-ExtB')
        pyperclip.copy('@MingLiU-ExtB')
    if event == "button93":
        print('PMingLiU-ExtB')
        pyperclip.copy('PMingLiU-ExtB')
    if event == "button94":
        print('@PMingLiU-ExtB')
        pyperclip.copy('@PMingLiU-ExtB')
    if event == "button95":
        print('MingLiU_HKSCS-ExtB')
        pyperclip.copy('MingLiU_HKSCS-ExtB')
    if event == "button96":
        print('@MingLiU_HKSCS-ExtB')
        pyperclip.copy('@MingLiU_HKSCS-ExtB')
    if event == "button97":
        print('Mongolian Baiti')
        pyperclip.copy('Mongolian Baiti')
    if event == "button98":
        print('ＭＳ ゴシック')
        pyperclip.copy('ＭＳ ゴシック')
    if event == "button99":
        print('@ＭＳ ゴシック')
        pyperclip.copy('@ＭＳ ゴシック')
    if event == "button100":
        print('MS UI Gothic')
        pyperclip.copy('MS UI Gothic')
    if event == "button101":
        print('@MS UI Gothic')
        pyperclip.copy('@MS UI Gothic')
    if event == "button102":
        print('ＭＳ Ｐゴシック')
        pyperclip.copy('ＭＳ Ｐゴシック')
    if event == "button103":
        print('@ＭＳ Ｐゴシック')
        pyperclip.copy('@ＭＳ Ｐゴシック')
    if event == "button104":
        print('MV Boli')
        pyperclip.copy('MV Boli')
    if event == "button105":
        print('Myanmar Text')
        pyperclip.copy('Myanmar Text')
    if event == "button106":
        print('Nirmala UI')
        pyperclip.copy('Nirmala UI')
    if event == "button107":
        print('Nirmala UI Semilight')
        pyperclip.copy('Nirmala UI Semilight')
    if event == "button108":
        print('Palatino Linotype')
        pyperclip.copy('Palatino Linotype')
    if event == "button109":
        print('Segoe MDL2 Assets')
        pyperclip.copy('Segoe MDL2 Assets')
    if event == "button110":
        print('Segoe Print')
        pyperclip.copy('Segoe Print')
    if event == "button111":
        print('Segoe Script')
        pyperclip.copy('Segoe Script')
    if event == "button112":
        print('Segoe UI')
        pyperclip.copy('Segoe UI')
    if event == "button113":
        print('Segoe UI Black')
        pyperclip.copy('Segoe UI Black')
    if event == "button114":
        print('Segoe UI Emoji')
        pyperclip.copy('Segoe UI Emoji')
    if event == "button115":
        print('Segoe UI Historic')
        pyperclip.copy('Segoe UI Historic')
    if event == "button116":
        print('Segoe UI Light')
        pyperclip.copy('Segoe UI Light')
    if event == "button117":
        print('Segoe UI Semibold')
        pyperclip.copy('Segoe UI Semibold')
    if event == "button118":
        print('Segoe UI Semilight')
        pyperclip.copy('Segoe UI Semilight')
    if event == "button119":
        print('Segoe UI Symbol')
        pyperclip.copy('Segoe UI Symbol')
    if event == "button120":
        print('SimSun')
        pyperclip.copy('SimSun')
    if event == "button121":
        print('@SimSun')
        pyperclip.copy('@SimSun')
    if event == "button122":
        print('NSimSun')
        pyperclip.copy('NSimSun')
    if event == "button123":
        print('@NSimSun')
        pyperclip.copy('@NSimSun')
    if event == "button124":
        print('SimSun-ExtB')
        pyperclip.copy('SimSun-ExtB')
    if event == "button125":
        print('@SimSun-ExtB')
        pyperclip.copy('@SimSun-ExtB')
    if event == "button126":
        print('Sitka Small')
        pyperclip.copy('Sitka Small')
    if event == "button127":
        print('Sitka Text')
        pyperclip.copy('Sitka Text')
    if event == "button128":
        print('Sitka Subheading')
        pyperclip.copy('Sitka Subheading')
    if event == "button129":
        print('Sitka Heading')
        pyperclip.copy('Sitka Heading')
    if event == "button130":
        print('Sitka Display')
        pyperclip.copy('Sitka Display')
    if event == "button131":
        print('Sitka Banner')
        pyperclip.copy('Sitka Banner')
    if event == "button132":
        print('Sylfaen')
        pyperclip.copy('Sylfaen')
    if event == "button133":
        print('Symbol')
        pyperclip.copy('Symbol')
    if event == "button134":
        print('Tahoma')
        pyperclip.copy('Tahoma')
    if event == "button135":
        print('Times New Roman')
        pyperclip.copy('Times New Roman')
    if event == "button136":
        print('Times New Roman Baltic')
        pyperclip.copy('Times New Roman Baltic')
    if event == "button137":
        print('Times New Roman CE')
        pyperclip.copy('Times New Roman CE')
    if event == "button138":
        print('Times New Roman CYR')
        pyperclip.copy('Times New Roman CYR')
    if event == "button139":
        print('Times New Roman Greek')
        pyperclip.copy('Times New Roman Greek')
    if event == "button140":
        print('Times New Roman TUR')
        pyperclip.copy('Times New Roman TUR')
    if event == "button141":
        print('Trebuchet MS')
        pyperclip.copy('Trebuchet MS')
    if event == "button142":
        print('Verdana')
        pyperclip.copy('Verdana')
    if event == "button143":
        print('Webdings')
        pyperclip.copy('Webdings')
    if event == "button144":
        print('Wingdings')
        pyperclip.copy('Wingdings')
    if event == "button145":
        print('游ゴシック')
        pyperclip.copy('游ゴシック')
    if event == "button146":
        print('@游ゴシック')
        pyperclip.copy('@游ゴシック')
    if event == "button147":
        print('Yu Gothic UI')
        pyperclip.copy('Yu Gothic UI')
    if event == "button148":
        print('@Yu Gothic UI')
        pyperclip.copy('@Yu Gothic UI')
    if event == "button149":
        print('Yu Gothic UI Semibold')
        pyperclip.copy('Yu Gothic UI Semibold')
    if event == "button150":
        print('@Yu Gothic UI Semibold')
        pyperclip.copy('@Yu Gothic UI Semibold')
    if event == "button151":
        print('游ゴシック Light')
        pyperclip.copy('游ゴシック Light')
    if event == "button152":
        print('@游ゴシック Light')
        pyperclip.copy('@游ゴシック Light')
    if event == "button153":
        print('Yu Gothic UI Light')
        pyperclip.copy('Yu Gothic UI Light')
    if event == "button154":
        print('@Yu Gothic UI Light')
        pyperclip.copy('@Yu Gothic UI Light')
    if event == "button155":
        print('游ゴシック Medium')
        pyperclip.copy('游ゴシック Medium')
    if event == "button156":
        print('@游ゴシック Medium')
        pyperclip.copy('@游ゴシック Medium')
    if event == "button157":
        print('Yu Gothic UI Semilight')
        pyperclip.copy('Yu Gothic UI Semilight')
    if event == "button158":
        print('@Yu Gothic UI Semilight')
        pyperclip.copy('@Yu Gothic UI Semilight')
    if event == "button159":
        print('BIZ UDゴシック')
        pyperclip.copy('BIZ UDゴシック')
    if event == "button160":
        print('@BIZ UDゴシック')
        pyperclip.copy('@BIZ UDゴシック')
    if event == "button161":
        print('BIZ UDPゴシック')
        pyperclip.copy('BIZ UDPゴシック')
    if event == "button162":
        print('@BIZ UDPゴシック')
        pyperclip.copy('@BIZ UDPゴシック')
    if event == "button163":
        print('BIZ UD明朝 Medium')
        pyperclip.copy('BIZ UD明朝 Medium')
    if event == "button164":
        print('@BIZ UD明朝 Medium')
        pyperclip.copy('@BIZ UD明朝 Medium')
    if event == "button165":
        print('BIZ UDP明朝 Medium')
        pyperclip.copy('BIZ UDP明朝 Medium')
    if event == "button166":
        print('@BIZ UDP明朝 Medium')
        pyperclip.copy('@BIZ UDP明朝 Medium')
    if event == "button167":
        print('メイリオ')
        pyperclip.copy('メイリオ')
    if event == "button168":
        print('@メイリオ')
        pyperclip.copy('@メイリオ')
    if event == "button169":
        print('Meiryo UI')
        pyperclip.copy('Meiryo UI')
    if event == "button170":
        print('@Meiryo UI')
        pyperclip.copy('@Meiryo UI')
    if event == "button171":
        print('ＭＳ 明朝')
        pyperclip.copy('ＭＳ 明朝')
    if event == "button172":
        print('@ＭＳ 明朝')
        pyperclip.copy('@ＭＳ 明朝')
    if event == "button173":
        print('ＭＳ Ｐ明朝')
        pyperclip.copy('ＭＳ Ｐ明朝')
    if event == "button174":
        print('@ＭＳ Ｐ明朝')
        pyperclip.copy('@ＭＳ Ｐ明朝')
    if event == "button175":
        print('UD デジタル 教科書体 N-B')
        pyperclip.copy('UD デジタル 教科書体 N-B')
    if event == "button176":
        print('@UD デジタル 教科書体 N-B')
        pyperclip.copy('@UD デジタル 教科書体 N-B')
    if event == "button177":
        print('UD デジタル 教科書体 NP-B')
        pyperclip.copy('UD デジタル 教科書体 NP-B')
    if event == "button178":
        print('@UD デジタル 教科書体 NP-B')
        pyperclip.copy('@UD デジタル 教科書体 NP-B')
    if event == "button179":
        print('UD デジタル 教科書体 NK-B')
        pyperclip.copy('UD デジタル 教科書体 NK-B')
    if event == "button180":
        print('@UD デジタル 教科書体 NK-B')
        pyperclip.copy('@UD デジタル 教科書体 NK-B')
    if event == "button181":
        print('UD デジタル 教科書体 N-R')
        pyperclip.copy('UD デジタル 教科書体 N-R')
    if event == "button182":
        print('@UD デジタル 教科書体 N-R')
        pyperclip.copy('@UD デジタル 教科書体 N-R')
    if event == "button183":
        print('UD デジタル 教科書体 NP-R')
        pyperclip.copy('UD デジタル 教科書体 NP-R')
    if event == "button184":
        print('@UD デジタル 教科書体 NP-R')
        pyperclip.copy('@UD デジタル 教科書体 NP-R')
    if event == "button185":
        print('UD デジタル 教科書体 NK-R')
        pyperclip.copy('UD デジタル 教科書体 NK-R')
    if event == "button186":
        print('@UD デジタル 教科書体 NK-R')
        pyperclip.copy('@UD デジタル 教科書体 NK-R')
    if event == "button187":
        print('游明朝')
        pyperclip.copy('游明朝')
    if event == "button188":
        print('@游明朝')
        pyperclip.copy('@游明朝')
    if event == "button189":
        print('游明朝 Demibold')
        pyperclip.copy('游明朝 Demibold')
    if event == "button190":
        print('@游明朝 Demibold')
        pyperclip.copy('@游明朝 Demibold')
    if event == "button191":
        print('游明朝 Light')
        pyperclip.copy('游明朝 Light')
    if event == "button192":
        print('@游明朝 Light')
        pyperclip.copy('@游明朝 Light')
    if event == "button193":
        print('HoloLens MDL2 Assets')
        pyperclip.copy('HoloLens MDL2 Assets')
    if event == "button194":
        print('HGｺﾞｼｯｸE')
        pyperclip.copy('HGｺﾞｼｯｸE')
    if event == "button195":
        print('@HGｺﾞｼｯｸE')
        pyperclip.copy('@HGｺﾞｼｯｸE')
    if event == "button196":
        print('HGPｺﾞｼｯｸE')
        pyperclip.copy('HGPｺﾞｼｯｸE')
    if event == "button197":
        print('@HGPｺﾞｼｯｸE')
        pyperclip.copy('@HGPｺﾞｼｯｸE')
    if event == "button198":
        print('HGSｺﾞｼｯｸE')
        pyperclip.copy('HGSｺﾞｼｯｸE')
    if event == "button199":
        print('@HGSｺﾞｼｯｸE')
        pyperclip.copy('@HGSｺﾞｼｯｸE')
    if event == "button200":
        print('HGｺﾞｼｯｸM')
        pyperclip.copy('HGｺﾞｼｯｸM')
    if event == "button201":
        print('@HGｺﾞｼｯｸM')
        pyperclip.copy('@HGｺﾞｼｯｸM')
    if event == "button202":
        print('HGPｺﾞｼｯｸM')
        pyperclip.copy('HGPｺﾞｼｯｸM')
    if event == "button203":
        print('@HGPｺﾞｼｯｸM')
        pyperclip.copy('@HGPｺﾞｼｯｸM')
    if event == "button204":
        print('HGSｺﾞｼｯｸM')
        pyperclip.copy('HGSｺﾞｼｯｸM')
    if event == "button205":
        print('@HGSｺﾞｼｯｸM')
        pyperclip.copy('@HGSｺﾞｼｯｸM')
    if event == "button206":
        print('HG行書体')
        pyperclip.copy('HG行書体')
    if event == "button207":
        print('@HG行書体')
        pyperclip.copy('@HG行書体')
    if event == "button208":
        print('HGP行書体')
        pyperclip.copy('HGP行書体')
    if event == "button209":
        print('@HGP行書体')
        pyperclip.copy('@HGP行書体')
    if event == "button210":
        print('HGS行書体')
        pyperclip.copy('HGS行書体')
    if event == "button211":
        print('@HGS行書体')
        pyperclip.copy('@HGS行書体')
    if event == "button212":
        print('HG教科書体')
        pyperclip.copy('HG教科書体')
    if event == "button213":
        print('@HG教科書体')
        pyperclip.copy('@HG教科書体')
    if event == "button214":
        print('HGP教科書体')
        pyperclip.copy('HGP教科書体')
    if event == "button215":
        print('@HGP教科書体')
        pyperclip.copy('@HGP教科書体')
    if event == "button216":
        print('HGS教科書体')
        pyperclip.copy('HGS教科書体')
    if event == "button217":
        print('@HGS教科書体')
        pyperclip.copy('@HGS教科書体')
    if event == "button218":
        print('HG明朝B')
        pyperclip.copy('HG明朝B')
    if event == "button219":
        print('@HG明朝B')
        pyperclip.copy('@HG明朝B')
    if event == "button220":
        print('HGP明朝B')
        pyperclip.copy('HGP明朝B')
    if event == "button221":
        print('@HGP明朝B')
        pyperclip.copy('@HGP明朝B')
    if event == "button222":
        print('HGS明朝B')
        pyperclip.copy('HGS明朝B')
    if event == "button223":
        print('@HGS明朝B')
        pyperclip.copy('@HGS明朝B')
    if event == "button224":
        print('HG明朝E')
        pyperclip.copy('HG明朝E')
    if event == "button225":
        print('@HG明朝E')
        pyperclip.copy('@HG明朝E')
    if event == "button226":
        print('HGP明朝E')
        pyperclip.copy('HGP明朝E')
    if event == "button227":
        print('@HGP明朝E')
        pyperclip.copy('@HGP明朝E')
    if event == "button228":
        print('HGS明朝E')
        pyperclip.copy('HGS明朝E')
    if event == "button229":
        print('@HGS明朝E')
        pyperclip.copy('@HGS明朝E')
    if event == "button230":
        print('HG創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('HG創英角ﾎﾟｯﾌﾟ体')
    if event == "button231":
        print('@HG創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('@HG創英角ﾎﾟｯﾌﾟ体')
    if event == "button232":
        print('HGP創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('HGP創英角ﾎﾟｯﾌﾟ体')
    if event == "button233":
        print('@HGP創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('@HGP創英角ﾎﾟｯﾌﾟ体')
    if event == "button234":
        print('HGS創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('HGS創英角ﾎﾟｯﾌﾟ体')
    if event == "button235":
        print('@HGS創英角ﾎﾟｯﾌﾟ体')
        pyperclip.copy('@HGS創英角ﾎﾟｯﾌﾟ体')
    if event == "button236":
        print('HG創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('HG創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button237":
        print('@HG創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('@HG創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button238":
        print('HGP創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('HGP創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button239":
        print('@HGP創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('@HGP創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button240":
        print('HGS創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('HGS創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button241":
        print('@HGS創英ﾌﾟﾚｾﾞﾝｽEB')
        pyperclip.copy('@HGS創英ﾌﾟﾚｾﾞﾝｽEB')
    if event == "button242":
        print('HG創英角ｺﾞｼｯｸUB')
        pyperclip.copy('HG創英角ｺﾞｼｯｸUB')
    if event == "button243":
        print('@HG創英角ｺﾞｼｯｸUB')
        pyperclip.copy('@HG創英角ｺﾞｼｯｸUB')
    if event == "button244":
        print('HGP創英角ｺﾞｼｯｸUB')
        pyperclip.copy('HGP創英角ｺﾞｼｯｸUB')
    if event == "button245":
        print('@HGP創英角ｺﾞｼｯｸUB')
        pyperclip.copy('@HGP創英角ｺﾞｼｯｸUB')
    if event == "button246":
        print('HGS創英角ｺﾞｼｯｸUB')
        pyperclip.copy('HGS創英角ｺﾞｼｯｸUB')
    if event == "button247":
        print('@HGS創英角ｺﾞｼｯｸUB')
        pyperclip.copy('@HGS創英角ｺﾞｼｯｸUB')
    if event == "button248":
        print('HG正楷書体-PRO')
        pyperclip.copy('HG正楷書体-PRO')
    if event == "button249":
        print('@HG正楷書体-PRO')
        pyperclip.copy('@HG正楷書体-PRO')
    if event == "button250":
        print('HG丸ｺﾞｼｯｸM-PRO')
        pyperclip.copy('HG丸ｺﾞｼｯｸM-PRO')
    if event == "button251":
        print('@HG丸ｺﾞｼｯｸM-PRO')
        pyperclip.copy('@HG丸ｺﾞｼｯｸM-PRO')
    if event == "button252":
        print('OCRB')
        pyperclip.copy('OCRB')
    if event == "button253":
        print('Book Antiqua')
        pyperclip.copy('Book Antiqua')
    if event == "button254":
        print('Arial Narrow')
        pyperclip.copy('Arial Narrow')
    if event == "button255":
        print('Arial Unicode MS')
        pyperclip.copy('Arial Unicode MS')
    if event == "button256":
        print('@Arial Unicode MS')
        pyperclip.copy('@Arial Unicode MS')
    if event == "button257":
        print('Bookman Old Style')
        pyperclip.copy('Bookman Old Style')
    if event == "button258":
        print('Bradley Hand ITC')
        pyperclip.copy('Bradley Hand ITC')
    if event == "button259":
        print('Bookshelf Symbol 7')
        pyperclip.copy('Bookshelf Symbol 7')
    if event == "button260":
        print('Century')
        pyperclip.copy('Century')
    if event == "button261":
        print('Freestyle Script')
        pyperclip.copy('Freestyle Script')
    if event == "button262":
        print('French Script MT')
        pyperclip.copy('French Script MT')
    if event == "button263":
        print('Garamond')
        pyperclip.copy('Garamond')
    if event == "button264":
        print('Century Gothic')
        pyperclip.copy('Century Gothic')
    if event == "button265":
        print('Kristen ITC')
        pyperclip.copy('Kristen ITC')
    if event == "button266":
        print('Juice ITC')
        pyperclip.copy('Juice ITC')
    if event == "button267":
        print('Lucida Handwriting')
        pyperclip.copy('Lucida Handwriting')
    if event == "button268":
        print('Mistral')
        pyperclip.copy('Mistral')
    if event == "button269":
        print('Monotype Corsiva')
        pyperclip.copy('Monotype Corsiva')
    if event == "button270":
        print('MT Extra')
        pyperclip.copy('MT Extra')
    if event == "button271":
        print('MS Outlook')
        pyperclip.copy('MS Outlook')
    if event == "button272":
        print('Papyrus')
        pyperclip.copy('Papyrus')
    if event == "button273":
        print('Pristina')
        pyperclip.copy('Pristina')
    if event == "button274":
        print('MS Reference Sans Serif')
        pyperclip.copy('MS Reference Sans Serif')
    if event == "button275":
        print('MS Reference Specialty')
        pyperclip.copy('MS Reference Specialty')
    if event == "button276":
        print('Tempus Sans ITC')
        pyperclip.copy('Tempus Sans ITC')
    if event == "button277":
        print('Wingdings 2')
        pyperclip.copy('Wingdings 2')
    if event == "button278":
        print('Wingdings 3')
        pyperclip.copy('Wingdings 3')
    if event == "button279":
        print('Rounded Mplus 1c Medium')
        pyperclip.copy('Rounded Mplus 1c Medium')
    if event == "button280":
        print('@Rounded Mplus 1c Medium')
        pyperclip.copy('@Rounded Mplus 1c Medium')
    if event == "button281":
        print('Rounded Mplus 1c Bold')
        pyperclip.copy('Rounded Mplus 1c Bold')
    if event == "button282":
        print('@Rounded Mplus 1c Bold')
        pyperclip.copy('@Rounded Mplus 1c Bold')