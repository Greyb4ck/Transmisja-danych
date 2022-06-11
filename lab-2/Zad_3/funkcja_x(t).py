
import math
import numpy as np
import time 
import matplotlib.pyplot as plt

Tc= 2 #czas trwania sygnału 
fs = 80 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1


imag = []
real = []
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
def f(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

x=[]
y=[]


for i in range(0, N):
    Tc = i/fs

    x.append(Tc)
    y.append(f(Tc))

##################################################### 4

dft_b1 = DFT(y)


result_b1 = []



for i in range(len(y)):

    result_b1.append(math.sqrt(dft_b1[0][i]**2 + dft_b1[1][i]**2))



#plt.plot(range(len(result_b1)), result_b1)
#plt.show()
#plt.plot(range(len(result_b2)), result_b2)
#plt.show()
#plt.plot(range(len(result_b3)), result_b3)
#plt.show()


result_dok_b1 = []

for i in range(round(N/2)):
    result_dok_b1.append(10*math.log10(result_b1[i]))


freq_b1=[]

for i in range(round(N/2)):
    freq_b1.append(i*(fs/N))



plt.plot(freq_b1, result_dok_b1)
plt.show()
