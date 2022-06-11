import math
import numpy as np
import matplotlib.pyplot as plt

Tc = 1
fs = 4000
Fm = 20
Fn = 1000
kA = 0.5
Kp = 0.5
Kf = 0.5
N = Tc * fs

def m_t(t):
	return math.sin(2*math.pi * Fm * t)

def z_A(t):
	return (kA * m_t(t) + 1) * math.cos(2*math.pi * Fn * t)

def z_P(t):
	return math.cos(2*math.pi * Fn * t + Kp * m_t(t))

def z_F(t):
	return math.cos(2*math.pi * Fn * t + Kf/Fm * m_t(t))

x = []
zA = []
zP = []
zF = []

for i in range(0, N):
	x.append(i)
	zA.append(z_A(i/fs))
	zP.append(z_P(i/fs))
	zF.append(z_F(i/fs))

#plt.plot(x, zA)
#plt.show()

#plt.plot(x, zP)
#plt.show()

#plt.plot(x, zF)
#plt.show()
def zad2(funkcja):
	zA_fft = np.fft.fft(funkcja)
	freq=[]
	result = []
	for i in range(0,N):

	
		result.append(math.sqrt(zA_fft[i].real**2 + zA_fft[i].imag**2))


	#plt.plot(range(len(result)), result)
	#plt.show()


	result_dok = []
	for i in range(round(N/2)):
		result_dok.append(10*math.log10(result[i]))

	for i in range(round(N/2)):
		freq.append(i*(fs/N))


	plt.plot(freq, result_dok)
	plt.show()
	

#zad2(zA)
#zad2(zP)
#zad2(zF)





def zad3(funkcja, W):
	zA_fft = np.fft.fft(funkcja)

	result = []
	for i in range(0,N):

	
		result.append(math.sqrt(zA_fft[i].real**2 + zA_fft[i].imag**2))

	

	result_dok = []
	for i in range(round(N/2)):
		result_dok.append(10*math.log10(result[i]))

	decMax = max(result_dok)

	Itre = decMax - W

	freq=[]
	for i in range(round(N/2)):
		freq.append(i*(fs/N))

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

	#plt.plot(freq, result_dok)
	#plt.show()

zad3(zA,3)
zad3(zA,6)
zad3(zA,12)
#zad3(zP,3)
#zad3(zP,6)
#zad3(zP,12)
#zad3(zF,3)
#zad3(zF,6)
#zad3(zF,12)