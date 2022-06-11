import math
import numpy as np
import matplotlib.pyplot as plt

Tc = 1
fs = 5000
Fm = 90
Fn = 1300
kA = 0.9
Kp = 0.4
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
	freq=[]

zad2(zA)
zad2(zP)
zad2(zF)





def zad3(funkcja):
	zA_fft = np.fft.fft(funkcja)

	result = []
	for i in range(0,N):

	
		result.append(math.sqrt(zA_fft[i].real**2 + zA_fft[i].imag**2))



	result_dok = []
	for i in range(round(N/2)):
		result_dok.append(10*math.log10(result[i]))

	freq=[]
	for i in range(round(N/2)):
		freq.append(i*(fs/N))


	plt.plot(freq, result_dok)
	plt.show()