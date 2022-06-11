import math
from matplotlib import pyplot as plt
import numpy as np
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
if len(b)>10:
	B = 10
else:
	B = len(b)



tb = tc / (B)
a1 = 1
a2 = 2
w = 300
fn = w / tb
fn1 = (w+1) / tb
fn2 = (w+2) / tb
n = round(tc*fs)

nb = round( n / B )

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

def zad4(funkcja):
	zA_fft = np.fft.fft(funkcja)
	freq=[]
	result = []
	for i in range(0,n):

	
		result.append(math.sqrt(zA_fft[i].real**2 + zA_fft[i].imag**2))


	#plt.plot(range(len(result)), result)
	#plt.show()


	result_dok = []
	for i in range(round(n/2)):
		result_dok.append(10*math.log10(result[i]))

	for i in range(round(n/2)):
		freq.append(i*(fs/n))


	plt.plot(freq, result_dok)
	plt.show()

def zad5_width(funkcja, W):
	zA_fft = np.fft.fft(funkcja)

	result = []
	for i in range(0,n):

	
		result.append(math.sqrt(zA_fft[i].real**2 + zA_fft[i].imag**2))

	

	result_dok = []
	for i in range(round(n/2)):
		result_dok.append(10*math.log10(result[i]))

	decMax = max(result_dok)

	Itre = decMax - W

	freq=[]
	for i in range(round(n/2)):
		freq.append(i*(fs/n))

	check = []

	for i in range(len(result_dok) - 1):
		if result_dok[i] >= Itre and result_dok[i + 1] <= Itre:
			
			check.append((freq[i]+freq[i + 1])/2)
		if result_dok[i + 1] >= Itre  and  result_dok[i] <= Itre:
			check.append((freq[i]+freq[i + 1])/2)
	fmin = min(check)
	fmax = max(check)
	width = fmax - fmin
	return print(width)

for i in b:
    for j in range(0,nb):
        t.append(index)
        za.append(z_a(b[i],dex))
        zp.append(z_p(b[i],dex))
        zf.append(z_f(b[i],dex))
        dex += 1
        index += 1 / fs





zad4(za)
zad4(zp)
zad4(zf)


#print(zad5_width(za,3))
#print(zad5_width(za,6))
#print(zad5_width(za,12))


#print(zad5_width(zp,3))
#print(zad5_width(zp,6))
#print(zad5_width(zp,12))


#print(zad5_width(zf,3))
#print(zad5_width(zf,6))
#print(zad5_width(zf,12))


#plt.title("ask")
#plt.plot(t,za)
#plt.show()

#plt.title("psk")
#plt.plot(t, zp)
#plt.show()

#plt.title("fsk")
#plt.plot(t, zf)
#plt.show()



