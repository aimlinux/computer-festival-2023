import random as rnd

f=open("text.bin","rb")
a=[]
for i in range(93):
    aa=[]
    for j in range(93):
        b=f.read(2)
        aaa=b[0]*256+b[1]
        aa=aa+[aaa]
    a=a+[aa]
f.close

c=input()
cc=[0]
enc=c.encode("utf-8")
for i in range(len(c)):
    cc=cc+[enc[i*3+2]-160+(enc[i*3+1]==131)*64]
cc=cc+[0]

sum=0
while sum==0:
    r=rnd.randint(0,len(c))
    aa=[0]*92
    sum=0
    for j in range(92):
        i=j+1
        aa[j]=a[cc[r]][i]*a[i][cc[r+1]]
        sum=sum+aa[j]

rr=rnd.randint(1,sum)
count=0
i=0
while count<rr:
    count=count+aa[i]
    i=i+1
cc=cc[:r+1]+[i]+cc[r+1:]
cc=cc[1:]

ccc=[]
for i in range(len(c)+1):
    ccc=ccc+[227,130+(cc[i]>31),cc[i]+160-(cc[i]>31)*64]
c=bytes(ccc).decode("utf-8")
print(c)