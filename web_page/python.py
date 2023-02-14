import random
random.random()

c = [0] * 40
print(c)

ca = [-126, -125, -124, -123, -122,
    -121, -120, -119, -118, -117, 
    -116, -115, -114, -113, -112, 
    -111, -110, -109, -108, -107,
    -106, -105, -104, -103, -102, 
    -101, -100, -99, -98, -97, -96]

#ca[0] = -125
#ca[1] = 65

c = list(input(''))

for i in range(len(c)):
    a = random.choice(ca)
    a_int = int(a)
    print(a_int)


ca[1] = ca[1] + 
    