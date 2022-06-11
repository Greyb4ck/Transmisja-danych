import math
import numpy as np
import time 
import matplotlib.pyplot as plt

retkom = []
imag = []
real = []

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

Tc= 2 #czas trwania sygnału 
fs = 80 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1


#Zadanie 2
#Wybrana funkcja nr 2

def f_x(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

def f_y(x):
    return ( f_x(Tc) * Tc**3)/3

def f_z(x):
    return 1.92 * (math.cos(3 * math.pi * Tc/2) + math.cos(f_y(Tc)**2)/(8 * f_x(Tc) + 3) * Tc )

def f_v(x):
    return (f_y(Tc) * f_z(Tc)/ (f_x(Tc) + 2 )  * math.cos(7.2 * math.pi * Tc) + math.sin(math.pi * Tc**2))


prop=[]
fun_y=[]
fun_z=[]
fun_v=[]

for i in range(N):
    Tc = i/fs

    prop.append(Tc)
    fun_y.append(f_y(Tc))
    fun_z.append(f_z(Tc))
    fun_v.append(f_v(Tc))



#plt.plot(prop, fun_y)
#plt.show()

#plt.plot(prop, fun_z)
#plt.show()

#plt.plot(prop, fun_v)
#plt.show()

dft_y = DFT(fun_y)
#dft_z = DFT(fun_z)
#dft_v = DFT(fun_v)

##################################################### 4
result_y = []
result_z = []
result_v = []

for i in range(len(prop)):

    result_y.append(math.sqrt(dft_y[0][i]**2 + dft_y[1][i]**2))
    #result_z.append(math.sqrt(dft_z[0][i]**2 + dft_z[1][i]**2))
    #result_v.append(math.sqrt(dft_v[0][i]**2 + dft_v[1][i]**2))

#plt.plot(range(len(result_b1)), result_b1)
#plt.show()
#plt.plot(range(len(result_b2)), result_b2)
#plt.show()
#plt.plot(range(len(result_b3)), result_b3)
#plt.show()

result_dok_y = []
result_dok_z = []
result_dok_v = []
for i in range(round(N/2)):
    result_dok_y.append(10*math.log10(result_y[i]))

#for i in range(round(N/2)):
#    result_dok_z.append(10*math.log10(result_z[i]))

#for i in range(round(N/2)):
#    result_dok_v.append(10*math.log10(result_v[i]))

freq_y=[]
freq_z=[]
freq_v=[]

for i in range(round(N/2)):
    freq_y.append(i*(fs/N))

#for i in range(round(N/2)):
#    freq_z.append(i*(fs/N))


#for i in range(round(N/2)):
#    freq_v.append(i*(fs/N))

plt.plot(freq_y, result_dok_y)
plt.show()
#plt.plot(freq_z, result_dok_z)
#plt.show()
#plt.plot(freq_v, result_dok_v)
#plt.show()


