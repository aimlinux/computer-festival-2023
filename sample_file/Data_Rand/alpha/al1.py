a=[[0 for i in range(27)] for j in range(27)]#61-7a a[x][y]でx->y,x=0が最初の文字、y=0が単語の終わり
f=open("alpha.txt","r",encoding="utf-8")
word=f.readline()   #一行読み込み
while len(word)>0:
    #print(len(word))
    enc=word.encode("utf-8")
    en=enc[0]-96  #文字コードを1～92に変換
    a[0][en]=a[0][en]+1 #始まりのカウント
    for i in range(len(word)-2):
        #print(i)
        en2=enc[i+1]-96 #文字コードを1～92に変換    en->en2
        a[en][en2]=a[en][en2]+1 #つながりのカウント
        en=en2
    a[en][0]=a[en][0]+1 #終わりのカウント
    word=f.readline()   #一行読み込み
f.close
#print(a)

#ファイル出力
fout=open("alp.bin","wb")
for i in range(27):
    for j in range(27):
        fout.write(bytes([int(a[i][j]/256),a[i][j]%256]))
fout.close