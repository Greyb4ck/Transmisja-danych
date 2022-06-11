import numpy as np
import time 
import math
import matplotlib.pyplot as plt

#Zadanie 3 funkcja 6
Tc= 1 #czas trwania sygnału 
fs = 4000 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1


real = []
imag = []
retkom = []

def DFT(x):
    #return (  x * math.exp**(-i * ( (2*math.pi * k * n)/N  ) ) )
	n = len(x)           

	for k in range(n):
			sumreal = 0
			sumimag = 0
			for t in range(n): 
				sumreal +=  x[t]*math.cos( (2*math.pi * k * t)/n  )
				sumimag +=  x[t]*math.sin( (-2*math.pi * k * t)/n  )
			real.append(sumreal)
			imag.append(sumimag)
			retkom.append((sumreal , sumimag))
	print('dft')
	#print("Real numbers:\n",real)
	#print("Imaginery numbers:\n",imag)
	return[real , imag]


######################################### 4


def f_x(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

def f_y(x):
    return (-Tc/2) * math.sin(20*Tc**3 - 18*Tc**2)

def f_z(x):
    return math.cos(5* math.pi * Tc) * math.sin(12 * math.pi * Tc**2)

def f_v(x):
    return (Tc - 3 / 3) * math.sin((12 - Tc)* math.pi * Tc**2)


prop=[]
fun_y=[]


for i in range(0, N):
    Tc = i/fs

    if Tc >=0 and Tc<1.8:
        fun_y.append(f_y(Tc))
        prop.append(Tc)

    if Tc >=1.8 and Tc<3:
        fun_y.append(f_z(Tc))
        prop.append(Tc)

    if Tc >=3 and Tc<4.5:
        fun_y.append(f_v(Tc))
        prop.append(Tc)



plt.plot(prop, fun_y)
plt.show()
##################################################### 4


dft_fy = DFT(fun_y)

resultF_y = []



for i in range(len(fun_y)):

    resultF_y.append(math.sqrt(dft_fy[0][i]**2 + dft_fy[1][i]**2))


    



#plt.plot(range(len(result_b1)), result_b1)
#plt.show()
#plt.plot(range(len(result_b2)), result_b2)
#plt.show()
#plt.plot(range(len(result_b3)), result_b3)
#plt.show()


result_dok_Fy = []

for i in range(round(len(fun_y)/2)):
    result_dok_Fy.append(10*math.log10(resultF_y[i]))



freq_Fy=[]


for i in range(round(N/2)):
    freq_Fy.append(i*(fs/N))




plt.plot(freq_Fy, result_dok_Fy)
plt.show()



