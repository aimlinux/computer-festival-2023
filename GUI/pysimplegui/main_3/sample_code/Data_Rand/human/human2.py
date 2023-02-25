import random as rand
#--------各環境で相対パスを変更しよう！！--------
f_sub5=open("GUI/pysimplegui/main_3/sample_code/Data_Rand/human/human.bin","rb")
sum_sub5=[0]*85
a_sub5=[]
for i_sub5 in range(85):
    aa_sub5=[]
    for j_sub5 in range(85):
        b_sub5=f_sub5.read(2)
        aaa_sub5=b_sub5[0]*256+b_sub5[1]
        aa_sub5=aa_sub5+[aaa_sub5]
        sum_sub5[i_sub5]=sum_sub5[i_sub5]+aaa_sub5
    a_sub5=a_sub5+[aa_sub5]
f_sub5.close
#print(a_sub5)

c_sub5=[]
front_sub5=0
while True:
    r_sub5=rand.randint(1,sum_sub5[front_sub5])
    count_sub5=0
    i_sub5=-1
    while count_sub5<r_sub5:
        i_sub5=i_sub5+1
        count_sub5=count_sub5+a_sub5[front_sub5][i_sub5]
    #print(i_sub5)
    if i_sub5==0:
        break
    #c_sub5=c_sub5+[i_sub5+(227*256+130)*256+160+(i_sub5>32)*192]
    c_sub5=c_sub5+[227,129+(i_sub5>63),i_sub5+128-(i_sub5>63)*64]
    front_sub5=i_sub5
#print(c_sub5)
cc_sub5=bytes(c_sub5).decode("utf-8")
print(cc_sub5)