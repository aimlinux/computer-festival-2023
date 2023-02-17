import random as rand

c = list (input())

a = rand.randint(0,len(c))
#print(a)
while True:
    ca = rand.randint(12353,12527)
    if 12438 > ca or ca > 12449:
        break; 

cc = c[:a]

cc.append(chr(ca))
i = a
for i in range(len(c)-a):
    cc.append(c[i+a])
cc = ''.join(cc)
print(cc)