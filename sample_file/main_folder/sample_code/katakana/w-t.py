a=[[0 for i in range(93)] for j in range(93)]#e382a1-e383bc a[x][y]でx->y,x=0が最初の文字、y=0が単語の終わり
#--------各環境で相対パスを変更しよう！！--------
f=open("GUI\pysimplegui\main_3\sample_code\Data_Rand\katakana\word.txt","r",encoding="utf-8")
word=f.readline()   #一行読み込み
while len(word)>0:
    #print(len(word))
    enc=word.encode("utf-8")
    en=enc[2]-160+(enc[1]==131)*64  #文字コードを1～92に変換
    a[0][en]=a[0][en]+1 #始まりのカウント
    for i in range(len(word)-2):
        #print(i)
        en2=enc[i*3+5]-160+(enc[i*3+4]==131)*64 #文字コードを1～92に変換    en->en2
        a[en][en2]=a[en][en2]+1 #つながりのカウント
        en=en2
    a[en][0]=a[en][0]+1 #終わりのカウント
    word=f.readline()   #一行読み込み
f.close
#print(a)

#ファイル出力
#--------各環境で相対パスを変更しよう！！--------
fout=open("kata.bin","wb")
for i in range(93):
    for j in range(93):
        fout.write(bytes([int(a[i][j]/256),a[i][j]%256]))
fout.close