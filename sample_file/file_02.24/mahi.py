import random as rnd
f=open("hira.bin","rb")
sum=[0]*85
a=[]
for i in range(85):
    aa=[]
    for j in range(85):
        b=f.read(2)
        aaa=b[0]*256+b[1]
        aa=aa+[aaa]
        sum[i]=sum[i]+aaa
    a=a+[aa]
f.close
#print(a)

c=[]
front=0
while True:
    r=rnd.randint(1,sum[front])
    count=0
    i=-1
    while count<r:
        i=i+1
        count=count+a[front][i]
    #print(i)
    if i==0:
        break
    #c=c+[i+(227*256+130)*256+160+(i>32)*192]
    c=c+[227,129+(i>63),i+128-(i>63)*64]
    front=i
#print(c)
cc=bytes(c).decode("utf-8")
print(cc)