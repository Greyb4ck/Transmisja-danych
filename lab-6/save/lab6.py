import math

bina = []
bn = []
def string2bits(s=''):
    for x in s:
        bina.append(bin(ord(x))[2:])
    bits = ''
    for i in range(0,len(bina)):
        bits += bina[i]
    return [int(i) for i in str(bits)]

s = "Ob"

b = string2bits(s)
print(b)


kod_H = []


for i in range(0, len(b)):

    kod_H.append(b[i])
