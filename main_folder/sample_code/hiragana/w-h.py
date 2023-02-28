a=[[0 for i in range(85)] for j in range(85)]#e38181-e38294 a[x][y]でx->y,x=0が最初の文字、y=0が単語の終わり
#--------各環境で相対パスを変更しよう！！--------
f=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/hiragana/hiragana.txt","r",encoding="utf-8")
word=f.readline()   #一行読み込み
while len(word)>0:
    #print(len(word))
    enc=word.encode("utf-8")
    en=enc[2]-128+(enc[1]==130)*64  #文字コードを1～92に変換
    a[0][en]=a[0][en]+1 #始まりのカウント
    for i in range(len(word)-2):
        #print(i)
        en2=enc[i*3+5]-128+(enc[i*3+4]==130)*64 #文字コードを1～92に変換    en->en2
        a[en][en2]=a[en][en2]+1 #つながりのカウント
        en=en2
    a[en][0]=a[en][0]+1 #終わりのカウント
    word=f.readline()   #一行読み込み
f.close
#print(a)

#ファイル出力
#--------各環境で相対パスを変更しよう！！--------
fout=open("hira.bin","wb")
for i in range(85):
    for j in range(85):
        fout.write(bytes([int(a[i][j]/256),a[i][j]%256]))
fout.close