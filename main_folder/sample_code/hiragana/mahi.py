import random as rand
#--------各環境で相対パスを変更しよう！！--------
f_sub2=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/hiragana/hira.bin","rb")
sum_sub2=[0]*85
a_sub2=[]
for i_sub2 in range(85):
    aa_sub2=[]
    for j_sub2 in range(85):
        b_sub2=f_sub2.read(2)
        aaa_sub2=b_sub2[0]*256+b_sub2[1]
        aa_sub2=aa_sub2+[aaa_sub2]
        sum_sub2[i_sub2]=sum_sub2[i_sub2]+aaa_sub2
    a_sub2=a_sub2+[aa_sub2]
f_sub2.close
#print(a)

c_sub2=[]
front_sub2=0
while True:
    r_sub2=rand.randint(1,sum_sub2[front_sub2])
    count_sub2=0
    i_sub2=-1
    while count_sub2<r_sub2:
        i_sub2=i_sub2+1
        count_sub2=count_sub2+a_sub2[front_sub2][i_sub2]
    #print(i_sub2)
    if i_sub2==0:
        break
    #c_sub2=c_sub2+[i_sub2+(227*256+130)*256+160+(i_sub2>32)*192]
    c_sub2=c_sub2+[227,129+(i_sub2>63),i_sub2+128-(i_sub2>63)*64]
    front_sub2=i_sub2
#print(c_sub2)
cc_sub2=bytes(c_sub2).decode("utf-8")
print(cc_sub2)