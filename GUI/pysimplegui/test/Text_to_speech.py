#----日本語テキストの読み上げ----

#モジュールの追加
import pyttsx3

#音声読み上げ
engine = pyttsx3.init()
engine.say(cc)
engine.runAndWait()