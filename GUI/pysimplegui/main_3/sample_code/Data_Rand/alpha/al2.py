import random as rand
#--------各環境で相対パスを変更しよう！！--------
f_sub4=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/alpha/alp.bin","rb")
sum_sub4=[0]*27
a_sub4=[]
for i_sub4 in range(27):
    aa_sub4=[]
    for j_sub4 in range(27):
        b_sub4=f_sub4.read(2)
        aaa_sub4=b_sub4[0]*256+b_sub4[1]
        aa_sub4=aa_sub4+[aaa_sub4]
        sum_sub4[i_sub4]=sum_sub4[i_sub4]+aaa_sub4
    a_sub4=a_sub4+[aa_sub4]
f_sub4.close
#print(a_sub4)

c_sub4=[]
front_sub4=0
while True:
    r_sub4=rand.randint(1,sum_sub4[front_sub4])
    count_sub4=0
    i_sub4=-1
    while count_sub4<r_sub4:
        i_sub4=i_sub4+1
        count_sub4=count_sub4+a_sub4[front_sub4][i_sub4]
    #print(i_sub4)
    if i_sub4==0:
        break
    #c_sub4=c_sub4+[i_sub4+(227*256+130)*256+160+(i_sub4>32)*192]
    c_sub4=c_sub4+[i_sub4+96]
    front_sub4=i_sub4
#print(c_sub4)
cc_sub4=bytes(c_sub4).decode("utf-8")
print(cc_sub4)