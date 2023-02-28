import random as rand
#--------各環境で相対パスを変更しよう！！--------
f_sub3=open("GUI\pysimplegui\main_3\sample_code\Data_Rand\katakana\kata.bin","rb")
sum_sub3=[0]*93
a_sub3=[]
for i_sub3 in range(93):
    aa_sub3=[]
    for j_sub3 in range(93):
        b_sub3=f_sub3.read(2)
        aaa_sub3=b_sub3[0]*256+b_sub3[1]
        aa_sub3=aa_sub3+[aaa_sub3]
        sum_sub3[i_sub3]=sum_sub3[i_sub3]+aaa_sub3
    a_sub3=a_sub3+[aa_sub3]
f_sub3.close
#print(a_sub3)

c_sub3=[]
front_sub3=0
while True:
    r_sub3=rand.randint(1,sum_sub3[front_sub3])
    count_sub3=0
    i_sub3=-1
    while count_sub3<r_sub3:
        i_sub3=i_sub3+1
        count_sub3=count_sub3+a_sub3[front_sub3][i_sub3]
    #print(i_sub3)
    if i_sub3==0:
        break
    #c_sub3=c_sub3+[i_sub3+(227*256+130)*256+160+(i_sub3>32)*192]
    c_sub3=c_sub3+[227,130+(i_sub3>31),i_sub3+160-(i_sub3>31)*64]
    front_sub3=i_sub3
#print(c_sub3)
cc_sub3=bytes(c_sub3).decode("utf-8")
print(cc_sub3)