import random as rand

def gose(c1,c2,mode=0):
    if mode==0:#単純連結
        c=c1+c2
        return c
    if mode==1:#同じ文字でつなげる
        count=[]
        for i in range(len(c1)-1):
            for j in range(len(c2)-1):
                if c1[i+1]==c2[j]:
                    count=count+[i+1,j]
        if len(count):
            r=rand.randint(0,len(count)-1)
            c=c1[:count[0]]+c2[count[1]:]
        else:
            c="qqqqq"#同じ文字がない場合
        return c
    if mode==2:#間に文字を挟んでつなげる
        front=c1[-1].encode("utf-8")
        back=c2[0].encode("utf-8")
        nf=front[2]-160+(front[1]==131)*64
        nb=back[2]-160+(back[1]==131)*64
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
        aa=[0]*188
        su=0
        for j in range(188):
            i=j+1
            aa[j]=a[nf][i]*a[i][nb]
            su=su+aa[j]
        count=0
        i=0
        r=rand.randint(0,5)#0のとき複数文字挟む
        if su>0 and r>0:
            r=rand.randint(1,su)
            while count<r:
                count=count+aa[i]
                i=i+1
            ccc=[227,129+int(cc[i]/64),cc[i]+128-int(cc[i]/64)*64]
            cc=bytes(ccc).decode("utf-8")
            c=c1+cc+c2
            return c
        else:
            r=rand.randint(1+a[nf][0],sum[nf])
            while count<r:
                count=count+a[nf][i]
                i=i+1
            i=i-1
            ccc=[227,129+int(cc[i]/64),cc[i]+128-int(cc[i]/64)*64]
            cc=bytes(ccc).decode("utf-8")
            c=c1+cc
            return gose(c,c2,2)#再帰
    if mode==3:#略す
        if len(c1)>1:
            r=int(rand.randint(4,9-(len(c1)<3))/3)#1/6で3,3/6で2,2/6で1になる、c1からとる文字数
            cf=c1[:r]
        else:
            cf=c1
        l=len(c2)
        if l==1:
            return cf+c2
        
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
                return c
            
        r=int(rand.randint(4,9-(l==2))/3)#1/6で3,3/6で2,2/6で1になる、c2からとる文字数
        c=cf+c2[:r]
        return c


print(gose(input(),input(),3))