import random as rand


c1 = input()
c2 = input()

if len(c1)>1:
    r=int(rand.randint(4,9-(len(c1)<3))/3)#1/6で3,3/6で2,2/6で1になる、c1からとる文字数
    cf=c1[:r]
cf=c1
l=len(c2)
if l==1:
    c = cf + c2
    
r=rand.randint(0,7)#0-3なら後ろから,4-7なら前からとる
if r<4:
    f=open("hrkt.bin","rb")#つながりのファイル
    a=[]
    sum=[]
    for i in range(189):
        aa=[]
        su=0
        for j in range(189):
            b=f.read(2)
            aaa=b[0]*256+b[1]
            aa=aa+[aaa]
            su=su+aaa
        a=a+[aa]
        sum=sum+[su]
    f.close
    front=cf[-1].encode("utf-8")
    nf=front[2]-128+(front[1]-129)*64
    b=[2,3,1]#1,2,3文字になる確率の比
    abc=3-(l==2)
    aa=[0]*abc
    su=0
    for i in range(abc):
        back=c2[-i-1].encode("utf-8")
        nb=back[2]-128+(back[1]-129)*64
        aa[i]=a[nf][nb]*b[i]
        su=su+aa[i]
    if su:#su=0(つながらない)のときは前からとる
        r=rand.randint(1,su)
        i=-1
        count=0
        while count<r:
            i=i+1
            count=count+aa[i]
        c=cf+c2[-i-1:]
r=int(rand.randint(4,9-(l==2))/3)#1/6で3,3/6で2,2/6で1になる、c2からとる文字数
c=cf+c2[:r]

print(c)