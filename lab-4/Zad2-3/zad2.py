import math
from matplotlib import pyplot as plt

bina = []
bn = []
def string2bits(s=''):
    for x in s:
        bina.append(bin(ord(x))[2:])
    bits = ''
    for i in range(0,len(bina)):
        bits += bina[i]
    return [int(i) for i in str(bits)]

s = "Labko"

b = string2bits(s)
print(b)

#a_string = "abcde"

#split_strings = []

#for index in range(0, len(a_string), n):
#    split_strings.append(a_string[index : index + 1])

#print(split_strings)
    

#zad 2

tc = 7
fs=8000
tb = tc / (len(b))
a1 = 1
a2 = 2
w = 2
fn = w / tb
fn1 = (w+1) / tb
fn2 = (w+2) / tb
n = round(tc*fs)
nb = round( n / len(b) )

t = []
za = []
zp = []
zf = []
index = 0
dex = 0
def z_a(d,i):
    if d == 0:
        return a1 * math.sin(2*math.pi * fn * t[i])
    else:
        return a2 * math.sin(2*math.pi * fn * t[i])


def z_p(d,i):
    if d == 0:
        return math.sin(2*math.pi * fn * t[i])
    else:
        return math.sin(2*math.pi * fn * t[i] + math.pi)


def z_f(d,i):
    if d == 0:
        return math.sin(2*math.pi * fn1 * t[i])
    else:
        return math.sin(2*math.pi * fn2 * t[i])



for i in b:
    for j in range(0,nb):
        t.append(index)
        za.append(z_a(b[i],dex))
        zp.append(z_p(b[i],dex))
        zf.append(z_f(b[i],dex))
        dex += 1
        index += 1 / fs


plt.title("ask")
plt.plot(t,za)
plt.show()

plt.title("psk")
plt.plot(t, zp)
plt.show()

plt.title("fsk")
plt.plot(t, zf)
plt.show()


